---
id: successive-over-relaxation
title: Successive Over-Relaxation (SOR)
domain: mathematics
course: numerical-analysis
prerequisites:
- id: gauss-seidel-method
  type: hard
builds-toward:
- convergence-iterative-methods
tags:
- sor
- over-relaxation
- iterative
stage: abstract-reasoning
status: draft
---

# Successive Over-Relaxation (SOR)

## Core Idea
SOR accelerates Gauss-Seidel by introducing a relaxation parameter ω: x_i^{(k+1)} = (1-ω)x_i^{(k)} + ω·(Gauss-Seidel step). For 0 < ω < 2, SOR can significantly reduce iterations needed for convergence. The optimal ω depends on the matrix eigenvalues; poor choice of ω can slow or even prevent convergence.
