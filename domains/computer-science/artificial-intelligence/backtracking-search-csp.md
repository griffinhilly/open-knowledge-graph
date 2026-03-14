---
id: backtracking-search-csp
title: Backtracking Search for CSPs
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: constraint-satisfaction-problems
  type: hard
- id: recursion-basics
  type: hard
- id: depth-first-search
  type: soft
builds-toward:
- constraint-propagation
tags:
- search
- csp
- backtracking
- variable-ordering
stage: advanced
status: draft
---

# Backtracking Search for CSPs

## Core Idea
Backtracking search systematically explores the solution space by assigning variables one at a time and undoing assignments when conflicts arise. Variable ordering heuristics (minimum remaining values, degree heuristic) and value ordering (least constraining value) dramatically improve performance by reducing the branching factor. The search can be dramatically accelerated by combining with constraint propagation.

## How It's Best Learned
Implement backtracking with and without the MRV heuristic on map coloring or N-queens to observe performance differences.
