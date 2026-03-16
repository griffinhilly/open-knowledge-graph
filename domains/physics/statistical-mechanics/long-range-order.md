---
id: long-range-order
title: Long-Range Order
domain: physics
course: statistical-mechanics
prerequisites:
- id: two-point-correlation-functions
  type: hard
- id: phase-transitions
  type: soft
builds-toward:
- symmetry-breaking-phase-transitions
- goldstone-theorem
tags:
- order
- correlations
- phase-transitions
stage: advanced
status: draft
---

# Long-Range Order

## Core Idea
Long-range order characterizes correlations that persist at arbitrarily large distances, quantified by non-zero lim_{|r|→∞} ⟨σ(r)σ(0)⟩. Ordered phases (crystals, ferromagnets, superconductors) exhibit long-range order; disordered phases do not. Its appearance/disappearance marks a phase transition.

## Explainer

You learned about **two-point correlation functions** ⟨σ(r)σ(0)⟩ as a way to quantify how fluctuations at one point in a system relate to fluctuations at another. In a completely disordered phase — a high-temperature paramagnet, or a liquid well above its critical temperature — correlations decay exponentially: ⟨σ(r)σ(0)⟩ ~ exp(−|r|/ξ), where ξ is the **correlation length**. Beyond a few correlation lengths, distant points are statistically independent. **Long-range order** is precisely the opposite behavior: the two-point function approaches a non-zero constant as |r| → ∞, meaning distant regions of the system remain statistically coupled no matter how far apart they are. The system has global coherence built into its equilibrium state.

The physical picture behind long-range order is **spontaneous symmetry breaking**. In a ferromagnet below the Curie temperature, every spin preferentially aligns along a global direction even though the Hamiltonian treats up and down symmetrically. Once the symmetry is broken, a spin at position r "knows" about the preferred direction regardless of its distance from the origin — hence non-zero ⟨σ(r)σ(0)⟩ at large |r|. The **order parameter** m = ⟨σ⟩ is non-zero in the ordered phase: the system has selected one particular state from among the symmetry-equivalent options. The correlation function at large distance approaches m², because when |r| is very large the two spins are statistically independent conditional on the global order: ⟨σ(r)σ(0)⟩ → ⟨σ(r)⟩⟨σ(0)⟩ = m².

Different physical systems exhibit distinct types of long-range order. Crystals have **translational long-range order**: the density-density correlation function ⟨ρ(r)ρ(0)⟩ oscillates at the lattice periodicity and maintains that oscillation out to arbitrarily large distances. Liquids lack this — density correlations decay within a few molecular diameters. Superconductors and superfluids carry **off-diagonal long-range order** (ODLRO): the off-diagonal elements of the one-particle density matrix ⟨ψ†(r)ψ(0)⟩ remain non-zero at large separation, reflecting the macroscopic phase coherence of the condensate. All these examples share the same mathematical signature: a two-point function that does not decay to zero.

The appearance or disappearance of long-range order defines a phase transition. Approaching the critical point from below, the order parameter m → 0 continuously (for a second-order transition), and correlations become long-ranged but not infinite. Exactly at the critical point, the correlation length ξ diverges and the two-point function decays as a power law: ⟨σ(r)σ(0)⟩ ~ |r|^(−(d−2+η)), where η is a critical exponent. This scale-invariant behavior at the critical point — and the fact that the same exponents appear in seemingly different systems — is what makes the renormalization group approach so powerful. The correlation function is therefore not just a diagnostic of order: it is the microscopic quantity that encodes the full structure of each phase, the phase boundaries between them, and the universal behavior at criticality.
