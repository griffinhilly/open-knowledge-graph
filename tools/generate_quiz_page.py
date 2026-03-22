#!/usr/bin/env python3
"""Generate the interactive quiz page for the OKG learning platform.

Reads assessment-questions.json and lib/fluency.js, then generates
output/quiz.html — a self-contained adaptive quiz that feeds answers
into the fluency model.

Phase 1 (Warm-Up): Cross-domain MC/TF rotation, pre-formal to concrete.
Phase 2 (Exploration): Per-domain adaptive questioning, all stages.
Results: Fluency summary with links to the knowledge graph.

Usage:
    python tools/generate_quiz_page.py
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "output"
LIB_DIR = ROOT / "lib"


def generate_quiz_html() -> str:
    """Generate the complete quiz HTML page with embedded data and fluency engine."""
    # Load question data
    data_path = OUTPUT_DIR / "assessment-questions.json"
    if data_path.exists():
        embedded_data = data_path.read_text(encoding="utf-8")
    else:
        embedded_data = "null"
        print("WARNING: assessment-questions.json not found, embedding null")

    # Load fluency engine
    fluency_path = LIB_DIR / "fluency.js"
    if fluency_path.exists():
        fluency_js = fluency_path.read_text(encoding="utf-8")
    else:
        fluency_js = "const OKGFluency = null;"
        print("WARNING: fluency.js not found, fluency tracking disabled")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Knowledge Trivia — Open Knowledge Graph</title>
<style>
{_css()}
</style>
</head>
<body>

<div id="app"></div>

<script>
// --- Fluency Engine (embedded) ---
{fluency_js}
</script>

<script>
// --- Quiz Data (embedded) ---
const DATA = {embedded_data};

// --- Quiz Application ---
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

.container {
  max-width: 720px; margin: 0 auto; padding: 40px 20px;
}

h1 { color: #eee; font-size: 28px; margin-bottom: 6px; }
h2 { color: #ddd; font-size: 22px; margin-bottom: 12px; }
.subtitle { color: #777; font-size: 14px; margin-bottom: 32px; }

/* --- Progress bar --- */
.progress-wrap {
  background: rgba(40,40,70,0.6); border-radius: 8px;
  height: 8px; margin-bottom: 24px; overflow: hidden;
}
.progress-bar {
  height: 100%; border-radius: 8px;
  background: linear-gradient(90deg, #4a9eff, #7c4dff);
  transition: width 0.4s ease;
}

/* --- Phase label --- */
.phase-label {
  display: inline-block; padding: 4px 12px; border-radius: 12px;
  font-size: 11px; font-weight: 600; letter-spacing: 0.5px; text-transform: uppercase;
  margin-bottom: 16px;
}
.phase-label.warmup { background: rgba(74,158,255,0.15); color: #4a9eff; }
.phase-label.explore { background: rgba(124,77,255,0.15); color: #7c4dff; }

/* --- Domain tag --- */
.domain-tag {
  display: inline-block; padding: 3px 10px; border-radius: 10px;
  font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px;
  margin-bottom: 14px; background: rgba(255,255,255,0.08); color: #999;
}

/* --- Question card --- */
.question-card {
  background: rgba(40,40,70,0.6); border: 1px solid #333;
  border-radius: 12px; padding: 28px 24px; margin-bottom: 20px;
  animation: fadeIn 0.3s ease;
  transition: border-color 0.3s;
}
.question-card.correct { border-color: #4CAF50; }
.question-card.wrong { border-color: #F44336; }

@keyframes fadeIn { from { opacity:0; transform:translateY(8px); } to { opacity:1; transform:translateY(0); } }

.question-text {
  color: #eee; font-size: 17px; line-height: 1.6; margin-bottom: 20px;
}

/* --- Answer buttons --- */
.answers { display: flex; flex-direction: column; gap: 10px; }

.answer-btn {
  background: rgba(50,50,85,0.7); border: 1px solid #444; border-radius: 8px;
  padding: 14px 18px; color: #ccc; font-size: 15px; cursor: pointer;
  transition: all 0.2s ease; text-align: left; position: relative;
}
.answer-btn:hover:not(.disabled) { border-color: #888; background: rgba(60,60,100,0.8); color: #eee; }
.answer-btn.disabled { cursor: default; opacity: 0.7; }
.answer-btn.selected { border-color: #7c4dff; background: rgba(124,77,255,0.15); }
.answer-btn.correct-answer { border-color: #4CAF50; background: rgba(76,175,80,0.15); color: #eee; }
.answer-btn.wrong-answer { border-color: #F44336; background: rgba(244,67,54,0.12); }

.answer-letter {
  display: inline-block; width: 28px; height: 28px; line-height: 28px;
  text-align: center; border-radius: 50%; margin-right: 12px;
  background: rgba(255,255,255,0.08); color: #888; font-weight: 600; font-size: 13px;
}
.answer-btn.correct-answer .answer-letter { background: rgba(76,175,80,0.3); color: #4CAF50; }
.answer-btn.wrong-answer .answer-letter { background: rgba(244,67,54,0.3); color: #F44336; }

/* --- TF buttons --- */
.tf-buttons { display: flex; gap: 12px; }
.tf-btn {
  flex: 1; padding: 16px; border-radius: 8px; font-size: 16px; font-weight: 600;
  cursor: pointer; transition: all 0.2s; text-align: center;
  background: rgba(50,50,85,0.7); border: 1px solid #444; color: #ccc;
}
.tf-btn:hover:not(.disabled) { border-color: #888; }
.tf-btn.disabled { cursor: default; opacity: 0.7; }
.tf-btn.selected { border-color: #7c4dff; background: rgba(124,77,255,0.15); }
.tf-btn.correct-answer { border-color: #4CAF50; background: rgba(76,175,80,0.15); color: #4CAF50; }
.tf-btn.wrong-answer { border-color: #F44336; background: rgba(244,67,54,0.12); color: #F44336; }

/* --- Feedback --- */
.feedback {
  margin-top: 16px; padding: 14px 16px; border-radius: 8px;
  font-size: 13px; line-height: 1.6;
  animation: fadeIn 0.2s ease;
}
.feedback.correct { background: rgba(76,175,80,0.1); border: 1px solid rgba(76,175,80,0.3); color: #a5d6a7; }
.feedback.wrong { background: rgba(244,67,54,0.08); border: 1px solid rgba(244,67,54,0.25); color: #ef9a9a; }
.feedback-icon { font-size: 16px; margin-right: 6px; }

/* --- Next button --- */
.next-btn {
  display: inline-block; margin-top: 16px; padding: 10px 24px; border-radius: 8px;
  background: #3a3a7a; border: 1px solid #555; color: #eee;
  font-size: 14px; cursor: pointer; transition: all 0.2s;
}
.next-btn:hover { background: #4a4a8a; border-color: #777; }

/* --- Action buttons row --- */
.action-row {
  display: flex; gap: 10px; flex-wrap: wrap; margin-top: 12px;
}
.action-btn {
  padding: 8px 16px; border-radius: 6px; font-size: 13px;
  cursor: pointer; transition: all 0.2s; border: 1px solid #444;
  background: rgba(50,50,85,0.5); color: #999;
}
.action-btn:hover { border-color: #777; color: #ccc; }
.action-btn.primary {
  background: #3a3a7a; border-color: #555; color: #eee;
}
.action-btn.primary:hover { background: #4a4a8a; }

/* --- Score display --- */
.score-display {
  display: inline-block; padding: 3px 10px; border-radius: 10px;
  font-size: 12px; font-weight: 600; margin-left: 8px;
  background: rgba(255,255,255,0.06); color: #888;
}

/* --- Intro card --- */
.intro-card {
  background: rgba(40,40,70,0.6); border: 1px solid #333;
  border-radius: 12px; padding: 32px 28px; margin-bottom: 20px;
}
.intro-features { list-style: none; margin: 20px 0 24px; }
.intro-features li {
  color: #aaa; font-size: 14px; line-height: 2;
  padding-left: 24px; position: relative;
}
.intro-features li::before {
  content: attr(data-icon); position: absolute; left: 0;
}

/* --- Domain picker grid --- */
.domain-grid {
  display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 12px; margin-bottom: 24px;
}
.domain-card {
  background: rgba(40,40,70,0.6); border: 1px solid #333;
  border-radius: 10px; padding: 16px 18px; cursor: pointer;
  transition: all 0.2s;
}
.domain-card:hover { border-color: #666; background: rgba(50,50,90,0.6); }
.domain-card.strong { border-left: 4px solid #4CAF50; }
.domain-card.familiar { border-left: 4px solid #FFC107; }
.domain-card.weak { border-left: 4px solid #555; }
.domain-card.explored { opacity: 0.5; }
.domain-card .name { color: #ddd; font-weight: 600; font-size: 14px; margin-bottom: 4px; }
.domain-card .info { color: #777; font-size: 12px; }
.domain-card .bar { height: 3px; border-radius: 2px; margin-top: 8px; background: rgba(255,255,255,0.06); overflow: hidden; }
.domain-card .bar-fill { height: 100%; border-radius: 2px; transition: width 0.3s; }

/* --- Results --- */
.results-grid {
  display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 12px; margin-bottom: 24px;
}
.result-card {
  background: rgba(40,40,70,0.6); border: 1px solid #333;
  border-radius: 10px; padding: 16px 18px;
}
.result-card .domain-name { color: #ddd; font-size: 14px; font-weight: 600; margin-bottom: 4px; }
.result-card .score { font-size: 24px; font-weight: 700; margin-bottom: 2px; }
.result-card .detail { color: #777; font-size: 12px; }

.stat-bar {
  display: flex; align-items: center; gap: 12px; margin-bottom: 10px;
}
.stat-bar .label { color: #999; font-size: 13px; min-width: 100px; }
.stat-bar .bar { flex: 1; height: 8px; border-radius: 4px; background: rgba(255,255,255,0.06); overflow: hidden; }
.stat-bar .bar-fill { height: 100%; border-radius: 4px; }
.stat-bar .value { color: #ccc; font-size: 13px; font-weight: 600; min-width: 40px; text-align: right; }

/* --- Summary card --- */
.summary-card {
  background: rgba(40,40,70,0.6); border: 1px solid #333;
  border-radius: 12px; padding: 28px 24px; margin-bottom: 20px;
}

/* --- Links --- */
.link-row { display: flex; gap: 12px; flex-wrap: wrap; margin-top: 24px; }
.link-btn {
  display: inline-block; padding: 10px 20px;
  background: #2a2a5a; border: 1px solid #555; border-radius: 6px;
  color: #ccc; text-decoration: none; font-size: 14px;
  transition: all 0.2s; cursor: pointer;
}
.link-btn:hover { background: #3a3a6a; border-color: #777; color: #eee; }

/* --- Mobile --- */
@media (max-width: 600px) {
  .container { padding: 24px 14px; }
  h1 { font-size: 22px; }
  .question-card { padding: 20px 16px; }
  .question-text { font-size: 15px; }
  .results-grid { grid-template-columns: 1fr; }
  .domain-grid { grid-template-columns: 1fr 1fr; }
  .tf-buttons { flex-direction: column; }
}
"""


def _js() -> str:
    return r"""
'use strict';

// ============================================================
// Constants
// ============================================================
const EXPLORE_PER_DOMAIN = 7;     // questions per domain visit
const TIER_QUESTIONS = 3;         // questions per stage tier before escalation check
const TIER_PROMOTE = 0.6;         // 60%+ correct at a tier → escalate
// No auto-advance — user clicks "Next" manually to avoid misclicks

const STAGES_ORDERED = [
  'pre-formal', 'concrete-operations', 'abstract-reasoning',
  'formal-systems', 'advanced'
];
const STAGE_LABELS = {
  'pre-formal':          'Pre-Formal',
  'concrete-operations': 'Concrete Operations',
  'abstract-reasoning':  'Abstract Reasoning',
  'formal-systems':      'Formal Systems',
  'advanced':            'Advanced'
};

const DOMAIN_ORDER = [
  'mathematics', 'formal-sciences-and-logic', 'philosophy', 'computer-science',
  'engineering', 'physics', 'earth-and-space-sciences', 'chemistry', 'biology',
  'health-and-human-development', 'psychology', 'social-sciences', 'economics',
  'practical-life-skills', 'history', 'language-and-communication', 'literature',
  'arts-and-aesthetics', 'music'
];

// Median response times (ms) for evidence weighting
const MEDIAN_MC = 12000;
const MEDIAN_TF = 8000;

// ============================================================
// State
// ============================================================
let S = {
  phase: 'loading',
  // Warmup (adaptive tier escalation)
  warmupPools: {},      // stage -> [questions]
  warmupTier: 0,        // current stage index (0=pre-formal ... 4=advanced)
  warmupTierIndex: 0,   // questions asked at current tier
  warmupTierCorrect: 0, // correct at current tier
  warmupAnswers: [],     // {topicId, domain, correct, responseTimeMs, stage}
  warmupDone: false,
  questionStart: null,
  showingFeedback: false,
  feedbackTimer: null,
  // Exploration
  exploreDomain: null,
  exploreQueue: [],
  exploreIndex: 0,
  exploreAnswers: [],
  exploredDomains: {},  // domain -> {correct, total}
  skippedDomains: {},
  // Tracking
  usedQuestionKeys: {},  // "topicId::question" -> true
};

// ============================================================
// Rendering helpers
// ============================================================
const app = () => document.getElementById('app');

function h(tag, attrs, ...children) {
  const el = document.createElement(tag);
  if (attrs) {
    for (const [k, v] of Object.entries(attrs)) {
      if (k === 'className') el.className = v;
      else if (k.startsWith('on') && typeof v === 'function') el.addEventListener(k.slice(2).toLowerCase(), v);
      else if (k === 'style' && typeof v === 'object') Object.assign(el.style, v);
      else if (k === 'innerHTML') el.innerHTML = v;
      else el.setAttribute(k, v);
    }
  }
  for (const c of children.flat()) {
    if (c == null || c === false) continue;
    if (typeof c === 'string' || typeof c === 'number') el.appendChild(document.createTextNode(c));
    else if (c instanceof Node) el.appendChild(c);
  }
  return el;
}

function setContent(el) {
  app().innerHTML = '';
  app().appendChild(el);
}

function formatDomain(slug) {
  return slug.replace(/-/g, ' ').replace(/\band\b/g, '&')
    .replace(/\b\w/g, c => c.toUpperCase());
}

function qKey(q) { return q.topicId + '::' + q.question.slice(0, 60); }

// ============================================================
// Shuffle
// ============================================================
function shuffle(arr) {
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

// ============================================================
// Build warmup pools: one shuffled pool per stage tier
// ============================================================
function buildWarmupPools() {
  const pools = {};
  for (const q of DATA.warmup) {
    if (!pools[q.stage]) pools[q.stage] = [];
    pools[q.stage].push(q);
  }
  // Also pull exploration questions into pools as overflow
  for (const domain in DATA.exploration) {
    for (const q of DATA.exploration[domain]) {
      if (!pools[q.stage]) pools[q.stage] = [];
      pools[q.stage].push(q);
    }
  }
  // Shuffle each pool, rotating domains for variety
  for (const stage in pools) {
    // Sort by domain first, then interleave
    const byDomain = {};
    for (const q of pools[stage]) {
      if (!byDomain[q.domain]) byDomain[q.domain] = [];
      byDomain[q.domain].push(q);
    }
    for (const d in byDomain) shuffle(byDomain[d]);
    const domains = shuffle(Object.keys(byDomain));
    const interleaved = [];
    let round = 0;
    let added = true;
    while (added) {
      added = false;
      for (const d of domains) {
        if (round < byDomain[d].length) {
          interleaved.push(byDomain[d][round]);
          added = true;
        }
      }
      round++;
    }
    pools[stage] = interleaved;
  }
  return pools;
}

// ============================================================
// Build exploration queue for a domain
// ============================================================
function buildExploreQueue(domain) {
  const questions = DATA.exploration[domain];
  if (!questions) return [];

  // Sort by stage order, then shuffle within stage
  const byStage = {};
  for (const q of questions) {
    if (S.usedQuestionKeys[qKey(q)]) continue;
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
  return queue;
}

// ============================================================
// Fluency integration
// ============================================================
function recordAnswer(question, correct, responseTimeMs) {
  if (typeof OKGFluency !== 'undefined' && OKGFluency) {
    OKGFluency.updateTopic(question.topicId, correct, {
      difficulty: question.difficulty || 0.5,
      responseTimeMs: responseTimeMs,
      medianTimeMs: question.type === 'true-false' ? MEDIAN_TF : MEDIAN_MC
    });
  }
  S.usedQuestionKeys[qKey(question)] = true;
}

// ============================================================
// Domain performance analysis
// ============================================================
function domainPerformance() {
  const perf = {};
  const all = [...S.warmupAnswers, ...S.exploreAnswers];
  for (const a of all) {
    if (!perf[a.domain]) perf[a.domain] = {correct: 0, total: 0};
    perf[a.domain].total++;
    if (a.correct) perf[a.domain].correct++;
  }
  // Merge explored domains
  for (const d in S.exploredDomains) {
    if (!perf[d]) perf[d] = {correct: 0, total: 0};
  }
  return perf;
}

function domainStrength(perf, domain) {
  const p = perf[domain];
  if (!p || p.total === 0) return 'weak';
  const pct = p.correct / p.total;
  if (pct >= 0.6) return 'strong';
  if (pct >= 0.3) return 'familiar';
  return 'weak';
}

// ============================================================
// Phase: Welcome
// ============================================================
function renderWelcome() {
  const totalQ = DATA.stats.topics_with_questions;

  setContent(h('div', {className: 'container'},
    h('h1', null, 'Knowledge Trivia'),
    h('p', {className: 'subtitle'}, 'A fun way to map what you know'),
    h('div', {className: 'intro-card'},
      h('p', {style: {color: '#bbb', fontSize: '15px', lineHeight: '1.7', marginBottom: '20px'}},
        'This isn\'t a test \u2014 it\'s a trivia game that helps personalize your knowledge map. ' +
        'Answer what you can, skip what you can\'t. Every answer teaches us something about where you are.'
      ),
      h('ul', {className: 'intro-features'},
        h('li', {'data-icon': '\uD83C\uDFAF'}, 'Quick-fire questions across ' + Object.keys(DATA.exploration).length + ' domains'),
        h('li', {'data-icon': '\uD83E\uDDE0'}, 'Your answers color your personal knowledge graph'),
        h('li', {'data-icon': '\u23F1\uFE0F'}, 'Takes about 5\u201310 minutes \u2014 stop anytime'),
        h('li', {'data-icon': '\uD83D\uDD13'}, 'No grades, no pressure, just discovery')
      ),
      h('button', {className: 'next-btn', style: {fontSize: '16px', padding: '14px 32px'}, onClick: startWarmup},
        'Let\'s Play')
    ),
    h('div', {className: 'action-row'},
      h('a', {href: 'assessment.html', className: 'action-btn'}, 'Self-Assessment Instead'),
      h('a', {href: 'index.html', className: 'action-btn'}, 'Browse Graph')
    )
  ));
}

// ============================================================
// Phase: Warmup (adaptive tier escalation)
// ============================================================
// Asks TIER_QUESTIONS per stage tier, then escalates if doing well.
// A college-educated user should breeze through easy tiers in ~6 questions
// and hit their ceiling within ~15 total.

const TIER_LABELS_SHORT = {
  'pre-formal': 'Basics',
  'concrete-operations': 'Elementary',
  'abstract-reasoning': 'Intermediate',
  'formal-systems': 'Advanced',
  'advanced': 'Expert'
};

function startWarmup() {
  S.phase = 'warmup';
  S.warmupPools = buildWarmupPools();
  S.warmupTier = 0;
  S.warmupTierIndex = 0;
  S.warmupTierCorrect = 0;
  S.warmupAnswers = [];
  S.warmupDone = false;
  S.showingFeedback = false;
  // Skip to lowest tier that has questions
  while (S.warmupTier < STAGES_ORDERED.length &&
         (!S.warmupPools[STAGES_ORDERED[S.warmupTier]] ||
          S.warmupPools[STAGES_ORDERED[S.warmupTier]].length === 0)) {
    S.warmupTier++;
  }
  render();
}

function getWarmupQuestion() {
  // Get next question from current tier's pool
  const stage = STAGES_ORDERED[S.warmupTier];
  const pool = S.warmupPools[stage];
  if (!pool) return null;
  // Find next unused question
  for (let i = 0; i < pool.length; i++) {
    if (!S.usedQuestionKeys[qKey(pool[i])]) return pool[i];
  }
  return null;
}

function advanceTier() {
  // Always advance to the next tier — don't stop on easy misses.
  // Domain-specific questions at lower tiers aren't good indicators
  // of general academic level. The inference uses the HIGHEST tier
  // where the user demonstrated competence across multiple domains,
  // so missing "are ribosomes organelles?" doesn't matter if you
  // later ace formal-systems math.
  S.warmupTier++;
  S.warmupTierIndex = 0;
  S.warmupTierCorrect = 0;
  // Skip tiers with no questions
  while (S.warmupTier < STAGES_ORDERED.length &&
         !getWarmupQuestion()) {
    S.warmupTier++;
  }
}

function renderWarmup() {
  if (S.warmupDone || S.warmupTier >= STAGES_ORDERED.length) {
    showWarmupResults();
    return;
  }

  const q = getWarmupQuestion();
  if (!q) {
    // No more questions at this tier, try next
    S.warmupTier++;
    if (S.warmupTier >= STAGES_ORDERED.length) {
      showWarmupResults();
      return;
    }
    S.warmupTierIndex = 0;
    S.warmupTierCorrect = 0;
    render();
    return;
  }

  const tierLabel = TIER_LABELS_SHORT[STAGES_ORDERED[S.warmupTier]] || '';
  const totalAnswered = S.warmupAnswers.length;
  const totalCorrect = S.warmupAnswers.filter(a => a.correct).length;
  const scoreText = totalAnswered > 0 ? totalCorrect + '/' + totalAnswered : '';

  // Progress: show tier progression (5 tiers)
  const tierProgress = ((S.warmupTier + S.warmupTierIndex / TIER_QUESTIONS) / STAGES_ORDERED.length) * 100;

  setContent(h('div', {className: 'container'},
    h('div', {style: {display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '6px'}},
      h('h1', {style: {margin: 0}}, 'Knowledge Trivia'),
      scoreText ? h('span', {className: 'score-display'}, scoreText) : null
    ),
    h('p', {className: 'subtitle'},
      tierLabel + ' \u2014 Question ' + (S.warmupTierIndex + 1) + ' of ' + TIER_QUESTIONS +
      ' (Tier ' + (S.warmupTier + 1) + ' of ' + STAGES_ORDERED.length + ')'
    ),
    h('div', {className: 'progress-wrap'},
      h('div', {className: 'progress-bar', style: {width: tierProgress + '%'}})
    ),
    h('span', {className: 'phase-label warmup'}, tierLabel),
    renderQuestionCard(q, 'warmup'),
    h('div', {className: 'action-row'},
      h('button', {className: 'action-btn', onClick: skipWarmupQuestion}, 'Skip'),
      h('button', {className: 'action-btn', onClick: () => { showWarmupResults(); }}, 'I\'m Done')
    )
  ));
  S.questionStart = performance.now();
}

function answerWarmup(q, selectedAnswer) {
  if (S.showingFeedback) return;
  S.showingFeedback = true;

  const responseTimeMs = Math.round(performance.now() - S.questionStart);
  const correct = selectedAnswer === q.answer;

  recordAnswer(q, correct, responseTimeMs);
  S.warmupAnswers.push({
    topicId: q.topicId, domain: q.domain, correct, responseTimeMs,
    stage: q.stage
  });

  S.warmupTierIndex++;
  S.warmupTierCorrect += correct ? 1 : 0;

  showFeedback(q, selectedAnswer, correct, () => {
    S.showingFeedback = false;
    // Check tier escalation after TIER_QUESTIONS at this tier
    if (S.warmupTierIndex >= TIER_QUESTIONS) {
      advanceTier();
    }
    render();
  });
}

function skipWarmupQuestion() {
  if (S.showingFeedback) return;
  const q = getWarmupQuestion();
  if (q) S.usedQuestionKeys[qKey(q)] = true;
  S.warmupTierIndex++;
  if (S.warmupTierIndex >= TIER_QUESTIONS) {
    advanceTier();
  }
  render();
}

function showWarmupResults() {
  S.phase = 'warmup-results';
  render();
}

function renderWarmupResults() {
  const perf = domainPerformance();
  const totalCorrect = S.warmupAnswers.filter(a => a.correct).length;
  const totalAnswered = S.warmupAnswers.length;
  const pct = totalAnswered > 0 ? Math.round(totalCorrect / totalAnswered * 100) : 0;

  // Build domain results sorted by performance
  const domainResults = [];
  for (const d of DOMAIN_ORDER) {
    if (perf[d] && perf[d].total > 0) {
      const p = perf[d];
      domainResults.push({domain: d, correct: p.correct, total: p.total, pct: Math.round(p.correct / p.total * 100)});
    }
  }
  domainResults.sort((a, b) => b.pct - a.pct);

  const hasExploreQuestions = Object.keys(DATA.exploration).length > 0;

  setContent(h('div', {className: 'container'},
    h('h1', null, 'Warm-Up Complete!'),
    h('p', {className: 'subtitle'}, 'You got ' + totalCorrect + ' out of ' + totalAnswered + ' right (' + pct + '%)'),
    h('div', {className: 'summary-card'},
      h('h2', null, 'Domain Breakdown'),
      ...domainResults.map(dr =>
        h('div', {className: 'stat-bar'},
          h('span', {className: 'label'}, formatDomain(dr.domain)),
          h('div', {className: 'bar'},
            h('div', {className: 'bar-fill', style: {
              width: dr.pct + '%',
              background: dr.pct >= 60 ? '#4CAF50' : dr.pct >= 30 ? '#FFC107' : '#666'
            }})
          ),
          h('span', {className: 'value'}, dr.correct + '/' + dr.total)
        )
      )
    ),
    hasExploreQuestions ? h('div', {className: 'intro-card'},
      h('h2', null, 'Ready to Explore Deeper?'),
      h('p', {style: {color: '#999', fontSize: '14px', marginBottom: '16px'}},
        'Pick a domain to dive into harder questions. You can explore as many or as few as you like.'
      ),
      h('button', {className: 'next-btn', style: {fontSize: '16px', padding: '14px 32px'}, onClick: startExplore},
        'Explore Domains')
    ) : null,
    h('div', {className: 'link-row'},
      h('button', {className: 'link-btn', onClick: showResults}, 'See Final Results'),
      h('a', {href: 'radial-graph.html', className: 'link-btn'}, 'View Knowledge Graph')
    )
  ));
}

// ============================================================
// Phase: Exploration
// ============================================================
function startExplore() {
  S.phase = 'explore-pick';
  render();
}

function renderExplorePick() {
  const perf = domainPerformance();

  // Build domain cards
  const strong = [], familiar = [], weak = [];
  for (const d of DOMAIN_ORDER) {
    if (!DATA.exploration[d]) continue;
    if (S.skippedDomains[d]) continue;

    const remaining = DATA.exploration[d].filter(q => !S.usedQuestionKeys[qKey(q)]).length;
    if (remaining === 0) continue;

    const strength = domainStrength(perf, d);
    const explored = S.exploredDomains[d] || null;
    const card = {domain: d, strength, remaining, explored};

    if (strength === 'strong') strong.push(card);
    else if (strength === 'familiar') familiar.push(card);
    else weak.push(card);
  }

  const allCards = [...strong, ...familiar, ...weak];

  if (allCards.length === 0) {
    showResults();
    return;
  }

  function makeCard(c) {
    const p = perf[c.domain];
    const pStr = p && p.total > 0 ? p.correct + '/' + p.total + ' correct' : c.remaining + ' questions';
    const cls = 'domain-card ' + c.strength + (c.explored ? ' explored' : '');
    return h('div', {className: cls, onClick: () => startDomainExplore(c.domain)},
      h('div', {className: 'name'}, formatDomain(c.domain)),
      h('div', {className: 'info'}, pStr + (c.explored ? ' \u2014 explored' : ''))
    );
  }

  setContent(h('div', {className: 'container'},
    h('h1', null, 'Choose a Domain'),
    h('p', {className: 'subtitle'}, 'Pick a domain to explore with harder questions'),
    h('div', {className: 'domain-grid'},
      ...allCards.map(makeCard)
    ),
    h('div', {className: 'link-row'},
      h('button', {className: 'link-btn', onClick: showResults}, 'See Final Results'),
      h('a', {href: 'radial-graph.html', className: 'link-btn'}, 'View Knowledge Graph')
    )
  ));
}

function startDomainExplore(domain) {
  S.phase = 'explore';
  S.exploreDomain = domain;
  S.exploreQueue = buildExploreQueue(domain);
  S.exploreIndex = 0;
  S.showingFeedback = false;
  if (S.exploreQueue.length === 0) {
    S.phase = 'explore-pick';
    render();
    return;
  }
  render();
}

function renderExplore() {
  if (S.exploreIndex >= S.exploreQueue.length || S.exploreIndex >= EXPLORE_PER_DOMAIN) {
    finishDomainExplore();
    return;
  }

  const q = S.exploreQueue[S.exploreIndex];
  const progress = (S.exploreIndex / Math.min(EXPLORE_PER_DOMAIN, S.exploreQueue.length)) * 100;

  // Domain explore score
  const domainAnswers = S.exploreAnswers.filter(a => a.domain === S.exploreDomain);
  const correct = domainAnswers.filter(a => a.correct).length;
  const total = domainAnswers.length;
  const scoreText = total > 0 ? correct + '/' + total : '';

  setContent(h('div', {className: 'container'},
    h('div', {style: {display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '6px'}},
      h('h1', {style: {margin: 0}}, formatDomain(S.exploreDomain)),
      scoreText ? h('span', {className: 'score-display'}, scoreText) : null
    ),
    h('p', {className: 'subtitle'},
      'Question ' + (S.exploreIndex + 1) + ' of ' + Math.min(EXPLORE_PER_DOMAIN, S.exploreQueue.length) +
      ' \u2014 ' + STAGE_LABELS[q.stage]
    ),
    h('div', {className: 'progress-wrap'},
      h('div', {className: 'progress-bar', style: {width: progress + '%'}})
    ),
    h('span', {className: 'phase-label explore'}, 'Exploration'),
    renderQuestionCard(q, 'explore'),
    h('div', {className: 'action-row'},
      h('button', {className: 'action-btn', onClick: skipExploreQuestion}, 'Skip'),
      h('button', {className: 'action-btn', onClick: () => { S.phase = 'explore-pick'; render(); }}, 'Something Different'),
      h('button', {className: 'action-btn', onClick: () => { S.skippedDomains[S.exploreDomain] = true; S.phase = 'explore-pick'; render(); }}, 'Skip Domain'),
      h('button', {className: 'action-btn', onClick: showResults}, 'I\'m Done')
    )
  ));
  S.questionStart = performance.now();
}

function answerExplore(q, selectedAnswer) {
  if (S.showingFeedback) return;
  S.showingFeedback = true;

  const responseTimeMs = Math.round(performance.now() - S.questionStart);
  const correct = q.type === 'multiple-choice'
    ? selectedAnswer === q.answer
    : selectedAnswer === q.answer;

  recordAnswer(q, correct, responseTimeMs);
  S.exploreAnswers.push({topicId: q.topicId, domain: q.domain, correct, responseTimeMs});

  showFeedback(q, selectedAnswer, correct, () => {
    S.showingFeedback = false;
    S.exploreIndex++;
    render();
  });
}

function skipExploreQuestion() {
  if (S.showingFeedback) return;
  S.usedQuestionKeys[qKey(S.exploreQueue[S.exploreIndex])] = true;
  S.exploreIndex++;
  render();
}

function finishDomainExplore() {
  const domainAnswers = S.exploreAnswers.filter(a => a.domain === S.exploreDomain);
  S.exploredDomains[S.exploreDomain] = {
    correct: domainAnswers.filter(a => a.correct).length,
    total: domainAnswers.length
  };
  S.phase = 'explore-pick';
  render();
}

// ============================================================
// Question card rendering (shared)
// ============================================================
function renderQuestionCard(q, phase) {
  const answerHandler = phase === 'warmup'
    ? (ans) => answerWarmup(q, ans)
    : (ans) => answerExplore(q, ans);

  const card = h('div', {className: 'question-card', id: 'qcard'},
    h('span', {className: 'domain-tag'}, formatDomain(q.domain)),
    h('div', {className: 'question-text'}, q.question)
  );

  if (q.type === 'multiple-choice' && q.options) {
    const letters = ['A', 'B', 'C', 'D', 'E', 'F'];
    const answersDiv = h('div', {className: 'answers'});
    q.options.forEach((opt, i) => {
      const btn = h('button', {
        className: 'answer-btn',
        id: 'opt-' + i,
        onClick: () => answerHandler(i)
      },
        h('span', {className: 'answer-letter'}, letters[i]),
        String(opt)
      );
      answersDiv.appendChild(btn);
    });
    card.appendChild(answersDiv);
  } else if (q.type === 'true-false') {
    const tfDiv = h('div', {className: 'tf-buttons'},
      h('button', {className: 'tf-btn', id: 'tf-true', onClick: () => answerHandler(true)}, 'True'),
      h('button', {className: 'tf-btn', id: 'tf-false', onClick: () => answerHandler(false)}, 'False')
    );
    card.appendChild(tfDiv);
  }

  return card;
}

// ============================================================
// Feedback display
// ============================================================
function showFeedback(q, selectedAnswer, correct, onDone) {
  const card = document.getElementById('qcard');
  if (!card) { onDone(); return; }

  // Guard against double-fire (timer + click)
  let fired = false;
  function advance() {
    if (fired) return;
    fired = true;
    clearTimeout(S.feedbackTimer);
    onDone();
  }

  card.classList.add(correct ? 'correct' : 'wrong');

  // Highlight answers
  if (q.type === 'multiple-choice') {
    const buttons = card.querySelectorAll('.answer-btn');
    buttons.forEach((btn, i) => {
      btn.classList.add('disabled');
      if (i === q.answer) btn.classList.add('correct-answer');
      if (i === selectedAnswer && !correct) btn.classList.add('wrong-answer');
      if (i === selectedAnswer) btn.classList.add('selected');
    });
  } else {
    const trueBtn = document.getElementById('tf-true');
    const falseBtn = document.getElementById('tf-false');
    if (trueBtn && falseBtn) {
      trueBtn.classList.add('disabled');
      falseBtn.classList.add('disabled');
      if (q.answer === true) trueBtn.classList.add('correct-answer');
      else falseBtn.classList.add('correct-answer');
      if (selectedAnswer === true && !correct) trueBtn.classList.add('wrong-answer');
      if (selectedAnswer === false && !correct) falseBtn.classList.add('wrong-answer');
      if (selectedAnswer === true) trueBtn.classList.add('selected');
      if (selectedAnswer === false) falseBtn.classList.add('selected');
    }
  }

  // Show explanation
  const feedbackDiv = h('div', {className: 'feedback ' + (correct ? 'correct' : 'wrong')},
    h('span', {className: 'feedback-icon'}, correct ? '\u2705' : '\u274C'),
    correct ? 'Correct!' : 'Not quite.',
    q.explanation ? h('span', {style: {display: 'block', marginTop: '6px', fontSize: '12px', color: '#999'}}, q.explanation) : null
  );
  card.appendChild(feedbackDiv);

  // Next button (manual only — no auto-advance to prevent misclicks)
  const nextBtn = h('button', {className: 'next-btn', onClick: advance}, 'Next \u2192');
  card.appendChild(nextBtn);
  nextBtn.focus();
}

// ============================================================
// Phase: Results
// ============================================================
function showResults() {
  S.phase = 'results';

  // Run post-assessment inference before rendering results
  if (typeof OKGFluency !== 'undefined' && OKGFluency && DATA.topicIndex) {
    S.inferenceResult = runInference();
  }

  render();
}

/**
 * Build domain-stage performance map and run inference.
 */
function runInference() {
  const allAnswers = [...S.warmupAnswers, ...S.exploreAnswers];

  // Build domainPerformance: {domain: {stage: {correct, total}}}
  // We need to map answers back to their stage via the question data
  const stagePerf = {};
  for (const a of allAnswers) {
    // Find the question to get its stage
    const q = findQuestionByTopic(a.topicId);
    const stage = q ? q.stage : null;
    if (!stage) continue;

    if (!stagePerf[a.domain]) stagePerf[a.domain] = {};
    if (!stagePerf[a.domain][stage]) stagePerf[a.domain][stage] = {correct: 0, total: 0};
    stagePerf[a.domain][stage].total++;
    if (a.correct) stagePerf[a.domain][stage].correct++;
  }

  return OKGFluency.postAssessmentInference(stagePerf, DATA.topicIndex);
}

function findQuestionByTopic(topicId) {
  // Search warmup and exploration pools
  for (const q of DATA.warmup) {
    if (q.topicId === topicId) return q;
  }
  for (const domain in DATA.exploration) {
    for (const q of DATA.exploration[domain]) {
      if (q.topicId === topicId) return q;
    }
  }
  return null;
}

function renderResults() {
  const allAnswers = [...S.warmupAnswers, ...S.exploreAnswers];
  const totalCorrect = allAnswers.filter(a => a.correct).length;
  const totalAnswered = allAnswers.length;
  const pct = totalAnswered > 0 ? Math.round(totalCorrect / totalAnswered * 100) : 0;

  // Per-domain results
  const perf = domainPerformance();
  const domainResults = [];
  for (const d of DOMAIN_ORDER) {
    const p = perf[d];
    if (!p || p.total === 0) continue;
    domainResults.push({
      domain: d,
      correct: p.correct,
      total: p.total,
      pct: Math.round(p.correct / p.total * 100)
    });
  }
  domainResults.sort((a, b) => b.pct - a.pct);

  // Fluency summary (after inference)
  let fluencySummary = null;
  if (typeof OKGFluency !== 'undefined' && OKGFluency) {
    fluencySummary = OKGFluency.summary();
  }

  // Unique topics directly tested
  const uniqueTopics = new Set(allAnswers.map(a => a.topicId)).size;

  // Inference stats
  const inf = S.inferenceResult || {topicsInferred: 0, domainsProcessed: 0, crossDomainApplied: false, overallTier: null};

  // Tier labels
  const TIER_LABELS = {
    'pre-formal': 'Early Learner',
    'concrete-operations': 'Elementary',
    'abstract-reasoning': 'High School',
    'formal-systems': 'College',
    'advanced': 'Graduate'
  };

  setContent(h('div', {className: 'container'},
    h('h1', null, 'Your Results'),
    h('p', {className: 'subtitle'},
      totalCorrect + ' of ' + totalAnswered + ' correct (' + pct + '%) across ' + uniqueTopics + ' topics'
    ),

    // Overall stats
    h('div', {className: 'summary-card'},
      h('h2', null, 'Summary'),
      h('div', {style: {display: 'flex', gap: '24px', flexWrap: 'wrap', marginBottom: '16px'}},
        h('div', null,
          h('div', {style: {fontSize: '32px', fontWeight: '700', color: '#eee'}}, pct + '%'),
          h('div', {style: {color: '#777', fontSize: '12px'}}, 'Accuracy')
        ),
        h('div', null,
          h('div', {style: {fontSize: '32px', fontWeight: '700', color: '#eee'}}, String(uniqueTopics)),
          h('div', {style: {color: '#777', fontSize: '12px'}}, 'Directly Tested')
        ),
        inf.topicsInferred > 0 ? h('div', null,
          h('div', {style: {fontSize: '32px', fontWeight: '700', color: '#b39ddb'}}, String(inf.topicsInferred)),
          h('div', {style: {color: '#777', fontSize: '12px'}}, 'Inferred')
        ) : null,
        h('div', null,
          h('div', {style: {fontSize: '32px', fontWeight: '700', color: '#eee'}}, String(domainResults.length)),
          h('div', {style: {color: '#777', fontSize: '12px'}}, 'Domains Covered')
        )
      ),

      // Tier estimate
      inf.overallTier ? h('p', {style: {color: '#b39ddb', fontSize: '14px', fontWeight: '600', marginBottom: '8px'}},
        'Estimated level: ' + (TIER_LABELS[inf.overallTier] || inf.overallTier)
      ) : null,

      // Inference explanation
      inf.topicsInferred > 0 ? h('p', {style: {color: '#999', fontSize: '13px', marginBottom: '8px'}},
        'Inferred knowledge for ' + inf.topicsInferred.toLocaleString() +
        ' additional topics across ' + inf.domainsProcessed + ' domains' +
        (inf.crossDomainApplied ? ' (general-education baseline applied).' : '.')
      ) : null,

      fluencySummary && fluencySummary.totalTracked > 0 ? h('p', {style: {color: '#999', fontSize: '13px'}},
        fluencySummary.totalTracked.toLocaleString() + ' topics now have fluency scores. ' +
        'Visit the knowledge graph to see your progress visualized.'
      ) : null,

      // Confidence note
      h('p', {style: {color: '#666', fontSize: '11px', fontStyle: 'italic', marginTop: '8px'}},
        'Directly tested topics have high confidence. Inferred topics have lower confidence ' +
        'and may not reflect specialized knowledge gaps. ' +
        'Multiple-choice scores can also reflect test-taking skill \u2014 short-answer questions (coming soon) will give more precise readings.'
      )
    ),

    // Domain breakdown
    domainResults.length > 0 ? h('div', {className: 'summary-card'},
      h('h2', null, 'Domain Performance'),
      ...domainResults.map(dr => {
        // Show confidence indicator per domain
        const confLabel = dr.pct >= 60 ? 'high' : dr.pct >= 30 ? 'medium' : 'low';
        const confColor = dr.pct >= 60 ? '#4CAF50' : dr.pct >= 30 ? '#FFC107' : '#666';
        return h('div', {className: 'stat-bar'},
          h('span', {className: 'label'}, formatDomain(dr.domain)),
          h('div', {className: 'bar'},
            h('div', {className: 'bar-fill', style: {
              width: dr.pct + '%',
              background: confColor
            }})
          ),
          h('span', {className: 'value', style: {color: confColor}}, dr.correct + '/' + dr.total)
        );
      })
    ) : null,

    // Actions
    h('div', {className: 'link-row'},
      h('a', {href: 'radial-graph.html', className: 'link-btn', style: {background: '#2a4a2a', borderColor: '#4CAF50'}},
        'View Your Knowledge Graph'),
      h('a', {href: 'index.html', className: 'link-btn'}, 'Browse All Domains'),
      h('button', {className: 'link-btn', onClick: resetQuiz,
        style: {background: 'rgba(244,67,54,0.1)', borderColor: '#F44336', color: '#F44336'}},
        'Play Again')
    )
  ));
}

function resetQuiz() {
  S = {
    phase: 'welcome',
    warmupPools: {},
    warmupTier: 0,
    warmupTierIndex: 0,
    warmupTierCorrect: 0,
    warmupAnswers: [],
    warmupDone: false,
    questionStart: null,
    showingFeedback: false,
    feedbackTimer: null,
    exploreDomain: null,
    exploreQueue: [],
    exploreIndex: 0,
    exploreAnswers: [],
    exploredDomains: {},
    skippedDomains: {},
    usedQuestionKeys: {},
  };
  render();
}

// ============================================================
// Main render dispatcher
// ============================================================
function render() {
  switch (S.phase) {
    case 'loading':
      setContent(h('div', {className: 'container'},
        h('div', {style: {textAlign: 'center', padding: '60px 0'}},
          h('div', {style: {
            width: '36px', height: '36px', border: '3px solid #333',
            borderTopColor: '#7c4dff', borderRadius: '50%',
            animation: 'spin 0.8s linear infinite', margin: '0 auto 16px'
          }}),
          h('p', null, 'Loading quiz data...')
        )
      ));
      break;
    case 'welcome':       renderWelcome(); break;
    case 'warmup':        renderWarmup(); break;
    case 'warmup-results': renderWarmupResults(); break;
    case 'explore-pick':  renderExplorePick(); break;
    case 'explore':       renderExplore(); break;
    case 'results':       renderResults(); break;
    default:
      setContent(h('div', {className: 'container'},
        h('p', {style: {color: '#F44336'}}, 'Unknown phase: ' + S.phase)
      ));
  }
}

// ============================================================
// Boot
// ============================================================
function boot() {
  if (!DATA) {
    setContent(h('div', {className: 'container'},
      h('h1', null, 'Knowledge Trivia'),
      h('p', {style: {color: '#F44336'}},
        'Quiz data not found. Run generate_assessment_questions.py first.')
    ));
    return;
  }
  S.phase = 'welcome';
  render();
}

// Add spin animation
const style = document.createElement('style');
style.textContent = '@keyframes spin { to { transform: rotate(360deg); } }';
document.head.appendChild(style);

render();
boot();
"""


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    html = generate_quiz_html()
    out_path = OUTPUT_DIR / "quiz.html"
    out_path.write_text(html, encoding="utf-8")
    size_kb = len(html.encode("utf-8")) / 1024
    print(f"Generated {out_path} ({size_kb:.0f} KB)")


if __name__ == "__main__":
    main()
