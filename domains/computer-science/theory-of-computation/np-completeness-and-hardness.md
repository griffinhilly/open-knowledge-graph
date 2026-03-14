---
id: np-completeness-and-hardness
title: NP-Completeness and NP-Hardness
domain: computer-science
course: theory-of-computation
prerequisites:
- id: np-completeness
  type: hard
- id: complexity-class-np-definition
  type: soft
builds-toward:
- boolean-satisfiability-and-reductions
tags:
- np-complete
- np-hard
- reduction
- hardest-problems
- equivalence
stage: advanced
status: draft
---

# NP-Completeness and NP-Hardness

## Core Idea
A language is NP-complete if it's in NP and every NP language polynomial-time reduces to it. NP-hard means hard but not necessarily in NP (e.g., TQBF). If any NP-complete problem is in P, then P = NP. NP-complete problems (SAT, 3-SAT, clique, vertex cover) are equivalent in difficulty—if one is tractable, all are.
