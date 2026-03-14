---
id: stability-regions-ode
title: Stability Regions and A-Stability
domain: mathematics
course: numerical-analysis
prerequisites:
- id: stiff-equations
  type: hard
tags:
- stability
- a-stability
- ode
stage: abstract-reasoning
status: draft
---

# Stability Regions and A-Stability

## Core Idea
For the test problem dy/dt = λy with Re(λ) < 0, a numerical method is stable if |y_{n+1}| ≤ |y_n|. The stability region is the set of hλ values for which the method is stable. An A-stable method (like implicit Euler or Crank-Nicolson) is stable for all hλ with Re(hλ) < 0, making it safe for stiff problems. Explicit methods have bounded stability regions, severely limiting step size for stiff systems.
