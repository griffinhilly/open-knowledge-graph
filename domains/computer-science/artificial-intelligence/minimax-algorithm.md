---
id: minimax-algorithm
title: Minimax Algorithm
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: algorithm-design-basics
  type: hard
- id: recursion-basics
  type: hard
- id: proof-by-cases
  type: soft
tags:
- adversarial-search
- games
- game-theory
stage: advanced
status: draft
---

# Minimax Algorithm

## Core Idea
Minimax is a recursive algorithm for two-player zero-sum games where one player maximizes utility and the other minimizes it. Values propagate from leaves: max nodes return the maximum child value, min nodes return the minimum. The algorithm assumes both players play optimally.
