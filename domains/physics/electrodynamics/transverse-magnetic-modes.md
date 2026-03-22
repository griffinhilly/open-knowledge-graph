---
id: transverse-magnetic-modes
title: Transverse Magnetic (TM) Modes
domain: physics
course: electrodynamics
prerequisites:
- id: waveguide-equations-general
  type: hard
builds-toward:
- rectangular-waveguide-propagation
- circular-waveguide-propagation
tags:
- tm-modes
- guided-waves
- cutoff-frequency
stage: advanced
status: draft
---

# Transverse Magnetic (TM) Modes

## Core Idea
TM modes have zero longitudinal magnetic field (Hz = 0) but nonzero Ez. Like TE modes, they have cutoff frequencies. The boundary condition Ez = 0 at perfect conductors determines allowed transverse wavenumbers and mode patterns.

## Questions

```yaml
- question: "In a rectangular waveguide, why is TM₁₁ the lowest-order TM mode, while TE₁₀ is the lowest-order TE mode?"
  type: multiple-choice
  options:
    - "TM modes inherently require higher frequencies than TE modes, so their mode indices must both be at least 1"
    - "The boundary condition Ez = 0 at the walls forces both m and n ≥ 1, since setting either to zero makes Ez vanish everywhere; TE modes have no such constraint on Hz"
    - "TM₁₀ exists but has a higher cutoff frequency than TE₁₀, so TM₁₁ is only the second-lowest TM mode"
    - "The transverse magnetic field in TM modes prohibits a zero index in the y-direction only, requiring n ≥ 1"
  answer: 1
  explanation: "For TM modes, Ez ∝ sin(mπx/a)sin(nπy/b). Setting m = 0 or n = 0 forces a sine argument to zero, making Ez identically zero everywhere — a trivial solution with no actual mode. For TE modes, Hz ∝ cos(mπx/a)cos(nπy/b), and cos(0) = 1, so setting m = 0 (TE₁₀) still gives a non-trivial field distribution. The difference lies in the Dirichlet (sine) vs. Neumann (cosine) nature of the two boundary conditions."

- question: "A rectangular waveguide operates at a frequency between the cutoff frequencies of TM₁₁ and TM₂₁. Which TM modes propagate?"
  type: multiple-choice
  options:
    - "None — at a frequency between two mode cutoffs, all TM modes are evanescent"
    - "Both TM₁₁ and TM₂₁ — once the guide is above any mode's cutoff, all modes propagate simultaneously"
    - "Only TM₁₁ — its cutoff is below the operating frequency, so it propagates; TM₂₁ is above cutoff and cannot propagate"
    - "Only TM₁₁ — it is above its cutoff frequency, so it propagates; TM₂₁ is below its cutoff and is evanescent"
  answer: 3
  explanation: "A mode propagates if and only if the operating frequency exceeds that mode's cutoff frequency. Between fc(TM₁₁) and fc(TM₂₁), the frequency is above the lower cutoff (TM₁₁ propagates) and below the upper cutoff (TM₂₁ is evanescent — exponentially decaying). Option C reverses the logic: 'above cutoff' means the mode propagates, not the reverse."

- question: "In a TM waveguide mode, both the phase velocity and the group velocity exceed the speed of light in vacuum."
  type: true-false
  answer: false
  explanation: "Only the phase velocity (v_p = ω/β) exceeds c; the group velocity (v_g = dω/dβ), which carries energy and information, is always less than c. Their product satisfies v_p · v_g = c². This apparent superluminal phase velocity is not a violation of special relativity because phase fronts do not carry energy or information — only the group velocity does."

- question: "For TM modes in a rectangular waveguide, all four transverse field components (Ex, Ey, Hx, Hy) can be derived entirely from the longitudinal field Ez once the boundary conditions are satisfied."
  type: true-false
  answer: true
  explanation: "This is a fundamental structural property of the TE/TM decomposition. For TM modes (Hz = 0), the 2D Helmholtz equation determines Ez, and the waveguide equations then give all transverse components algebraically in terms of Ez and its derivatives. Ez is the 'generating function' for the entire mode — knowing it completely specifies the field distribution."

- question: "Explain why TM modes in a rectangular waveguide cannot have either mode index equal to zero, and what this implies about TM cutoff frequencies compared to TE modes."
  type: short-answer
  answer: "For TM modes, Ez ∝ sin(mπx/a)sin(nπy/b). If m = 0 or n = 0, the corresponding sine is identically zero, making Ez = 0 everywhere — no mode exists. So both m, n ≥ 1, and the lowest TM mode is TM₁₁. TE modes use cosines for Hz, so cos(0) = 1 ≠ 0 allows m = 0 or n = 0, giving the TE₁₀ fundamental mode. Since TM₁₁ has a higher cutoff frequency than TE₁₀, the dominant mode in a standard rectangular waveguide is always TE₁₀."
  explanation: "The underlying reason is the difference in boundary conditions: TM modes satisfy a Dirichlet condition (Ez = 0 at the wall), leading to sine eigenfunctions that vanish at zero index; TE modes satisfy a Neumann condition (∂Hz/∂n = 0 at the wall), leading to cosine eigenfunctions that do not vanish at zero index. This has major practical consequences — microwave engineers always design single-mode waveguides around TE₁₀, not any TM mode."
```

## Explainer

From your study of general waveguide theory, you know that electromagnetic fields inside a metallic waveguide can be decomposed into two independent families: **transverse electric (TE)** modes, which have Ez = 0, and **transverse magnetic (TM)** modes, which have Hz = 0. In TM modes, the magnetic field is entirely transverse to the propagation direction, while the electric field has both transverse components and a longitudinal component Ez along the guide axis.

The governing equation for TM modes comes from substituting Hz = 0 into the waveguide equations. The longitudinal electric field satisfies the 2D Helmholtz equation in the transverse plane: (∇²ₜ + γ²c)Ez = 0, where γc = √(k² − β²) is the transverse wavenumber, k = ω/c is the free-space wavenumber, and β is the propagation constant along the guide. Once Ez is found by solving this equation with boundary conditions, all transverse field components (Eₓ, Eᵧ, Hₓ, Hᵧ) follow algebraically.

The crucial difference between TM and TE modes lies in their boundary condition. For a perfect conductor, the tangential electric field must vanish at the walls. Since Ez is tangential to the transverse walls of a rectangular guide, the condition is **Ez = 0 on all conducting surfaces**. This is a Dirichlet boundary condition for Ez, the same structure as the "particle in a box" in quantum mechanics. For a rectangular guide with width a and height b, the allowed transverse modes are Ez ∝ sin(mπx/a)sin(nπy/b) with integers m,n ≥ 1. Neither m nor n can be zero in TM modes — setting either to zero makes Ez identically zero everywhere, which would make the entire TM mode trivial. This is why the lowest TM mode in a rectangular guide is TM₁₁, unlike TE modes where TE₁₀ (with one index zero) is the fundamental mode.

Each (m,n) combination defines a **cutoff frequency** fc = (c/2π)√((mπ/a)² + (nπ/b)²) below which that mode cannot propagate — it becomes evanescent. Above cutoff, the mode propagates with phase velocity v_p = ω/β > c and group velocity v_g = dω/dβ < c, so energy travels slower than light even though phase fronts travel faster. This dispersion is a direct consequence of the transverse boundary conditions selecting only discrete wavenumbers. Understanding TM modes alongside TE modes gives you the complete modal structure of waveguides, which is the foundation for designing microwave components, cavity resonators, and antenna feed systems.
