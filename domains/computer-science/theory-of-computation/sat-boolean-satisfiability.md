---
id: sat-boolean-satisfiability
title: 'SAT: Boolean Satisfiability Problem'
domain: computer-science
course: theory-of-computation
prerequisites:
- id: complexity-class-np-definition
  type: hard
- id: boolean-satisfiability-and-reductions
  type: hard
tags:
- np-complete
- satisfiability
- canonical-problem
stage: advanced
status: draft
---

# SAT: Boolean Satisfiability Problem

## Core Idea
The SAT problem asks: given a Boolean formula in conjunctive normal form (CNF), does an assignment exist making the formula true? SAT is the canonical NP-complete problem (Cook-Levin theorem); all other NP-completeness proofs reduce to SAT. Despite its NP-completeness, modern SAT solvers (using DPLL, clause learning, and heuristics) solve many practical instances efficiently, making SAT critical for formal verification, constraint satisfaction, and cryptanalysis.

## How It's Best Learned
Study the Cook-Levin proof of SAT's NP-completeness. Understand CNF representation and conversion. Use SAT solvers on small instances to observe practical tractability despite theoretical hardness.

## Common Misconceptions
Confusing NP-completeness (no known polynomial algorithm) with unsolvability. Thinking practical SAT solvability contradicts NP-completeness (fast heuristics ≠ polynomial guarantee). Assuming all satisfiable formulas are equally hard.
