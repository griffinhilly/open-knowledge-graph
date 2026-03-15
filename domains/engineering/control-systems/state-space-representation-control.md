---
id: state-space-representation-control
title: State-Space Representation
domain: engineering
course: control-systems
prerequisites:
- id: transfer-functions-control
  type: soft
- id: matrices-intro
  type: hard
- id: differential-equations-intro-separable
  type: hard
- id: eigenvalues-and-eigenvectors
  type: soft
- id: linear-transformations
  type: hard
- id: eigenvalues-eigenvectors
  type: hard
builds-toward:
- state-transition-matrix
- controllability-and-observability
tags:
- state-space
- state-variables
- A-matrix
- MIMO
- modern-control
stage: advanced
status: validated
---

# State-Space Representation

## Core Idea
State-space representation describes a dynamical system using first-order matrix differential equations: ẋ = Ax + Bu, y = Cx + Du, where x is the state vector, u is the input, y is the output, and A, B, C, D are constant system matrices. Unlike transfer functions, state-space models naturally represent MIMO (multiple-input, multiple-output) systems and capture all internal dynamics including unobservable or uncontrollable modes. The eigenvalues of the A matrix are the system's natural frequencies (closed-loop poles). State variables are not unique — any invertible linear transformation yields an equivalent representation with different A, B, C matrices but identical input-output behavior.

## How It's Best Learned
Practice converting second-order differential equations into companion-form state space, then verify by computing H(s) = C(sI−A)⁻¹B + D and confirming it matches the original transfer function. Implement state-space simulations using scipy.signal.StateSpace.

## Common Misconceptions
- State variables need not be physical quantities — they are mathematical constructs chosen to make equations first-order, and infinitely many valid choices exist for the same system.
- Transfer functions can miss uncontrollable or unobservable modes that cancel in the ratio Y(s)/U(s); state-space models expose all internal dynamics.
- The D matrix (direct feedthrough) is zero for strictly proper systems (more denominator poles than numerator zeros), which includes most physical plants.
