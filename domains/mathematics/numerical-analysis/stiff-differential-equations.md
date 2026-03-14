---
id: stiff-differential-equations
title: Stiff Differential Equations and Stability Regions
domain: mathematics
course: numerical-analysis
prerequisites:
- id: runge-kutta-methods-for-odes
  type: hard
tags:
- stiff-equations
- stability-region
- implicit-methods
stage: advanced
status: draft
---

# Stiff Differential Equations and Stability Regions

## Core Idea
Stiff ODEs have widely separated eigenvalues; fast modes force explicit methods to use tiny steps for stability, though slow modes change slowly. Implicit methods have larger stability regions, allowing larger steps. Stiffness is problem-dependent and characterized by the ratio of largest to smallest eigenvalue magnitudes times the integration interval length.
