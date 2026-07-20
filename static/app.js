const state = {
  data: null,
  activeLessonId: null,
  collapsedCategories: new Set(),
  busy: false,
  ideBusy: false,
  openAfterIdeSave: false,
};

const elements = {
  curriculum: document.querySelector("#curriculum"),
  lessonPane: document.querySelector("#lesson-pane"),
  progressLabel: document.querySelector("#progress-label"),
  progressFill: document.querySelector("#progress-fill"),
  sidebar: document.querySelector("#sidebar"),
  scrim: document.querySelector("#sidebar-scrim"),
  toast: document.querySelector("#toast"),
  ideDialog: document.querySelector("#ide-dialog"),
  ideForm: document.querySelector("#ide-form"),
  ideSelect: document.querySelector("#ide-select"),
  customIdeGroup: document.querySelector("#custom-ide-group"),
  customIdeCommand: document.querySelector("#custom-ide-command"),
  ideFormError: document.querySelector("#ide-form-error"),
  saveIdeButton: document.querySelector("#save-ide-button"),
};

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

function inlineCode(value) {
  return escapeHtml(value).replace(/`([^`]+)`/g, "<code>$1</code>");
}

function activeLesson() {
  return state.data.lessons.find((lesson) => lesson.id === state.activeLessonId);
}

function setData(data) {
  state.data = data;
  if (!state.activeLessonId || !data.lessons.some((item) => item.id === state.activeLessonId)) {
    const hashId = decodeURIComponent(location.hash.slice(1));
    state.activeLessonId = data.lessons.some((item) => item.id === hashId)
      ? hashId
      : data.lessons[0].id;
  }
  render();
}

function render() {
  renderProgress();
  renderCurriculum();
  renderLesson();
}

function renderProgress() {
  const { completed, total } = state.data.summary;
  const percentage = total ? Math.round((completed / total) * 100) : 0;
  elements.progressLabel.textContent = `${completed} of ${total} complete`;
  elements.progressFill.style.width = `${percentage}%`;
}

function renderCurriculum() {
  elements.curriculum.innerHTML = state.data.categories.map((category) => {
    const lessons = state.data.lessons.filter((lesson) => lesson.category === category.id);
    const completed = lessons.filter((lesson) => lesson.progress.completed).length;
    const collapsed = state.collapsedCategories.has(category.id);
    return `
      <section class="category ${collapsed ? "collapsed" : ""}" data-category="${escapeHtml(category.id)}">
        <button class="category-toggle" type="button" aria-expanded="${!collapsed}">
          <span class="category-chevron" aria-hidden="true">›</span>
          <span>
            <span class="category-name">${escapeHtml(category.title)}</span>
            <span class="category-description">${escapeHtml(category.description)}</span>
          </span>
          <span class="category-count">${completed}/${lessons.length}</span>
        </button>
        <div class="category-lessons">
          ${lessons.map((lesson) => `
            <button class="lesson-link ${lesson.id === state.activeLessonId ? "active" : ""}" type="button" data-lesson-id="${escapeHtml(lesson.id)}">
              <span class="lesson-check ${lesson.progress.completed ? "complete" : ""}" aria-label="${lesson.progress.completed ? "Completed" : "Not completed"}">✓</span>
              <span class="lesson-link-title">${lesson.order}. ${escapeHtml(lesson.title)}</span>
            </button>
          `).join("")}
        </div>
      </section>
    `;
  }).join("");

  elements.curriculum.querySelectorAll(".category-toggle").forEach((button) => {
    button.addEventListener("click", () => {
      const category = button.closest(".category").dataset.category;
      state.collapsedCategories.has(category)
        ? state.collapsedCategories.delete(category)
        : state.collapsedCategories.add(category);
      renderCurriculum();
    });
  });

  elements.curriculum.querySelectorAll(".lesson-link").forEach((button) => {
    button.addEventListener("click", () => selectLesson(button.dataset.lessonId));
  });
}

function renderLesson() {
  const lesson = activeLesson();
  const category = state.data.categories.find((item) => item.id === lesson.category);
  const index = state.data.lessons.findIndex((item) => item.id === lesson.id);
  const previous = state.data.lessons[index - 1];
  const next = state.data.lessons[index + 1];
  const completionText = lesson.progress.completed ? "Completed" : "Check answer";
  const ideLabel = state.data.ide.selected_label || "No IDE selected";

  elements.lessonPane.innerHTML = `
    <article class="lesson-content">
      <div class="lesson-topline">
        <span class="breadcrumb">${escapeHtml(category.title)} · Lesson ${lesson.order}</span>
        <button class="button button-secondary" id="reset-button" type="button" title="Reset lesson">
          <span aria-hidden="true">↻</span><span class="reset-label">Reset lesson</span>
        </button>
      </div>
      <h1 class="lesson-title">${escapeHtml(lesson.title)}</h1>
      <p class="lesson-summary">${escapeHtml(lesson.summary)}</p>
      <ul class="concept-list">${lesson.concepts.map((concept) => `<li>${escapeHtml(concept)}</li>`).join("")}</ul>

      <section class="lesson-section">
        <p class="section-kicker">The idea</p>
        <h2 class="section-title">How it works</h2>
        <p class="section-copy">${inlineCode(lesson.explanation)}</p>
      </section>

      ${lesson.eli10 ? `
        <aside class="eli10">
          <p class="section-kicker">Explain it like I’m 10</p>
          <p class="section-copy">${inlineCode(lesson.eli10)}</p>
        </aside>
      ` : ""}

      <section class="lesson-section">
        <p class="section-kicker">Example</p>
        <h2 class="section-title">See it in Python</h2>
        <div class="code-block">
          <button class="code-copy" type="button" data-copy="${escapeHtml(lesson.example)}">Copy code</button>
          <pre><code>${escapeHtml(lesson.example)}</code></pre>
        </div>
      </section>

      <section class="lesson-section">
        <div class="assignment-band">
          <p class="section-kicker">Assignment</p>
          <h2 class="section-title">Your turn</h2>
          <p class="section-copy">${escapeHtml(lesson.assignment)}</p>

          <div class="assignment-guidance">
            <h3>Suggested approach</h3>
            <ol>${lesson.assignment_steps.map((step) => `<li>${inlineCode(step)}</li>`).join("")}</ol>
            <details>
              <summary>Need a hint?</summary>
              <p>${inlineCode(lesson.hint)}</p>
            </details>
          </div>

          <div class="ide-launch-row">
            <div class="ide-choice">
              Opens with
              <strong>${escapeHtml(ideLabel)}</strong>
            </div>
            <div class="ide-buttons">
              <button class="button button-primary" id="open-ide-button" type="button"><span aria-hidden="true">↗</span> Open in IDE</button>
              <button class="button button-secondary" id="change-ide-button" type="button">${state.data.ide.selected_id ? "Change IDE" : "Choose IDE"}</button>
            </div>
          </div>

          <span class="field-label">Check from this assignment folder</span>
          <div class="copy-field">
            <span class="copy-value">${escapeHtml(lesson.check_command)}</span>
            <button class="copy-button" type="button" data-copy="${escapeHtml(lesson.check_command)}">Copy command</button>
          </div>

          <div class="assignment-actions">
            <button class="button button-primary" id="check-button" type="button">${lesson.progress.completed ? "✓" : "▶"} ${completionText}</button>
            <span class="category-count">${lesson.progress.attempts ? `${lesson.progress.attempts} check${lesson.progress.attempts === 1 ? "" : "s"}` : "Not checked yet"}</span>
          </div>
          <div class="check-result" id="check-result" aria-live="polite"></div>
        </div>
      </section>

      <nav class="lesson-navigation" aria-label="Lesson navigation">
        ${previous ? `<button class="nav-button" type="button" data-go-to="${escapeHtml(previous.id)}"><span class="nav-direction">← Previous</span><span class="nav-title">${escapeHtml(previous.title)}</span></button>` : ""}
        ${next ? `<button class="nav-button next" type="button" data-go-to="${escapeHtml(next.id)}"><span class="nav-direction">Next →</span><span class="nav-title">${escapeHtml(next.title)}</span></button>` : ""}
      </nav>
    </article>
  `;

  elements.lessonPane.querySelectorAll("[data-copy]").forEach((button) => {
    button.addEventListener("click", () => copyText(button.dataset.copy, button));
  });
  elements.lessonPane.querySelectorAll("[data-go-to]").forEach((button) => {
    button.addEventListener("click", () => selectLesson(button.dataset.goTo, true));
  });
  document.querySelector("#check-button").addEventListener("click", checkLesson);
  document.querySelector("#reset-button").addEventListener("click", resetLesson);
  document.querySelector("#open-ide-button").addEventListener("click", openInIde);
  document.querySelector("#change-ide-button").addEventListener("click", () => openIdePicker(false));
}

function selectLesson(lessonId, focus = false) {
  state.activeLessonId = lessonId;
  location.hash = encodeURIComponent(lessonId);
  renderCurriculum();
  renderLesson();
  closeSidebar();
  window.scrollTo({ top: 0, behavior: "smooth" });
  if (focus) elements.lessonPane.focus({ preventScroll: true });
}

async function copyText(text, button) {
  try {
    await navigator.clipboard.writeText(text);
    const original = button.textContent;
    button.textContent = "Copied";
    showToast("Copied to clipboard");
    window.setTimeout(() => { button.textContent = original; }, 1200);
  } catch (_) {
    showToast("Clipboard access was blocked. Select the text manually.");
  }
}

async function checkLesson() {
  if (state.busy) return;
  state.busy = true;
  const lessonId = state.activeLessonId;
  const button = document.querySelector("#check-button");
  const resultBox = document.querySelector("#check-result");
  button.disabled = true;
  button.textContent = "Checking…";
  resultBox.className = "check-result";
  try {
    const response = await fetch(`/api/lessons/${lessonId}:check`, { method: "POST" });
    const payload = await response.json();
    if (!response.ok) throw new Error(payload.error || "The check could not run.");
    state.data = payload.state;
    renderProgress();
    renderCurriculum();
    const currentButton = document.querySelector("#check-button");
    currentButton.disabled = false;
    currentButton.textContent = payload.passed ? "✓ Completed" : "▶ Check answer";
    const currentResult = document.querySelector("#check-result");
    currentResult.className = `check-result visible ${payload.passed ? "pass" : "fail"}`;
    currentResult.innerHTML = `<strong>${payload.passed ? "All tests passed" : "Some tests failed"}</strong><pre>${escapeHtml(payload.output)}</pre>`;
    showToast(payload.passed ? "Lesson completed" : "Tests found something to fix");
  } catch (error) {
    resultBox.className = "check-result visible fail";
    resultBox.innerHTML = `<strong>Check failed to run</strong><pre>${escapeHtml(error.message)}</pre>`;
    button.disabled = false;
    button.textContent = "▶ Check answer";
  } finally {
    state.busy = false;
  }
}

async function resetLesson() {
  if (state.busy) return;
  const lesson = activeLesson();
  const confirmed = window.confirm(`Reset “${lesson.title}”? This replaces solution.py with the starter code and clears its progress.`);
  if (!confirmed) return;
  state.busy = true;
  const button = document.querySelector("#reset-button");
  button.disabled = true;
  try {
    const response = await fetch(`/api/lessons/${lesson.id}:reset`, { method: "POST" });
    const payload = await response.json();
    if (!response.ok) throw new Error(payload.error || "The lesson could not be reset.");
    state.data = payload.state;
    render();
    showToast("Lesson reset to its starter state");
  } catch (error) {
    button.disabled = false;
    showToast(error.message);
  } finally {
    state.busy = false;
  }
}

function populateIdePicker() {
  elements.ideSelect.innerHTML = state.data.ide.options.map((option) => (
    `<option value="${escapeHtml(option.id)}">${escapeHtml(option.label)}</option>`
  )).join("");
  elements.ideSelect.value = state.data.ide.selected_id || "vscode";
  elements.customIdeCommand.value = state.data.ide.custom_command || "";
  updateCustomIdeVisibility();
}

function openIdePicker(openAfterSave) {
  state.openAfterIdeSave = openAfterSave;
  elements.ideFormError.textContent = "";
  elements.saveIdeButton.textContent = openAfterSave ? "Save and open" : "Save IDE";
  populateIdePicker();
  elements.ideDialog.showModal();
  elements.ideSelect.focus();
}

function closeIdePicker() {
  state.openAfterIdeSave = false;
  elements.ideDialog.close();
}

function updateCustomIdeVisibility() {
  const isCustom = elements.ideSelect.value === "custom";
  elements.customIdeGroup.hidden = !isCustom;
  elements.customIdeCommand.required = isCustom;
}

async function saveIde(event) {
  event.preventDefault();
  if (state.ideBusy) return;
  const shouldOpen = state.openAfterIdeSave;
  state.ideBusy = true;
  elements.saveIdeButton.disabled = true;
  elements.ideFormError.textContent = "";
  try {
    const response = await fetch("/api/settings/ide", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        ide_id: elements.ideSelect.value,
        custom_command: elements.customIdeCommand.value,
      }),
    });
    const payload = await response.json();
    if (!response.ok) throw new Error(payload.error || "The IDE choice could not be saved.");
    state.data = payload.state;
    closeIdePicker();
    renderLesson();
    showToast(`Saved ${state.data.ide.selected_label}`);
    if (shouldOpen) await launchIde();
  } catch (error) {
    elements.ideFormError.textContent = error.message;
  } finally {
    state.ideBusy = false;
    elements.saveIdeButton.disabled = false;
  }
}

async function openInIde() {
  if (!state.data.ide.selected_id) {
    openIdePicker(true);
    return;
  }
  await launchIde();
}

async function launchIde() {
  if (state.ideBusy) return;
  state.ideBusy = true;
  const button = document.querySelector("#open-ide-button");
  button.disabled = true;
  button.textContent = "Opening…";
  try {
    const response = await fetch(`/api/lessons/${state.activeLessonId}:open`, { method: "POST" });
    const payload = await response.json();
    if (!response.ok) throw new Error(payload.error || "The IDE could not be opened.");
    showToast(`Opened in ${payload.ide_label}`);
  } catch (error) {
    showToast(error.message);
  } finally {
    state.ideBusy = false;
    const currentButton = document.querySelector("#open-ide-button");
    if (currentButton) {
      currentButton.disabled = false;
      currentButton.innerHTML = '<span aria-hidden="true">↗</span> Open in IDE';
    }
  }
}

let toastTimer;
function showToast(message) {
  window.clearTimeout(toastTimer);
  elements.toast.textContent = message;
  elements.toast.classList.add("visible");
  toastTimer = window.setTimeout(() => elements.toast.classList.remove("visible"), 2200);
}

function openSidebar() {
  elements.sidebar.classList.add("open");
  elements.scrim.classList.add("visible");
}

function closeSidebar() {
  elements.sidebar.classList.remove("open");
  elements.scrim.classList.remove("visible");
}

document.querySelector("#menu-button").addEventListener("click", openSidebar);
document.querySelector("#close-menu-button").addEventListener("click", closeSidebar);
elements.scrim.addEventListener("click", closeSidebar);
elements.ideSelect.addEventListener("change", updateCustomIdeVisibility);
elements.ideForm.addEventListener("submit", saveIde);
document.querySelector("#close-ide-dialog").addEventListener("click", closeIdePicker);
document.querySelector("#cancel-ide-dialog").addEventListener("click", closeIdePicker);
elements.ideDialog.addEventListener("click", (event) => {
  if (event.target === elements.ideDialog) closeIdePicker();
});
window.addEventListener("hashchange", () => {
  const lessonId = decodeURIComponent(location.hash.slice(1));
  if (state.data && state.data.lessons.some((lesson) => lesson.id === lessonId)) {
    state.activeLessonId = lessonId;
    render();
  }
});

fetch("/api/state")
  .then((response) => {
    if (!response.ok) throw new Error("Could not load the local curriculum.");
    return response.json();
  })
  .then(setData)
  .catch((error) => {
    elements.lessonPane.innerHTML = `<div class="loading-state"><h1>LearnLab could not start</h1><p>${escapeHtml(error.message)}</p></div>`;
  });
