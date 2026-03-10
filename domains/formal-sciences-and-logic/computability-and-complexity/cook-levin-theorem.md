---
id: cook-levin-theorem
title: The Cook-Levin Theorem
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: np-completeness
  type: hard
- id: polynomial-time-reductions
  type: hard
- id: nondeterministic-turing-machines
  type: hard
- id: boolean-algebra
  type: soft
- id: big-o-notation
  type: soft
tags:
- NP-complete
- SAT
- satisfiability
- Cook-Levin
stage: advanced
status: draft
---

# The Cook-Levin Theorem

## Core Idea
The Cook-Levin theorem proves that Boolean satisfiability (SAT) is NP-complete — the first problem proven NP-complete (Cook 1971, independently Levin 1973). The proof encodes the computation of an arbitrary NTM as a propositional formula: variables represent tape cells, head positions, and states at each time step, while clauses enforce the transition rules. Since every NP problem reduces to SAT, SAT is the 'universal' hard problem in NP and the historical starting point for the entire theory of NP-completeness.

## How It's Best Learned
Work through the tableau construction carefully: understand how an NTM's accepting computation of length t is encoded as a formula of size O(t²). Appreciate that the reduction itself runs in polynomial time even though the formula can be large relative to the original instance.

## Common Misconceptions
- The theorem proves SAT is NP-complete, not that SAT is unsolvable — SAT is in NP, so it can be solved, just not known to be solvable in polynomial time.
- The historical significance is not merely proving SAT hard, but establishing the concept of NP-completeness itself and identifying the first complete problem from which all others reduce.
