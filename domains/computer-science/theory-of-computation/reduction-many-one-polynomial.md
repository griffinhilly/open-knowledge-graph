---
id: reduction-many-one-polynomial
title: Polynomial Many-One Reductions
domain: computer-science
course: theory-of-computation
prerequisites:
- id: np-completeness
  type: hard
- id: boolean-satisfiability-and-reductions
  type: hard
tags:
- reductions
- hardness
- complexity-classes
stage: advanced
status: draft
---

# Polynomial Many-One Reductions

## Core Idea
A polynomial many-one reduction from L₁ to L₂ is a polynomial-time computable function f where x ∈ L₁ ⟺ f(x) ∈ L₂, formalizing 'problem L₁ is no harder than L₂.' If L₂ is polynomial-solvable and L₁ reduces to L₂, then L₁ is solvable in polynomial time. NP-completeness is defined via such reductions: a problem is NP-complete if in NP and all NP problems reduce to it. Reductions form the backbone of complexity theory, transferring difficulty between problems.
