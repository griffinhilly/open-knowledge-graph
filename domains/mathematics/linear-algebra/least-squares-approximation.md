---
id: least-squares-approximation
title: Least Squares Approximation
domain: mathematics
course: linear-algebra
prerequisites:
- id: orthogonal-projections
  type: hard
- id: gram-schmidt-process
  type: hard
tags:
- least-squares
- approximation
- regression
stage: formal-systems
status: draft
---

# Least Squares Approximation

## Core Idea
For an overdetermined system Ax ≈ b (more equations than unknowns), the least-squares solution minimizes ‖Ax − b‖² and satisfies the normal equation Aᵀ Ax = Aᵀ b. The solution is x̂ = (AᵀA)⁻¹ Aᵀ b, obtained by projecting b onto col(A). This is fundamental to data fitting, regression, and numerical analysis.
