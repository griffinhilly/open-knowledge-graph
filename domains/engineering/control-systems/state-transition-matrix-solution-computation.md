---
id: state-transition-matrix-solution-computation
title: State Transition Matrix and Solution Computation
domain: engineering
course: control-systems
prerequisites:
- id: state-transition-matrix
  type: hard
- id: state-space-representation-control
  type: hard
builds-toward:
- state-observer-full-and-partial-observation
tags:
- state-space
- exponential-matrix
- time-domain-solution
- discretization
stage: abstract-reasoning
status: draft
---

# State Transition Matrix and Solution Computation

## Core Idea
The state transition matrix Φ(t) = eAt solves the homogeneous state equation ẋ = Ax without Laplace transforms. The complete solution is x(t) = Φ(t)x(0) + ∫₀ᵗ Φ(t−τ)Bu(τ)dτ. Computation of eAt can be done via Laplace transform inversion or diagonalization.
