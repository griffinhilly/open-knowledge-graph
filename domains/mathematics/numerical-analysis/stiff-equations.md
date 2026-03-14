---
id: stiff-equations
title: Stiff Differential Equations
domain: mathematics
course: numerical-analysis
prerequisites:
- id: multistep-methods-adams
  type: hard
builds-toward:
- stability-regions-ode
tags:
- stiff-equations
- ode
- eigenvalues
stage: abstract-reasoning
status: draft
---

# Stiff Differential Equations

## Core Idea
A system dy/dt = f(t,y) is stiff if it contains vastly different time scales—some components decay rapidly while others change slowly. The stiffness ratio is proportional to the ratio of largest to smallest eigenvalue magnitudes of the Jacobian. Explicit methods must use tiny steps for stability, making implicit methods (which are A-stable) necessary for practical stiff ODE solving.
