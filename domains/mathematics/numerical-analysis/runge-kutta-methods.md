---
id: runge-kutta-methods
title: Runge-Kutta Methods
domain: mathematics
course: numerical-analysis
prerequisites:
- id: eulers-method-convergence
  type: hard
builds-toward:
- multistep-methods-adams
- stiff-equations
tags:
- runge-kutta
- ode
- high-order
stage: abstract-reasoning
status: draft
---

# Runge-Kutta Methods

## Core Idea
Runge-Kutta methods use intermediate (stage) evaluations of f to improve accuracy. The classical 4th-order RK4 achieves error O(h⁵) with four function evaluations per step. RK methods are explicit (computing stages sequentially) or implicit (solving systems), with explicit methods simpler but sensitive to stiffness. RK methods are the workhorse of ODE solving due to their simplicity and effectiveness.
