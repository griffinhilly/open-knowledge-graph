// Regression test for the origin-layer fluency guards (plans/origin-layer-spec.md sec 0.2).
// Run: node tools/test_fluency_capacity.js
//
// Loads the REAL lib/fluency.js with a localStorage stub and asserts:
//  (1) a kind:capacity hard prereq NEVER caps its successor (the premortem-verified bug);
//  (2) a normal kind:topic hard prereq STILL caps (control — proves the test is live, not a no-op);
//  (3) adding a capacity prereq lowers no successor's effective score (before/after on a chain);
//  (4) computePathToGoal never surfaces a kind:capacity node (assumed-known for learners).
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const FLUENCY_PATH = path.resolve(__dirname, '..', 'lib', 'fluency.js');

function makeLS(initial) {
  const store = Object.assign({}, initial);
  return {
    getItem: (k) => (k in store ? store[k] : null),
    setItem: (k, v) => { store[k] = String(v); },
    removeItem: (k) => { delete store[k]; },
    clear: () => { for (const k in store) delete store[k]; },
  };
}

function loadFluency(localStorageStub) {
  const src = fs.readFileSync(FLUENCY_PATH, 'utf8');
  const sandbox = { localStorage: localStorageStub, console, JSON, Math, Object, Array, Date };
  sandbox.globalThis = sandbox;
  vm.createContext(sandbox);
  vm.runInContext(src + '\n;this.__OKG = OKGFluency;', sandbox);
  return sandbox.__OKG;
}

let failures = 0;
function assert(name, cond, detail) {
  if (cond) { console.log('  PASS  ' + name); }
  else { console.log('  FAIL  ' + name + '  ' + (detail || '')); failures++; }
}

// (1) capacity prereq must NOT cap successor
{
  const F = loadFluency(makeLS({ 'okg-fluency': JSON.stringify({ A: 100, B: 100 }) }));
  const graph = {
    A: { prereqs: [], successors: [{ id: 'B', type: 'hard' }], kind: 'capacity' },
    B: { prereqs: [{ id: 'A', type: 'hard' }], successors: [], kind: 'topic' },
  };
  const eff = F.propagate(graph);
  assert('capacity prereq does NOT cap successor (B stays 100)', eff.B === 100, 'B=' + eff.B);
}

// (2) CONTROL: a normal topic prereq STILL caps
{
  const F = loadFluency(makeLS({ 'okg-fluency': JSON.stringify({ A2: 100, B2: 100 }) }));
  const graph = {
    A2: { prereqs: [], successors: [{ id: 'B2', type: 'hard' }], kind: 'topic' },
    B2: { prereqs: [{ id: 'A2', type: 'hard' }], successors: [], kind: 'topic' },
  };
  const eff = F.propagate(graph);
  assert('control: normal topic prereq DOES cap successor (B2 -> 90)', eff.B2 === 90, 'B2=' + eff.B2);
}

// (3) adding a capacity prereq lowers no successor's effective score
{
  const baseGraph = () => ({
    root: { prereqs: [], successors: [{ id: 'mid', type: 'hard' }], kind: 'topic' },
    mid: { prereqs: [{ id: 'root', type: 'hard' }], successors: [{ id: 'deep', type: 'hard' }], kind: 'topic' },
    deep: { prereqs: [{ id: 'mid', type: 'hard' }], successors: [], kind: 'topic' },
  });
  const Fa = loadFluency(makeLS({ 'okg-fluency': JSON.stringify({ deep: 100, root: 100, mid: 100 }) }));
  const before = Fa.propagate(baseGraph());

  const withCap = baseGraph();
  withCap.cap = { prereqs: [], successors: [{ id: 'root', type: 'hard' }], kind: 'capacity' };
  withCap.root.prereqs = [{ id: 'cap', type: 'hard' }];
  const Fb = loadFluency(makeLS({ 'okg-fluency': JSON.stringify({ deep: 100, root: 100, mid: 100, cap: 100 }) }));
  const after = Fb.propagate(withCap);

  assert('adding capacity prereq lowers no successor (root)', after.root >= before.root, 'before=' + before.root + ' after=' + after.root);
  assert('adding capacity prereq lowers no successor (mid)', after.mid >= before.mid, 'before=' + before.mid + ' after=' + after.mid);
  assert('adding capacity prereq lowers no successor (deep)', after.deep >= before.deep, 'before=' + before.deep + ' after=' + after.deep);
}

// (4) path pruning: capacity never surfaces in a learner path
{
  const F = loadFluency(makeLS({}));
  const graph = {
    goal: { prereqs: [{ id: 'r', type: 'hard' }], successors: [], kind: 'topic' },
    r: { prereqs: [{ id: 'cap', type: 'hard' }], successors: [{ id: 'goal', type: 'hard' }], kind: 'topic' },
    cap: { prereqs: [], successors: [{ id: 'r', type: 'hard' }], kind: 'capacity' },
  };
  const p = F.computePathToGoal(graph, {}, 'goal');
  assert('computePathToGoal excludes capacity node', p.indexOf('cap') === -1, 'path=' + JSON.stringify(p));
  assert('computePathToGoal still includes the real root r', p.indexOf('r') !== -1, 'path=' + JSON.stringify(p));
}

console.log(failures === 0 ? '\nALL PASS' : '\n' + failures + ' FAILED');
process.exit(failures === 0 ? 0 : 1);
