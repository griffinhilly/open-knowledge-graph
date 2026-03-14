---
id: three-sat-np-complete
title: 3-SAT and NP-Completeness via CNF
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: sat-boolean-satisfiability
  type: hard
- id: cook-levin-theorem-formal
  type: hard
- id: np-completeness-formal
  type: hard
builds-toward:
- vertex-cover-problem
- clique-problem-np-complete
tags:
- sat
- cnf
- np-complete
stage: advanced
status: draft
---

# 3-SAT and NP-Completeness via CNF

## Core Idea
3-SAT restricts SAT to formulas in CNF where each clause has exactly three literals. Despite this restriction, 3-SAT remains NP-complete, making it a canonical problem for showing other problems are NP-hard via reduction. The Cook-Levin theorem proves that every NP problem reduces to 3-SAT in polynomial time.
