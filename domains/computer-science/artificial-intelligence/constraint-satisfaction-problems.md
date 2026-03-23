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
status: validated
---

# Constraint Satisfaction Problem Solving

## Core Idea
CSPs are defined by variables with domains and constraints restricting valid assignments. Solving means finding an assignment satisfying all constraints or proving infeasibility. CSPs unify scheduling, graph coloring, and puzzle problems. Systematic search with constraint propagation solves them efficiently.

## How It's Best Learned
Model N-Queens as a CSP, implement backtracking with forward checking, and measure speedup against basic backtracking.

## Common Misconceptions
Constraint propagation alone is insufficient for most CSPs; search remains necessary. Higher-order consistency has diminishing returns.

## Questions

```yaml
- question: "You are solving a Sudoku puzzle using only constraint propagation (arc consistency). After running AC-3 to completion, several cells still have two or more possible values. What can you conclude?"
  type: multiple-choice
  options:
    - "The puzzle has no solution — if it did, propagation would have found all unique values"
    - "The puzzle has multiple solutions, since propagation would have determined unique values if only one solution existed"
    - "Constraint propagation has eliminated all provably impossible values, but backtracking search is still needed to commit to specific values"
    - "The remaining ambiguity indicates an error in the constraint specification"
  answer: 2
  explanation: "Constraint propagation (including arc consistency) is not a complete solver — it removes values that are inconsistent with current assignments, but it cannot by itself determine which of multiple consistent values is correct. Most real CSPs require both propagation and search. Propagation without search is incomplete; search without propagation is exponentially slow. Options A and B confuse propagation's capability with a complete solver's; option D is false — even correctly specified CSPs routinely require search after propagation."

- question: "The Minimum Remaining Values (MRV) heuristic selects the next variable to assign by choosing the one with the fewest remaining legal values. Why does this tend to speed up solving?"
  type: multiple-choice
  options:
    - "Variables with fewer remaining values are more likely to have the correct value, guiding the solver toward the solution"
    - "Variables with fewer remaining values are most constrained and most likely to cause failure — detecting that failure early prunes the search tree before more variables are assigned"
    - "MRV reduces the total number of constraints by eliminating variables with small domains first"
    - "MRV ensures every variable gets at least one value assigned, preventing the solver from getting stuck"
  answer: 1
  explanation: "MRV is a 'fail-first' heuristic. If the most constrained variable will eventually fail (has no legal assignment), discovering that failure NOW — before branching on many other variables — means the solver backtracks immediately with minimal wasted work. This prunes entire subtrees of the search space at their root rather than their leaves. Option A is incorrect — fewer remaining values does not imply 'more likely to be correct.' Options C and D mischaracterize what the heuristic actually does."

- question: "If arc consistency (AC-3) is enforced globally before any variable is assigned, the resulting reduced domains are guaranteed to contain a valid complete assignment."
  type: true-false
  answer: false
  explanation: "Arc consistency removes values that have no support in neighboring domains, but it does not guarantee that a globally consistent assignment exists. A CSP can be arc-consistent yet infeasible — for example, in graph 3-coloring, arc consistency may reduce domains but cannot detect that no valid coloring exists without search. This is precisely why backtracking search remains necessary: propagation is incomplete as a solver, and arc consistency is a local property that does not imply global satisfiability."

- question: "CSP backtracking search is more efficient than naive exhaustive enumeration because it detects constraint violations in partial assignments and abandons branches that cannot lead to solutions."
  type: true-false
  answer: true
  explanation: "Naive enumeration generates all complete assignments before checking constraints — exponential work. Backtracking prunes the search tree as soon as a partial assignment violates a constraint, cutting off entire subtrees that could never lead to a solution. Combined with forward checking (propagating constraints from newly assigned variables), most infeasible branches are pruned before they are explored, often reducing search from exponential to tractable for practical CSP instances."

- question: "Explain why combining constraint propagation with backtracking is more powerful than either technique used alone."
  type: short-answer
  answer: "Constraint propagation alone is incomplete — it can reduce domains by eliminating clearly impossible values, but for most CSPs it cannot determine which of the remaining consistent values is correct without committing to one. Backtracking alone is correct but exponentially slow — it must explore an enormous search tree. When combined, propagation prunes the search tree at each decision node by eliminating values made impossible by the current partial assignment, dramatically reducing the branching factor before the solver makes new commitments. Backtracking then handles the residual search. Each constraint violation detected by propagation eliminates not just one assignment but an entire subtree."
  explanation: "This synergy is why real CSP solvers scale to thousands of variables. The key insight is that propagation is cheap per node and dramatically reduces the size of the remaining search problem, while backtracking provides the completeness guarantee. Neither alone is practical for large real-world CSPs; together they are the foundation of every modern constraint solver."
```

## Explainer

From graph theory, you know how to represent relationships between entities as nodes and edges. From algorithm design, you know how to systematically explore solution spaces through search. **Constraint satisfaction problems (CSPs)** combine these ideas into a powerful general framework: you have a set of variables, each with a domain of possible values, and a set of constraints that restrict which combinations of values are allowed. Solving a CSP means finding an assignment of values to all variables that satisfies every constraint simultaneously — or proving that no such assignment exists.

Consider a concrete example: **map coloring**. You have regions (variables), colors (domains, say {red, green, blue}), and the constraint that adjacent regions must have different colors. This is a CSP. Sudoku is another: variables are the 81 cells, domains are digits 1–9, and constraints enforce that no digit repeats in any row, column, or 3×3 box. Scheduling — assigning time slots and rooms to classes so no instructor teaches two classes simultaneously and no room is double-booked — is yet another. The power of the CSP formalism is that these wildly different problems share the same structure and can be solved by the same algorithms.

The naive approach is **backtracking search**: assign a value to one variable, move to the next, and if a constraint is violated, undo the last assignment and try a different value. This works but is exponentially slow in the worst case. The key acceleration comes from **constraint propagation** — using constraints to eliminate impossible values before committing to them. The most common technique is **arc consistency (AC-3)**: for every pair of constrained variables, remove any value from one variable's domain that has no compatible value in the other variable's domain. Propagation cascades — removing a value from one domain may trigger further removals elsewhere. Combined with backtracking, this dramatically prunes the search space. **Forward checking**, a lighter version, only propagates constraints from the most recently assigned variable.

Smart heuristics further improve performance. The **minimum remaining values (MRV)** heuristic selects the variable with the fewest remaining legal values to assign next — the idea being that this variable is most likely to cause a failure, so detecting that failure early saves the most work. The **least constraining value** heuristic picks the value that eliminates the fewest options for neighboring variables, maximizing flexibility for future assignments. Together, intelligent variable and value ordering with constraint propagation can solve CSPs with thousands of variables in seconds that would take brute-force search longer than the age of the universe.
