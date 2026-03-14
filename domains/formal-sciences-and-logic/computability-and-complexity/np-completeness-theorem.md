---
id: np-completeness-theorem
title: NP-Completeness and the Cook-Levin Theorem
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: cook-levin-theorem-formal
  type: hard
- id: np-hardness
  type: hard
builds-toward:
- sat-canonical-problem
- three-sat-reductions
tags:
- np-completeness
- cook-levin
- sat
- completeness
stage: advanced
status: draft
---

# NP-Completeness and the Cook-Levin Theorem

## Core Idea
The Cook-Levin theorem proves that Boolean satisfiability (SAT) is NP-complete: every NP problem reduces to SAT, and SAT is in NP. This provides the first NP-complete problem; all other NP-complete problems are discovered by reducing from previously known NP-complete problems, creating a network of reductions.

## How It's Best Learned
Carefully study the Cook-Levin proof structure: how an NP Turing machine is encoded in a Boolean formula. Work through simplified reductions (e.g., CLIQUE → 3-SAT).

## Common Misconceptions
- Missing why Cook-Levin is a breakthrough: it provides the first NP-complete problem, enabling all subsequent reductions.
- Assuming Cook-Levin applies uniformly to other problems. It specifically handles SAT; other completeness proofs reduce from known NP-complete problems.
