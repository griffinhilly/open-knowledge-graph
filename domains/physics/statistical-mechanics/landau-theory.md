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
stage: expert
status: draft
---

# Landau Theory of Phase Transitions

## Core Idea
Landau theory expands the free energy as a power series in an order parameter m that vanishes in the disordered phase. A phenomenological expansion F(m,T) = F_0 + a(T)m^2 + b m^4 + ... predicts second-order transitions at a(T)=0 and reproduces critical exponents (β=1/2, γ=1, ν=1/2), though these differ from experimental values due to mean-field approximations.

## Questions

```yaml
- question: "In a Landau expansion F = F₀ + a(T)m² + bm⁴ (with b > 0), suppose a(T) is positive at high temperature and changes sign as temperature decreases through T_c. What happens to the equilibrium state at the transition?"
  type: multiple-choice
  options:
    - "The order parameter m jumps discontinuously from 0 to a large nonzero value — a first-order transition"
    - "The minimum of F shifts smoothly from m = 0 to two symmetric minima at m = ±√(−a/2b), so the order parameter grows continuously from zero — a second-order transition"
    - "The order parameter remains zero below T_c because the free energy is always minimized at m = 0"
    - "The system becomes unstable and no equilibrium exists below T_c"
  answer: 1
  explanation: "When a > 0, the free energy has a single minimum at m = 0 (disordered phase). As a passes through zero and becomes negative, the curvature at the origin reverses: m = 0 becomes a local maximum, and two new minima appear symmetrically at m = ±√(−a/2b). Because the minima emerge continuously from m = 0, this is a second-order (continuous) transition. A first-order transition (option A) would require the coexistence of a local minimum at m = 0 and minima at m ≠ 0 simultaneously — which would require a cubic term or a negative b, neither of which is present here."

- question: "Landau theory predicts the critical exponent β = 1/2 for the onset of order below T_c, but experiments on 3D magnets give β ≈ 0.33. What is the fundamental physical reason for this discrepancy?"
  type: multiple-choice
  options:
    - "The power-series expansion of F is truncated too early; including higher-order terms would give the correct exponent"
    - "Landau theory neglects fluctuations in the order parameter, which become large and long-range correlated near the critical point — the mean-field approximation fails precisely where it matters most"
    - "The order parameter for a ferromagnet was chosen incorrectly; the correct choice would give β = 0.33"
    - "The linear approximation a(T) = a₀(T − T_c) is too crude; a nonlinear a(T) would fix the exponent"
  answer: 1
  explanation: "Landau theory is a mean-field theory: it assumes the order parameter is uniform throughout the system and ignores spatial fluctuations. Near the critical point, this assumption breaks down catastrophically — fluctuations in the order parameter become large and correlated over distances that diverge as T → T_c. These fluctuations, completely absent from the Landau free energy, are what drive the critical exponents away from mean-field values. Including more terms in the polynomial (option A) or modifying a(T) (option D) does not address the root issue, which is the neglect of correlated fluctuations. The renormalization group framework is the correct tool for treating fluctuations systematically."

- question: "Landau theory can describe any second-order phase transition by choosing an appropriate order parameter — the mathematical structure of the free energy expansion is determined by the symmetry being broken, not by microscopic details."
  type: true-false
  answer: true
  explanation: "This is the deep power of Landau theory: it is a symmetry-based framework, not a microscopic model. Once you identify the order parameter and the symmetry it breaks, symmetry constraints determine which terms appear in the expansion. A ferromagnet with m → −m symmetry gets only even powers. A superconductor with a complex order parameter gets |ψ|² and |ψ|⁴ terms. A liquid crystal with a traceless tensor order parameter gets a cubic term (enabling first-order transitions). The same mathematical structure unifies ferromagnetism, superconductivity, liquid crystal transitions, and many others — the physics differs, but the symmetry analysis is identical."

- question: "Landau theory fails because its polynomial expansion of the free energy is the wrong mathematical form; replacing it with a more accurate functional would give the correct experimental critical exponents."
  type: true-false
  answer: false
  explanation: "The failure of Landau theory is not about the functional form of the free energy — it is about the neglect of spatial fluctuations. Even if you used a more sophisticated free energy functional, a mean-field treatment that ignores fluctuations would still give the wrong critical exponents. What is needed is not a better free energy but a fundamentally different approach — the renormalization group — that explicitly accounts for how fluctuations at different length scales contribute to the critical behavior. Landau theory gets the qualitative structure of transitions right; its quantitative failure at the critical point is specifically due to the divergence of fluctuation-driven correlations, not the polynomial approximation."

- question: "Explain why Landau theory correctly predicts the qualitative structure of a phase transition — including symmetry breaking and the shape of the phase diagram — while giving wrong quantitative values for critical exponents."
  type: short-answer
  answer: "Landau theory captures the correct qualitative physics because the existence and symmetry of the phase transition are determined by the topology of the free energy landscape, which is correctly described by the polynomial expansion: one minimum vs. two minima, and the symmetry of those minima. The critical exponents, however, depend on how fluctuations grow as T → T_c, and Landau theory ignores these fluctuations entirely. Near the critical point, the correlation length diverges and the order parameter fluctuates over long distances — these fluctuations renormalize the effective coefficients in the free energy in ways that Landau theory cannot capture. The mean-field approximation is excellent far from T_c (where fluctuations are small) and wrong at T_c (where they dominate)."
  explanation: "This distinction — correct qualitative structure, wrong quantitative exponents — is pedagogically important because it shows that a theory can be both useful and wrong. Landau theory organizes our thinking about all second-order transitions, provides the correct symmetry analysis, and gives good quantitative predictions outside the critical region. Its failure is localized and understood, which is exactly the kind of failure that leads to progress: the renormalization group was developed specifically to fix this known deficiency."
```

## Explainer

From your study of critical phenomena and the Helmholtz free energy, you know that a system minimizes its free energy F = U − TS at equilibrium, and that near a critical point, observables like magnetization or density difference develop singular behavior described by critical exponents. Landau theory is a remarkably elegant framework for organizing this physics without solving any microscopic model: the entire structure of the phase transition follows from symmetry and the requirement that F be analytic in the order parameter.

The **order parameter** m is the quantity that is zero in the disordered phase and nonzero in the ordered phase. For a ferromagnet, it is the spontaneous magnetization; for a liquid-gas transition near the critical point, it is the density difference (ρ_liq − ρ_gas); for a superconductor, it is the complex amplitude of the Cooper pair wavefunction. The specific choice of order parameter encodes the symmetry that is broken at the transition. Landau's insight was that near the transition, m is small, so F can be expanded as a power series in m. Symmetry then restricts which terms appear: if the system has m → −m symmetry (as a ferromagnet does), only even powers survive: F = F_0 + a(T)m² + bm⁴ + ...

The physics is determined by the coefficient a(T). When a > 0, the free energy has a single minimum at m = 0 — the system is in the disordered phase. When a < 0, the m = 0 state becomes a local maximum (unstable), and two new minima appear at m = ±√(−a/2b) — the system spontaneously breaks symmetry and orders. The transition occurs when a changes sign, which Landau parametrizes as a(T) = a₀(T − T_c). This simple linear form for a(T) is the mean-field assumption, and it predicts that the order parameter grows as m ∝ (T_c − T)^β with **β = 1/2** — a square-root onset just below the critical temperature.

Landau theory predicts a consistent set of critical exponents (β = 1/2, γ = 1, ν = 1/2), forming what is called **mean-field exponents**. These are wrong for real systems in low dimensions — experiments on magnetic materials give β ≈ 0.33 in 3D — because Landau theory ignores fluctuations. Near the critical point, fluctuations in the order parameter are not small and not spatially independent; they are correlated over long distances (the correlation length diverges). Landau theory's power is as the baseline: it gets the qualitative structure correct (the existence of a transition, the symmetry-breaking pattern, the shape of the phase diagram), and it identifies precisely where fluctuations matter most — near the critical point. Understanding where mean-field theory fails is the starting point for the renormalization group.
