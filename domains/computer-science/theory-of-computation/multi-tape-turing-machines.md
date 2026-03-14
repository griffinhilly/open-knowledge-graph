---
id: multi-tape-turing-machines
title: Multi-Tape Turing Machines and Simulation
domain: computer-science
course: theory-of-computation
prerequisites:
- id: turing-machine-model-and-definition
  type: hard
builds-toward:
- universal-turing-machine
tags:
- multi-tape
- simulation
- equivalence
- time-complexity
- encoding
stage: advanced
status: draft
---

# Multi-Tape Turing Machines and Simulation

## Core Idea
Multi-tape TMs have multiple tapes and heads, enabling parallel processing. Despite this apparent enhancement, they recognize no more languages than single-tape TMs. A single-tape TM can simulate multi-tape in quadratic time by encoding all tapes on one tape. This shows that language class is model-independent, though time complexity depends on efficiency of simulation.
