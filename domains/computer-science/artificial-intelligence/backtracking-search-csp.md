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

## Explainer

You already know that a constraint satisfaction problem (CSP) consists of variables, domains (possible values for each variable), and constraints (rules about which combinations of values are allowed). A naive approach would enumerate every possible combination of values and check each one — but for a problem with n variables each having d possible values, that means checking d^n combinations, which quickly becomes intractable. **Backtracking search** improves on this by building assignments incrementally: assign one variable at a time, and the moment an assignment violates a constraint, immediately undo it and try a different value. This is the key insight from recursion and depth-first search applied to CSPs — you explore one branch deeply, and when you hit a dead end, you back up to the most recent choice point.

The basic backtracking algorithm works like a depth-first search through the space of partial assignments. Pick an unassigned variable, try a value from its domain, check if it is consistent with all constraints involving already-assigned variables, and if so, recurse to assign the next variable. If no value works, return failure — this triggers backtracking to the previous variable, which tries its next value. The recursion bottoms out successfully when all variables are assigned consistently. Even this simple approach is far better than brute-force enumeration because it prunes entire subtrees as soon as a conflict is detected, rather than waiting until all variables are assigned.

What makes backtracking practical for large CSPs is the choice of **heuristics** for variable and value ordering. The **minimum remaining values (MRV)** heuristic selects the variable with the fewest legal values remaining in its domain — the idea being that this variable is most likely to cause a failure, and it is better to fail early than to waste time assigning other variables first. Think of it as tackling the hardest constraint first. The **degree heuristic** breaks MRV ties by preferring the variable involved in the most constraints on unassigned variables, maximizing the pruning effect. For value ordering, the **least constraining value (LCV)** heuristic picks the value that rules out the fewest choices for neighboring variables — giving the rest of the problem the best chance of being solvable.

Consider the classic map-coloring problem: color the regions of a map with three colors such that no adjacent regions share a color. Without heuristics, the algorithm might start with a region that has many valid options and only discover deep in the search that a tightly constrained region has no valid color left. With MRV, it starts with the most constrained region, detects failures immediately, and avoids exploring large portions of the search tree that can never lead to a solution. The difference in practice can be enormous — from millions of nodes explored down to hundreds. When combined with constraint propagation techniques like arc consistency, backtracking search becomes powerful enough to solve real-world CSPs with thousands of variables.
