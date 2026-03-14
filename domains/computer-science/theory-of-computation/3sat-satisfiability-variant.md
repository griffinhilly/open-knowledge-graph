---
id: 3sat-satisfiability-variant
title: 3-SAT and k-SAT Variants
domain: computer-science
course: theory-of-computation
prerequisites:
- id: sat-boolean-satisfiability
  type: hard
- id: np-completeness
  type: hard
tags:
- np-complete
- clause-restrictions
stage: advanced
status: draft
---

# 3-SAT and k-SAT Variants

## Core Idea
3-SAT restricts SAT to formulas where each clause has exactly three literals; k-SAT generalizes to k literals per clause. Remarkably, 3-SAT remains NP-complete despite the restriction—restricting clause size doesn't reduce hardness beyond 3 literals. 2-SAT is solvable in polynomial time via implication graphs; k-SAT for k ≥ 3 is NP-complete. The phase transition phenomenon—random k-SAT formulas become hardest near the satisfiability threshold—is a major topic in complexity physics.
