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
status: validated
---

# Backtracking and Constraint Satisfaction

## Core Idea
Backtracking is a depth-first search strategy that explores solution space, undoing (backtracking) when a partial solution violates constraints. It's used to solve constraint satisfaction problems like N-Queens, Sudoku, and graph coloring by building solutions incrementally.

## Questions

```yaml
- question: "A backtracking algorithm is solving an 8-Queens problem. After placing queens in rows 1–5, it finds that every column in row 6 conflicts with an existing queen. What does backtracking do next?"
  type: multiple-choice
  options:
    - "It tries all column assignments for rows 7 and 8 before giving up on the current partial solution"
    - "It immediately backtracks to row 5 and tries the next unused column there"
    - "It restarts the search from row 1 with a different initial column"
    - "It marks the problem unsolvable and terminates"
  answer: 1
  explanation: "The power of backtracking is immediate abandonment of a branch the moment a constraint cannot be satisfied. Since no valid placement exists for row 6, every extension of this partial solution is guaranteed to fail — there is no point exploring rows 7 or 8. The algorithm backtracks to the most recent decision (row 5) and tries the next option. Option A describes brute-force generation, not backtracking; the whole point is to prune rather than enumerate."

- question: "In a CSP with 9 variables, variable A has 4 remaining legal values, variable B has 1, and variable C has 7. Which should the MRV (most constrained variable) heuristic assign next?"
  type: multiple-choice
  options:
    - "Variable C, because more options provide greater flexibility to satisfy constraints later"
    - "Variable A, as a balanced middle choice"
    - "Variable B, because it has the fewest remaining legal values"
    - "Whichever variable appears first in the problem's variable list"
  answer: 2
  explanation: "MRV stands for 'minimum remaining values' — also called 'fail-first' because you assign the variable most likely to hit a dead end. Variable B has only one legal value: assigning it now costs almost nothing (there is only one option) and immediately reveals whether this branch survives. If B has zero legal values, the algorithm would backtrack right away instead of wasting effort assigning A and C first. Option A reverses the logic: a variable with many options can be assigned later without risk."

- question: "Backtracking is more efficient than brute-force enumeration because it checks constraints after each partial assignment rather than only after all variables have been assigned."
  type: true-false
  answer: true
  explanation: "This is the defining efficiency gain of backtracking. By checking constraints at each step, the algorithm detects infeasible partial solutions early and prunes entire subtrees from consideration. A brute-force approach generates all complete assignments and checks each one — exponential in the number of variables. Backtracking avoids enumerating every extension of a failed partial assignment."

- question: "Constraint propagation in backtracking only updates the domain of the variable currently being assigned; it leaves all other variables' domains unchanged."
  type: true-false
  answer: false
  explanation: "Constraint propagation does the opposite: when you assign a value to one variable, it removes that value — and any values made illegal by the assignment — from the domains of all constrained neighbor variables. This forward propagation can eliminate values from many variables simultaneously, detecting future failures early without even trying to assign those variables. If propagation reduces a neighbor's domain to zero values, the algorithm backtracks immediately."

- question: "Explain why checking constraints on partial assignments — before a complete solution is formed — makes backtracking more efficient than generating all complete assignments and checking each one."
  type: short-answer
  answer: "Each partial assignment that violates a constraint represents the root of a subtree of complete assignments, all of which are guaranteed to also violate that constraint. By detecting the violation in the partial assignment, backtracking prunes the entire subtree at once rather than exploring every node within it. In an N-Queens problem, detecting a conflict in row 3 avoids generating all placements for rows 4 through N under that partial configuration — potentially billions of nodes pruned from a single early detection."
  explanation: "The key insight is that constraints are inherited downward through partial solutions: if partial assignment P violates a constraint, every complete assignment extending P also violates it. Brute force ignores this structure; backtracking exploits it. Combined with heuristics like MRV and constraint propagation, this can reduce exponential search to near-linear in well-constrained problems like Sudoku."
```

## Explainer

You already know how recursion works — a function calling itself on smaller subproblems until reaching a base case. **Backtracking** uses recursion in a specific way: it builds a solution one decision at a time, and at each step, it checks whether the partial solution so far could possibly lead to a valid complete solution. If the answer is no, it immediately abandons that path and tries the next option — "backtracking" to the previous decision point. This is far more efficient than generating all possible combinations and checking each one, because it prunes entire branches of the search tree as soon as a constraint is violated.

Consider the **N-Queens problem**: place N queens on an N×N chessboard so that no two queens attack each other. A brute-force approach would try all possible placements of N queens on N² squares — an astronomical number of combinations. Backtracking instead places queens one row at a time. Place a queen in row 1, column 1. Move to row 2 and try column 1 — conflict with the queen above, so skip it. Try column 2 — diagonal conflict, skip. Try column 3 — no conflicts, place it. Move to row 3. If every column in row 3 conflicts with existing queens, backtrack: remove the queen from row 2, try the next column there, and continue. Each time a constraint is violated, the algorithm avoids exploring all the downstream possibilities from that invalid partial placement.

A **constraint satisfaction problem (CSP)** formalizes this pattern. A CSP has three components: **variables** (what you need to assign values to), **domains** (the possible values each variable can take), and **constraints** (rules about which combinations of values are allowed). In Sudoku, the variables are the 81 cells, each domain is {1-9}, and the constraints say no row, column, or 3×3 box can repeat a value. In graph coloring, the variables are vertices, the domain is the set of available colors, and the constraint says adjacent vertices must differ in color. Backtracking solves CSPs by assigning values to variables one at a time, checking constraints after each assignment, and undoing assignments that lead to violations.

The efficiency of backtracking depends heavily on two choices: **variable ordering** (which variable to assign next) and **value ordering** (which value to try first). A powerful heuristic is **most constrained variable** (also called MRV or "fail-first"): always assign next the variable with the fewest remaining legal values. If a variable has only one legal value left, assign it immediately. If a variable has zero legal values, backtrack immediately — you've detected failure as early as possible. Combined with **constraint propagation** (when you assign a value, immediately eliminate that value from the domains of all constrained neighbors), these heuristics can reduce exponential search spaces to manageable sizes. Sudoku solvers, for example, often solve puzzles with almost no backtracking at all once propagation handles the forced moves.
