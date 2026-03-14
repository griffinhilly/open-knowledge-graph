---
id: logarithmic-space-classes
title: Logarithmic Space Classes (L and NL)
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: space-complexity-classes-formal
  type: hard
builds-toward:
- nl-completeness
tags:
- space-complexity
- resource-bounded
- turing-machines
stage: advanced
status: draft
---

# Logarithmic Space Classes (L and NL)

## Core Idea
L (deterministic log space) and NL (nondeterministic log space) are fundamental space-bounded complexity classes capturing problems solvable with logarithmic auxiliary space. While it is unknown whether L = NL, Savitch's theorem shows NL ⊆ P, placing space-bounded computation between log space and polynomial time. These classes model algorithm design where space is severely constrained relative to input size.

## How It's Best Learned
Consider what computation is possible with log-space: you can store a few pointers and counters but not the entire input. Understand Savitch's theorem by simulating nondeterministic choices via DFS with limited space.
