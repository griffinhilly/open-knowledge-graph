---
id: space-hierarchy-theorem
title: Space Hierarchy Theorem
domain: computer-science
course: theory-of-computation
prerequisites:
- id: space-complexity-classes
  type: hard
- id: turing-machines
  type: hard
builds-toward:
- pspace-complexity-class
tags:
- complexity-theory
- hierarchy
- provable-separation
stage: advanced
status: draft
---

# Space Hierarchy Theorem

## Core Idea
The space hierarchy theorem states that for space-constructible f(n) ≥ log n, DSPACE(f(n)) ⊂ DSPACE(f(n) log f(n)). Unlike time (which requires quadratic growth), space only needs logarithmic growth because space is 'reusable'—the machine can overwrite previous values. The theorem shows space classes strictly increase even with tighter bounds than time, but the proof technique differs fundamentally: verifying space usage requires tracking maximum usage, not cumulative cost.

## Explainer

From your study of space complexity classes, you know that DSPACE(f(n)) collects all languages decidable by a deterministic Turing machine using at most f(n) tape cells. A natural question follows: does giving a machine genuinely more space let it solve strictly more problems? The space hierarchy theorem answers yes — and it does so with a surprisingly tight bound. If you allow a machine f(n) · log f(n) space instead of f(n), there exist languages decidable with the larger budget that no f(n)-bounded machine can handle. The strict inclusion DSPACE(f(n)) ⊊ DSPACE(f(n) log f(n)) is provable, not conjectured.

The proof uses **diagonalization**, the same technique that underlies the halting problem and the time hierarchy theorem, but adapted for space. The key idea is to construct a language L that a machine M with the larger space budget can decide by simulating every f(n)-bounded machine and then doing the opposite of what each one does on a carefully chosen input. The simulator needs to track how much space the simulated machine uses, and this bookkeeping — counting tape cells up to f(n) — costs an additional log f(n) factor, since writing down a number up to f(n) requires log f(n) bits.

Compare this to the time hierarchy theorem, which requires a quadratic blowup: DTIME(f(n)) ⊊ DTIME(f(n)²). The reason space gets away with only a logarithmic overhead is that **space is reusable**. A Turing machine can overwrite tape cells and reuse them for different parts of the simulation. Time, once spent, is gone forever — each simulation step of the simulated machine costs the simulator real steps, and the overhead accumulates multiplicatively. Space overhead, by contrast, only reflects the maximum simultaneous usage, not cumulative consumption. This reusability is what makes space hierarchies tighter than time hierarchies.

The practical consequence is a clean ladder of provably distinct complexity classes. DSPACE(n) is strictly contained in DSPACE(n log n), which is strictly contained in DSPACE(n²), and so on. Each rung of the ladder contains languages that genuinely require that much space — no clever algorithm can compress them into a smaller class. This is powerful because most separations in complexity theory (like P vs. NP) remain unproven. The hierarchy theorems are among the few tools that deliver unconditional, proven separations between complexity classes, giving the field its backbone of known structure.
