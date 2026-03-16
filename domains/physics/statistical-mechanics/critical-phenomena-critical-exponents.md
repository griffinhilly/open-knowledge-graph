---
id: critical-phenomena-critical-exponents
title: Critical Phenomena and Critical Exponents
domain: physics
course: statistical-mechanics
prerequisites:
- id: phase-transitions-first-and-second-order
  type: hard
builds-toward:
- landau-theory
- renormalization-group-intro
tags:
- critical-point
- scaling
- universality
stage: advanced
status: draft
---

# Critical Phenomena and Critical Exponents

## Core Idea
Near a critical point, physical quantities diverge as power laws: correlation length ξ ∝ |T−T_c|^{−ν}, order parameter m ∝ |T−T_c|^β, susceptibility χ ∝ |T−T_c|^{−γ}. Remarkably, these critical exponents are universal—they depend only on dimension and symmetry, not microscopic details. This universality is explained by the renormalization group.

## Explainer

From your study of phase transitions, you know that a second-order (continuous) transition is characterized by the continuous vanishing of an **order parameter** — for a ferromagnet, the spontaneous magnetization m that is nonzero below T_c and zero above it. Near T_c, this vanishing is not abrupt but follows a specific functional form. The central discovery of critical phenomena is that this form is a power law: m ∝ |T − T_c|^β, where β is a dimensionless number called a **critical exponent**. The striking fact is not merely that power laws appear, but that β takes the same value for systems as physically different as a ferromagnet and a liquid-gas transition near its critical point — despite having completely different microscopic Hamiltonians.

Each observable quantity near T_c has its own critical exponent. The **correlation length** ξ measures how far apart two spins (or density fluctuations) remain correlated; it diverges as ξ ∝ |T − T_c|^{−ν}. As T → T_c from either side, correlated regions grow without bound — the system develops fluctuations on all length scales simultaneously, which is why it looks the same under a microscope and under a telescope (scale invariance). The **magnetic susceptibility** χ = ∂m/∂h (how much the order parameter responds to a small external field) also diverges: χ ∝ |T − T_c|^{−γ}. This divergence reflects the fact that near T_c the system is poised between ordered and disordered phases, so it responds infinitely sensitively to any perturbation. The specific heat diverges as C ∝ |T − T_c|^{−α}. These four exponents β, ν, γ, α are not independent — they obey scaling relations like the Rushbrooke identity α + 2β + γ = 2, so only two are truly free.

**Universality** is the profound result that all systems with the same spatial dimension d and the same symmetry of the order parameter share identical critical exponents, regardless of their microscopic details. The 3D Ising universality class (discrete up/down symmetry, three dimensions) includes both uniaxial ferromagnets and the liquid-gas critical point — β ≈ 0.326 for both, measured to three decimal places. The 3D XY class (complex order parameter, like a superfluid) has a different β ≈ 0.346. This is extraordinary: the atomic structure of helium versus a magnetic material is entirely different, yet their critical fluctuations are mathematically identical. Universality means that T_c depends on microscopic details but the exponents do not — they are determined purely by dimension and symmetry.

The key intuition for why universality holds is that near T_c the diverging correlation length ξ → ∞ means microscopic details are irrelevant. When correlated patches span millions of atoms, the behavior is governed by long-wavelength, low-frequency fluctuations, not by the specific interactions at the atomic scale. The renormalization group formalizes this by showing that under successive coarse-graining (averaging over shorter-length-scale degrees of freedom), all systems with the same symmetry flow toward the same **fixed point** in the space of Hamiltonians. The critical exponents are determined by the linearized flow near this fixed point — they are properties of the fixed point, not of the microscopic starting Hamiltonian. This is why two systems as different as water and iron can have the same β: they flow to the same fixed point under coarse-graining.
