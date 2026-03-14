---
id: stability-classification
title: Stability Analysis and Classification of Equilibria
domain: mathematics
course: differential-equations
prerequisites:
- id: phase-portraits-for-linear-systems
  type: hard
- id: eigenvalue-method-for-systems
  type: hard
builds-toward:
- linearization-of-nonlinear-systems
tags:
- stability
- classification
- dynamics
stage: advanced
status: draft
---

# Stability Analysis and Classification of Equilibria

## Core Idea
For a 2D linear system y' = Ay, equilibrium (0,0) is classified as a node, saddle, spiral, or center based on eigenvalues: stable if Re(λ) < 0, unstable if Re(λ) > 0. The trace and determinant of A quickly reveal the classification.

## How It's Best Learned
Sketch the (trace, determinant) plane and label regions (stable node, unstable node, saddle, spiral, etc.). Verify classifications by computing eigenvalues and drawing phase portraits.
