---
id: monte-carlo-tree-search
title: Monte Carlo Tree Search
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: algorithm-design-basics
  type: hard
- id: probability
  type: soft
- id: expected-value
  type: soft
tags:
- search
- monte-carlo
- games
- sampling
stage: advanced
status: draft
---

# Monte Carlo Tree Search

## Core Idea
MCTS builds a game tree incrementally through random simulations. Each iteration selects nodes using UCB, expands children, runs random playouts, and backpropagates results. It excels in large branching-factor games where evaluation functions are unavailable, balancing exploration and exploitation.
