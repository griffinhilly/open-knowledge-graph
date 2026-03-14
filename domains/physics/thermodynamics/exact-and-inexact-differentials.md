---
id: exact-and-inexact-differentials
title: Exact and Inexact Differentials
domain: physics
course: thermodynamics
prerequisites:
- id: path-functions-vs-state-functions
  type: hard
- id: partial-derivatives
  type: soft
builds-toward:
- maxwell-relations-thermodynamics
- legendre-transformations-potentials
tags:
- mathematics
- differentials
- path-dependence
stage: formal-systems
status: draft
---

# Exact and Inexact Differentials

## Core Idea
An exact differential dZ represents a state function—integrating it between two states always yields the same result regardless of path, symbolized by the line integral ∮ dZ = 0 around any closed path. An inexact differential đQ (heat) or đW (work) depends on the path taken and cannot be written as a state function differential; this is indicated by the bar through the d. Recognizing which differentials are exact is essential for identifying which quantities are state functions.

## How It's Best Learned
Test exactness using the condition ∂M/∂y = ∂N/∂x for a differential M dx + N dy. Apply to internal energy and heat in simple thermodynamic processes.

## Common Misconceptions
- Writing dQ when Q is not a state function; the symbol đQ is correct.
- Thinking inexact differentials cannot be integrated.
- Confusing inexact differentials with non-conservative forces in mechanics.
