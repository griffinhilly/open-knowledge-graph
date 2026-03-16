---
id: constraint-satisfaction-problems
title: Constraint Satisfaction Problem Solving
domain: computer-science
course: artificial-intelligence
prerequisites:
- id: graph-theory-intro
  type: hard
- id: algorithm-design-basics
  type: hard
tags:
- constraint-solving
- search
- optimization
stage: advanced
status: draft
---

# Constraint Satisfaction Problem Solving

## Core Idea
CSPs are defined by variables with domains and constraints restricting valid assignments. Solving means finding an assignment satisfying all constraints or proving infeasibility. CSPs unify scheduling, graph coloring, and puzzle problems. Systematic search with constraint propagation solves them efficiently.

## How It's Best Learned
Model N-Queens as a CSP, implement backtracking with forward checking, and measure speedup against basic backtracking.

## Common Misconceptions
Constraint propagation alone is insufficient for most CSPs; search remains necessary. Higher-order consistency has diminishing returns.

## Explainer

From graph theory, you know how to represent relationships between entities as nodes and edges. From algorithm design, you know how to systematically explore solution spaces through search. **Constraint satisfaction problems (CSPs)** combine these ideas into a powerful general framework: you have a set of variables, each with a domain of possible values, and a set of constraints that restrict which combinations of values are allowed. Solving a CSP means finding an assignment of values to all variables that satisfies every constraint simultaneously — or proving that no such assignment exists.

Consider a concrete example: **map coloring**. You have regions (variables), colors (domains, say {red, green, blue}), and the constraint that adjacent regions must have different colors. This is a CSP. Sudoku is another: variables are the 81 cells, domains are digits 1–9, and constraints enforce that no digit repeats in any row, column, or 3×3 box. Scheduling — assigning time slots and rooms to classes so no instructor teaches two classes simultaneously and no room is double-booked — is yet another. The power of the CSP formalism is that these wildly different problems share the same structure and can be solved by the same algorithms.

The naive approach is **backtracking search**: assign a value to one variable, move to the next, and if a constraint is violated, undo the last assignment and try a different value. This works but is exponentially slow in the worst case. The key acceleration comes from **constraint propagation** — using constraints to eliminate impossible values before committing to them. The most common technique is **arc consistency (AC-3)**: for every pair of constrained variables, remove any value from one variable's domain that has no compatible value in the other variable's domain. Propagation cascades — removing a value from one domain may trigger further removals elsewhere. Combined with backtracking, this dramatically prunes the search space. **Forward checking**, a lighter version, only propagates constraints from the most recently assigned variable.

Smart heuristics further improve performance. The **minimum remaining values (MRV)** heuristic selects the variable with the fewest remaining legal values to assign next — the idea being that this variable is most likely to cause a failure, so detecting that failure early saves the most work. The **least constraining value** heuristic picks the value that eliminates the fewest options for neighboring variables, maximizing flexibility for future assignments. Together, intelligent variable and value ordering with constraint propagation can solve CSPs with thousands of variables in seconds that would take brute-force search longer than the age of the universe.
