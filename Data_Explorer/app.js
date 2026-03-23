const state = {
  data: null,
  filters: {
    search: "",
    app: "",
    category: "",
    source: "",
    recordingClass: "",
    timelineKind: "all",
  },
  filtered: [],
  selectedId: null,
  pendingSeekSeconds: null,
  pendingAutoplayAfterSeek: false,
};

const elements = {
  summaryCards: document.querySelector("#summary-cards"),
  searchInput: document.querySelector("#search-input"),
  appFilter: document.querySelector("#app-filter"),
  recordingFilter: document.querySelector("#recording-filter"),
  categoryFilter: document.querySelector("#category-filter"),
  sourceFilter: document.querySelector("#source-filter"),
  classFilter: document.querySelector("#class-filter"),
  resetFilters: document.querySelector("#reset-filters"),
  resultCount: document.querySelector("#result-count"),
  resultHint: document.querySelector("#result-hint"),
  detailView: document.querySelector("#detail-view"),
  emptyState: document.querySelector("#empty-state"),
  detailApp: document.querySelector("#detail-app"),
  detailRecording: document.querySelector("#detail-recording"),
  detailSubtitle: document.querySelector("#detail-subtitle"),
  detailBadges: document.querySelector("#detail-badges"),
  recordingVideo: document.querySelector("#recording-video"),
  detailVideoCaption: document.querySelector("#detail-video-caption"),
  primaryFileLinks: document.querySelector("#primary-file-links"),
  metadataGrid: document.querySelector("#metadata-grid"),
  timelineToggles: document.querySelector("#timeline-toggles"),
  timelineList: document.querySelector("#timeline-list"),
  fileGroups: document.querySelector("#file-groups"),
};

const TIMELINE_KINDS = [
  { id: "all", label: "All events" },
  { id: "gesture", label: "Gestures" },
  { id: "system_action", label: "System actions" },
  { id: "artifact", label: "Artifacts" },
];
const ASSET_VERSION = window.EXPLORER_ASSET_VERSION || "dev";

loadExplorer();

async function loadExplorer() {
  try {
    const response = await fetch(`./data/explorer-data.json?v=${encodeURIComponent(ASSET_VERSION)}`, {
      cache: "no-store",
    });
    if (!response.ok) {
      throw new Error(`Failed to load explorer data: ${response.status}`);
    }

    state.data = await response.json();
    bindControls();
    renderSummaryCards();
    populateFilters();
    applyFilters();
  } catch (error) {
    showFatalError(error);
  }
}

function bindControls() {
  elements.searchInput.addEventListener("input", (event) => {
    state.filters.search = event.target.value.trim().toLowerCase();
    applyFilters();
  });

  elements.appFilter.addEventListener("change", (event) => {
    state.filters.app = event.target.value;
    applyFilters();
  });

  elements.categoryFilter.addEventListener("change", (event) => {
    state.filters.category = event.target.value;
    applyFilters();
  });

  elements.recordingFilter.addEventListener("change", (event) => {
    state.selectedId = event.target.value || null;
    if (state.selectedId) {
      history.replaceState(null, "", `#${encodeURIComponent(state.selectedId)}`);
    }
    renderSelection();
  });

  elements.sourceFilter.addEventListener("change", (event) => {
    state.filters.source = event.target.value;
    applyFilters();
  });

  elements.classFilter.addEventListener("change", (event) => {
    state.filters.recordingClass = event.target.value;
    applyFilters();
  });

  elements.resetFilters.addEventListener("click", () => {
    state.filters = {
      search: "",
      app: "",
      category: "",
      source: "",
      recordingClass: "",
      timelineKind: "all",
    };
    elements.searchInput.value = "";
    elements.appFilter.value = "";
    elements.recordingFilter.value = "";
    elements.categoryFilter.value = "";
    elements.sourceFilter.value = "";
    elements.classFilter.value = "";
    applyFilters();
  });

  window.addEventListener("hashchange", () => {
    const nextId = decodeURIComponent(window.location.hash.replace(/^#/, ""));
    if (!nextId) {
      return;
    }
    state.selectedId = nextId;
    renderRecordingFilter();
    renderSelection();
  });
}

function showFatalError(error) {
  elements.emptyState.hidden = false;
  elements.detailView.hidden = true;
  elements.emptyState.innerHTML = `
    <h2>Explorer data could not be loaded.</h2>
    <p>${escapeHtml(error.message)}</p>
  `;
}

function renderSummaryCards() {
  const stats = state.data.summary;
  const cards = [
    ["Recordings", stats.total_recordings],
    ["Apps", stats.unique_apps],
    ["Gestures", stats.total_gesture_events],
    ["System actions", stats.total_system_action_events],
    ["Artifacts", stats.total_artifact_events],
    ["Sources", stats.unique_sources],
  ];

  elements.summaryCards.innerHTML = cards
    .map(
      ([label, value]) => `
        <article class="stat-card">
          <strong>${escapeHtml(String(value))}</strong>
          <span>${escapeHtml(label)}</span>
        </article>
      `
    )
    .join("");
}

function populateFilters() {
  fillSelect(elements.appFilter, state.data.filters.apps, "All apps");
  fillSelect(elements.categoryFilter, state.data.filters.categories, "All categories");
  fillSelect(elements.sourceFilter, state.data.filters.sources, "All sources");
  fillSelect(elements.classFilter, state.data.filters.classes, "All classes");
}

function fillSelect(select, values, defaultLabel) {
  const options = [`<option value="">${escapeHtml(defaultLabel)}</option>`]
    .concat(values.map((value) => `<option value="${escapeHtml(value)}">${escapeHtml(value)}</option>`));
  select.innerHTML = options.join("");
}

function applyFilters() {
  const filters = state.filters;
  state.filtered = state.data.recordings.filter((recording) => {
    const haystack = [
      recording.recording,
      recording.app_name,
      recording.categories.join(" "),
      recording.class,
      recording.source_platform,
      recording.languages.join(" "),
    ]
      .join(" ")
      .toLowerCase();

    return (
      (!filters.search || haystack.includes(filters.search)) &&
      (!filters.app || recording.app_name === filters.app) &&
      (!filters.category || recording.categories.includes(filters.category)) &&
      (!filters.source || recording.source_platform === filters.source) &&
      (!filters.recordingClass || recording.class === filters.recordingClass)
    );
  });

  state.filtered.sort((left, right) => right.id - left.id);

  syncSelection();
  renderRecordingFilter();
  renderSelection();
}

function syncSelection() {
  const hashId = decodeURIComponent(window.location.hash.replace(/^#/, ""));
  const validIds = new Set(state.filtered.map((item) => item.recording));
  if (hashId && validIds.has(hashId)) {
    state.selectedId = hashId;
    return;
  }

  if (state.selectedId && validIds.has(state.selectedId)) {
    return;
  }

  state.selectedId = state.filtered[0]?.recording ?? null;
  if (state.selectedId) {
    history.replaceState(null, "", `#${encodeURIComponent(state.selectedId)}`);
  } else {
    history.replaceState(null, "", window.location.pathname + window.location.search);
  }
}

function renderRecordingFilter() {
  const filtered = state.filtered;
  elements.resultCount.textContent = `${filtered.length} recording${filtered.length === 1 ? "" : "s"}`;
  elements.resultHint.textContent =
    filtered.length > 0
      ? "Choose a recording from the dropdown to inspect it."
      : "No recordings match the current filters.";

  if (filtered.length === 0) {
    elements.recordingFilter.innerHTML = `<option value="">No recordings available</option>`;
    return;
  }

  const grouped = new Map();
  for (const recording of filtered) {
    const current = grouped.get(recording.app_name) ?? [];
    current.push(recording);
    grouped.set(recording.app_name, current);
  }

  const optionGroups = Array.from(grouped.entries())
    .sort((left, right) => left[0].localeCompare(right[0]))
    .map(([appName, recordings]) => {
      const options = recordings
        .map(
          (recording) => `
            <option value="${escapeHtml(recording.recording)}" ${
              recording.recording === state.selectedId ? "selected" : ""
            }>
              ${escapeHtml(`${recording.recording} · ${recording.duration}s · ${recording.source_platform}`)}
            </option>
          `
        )
        .join("");
      return `<optgroup label="${escapeHtml(appName)}">${options}</optgroup>`;
    });

  elements.recordingFilter.innerHTML = [`<option value="">Select a recording</option>`]
    .concat(optionGroups)
    .join("");
}

function renderSelection() {
  const recording = state.filtered.find((item) => item.recording === state.selectedId);

  if (!recording) {
    elements.detailView.hidden = true;
    elements.emptyState.hidden = false;
    return;
  }

  elements.detailView.hidden = false;
  elements.emptyState.hidden = true;

  elements.detailApp.textContent = recording.app_name;
  elements.detailRecording.textContent = recording.recording;
  elements.detailSubtitle.textContent =
    `${recording.class} from ${recording.source_platform} on ${recording.upload_date}. ` +
    `${recording.timeline.length} timeline event${recording.timeline.length === 1 ? "" : "s"} recorded.`;
  elements.detailVideoCaption.textContent =
    `${recording.duration}s at ${recording.fps} fps, ${recording.resolution.label}`;

  renderDetailBadges(recording);
  renderVideo(recording);
  renderPrimaryFileLinks(recording);
  renderMetadata(recording);
  renderTimelineToggles();
  renderTimeline(recording);
  renderFileGroups(recording);
}

function renderDetailBadges(recording) {
  const badges = [
    ...recording.categories.map((category) => ({ label: category, warm: true })),
    ...recording.languages.map((language) => ({ label: language, warm: false })),
  ];

  elements.detailBadges.innerHTML = badges
    .map((badge) => `<span class="tag ${badge.warm ? "warm" : ""}">${escapeHtml(badge.label)}</span>`)
    .join("");
}

function renderVideo(recording) {
  state.pendingSeekSeconds = null;
  state.pendingAutoplayAfterSeek = false;
  const baseSrc = recording.files.video?.path ?? "";
  elements.recordingVideo.dataset.baseSrc = baseSrc;
  elements.recordingVideo.src = baseSrc;
  elements.recordingVideo.poster = "";
  elements.recordingVideo.load();
}

function renderPrimaryFileLinks(recording) {
  const primary = [
    ["Video on GitHub", recording.files.video?.github_path || recording.files.video?.path, true],
    ["APK", recording.files.apk?.github_path || recording.files.apk?.path, false],
    ["Context script", recording.files.context?.github_path || recording.files.context?.path, false],
    ["Replay script", recording.files.script?.github_path || recording.files.script?.path, false],
  ];

  elements.primaryFileLinks.innerHTML = primary
    .filter(([, path]) => Boolean(path))
    .map(
      ([label, path, primaryStyle]) => `
        <a class="file-link ${primaryStyle ? "primary" : ""}" href="${escapeHtml(path)}" target="_blank" rel="noreferrer">
          ${escapeHtml(label)}
        </a>
      `
    )
    .join("");
}

function renderMetadata(recording) {
  const values = [
    ["App version", recording.app_version],
    ["Class", recording.class],
    ["Categories", recording.categories.join(", ")],
    ["Source", recording.source_platform],
    ["Uploaded", recording.upload_date],
    ["Duration", `${recording.duration} seconds`],
    ["Resolution", recording.resolution.label],
    ["FPS", String(recording.fps)],
    ["Device brand", recording.recording_device_brand],
    ["Reproducible OS", recording.reproducible_device_OS_version],
    ["Languages", recording.languages.join(", ") || "None"],
    ["Sample folder", recording.files.sample_dir],
  ];

  elements.metadataGrid.innerHTML = values
    .map(
      ([term, description]) => `
        <div>
          <dt>${escapeHtml(term)}</dt>
          <dd>${renderMetadataValue(description)}</dd>
        </div>
      `
    )
    .join("");
}

function renderTimelineToggles() {
  elements.timelineToggles.innerHTML = TIMELINE_KINDS.map((kind) => {
    const active = state.filters.timelineKind === kind.id ? "active" : "";
    return `<button class="toggle-chip ${active}" data-kind="${kind.id}" type="button">${escapeHtml(kind.label)}</button>`;
  }).join("");

  for (const button of elements.timelineToggles.querySelectorAll(".toggle-chip")) {
    button.addEventListener("click", () => {
      state.filters.timelineKind = button.dataset.kind;
      renderTimeline(state.filtered.find((item) => item.recording === state.selectedId));
      renderTimelineToggles();
    });
  }
}

function renderTimeline(recording) {
  const visibleEvents = recording.timeline.filter((event) => {
    return state.filters.timelineKind === "all" || event.kind === state.filters.timelineKind;
  });

  elements.timelineList.innerHTML = visibleEvents
    .map(
      (event) => {
        const isJumpable = Number.isFinite(event.seek_seconds);
        const tagName = isJumpable ? "button" : "article";
        const actionIdentity = event.action_identity
          ? `<div class="timeline-identity">Action identity: ${escapeHtml(event.action_identity)}</div>`
          : "";

        return `
        <${tagName}
          class="timeline-item ${isJumpable ? "is-jumpable" : ""}"
          ${isJumpable ? `data-seek="${escapeHtml(String(event.seek_seconds))}"` : ""}
          ${isJumpable ? 'type="button"' : ""}
        >
          <div class="timeline-time">${escapeHtml(event.timestamp_in_seconds || "00:00")}</div>
          <div class="timeline-kind">${escapeHtml(formatKind(event.kind))}</div>
          <div class="timeline-body">
            <strong>${escapeHtml(event.label)}</strong>
            ${actionIdentity}
            <p>${escapeHtml(event.detail)}</p>
          </div>
        </${tagName}>
      `;
      }
    )
    .join("");

  for (const item of elements.timelineList.querySelectorAll("[data-seek]")) {
    item.addEventListener("click", () => {
      jumpVideoToTimestamp(Number(item.dataset.seek));
    });
  }
}

function renderFileGroups(recording) {
  const groups = [
    {
      title: "Primary files",
      items: [recording.files.video, recording.files.apk, recording.files.context, recording.files.script].filter(Boolean),
    },
    {
      title: "Extra files",
      items: recording.files.extras,
    },
  ].filter((group) => group.items.length > 0);

  elements.fileGroups.innerHTML = groups
    .map(
      (group) => `
        <section class="file-group">
          <h4>${escapeHtml(group.title)}</h4>
          <div class="file-group-links">
            ${group.items
              .map(
                (item) =>
                  item.type === "directory"
                    ? `
                      <a class="file-link file-link-static" href="${escapeHtml(
                        item.github_path || item.path
                      )}" target="_blank" rel="noreferrer">
                        ${escapeHtml(item.label)} (directory)
                      </a>
                    `
                    : `
                      <a class="file-link" href="${escapeHtml(item.github_path || item.path)}" target="_blank" rel="noreferrer">
                        ${escapeHtml(item.label)}
                      </a>
                    `
              )
              .join("")}
          </div>
        </section>
      `
    )
    .join("");
}

function formatKind(kind) {
  if (kind === "system_action") {
    return "System action";
  }
  return kind.charAt(0).toUpperCase() + kind.slice(1);
}

function jumpVideoToTimestamp(seekSeconds) {
  const video = elements.recordingVideo;
  const baseSrc = (video.dataset.baseSrc || video.currentSrc || video.src || "").split("#")[0];
  if (!Number.isFinite(seekSeconds) || !baseSrc) {
    return;
  }

  state.pendingSeekSeconds = seekSeconds;
  state.pendingAutoplayAfterSeek = true;
  video.pause();
  video.src = `${baseSrc}#t=${Math.max(0, seekSeconds).toFixed(3)}`;
  video.load();
}

elements.recordingVideo.addEventListener("loadedmetadata", () => {
  if (!Number.isFinite(state.pendingSeekSeconds)) {
    return;
  }

  const pendingSeekSeconds = state.pendingSeekSeconds;
  const video = elements.recordingVideo;
  const duration = Number.isFinite(video.duration) ? video.duration : null;
  const clampedSeek = duration ? Math.min(pendingSeekSeconds, Math.max(duration - 0.05, 0)) : pendingSeekSeconds;

  if (Math.abs(video.currentTime - clampedSeek) > 0.25) {
    video.currentTime = Math.max(0, clampedSeek);
  }
});

elements.recordingVideo.addEventListener("canplay", () => {
  if (!state.pendingAutoplayAfterSeek) {
    return;
  }

  state.pendingAutoplayAfterSeek = false;
  state.pendingSeekSeconds = null;
  elements.recordingVideo.play().catch(() => {});
});

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#39;");
}

function renderMetadataValue(value) {
  if (value && typeof value === "object" && value.path && value.label) {
    return `<a class="meta-link" href="${escapeHtml(value.path)}" target="_blank" rel="noreferrer">${escapeHtml(
      value.label
    )}</a>`;
  }

  return escapeHtml(value || "Unknown");
}
