---
id: sat-boolean-satisfiability-computability-and-complexity
title: Boolean Satisfiability (SAT)
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: satisfiability-and-unsatisfiability
  type: hard
- id: np-and-polynomial-time
  type: hard
- id: boolean-algebra
  type: hard
- id: boolean-functions-and-circuits
  type: soft
builds-toward:
- three-sat-np-complete
tags:
- satisfiability
- np
- decision-problems
stage: advanced
status: draft
---

# Boolean Satisfiability (SAT)

## Core Idea
The Boolean satisfiability problem asks whether a propositional formula can be made true by assigning truth values to its variables. SAT is the canonical NP problem: every problem in NP can be reduced to SAT. Despite its centrality, no polynomial-time algorithm is known, and SAT is widely believed to require exponential time in the worst case.

## How It's Best Learned
Experiment with small propositional formulas: try to find assignments making them true. Understand why verifying a satisfying assignment is easy (linear time) but finding one seems hard.

## Common Misconceptions
- SAT is tractable because individual assignments can be checked quickly (confuses verification with solving).
- SAT-solvers are polynomial-time algorithms (in fact, SAT-solvers employ heuristics that work well in practice but guarantee no worst-case bound).
