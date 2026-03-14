---
id: mealy-moore-machines
title: Mealy and Moore Machines
domain: computer-science
course: theory-of-computation
prerequisites:
- id: deterministic-finite-automata
  type: hard
- id: finite-state-machines
  type: hard
tags:
- automata
- output-machines
- transducers
stage: advanced
status: draft
---

# Mealy and Moore Machines

## Core Idea
Mealy and Moore machines extend finite automata with output. Moore machines output from states (output = f(state)); Mealy machines output from transitions (output = g(state, input)). Both recognize the same input languages but differ in output timing: Moore machines are synchronous, Mealy machines asynchronous. Both are equivalent in power and widely model digital sequential circuits, protocol controllers, and stateful transducers where input and output are intertwined.
