import json
import sqlite3
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parent
ASSETS_ROOT = ROOT.parent / "Assets"
DB_PATH = ASSETS_ROOT / "database_working_copy.db"
BENCHMARK_ROOT = ASSETS_ROOT / "Benchmark"
OUTPUT_PATH = ROOT / "data" / "explorer-data.json"


def relative_url(path: Path) -> str:
    parts = [quote(part) for part in path.relative_to(ROOT.parent).parts]
    return "../" + "/".join(parts)


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
        "sample_dir": relative_url(sample_dir) if sample_dir else None,
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
            "path": relative_url(entry),
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
