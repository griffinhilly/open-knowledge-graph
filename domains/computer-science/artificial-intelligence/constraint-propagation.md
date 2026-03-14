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
builds-toward:
- backtracking-search-csp
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
