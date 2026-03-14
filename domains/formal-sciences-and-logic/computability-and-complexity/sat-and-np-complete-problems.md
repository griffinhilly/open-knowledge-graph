---
id: sat-and-np-complete-problems
title: Boolean Satisfiability and Standard NP-Complete Problems
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: np-completeness-formal
  type: hard
- id: cook-levin-theorem-formal
  type: hard
builds-toward:
- np-completeness-reduction-proof-techniques
tags:
- SAT
- NP-completeness
- hard-problems
stage: advanced
status: draft
---

# Boolean Satisfiability and Standard NP-Complete Problems

## Core Idea
SAT (Boolean satisfiability) is NP-complete by the Cook-Levin theorem: any NP problem reduces to SAT in polynomial time. Other canonical NP-complete problems—3-SAT, independent set, vertex cover, Hamiltonian path—form a landscape of computationally hard problems. Solving SAT efficiently would imply P = NP and break modern cryptography.
