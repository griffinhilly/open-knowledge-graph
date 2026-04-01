#!/usr/bin/env python3
"""Generate the domain-specific quiz page for OKG.

Outputs a single lightweight HTML page that loads per-domain question data
via fetch and provides course-level quiz selection with fluency integration.

Usage:
    python tools/generate_domain_quiz.py
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "output"


def generate():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    html = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Domain Quiz — Open Knowledge Graph</title>
<style>
* { margin:0; padding:0; box-sizing:border-box; }
body {
  background:#1a1a2e; color:#ccc;
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
  min-height:100vh;
}
.container { max-width:720px; margin:0 auto; padding:40px 20px; }
h1 { color:#eee; font-size:24px; margin-bottom:4px; }
.subtitle { color:#888; font-size:14px; margin-bottom:24px; }
.back-link { color:#668; text-decoration:none; font-size:13px; display:inline-block; margin-bottom:16px; }
.back-link:hover { color:#99b; }

/* Course picker */
.picker-header { color:#aaa; font-size:13px; text-transform:uppercase; letter-spacing:1px; margin-bottom:12px; }
.stage-group { margin-bottom:16px; }
.stage-label {
  color:#777; font-size:11px; text-transform:uppercase; letter-spacing:1px;
  margin-bottom:6px; padding-left:4px;
}
.course-item {
  display:flex; align-items:center; gap:10px;
  padding:8px 12px; border-radius:6px; cursor:pointer;
  transition:background 0.1s;
}
.course-item:hover { background:rgba(255,255,255,0.04); }
.course-item input[type="checkbox"] { accent-color:#7c4dff; width:16px; height:16px; cursor:pointer; }
.course-item label { cursor:pointer; flex:1; color:#ccc; font-size:14px; }
.course-item .qcount { color:#666; font-size:12px; white-space:nowrap; }

.btn-row { display:flex; gap:12px; margin-top:20px; flex-wrap:wrap; }
.btn {
  padding:10px 24px; border-radius:8px; border:none;
  font-size:14px; cursor:pointer; font-family:inherit;
  transition:background 0.15s, transform 0.1s;
}
.btn:hover { transform:translateY(-1px); }
.btn-primary { background:#7c4dff; color:#fff; }
.btn-primary:hover { background:#9068ff; }
.btn-primary:disabled { background:#444; color:#777; cursor:default; transform:none; }
.btn-outline { background:transparent; border:1px solid #555; color:#aaa; }
.btn-outline:hover { background:rgba(255,255,255,0.06); border-color:#777; }

/* Quiz */
.progress-wrap {
  height:4px; background:#2a2a44; border-radius:2px; margin-bottom:16px; overflow:hidden;
}
.progress-bar { height:100%; background:#7c4dff; transition:width 0.3s; }
.score-display { color:#8bc48b; font-size:14px; font-weight:600; }
.phase-label {
  display:inline-block; padding:3px 10px; border-radius:12px;
  font-size:11px; margin-bottom:12px; background:rgba(124,77,255,0.2); color:#b39ddb;
}
.question-card {
  background:rgba(30,30,50,0.8); border:1px solid #333; border-radius:12px;
  padding:24px; margin-bottom:16px;
}
.question-text { color:#eee; font-size:16px; line-height:1.6; margin-bottom:16px; }
.option-btn {
  display:block; width:100%; text-align:left;
  padding:12px 16px; margin-bottom:8px;
  background:rgba(40,40,70,0.6); border:1px solid #333; border-radius:8px;
  color:#ccc; font-size:14px; cursor:pointer; transition:border-color 0.15s, background 0.15s;
  font-family:inherit;
}
.option-btn:hover { border-color:#666; background:rgba(50,50,80,0.8); }
.option-btn.correct { border-color:#4caf50; background:rgba(76,175,80,0.15); color:#81c784; }
.option-btn.wrong { border-color:#f44336; background:rgba(244,67,54,0.15); color:#e57373; }
.option-btn.reveal { border-color:#4caf50; background:rgba(76,175,80,0.08); }
.option-btn:disabled { cursor:default; }

.tf-row { display:flex; gap:12px; margin-bottom:8px; }
.tf-btn {
  flex:1; padding:12px; text-align:center;
  background:rgba(40,40,70,0.6); border:1px solid #333; border-radius:8px;
  color:#ccc; font-size:14px; cursor:pointer; font-family:inherit;
  transition:border-color 0.15s, background 0.15s;
}
.tf-btn:hover { border-color:#666; }
.tf-btn.correct { border-color:#4caf50; background:rgba(76,175,80,0.15); color:#81c784; }
.tf-btn.wrong { border-color:#f44336; background:rgba(244,67,54,0.15); color:#e57373; }
.tf-btn.reveal { border-color:#4caf50; background:rgba(76,175,80,0.08); }

.sa-area {
  width:100%; min-height:80px; padding:12px; margin-bottom:8px;
  background:rgba(20,20,40,0.8); border:1px solid #333; border-radius:8px;
  color:#ccc; font-size:14px; font-family:inherit; resize:vertical;
}
.grade-row { display:flex; gap:8px; margin-top:8px; }
.grade-btn {
  flex:1; padding:8px; text-align:center; border-radius:6px;
  border:1px solid #333; font-size:13px; cursor:pointer; font-family:inherit;
}
.grade-btn.got-it { background:rgba(76,175,80,0.15); border-color:rgba(76,175,80,0.4); color:#81c784; }
.grade-btn.partial { background:rgba(255,193,7,0.15); border-color:rgba(255,193,7,0.4); color:#ffd54f; }
.grade-btn.missed { background:rgba(244,67,54,0.15); border-color:rgba(244,67,54,0.4); color:#e57373; }

.explanation {
  margin-top:12px; padding:12px 16px;
  background:rgba(40,50,40,0.3); border-left:3px solid #4caf50;
  border-radius:0 6px 6px 0; color:#a5c8a5; font-size:13px; line-height:1.5;
}

.action-row { display:flex; gap:12px; justify-content:center; margin-top:8px; }

/* Results */
.result-card {
  background:rgba(30,30,50,0.8); border:1px solid #333; border-radius:10px;
  padding:20px; margin-bottom:12px;
}
.result-card h3 { color:#ddd; font-size:16px; margin-bottom:8px; }
.stat-row { display:flex; gap:24px; flex-wrap:wrap; margin-bottom:8px; }
.stat { text-align:center; }
.stat-val { color:#eee; font-size:24px; font-weight:700; }
.stat-label { color:#777; font-size:11px; }

/* Loading */
.spinner {
  width:32px; height:32px; border:3px solid #333;
  border-top-color:#7c4dff; border-radius:50%;
  animation:spin 0.8s linear infinite; margin:0 auto 16px;
}
@keyframes spin { to { transform:rotate(360deg); } }
.error { color:#e57373; }
</style>
</head>
<body>

<div class="container" id="app">
  <div style="text-align:center; padding:60px 0">
    <div class="spinner"></div>
    <p>Loading questions...</p>
  </div>
</div>

<script src="js/fluency.js"></script>
<script>
'use strict';

// ---------------------------------------------------------------------------
// State
// ---------------------------------------------------------------------------
const params = new URLSearchParams(location.search);
const DOMAIN = params.get('domain') || '';
const DOMAIN_LABEL = DOMAIN.replace(/-/g, ' ').replace(/\band\b/g, '&')
  .replace(/\b\w/g, c => c.toUpperCase());

let DATA = null;       // loaded via fetch
let GRAPH = null;      // built from embedded prereq data if available
let S = {
  phase: 'loading',    // loading | picker | quiz | results
  selectedCourses: new Set(),
  queue: [],
  index: 0,
  answers: [],         // {topicId, course, stage, correct, score, responseTimeMs}
  questionStart: null,
  showingFeedback: false,
};

const STAGES_ORDERED = [
  'pre-formal', 'concrete-operations', 'abstract-reasoning',
  'formal-systems', 'advanced', 'expert'
];
const STAGE_LABELS = {
  'pre-formal': 'Pre-Formal',
  'concrete-operations': 'Concrete Operations',
  'abstract-reasoning': 'Abstract Reasoning',
  'formal-systems': 'Formal Systems',
  'advanced': 'Advanced',
  'expert': 'Expert'
};

// Median response times (ms) for evidence weighting
const MEDIAN_MC = 12000;
const MEDIAN_TF = 8000;
const MEDIAN_SA = 20000;

// ---------------------------------------------------------------------------
// DOM helpers
// ---------------------------------------------------------------------------
const app = () => document.getElementById('app');

function h(tag, attrs) {
  const children = Array.from(arguments).slice(2).flat();
  const el = document.createElement(tag);
  if (attrs) {
    for (const [k, v] of Object.entries(attrs)) {
      if (k === 'className') el.className = v;
      else if (k.startsWith('on') && typeof v === 'function')
        el.addEventListener(k.slice(2).toLowerCase(), v);
      else if (k === 'style' && typeof v === 'object') Object.assign(el.style, v);
      else if (k === 'innerHTML') el.innerHTML = v;
      else if (v == null) el.removeAttribute(k);
      else el.setAttribute(k, v);
    }
  }
  for (const c of children) {
    if (c == null || c === false) continue;
    if (typeof c === 'string' || typeof c === 'number')
      el.appendChild(document.createTextNode(c));
    else if (c instanceof Node) el.appendChild(c);
  }
  return el;
}

function setContent(el) { app().innerHTML = ''; app().appendChild(el); }

function shuffle(arr) {
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

// ---------------------------------------------------------------------------
// Data loading
// ---------------------------------------------------------------------------
async function loadData() {
  if (!DOMAIN) {
    setContent(h('div', {className: 'container'},
      h('p', {className: 'error'}, 'No domain specified. Use ?domain=mathematics')
    ));
    return;
  }
  try {
    const resp = await fetch('questions/' + DOMAIN + '.json');
    if (!resp.ok) throw new Error('HTTP ' + resp.status);
    DATA = await resp.json();
    S.phase = 'picker';
    render();
  } catch (e) {
    setContent(h('div', {className: 'container'},
      h('p', {className: 'error'}, 'Failed to load questions for ' + DOMAIN_LABEL + ': ' + e.message)
    ));
  }
}

// ---------------------------------------------------------------------------
// Build prerequisite graph from question data (for propagation)
// ---------------------------------------------------------------------------
// We don't have full prereq data in the question JSON, but fluency.js
// propagation needs a graph. We fetch the domain's map data for this.
async function loadPrereqGraph() {
  // The domain map HTML has embedded graph data, but we can't easily extract it.
  // Instead, we'll rely on OKGFluency.propagate() being called on the domain map
  // page when the user returns. For now, just do direct score updates.
  // A future enhancement could embed prereq edges in the question JSON.
  return null;
}

// ---------------------------------------------------------------------------
// Course picker
// ---------------------------------------------------------------------------
function renderPicker() {
  const byStage = {};
  for (const c of DATA.courses) {
    if (!byStage[c.stage]) byStage[c.stage] = [];
    byStage[c.stage].push(c);
  }

  const groups = [];
  for (const stage of STAGES_ORDERED) {
    if (!byStage[stage] || byStage[stage].length === 0) continue;
    const items = byStage[stage].map(c => {
      const checked = S.selectedCourses.has(c.id);
      return h('div', {className: 'course-item', onClick: () => {
        if (S.selectedCourses.has(c.id)) S.selectedCourses.delete(c.id);
        else S.selectedCourses.add(c.id);
        render();
      }},
        h('input', {type: 'checkbox', checked: checked ? 'checked' : null,
          id: 'c-' + c.id}),
        h('label', {for: 'c-' + c.id}, c.title),
        h('span', {className: 'qcount'}, c.questionCount + ' questions')
      );
    });
    groups.push(h('div', {className: 'stage-group'},
      h('div', {className: 'stage-label'}, STAGE_LABELS[stage] || stage),
      ...items
    ));
  }

  const totalSelected = S.selectedCourses.size;
  const totalQ = DATA.courses
    .filter(c => S.selectedCourses.has(c.id))
    .reduce((sum, c) => sum + c.questionCount, 0);

  setContent(h('div', {className: 'container'},
    h('a', {className: 'back-link', href: DOMAIN + '-map.html'}, '\u2190 Back to ' + DOMAIN_LABEL + ' Map'),
    h('h1', null, DOMAIN_LABEL + ' Quiz'),
    h('p', {className: 'subtitle'}, 'Select courses to test your knowledge. Questions progress from easier to harder.'),
    h('div', {className: 'picker-header'}, 'Courses'),
    h('div', {className: 'btn-row', style: {marginBottom: '16px'}},
      h('button', {className: 'btn btn-outline', onClick: () => {
        DATA.courses.forEach(c => S.selectedCourses.add(c.id));
        render();
      }}, 'Select All'),
      h('button', {className: 'btn btn-outline', onClick: () => {
        S.selectedCourses.clear();
        render();
      }}, 'Clear')
    ),
    ...groups,
    h('div', {className: 'btn-row'},
      h('button', {
        className: 'btn btn-primary',
        disabled: totalSelected === 0 ? 'disabled' : null,
        onClick: startQuiz
      }, totalSelected === 0
        ? 'Select courses to begin'
        : 'Start Quiz (' + totalQ + ' questions)')
    )
  ));
}

// ---------------------------------------------------------------------------
// Build quiz queue
// ---------------------------------------------------------------------------
function startQuiz() {
  // Filter questions to selected courses
  const selected = S.selectedCourses;
  let pool = DATA.questions.filter(q => selected.has(q.course));

  // Sort by stage order, shuffle within each stage
  const byStage = {};
  for (const q of pool) {
    if (!byStage[q.stage]) byStage[q.stage] = [];
    byStage[q.stage].push(q);
  }

  const queue = [];
  for (const stage of STAGES_ORDERED) {
    if (byStage[stage]) {
      shuffle(byStage[stage]);
      queue.push(...byStage[stage]);
    }
  }

  S.queue = queue;
  S.index = 0;
  S.answers = [];
  S.phase = 'quiz';
  S.showingFeedback = false;
  render();
}

// ---------------------------------------------------------------------------
// Quiz rendering
// ---------------------------------------------------------------------------
function renderQuiz() {
  if (S.index >= S.queue.length) {
    finishQuiz();
    return;
  }

  const q = S.queue[S.index];
  const totalAnswered = S.answers.length;
  const totalCorrect = S.answers.filter(a => a.correct).length;
  const progress = (S.index / S.queue.length) * 100;

  const card = renderQuestionCard(q);

  setContent(h('div', {className: 'container'},
    h('a', {className: 'back-link', href: DOMAIN + '-map.html'}, '\u2190 Back to Map'),
    h('div', {style: {display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '6px'}},
      h('h1', {style: {margin: 0}}, DOMAIN_LABEL + ' Quiz'),
      totalAnswered > 0
        ? h('span', {className: 'score-display'}, totalCorrect + '/' + totalAnswered)
        : null
    ),
    h('p', {className: 'subtitle'},
      'Question ' + (S.index + 1) + ' of ' + S.queue.length +
      ' \u2014 ' + (STAGE_LABELS[q.stage] || q.stage)
    ),
    h('div', {className: 'progress-wrap'},
      h('div', {className: 'progress-bar', style: {width: progress + '%'}})
    ),
    h('span', {className: 'phase-label'}, q.topicTitle),
    card,
    h('div', {className: 'action-row'},
      h('button', {className: 'btn btn-outline', onClick: skipQuestion}, 'Skip'),
      h('button', {className: 'btn btn-outline', onClick: () => { finishQuiz(); }}, 'I\'m Done')
    )
  ));

  S.questionStart = performance.now();
}

function renderQuestionCard(q) {
  const card = h('div', {className: 'question-card'});
  card.appendChild(h('div', {className: 'question-text'}, q.question));

  if (q.type === 'multiple-choice') {
    (q.options || []).forEach((opt, i) => {
      card.appendChild(h('button', {
        className: 'option-btn',
        id: 'opt-' + i,
        onClick: () => answerMC(q, i)
      }, opt));
    });
  } else if (q.type === 'true-false') {
    card.appendChild(h('div', {className: 'tf-row'},
      h('button', {className: 'tf-btn', id: 'tf-true', onClick: () => answerTF(q, true)}, 'True'),
      h('button', {className: 'tf-btn', id: 'tf-false', onClick: () => answerTF(q, false)}, 'False')
    ));
  } else if (q.type === 'short-answer') {
    card.appendChild(h('textarea', {className: 'sa-area', id: 'sa-input',
      placeholder: 'Type your answer...'}));
    card.appendChild(h('button', {className: 'btn btn-primary', id: 'reveal-btn',
      onClick: () => revealSA(q)}, 'Reveal Answer'));
    card.appendChild(h('div', {id: 'sa-model', style: {display: 'none'}}));
    card.appendChild(h('div', {className: 'grade-row', id: 'grade-row', style: {display: 'none'}},
      h('button', {className: 'grade-btn got-it', onClick: () => gradeSA(q, 1.0)}, 'Got it'),
      h('button', {className: 'grade-btn partial', onClick: () => gradeSA(q, 0.5)}, 'Partially'),
      h('button', {className: 'grade-btn missed', onClick: () => gradeSA(q, 0.0)}, 'Missed it')
    ));
  }

  card.appendChild(h('div', {className: 'explanation', id: 'expl',
    style: {display: 'none'}}, q.explanation));

  return card;
}

// ---------------------------------------------------------------------------
// Answer handlers
// ---------------------------------------------------------------------------
function answerMC(q, selected) {
  if (S.showingFeedback) return;
  S.showingFeedback = true;

  const responseTimeMs = Math.round(performance.now() - S.questionStart);
  const correct = selected === q.answer;

  // Color buttons
  (q.options || []).forEach((_, i) => {
    const btn = document.getElementById('opt-' + i);
    if (!btn) return;
    btn.disabled = true;
    if (i === q.answer) btn.className = 'option-btn correct';
    else if (i === selected) btn.className = 'option-btn wrong';
  });

  recordAndAdvance(q, correct, correct ? 1.0 : 0.0, responseTimeMs);
}

function answerTF(q, selected) {
  if (S.showingFeedback) return;
  S.showingFeedback = true;

  const responseTimeMs = Math.round(performance.now() - S.questionStart);
  const correct = selected === q.answer;

  const trueBtn = document.getElementById('tf-true');
  const falseBtn = document.getElementById('tf-false');
  if (trueBtn) { trueBtn.disabled = true; }
  if (falseBtn) { falseBtn.disabled = true; }

  if (q.answer === true) {
    if (trueBtn) trueBtn.className = 'tf-btn correct';
    if (!correct && falseBtn) falseBtn.className = 'tf-btn wrong';
  } else {
    if (falseBtn) falseBtn.className = 'tf-btn correct';
    if (!correct && trueBtn) trueBtn.className = 'tf-btn wrong';
  }

  recordAndAdvance(q, correct, correct ? 1.0 : 0.0, responseTimeMs);
}

function revealSA(q) {
  const model = document.getElementById('sa-model');
  const gradeRow = document.getElementById('grade-row');
  const revealBtn = document.getElementById('reveal-btn');
  if (model) {
    model.style.display = '';
    model.appendChild(h('div', {className: 'question-card', style: {marginTop: '8px'}},
      h('div', {style: {color: '#aaa', fontSize: '11px', marginBottom: '4px'}}, 'Model Answer:'),
      h('div', {style: {color: '#eee', fontSize: '14px', lineHeight: '1.5'}}, q.modelAnswer || '')
    ));
  }
  if (gradeRow) gradeRow.style.display = '';
  if (revealBtn) revealBtn.style.display = 'none';

  S.questionStart = performance.now(); // reset timer to measure grading time
}

function gradeSA(q, grade) {
  if (S.showingFeedback) return;
  S.showingFeedback = true;
  const responseTimeMs = Math.round(performance.now() - S.questionStart);
  recordAndAdvance(q, grade >= 0.5, grade, responseTimeMs);
}

function recordAndAdvance(q, correct, score, responseTimeMs) {
  // Update fluency
  if (typeof OKGFluency !== 'undefined') {
    OKGFluency.updateTopic(q.topicId, correct, {
      difficulty: STAGES_ORDERED.indexOf(q.stage) / 5,
      responseTimeMs: responseTimeMs,
      medianTimeMs: q.type === 'true-false' ? MEDIAN_TF
                  : q.type === 'short-answer' ? MEDIAN_SA : MEDIAN_MC
    });
  }

  S.answers.push({
    topicId: q.topicId, course: q.course, stage: q.stage,
    correct: correct, score: score, responseTimeMs: responseTimeMs
  });

  // Show explanation and next button
  const expl = document.getElementById('expl');
  if (expl) expl.style.display = '';

  const actionRow = document.querySelector('.action-row');
  if (actionRow) {
    actionRow.innerHTML = '';
    const nextBtn = h('button', {className: 'btn btn-primary', onClick: () => {
      S.showingFeedback = false;
      S.index++;
      render();
    }}, S.index + 1 >= S.queue.length ? 'See Results' : 'Next Question');
    actionRow.appendChild(nextBtn);
  }
}

function skipQuestion() {
  if (S.showingFeedback) return;
  S.index++;
  render();
}

// ---------------------------------------------------------------------------
// Results + stage floor inference
// ---------------------------------------------------------------------------
function finishQuiz() {
  // Apply domain-level stage floor inference
  applyStageFloors();
  S.phase = 'results';
  render();
}

function applyStageFloors() {
  if (typeof OKGFluency === 'undefined' || S.answers.length === 0) return;

  // Calculate accuracy per stage
  const byStage = {};
  for (const a of S.answers) {
    if (!byStage[a.stage]) byStage[a.stage] = {correct: 0, total: 0};
    byStage[a.stage].total++;
    if (a.correct) byStage[a.stage].correct++;
  }

  // Find highest stage with >= 60% accuracy
  let highestDemonstrated = -1;
  for (let i = 0; i < STAGES_ORDERED.length; i++) {
    const sp = byStage[STAGES_ORDERED[i]];
    if (sp && sp.total >= 2 && sp.correct / sp.total >= 0.6) {
      highestDemonstrated = i;
    }
  }

  if (highestDemonstrated < 1) return; // nothing to infer

  // Set floors for all stages below the demonstrated level
  // For each topic in DATA that belongs to a stage below demonstrated,
  // set a minimum fluency score
  const FLOOR_SCORES = [95, 90, 80, 70, 55, 40]; // per stage index

  const scores = OKGFluency.loadScores();
  let inferred = 0;

  for (const q of DATA.questions) {
    const stageIdx = STAGES_ORDERED.indexOf(q.stage);
    if (stageIdx < 0 || stageIdx >= highestDemonstrated) continue;
    // Only infer for courses that were selected (or all if they tested broadly)
    if (S.selectedCourses.size < DATA.courses.length &&
        !S.selectedCourses.has(q.course)) continue;

    const floor = FLOOR_SCORES[stageIdx] || 50;
    const current = scores[q.topicId] || 0;
    if (current < floor) {
      scores[q.topicId] = floor;
      inferred++;
    }
  }

  if (inferred > 0) {
    // Use bulkSetScores to persist
    OKGFluency.bulkSetScores(scores);
  }

  S._inferred = inferred;
  S._highestStage = STAGES_ORDERED[highestDemonstrated];
}

function renderResults() {
  const total = S.answers.length;
  const correct = S.answers.filter(a => a.correct).length;
  const pct = total > 0 ? Math.round(100 * correct / total) : 0;

  // Per-course breakdown
  const byCourse = {};
  for (const a of S.answers) {
    if (!byCourse[a.course]) byCourse[a.course] = {correct: 0, total: 0};
    byCourse[a.course].total++;
    if (a.correct) byCourse[a.course].correct++;
  }

  const courseCards = DATA.courses
    .filter(c => byCourse[c.id])
    .map(c => {
      const p = byCourse[c.id];
      const cpct = Math.round(100 * p.correct / p.total);
      return h('div', {style: {display: 'flex', justifyContent: 'space-between',
        padding: '6px 0', borderBottom: '1px solid #2a2a44'}},
        h('span', null, c.title),
        h('span', {style: {color: cpct >= 60 ? '#81c784' : cpct >= 30 ? '#ffd54f' : '#e57373'}},
          p.correct + '/' + p.total + ' (' + cpct + '%)')
      );
    });

  const inferMsg = S._inferred > 0
    ? h('div', {className: 'result-card'},
        h('h3', null, 'Prerequisite Inference'),
        h('p', {style: {color: '#a5c8a5', fontSize: '14px'}},
          'Based on your performance at the ' + (STAGE_LABELS[S._highestStage] || '') +
          ' level, fluency has been inferred for ' + S._inferred +
          ' prerequisite topics in earlier stages.')
      )
    : null;

  setContent(h('div', {className: 'container'},
    h('a', {className: 'back-link', href: DOMAIN + '-map.html'}, '\u2190 Back to ' + DOMAIN_LABEL + ' Map'),
    h('h1', null, DOMAIN_LABEL + ' Quiz Results'),
    h('div', {className: 'result-card'},
      h('div', {className: 'stat-row'},
        h('div', {className: 'stat'},
          h('div', {className: 'stat-val'}, correct + '/' + total),
          h('div', {className: 'stat-label'}, 'Correct')
        ),
        h('div', {className: 'stat'},
          h('div', {className: 'stat-val'}, pct + '%'),
          h('div', {className: 'stat-label'}, 'Accuracy')
        ),
        h('div', {className: 'stat'},
          h('div', {className: 'stat-val'}, String(S.answers.length)),
          h('div', {className: 'stat-label'}, 'Answered')
        )
      )
    ),
    inferMsg,
    h('div', {className: 'result-card'},
      h('h3', null, 'By Course'),
      ...courseCards
    ),
    h('div', {className: 'btn-row'},
      h('a', {className: 'btn btn-primary', href: DOMAIN + '-map.html',
        style: {textDecoration: 'none', textAlign: 'center'}},
        'View ' + DOMAIN_LABEL + ' Map'),
      h('button', {className: 'btn btn-outline', onClick: () => {
        S.phase = 'picker';
        S.selectedCourses = new Set();
        render();
      }}, 'Test Again')
    )
  ));
}

// ---------------------------------------------------------------------------
// Render dispatch
// ---------------------------------------------------------------------------
function render() {
  switch (S.phase) {
    case 'loading': break; // initial load handled by loadData
    case 'picker': renderPicker(); break;
    case 'quiz': renderQuiz(); break;
    case 'results': renderResults(); break;
  }
}

// Boot
loadData();
</script>

</body>
</html>"""

    out_path = OUTPUT_DIR / "domain-quiz.html"
    out_path.write_text(html, encoding="utf-8")
    size_kb = out_path.stat().st_size / 1024
    print(f"Generated {out_path} ({size_kb:.0f} KB)")


if __name__ == "__main__":
    generate()
