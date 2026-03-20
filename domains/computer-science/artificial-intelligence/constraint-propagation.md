---
id: constraint-propagation
title: Constraint Propagation
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: constraint-satisfaction-problems
  type: hard
- id: algorithm-design-basics
  type: soft
builds-toward: []
tags:
- constraints
- csp
- domain-reduction
- inference
stage: advanced
status: draft
---
# Constraint Propagation

## Core Idea
Constraint propagation reduces the search space by eliminating values from variable domains that cannot satisfy constraints, even before search begins. Techniques like arc consistency (AC-3) detect unsatisfiable constraints early and can sometimes solve CSPs without any backtracking. The consistency check is polynomial but repeated propagation increases algorithm complexity.

## How It's Best Learned
Implement AC-3 and trace through a small CSP by hand to understand how arc consistency eliminates values iteratively.

## Common Misconceptions
Constraint propagation always finds a solution (it only ensures consistency, not satisfiability). AC-3 is the strongest consistency check (higher-order consistencies like k-consistency are stronger but more expensive).

## Explainer

In a constraint satisfaction problem, you have variables with domains of possible values and constraints that restrict which combinations are allowed. A brute-force approach would try every possible assignment and check constraints at the end. Backtracking improves on this by checking constraints as it goes. **Constraint propagation** goes further still: it reasons about constraints *before and during* search to eliminate values that can never participate in a valid solution, shrinking the search space without ever guessing.

The core idea is **arc consistency**. An arc is a directed edge from variable X to variable Y in the constraint graph. X is arc-consistent with respect to Y if, for every value in X's domain, there exists at least one value in Y's domain that satisfies the constraint between them. If some value x in X's domain has no compatible value in Y's domain, then x can never be part of a valid solution — so you can safely remove it. The **AC-3 algorithm** enforces arc consistency across the entire problem by maintaining a queue of arcs to check. When a value is removed from a variable's domain, all arcs pointing to that variable are re-added to the queue, because the removal might make previously consistent values in neighboring variables now inconsistent. The process repeats until no more values can be removed.

Consider a concrete example: a Sudoku puzzle. Each cell is a variable with domain {1–9}, and constraints require that each row, column, and 3×3 box contains distinct values. When you place a 5 in a cell, constraint propagation immediately removes 5 from the domains of every other cell in the same row, column, and box. If that removal leaves some other cell with only one possible value, that value is propagated further, potentially triggering a cascade of deductions. In easy Sudoku puzzles, arc consistency alone solves the entire puzzle with no search at all. In harder puzzles, it dramatically reduces the domains before backtracking search takes over — and propagation continues at every step of the search, pruning dead ends that backtracking alone would have to explore the hard way.

The computational cost of AC-3 is O(ed³), where e is the number of arcs (constraints) and d is the maximum domain size — polynomial and typically fast in practice. However, arc consistency has limits. It only checks pairs of variables at a time, so it can miss inconsistencies that involve three or more variables simultaneously. Stronger forms of consistency (path consistency, k-consistency) catch more, but at higher computational cost. The practical sweet spot for most CSP solvers is to use arc consistency as the propagation engine within backtracking search: assign a variable, propagate, and if any domain becomes empty, backtrack immediately. This combination of search and inference is far more efficient than either technique alone.
