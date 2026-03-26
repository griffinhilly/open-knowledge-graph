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
- id: backtracking-constraint-satisfaction-problems
  type: soft
builds-toward:
- constraint-propagation
tags:
- search
- csp
- backtracking
- variable-ordering
stage: advanced
status: validated
---
# Backtracking Search for CSPs

## Core Idea
Backtracking search systematically explores the solution space by assigning variables one at a time and undoing assignments when conflicts arise. Variable ordering heuristics (minimum remaining values, degree heuristic) and value ordering (least constraining value) dramatically improve performance by reducing the branching factor. The search can be dramatically accelerated by combining with constraint propagation.

## How It's Best Learned
Implement backtracking with and without the MRV heuristic on map coloring or N-queens to observe performance differences.

## Questions

```yaml
- question: "In a CSP with 10 variables, variable A has only 1 legal value remaining while variable B has 8 legal values remaining. The MRV heuristic assigns which variable next, and why?"
  type: multiple-choice
  options:
    - "Variable B, because more legal values means more flexibility to find a solution"
    - "Variable A, because a variable with fewer legal values is most likely to cause failure soon, and it is better to detect failure early"
    - "Either variable — MRV only matters when breaking ties between equally constrained variables"
    - "Variable B, because exploring more options first reduces backtracking later"
  answer: 1
  explanation: "MRV selects the variable with the fewest remaining legal values — variable A with 1 remaining value. The intuition is 'fail early': if A has only one valid value and it conflicts with the current partial assignment, you want to discover that failure immediately rather than after assigning B and all other variables. Backtracking is expensive; the earlier you detect a dead end, the fewer nodes you explore. Variable A is the 'most constrained' variable, and assigning it first maximizes pruning of the search tree."

- question: "A backtracking search without heuristics explores 1,000,000 nodes on a CSP. After adding the MRV heuristic, the same problem is solved in 500 nodes. What has the heuristic actually changed?"
  type: multiple-choice
  options:
    - "The heuristic changed the set of valid solutions found — it finds a better solution in fewer steps"
    - "The heuristic changed the order in which variables are assigned, causing failures to be detected earlier and pruning large subtrees"
    - "The heuristic changed the constraint definitions, making the problem easier to solve"
    - "The heuristic reduced domain sizes by eliminating illegal values before search begins"
  answer: 1
  explanation: "MRV is an ordering heuristic — it changes nothing about the problem's constraints, domains, or the set of valid solutions. It only changes which variable is assigned next. By tackling the most constrained variable first, failures are detected as early as possible in the search tree. When a variable with few legal values runs out of options, the algorithm backtracks immediately rather than continuing to assign other variables that could never lead to a solution. This collapses exponential subtrees, reducing node count dramatically while guaranteeing the same correct solutions."

- question: "Backtracking search with MRV is not expected to find a solution if one exists — the heuristic ordering may cause it to give up and report failure incorrectly."
  type: true-false
  answer: false
  explanation: "Backtracking search is complete — if a solution exists, it will find one. MRV is an ordering heuristic that changes which variable is assigned next but never skips a variable or permanently removes a value from consideration. Backtracking ensures that when a dead end is reached, the algorithm backtracks to a previous decision point and tries alternative values. MRV affects efficiency (how many nodes are explored), not completeness (whether a solution is found if one exists)."

- question: "The least constraining value (LCV) heuristic for value ordering selects the value that rules out the fewest choices for neighboring unassigned variables."
  type: true-false
  answer: true
  explanation: "LCV is designed to keep options open for the rest of the search. When assigning a value to the current variable, choosing a value that eliminates many values from neighboring domains makes those neighbors harder to assign — possibly causing failures that force backtracking. LCV selects the most cooperative value: the one that imposes the least restriction on remaining variables, giving the overall search the best chance of succeeding without backtracking. LCV complements MRV: MRV chooses which variable to assign; LCV chooses which value to try first for that variable."

- question: "Explain why 'fail early' is the core principle behind the MRV heuristic, and how it reduces the total number of nodes explored."
  type: short-answer
  answer: "MRV selects the variable with the fewest remaining legal values because that variable is most likely to fail soon. If it has only one value left and that value conflicts, failure is detected immediately. Without MRV, the algorithm might assign many other variables first — exploring a large subtree — only to discover that the constrained variable has no legal values and all that work must be undone. By assigning the most constrained variable first, any failure causes immediate backtracking, pruning every assignment that would have followed it. This fail-early strategy collapses exponential subtrees at their roots rather than exploring them fully before detecting failure."
  explanation: "The key insight is that backtracking's cost is not detecting failure — it is the wasted work of exploring subtrees that are doomed from the beginning. MRV minimizes wasted work by making the search tree fail as shallowly as possible. In map-coloring, assigning the most tightly constrained region first means failures at that region immediately eliminate large portions of the search space — the difference can be from millions of nodes down to hundreds."
```

## Explainer

You already know that a constraint satisfaction problem (CSP) consists of variables, domains (possible values for each variable), and constraints (rules about which combinations of values are allowed). A naive approach would enumerate every possible combination of values and check each one — but for a problem with n variables each having d possible values, that means checking d^n combinations, which quickly becomes intractable. **Backtracking search** improves on this by building assignments incrementally: assign one variable at a time, and the moment an assignment violates a constraint, immediately undo it and try a different value. This is the key insight from recursion and depth-first search applied to CSPs — you explore one branch deeply, and when you hit a dead end, you back up to the most recent choice point.

The basic backtracking algorithm works like a depth-first search through the space of partial assignments. Pick an unassigned variable, try a value from its domain, check if it is consistent with all constraints involving already-assigned variables, and if so, recurse to assign the next variable. If no value works, return failure — this triggers backtracking to the previous variable, which tries its next value. The recursion bottoms out successfully when all variables are assigned consistently. Even this simple approach is far better than brute-force enumeration because it prunes entire subtrees as soon as a conflict is detected, rather than waiting until all variables are assigned.

What makes backtracking practical for large CSPs is the choice of **heuristics** for variable and value ordering. The **minimum remaining values (MRV)** heuristic selects the variable with the fewest legal values remaining in its domain — the idea being that this variable is most likely to cause a failure, and it is better to fail early than to waste time assigning other variables first. Think of it as tackling the hardest constraint first. The **degree heuristic** breaks MRV ties by preferring the variable involved in the most constraints on unassigned variables, maximizing the pruning effect. For value ordering, the **least constraining value (LCV)** heuristic picks the value that rules out the fewest choices for neighboring variables — giving the rest of the problem the best chance of being solvable.

Consider the classic map-coloring problem: color the regions of a map with three colors such that no adjacent regions share a color. Without heuristics, the algorithm might start with a region that has many valid options and only discover deep in the search that a tightly constrained region has no valid color left. With MRV, it starts with the most constrained region, detects failures immediately, and avoids exploring large portions of the search tree that can never lead to a solution. The difference in practice can be enormous — from millions of nodes explored down to hundreds. When combined with constraint propagation techniques like arc consistency, backtracking search becomes powerful enough to solve real-world CSPs with thousands of variables.
