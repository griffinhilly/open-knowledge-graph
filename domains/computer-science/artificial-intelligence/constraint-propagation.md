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
status: validated
---
# Constraint Propagation

## Core Idea
Constraint propagation reduces the search space by eliminating values from variable domains that cannot satisfy constraints, even before search begins. Techniques like arc consistency (AC-3) detect unsatisfiable constraints early and can sometimes solve CSPs without any backtracking. The consistency check is polynomial but repeated propagation increases algorithm complexity.

## How It's Best Learned
Implement AC-3 and trace through a small CSP by hand to understand how arc consistency eliminates values iteratively.

## Common Misconceptions
Constraint propagation always finds a solution (it only ensures consistency, not satisfiability). AC-3 is the strongest consistency check (higher-order consistencies like k-consistency are stronger but more expensive).

## Questions

```yaml
- question: "AC-3 runs to completion on a CSP and no variable domain becomes empty. What can you conclude?"
  type: multiple-choice
  options:
    - "The CSP has at least one valid solution"
    - "The CSP is arc-consistent, meaning each remaining value has a compatible value in every adjacent variable's domain — but a solution may or may not exist"
    - "The CSP has no solution, since AC-3 found values to remove"
    - "Backtracking search is no longer needed because propagation has found the solution"
  answer: 1
  explanation: "Arc consistency means that every remaining value in every variable's domain has at least one compatible value in each neighboring variable's domain. This is a necessary but not sufficient condition for a solution. A CSP can be arc-consistent and still have no solution — arc consistency only checks pairs of variables, missing contradictions involving three or more variables simultaneously. This is the most important misconception about constraint propagation: ensuring consistency is not the same as finding or guaranteeing a solution."

- question: "In AC-3, when a value is removed from a variable X's domain, what happens next?"
  type: multiple-choice
  options:
    - "The algorithm terminates and reports that the problem may be unsolvable"
    - "The algorithm immediately backtracks to a previous variable assignment"
    - "All arcs pointing TO variable X are re-added to the processing queue"
    - "All constraints involving X are checked once and then discarded"
  answer: 2
  explanation: "When a value is removed from X's domain, it may make previously consistent values in X's neighbors inconsistent — because those neighbors were consistent assuming X's full domain was available. To catch these newly created inconsistencies, AC-3 re-adds all arcs pointing to X (i.e., from X's neighbors to X) to the queue. This cascading re-check is what makes AC-3 a complete arc-consistency enforcer rather than a single-pass filter. Without it, some inconsistencies would slip through."

- question: "Arc consistency (AC-3) can sometimes solve a CSP entirely, without any backtracking search."
  type: true-false
  answer: true
  explanation: "In well-constrained problems like easy Sudoku puzzles, propagating arc consistency after each deduction can eliminate all but one value from every variable's domain, effectively solving the puzzle. Each time a cell's value is determined, constraint propagation removes that value from all cells in the same row, column, and box — which may force other cells, which propagate further. Hard Sudoku puzzles cannot be solved this way and require search, but they still benefit from propagation dramatically reducing the search space."

- question: "Constraint propagation guarantees that if a CSP has a solution, AC-3 will find it."
  type: true-false
  answer: false
  explanation: "Constraint propagation ensures consistency — it removes values that provably cannot be in any solution — but it does not find solutions. After propagation, backtracking search is typically still needed to make assignments and explore the reduced space. Moreover, if propagation empties any variable's domain, it proves there is NO solution — but propagation running to completion without emptying a domain does not prove a solution exists. The combination of constraint propagation with backtracking is what provides both efficiency and completeness."

- question: "What is the difference between arc consistency and satisfiability in the context of CSPs, and why does this distinction matter for algorithm design?"
  type: short-answer
  answer: "Arc consistency is a local property: variable X is arc-consistent with Y if every value in X's domain has at least one compatible value in Y's domain. A CSP is arc-consistent if all arcs have this property. Satisfiability means a complete assignment exists that satisfies all constraints simultaneously. A CSP can be arc-consistent but unsatisfiable — arc consistency only checks pairs of variables, not combinations of three or more. This matters because it tells us constraint propagation is an inference tool that prunes the search space, not a solver that replaces search."
  explanation: "Algorithm designers use this distinction to avoid the 'propagation always works' misconception. AC-3 is fast (polynomial) but incomplete — it may leave work for backtracking to do. Stronger consistency checks (path consistency, k-consistency) catch more but cost more. The practical design choice is to use cheap arc consistency as an inference engine within backtracking search, running propagation after each assignment and backtracking when any domain empties."
```

## Explainer

In a constraint satisfaction problem, you have variables with domains of possible values and constraints that restrict which combinations are allowed. A brute-force approach would try every possible assignment and check constraints at the end. Backtracking improves on this by checking constraints as it goes. **Constraint propagation** goes further still: it reasons about constraints *before and during* search to eliminate values that can never participate in a valid solution, shrinking the search space without ever guessing.

The core idea is **arc consistency**. An arc is a directed edge from variable X to variable Y in the constraint graph. X is arc-consistent with respect to Y if, for every value in X's domain, there exists at least one value in Y's domain that satisfies the constraint between them. If some value x in X's domain has no compatible value in Y's domain, then x can never be part of a valid solution — so you can safely remove it. The **AC-3 algorithm** enforces arc consistency across the entire problem by maintaining a queue of arcs to check. When a value is removed from a variable's domain, all arcs pointing to that variable are re-added to the queue, because the removal might make previously consistent values in neighboring variables now inconsistent. The process repeats until no more values can be removed.

Consider a concrete example: a Sudoku puzzle. Each cell is a variable with domain {1–9}, and constraints require that each row, column, and 3×3 box contains distinct values. When you place a 5 in a cell, constraint propagation immediately removes 5 from the domains of every other cell in the same row, column, and box. If that removal leaves some other cell with only one possible value, that value is propagated further, potentially triggering a cascade of deductions. In easy Sudoku puzzles, arc consistency alone solves the entire puzzle with no search at all. In harder puzzles, it dramatically reduces the domains before backtracking search takes over — and propagation continues at every step of the search, pruning dead ends that backtracking alone would have to explore the hard way.

The computational cost of AC-3 is O(ed³), where e is the number of arcs (constraints) and d is the maximum domain size — polynomial and typically fast in practice. However, arc consistency has limits. It only checks pairs of variables at a time, so it can miss inconsistencies that involve three or more variables simultaneously. Stronger forms of consistency (path consistency, k-consistency) catch more, but at higher computational cost. The practical sweet spot for most CSP solvers is to use arc consistency as the propagation engine within backtracking search: assign a variable, propagate, and if any domain becomes empty, backtrack immediately. This combination of search and inference is far more efficient than either technique alone.
