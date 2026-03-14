---
id: successive-over-relaxation-sor
title: Successive Over-Relaxation (SOR)
domain: mathematics
course: numerical-analysis
prerequisites:
- id: gauss-seidel-iterative-method
  type: hard
builds-toward:
- convergence-iterative-linear-solvers
tags:
- sor
- over-relaxation
- acceleration
stage: advanced
status: draft
---

# Successive Over-Relaxation (SOR)

## Core Idea
SOR accelerates Gauss-Seidel using a relaxation parameter ω: x_i^{(k+1)} = (1-ω)x_i^{(k)} + ω(GS_i^{(k+1)}) where GS_i is the Gauss-Seidel update. For ω > 1, the method overrelaxes the corrections, accelerating convergence when ω is chosen optimally. Optimal ω depends on spectral properties of the system and must be determined numerically or theoretically.
