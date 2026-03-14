---
id: heuristic-search-functions
title: Heuristic Search Functions
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: astar-search-algorithm
  type: hard
- id: greedy-algorithms
  type: soft
builds-toward:
- local-search-optimization
- constraint-propagation
tags:
- search
- heuristics
- admissibility
- optimization
stage: advanced
status: draft
---

# Heuristic Search Functions

## Core Idea
Heuristic functions estimate the cost from a state to the goal without exploring the full search space, enabling guided search. Well-designed heuristics must be admissible (never overestimate) to guarantee optimal solutions, and consistent heuristics satisfy the triangle inequality to enable efficient pruning. The quality of the heuristic determines whether A* will terminate quickly or explore exponentially many states.

## How It's Best Learned
Study examples of admissible heuristics like Manhattan distance for grid puzzles and implement A* with different heuristics to observe how heuristic quality affects search performance.

## Common Misconceptions
A faster heuristic is always better (domination matters: h1 dominates h2 if h1(s) ≥ h2(s) for all s). Optimality requires admissibility, not just consistency.
