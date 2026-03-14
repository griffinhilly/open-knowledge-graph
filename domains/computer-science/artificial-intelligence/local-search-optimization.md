---
id: local-search-optimization
title: Local Search Optimization
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: algorithm-design-basics
  type: hard
- id: greedy-algorithms
  type: soft
builds-toward:
- simulated-annealing
- genetic-algorithms
tags:
- optimization
- local-search
- hill-climbing
- metaheuristics
stage: advanced
status: draft
---

# Local Search Optimization

## Core Idea
Local search maintains a single current state and iteratively moves to neighboring states, useful for optimization problems where the path is irrelevant and only the goal state matters. Methods like hill climbing, simulated annealing, and tabu search balance exploration (escaping local optima) and exploitation (converging to good solutions). Local search trades completeness for efficiency, making it applicable to large combinatorial problems.

## How It's Best Learned
Implement hill climbing on a landscape with multiple local optima to understand the problem, then compare with simulated annealing to see how probabilistic moves help escape local optima.
