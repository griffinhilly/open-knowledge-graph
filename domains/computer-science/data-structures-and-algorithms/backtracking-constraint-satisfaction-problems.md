---
id: backtracking-constraint-satisfaction-problems
title: Backtracking and Constraint Satisfaction
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: recursion-tail-recursion-optimization
  type: hard
builds-toward:
- dynamic-programming-intro
- greedy-algorithms
tags:
- backtracking
- csp
- search
stage: formal-systems
status: draft
---

# Backtracking and Constraint Satisfaction

## Core Idea
Backtracking is a depth-first search strategy that explores solution space, undoing (backtracking) when a partial solution violates constraints. It's used to solve constraint satisfaction problems like N-Queens, Sudoku, and graph coloring by building solutions incrementally.

## Explainer

You already know how recursion works — a function calling itself on smaller subproblems until reaching a base case. **Backtracking** uses recursion in a specific way: it builds a solution one decision at a time, and at each step, it checks whether the partial solution so far could possibly lead to a valid complete solution. If the answer is no, it immediately abandons that path and tries the next option — "backtracking" to the previous decision point. This is far more efficient than generating all possible combinations and checking each one, because it prunes entire branches of the search tree as soon as a constraint is violated.

Consider the **N-Queens problem**: place N queens on an N×N chessboard so that no two queens attack each other. A brute-force approach would try all possible placements of N queens on N² squares — an astronomical number of combinations. Backtracking instead places queens one row at a time. Place a queen in row 1, column 1. Move to row 2 and try column 1 — conflict with the queen above, so skip it. Try column 2 — diagonal conflict, skip. Try column 3 — no conflicts, place it. Move to row 3. If every column in row 3 conflicts with existing queens, backtrack: remove the queen from row 2, try the next column there, and continue. Each time a constraint is violated, the algorithm avoids exploring all the downstream possibilities from that invalid partial placement.

A **constraint satisfaction problem (CSP)** formalizes this pattern. A CSP has three components: **variables** (what you need to assign values to), **domains** (the possible values each variable can take), and **constraints** (rules about which combinations of values are allowed). In Sudoku, the variables are the 81 cells, each domain is {1-9}, and the constraints say no row, column, or 3×3 box can repeat a value. In graph coloring, the variables are vertices, the domain is the set of available colors, and the constraint says adjacent vertices must differ in color. Backtracking solves CSPs by assigning values to variables one at a time, checking constraints after each assignment, and undoing assignments that lead to violations.

The efficiency of backtracking depends heavily on two choices: **variable ordering** (which variable to assign next) and **value ordering** (which value to try first). A powerful heuristic is **most constrained variable** (also called MRV or "fail-first"): always assign next the variable with the fewest remaining legal values. If a variable has only one legal value left, assign it immediately. If a variable has zero legal values, backtrack immediately — you've detected failure as early as possible. Combined with **constraint propagation** (when you assign a value, immediately eliminate that value from the domains of all constrained neighbors), these heuristics can reduce exponential search spaces to manageable sizes. Sudoku solvers, for example, often solve puzzles with almost no backtracking at all once propagation handles the forced moves.
