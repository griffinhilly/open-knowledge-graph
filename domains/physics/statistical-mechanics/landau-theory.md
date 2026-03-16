---
id: landau-theory
title: Landau Theory of Phase Transitions
domain: physics
course: statistical-mechanics
prerequisites:
- id: critical-phenomena-critical-exponents
  type: hard
- id: helmholtz-free-energy
  type: hard
builds-toward:
- mean-field-theory
tags:
- phase-transitions
- order-parameter
- mean-field
stage: advanced
status: draft
---

# Landau Theory of Phase Transitions

## Core Idea
Landau theory expands the free energy as a power series in an order parameter m that vanishes in the disordered phase. A phenomenological expansion F(m,T) = F_0 + a(T)m^2 + b m^4 + ... predicts second-order transitions at a(T)=0 and reproduces critical exponents (β=1/2, γ=1, ν=1/2), though these differ from experimental values due to mean-field approximations.

## Explainer

From your study of critical phenomena and the Helmholtz free energy, you know that a system minimizes its free energy F = U − TS at equilibrium, and that near a critical point, observables like magnetization or density difference develop singular behavior described by critical exponents. Landau theory is a remarkably elegant framework for organizing this physics without solving any microscopic model: the entire structure of the phase transition follows from symmetry and the requirement that F be analytic in the order parameter.

The **order parameter** m is the quantity that is zero in the disordered phase and nonzero in the ordered phase. For a ferromagnet, it is the spontaneous magnetization; for a liquid-gas transition near the critical point, it is the density difference (ρ_liq − ρ_gas); for a superconductor, it is the complex amplitude of the Cooper pair wavefunction. The specific choice of order parameter encodes the symmetry that is broken at the transition. Landau's insight was that near the transition, m is small, so F can be expanded as a power series in m. Symmetry then restricts which terms appear: if the system has m → −m symmetry (as a ferromagnet does), only even powers survive: F = F_0 + a(T)m² + bm⁴ + ...

The physics is determined by the coefficient a(T). When a > 0, the free energy has a single minimum at m = 0 — the system is in the disordered phase. When a < 0, the m = 0 state becomes a local maximum (unstable), and two new minima appear at m = ±√(−a/2b) — the system spontaneously breaks symmetry and orders. The transition occurs when a changes sign, which Landau parametrizes as a(T) = a₀(T − T_c). This simple linear form for a(T) is the mean-field assumption, and it predicts that the order parameter grows as m ∝ (T_c − T)^β with **β = 1/2** — a square-root onset just below the critical temperature.

Landau theory predicts a consistent set of critical exponents (β = 1/2, γ = 1, ν = 1/2), forming what is called **mean-field exponents**. These are wrong for real systems in low dimensions — experiments on magnetic materials give β ≈ 0.33 in 3D — because Landau theory ignores fluctuations. Near the critical point, fluctuations in the order parameter are not small and not spatially independent; they are correlated over long distances (the correlation length diverges). Landau theory's power is as the baseline: it gets the qualitative structure correct (the existence of a transition, the symmetry-breaking pattern, the shape of the phase diagram), and it identifies precisely where fluctuations matter most — near the critical point. Understanding where mean-field theory fails is the starting point for the renormalization group.
