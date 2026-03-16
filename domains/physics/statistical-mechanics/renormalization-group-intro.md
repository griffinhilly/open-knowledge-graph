---
id: renormalization-group-intro
title: 'Renormalization Group: Introduction'
domain: physics
course: statistical-mechanics
prerequisites:
- id: critical-phenomena-critical-exponents
  type: hard
- id: mean-field-theory
  type: hard
tags:
- renormalization-group
- scaling
- critical-phenomena
stage: advanced
status: draft
---

# Renormalization Group: Introduction

## Core Idea
Renormalization group (RG) methods remove short-distance degrees of freedom and rescale the system, generating a flow of effective parameters (coupling constants) that governs how properties change across length scales. The RG flow toward fixed points explains universality: different microscopic systems converge to the same critical behavior if they share the same symmetry and dimensionality. RG quantitatively predicts critical exponents.

## Explainer

You've seen that mean-field theory fails to predict critical exponents correctly in low dimensions, and that the reason is the diverging correlation length ξ → ∞ at the critical point. When fluctuations exist at every length scale simultaneously, there is no single scale you can ignore — any approximation that discards small-scale fluctuations will miss their large-scale consequences. The renormalization group (RG) is the systematic procedure for dealing with this: rather than ignoring any scale, it handles them one at a time, keeping track of how the physics changes as you zoom out.

The core procedure is **coarse-graining**. Take a lattice spin system: group spins into blocks of size b (say, 2×2 blocks in two dimensions), replace each block with a single effective spin representing the majority or average, and then rescale distances so the new system looks like the original lattice. The coarse-grained system has the same form as the original Hamiltonian but with different coupling constants — a renormalized temperature, interaction strength, and so on. This generates an **RG transformation** in the space of coupling constants, and repeating the procedure traces out a **flow** through that space.

**Fixed points** of the RG flow are coupling configurations that map to themselves under coarse-graining — theories that look identical at all length scales. A critical point is exactly such a fixed point, which is why the correlation length diverges there (rescaling doesn't change the theory, so no length scale is introduced). Near a fixed point, the RG flow is linearized and characterized by **relevant** and **irrelevant** directions. Relevant perturbations grow under coarse-graining (moving you away from the fixed point); irrelevant ones shrink (flowing back). The critical exponents are determined entirely by the eigenvalues of the linearized RG transformation at the fixed point — not by the microscopic details of the model.

This is the deep explanation of universality: any two systems whose coupling constants lie in the same basin of attraction of the same fixed point will converge to the same fixed point under repeated coarse-graining, and therefore exhibit identical critical exponents. The Ising model in two dimensions, liquid-gas systems, polymer collapse — all belong to the same universality class because they share the same symmetry (Z₂) and dimensionality (2D), and thus the same fixed point. Mean-field theory gives the wrong exponents because it corresponds to the fixed point of a hypothetical infinite-dimensional system; in lower dimensions, the relevant directions of the RG flow push the system toward a different fixed point with different exponents. RG predictions of critical exponents, confirmed to extraordinary precision experimentally and numerically, stand as one of the great quantitative successes of twentieth-century theoretical physics.
