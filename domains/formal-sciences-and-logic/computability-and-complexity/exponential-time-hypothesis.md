---
id: exponential-time-hypothesis
title: Exponential Time Hypothesis (ETH)
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: np-completeness-formal
  type: hard
- id: time-complexity-classes-formal
  type: soft
tags:
- conjecture
- lower-bounds
- hardness
stage: advanced
status: draft
---

# Exponential Time Hypothesis (ETH)

## Core Idea
The Exponential Time Hypothesis (ETH) conjectures that 3-SAT requires time 2^(c·n) for some constant c > 0, implying SAT cannot be solved in 2^(o(n)) time. ETH is a refined hardness assumption stronger than P ≠ NP but potentially weaker than assuming exponential lower bounds hold universally. It has become influential for proving conditional lower bounds: many problems' hardness is established assuming ETH holds.
