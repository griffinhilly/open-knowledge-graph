---
id: constraint-satisfaction-problems-cognitive-psychology
title: Constraint Satisfaction in Problem-Solving
domain: psychology
course: cognitive-psychology
prerequisites:
- id: problem-representation-and-search
  type: hard
tags:
- problem-solving
- constraints
- satisfaction
- reasoning
stage: advanced
status: draft
---

# Constraint Satisfaction in Problem-Solving

## Core Idea
Many problems require satisfying multiple constraints simultaneously. Constraint satisfaction approaches systematically narrow solution spaces by eliminating options violating constraints. This explains insights and the role of constraint propagation in human problem-solving, particularly in domains like puzzle-solving and design.

## Explainer

From your study of problem representation and search, you know that solving a problem involves representing a **problem space** — a set of states and operators — and searching through that space toward a goal state. Many real problems have an additional structure: not just a goal to reach, but a set of **constraints** that any acceptable solution must simultaneously satisfy. Constraint satisfaction is the framework for thinking about this class of problems.

A simple example makes the structure concrete. In a Sudoku puzzle, the goal is to fill a 9×9 grid with digits 1–9 such that each digit appears exactly once in every row, column, and 3×3 box. Every empty cell is a variable; its domain is {1–9}; the constraints are the uniqueness rules. A naive search strategy — try every possible digit in every cell and check whether the completed grid is valid — is computationally explosive. A smarter approach uses **constraint propagation**: when you place a 7 in a particular cell, that immediately eliminates 7 as a candidate from every other cell in the same row, column, and box. Propagating this constraint often eliminates candidates from other cells, which propagates further constraints, and so on. Often a chain of propagations resolves large portions of the grid without any guessing at all. When propagation stalls, you pick a cell with the fewest remaining candidates and branch — a process called **backtracking search** with constraint propagation.

The cognitive psychology question is whether human problem-solvers use analogous processes. The answer is yes, though in a less explicit, more parallel form. Research on human puzzle-solving suggests that people do not exhaustively search the problem space; instead, they maintain implicit constraint representations and use them to prune the space of options before consciously deliberating. **Insight problems** — where the solution appears suddenly and feels qualitatively different from deliberate search — are often explained in constraint satisfaction terms: prior framing inadvertently sets an incorrect constraint (e.g., "lines must stay within the boundary" in the nine-dot problem), blocking productive search paths. The "aha moment" corresponds to relaxing or reinterpreting a constraint, which suddenly opens a large region of solution space that was previously unavailable.

Constraint satisfaction thinking is also powerful in design and planning contexts, where multiple requirements (cost, performance, aesthetics, timeline) must be balanced simultaneously. The insight from this framework is that the difficulty of a problem is not just a function of how large the search space is — it is heavily shaped by which constraints are active, how many variables they link, and whether constraint propagation can do the heavy lifting before costly search begins. Problems that feel intractable often become tractable once constraints are made explicit and propagated: the act of formally writing down every requirement and asking what each eliminates is itself a powerful problem-solving move.
