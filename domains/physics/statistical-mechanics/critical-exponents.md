---
id: critical-exponents
title: Critical Exponents and Universality Classes
domain: physics
course: statistical-mechanics
prerequisites:
- id: critical-phenomena-statmech
  type: hard
- id: order-parameter-phase-transition
  type: soft
builds-toward:
- renormalization-group-scaling
- scaling-invariance-universality
tags:
- critical-exponents
- universality
- scaling-laws
stage: advanced
status: draft
---

# Critical Exponents and Universality Classes

## Core Idea
Near criticality, macroscopic quantities scale as powers of the distance from criticality: heat capacity ~ |T - T_c|^(-α), order parameter ~ |T - T_c|^β, etc. Remarkably, many different microscopic systems share the same exponents (universality), determined only by symmetry and dimensionality. Exponent values are non-trivial and require renormalization group analysis.

## Explainer

You have learned that second-order phase transitions involve continuous changes in an order parameter as temperature crosses T_c — a magnet losing its spontaneous magnetization, a liquid becoming indistinguishable from its vapor. Near T_c, correlations between distant parts of the system grow without bound, and the usual approximations that work at generic temperatures break down. The system is scale-free: fluctuations occur on every length scale simultaneously. In this regime, macroscopic quantities do not vary analytically with temperature — instead, they follow **power laws** characterized by **critical exponents**.

The main exponents encode how different physical quantities vanish or diverge as the reduced temperature t = (T − T_c)/T_c approaches zero. The **order parameter exponent** β governs how the order parameter m (magnetization, density difference, etc.) vanishes below T_c: m ~ |t|^β for t < 0. The **heat capacity exponent** α describes C ~ |t|^{−α} (a divergence if α > 0, a cusp if α < 0). The **susceptibility exponent** γ governs how the response function (magnetic susceptibility, compressibility) diverges: χ ~ |t|^{−γ}. The **correlation length exponent** ν controls the length scale below which fluctuations are correlated: ξ ~ |t|^{−ν}. At exactly T_c, the order parameter response to a field goes as m ~ h^{1/δ}.

The profound mystery — and the central result — is **universality**: iron, nickel, a liquid-gas mixture, a binary alloy, and a polymer solution all share the same values of β, γ, α, ν, δ if they belong to the same **universality class**. The 3D Ising universality class (β ≈ 0.326, γ ≈ 1.237, ν ≈ 0.630) is shared by every system with a scalar order parameter in three dimensions, regardless of its microscopic chemistry. The exponents depend only on the symmetry of the order parameter and the spatial dimension. Mean-field theory predicts specific values (β = ½, γ = 1, ν = ½) that are exactly correct above the **upper critical dimension** (d = 4 for the Ising universality class) but wrong in lower dimensions due to fluctuations.

The exponents are not independent — they satisfy **scaling laws** that relate them: the Rushbrooke relation α + 2β + γ = 2, the Widom relation γ = β(δ − 1), and the Fisher relation γ = ν(2 − η). These constraints come from the scaling hypothesis: near T_c, the free energy is a generalized homogeneous function of t and h, and all critical behavior follows. Deriving the actual values requires renormalization group theory, which explains why universality holds and computes the exponents systematically by integrating out short-scale fluctuations.
