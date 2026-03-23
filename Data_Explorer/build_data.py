import ast
import json
import os
import re
import sqlite3
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parent
ASSETS_ROOT = ROOT.parent / "Assets"
DB_PATH = ASSETS_ROOT / "database_working_copy.db"
BENCHMARK_ROOT = ASSETS_ROOT / "Benchmark"
OUTPUT_PATH = ROOT / "data" / "explorer-data.json"
MANUAL_ACTION_IDENTITIES_PATH = ROOT / "data" / "manual-action-identities.json"
BENCHMARK_PUBLIC_BASE_URL = os.environ.get(
    "BENCHMARK_PUBLIC_BASE_URL",
    "https://pub-9c59b549722b4472aaaeb0656691069f.r2.dev",
).rstrip("/")
GITHUB_REPO_BASE_URL = os.environ.get(
    "GITHUB_REPO_BASE_URL",
    "https://github.com/Janinho10/UIBenchmark",
).rstrip("/")
GITHUB_REPO_BRANCH = os.environ.get("GITHUB_REPO_BRANCH", "main")
GENERIC_MESSAGES = {"success", "successful replay", "found download apk"}
SELECTOR_PRIORITY_KEYS = ("text", "textContains", "description", "descriptionContains")
SELECTOR_FALLBACK_KEYS = ("resourceId", "focused", "className")
SEARCH_WINDOW = 8


def benchmark_public_url(path: Path) -> str:
    parts = [quote(part) for part in path.relative_to(ASSETS_ROOT).parts]
    return f"{BENCHMARK_PUBLIC_BASE_URL}/" + "/".join(parts)


def github_repo_url(path: Path) -> str:
    relative_parts = [quote(part) for part in path.relative_to(ROOT.parent).parts]
    object_kind = "tree" if path.is_dir() else "blob"
    return f"{GITHUB_REPO_BASE_URL}/{object_kind}/{GITHUB_REPO_BRANCH}/" + "/".join(relative_parts)


def benchmark_label(path: Path) -> str:
    return path.relative_to(ROOT.parent).as_posix()


def load_manual_action_identities() -> dict[str, list[dict]]:
    if not MANUAL_ACTION_IDENTITIES_PATH.exists():
        return {}
    return json.loads(MANUAL_ACTION_IDENTITIES_PATH.read_text())


def mmss_to_seconds(value: str | None) -> float | None:
    if not value:
        return None

    parts = value.split(":")
    if not parts:
        return None

    try:
        if len(parts) == 2:
            minutes, seconds = parts
            return int(minutes) * 60 + int(seconds)
        if len(parts) == 3:
            hours, minutes, seconds = parts
            return int(hours) * 3600 + int(minutes) * 60 + int(seconds)
    except ValueError:
        return None

    return None


def to_seek_seconds(timestamp_in_frames: int | None, fps: int | None, timestamp_in_seconds: str | None) -> float | None:
    if timestamp_in_frames is not None and fps:
        return round(timestamp_in_frames / fps, 3)
    return mmss_to_seconds(timestamp_in_seconds)


def load_sample_dirs() -> dict[str, Path]:
    sample_dirs = {}
    for app_dir in BENCHMARK_ROOT.iterdir():
        if not app_dir.is_dir():
            continue
        for sample_dir in app_dir.iterdir():
            if sample_dir.is_dir() and "#" in sample_dir.name:
                sample_dirs[sample_dir.name] = sample_dir
    return sample_dirs


def describe_files(sample_dir: Path | None) -> dict:
    files = {
        "sample_dir": (
            {
                "label": benchmark_label(sample_dir),
                "path": github_repo_url(sample_dir),
                "type": "directory",
            }
            if sample_dir
            else None
        ),
        "video": None,
        "apk": None,
        "context": None,
        "script": None,
        "extras": [],
    }

    if sample_dir is None:
        return files

    for entry in sorted(sample_dir.iterdir(), key=lambda item: item.name.lower()):
        if entry.name == ".DS_Store":
            continue

        item = {
            "label": entry.name,
            "path": benchmark_public_url(entry),
            "github_path": github_repo_url(entry),
            "type": "directory" if entry.is_dir() else "file",
        }

        if entry.is_file() and entry.name.startswith("video-") and entry.suffix.lower() == ".mp4":
            files["video"] = item
        elif entry.is_file() and entry.suffix.lower() == ".apk" and files["apk"] is None:
            files["apk"] = item
        elif entry.is_file() and entry.name.startswith("context-") and entry.suffix.lower() == ".py":
            files["context"] = item
        elif entry.is_file() and entry.name.startswith("script-") and entry.suffix.lower() == ".py":
            files["script"] = item
        else:
            files["extras"].append(item)

    return files


def normalize_whitespace(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def humanize_identifier(value: str) -> str:
    cleaned = value.split(":id/")[-1].split("/")[-1]
    cleaned = cleaned.replace("_", " ").replace("-", " ")
    cleaned = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", cleaned)
    return normalize_whitespace(cleaned).title()


def humanize_class_name(value: str) -> str:
    return normalize_whitespace(value.split(".")[-1].replace("_", " "))


def literal_value(node: ast.AST, source: str):
    if isinstance(node, ast.Constant):
        return node.value
    segment = ast.get_source_segment(source, node)
    if segment:
        return segment.strip()
    return ast.unparse(node).strip()


def call_keywords(call_node: ast.Call, source: str) -> dict[str, str]:
    values = {}
    for keyword in call_node.keywords:
        if keyword.arg is None:
            continue
        raw_value = literal_value(keyword.value, source)
        values[keyword.arg] = str(raw_value)
    return values


def collect_chain(node: ast.AST) -> list[dict]:
    segments = []

    while True:
        if isinstance(node, ast.Call):
            func = node.func
            if isinstance(func, ast.Attribute):
                segments.append({"type": "call", "name": func.attr, "node": node})
                node = func.value
                continue
            if isinstance(func, ast.Name):
                segments.append({"type": "call", "name": func.id, "node": node})
            break

        if isinstance(node, ast.Attribute):
            segments.append({"type": "attr", "name": node.attr, "node": node})
            node = node.value
            continue

        if isinstance(node, ast.Subscript):
            segments.append({"type": "subscript", "node": node})
            node = node.value
            continue

        if isinstance(node, ast.Name):
            segments.append({"type": "name", "name": node.id, "node": node})
            break

        break

    return list(reversed(segments))


def selector_label_from_keywords(keywords: dict[str, str]) -> str | None:
    for key in SELECTOR_PRIORITY_KEYS:
        value = keywords.get(key)
        if value:
            return value

    resource_id = keywords.get("resourceId")
    if resource_id:
        return humanize_identifier(resource_id)

    if keywords.get("focused", "").lower() == "true":
        return "Focused field"

    class_name = keywords.get("className")
    if class_name:
        label = humanize_class_name(class_name)
        index = keywords.get("index")
        if index is not None:
            label = f"{label} {index}"
        return label

    return None


def compose_selector_identity(labels: list[str]) -> str | None:
    cleaned = []
    seen = set()
    for label in labels:
        normalized = normalize_whitespace(label).strip("\"'")
        if not normalized:
            continue
        lowered = normalized.lower()
        if lowered in seen:
            continue
        seen.add(lowered)
        cleaned.append(normalized)

    if not cleaned:
        return None
    if len(cleaned) == 1:
        return cleaned[0]
    return " -> ".join(cleaned[:2])


def simplify_message(message: str | None) -> str | None:
    if not message:
        return None

    cleaned = normalize_whitespace(message)
    cleaned = re.sub(r"^(success|successful replay)\s*:\s*", "", cleaned, flags=re.IGNORECASE)
    cleaned = cleaned.strip("\"' ")

    if cleaned.lower() in GENERIC_MESSAGES:
        return None

    patterns = (
        r"^(clicked on|clicked|click on|click)\s+",
        r"^(pressed|press)\s+",
        r"^(opened|open)\s+",
        r"^(set text to)\s+",
        r"^(input|enter)\s+",
        r"^(turned on|turn on|turn off|turned off)\s+",
        r"^(long click(?:ed)?|long clicked)\s+",
        r"^(scrolled to|scroll to)\s+",
        r"^(scrolled|scroll)\s+",
        r"^(swiped|swipe)\s+",
        r"^(choose|chose)\s+",
    )

    for pattern in patterns:
        next_value = re.sub(pattern, "", cleaned, flags=re.IGNORECASE)
        if next_value != cleaned:
            cleaned = next_value
            break

    cleaned = re.sub(r"^(on|the)\s+", "", cleaned, flags=re.IGNORECASE)
    cleaned = cleaned.strip("\"' ")
    return cleaned or None


def extract_print_message(node: ast.AST, source: str) -> str | None:
    if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
        call = node.value
        if isinstance(call.func, ast.Name) and call.func.id == "print" and call.args:
            message = literal_value(call.args[0], source)
            return str(message)

    if isinstance(node, ast.If):
        for child in node.body:
            message = extract_print_message(child, source)
            if message:
                return message

    return None


def extract_alias_names(node: ast.AST) -> list[str]:
    if isinstance(node, ast.Name):
        return [node.id]
    if isinstance(node, ast.Tuple):
        names = []
        for element in node.elts:
            names.extend(extract_alias_names(element))
        return names
    return []


def alias_identity_from_args(args: list[ast.AST], keywords: list[ast.keyword], aliases: dict[str, str]) -> str | None:
    labels = []

    def collect_from_node(node: ast.AST) -> None:
        if isinstance(node, ast.Name) and node.id in aliases:
            labels.append(aliases[node.id])
        elif isinstance(node, ast.Tuple):
            for element in node.elts:
                collect_from_node(element)

    for argument in args:
        collect_from_node(argument)

    for keyword in keywords:
        if keyword.arg in {"x", "y", "fx", "fy", "tx", "ty"}:
            collect_from_node(keyword.value)

    return compose_selector_identity(labels)


def extract_selector_labels(chain: list[dict], source: str) -> list[str]:
    labels = []
    for segment in chain:
        if segment["type"] != "call":
            continue

        node = segment["node"]
        if not isinstance(node, ast.Call):
            continue

        if segment["name"] in {"d", "child", "right"}:
            label = selector_label_from_keywords(call_keywords(node, source))
            if label:
                labels.append(label)
        elif segment["name"] == "xpath" and node.args:
            labels.append("XPath target")

    return labels


def classify_script_action(action: dict) -> str:
    return action["kind"]


def default_identity_for_action(kind: str, direction: str | None) -> str:
    if kind == "tap":
        return "Tap target"
    if kind == "long_tap":
        return "Long press target"
    if kind == "double_tap":
        return "Double tap target"
    if kind == "typing":
        return "Text field"
    if kind == "back":
        return "Back"
    if kind == "home":
        return "Home"
    if kind == "overview":
        return "Overview"
    if kind == "rotation":
        return "Screen rotation"
    if kind == "drag":
        return "Drag target"
    if kind == "drawing":
        return "Gesture path"
    if kind == "open_notification":
        return "Notification shade"
    if kind == "open_quick_settings":
        return "Quick settings"
    if kind in {"scroll", "swipe"} and direction:
        return f"{kind.title()} {direction}"
    if kind == "scroll":
        return "Scroll"
    if kind == "swipe":
        return "Swipe"
    if kind == "paste":
        return "Paste"
    if kind == "enter":
        return "Enter"
    return kind.replace("_", " ").title()


def action_from_call(call: ast.Call, source: str, aliases: dict[str, str], message: str | None) -> dict | None:
    chain = collect_chain(call)
    call_segments = [segment for segment in chain if segment["type"] == "call"]
    if not call_segments:
        return None

    final_segment = call_segments[-1]
    method = final_segment["name"]
    selector_identity = compose_selector_identity(extract_selector_labels(chain, source))
    selector_identity = selector_identity or alias_identity_from_args(call.args, call.keywords, aliases)
    message_identity = simplify_message(message)
    direction = None
    kind = None

    if method == "click":
        kind = "tap"
    elif method == "long_click":
        kind = "long_tap"
    elif method == "double_click":
        kind = "double_tap"
    elif method == "set_text":
        kind = "typing"
    elif method == "drag_to":
        kind = "drag"
    elif method == "gesture":
        kind = "drawing"
    elif method == "press":
        pressed = str(literal_value(call.args[0], source)).lower() if call.args else ""
        if pressed == "back":
            kind = "back"
        elif pressed == "home":
            kind = "home"
        elif pressed == "recent":
            kind = "overview"
        elif pressed == "enter":
            kind = "enter"
        else:
            kind = "press"
        direction = pressed
    elif method == "open_notification":
        kind = "open_notification"
    elif method == "open_quick_settings":
        kind = "open_quick_settings"
    elif method in {"swipe", "swipe_ext"}:
        kind = "swipe"
        if call.args and isinstance(call.args[0], ast.Constant) and isinstance(call.args[0].value, str):
            direction = str(call.args[0].value)
        else:
            keywords = call_keywords(call, source)
            direction = keywords.get("direction")
    elif method in {"to", "toEnd", "toBeginning", "forward", "backward"} and any(
        segment["name"] == "scroll" for segment in chain if segment["type"] in {"call", "attr"}
    ):
        kind = "scroll"
        keywords = call_keywords(call, source)
        direction = keywords.get("direction")
        if method == "to" and call.keywords:
            for keyword in call.keywords:
                if keyword.arg in {"text", "textContains", "description", "descriptionContains"}:
                    selector_identity = str(literal_value(keyword.value, source))
                    break
        elif method == "toEnd":
            direction = "to end"
        elif method == "toBeginning":
            direction = "to beginning"
        else:
            axis = None
            for segment in chain:
                if segment["type"] == "attr" and segment["name"] in {"horiz", "vert"}:
                    axis = segment["name"]
                    break
            base_direction = "forward" if method == "forward" else "backward"
            if axis == "horiz":
                direction = f"horizontal {base_direction}"
            elif axis == "vert":
                direction = f"vertical {base_direction}"
            else:
                direction = direction or base_direction

    if kind is None:
        return None

    identity = selector_identity or message_identity or default_identity_for_action(kind, direction)
    if kind == "scroll" and selector_identity and method == "to":
        identity = f"Scroll to {selector_identity}"
    elif kind in {"scroll", "swipe"} and not selector_identity and message_identity:
        identity = message_identity
        if message_identity.lower() in {"up", "down", "left", "right", "forward", "backward", "beginning", "end"}:
            identity = f"{kind.title()} {message_identity}"

    return {
        "kind": kind,
        "identity": identity,
        "line": getattr(call, "lineno", None),
        "message": message_identity,
        "direction": direction,
    }


def register_selector_alias(statement: ast.AST, source: str, aliases: dict[str, str]) -> None:
    if not isinstance(statement, ast.Assign):
        return
    if not isinstance(statement.value, ast.Call):
        return

    chain = collect_chain(statement.value)
    if not chain or chain[-1]["type"] != "call" or chain[-1]["name"] != "center":
        return

    names = []
    for target in statement.targets:
        names.extend(extract_alias_names(target))

    selector_identity = compose_selector_identity(extract_selector_labels(chain[:-1], source))
    if not selector_identity or not names:
        return

    for name in names:
        aliases[name] = selector_identity


def is_main_guard(test: ast.AST, source: str) -> bool:
    segment = ast.get_source_segment(source, test) or ""
    compact = segment.replace(" ", "")
    return compact in {'__name__=="__main__"', "__name__=='__main__'"}


def collect_script_actions(script_path: Path | None) -> list[dict]:
    if script_path is None or not script_path.exists():
        return []

    source = script_path.read_text(errors="replace")
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return []

    aliases: dict[str, str] = {}
    actions: list[dict] = []

    def walk_block(statements: list[ast.stmt]) -> None:
        for index, statement in enumerate(statements):
            register_selector_alias(statement, source, aliases)
            next_statement = statements[index + 1] if index + 1 < len(statements) else None
            message = extract_print_message(next_statement, source) if next_statement is not None else None

            if isinstance(statement, (ast.Assign, ast.Expr)) and isinstance(statement.value, ast.Call):
                action = action_from_call(statement.value, source, aliases, message)
                if action:
                    actions.append(action)

            if isinstance(statement, ast.If):
                if is_main_guard(statement.test, source):
                    walk_block(statement.body)
                else:
                    walk_block(statement.body)
                    walk_block(statement.orelse)
            elif isinstance(statement, (ast.For, ast.While)):
                walk_block(statement.body)
                walk_block(statement.orelse)
            elif isinstance(statement, (ast.FunctionDef, ast.AsyncFunctionDef)):
                walk_block(statement.body)
            elif isinstance(statement, ast.Try):
                walk_block(statement.body)
                walk_block(statement.orelse)
                walk_block(statement.finalbody)
                for handler in statement.handlers:
                    walk_block(handler.body)

    walk_block(tree.body)
    return actions


def classify_event(event: dict) -> str:
    if event["kind"] == "system_action":
        mapping = {
            "BACK": "back",
            "HOME": "home",
            "OVERVIEW": "overview",
            "SCREEN ROTATION": "rotation",
            "TURN ON PHONE": "power",
        }
        return mapping.get(event["label"], "system_action")

    label = event["label"]
    detail = (event.get("detail") or "").upper()

    if label == "TAP":
        return "tap"
    if label == "LONG TAP":
        return "long_tap"
    if label == "DOUBLE TAP":
        return "double_tap"
    if label == "MULTIFINGER TAP":
        return "tap"
    if label == "TYPING":
        return "typing"
    if label == "PASTE":
        return "paste"
    if label == "GO BACK":
        return "back"
    if label == "HOLD TAP AND DRAG":
        return "drag"
    if label in {"DRAWING", "DRAW CIRCLE"}:
        return "drawing"
    if label in {"SCROLL", "SWIPE"}:
        if "LEFT" in detail or "RIGHT" in detail:
            return "swipe"
        return "scroll"
    return "gesture"


def compatible_event_action(event_kind: str, action: dict) -> bool:
    action_kind = classify_script_action(action)
    compatibility = {
        "tap": {"tap", "double_tap"},
        "long_tap": {"long_tap"},
        "double_tap": {"double_tap", "tap"},
        "typing": {"typing", "enter", "paste"},
        "paste": {"paste", "tap", "typing"},
        "scroll": {"scroll", "swipe", "open_notification", "open_quick_settings"},
        "swipe": {"swipe", "scroll", "drag"},
        "drag": {"drag", "swipe"},
        "drawing": {"drawing", "drag"},
        "back": {"back", "swipe"},
        "home": {"home"},
        "overview": {"overview"},
        "rotation": {"rotation"},
        "power": {"power"},
    }
    if action_kind not in compatibility.get(event_kind, {event_kind}):
        return False

    if event_kind == "back" and action_kind == "swipe":
        hint = " ".join(filter(None, [action.get("identity"), action.get("message"), action.get("direction")])).lower()
        return "back" in hint

    return True


def align_action_identities(timeline: list[dict], script_actions: list[dict]) -> None:
    action_index = 0

    for event in timeline:
        if event["kind"] == "artifact":
            continue

        event_kind = classify_event(event)
        matched_index = None
        upper_bound = min(len(script_actions), action_index + SEARCH_WINDOW)

        for candidate_index in range(action_index, upper_bound):
            if compatible_event_action(event_kind, script_actions[candidate_index]):
                matched_index = candidate_index
                break

        if matched_index is None:
            continue

        matched_action = script_actions[matched_index]
        event["action_identity"] = matched_action["identity"]
        action_index = matched_index + 1

        if (
            event_kind == "typing"
            and action_index < len(script_actions)
            and classify_script_action(script_actions[action_index]) == "enter"
        ):
            action_index += 1

        if (
            event_kind == "double_tap"
            and action_index < len(script_actions)
            and classify_script_action(script_actions[action_index]) in {"tap", "double_tap"}
        ):
            action_index += 1


def apply_manual_action_identities(recording_name: str, timeline: list[dict], manual_identities: dict[str, list[dict]]) -> None:
    mapping = manual_identities.get(recording_name, [])
    if not mapping:
        return

    interactive_events = [event for event in timeline if event["kind"] != "artifact"]
    for entry in mapping:
        index = entry.get("index")
        identity = entry.get("identity")
        if not isinstance(index, int):
            continue
        if index < 0 or index >= len(interactive_events):
            continue
        if not identity:
            continue
        interactive_events[index]["action_identity"] = identity


def timeline_label(kind: str, name: str, parameter: str | None) -> tuple[str, str]:
    if kind == "gesture":
        label = name
        detail = f"Gesture"
    elif kind == "system_action":
        label = name
        detail = "System action"
    else:
        label = name
        detail = "Artifact"

    if parameter:
        detail = f"{detail}: {parameter}"
    return label, detail


def main() -> None:
    sample_dirs = load_sample_dirs()
    manual_action_identities = load_manual_action_identities()
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    recordings = [dict(row) for row in cur.execute("SELECT * FROM Recordings ORDER BY id")]

    languages_by_id = defaultdict(list)
    for row in cur.execute(
        """
        SELECT rl.recording_id, l.language_name
        FROM Recordings_Languages rl
        JOIN Languages l ON l.id = rl.language_id
        ORDER BY rl.recording_id, l.language_name
        """
    ):
        languages_by_id[row["recording_id"]].append(row["language_name"])

    categories_by_id = defaultdict(list)
    for row in cur.execute(
        """
        SELECT rc.recording_id, c.category_name
        FROM Recordings_Categories rc
        JOIN Categories c ON c.id = rc.category_id
        ORDER BY rc.recording_id, c.category_name
        """
    ):
        categories_by_id[row["recording_id"]].append(row["category_name"])

    gestures_by_id = defaultdict(list)
    for row in cur.execute(
        """
        SELECT rg.recording_id, g.gesture, rg.duration_in_frames, rg.timestamp_in_frames,
               rg.gesture_parameters, rg.timestamp_in_seconds, rg.duration_in_seconds
        FROM Recordings_Gestures rg
        JOIN Gestures g ON g.id = rg.gesture_id
        ORDER BY rg.recording_id, rg.timestamp_in_frames, rg.id
        """
    ):
        event = dict(row)
        event["kind"] = "gesture"
        gestures_by_id[row["recording_id"]].append(event)

    system_actions_by_id = defaultdict(list)
    for row in cur.execute(
        """
        SELECT rsa.recording_id, sa.system_action, rsa.duration_in_frames, rsa.timestamp_in_frames,
               rsa.action_parameters, rsa.timestamp_in_seconds, rsa.duration_in_seconds
        FROM Recordings_System_Actions rsa
        JOIN System_Actions sa ON sa.id = rsa.action_id
        ORDER BY rsa.recording_id, rsa.timestamp_in_frames, rsa.id
        """
    ):
        event = dict(row)
        event["kind"] = "system_action"
        system_actions_by_id[row["recording_id"]].append(event)

    artifacts_by_id = defaultdict(list)
    for row in cur.execute(
        """
        SELECT ra.recording_id, a.artifact, ra.duration_in_frames, ra.timestamp_in_frames,
               ra.parameters, ra.timestamp_in_seconds, ra.duration_in_seconds
        FROM Recordings_Artifacts ra
        JOIN Artifacts a ON a.id = ra.artifact_id
        ORDER BY ra.recording_id, ra.timestamp_in_frames, ra.id
        """
    ):
        event = dict(row)
        event["kind"] = "artifact"
        artifacts_by_id[row["recording_id"]].append(event)

    explorer_recordings = []
    source_counter = Counter()
    class_counter = Counter()
    category_counter = Counter()
    app_counter = Counter()
    total_gesture_events = 0
    total_system_action_events = 0
    total_artifact_events = 0

    for row in recordings:
        recording_id = row["id"]
        categories = categories_by_id[recording_id]
        languages = languages_by_id[recording_id]
        sample_dir = sample_dirs.get(row["Recording"])
        files = describe_files(sample_dir)

        timeline = []

        for gesture in gestures_by_id[recording_id]:
            label, detail = timeline_label("gesture", gesture["gesture"], gesture["gesture_parameters"])
            timeline.append(
                {
                    "kind": "gesture",
                    "label": label,
                    "detail": detail,
                    "timestamp_in_frames": gesture["timestamp_in_frames"],
                    "timestamp_in_seconds": gesture["timestamp_in_seconds"],
                    "seek_seconds": to_seek_seconds(
                        gesture["timestamp_in_frames"], row["fps"], gesture["timestamp_in_seconds"]
                    ),
                    "duration_in_frames": gesture["duration_in_frames"],
                    "duration_in_seconds": gesture["duration_in_seconds"],
                }
            )

        for action in system_actions_by_id[recording_id]:
            label, detail = timeline_label("system_action", action["system_action"], action["action_parameters"])
            timeline.append(
                {
                    "kind": "system_action",
                    "label": label,
                    "detail": detail,
                    "timestamp_in_frames": action["timestamp_in_frames"],
                    "timestamp_in_seconds": action["timestamp_in_seconds"],
                    "seek_seconds": to_seek_seconds(
                        action["timestamp_in_frames"], row["fps"], action["timestamp_in_seconds"]
                    ),
                    "duration_in_frames": action["duration_in_frames"],
                    "duration_in_seconds": action["duration_in_seconds"],
                }
            )

        for artifact in artifacts_by_id[recording_id]:
            label, detail = timeline_label("artifact", artifact["artifact"], artifact["parameters"])
            timeline.append(
                {
                    "kind": "artifact",
                    "label": label,
                    "detail": detail,
                    "timestamp_in_frames": artifact["timestamp_in_frames"],
                    "timestamp_in_seconds": artifact["timestamp_in_seconds"],
                    "seek_seconds": to_seek_seconds(
                        artifact["timestamp_in_frames"], row["fps"], artifact["timestamp_in_seconds"]
                    ),
                    "duration_in_frames": artifact["duration_in_frames"],
                    "duration_in_seconds": artifact["duration_in_seconds"],
                }
            )

        timeline.sort(
            key=lambda item: (
                item["timestamp_in_frames"] if item["timestamp_in_frames"] is not None else -1,
                {"artifact": 0, "system_action": 1, "gesture": 2}[item["kind"]],
                item["label"],
            )
        )
        apply_manual_action_identities(row["Recording"], timeline, manual_action_identities)

        explorer_recordings.append(
            {
                "id": recording_id,
                "recording": row["Recording"],
                "app_name": row["app_name"],
                "categories": categories,
                "app_version": row["app_version"],
                "class": row["class"],
                "source_platform": row["source_platform"],
                "upload_date": row["upload_date"],
                "duration": row["duration"],
                "resolution": {
                    "width": row["width"],
                    "height": row["height"],
                    "label": f'{row["width"]}x{row["height"]}',
                },
                "fps": row["fps"],
                "recording_device_brand": row["recording_device_brand"],
                "reproducible_device_OS_version": row["reproducible_device_OS_version"],
                "languages": languages,
                "gesture_count": len(gestures_by_id[recording_id]),
                "system_action_count": len(system_actions_by_id[recording_id]),
                "artifact_count": len(artifacts_by_id[recording_id]),
                "files": files,
                "timeline": timeline,
            }
        )

        source_counter[row["source_platform"]] += 1
        class_counter[row["class"]] += 1
        app_counter[row["app_name"]] += 1
        total_gesture_events += len(gestures_by_id[recording_id])
        total_system_action_events += len(system_actions_by_id[recording_id])
        total_artifact_events += len(artifacts_by_id[recording_id])
        for category in categories:
            category_counter[category] += 1

    payload = {
        "summary": {
            "total_recordings": len(explorer_recordings),
            "unique_apps": len(app_counter),
            "unique_sources": len(source_counter),
            "total_gesture_events": total_gesture_events,
            "total_system_action_events": total_system_action_events,
            "total_artifact_events": total_artifact_events,
        },
        "filters": {
            "apps": sorted(app_counter),
            "categories": sorted(category_counter),
            "sources": sorted(source_counter),
            "classes": sorted(class_counter),
        },
        "recordings": explorer_recordings,
    }

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(payload, indent=2))
    conn.close()
    print(f"Wrote {OUTPUT_PATH}")
    print(f"Recordings exported: {len(explorer_recordings)}")


if __name__ == "__main__":
    main()
