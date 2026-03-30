---
id: anderson-localization
title: Disordered Systems and Anderson Localization
domain: physics
course: condensed-matter-physics
prerequisites:
- id: bloch-theorem
  type: hard
- id: band-structure-density-of-states
  type: soft
tags:
- anderson-localization
- disorder
- metal-insulator-transition
- weak-localization
stage: expert
status: validated
---

# Disordered Systems and Anderson Localization

## Core Idea
Anderson localization is the absence of diffusion of waves in a disordered medium. In a crystal with random potential disorder, sufficiently strong disorder causes all electronic wavefunctions to become exponentially localized: |psi(r)| ~ exp(-|r - r_0|/xi_loc), where xi_loc is the localization length. In 1D and 2D, all states are localized for any amount of disorder. In 3D, a mobility edge separates localized states (in the band tails) from extended states (in the band center), and the metal-insulator transition (Anderson transition) occurs when the Fermi level crosses the mobility edge. Anderson localization is a wave interference phenomenon — it applies to light, sound, and matter waves, not just electrons.

## Questions

```yaml
- question: "Anderson localization is fundamentally a wave interference phenomenon, not a classical scattering effect. What distinguishes it from classical diffusion in a disordered medium?"
  type: multiple-choice
  options:
    - "Classical scattering also produces localization if the mean free path is short enough"
    - "In classical diffusion, waves (or particles) scatter randomly and eventually diffuse to infinity. Anderson localization occurs when quantum interference between multiply scattered wave paths causes destructive interference in the forward direction and constructive interference in the backward direction (coherent backscattering), suppressing diffusion. This is purely a wave effect — it requires phase coherence and has no classical analog"
    - "Anderson localization only occurs at zero temperature"
    - "Classical diffusion is faster than quantum diffusion"
  answer: 1
  explanation: "The key insight is that in a disordered potential, a wave traveling along path A from point 1 to point 2 interferes with waves along all other paths. Most interference averages out (random phases). But the time-reversed path (path A traversed backward) always has exactly the same phase as path A, producing constructive interference in the backward direction. This 'coherent backscattering' enhances the return probability by a factor of 2 over the classical value and, for strong enough disorder, halts diffusion entirely. The effect requires phase coherence and is destroyed by decoherence (inelastic scattering, finite temperature)."

- question: "In 1D and 2D, all single-particle states are localized for any amount of disorder, no matter how weak. In 3D, a metal-insulator transition occurs at finite disorder strength. What causes this dimensional dependence?"
  type: multiple-choice
  options:
    - "The density of states is different in different dimensions"
    - "In lower dimensions, quantum interference corrections to conductivity (weak localization) are logarithmically (2D) or linearly (1D) divergent as temperature → 0 or system size → ∞, inevitably driving the conductivity to zero. In 3D, the corrections are finite and the system can remain metallic for weak disorder. The scaling theory of localization (Abrahams, Anderson, Licciardello, Ramakrishnan, 1979) shows that the 'beta function' β = d(ln g)/d(ln L) determines the flow: in ≤2D it always flows to g = 0 (insulator); in 3D there is an unstable fixed point separating metallic and insulating flows"
    - "Disorder is stronger in lower dimensions"
    - "The crystal structure prevents localization in 3D"
  answer: 1
  explanation: "The scaling theory makes this precise using the dimensionless conductance g(L) at scale L. For g >> 1 (metallic regime), δg/g ∝ L^{d-2}, where d is the dimension. In 1D and 2D, the correction is always negative and grows with L, so g(L) → 0 as L → ∞ regardless of the initial g. In 3D, the Ohmic correction g ~ σL is positive and grows faster than the quantum correction, so a metal with high enough g remains metallic. The critical disorder where the 3D transition occurs defines the mobility edge in energy."

- question: "Anderson localization has been directly observed not only for electrons but also for photons, ultrasound, and ultracold atoms, confirming its wave-interference nature."
  type: true-false
  answer: true
  explanation: "Anderson localization is a universal wave phenomenon. It was observed for microwaves in random media (1997), for ultrasound in elastic networks (2008), for photons in disordered photonic lattices (2007), and for ultracold atoms in random optical potentials (2008, simultaneously by Billy et al. and Roati et al.). These experiments are particularly clean because they avoid the complications of electron-electron interactions and inelastic scattering that complicate electronic Anderson localization. The observations confirm that localization arises purely from coherent interference of multiply scattered waves in a random medium."

- question: "Explain the concept of weak localization and its experimental signature in magnetoresistance measurements."
  type: short-answer
  answer: "Weak localization is the precursor to Anderson localization in weakly disordered metals. Coherent backscattering enhances the return probability of an electron to its starting point, reducing the classical conductivity by a small correction δσ. A magnetic field breaks time-reversal symmetry, destroying the constructive interference between time-reversed paths. This removes the weak localization correction, increasing the conductivity — producing a negative magnetoresistance (resistance decreases with field). This is the experimental signature: a cusp-like dip in resistance at B = 0, with the resistance rising as |B| increases on a scale set by the phase coherence length. The phase coherence length L_φ (limited by inelastic scattering) can be extracted from the magnetoresistance curve."
  explanation: "Weak anti-localization occurs in materials with strong spin-orbit coupling, where the spin rotates during scattering and the interference becomes destructive (positive magnetoresistance, resistance peak at B = 0). This is actually the case for topological insulator surface states, providing an experimental signature of their spin-orbit-coupled nature."
```

## Explainer

Bloch's theorem tells us that electrons in a perfect crystal propagate freely as Bloch waves. But real materials always contain disorder: impurities, vacancies, grain boundaries, lattice distortions. Philip Anderson showed in 1958 that sufficiently strong disorder causes a qualitative change in the nature of electronic states: they become **exponentially localized** in space, with wavefunctions decaying as |psi| ~ exp(-|r|/xi_loc). A localized electron cannot propagate to infinity and does not contribute to DC transport. If all states at the Fermi level are localized, the material is an Anderson insulator.

The mechanism is **quantum interference** among multiply scattered wave paths. In a disordered potential, an electron follows many scattering paths from point A to point B, and their amplitudes add coherently. For most paths, the phases are random and average out. But there is a special class of paths: for every path from A back to A, the time-reversed path has exactly the same phase (by time-reversal symmetry). This **coherent backscattering** doubles the return probability compared to the classical expectation, suppressing diffusion. When this effect is strong enough — in strongly disordered systems or low dimensions — diffusion halts entirely and all states become localized.

The **scaling theory of localization** (1979) provides the dimensional classification. The key quantity is the dimensionless conductance g(L) of a sample of size L. In 1D and 2D, quantum corrections always drive g(L) to zero as L increases, meaning all states are localized for any disorder strength. In 3D, a metallic regime (g increasing with L) can persist for weak disorder, and the **Anderson metal-insulator transition** occurs at a critical disorder strength. At the transition, the localization length diverges: xi_loc ~ |W - W_c|^{-nu}, with a universal critical exponent nu ~ 1.57 in 3D.

The practical manifestation of weak disorder in metals is **weak localization** — a small quantum correction to the classical (Drude) conductivity. Weak localization reduces the conductivity at zero magnetic field but is destroyed by an applied field (which breaks time-reversal symmetry and removes coherent backscattering). The resulting **negative magnetoresistance** — resistance dipping at B = 0 — is one of the most commonly measured quantum transport signatures in mesoscopic physics. In materials with strong spin-orbit coupling, the sign flips (weak anti-localization, positive magnetoresistance), providing a direct probe of spin-orbit physics. Anderson localization extends far beyond electrons: it has been observed for light, sound, and cold atoms, confirming its universal wave-interference origin and establishing it as one of the most fundamental phenomena in wave physics.
