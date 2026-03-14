---
id: stability-classification
title: Stability Classification of Linear Systems
domain: mathematics
course: differential-equations
prerequisites:
- id: phase-portraits-linear-systems
  type: hard
builds-toward:
- linearization-nonlinear-systems
tags:
- stability
- equilibrium
- classification
stage: advanced
status: draft
---

# Stability Classification of Linear Systems

## Core Idea
For dx/dt = Ax with equilibrium at x = 0, stability is determined by eigenvalues: asymptotically stable if all Re(λ) < 0 (decay to origin); unstable if any Re(λ) > 0 (grow unbounded); marginally stable if Re(λ) = 0 with geometric multiplicity equal to algebraic multiplicity. Stability is geometric and visible in phase portraits, making it the lens for understanding system behavior.
