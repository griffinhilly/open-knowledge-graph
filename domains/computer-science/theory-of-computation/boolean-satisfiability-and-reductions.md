---
id: boolean-satisfiability-and-reductions
title: Boolean Satisfiability, Cook-Levin, and Reductions
domain: computer-science
course: theory-of-computation
prerequisites:
- id: cook-levin-theorem
  type: hard
- id: np-completeness-and-hardness
  type: soft
builds-toward:
- space-complexity-definitions
tags:
- sat
- 3sat
- cook-levin
- cnf
- reduction
- canonical
stage: advanced
status: draft
---

# Boolean Satisfiability, Cook-Levin, and Reductions

## Core Idea
SAT (Boolean satisfiability) asks if a CNF formula has a satisfying assignment. Cook-Levin theorem proves SAT is NP-complete by showing every NP language reduces to SAT—establishing SAT as canonical. 3-SAT (3 literals per clause) is NP-complete. Reductions from SAT prove other problems NP-complete: map satisfying assignments to solutions of the target problem.
