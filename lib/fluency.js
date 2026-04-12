/**
 * OKG Fluency Engine
 *
 * Bayesian fluency model for the Open Knowledge Graph.
 * Tracks per-topic mastery (0-100), updates via log-odds,
 * propagates through prerequisite graph, and maps scores to colors.
 *
 * localStorage keys:
 *   okg-fluency       — {topicId: score} (only non-zero topics)
 *   okg-fluency-conf  — {topicId: confidence} (0-1, only non-zero)
 *   okg-fluency-meta  — {lastUpdated, totalAnswered, version}
 *   okg-goals         — [topicId, ...] (starred target topics)
 *   okg-adjustments   — {courseId: delta} (manual course-level overrides)
 */
const OKGFluency = (function () {
  'use strict';

  // ---------------------------------------------------------------------------
  // Constants
  // ---------------------------------------------------------------------------

  const STORAGE_KEYS = {
    fluency:     'okg-fluency',
    confidence:  'okg-fluency-conf',
    meta:        'okg-fluency-meta',
    goals:       'okg-goals',
    adjustments: 'okg-adjustments',
    userStage:   'okg-user-stage',
    domainPrior: 'okg-domain-prior',
    touched:     'okg-fluency-touched',  // {topicId: unix_ms_timestamp}
  };

  // Stale-topics threshold: a touched-then-left-alone topic with decaying
  // fluency in this range should surface for review rather than sit unseen.
  const STALE_MIN_SCORE = 50;
  const STALE_MAX_SCORE = 85;
  const STALE_AGE_MS = 21 * 24 * 60 * 60 * 1000;  // 3 weeks

  const VERSION = 1;

  // Stage ordering — matches meta/developmental-stages.md
  const STAGE_INDEX = {
    'pre-formal':          0,
    'concrete-operations': 1,
    'abstract-reasoning':  2,
    'formal-systems':      3,
    'advanced':            4,
    'expert':              5,
  };
  const DEFAULT_USER_STAGE = 0;   // first-time visitor: elementary
  const STAGE_DECAY_RATE   = 0.4; // each stage away from user = 40% decay
  const DEFAULT_DOMAIN_PRIOR = 1.0;

  // Bayesian update parameters
  const DEFAULT_EVIDENCE   = 1.0;   // log-odds delta for a standard question
  const WRONG_PENALTY_MULT = 0.7;   // wrong answers penalized at 70% of correct reward
  const FLOOR_LOGIT        = -4.6;  // ~1% — practical floor
  const CEIL_LOGIT         =  4.6;  // ~99% — practical ceiling

  // Response time modifiers (multiplied against evidence)
  const RT_FAST_CORRECT = 1.3;  // confident correct = stronger evidence
  const RT_SLOW_CORRECT = 0.8;  // hesitant correct = moderate evidence
  const RT_FAST_WRONG   = 0.4;  // likely misclick = low penalty
  const RT_SLOW_WRONG   = 1.0;  // genuine gap = full penalty

  // Prerequisite propagation — per-edge decay depends on edge type.
  // Hard edge: "must know first" — strong inference both directions.
  // Soft edge: "helpful but not required" — half weight in backward
  // propagation, and zero weight in forward capping (soft prereqs shouldn't
  // hold back a successor).
  const BACKWARD_DECAY_HARD = 0.85; // per hard hop: implied fluency = score * 0.85^d
  const BACKWARD_DECAY_SOFT = 0.425; // per soft hop: half weight
  const BACKWARD_DECAY = BACKWARD_DECAY_HARD;  // legacy alias (kept exported for tests)
  const FORWARD_CAP_WEIGHT = 0.9;  // successor capped at 90% of min hard-prereq fluency
  const MAX_PROPAGATION_DEPTH = 12; // don't propagate beyond 12 hops

  // Prereq list normalization — accept either string IDs (legacy) or
  // {id, type} objects (Cut 6+). All propagation/frontier helpers route
  // through these so the storage shape can vary per graph source.
  function prereqId(p) {
    return typeof p === 'string' ? p : (p && p.id);
  }
  function prereqType(p) {
    if (typeof p === 'string') return 'hard';
    if (p && p.type === 'soft') return 'soft';
    return 'hard';
  }

  // Color mapping — two modes:
  //
  // "radial" mode: keeps domain hue, modulates saturation/lightness.
  //   Works well on the cross-domain radial graph where the rainbow
  //   already distinguishes domains.
  //
  // "mastery" mode: universal gradient independent of domain hue.
  //   Gray → red → amber → green. Better for per-domain hierarchy
  //   views where all topics share a hue and you need to distinguish
  //   hundreds of nodes by fluency alone.

  // Radial mode: [threshold, saturation%, lightness%] — applied to domain hue
  const RADIAL_COLOR_STOPS = [
    [  0,  8, 30],  // dark gray — no data
    [ 15, 30, 35],  // dim tint
    [ 40, 55, 42],  // medium
    [ 65, 70, 48],  // bright
    [ 85, 80, 55],  // vivid
    [100, 90, 62],  // glow
  ];

  // Mastery mode: [threshold, hue, saturation%, lightness%] — fixed gradient
  const MASTERY_COLOR_STOPS = [
    [  0,   0,  0, 40],  // gray — no data
    [ 10,   0, 55, 42],  // red — just started
    [ 30,  25, 70, 48],  // orange — beginner
    [ 50,  42, 80, 50],  // amber — developing
    [ 70,  80, 75, 45],  // yellow-green — proficient
    [ 85, 130, 70, 42],  // green — strong
    [100, 140, 80, 45],  // bright green — mastered
  ];

  // Frontier: topic where prereqs are well-known but topic itself is not
  const FRONTIER_PREREQ_THRESHOLD = 60;  // prereqs must average above this
  const FRONTIER_SELF_THRESHOLD   = 30;  // own fluency must be below this


  // ---------------------------------------------------------------------------
  // Math utilities
  // ---------------------------------------------------------------------------

  function sigmoid(x) {
    if (x >= 20) return 1;
    if (x <= -20) return 0;
    return 1 / (1 + Math.exp(-x));
  }

  function logit(p) {
    p = Math.max(0.005, Math.min(0.995, p));
    return Math.log(p / (1 - p));
  }

  function clampLogit(x) {
    return Math.max(FLOOR_LOGIT, Math.min(CEIL_LOGIT, x));
  }

  function scoreToLogit(score) {
    return logit(score / 100);
  }

  function logitToScore(l) {
    return Math.round(sigmoid(l) * 100);
  }


  // ---------------------------------------------------------------------------
  // Storage layer
  // ---------------------------------------------------------------------------

  function loadJSON(key, fallback) {
    try {
      var raw = localStorage.getItem(key);
      return raw ? JSON.parse(raw) : fallback;
    } catch (e) {
      return fallback;
    }
  }

  function saveJSON(key, data) {
    try {
      localStorage.setItem(key, JSON.stringify(data));
    } catch (e) {
      // localStorage full or unavailable — silent fail
    }
  }

  /** Load all fluency scores. Returns {topicId: score (0-100)}. */
  function loadScores() {
    return loadJSON(STORAGE_KEYS.fluency, {});
  }

  /** Save all fluency scores. Only stores non-zero entries. */
  function saveScores(scores) {
    var compact = {};
    for (var id in scores) {
      if (scores[id] > 0) compact[id] = scores[id];
    }
    saveJSON(STORAGE_KEYS.fluency, compact);
  }

  /** Load all confidence scores. Returns {topicId: confidence (0-1)}. */
  function loadConfidence() {
    return loadJSON(STORAGE_KEYS.confidence, {});
  }

  /** Save all confidence scores. Only stores non-zero entries. */
  function saveConfidence(conf) {
    var compact = {};
    for (var id in conf) {
      if (conf[id] > 0) compact[id] = Math.round(conf[id] * 1000) / 1000;
    }
    saveJSON(STORAGE_KEYS.confidence, compact);
  }

  function loadMeta() {
    return loadJSON(STORAGE_KEYS.meta, {
      lastUpdated: null,
      totalAnswered: 0,
      version: VERSION,
    });
  }

  function saveMeta(meta) {
    meta.version = VERSION;
    saveJSON(STORAGE_KEYS.meta, meta);
  }

  function loadGoals() {
    return loadJSON(STORAGE_KEYS.goals, []);
  }

  function saveGoals(goals) {
    saveJSON(STORAGE_KEYS.goals, goals);
  }

  function loadAdjustments() {
    return loadJSON(STORAGE_KEYS.adjustments, {});
  }

  function saveAdjustments(adj) {
    saveJSON(STORAGE_KEYS.adjustments, adj);
  }

  function loadTouched() {
    return loadJSON(STORAGE_KEYS.touched, {});
  }

  function saveTouched(t) {
    saveJSON(STORAGE_KEYS.touched, t);
  }

  /** Record that a topic was touched (answered, marked known/unknown, etc.) now. */
  function markTouched(topicId) {
    var t = loadTouched();
    t[topicId] = Date.now();
    saveTouched(t);
  }


  // ---------------------------------------------------------------------------
  // Cold-start prior (user stage + domain prior)
  // ---------------------------------------------------------------------------

  // Display-only floor: when the user declares a stage (and optionally per-domain
  // priors), nearby-stage topics get a non-zero baseline score even without any
  // Bayesian evidence. This feeds the visual personalization pass in the radial.
  // Stored scores and Bayesian updates are NOT affected — callers that want the
  // floor must apply it explicitly on top of propagate()'s output.

  function getUserStage() {
    var raw = localStorage.getItem(STORAGE_KEYS.userStage);
    if (raw == null) return DEFAULT_USER_STAGE;
    var n = parseInt(raw, 10);
    if (isNaN(n)) return DEFAULT_USER_STAGE;
    return Math.max(0, Math.min(5, n));
  }

  function setUserStage(stage) {
    var n = Math.max(0, Math.min(5, parseInt(stage, 10) || 0));
    try { localStorage.setItem(STORAGE_KEYS.userStage, String(n)); } catch (e) {}
  }

  function getDomainPrior() {
    return loadJSON(STORAGE_KEYS.domainPrior, {});
  }

  function setDomainPrior(obj) {
    saveJSON(STORAGE_KEYS.domainPrior, obj || {});
  }

  function stageIndex(stage) {
    if (typeof stage === 'number') return Math.max(0, Math.min(5, stage | 0));
    var idx = STAGE_INDEX[stage];
    return idx != null ? idx : 2;  // default abstract-reasoning
  }

  /**
   * Compute the cold-start display floor for a topic (0-100).
   * floor = domainPrior[domain] × stageDecay(topic.stage, user.stage) × 100
   * stageDecay is symmetric: topics far from the user's declared stage
   * (in either direction) decay toward 0.
   *
   * @param {string|number} topicStage — stage name or index
   * @param {string} domain
   * @returns {number} floor score, 0-100
   */
  function computeFloor(topicStage, domain) {
    var u = getUserStage();
    var s = stageIndex(topicStage);
    var decay = Math.max(0, 1 - STAGE_DECAY_RATE * Math.abs(s - u));
    var prior = getDomainPrior();
    var dPrior = prior[domain] != null ? prior[domain] : DEFAULT_DOMAIN_PRIOR;
    return Math.round(100 * dPrior * decay);
  }


  // ---------------------------------------------------------------------------
  // Bayesian update engine
  // ---------------------------------------------------------------------------

  /**
   * Compute evidence weight for a single answer.
   *
   * @param {boolean} correct    — did the user answer correctly?
   * @param {number}  difficulty — question difficulty (0-1, higher = harder)
   * @param {number|null} responseTimeMs — how long the user took (null = no tracking)
   * @param {number}  medianTimeMs — median response time for this question type
   * @returns {number} signed log-odds delta (positive = toward mastery)
   */
  function computeEvidence(correct, difficulty, responseTimeMs, medianTimeMs) {
    // Base evidence scales with difficulty: harder questions = more informative
    var base = DEFAULT_EVIDENCE * (0.5 + difficulty);

    // Response time modifier
    var rtMod = 1.0;
    if (responseTimeMs != null && medianTimeMs > 0) {
      var fast = responseTimeMs < medianTimeMs * 0.6;
      if (correct) {
        rtMod = fast ? RT_FAST_CORRECT : RT_SLOW_CORRECT;
      } else {
        rtMod = fast ? RT_FAST_WRONG : RT_SLOW_WRONG;
      }
    }

    var evidence = base * rtMod;

    // Asymmetric: wrong answers have reduced penalty
    if (!correct) {
      evidence = -evidence * WRONG_PENALTY_MULT;
    }

    return evidence;
  }

  /**
   * Update a single topic's fluency based on an answered question.
   *
   * @param {string}  topicId
   * @param {boolean} correct
   * @param {object}  [opts]
   * @param {number}  [opts.difficulty=0.5]     — question difficulty 0-1
   * @param {number}  [opts.responseTimeMs]     — user's response time
   * @param {number}  [opts.medianTimeMs=8000]  — baseline median for this question type
   * @returns {number} new fluency score (0-100)
   */
  function updateTopic(topicId, correct, opts) {
    opts = opts || {};
    var difficulty = opts.difficulty != null ? opts.difficulty : 0.5;
    var responseTimeMs = opts.responseTimeMs != null ? opts.responseTimeMs : null;
    var medianTimeMs = opts.medianTimeMs || 8000;

    var scores = loadScores();
    var currentScore = scores[topicId] || 0;

    // Score 0 means "no data" — use neutral prior (50/50, logit=0)
    // so the first answer has meaningful impact
    var currentLogit = currentScore === 0 ? 0 : scoreToLogit(currentScore);

    var evidence = computeEvidence(correct, difficulty, responseTimeMs, medianTimeMs);
    var newLogit = clampLogit(currentLogit + evidence);
    var newScore = logitToScore(newLogit);

    scores[topicId] = newScore;
    saveScores(scores);
    markTouched(topicId);

    // Update confidence: each direct answer raises confidence toward 1.0
    // First answer = 0.45 (inference CAN override a single wrong answer)
    // Second answer = 0.70 (inference cannot override two answers)
    // Third = 0.83, etc.
    var conf = loadConfidence();
    var currentConf = conf[topicId] || 0;
    conf[topicId] = currentConf + (1 - currentConf) * 0.45;
    saveConfidence(conf);

    // Update meta
    var meta = loadMeta();
    meta.totalAnswered = (meta.totalAnswered || 0) + 1;
    meta.lastUpdated = new Date().toISOString();
    saveMeta(meta);

    return newScore;
  }

  /**
   * Directly set a topic's fluency score (for manual "I know this" toggle
   * or bulk import from assessment results).
   *
   * @param {string} topicId
   * @param {number} score — 0-100
   */
  function setScore(topicId, score) {
    var scores = loadScores();
    scores[topicId] = Math.max(0, Math.min(100, Math.round(score)));
    saveScores(scores);
    markTouched(topicId);
  }

  /**
   * Get the current fluency score for a topic.
   * Returns 0 if no data exists.
   */
  function getScore(topicId) {
    var scores = loadScores();
    return scores[topicId] || 0;
  }

  /**
   * Bulk set scores (e.g., from assessment import).
   * @param {Object} scoreMap — {topicId: score, ...}
   */
  function bulkSetScores(scoreMap) {
    var scores = loadScores();
    for (var id in scoreMap) {
      scores[id] = Math.max(0, Math.min(100, Math.round(scoreMap[id])));
    }
    saveScores(scores);
  }


  // ---------------------------------------------------------------------------
  // Prerequisite propagation
  // ---------------------------------------------------------------------------

  /**
   * Propagate fluency through a prerequisite graph.
   *
   * Given a graph of topics and their prerequisites, infers fluency for
   * topics the user hasn't directly answered questions on:
   *   - Backward: knowing a topic implies partial knowledge of its prereqs
   *   - Forward: not knowing prereqs caps fluency of successors
   *
   * @param {Object} graph — {topicId: {prereqs: [topicId, ...], successors: [topicId, ...]}}
   *                         prereqs should only include hard prerequisites
   * @returns {Object} effective scores — {topicId: effectiveScore}
   *                   (merges direct scores with propagated inferences)
   */
  function propagate(graph) {
    var direct = loadScores();
    var effective = {};

    // Start with direct scores
    for (var id in graph) {
      effective[id] = direct[id] || 0;
    }

    // --- Backward propagation ---
    // For each topic with a direct score, walk backward through prereqs
    // and infer minimum fluency on ancestors.
    var directIds = Object.keys(direct).filter(function (id) {
      return direct[id] > 0 && graph[id];
    });

    for (var i = 0; i < directIds.length; i++) {
      var startId = directIds[i];
      var startScore = direct[startId];

      // BFS backward through prereqs. Each queue item carries an accumulated
      // decay multiplier along its specific path, so a mix of hard and soft
      // edges on the way back produces the correct product (e.g., one hard
      // hop through a soft hop = 0.85 * 0.425 rather than 0.85^2).
      var queue = [];
      var visited = {};
      visited[startId] = true;

      var prereqs = graph[startId] ? (graph[startId].prereqs || []) : [];
      for (var p = 0; p < prereqs.length; p++) {
        var pid = prereqId(prereqs[p]);
        if (!pid || visited[pid]) continue;
        var ptype = prereqType(prereqs[p]);
        var initialDecay = ptype === 'soft' ? BACKWARD_DECAY_SOFT : BACKWARD_DECAY_HARD;
        queue.push({id: pid, depth: 1, decay: initialDecay});
        visited[pid] = true;
      }

      while (queue.length > 0) {
        var item = queue.shift();
        if (item.depth > MAX_PROPAGATION_DEPTH) continue;

        var implied = Math.round(startScore * item.decay);
        if (implied <= 1) continue;  // too decayed to matter

        // Only raise topics with no direct evidence (direct scores are authoritative)
        if (implied > effective[item.id] && !direct[item.id]) {
          effective[item.id] = implied;
        }

        // Continue walking backward with edge-type-weighted decay
        var ancestors = graph[item.id] ? (graph[item.id].prereqs || []) : [];
        for (var a = 0; a < ancestors.length; a++) {
          var aid = prereqId(ancestors[a]);
          if (!aid || visited[aid]) continue;
          var atype = prereqType(ancestors[a]);
          var stepDecay = atype === 'soft' ? BACKWARD_DECAY_SOFT : BACKWARD_DECAY_HARD;
          queue.push({id: aid, depth: item.depth + 1, decay: item.decay * stepDecay});
          visited[aid] = true;
        }
      }
    }

    // --- Forward propagation (capping) ---
    // Only cap based on DIRECT evidence (or scores already capped by direct evidence).
    // Backward-inferred scores should not cap their successors — that would create
    // circular reasoning (C=90 infers A=65, then A=65 caps B=59, destroying the
    // backward inference that was correct).
    var topo = topoSort(graph);

    // Track which scores are authoritative for capping purposes
    var capSource = {};  // 'direct' | 'capped' — only these can cap successors
    for (var cs = 0; cs < topo.length; cs++) {
      if (direct[topo[cs]] > 0) capSource[topo[cs]] = 'direct';
    }

    for (var t = 0; t < topo.length; t++) {
      var tid = topo[t];
      var node = graph[tid];
      if (!node || !node.prereqs || node.prereqs.length === 0) continue;

      // Forward cap considers HARD prereqs only — soft edges are "helpful,
      // not required" and shouldn't hold back a successor's effective score.
      var capBasis = Infinity;
      var hasCappingPrereq = false;
      for (var pr = 0; pr < node.prereqs.length; pr++) {
        if (prereqType(node.prereqs[pr]) !== 'hard') continue;
        var pid = prereqId(node.prereqs[pr]);
        if (pid && capSource[pid]) {
          capBasis = Math.min(capBasis, effective[pid]);
          hasCappingPrereq = true;
        }
      }

      if (!hasCappingPrereq) continue;

      var cap = Math.round(capBasis * FORWARD_CAP_WEIGHT);
      if (effective[tid] > cap) {
        effective[tid] = cap;
        capSource[tid] = 'capped';  // propagates: this cap can affect successors
      }
    }

    // Apply course-level adjustments
    var adjustments = loadAdjustments();
    if (Object.keys(adjustments).length > 0) {
      for (var adjId in graph) {
        var course = graph[adjId].course;
        if (course && adjustments[course]) {
          effective[adjId] = Math.max(0, Math.min(100,
            effective[adjId] + adjustments[course]
          ));
        }
      }
    }

    return effective;
  }

  /**
   * Kahn's algorithm topological sort.
   * Returns topic IDs in dependency order (prereqs before successors).
   */
  function topoSort(graph) {
    var inDegree = {};
    var ids = Object.keys(graph);

    for (var i = 0; i < ids.length; i++) {
      if (inDegree[ids[i]] == null) inDegree[ids[i]] = 0;
      var succs = graph[ids[i]].successors || [];
      for (var s = 0; s < succs.length; s++) {
        var sid = prereqId(succs[s]);
        if (!sid) continue;
        inDegree[sid] = (inDegree[sid] || 0) + 1;
      }
    }

    var queue = [];
    for (var j = 0; j < ids.length; j++) {
      if (inDegree[ids[j]] === 0) queue.push(ids[j]);
    }

    var sorted = [];
    while (queue.length > 0) {
      var node = queue.shift();
      sorted.push(node);
      var children = graph[node] ? (graph[node].successors || []) : [];
      for (var c = 0; c < children.length; c++) {
        var cid = prereqId(children[c]);
        if (!cid) continue;
        inDegree[cid]--;
        if (inDegree[cid] === 0) queue.push(cid);
      }
    }

    return sorted;
  }


  // ---------------------------------------------------------------------------
  // Frontier detection
  // ---------------------------------------------------------------------------

  /**
   * Identify frontier topics — topics the user is ready to learn next.
   * A frontier topic has high average prereq fluency but low own fluency.
   *
   * @param {Object} graph     — same format as propagate()
   * @param {Object} effective — output of propagate()
   * @param {Object} [options] — optional: {preferredDomains: {domain: weight}}
   *   Topics in preferred domains get a readiness boost (default 1.5x for explored,
   *   2.0x for deep-dived). This ensures "Ready to Learn" reflects user interests.
   * @returns {string[]} topic IDs sorted by readiness (most ready first)
   */
  function findFrontier(graph, effective, options) {
    var frontier = [];
    var domainWeights = (options && options.preferredDomains) || {};

    for (var id in graph) {
      var node = graph[id];
      if (!node) continue;

      var ownScore = effective[id] || 0;
      if (ownScore >= FRONTIER_SELF_THRESHOLD) continue;  // already known

      // Reflective domains (literature, philosophy, art history, music appreciation,
      // most of history, social sciences): prereq chains aren't meaningful for
      // readiness. Any untouched topic in a reflective domain is a frontier
      // candidate, ranked slightly below root-topic readiness so assessable
      // roots still win when they're competing for the same slot.
      if (node.pedagogyType === 'reflective') {
        var reflectiveBoost = domainWeights[node.domain] || 1.0;
        frontier.push({id: id, readiness: 80 * reflectiveBoost, ownScore: ownScore});
        continue;
      }

      // Only HARD prereqs gate frontier eligibility. Soft prereqs are
      // "helpful" and should neither delay a topic from being learnable
      // nor require any particular mastery level before unlocking.
      var prereqs = node.prereqs || [];
      var hardSum = 0;
      var hardCount = 0;
      for (var p = 0; p < prereqs.length; p++) {
        if (prereqType(prereqs[p]) !== 'hard') continue;
        var pid = prereqId(prereqs[p]);
        hardSum += (effective[pid] || 0);
        hardCount++;
      }

      if (hardCount === 0) {
        // Root topics (or topics with only soft prereqs): frontier if not yet learned
        if (ownScore < FRONTIER_SELF_THRESHOLD) {
          var rootBoost = domainWeights[node.domain] || 1.0;
          frontier.push({id: id, readiness: 100 * rootBoost, ownScore: ownScore});
        }
        continue;
      }

      var avgPrereq = hardSum / hardCount;
      if (avgPrereq >= FRONTIER_PREREQ_THRESHOLD) {
        var rawReadiness = avgPrereq - ownScore;
        var domainBoost = domainWeights[node.domain] || 1.0;
        frontier.push({
          id: id,
          readiness: rawReadiness * domainBoost,
          ownScore: ownScore,
        });
      }
    }

    // Sort by readiness descending
    frontier.sort(function (a, b) { return b.readiness - a.readiness; });

    return frontier.map(function (f) { return f.id; });
  }


  // ---------------------------------------------------------------------------
  // Color mapping
  // ---------------------------------------------------------------------------

  /**
   * Interpolate within a color stop table.
   * @param {Array} stops — array of stop arrays
   * @param {number} score — 0-100
   * @param {number} startIdx — index in each stop where values begin (after threshold)
   * @returns {number[]} interpolated values (same length as stop minus threshold)
   */
  function interpolateStops(stops, score, startIdx) {
    if (score <= stops[0][0]) {
      return stops[0].slice(startIdx);
    }
    for (var i = 1; i < stops.length; i++) {
      if (score <= stops[i][0]) {
        var lo = stops[i - 1];
        var hi = stops[i];
        var t = (score - lo[0]) / (hi[0] - lo[0]);
        var result = [];
        for (var v = startIdx; v < lo.length; v++) {
          result.push(Math.round(lo[v] + t * (hi[v] - lo[v])));
        }
        return result;
      }
    }
    return stops[stops.length - 1].slice(startIdx);
  }

  /**
   * Radial mode: map fluency to saturation/lightness, preserving domain hue.
   * Use for cross-domain views where the rainbow already differentiates domains.
   *
   * @param {number} score — 0-100
   * @returns {object} {saturation, lightness} as percentages
   */
  function fluencyToSL(score) {
    var vals = interpolateStops(RADIAL_COLOR_STOPS, score, 1);
    return {saturation: vals[0], lightness: vals[1]};
  }

  /**
   * Radial mode color: domain hue + fluency-modulated saturation/lightness.
   *
   * @param {number} domainHue — HSL hue (0-360)
   * @param {number} score     — fluency score (0-100)
   * @returns {string} CSS hsl() value
   */
  function fluencyColor(domainHue, score) {
    var sl = fluencyToSL(score);
    return 'hsl(' + domainHue + ', ' + sl.saturation + '%, ' + sl.lightness + '%)';
  }

  /**
   * Mastery mode: universal color independent of domain hue.
   * Gray → red → orange → amber → yellow-green → green.
   * Use for per-domain hierarchy views where all topics share a hue
   * and you need to distinguish hundreds of nodes by fluency alone.
   *
   * @param {number} score — 0-100
   * @returns {string} CSS hsl() value
   */
  function masteryColor(score) {
    var vals = interpolateStops(MASTERY_COLOR_STOPS, score, 1);
    return 'hsl(' + vals[0] + ', ' + vals[1] + '%, ' + vals[2] + '%)';
  }

  /**
   * Find topics that are stale — touched > STALE_AGE_MS ago AND own fluency
   * falls in the [STALE_MIN_SCORE, STALE_MAX_SCORE] band. Returned sorted
   * oldest-first so the most-overdue topic surfaces first.
   *
   * Semantics: a fluency below the min band is effectively forgotten already;
   * above the max is mastered. The sweet spot in the middle is where decay
   * matters and a nudge to review pays off.
   *
   * @returns {string[]} topic IDs, stale-first
   */
  function findStaleTopics() {
    var scores = loadScores();
    var touched = loadTouched();
    var cutoff = Date.now() - STALE_AGE_MS;
    var out = [];
    for (var id in scores) {
      var s = scores[id];
      if (s < STALE_MIN_SCORE || s > STALE_MAX_SCORE) continue;
      var t = touched[id];
      if (t == null || t > cutoff) continue;
      out.push({id: id, touched: t});
    }
    out.sort(function (a, b) { return a.touched - b.touched; });
    return out.map(function (o) { return o.id; });
  }

  /**
   * Check if a topic is on the frontier (for border styling).
   *
   * @param {string} topicId
   * @param {Object} graph
   * @param {Object} effective — output of propagate()
   * @returns {boolean}
   */
  function isFrontier(topicId, graph, effective) {
    var node = graph[topicId];
    if (!node) return false;

    var ownScore = effective[topicId] || 0;
    if (ownScore >= FRONTIER_SELF_THRESHOLD) return false;

    // Match findFrontier's hard-only semantics for avgPrereq
    var prereqs = node.prereqs || [];
    var sum = 0;
    var count = 0;
    for (var p = 0; p < prereqs.length; p++) {
      if (prereqType(prereqs[p]) !== 'hard') continue;
      var pid = prereqId(prereqs[p]);
      sum += (effective[pid] || 0);
      count++;
    }
    if (count === 0) return ownScore < FRONTIER_SELF_THRESHOLD;
    return (sum / count) >= FRONTIER_PREREQ_THRESHOLD;
  }


  // ---------------------------------------------------------------------------
  // Goals
  // ---------------------------------------------------------------------------

  function addGoal(topicId) {
    var goals = loadGoals();
    if (goals.indexOf(topicId) === -1) {
      goals.push(topicId);
      saveGoals(goals);
    }
  }

  function removeGoal(topicId) {
    var goals = loadGoals();
    var idx = goals.indexOf(topicId);
    if (idx !== -1) {
      goals.splice(idx, 1);
      saveGoals(goals);
    }
  }

  function isGoal(topicId) {
    return loadGoals().indexOf(topicId) !== -1;
  }


  // ---------------------------------------------------------------------------
  // Learning path engine
  // ---------------------------------------------------------------------------

  /**
   * Mastery threshold: topics at or above this score are considered "known"
   * and excluded from learning paths.
   */
  var PATH_MASTERY_THRESHOLD = 50;

  /**
   * Compute the learning path to a single goal topic.
   * BFS backward from the goal through prerequisites, collecting all
   * unmastered topics, then topological-sort them into learning order.
   *
   * @param {Object} graph    — {topicId: {prereqs:[], successors:[], domain, course}}
   * @param {Object} scores   — {topicId: fluencyScore}
   * @param {string} goalId   — target topic ID
   * @returns {string[]} topic IDs in learning order (prereqs first, goal last)
   */
  function computePathToGoal(graph, scores, goalId) {
    if (!graph[goalId]) return [];

    // BFS backward from goal through prerequisites
    var needed = {};
    var queue = [goalId];
    needed[goalId] = true;

    while (queue.length > 0) {
      var current = queue.shift();
      var node = graph[current];
      if (!node) continue;
      var prereqs = node.prereqs || [];
      for (var i = 0; i < prereqs.length; i++) {
        var pid = prereqId(prereqs[i]);
        if (pid && !needed[pid] && graph[pid]) {
          needed[pid] = true;
          queue.push(pid);
        }
      }
    }

    // Filter out already-mastered topics (but always include the goal itself)
    var unmastered = [];
    for (var id in needed) {
      if ((scores[id] || 0) < PATH_MASTERY_THRESHOLD || id === goalId) {
        unmastered.push(id);
      }
    }

    // Build subgraph and topo-sort
    var subgraph = {};
    for (var u = 0; u < unmastered.length; u++) {
      var uid = unmastered[u];
      var orig = graph[uid];
      // Only include successors that are in our unmastered set
      var filteredSucc = [];
      var succs = orig.successors || [];
      for (var s = 0; s < succs.length; s++) {
        var sid = prereqId(succs[s]);
        if (sid && needed[sid] && ((scores[sid] || 0) < PATH_MASTERY_THRESHOLD || sid === goalId)) {
          filteredSucc.push(succs[s]);
        }
      }
      subgraph[uid] = {prereqs: orig.prereqs, successors: filteredSucc};
    }

    return topoSort(subgraph);
  }

  /**
   * Compute a unified learning path across all starred goals.
   * Merges per-goal paths, deduplicates, and sorts by readiness.
   *
   * @param {Object} graph   — full prerequisite graph
   * @param {Object} scores  — {topicId: fluencyScore}
   * @returns {Object} {path: string[], goals: string[], stats: {total, mastered, remaining}}
   */
  function computeLearningPath(graph, scores) {
    var goals = loadGoals();
    if (goals.length === 0) return {path: [], goals: [], stats: {total: 0, mastered: 0, remaining: 0}};

    // Collect all needed topics across all goals
    var allNeeded = {};
    var validGoals = [];

    for (var g = 0; g < goals.length; g++) {
      if (!graph[goals[g]]) continue;
      validGoals.push(goals[g]);
      var path = computePathToGoal(graph, scores, goals[g]);
      for (var p = 0; p < path.length; p++) {
        allNeeded[path[p]] = true;
      }
    }

    // Build subgraph of all needed topics and topo-sort
    var subgraph = {};
    for (var id in allNeeded) {
      var orig = graph[id];
      if (!orig) continue;
      var filteredSucc = [];
      var succs = orig.successors || [];
      for (var s = 0; s < succs.length; s++) {
        var sid = prereqId(succs[s]);
        if (sid && allNeeded[sid]) filteredSucc.push(succs[s]);
      }
      subgraph[id] = {prereqs: orig.prereqs, successors: filteredSucc};
    }

    var sorted = topoSort(subgraph);

    // Count stats
    var totalInPath = sorted.length;
    var mastered = 0;
    for (var t = 0; t < sorted.length; t++) {
      if ((scores[sorted[t]] || 0) >= PATH_MASTERY_THRESHOLD) mastered++;
    }

    return {
      path: sorted,
      goals: validGoals,
      stats: {total: totalInPath, mastered: mastered, remaining: totalInPath - mastered},
    };
  }


  // ---------------------------------------------------------------------------
  // Confidence API
  // ---------------------------------------------------------------------------

  /**
   * Get the confidence for a topic (0-1).
   * 0 = no data, 1 = very confident (multiple direct answers).
   */
  function getConfidence(topicId) {
    var conf = loadConfidence();
    return conf[topicId] || 0;
  }

  /**
   * Directly set confidence for a topic.
   * @param {string} topicId
   * @param {number} confidence — 0 to 1
   */
  function setConfidence(topicId, confidence) {
    var conf = loadConfidence();
    conf[topicId] = Math.max(0, Math.min(1, confidence));
    saveConfidence(conf);
  }


  // ---------------------------------------------------------------------------
  // Post-assessment inference
  // ---------------------------------------------------------------------------

  /**
   * Stages in developmental order (must match assessment data).
   */
  var STAGE_ORDER = [
    'pre-formal', 'concrete-operations', 'abstract-reasoning',
    'formal-systems', 'advanced', 'expert'
  ];

  /**
   * Run post-assessment inference to fill in untested topics.
   *
   * After a quiz session, this function infers fluency for topics the user
   * wasn't directly tested on, based on demonstrated performance at various
   * developmental stages.
   *
   * Logic:
   *   1. Overall academic tier: estimate the user's general level
   *      (child / middle-school / high-school / college / graduate) based
   *      on the highest stage demonstrated across multiple domains.
   *      Apply universal floors to "general education" domains based on tier.
   *      Specialized domains (music, arts) only get floors with specific evidence.
   *
   *   2. Per-domain ceiling: find the highest stage where the user got ANY
   *      question correct. All topics at that stage and below get fluency
   *      floors. Topics one stage ABOVE the ceiling get a tentative floor.
   *
   *   3. Scores only go UP — inference never lowers a directly-tested score.
   *      Confidence for inferred topics is always lower than direct answers.
   *
   * @param {Object} domainPerformance — {domain: {stage: {correct, total}}}
   *   Performance per domain per stage from the quiz session.
   * @param {Object} topicIndex — {domain: {stage: [topicId, ...]}}
   *   Complete index of all topics by domain and stage.
   * @returns {Object} {topicsInferred, domainsProcessed, crossDomainApplied}
   */
  // Domains where general academic competence implies foundational knowledge.
  // If you have a college degree, you likely know HS-level content in these.
  var GENERAL_ED_DOMAINS = [
    'mathematics', 'language-and-communication', 'biology', 'chemistry',
    'physics', 'earth-and-space-sciences', 'health-and-human-development',
    'social-sciences', 'economics', 'practical-life-skills', 'psychology',
    'history', 'literature', 'computer-science'
  ];

  // Domains requiring specific exposure — only infer from direct evidence.
  // (music, arts, engineering, formal-sciences, philosophy)

  function postAssessmentInference(domainPerformance, topicIndex) {
    var scores = loadScores();
    var conf = loadConfidence();
    var topicsInferred = 0;
    var domainsProcessed = 0;

    // Helper: set floor on a list of topics (only raises, never lowers)
    // force=true overrides confidence guard (for strong within-domain inference)
    function applyFloor(topicIds, floor, inferConf, force) {
      if (!topicIds) return;
      for (var i = 0; i < topicIds.length; i++) {
        var tid = topicIds[i];
        var current = scores[tid] || 0;
        var currentConf = conf[tid] || 0;
        // Force mode: override even if confidence is high (for stages far below demonstrated)
        // Normal mode: only override low-confidence topics
        if (current < floor && (force || currentConf < 0.6)) {
          scores[tid] = floor;
          conf[tid] = Math.max(currentConf, inferConf);
          topicsInferred++;
        }
      }
    }

    // ---------------------------------------------------------------
    // Step 1: Estimate overall academic tier
    // ---------------------------------------------------------------
    // For each stage, count how many domains the user got at least 1 right.
    // Tier = highest stage demonstrated in 2+ domains.
    var stageHits = [];  // stageHits[stageIdx] = count of domains with a correct answer
    for (var sti = 0; sti < STAGE_ORDER.length; sti++) {
      var count = 0;
      for (var d in domainPerformance) {
        var sp = domainPerformance[d][STAGE_ORDER[sti]];
        if (sp && sp.correct >= 1) count++;
      }
      stageHits.push(count);
    }

    // Tier = highest stage with 2+ domain hits (or 1+ for advanced)
    var overallTier = -1;
    for (var ti = STAGE_ORDER.length - 1; ti >= 0; ti--) {
      var needed = ti >= 4 ? 1 : 2;  // advanced only needs 1 domain
      if (stageHits[ti] >= needed) {
        overallTier = ti;
        break;
      }
    }

    // ---------------------------------------------------------------
    // Step 2: Apply tier-based universal floors (general-ed domains)
    // ---------------------------------------------------------------
    // If we estimate the user is at tier T, they likely know content
    // at stages well below T in general-education domains.
    //
    // Tier 0 (pre-formal):          no inference
    // Tier 1 (concrete):            pre-formal → 85
    // Tier 2 (abstract/HS):         pre-formal → 90, concrete → 80
    // Tier 3 (formal/college):      pre-formal → 92, concrete → 85, abstract → 75
    // Tier 4 (advanced/graduate):   pre-formal → 95, concrete → 90, abstract → 82, formal → 70

    var tierFloors = [
      // [stageIdx]: [floor, confidence]  — applied if stageIdx < overallTier
      // indexed by distance below tier: distance 1, 2, 3, 4
    ];
    if (overallTier >= 1) {
      // Apply floors to general-ed domains for stages below the tier
      var isGeneralEd = {};
      for (var ge = 0; ge < GENERAL_ED_DOMAINS.length; ge++) {
        isGeneralEd[GENERAL_ED_DOMAINS[ge]] = true;
      }

      // Cross-domain inference is conservative — only apply to stages
      // 2+ below tier (pre-formal, concrete for a college-level user).
      // This avoids over-inferring specific content knowledge (e.g.,
      // knowing college math doesn't mean knowing Tang Dynasty history).
      for (var gd in topicIndex) {
        if (!isGeneralEd[gd]) continue;

        for (var si2 = 0; si2 < overallTier; si2++) {
          var dist = overallTier - si2;
          if (dist < 2) continue;  // Only infer stages 2+ below tier
          // Higher distance below tier = more confident they know it
          var tFloor = Math.min(90, 60 + dist * 7);
          var tConf = Math.min(0.35, 0.10 + dist * 0.06);
          applyFloor(topicIndex[gd][STAGE_ORDER[si2]], tFloor, tConf);
        }
      }
    }

    // ---------------------------------------------------------------
    // Step 3: Per-domain ceiling inference (all domains, including specialized)
    // ---------------------------------------------------------------
    for (var domain in domainPerformance) {
      var domainPerf = domainPerformance[domain];
      if (!topicIndex[domain]) continue;

      // Find the highest stage where user got ANY question correct
      var ceilingIdx = -1;
      for (var ci = STAGE_ORDER.length - 1; ci >= 0; ci--) {
        var csp = domainPerf[STAGE_ORDER[ci]];
        if (csp && csp.correct >= 1) {
          ceilingIdx = ci;
          break;
        }
      }

      if (ceilingIdx < 0) continue;
      domainsProcessed++;

      // Fill stages BELOW the ceiling — use force for stages 2+ below
      // (if you answer college-level math, you definitely know 2nd-grade math)
      for (var belowIdx = 0; belowIdx < ceilingIdx; belowIdx++) {
        var distance = ceilingIdx - belowIdx;
        var floor = Math.min(95, 75 + distance * 5);
        var inferConf = Math.min(0.55, 0.25 + distance * 0.08);
        var force = distance >= 2;  // Force override for stages well below demonstrated
        applyFloor(topicIndex[domain][STAGE_ORDER[belowIdx]], floor, inferConf, force);
      }

      // Fill AT the ceiling stage
      applyFloor(topicIndex[domain][STAGE_ORDER[ceilingIdx]], 68, 0.3);

      // Fill ONE ABOVE the ceiling (tentative)
      if (ceilingIdx + 1 < STAGE_ORDER.length) {
        applyFloor(topicIndex[domain][STAGE_ORDER[ceilingIdx + 1]], 45, 0.12);
      }
    }

    saveScores(scores);
    saveConfidence(conf);

    return {
      topicsInferred: topicsInferred,
      domainsProcessed: domainsProcessed,
      overallTier: overallTier >= 0 ? STAGE_ORDER[overallTier] : null,
      crossDomainApplied: overallTier >= 1,
    };
  }


  // ---------------------------------------------------------------------------
  // Import / Export
  // ---------------------------------------------------------------------------

  /**
   * Export all fluency data as a JSON-serializable object.
   * For cross-device transfer or backup.
   */
  function exportData() {
    return {
      version: VERSION,
      exportedAt: new Date().toISOString(),
      fluency: loadScores(),
      confidence: loadConfidence(),
      meta: loadMeta(),
      goals: loadGoals(),
      adjustments: loadAdjustments(),
    };
  }

  /**
   * Import fluency data from an exported object.
   * Merges with existing data (higher score wins per topic).
   *
   * @param {Object} data — output of exportData()
   * @param {boolean} [overwrite=false] — if true, replaces instead of merging
   */
  function importData(data, overwrite) {
    if (!data || data.version !== VERSION) {
      throw new Error('Incompatible fluency data version');
    }

    if (overwrite) {
      saveScores(data.fluency || {});
      saveConfidence(data.confidence || {});
      saveMeta(data.meta || {});
      saveGoals(data.goals || []);
      saveAdjustments(data.adjustments || {});
      return;
    }

    // Merge scores: higher score wins
    var existing = loadScores();
    var incoming = data.fluency || {};
    for (var id in incoming) {
      if (!existing[id] || incoming[id] > existing[id]) {
        existing[id] = incoming[id];
      }
    }
    saveScores(existing);

    // Merge confidence: higher confidence wins
    var existingConf = loadConfidence();
    var incomingConf = data.confidence || {};
    for (var cid in incomingConf) {
      if (!existingConf[cid] || incomingConf[cid] > existingConf[cid]) {
        existingConf[cid] = incomingConf[cid];
      }
    }
    saveConfidence(existingConf);

    // Merge goals (union)
    var existingGoals = loadGoals();
    var incomingGoals = data.goals || [];
    for (var g = 0; g < incomingGoals.length; g++) {
      if (existingGoals.indexOf(incomingGoals[g]) === -1) {
        existingGoals.push(incomingGoals[g]);
      }
    }
    saveGoals(existingGoals);

    // Merge adjustments (incoming wins)
    var existingAdj = loadAdjustments();
    var incomingAdj = data.adjustments || {};
    for (var course in incomingAdj) {
      existingAdj[course] = incomingAdj[course];
    }
    saveAdjustments(existingAdj);
  }

  /**
   * Clear all fluency data. Requires confirmation string.
   * @param {string} confirm — must be "RESET" to proceed
   */
  function resetAll(confirm) {
    if (confirm !== 'RESET') return false;
    localStorage.removeItem(STORAGE_KEYS.fluency);
    localStorage.removeItem(STORAGE_KEYS.confidence);
    localStorage.removeItem(STORAGE_KEYS.meta);
    localStorage.removeItem(STORAGE_KEYS.goals);
    localStorage.removeItem(STORAGE_KEYS.adjustments);
    return true;
  }


  // ---------------------------------------------------------------------------
  // Summary / Stats
  // ---------------------------------------------------------------------------

  /**
   * Get a summary of current fluency state.
   * @returns {Object} {totalTracked, averageFluency, topicsByBand, totalAnswered}
   */
  function summary() {
    var scores = loadScores();
    var meta = loadMeta();
    var ids = Object.keys(scores);
    var total = ids.length;

    if (total === 0) {
      return {
        totalTracked: 0,
        averageFluency: 0,
        topicsByBand: {unknown: 0, beginner: 0, developing: 0, proficient: 0, mastered: 0},
        totalAnswered: meta.totalAnswered || 0,
      };
    }

    var sum = 0;
    var bands = {unknown: 0, beginner: 0, developing: 0, proficient: 0, mastered: 0};

    for (var i = 0; i < ids.length; i++) {
      var s = scores[ids[i]];
      sum += s;
      if (s <= 0)       bands.unknown++;
      else if (s <= 25)  bands.beginner++;
      else if (s <= 50)  bands.developing++;
      else if (s <= 75)  bands.proficient++;
      else               bands.mastered++;
    }

    return {
      totalTracked: total,
      averageFluency: Math.round(sum / total),
      topicsByBand: bands,
      totalAnswered: meta.totalAnswered || 0,
    };
  }


  // ---------------------------------------------------------------------------
  // Public API
  // ---------------------------------------------------------------------------

  return {
    // Core
    updateTopic:    updateTopic,
    setScore:       setScore,
    getScore:       getScore,
    bulkSetScores:  bulkSetScores,
    loadScores:     loadScores,

    // Confidence
    getConfidence:  getConfidence,
    setConfidence:  setConfidence,
    loadConfidence: loadConfidence,

    // Propagation
    propagate:      propagate,
    findFrontier:   findFrontier,
    findStaleTopics: findStaleTopics,
    isFrontier:     isFrontier,

    // Touch tracking
    loadTouched:    loadTouched,
    markTouched:    markTouched,

    // Post-assessment inference
    postAssessmentInference: postAssessmentInference,

    // Colors
    fluencyColor:   fluencyColor,   // radial mode: domain hue + fluency S/L
    masteryColor:   masteryColor,   // mastery mode: universal gradient (for per-domain views)
    fluencyToSL:    fluencyToSL,

    // Goals & Learning Paths
    addGoal:        addGoal,
    removeGoal:     removeGoal,
    isGoal:         isGoal,
    loadGoals:      loadGoals,
    computePathToGoal:   computePathToGoal,
    computeLearningPath: computeLearningPath,

    // Adjustments
    loadAdjustments: loadAdjustments,
    saveAdjustments: saveAdjustments,

    // Cold-start prior (user stage + domain prior)
    getUserStage:   getUserStage,
    setUserStage:   setUserStage,
    getDomainPrior: getDomainPrior,
    setDomainPrior: setDomainPrior,
    stageIndex:     stageIndex,
    computeFloor:   computeFloor,

    // Import/Export
    exportData:     exportData,
    importData:     importData,
    resetAll:       resetAll,

    // Stats
    summary:        summary,

    // Constants (exposed for testing/tuning)
    BACKWARD_DECAY:            BACKWARD_DECAY,
    FORWARD_CAP_WEIGHT:        FORWARD_CAP_WEIGHT,
    WRONG_PENALTY_MULT:        WRONG_PENALTY_MULT,
    FRONTIER_PREREQ_THRESHOLD: FRONTIER_PREREQ_THRESHOLD,
    FRONTIER_SELF_THRESHOLD:   FRONTIER_SELF_THRESHOLD,
    VERSION:                   VERSION,
  };

})();
