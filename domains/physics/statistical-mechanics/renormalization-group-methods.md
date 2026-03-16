---
id: renormalization-group-methods
title: Renormalization Group Methods
domain: physics
course: statistical-mechanics
prerequisites:
- id: universality-classes-critical
  type: hard
- id: renormalization-group-intro
  type: soft
tags:
- renormalization
- scaling
- critical
stage: advanced
status: draft
---

# Renormalization Group Methods

## Core Idea
The renormalization group provides systematic methods for analyzing systems with scale invariance, especially near critical points. By iteratively coarse-graining (integrating out short-distance modes), one obtains RG flows showing how effective couplings evolve with length scale. Fixed points determine critical exponents and characterize universal behavior.

## Explainer

From your study of **universality classes** you know that very different physical systems share the same critical exponents near a phase transition — the same β, γ, ν. Landau theory explains why (same symmetry breaking pattern), but predicts the *wrong* exponents because it ignores fluctuations. The renormalization group (RG) is the tool that correctly handles fluctuations by systematically asking: what happens to a system's effective description when you look at it on progressively longer length scales?

The core operation is **coarse-graining**, also called a block-spin transformation (in the original Kadanoff picture). Imagine an Ising lattice of spins. Group neighboring spins into blocks and replace each block with a single effective spin representing the average. The new lattice has a larger lattice spacing but fewer degrees of freedom. Crucially, the original Hamiltonian with coupling J between nearest neighbors becomes a new effective Hamiltonian with a different coupling J'. The mapping J → J' is one RG step. Repeating this procedure traces out a **trajectory in coupling-constant space** — the RG flow. The flow shows how the effective description changes with scale: some couplings grow (become **relevant**), some shrink (become **irrelevant**), and some are unchanged at special points.

**Fixed points** of the RG flow are configurations where J' = J — the system looks the same at all scales. This is exactly scale invariance, and critical points are RG fixed points. Near a fixed point, you can linearize the RG transformation: perturbations grow or shrink as (length scale)^y, where y is an eigenvalue of the linearized transformation. Perturbations with y > 0 are relevant (they grow under coarse-graining and drive the system away from the fixed point), y < 0 are irrelevant (they shrink and don't affect the long-wavelength behavior), and y = 0 are marginal. The critical exponents are determined directly by these eigenvalues: for instance, the correlation length exponent ν = 1/y_T, where y_T is the eigenvalue of the thermal perturbation. Different universality classes correspond to different fixed points with different spectra of eigenvalues.

The practical implementation of these ideas is **Wilson's ε-expansion**: work in d = 4 − ε dimensions, where the Gaussian (non-interacting) fixed point becomes slightly unstable and a new Wilson-Fisher fixed point emerges perturbatively in ε. Computing critical exponents as series in ε and then setting ε = 1 gives surprisingly accurate results for 3D systems. More sophisticated methods — exact RG equations, numerical RG, and the conformal bootstrap — extend this power to strongly coupled systems. The deep lesson is that universality is not coincidence: it arises because all members of a universality class flow to the same fixed point under coarse-graining, and the fixed point knows nothing about microscopic details. The long-wavelength physics is determined entirely by the symmetry and dimensionality of the system, which is why the same exponents appear in a magnet, a superfluid, and a binary fluid mixture near their respective critical points.
