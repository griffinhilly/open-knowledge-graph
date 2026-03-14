---
id: two-way-finite-automata
title: Two-Way Finite Automata
domain: computer-science
course: theory-of-computation
prerequisites:
- id: deterministic-finite-automata
  type: hard
- id: nondeterministic-finite-automata
  type: hard
tags:
- automata
- bidirectional-reading
- equivalence
stage: advanced
status: draft
---

# Two-Way Finite Automata

## Core Idea
A two-way finite automaton (2DFA) can move its read head left or right on the input (unlike standard DFA/NFA, restricted to rightward movement). Remarkably, 2DFA and 2NFA recognize exactly the regular languages—bidirectional movement alone doesn't increase expressiveness. However, 2DFAs may require exponentially more states than equivalent standard DFAs. This separation shows movement power differs from computational power; state complexity, not directionality, determines expressiveness.
