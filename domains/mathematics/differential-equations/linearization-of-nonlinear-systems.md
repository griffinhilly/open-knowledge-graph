---
id: linearization-of-nonlinear-systems
title: Linearization of Nonlinear Systems
domain: mathematics
course: differential-equations
prerequisites:
- id: stability-classification
  type: hard
- id: partial-derivatives
  type: hard
builds-toward:
- bifurcation-in-odes
tags:
- nonlinear
- approximation
- local-analysis
stage: advanced
status: draft
---

# Linearization of Nonlinear Systems

## Core Idea
For a nonlinear system y' = f(y), linearize near an equilibrium y* by computing the Jacobian matrix J = ∇f(y*). The linearized system y' ≈ J(y - y*) reveals local stability; if J has eigenvalues with Re(λ) ≠ 0, the nonlinear equilibrium inherits the stability of the linearized system.
