#!/usr/bin/env python3
"""Generate the adaptive placement assessment page.

Renders output/assessment.html — a self-contained adaptive placement assessment
that loads topic data from assessment-data.json and runs a 3-round adaptive
assessment to estimate where a user sits on the knowledge graph.

Usage:
    python tools/generate_assessment_page.py
"""

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "output"


def generate_assessment_html() -> str:
    """Generate the complete assessment HTML page with embedded data."""
    # Load assessment data and embed it
    data_path = OUTPUT_DIR / "assessment-data.json"
    if data_path.exists():
        embedded_data = data_path.read_text(encoding="utf-8")
    else:
        embedded_data = "null"
        print("WARNING: assessment-data.json not found, embedding null")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Knowledge Placement Assessment — Open Knowledge Graph</title>
<style>
{_css()}
</style>
</head>
<body>

<div id="app"></div>

<script>
const EMBEDDED_DATA = {embedded_data};
{_js()}
</script>

</body>
</html>"""


def _css() -> str:
    return """\
* { margin: 0; padding: 0; box-sizing: border-box; }

body {
  background: #1a1a2e; color: #ccc;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  min-height: 100vh;
}

/* --- Layout --- */
.container {
  max-width: 720px; margin: 0 auto; padding: 40px 20px;
}

h1 { color: #eee; font-size: 28px; margin-bottom: 6px; }
h2 { color: #ddd; font-size: 22px; margin-bottom: 12px; }
h3 { color: #ccc; font-size: 16px; margin-bottom: 8px; }
.subtitle { color: #777; font-size: 14px; margin-bottom: 32px; }

/* --- Progress bar --- */
.progress-wrap {
  background: rgba(40,40,70,0.6); border-radius: 8px;
  height: 8px; margin-bottom: 28px; overflow: hidden;
}
.progress-bar {
  height: 100%; border-radius: 8px;
  background: linear-gradient(90deg, #4CAF50, #FFC107, #F44336);
  transition: width 0.4s ease;
}

/* --- Round label --- */
.round-label {
  display: inline-block; padding: 4px 12px; border-radius: 12px;
  font-size: 11px; font-weight: 600; letter-spacing: 0.5px; text-transform: uppercase;
  margin-bottom: 16px;
}
.round-label.r1 { background: rgba(76,175,80,0.2); color: #4CAF50; }
.round-label.r2 { background: rgba(255,193,7,0.2); color: #FFC107; }
.round-label.r3 { background: rgba(244,67,54,0.2); color: #F44336; }

/* --- Topic card (question) --- */
.topic-card {
  background: rgba(40,40,70,0.6); border: 1px solid #333;
  border-radius: 12px; padding: 28px 24px; margin-bottom: 20px;
  animation: fadeIn 0.3s ease;
}
@keyframes fadeIn { from { opacity:0; transform:translateY(8px); } to { opacity:1; transform:translateY(0); } }

.topic-card .topic-title { color: #eee; font-size: 20px; margin-bottom: 8px; }
.topic-card .topic-desc { color: #999; font-size: 14px; line-height: 1.5; margin-bottom: 6px; }
.topic-card .topic-meta { color: #666; font-size: 12px; margin-bottom: 20px; }

/* --- Answer buttons --- */
.answers { display: flex; flex-direction: column; gap: 10px; }
.answer-btn {
  background: rgba(50,50,85,0.7); border: 1px solid #444; border-radius: 8px;
  padding: 14px 18px; color: #ccc; font-size: 15px; cursor: pointer;
  transition: all 0.2s ease; text-align: left;
}
.answer-btn:hover { border-color: #888; background: rgba(60,60,100,0.8); color: #eee; }
.answer-btn.know   { border-left: 4px solid #4CAF50; }
.answer-btn.heard  { border-left: 4px solid #FFC107; }
.answer-btn.no     { border-left: 4px solid #F44336; }

/* --- Transition summary --- */
.round-summary {
  background: rgba(40,40,70,0.6); border: 1px solid #333;
  border-radius: 12px; padding: 28px 24px; margin-bottom: 20px;
  animation: fadeIn 0.3s ease;
}
.round-summary h2 { margin-bottom: 16px; }
.round-summary p { color: #999; font-size: 14px; line-height: 1.6; margin-bottom: 16px; }

.stage-badge {
  display: inline-block; padding: 6px 14px; border-radius: 16px;
  font-size: 14px; font-weight: 600; margin-bottom: 16px;
}

.continue-btn {
  display: inline-block; padding: 12px 28px; border-radius: 8px;
  background: #3a3a7a; border: 1px solid #555; color: #eee;
  font-size: 15px; cursor: pointer; transition: all 0.2s;
}
.continue-btn:hover { background: #4a4a8a; border-color: #777; }

/* --- Domain sweep summary --- */
.domain-grid {
  display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 10px; margin-bottom: 20px;
}
.domain-chip {
  padding: 10px 14px; border-radius: 8px; font-size: 13px;
  background: rgba(50,50,85,0.7); border: 1px solid #444;
}
.domain-chip.strong  { border-left: 4px solid #4CAF50; }
.domain-chip.familiar { border-left: 4px solid #FFC107; }
.domain-chip.weak    { border-left: 4px solid #666; }
.domain-chip .name { color: #ddd; font-weight: 600; }
.domain-chip .level { color: #888; font-size: 11px; margin-top: 2px; }

/* --- Results screen --- */
.results-grid {
  display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 14px; margin-bottom: 28px;
}
.result-card {
  background: rgba(40,40,70,0.6); border: 1px solid #333;
  border-radius: 10px; padding: 18px 20px;
  transition: border-color 0.2s;
}
.result-card:hover { border-color: #555; }
.result-card .domain-name { color: #ddd; font-size: 16px; font-weight: 600; margin-bottom: 6px; }
.result-card .stage-label { font-size: 12px; font-weight: 600; padding: 3px 10px; border-radius: 10px; display: inline-block; margin-bottom: 8px; }
.result-card .topics-ahead { color: #777; font-size: 12px; }

.stage-pre-formal          { background: rgba(76,175,80,0.2); color: #4CAF50; }
.stage-concrete-operations { background: rgba(139,195,74,0.2); color: #8BC34A; }
.stage-abstract-reasoning  { background: rgba(255,193,7,0.2); color: #FFC107; }
.stage-formal-systems      { background: rgba(255,152,0,0.2); color: #FF9800; }
.stage-advanced            { background: rgba(244,67,54,0.2); color: #F44336; }
.stage-unknown             { background: rgba(100,100,100,0.2); color: #888; }

/* stage borders for result cards */
.border-pre-formal          { border-left: 4px solid #4CAF50; }
.border-concrete-operations { border-left: 4px solid #8BC34A; }
.border-abstract-reasoning  { border-left: 4px solid #FFC107; }
.border-formal-systems      { border-left: 4px solid #FF9800; }
.border-advanced            { border-left: 4px solid #F44336; }
.border-unknown             { border-left: 4px solid #555; }

/* --- Links --- */
.link-row { display: flex; gap: 12px; flex-wrap: wrap; margin-top: 24px; }
.link-btn {
  display: inline-block; padding: 10px 20px;
  background: #2a2a5a; border: 1px solid #555; border-radius: 6px;
  color: #ccc; text-decoration: none; font-size: 14px;
  transition: all 0.2s;
}
.link-btn:hover { background: #3a3a6a; border-color: #777; }

/* --- Intro --- */
.intro-features { list-style: none; margin: 20px 0 28px; }
.intro-features li {
  color: #aaa; font-size: 14px; line-height: 1.8;
  padding-left: 20px; position: relative;
}
.intro-features li::before {
  content: "\\2022"; color: #FFC107; position: absolute; left: 0;
}

/* --- Loading / Error --- */
.loading { text-align: center; padding: 60px 0; }
.loading .spinner {
  width: 36px; height: 36px; border: 3px solid #333;
  border-top-color: #FFC107; border-radius: 50%;
  animation: spin 0.8s linear infinite; margin: 0 auto 16px;
}
@keyframes spin { to { transform: rotate(360deg); } }
.error-msg { color: #F44336; background: rgba(244,67,54,0.1); padding: 16px; border-radius: 8px; }

/* --- Mobile --- */
@media (max-width: 600px) {
  .container { padding: 24px 14px; }
  h1 { font-size: 22px; }
  .topic-card { padding: 20px 16px; }
  .results-grid { grid-template-columns: 1fr; }
  .domain-grid { grid-template-columns: 1fr 1fr; }
}
"""


def _js() -> str:
    return r"""
'use strict';

// ============================================================
// Constants
// ============================================================
const STAGES_ORDERED = [
  'pre-formal',
  'concrete-operations',
  'abstract-reasoning',
  'formal-systems',
  'advanced'
];

const STAGE_LABELS = {
  'pre-formal':          'Pre-Formal',
  'concrete-operations': 'Concrete Operations',
  'abstract-reasoning':  'Abstract Reasoning',
  'formal-systems':      'Formal Systems',
  'advanced':            'Advanced'
};

const STAGE_COLORS = {
  'pre-formal':          '#4CAF50',
  'concrete-operations': '#8BC34A',
  'abstract-reasoning':  '#FFC107',
  'formal-systems':      '#FF9800',
  'advanced':            '#F44336'
};

const LOCALSTORAGE_KEY = 'okg-assessment-results';

// ============================================================
// State
// ============================================================
let DATA = null;
let STATE = {
  phase: 'loading',        // loading | intro | r1 | r1-summary | r2 | r2-summary | r3 | results
  estimatedStage: null,    // index into STAGES_ORDERED after round 1
  r1Questions: [],         // [{topic, answer}]
  r1Index: 0,
  r1Low: 0,                // binary search bounds (stage indices)
  r1High: 4,
  r1CurrentTopic: null,    // {topic, stageIndex} — currently displayed R1 topic
  shownTopicIds: new Set(), // track all shown topic IDs across all rounds
  domainResults: {},       // domain -> 'strong' | 'familiar' | 'weak'
  r2Queue: [],             // [{domain, topic}]
  r2Index: 0,
  r3Queue: [],             // [{domain, chain, low, high, current, done, answer}]
  r3Index: 0,
  frontierResults: {},     // domain -> {stageIndex, topicsAhead}
};

// ============================================================
// Rendering helpers
// ============================================================
const $ = (id) => document.getElementById(id);
const app = () => document.getElementById('app');

function h(tag, attrs, ...children) {
  const el = document.createElement(tag);
  if (attrs) {
    for (const [k, v] of Object.entries(attrs)) {
      if (k === 'className') el.className = v;
      else if (k.startsWith('on')) el.addEventListener(k.slice(2).toLowerCase(), v);
      else if (k === 'style' && typeof v === 'object') Object.assign(el.style, v);
      else if (k === 'innerHTML') el.innerHTML = v;
      else el.setAttribute(k, v);
    }
  }
  for (const c of children) {
    if (typeof c === 'string') el.appendChild(document.createTextNode(c));
    else if (c) el.appendChild(c);
  }
  return el;
}

function setContent(el) {
  app().innerHTML = '';
  app().appendChild(el);
}

// ============================================================
// Data loading
// ============================================================
function loadData() {
  if (EMBEDDED_DATA) {
    DATA = EMBEDDED_DATA;
    checkSavedResults();
  } else {
    STATE.phase = 'error';
    render();
    console.error('No embedded assessment data found');
  }
}

function checkSavedResults() {
  const saved = localStorage.getItem(LOCALSTORAGE_KEY);
  if (saved) {
    try {
      const parsed = JSON.parse(saved);
      if (parsed && parsed.domainResults && parsed.frontierResults) {
        STATE.domainResults = parsed.domainResults;
        STATE.frontierResults = parsed.frontierResults;
        STATE.estimatedStage = parsed.estimatedStage;
        STATE.phase = 'results';
        render();
        return;
      }
    } catch (e) { /* ignore corrupted data */ }
  }
  STATE.phase = 'intro';
  render();
}

// ============================================================
// Phase: Intro
// ============================================================
function renderIntro() {
  const wrap = h('div', { className: 'container' },
    h('h1', null, 'Knowledge Placement Assessment'),
    h('p', { className: 'subtitle' }, 'Find your place on the knowledge graph (~5 minutes)'),
    h('div', { className: 'topic-card' },
      h('p', { className: 'topic-desc' },
        'This adaptive assessment estimates your knowledge level across ' +
        Object.keys(DATA.domain_probes).length + ' domains and ' +
        DATA.total_topics.toLocaleString() + ' topics. It takes about 5 minutes.'
      ),
      h('ul', { className: 'intro-features' },
        h('li', null, 'Round 1: Calibrate your general level (~5 questions)'),
        h('li', null, 'Round 2: Sweep all domains to find strengths (~19 questions)'),
        h('li', null, 'Round 3: Pinpoint your frontier in strong domains (~15\u201325 questions)')
      ),
      h('button', {
        className: 'continue-btn',
        onClick: startRound1,
        style: { marginTop: '8px' }
      }, 'Begin Assessment')
    )
  );
  setContent(wrap);
}

// ============================================================
// Phase: Round 1 — Stage Calibration
// ============================================================
function startRound1() {
  STATE.phase = 'r1';
  STATE.r1Questions = [];
  STATE.r1Index = 0;
  STATE.r1Low = 0;
  STATE.r1High = STAGES_ORDERED.length - 1;
  STATE.shownTopicIds = new Set();
  // Pre-select the first R1 topic so render and answer use the same one
  STATE.r1CurrentTopic = getR1Topic();
  if (STATE.r1CurrentTopic) {
    STATE.shownTopicIds.add(STATE.r1CurrentTopic.topic.id);
  }
  render();
}

function getR1Topic() {
  // Binary search: pick middle stage, find a calibration topic at that stage
  const mid = Math.floor((STATE.r1Low + STATE.r1High) / 2);
  const targetStage = STAGES_ORDERED[mid];
  const candidates = DATA.calibration.filter(t => t.stage === targetStage);
  // Avoid repeats: exclude both previously answered and globally shown topics
  const used = new Set(STATE.r1Questions.map(q => q.topic.id));
  const excluded = id => used.has(id) || STATE.shownTopicIds.has(id);
  const available = candidates.filter(t => !excluded(t.id));
  if (available.length > 0) {
    return { topic: available[Math.floor(Math.random() * available.length)], stageIndex: mid };
  }
  // Fallback: pick from adjacent stages
  for (let offset = 1; offset <= 2; offset++) {
    for (const dir of [1, -1]) {
      const idx = mid + dir * offset;
      if (idx >= 0 && idx < STAGES_ORDERED.length) {
        const fallback = DATA.calibration.filter(t => t.stage === STAGES_ORDERED[idx] && !excluded(t.id));
        if (fallback.length > 0) {
          return { topic: fallback[Math.floor(Math.random() * fallback.length)], stageIndex: idx };
        }
      }
    }
  }
  // Absolute fallback
  const any = DATA.calibration.filter(t => !excluded(t.id));
  if (any.length > 0) return { topic: any[0], stageIndex: mid };
  return null;
}

function answerR1(answer) {
  const current = STATE.r1CurrentTopic;
  if (!current) { finishR1(); return; }
  STATE.r1Questions.push({ topic: current.topic, answer, stageIndex: current.stageIndex });

  // Adapt binary search bounds
  if (answer === 'know') {
    // User knows this level — search higher
    STATE.r1Low = Math.min(current.stageIndex + 1, STAGES_ORDERED.length - 1);
  } else if (answer === 'no') {
    // User doesn't know this — search lower
    STATE.r1High = Math.max(current.stageIndex - 1, 0);
  }
  // 'heard' doesn't change bounds — ask another question at same level

  STATE.r1Index++;
  if (STATE.r1Index >= 5 || STATE.r1Low > STATE.r1High) {
    finishR1();
  } else {
    // Pre-select next topic so render and answer stay in sync
    STATE.r1CurrentTopic = getR1Topic();
    if (STATE.r1CurrentTopic) {
      STATE.shownTopicIds.add(STATE.r1CurrentTopic.topic.id);
    }
    render();
  }
}

function finishR1() {
  // Determine estimated stage: highest stage the user claimed to know, or the bracket midpoint
  let highestKnown = -1;
  for (const q of STATE.r1Questions) {
    if (q.answer === 'know') {
      highestKnown = Math.max(highestKnown, q.stageIndex);
    }
  }
  if (highestKnown >= 0) {
    STATE.estimatedStage = Math.min(highestKnown, STAGES_ORDERED.length - 1);
  } else {
    // No "know" answers — estimate from bracket
    STATE.estimatedStage = Math.floor((STATE.r1Low + STATE.r1High) / 2);
  }
  STATE.phase = 'r1-summary';
  render();
}

function renderR1() {
  const current = STATE.r1CurrentTopic;
  if (!current) { finishR1(); return; }

  const totalQ = 5;
  const progress = (STATE.r1Index / totalQ) * 100;

  const wrap = h('div', { className: 'container' },
    h('h1', null, 'Knowledge Placement Assessment'),
    h('p', { className: 'subtitle' }, 'Round 1 of 3 \u2014 Stage Calibration'),
    h('div', { className: 'progress-wrap' },
      h('div', { className: 'progress-bar', style: { width: progress + '%' } })
    ),
    h('span', { className: 'round-label r1' }, 'Round 1 \u2014 Calibration'),
    h('div', { className: 'topic-card' },
      h('div', { className: 'topic-title' }, current.topic.title),
      h('p', { className: 'topic-desc' }, current.topic.description || ''),
      h('p', { className: 'topic-meta' },
        (current.topic.domain ? formatDomain(current.topic.domain) + ' \u00B7 ' : '') +
        STAGE_LABELS[current.topic.stage]
      ),
      h('div', { className: 'answers' },
        h('button', { className: 'answer-btn know', onClick: () => answerR1('know') },
          '\u2705  I know this well'),
        h('button', { className: 'answer-btn heard', onClick: () => answerR1('heard') },
          '\u2753  I\'ve heard of it'),
        h('button', { className: 'answer-btn no', onClick: () => answerR1('no') },
          '\u274C  I don\'t know this')
      )
    ),
    h('p', { style: { color: '#555', fontSize: '12px', marginTop: '8px' } },
      'Question ' + (STATE.r1Index + 1) + ' of ~' + totalQ)
  );
  setContent(wrap);
}

function renderR1Summary() {
  const stage = STAGES_ORDERED[STATE.estimatedStage];
  const color = STAGE_COLORS[stage];

  const wrap = h('div', { className: 'container' },
    h('h1', null, 'Knowledge Placement Assessment'),
    h('p', { className: 'subtitle' }, 'Round 1 Complete'),
    h('div', { className: 'round-summary' },
      h('h2', null, 'Stage Calibration Results'),
      h('p', null, 'Based on your responses, your general knowledge level is approximately:'),
      h('span', { className: 'stage-badge', style: { background: color + '22', color: color } },
        STAGE_LABELS[stage]),
      h('p', null, 'Next, we\'ll check each domain individually to find your strengths.'),
      h('button', { className: 'continue-btn', onClick: startRound2, style: { marginTop: '12px' } },
        'Continue to Round 2')
    )
  );
  setContent(wrap);
}

// ============================================================
// Phase: Round 2 — Domain Sweep
// ============================================================
function startRound2() {
  STATE.phase = 'r2';
  STATE.r2Index = 0;
  STATE.domainResults = {};

  // Build queue: one probe per domain near the estimated stage
  const domains = Object.keys(DATA.domain_probes);
  STATE.r2Queue = [];
  const estStage = STAGES_ORDERED[STATE.estimatedStage];

  for (const domain of domains) {
    const probes = DATA.domain_probes[domain];
    if (!probes || probes.length === 0) continue;

    // Prefer a probe at the estimated stage
    let best = probes.find(p => p.stage === estStage);
    if (!best) {
      // Find closest stage
      let bestDist = Infinity;
      for (const p of probes) {
        const dist = Math.abs(STAGES_ORDERED.indexOf(p.stage) - STATE.estimatedStage);
        if (dist < bestDist) { bestDist = dist; best = p; }
      }
    }
    if (best && !STATE.shownTopicIds.has(best.id)) {
      STATE.r2Queue.push({ domain, topic: best });
    } else if (best) {
      // Preferred probe was already shown; find an alternative
      const alt = probes.find(p => !STATE.shownTopicIds.has(p.id));
      if (alt) STATE.r2Queue.push({ domain, topic: alt });
      else STATE.r2Queue.push({ domain, topic: best }); // last resort: allow repeat
    }
  }
  // Mark the first R2 topic as shown
  if (STATE.r2Queue.length > 0) {
    STATE.shownTopicIds.add(STATE.r2Queue[0].topic.id);
  }
  render();
}

function answerR2(answer) {
  const current = STATE.r2Queue[STATE.r2Index];
  if (answer === 'know') STATE.domainResults[current.domain] = 'strong';
  else if (answer === 'heard') STATE.domainResults[current.domain] = 'familiar';
  else STATE.domainResults[current.domain] = 'weak';

  STATE.r2Index++;
  if (STATE.r2Index >= STATE.r2Queue.length) {
    STATE.phase = 'r2-summary';
  } else {
    // Mark next topic as shown
    STATE.shownTopicIds.add(STATE.r2Queue[STATE.r2Index].topic.id);
  }
  render();
}

function renderR2() {
  const current = STATE.r2Queue[STATE.r2Index];
  if (!current) { STATE.phase = 'r2-summary'; render(); return; }

  const totalQ = STATE.r2Queue.length;
  const overallProgress = ((5 + STATE.r2Index) / (5 + totalQ + 20)) * 100;
  const roundProgress = (STATE.r2Index / totalQ) * 100;

  const wrap = h('div', { className: 'container' },
    h('h1', null, 'Knowledge Placement Assessment'),
    h('p', { className: 'subtitle' }, 'Round 2 of 3 \u2014 Domain Sweep'),
    h('div', { className: 'progress-wrap' },
      h('div', { className: 'progress-bar', style: { width: overallProgress + '%' } })
    ),
    h('span', { className: 'round-label r2' }, 'Round 2 \u2014 Domain Sweep'),
    h('div', { className: 'topic-card' },
      h('h3', { style: { color: '#888', fontSize: '12px', marginBottom: '12px', textTransform: 'uppercase', letterSpacing: '1px' } },
        formatDomain(current.domain)),
      h('div', { className: 'topic-title' }, current.topic.title),
      h('p', { className: 'topic-desc' }, current.topic.description || ''),
      h('p', { className: 'topic-meta' }, STAGE_LABELS[current.topic.stage] || ''),
      h('div', { className: 'answers' },
        h('button', { className: 'answer-btn know', onClick: () => answerR2('know') },
          '\u2705  I know this well'),
        h('button', { className: 'answer-btn heard', onClick: () => answerR2('heard') },
          '\u2753  I\'ve heard of it'),
        h('button', { className: 'answer-btn no', onClick: () => answerR2('no') },
          '\u274C  I don\'t know this')
      )
    ),
    h('p', { style: { color: '#555', fontSize: '12px', marginTop: '8px' } },
      'Domain ' + (STATE.r2Index + 1) + ' of ' + totalQ)
  );
  setContent(wrap);
}

function renderR2Summary() {
  const strong = [], familiar = [], weak = [];
  for (const [domain, level] of Object.entries(STATE.domainResults)) {
    if (level === 'strong') strong.push(domain);
    else if (level === 'familiar') familiar.push(domain);
    else weak.push(domain);
  }

  const makeChips = (domains, cls) =>
    domains.map(d => h('div', { className: 'domain-chip ' + cls },
      h('div', { className: 'name' }, formatDomain(d)),
      h('div', { className: 'level' }, cls === 'strong' ? 'Strong' : cls === 'familiar' ? 'Familiar' : 'New')
    ));

  const chipContainer = h('div', { className: 'domain-grid' },
    ...makeChips(strong, 'strong'),
    ...makeChips(familiar, 'familiar'),
    ...makeChips(weak, 'weak')
  );

  const summaryParts = [];
  if (strong.length > 0) summaryParts.push('Strong in: ' + strong.map(formatDomain).join(', '));
  if (familiar.length > 0) summaryParts.push('Exploring: ' + familiar.map(formatDomain).join(', '));
  if (weak.length > 0) summaryParts.push('New to: ' + weak.map(formatDomain).join(', '));

  const hasStrongDomains = strong.length > 0;

  const wrap = h('div', { className: 'container' },
    h('h1', null, 'Knowledge Placement Assessment'),
    h('p', { className: 'subtitle' }, 'Round 2 Complete'),
    h('div', { className: 'round-summary' },
      h('h2', null, 'Domain Sweep Results'),
      chipContainer,
      h('p', { style: { color: '#999', fontSize: '13px', lineHeight: '1.6' } }, summaryParts.join('. ') + '.'),
      h('p', { style: { marginTop: '12px' } },
        hasStrongDomains
          ? 'Now let\'s find exactly where your knowledge frontier is in your strong domains.'
          : 'Assessment complete! Here are your results.'
      ),
      h('button', {
        className: 'continue-btn',
        onClick: hasStrongDomains ? startRound3 : showResults,
        style: { marginTop: '12px' }
      }, hasStrongDomains ? 'Continue to Round 3' : 'View Results')
    )
  );
  setContent(wrap);
}

// ============================================================
// Phase: Round 3 — Frontier Finding
// ============================================================
function startRound3() {
  STATE.phase = 'r3';
  STATE.r3Queue = [];
  STATE.r3Index = 0;
  STATE.frontierResults = {};

  const strongDomains = Object.entries(STATE.domainResults)
    .filter(([_, level]) => level === 'strong')
    .map(([domain]) => domain);

  for (const domain of strongDomains) {
    const chains = DATA.frontier_chains[domain];
    if (!chains || chains.length === 0) {
      // No chain data — mark at estimated stage
      STATE.frontierResults[domain] = {
        stage: STAGES_ORDERED[STATE.estimatedStage],
        stageIndex: STATE.estimatedStage
      };
      continue;
    }
    // Pick the longest chain for best binary search resolution
    const chain = chains.reduce((a, b) => a.length >= b.length ? a : b, chains[0]);
    const low = 0;
    const high = chain.length - 1;
    const mid = Math.floor((low + high) / 2);
    STATE.r3Queue.push({
      domain,
      chain,
      low,
      high,
      current: mid,
      steps: 0,
      maxSteps: Math.ceil(Math.log2(chain.length + 1)) + 1,
      lastKnown: -1   // index of last known topic in chain
    });
  }

  if (STATE.r3Queue.length === 0) {
    showResults();
    return;
  }
  render();
}

function getR3TopicInfo(topicId) {
  // Look up topic info from calibration or domain_probes
  for (const t of DATA.calibration) {
    if (t.id === topicId) return t;
  }
  for (const probes of Object.values(DATA.domain_probes)) {
    for (const t of probes) {
      if (t.id === topicId) return t;
    }
  }
  // Return minimal info
  return { id: topicId, title: topicId.replace(/-/g, ' ').replace(/\b\w/g, c => c.toUpperCase()), description: '', stage: '' };
}

function answerR3(answer) {
  const item = STATE.r3Queue[STATE.r3Index];
  item.steps++;

  if (answer === 'know') {
    item.lastKnown = Math.max(item.lastKnown, item.current);
    item.low = item.current + 1;
  } else if (answer === 'no') {
    item.high = item.current - 1;
  } else {
    // 'heard' — treat as partial, move slightly lower
    item.lastKnown = Math.max(item.lastKnown, item.current - 1);
    item.high = item.current;
    // Avoid getting stuck: if high == current, decrement
    if (item.low >= item.high) {
      item.lastKnown = Math.max(item.lastKnown, item.current - 1);
    }
  }

  // Check if done (converged or max steps)
  if (item.low > item.high || item.steps >= item.maxSteps) {
    // Record frontier for this domain
    const frontierIdx = item.lastKnown >= 0 ? item.lastKnown : -1;
    const topicsAhead = item.chain.length - (frontierIdx + 1);

    // Estimate stage from the frontier topic
    let stage = STAGES_ORDERED[STATE.estimatedStage];
    if (frontierIdx >= 0) {
      const frontierTopic = getR3TopicInfo(item.chain[frontierIdx]);
      if (frontierTopic.stage) stage = frontierTopic.stage;
    }

    STATE.frontierResults[item.domain] = {
      stage,
      stageIndex: STAGES_ORDERED.indexOf(stage),
      topicsAhead,
      frontierTopicId: frontierIdx >= 0 ? item.chain[frontierIdx] : null
    };

    STATE.r3Index++;
    if (STATE.r3Index >= STATE.r3Queue.length) {
      showResults();
      return;
    }
  } else {
    item.current = Math.floor((item.low + item.high) / 2);
  }

  render();
}

function renderR3() {
  const item = STATE.r3Queue[STATE.r3Index];
  if (!item) { showResults(); return; }

  const topicId = item.chain[item.current];
  STATE.shownTopicIds.add(topicId);
  const topicInfo = getR3TopicInfo(topicId);

  const totalR3 = STATE.r3Queue.reduce((s, q) => s + q.maxSteps, 0);
  const doneR3 = STATE.r3Queue.slice(0, STATE.r3Index).reduce((s, q) => s + q.steps, 0) + item.steps;
  const totalAll = 5 + STATE.r2Queue.length + totalR3;
  const doneAll = 5 + STATE.r2Queue.length + doneR3;
  const overallProgress = (doneAll / totalAll) * 100;

  const wrap = h('div', { className: 'container' },
    h('h1', null, 'Knowledge Placement Assessment'),
    h('p', { className: 'subtitle' }, 'Round 3 of 3 \u2014 Frontier Finding'),
    h('div', { className: 'progress-wrap' },
      h('div', { className: 'progress-bar', style: { width: overallProgress + '%' } })
    ),
    h('span', { className: 'round-label r3' }, 'Round 3 \u2014 Frontier'),
    h('div', { className: 'topic-card' },
      h('h3', { style: { color: '#888', fontSize: '12px', marginBottom: '12px', textTransform: 'uppercase', letterSpacing: '1px' } },
        formatDomain(item.domain) + ' \u2014 Finding your frontier'),
      h('div', { className: 'topic-title' }, topicInfo.title),
      h('p', { className: 'topic-desc' }, topicInfo.description || ''),
      h('p', { className: 'topic-meta' },
        (topicInfo.stage ? STAGE_LABELS[topicInfo.stage] || '' : '') +
        (topicInfo.course ? ' \u00B7 ' + formatCourse(topicInfo.course) : '')
      ),
      h('div', { className: 'answers' },
        h('button', { className: 'answer-btn know', onClick: () => answerR3('know') },
          '\u2705  I know this well'),
        h('button', { className: 'answer-btn heard', onClick: () => answerR3('heard') },
          '\u2753  I\'ve heard of it'),
        h('button', { className: 'answer-btn no', onClick: () => answerR3('no') },
          '\u274C  I don\'t know this')
      )
    ),
    h('p', { style: { color: '#555', fontSize: '12px', marginTop: '8px' } },
      'Domain ' + (STATE.r3Index + 1) + ' of ' + STATE.r3Queue.length +
      ' \u00B7 Step ' + (item.steps + 1) + ' of ~' + item.maxSteps)
  );
  setContent(wrap);
}

// ============================================================
// Phase: Results
// ============================================================
function showResults() {
  // Fill in results for non-strong domains
  for (const [domain, level] of Object.entries(STATE.domainResults)) {
    if (!STATE.frontierResults[domain]) {
      let stageIdx;
      if (level === 'familiar') {
        stageIdx = Math.max(0, STATE.estimatedStage - 1);
      } else {
        stageIdx = 0; // weak — start from the beginning
      }
      STATE.frontierResults[domain] = {
        stage: STAGES_ORDERED[stageIdx],
        stageIndex: stageIdx,
        topicsAhead: null // unknown without chain data
      };
    }
  }

  // Save to localStorage
  localStorage.setItem(LOCALSTORAGE_KEY, JSON.stringify({
    domainResults: STATE.domainResults,
    frontierResults: STATE.frontierResults,
    estimatedStage: STATE.estimatedStage,
    timestamp: new Date().toISOString()
  }));

  STATE.phase = 'results';
  render();
}

function renderResults() {
  // Sort domains: strong first, then familiar, then weak
  const order = { strong: 0, familiar: 1, weak: 2 };
  const sortedDomains = Object.keys(STATE.frontierResults).sort((a, b) => {
    const la = STATE.domainResults[a] || 'weak';
    const lb = STATE.domainResults[b] || 'weak';
    if (order[la] !== order[lb]) return order[la] - order[lb];
    return (STATE.frontierResults[b].stageIndex || 0) - (STATE.frontierResults[a].stageIndex || 0);
  });

  const cards = sortedDomains.map(domain => {
    const fr = STATE.frontierResults[domain];
    const stage = fr.stage || 'pre-formal';
    const stageCls = 'stage-' + stage;
    const borderCls = 'border-' + stage;
    const level = STATE.domainResults[domain] || 'weak';

    let aheadText = '';
    if (fr.topicsAhead !== null && fr.topicsAhead !== undefined) {
      aheadText = fr.topicsAhead + ' topics ahead';
    } else {
      aheadText = level === 'weak' ? 'Entire domain to explore' : 'Many topics to explore';
    }

    return h('div', { className: 'result-card ' + borderCls },
      h('div', { className: 'domain-name' }, formatDomain(domain)),
      h('span', { className: 'stage-label ' + stageCls }, STAGE_LABELS[stage] || stage),
      h('div', { className: 'topics-ahead' }, aheadText)
    );
  });

  // Find frontier suggestions (strong domains)
  const frontierTopics = [];
  for (const domain of sortedDomains) {
    const fr = STATE.frontierResults[domain];
    if (STATE.domainResults[domain] === 'strong' && fr.frontierTopicId) {
      const info = getR3TopicInfo(fr.frontierTopicId);
      frontierTopics.push({ domain, topic: info });
    }
  }

  const startLearningSection = frontierTopics.length > 0
    ? h('div', { className: 'round-summary', style: { marginTop: '24px' } },
        h('h2', null, 'Start Learning'),
        h('p', null, 'Pick up where you left off in your strongest domains:'),
        h('div', { style: { display: 'flex', flexDirection: 'column', gap: '8px', marginTop: '12px' } },
          ...frontierTopics.map(ft =>
            h('a', {
              href: 'topics/' + ft.topic.id + '.html',
              className: 'link-btn',
              style: { textAlign: 'left' }
            },
              formatDomain(ft.domain) + ': ' + ft.topic.title
            )
          )
        )
      )
    : null;

  const wrap = h('div', { className: 'container' },
    h('h1', null, 'Your Knowledge Profile'),
    h('p', { className: 'subtitle' },
      'Assessment complete \u2014 ' + sortedDomains.length + ' domains mapped'),
    h('div', { className: 'results-grid' }, ...cards),
    startLearningSection,
    h('div', { className: 'link-row' },
      h('a', { href: 'index.html', className: 'link-btn' }, 'Browse Knowledge Graph'),
      h('a', { href: 'radial-graph.html', className: 'link-btn', style: { background: '#3a2a6a' } },
        'View Radial Graph'),
      h('button', {
        className: 'link-btn',
        onClick: retakeAssessment,
        style: { background: 'rgba(244,67,54,0.15)', borderColor: '#F44336', color: '#F44336', cursor: 'pointer' }
      }, 'Retake Assessment')
    )
  );
  setContent(wrap);
}

function retakeAssessment() {
  localStorage.removeItem(LOCALSTORAGE_KEY);
  STATE = {
    phase: 'intro',
    estimatedStage: null,
    r1Questions: [],
    r1Index: 0,
    r1Low: 0,
    r1High: 4,
    r1CurrentTopic: null,
    shownTopicIds: new Set(),
    domainResults: {},
    r2Queue: [],
    r2Index: 0,
    r3Queue: [],
    r3Index: 0,
    frontierResults: {},
  };
  render();
}

// ============================================================
// Utilities
// ============================================================
function formatDomain(slug) {
  return slug.replace(/-/g, ' ').replace(/\band\b/g, '&')
    .replace(/\b\w/g, c => c.toUpperCase());
}

function formatCourse(slug) {
  return slug.replace(/-/g, ' ').replace(/\b\w/g, c => c.toUpperCase());
}

// ============================================================
// Main render dispatcher
// ============================================================
function render() {
  switch (STATE.phase) {
    case 'loading':
      setContent(h('div', { className: 'container' },
        h('div', { className: 'loading' },
          h('div', { className: 'spinner' }),
          h('p', null, 'Loading assessment data...')
        )
      ));
      break;
    case 'error':
      setContent(h('div', { className: 'container' },
        h('h1', null, 'Knowledge Placement Assessment'),
        h('p', { className: 'subtitle' }, 'Find your place on the knowledge graph'),
        h('div', { className: 'error-msg' },
          'Failed to load assessment-data.json. Make sure the file exists in the same directory as this page.'
        )
      ));
      break;
    case 'intro':     renderIntro(); break;
    case 'r1':        renderR1(); break;
    case 'r1-summary': renderR1Summary(); break;
    case 'r2':        renderR2(); break;
    case 'r2-summary': renderR2Summary(); break;
    case 'r3':        renderR3(); break;
    case 'results':   renderResults(); break;
  }
}

// ============================================================
// Boot
// ============================================================
render();
loadData();
"""


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    html = generate_assessment_html()
    out_path = OUTPUT_DIR / "assessment.html"
    out_path.write_text(html, encoding="utf-8")
    print(f"Generated {out_path} ({len(html):,} bytes)")


if __name__ == "__main__":
    main()
