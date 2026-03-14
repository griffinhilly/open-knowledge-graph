---
id: linearization-nonlinear-systems
title: Linearization of Nonlinear Systems Near Equilibria
domain: mathematics
course: differential-equations
prerequisites:
- id: stability-classification
  type: hard
- id: partial-derivatives
  type: hard
tags:
- linearization
- jacobian
- local-analysis
stage: advanced
status: draft
---

# Linearization of Nonlinear Systems Near Equilibria

## Core Idea
For a nonlinear system dx/dt = f(x) near equilibrium x*, compute the Jacobian J = ∂f/∂x at x*. The linearized system dx/dt ≈ J(x - x*) determines local behavior. If all eigenvalues of J have non-zero real parts, the nonlinear stability matches the linear prediction (Hartman-Grobman theorem). Linearization provides local information when global analysis is infeasible.
