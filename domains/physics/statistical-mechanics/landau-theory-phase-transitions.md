---
id: landau-theory-phase-transitions
title: Landau Theory of Phase Transitions
domain: physics
course: statistical-mechanics
prerequisites:
- id: free-energy-thermodynamic-relations
  type: hard
- id: phase-transition-equilibrium
  type: hard
builds-toward:
- renormalization-group-scaling
- scaling-invariance-universality
tags:
- landau-theory
- free-energy-expansion
- ginzburg-landau
stage: expert
status: validated
---

# Landau Theory of Phase Transitions

## Core Idea
Landau theory expands the free energy F as a power series in the order parameter m near criticality: F = f₀ + αm² + βm⁴ + .... The coefficients α(T) and β determine the phase diagram and critical exponents. Though it neglects fluctuations (failing near T_c), Landau theory is remarkably predictive and provides a unified framework for diverse transitions.

## Questions

```yaml
- question: "In the Landau free energy F = f₀ + αm² + βm⁴, why are odd-power terms like m³ excluded from the expansion?"
  type: multiple-choice
  options:
    - "Odd powers would make the free energy unbounded below for large |m|, causing the model to predict unphysical infinite order"
    - "The free energy must be symmetric under m → −m because the system looks the same in states of equal and opposite order — the symmetry of the problem forbids odd powers"
    - "Odd powers are negligible near the critical point where m is small, so they are dropped as an approximation"
    - "Landau theory only applies to magnetic systems where m is a magnetization, which is always positive"
  answer: 1
  explanation: "The exclusion of odd powers is a symmetry argument, not an approximation. If a system can be in a state with order parameter +m, an equally valid state −m must exist by symmetry (e.g., a magnet can point up or down; a binary alloy can be rich in either component). The free energy must therefore satisfy F(m) = F(−m), which forces all odd-power terms to zero. This is not about m being small near T_c — it is a fundamental constraint from the physical symmetry of the problem, and it applies at all temperatures."

- question: "Landau theory predicts the same critical exponents (e.g., m ∝ (T_c − T)^{1/2} below T_c) for magnets, superfluids, and binary alloys. What drives this universality within the theory?"
  type: multiple-choice
  options:
    - "The microscopic interactions in these systems are identical at sufficiently high temperatures"
    - "The Landau free energy expansion in powers of m has the same mathematical structure for all systems with the same symmetry, so minimizing it gives identical scaling regardless of microscopic details"
    - "Landau used empirical critical exponents measured in magnets and applied them to all other systems by analogy"
    - "Universality is an approximation that holds far from T_c but breaks down close to the critical point"
  answer: 1
  explanation: "Universality in Landau theory arises because the free energy F = f₀ + αm² + βm⁴ (with α changing sign at T_c) is the same mathematical object for any system with this symmetry pattern — regardless of whether m is magnetization, superfluid density, or concentration difference. Minimizing dF/dm = 0 gives m ∝ (T_c − T)^{1/2} by pure algebra, independent of the physical system. This is why systems with the same symmetry share critical exponents: the mathematical structure of the free energy, not the microscopic Hamiltonian, determines the scaling."

- question: "Landau theory becomes more accurate as temperature approaches T_c because the order parameter m becomes small, validating the power-series expansion."
  type: true-false
  answer: false
  explanation: "This is precisely backwards. Although m becomes small near T_c (validating the power-series expansion of F in m), fluctuations in m become large and spatially correlated on long length scales near T_c. Landau theory ignores these fluctuations — it assumes m is uniform in space and uses only the mean value. The Ginzburg criterion quantifies when fluctuations dominate: close to T_c, fluctuations overwhelm the mean-field prediction, and the Landau critical exponents (β = 1/2, γ = 1) are replaced by non-classical values. Landau theory is accurate away from T_c, not at it."

- question: "In Landau theory, the phase transition occurs when the coefficient α(T) changes sign from positive to negative as temperature decreases through T_c, causing two new free-energy minima with nonzero order parameter to appear."
  type: true-false
  answer: true
  explanation: "This is the mathematical heart of the theory. For α > 0, dF/dm = 2αm + 4βm³ = 0 has only the solution m = 0 — a single minimum at the disordered state. When α < 0, the second derivative at m = 0 becomes negative (it is a local maximum), and two symmetric minima appear at m = ±√(−α/2β). Landau assumes α(T) = a(T − T_c), so α changes sign exactly at T = T_c. The system spontaneously breaks symmetry by choosing one of the two minima — this is the phase transition, and it is entirely encoded in the sign change of α."

- question: "What is the 'order parameter' in Landau theory, and how does its behavior across the phase transition encode the physics of spontaneous symmetry breaking?"
  type: short-answer
  answer: "The order parameter m is a quantity that is zero in the disordered phase and takes a nonzero value in the ordered phase. For a ferromagnet it is average magnetization; for a liquid-gas transition near the critical point it is the density difference; for a superconductor it is the Cooper pair amplitude. Above T_c, α > 0 and the free energy has a single minimum at m = 0 — no preferred ordering. As T decreases through T_c, α changes sign and the potential well at m = 0 becomes a local maximum while two new symmetric minima appear at ±m₀. The system must 'choose' one — this spontaneous symmetry breaking is the transition. Below T_c, m ∝ (T_c − T)^{1/2}, growing continuously from zero and encoding both the fact and degree of ordering."
  explanation: "The order parameter is Landau's key abstraction: it reduces the enormous complexity of a phase transition (involving 10²³ interacting particles) to the behavior of a single scalar field whose equilibrium value encodes the thermodynamic phase. The same mathematical object works for magnets, superfluids, and liquid crystals because the symmetry structure, not the microscopic details, determines the form of the free energy expansion."
```

## Explainer

You know from **free energy and thermodynamic relations** that a system in equilibrium minimizes its free energy F at fixed temperature and volume (or minimizes G at fixed T and P). Landau's insight was to ask: what happens to F as you approach a phase transition? Rather than computing F from microscopic details, he wrote it as a power series in a single key variable called the **order parameter** m, which measures how ordered the system is. For a ferromagnet, m is the average magnetization — zero in the disordered phase, nonzero below the Curie temperature. For a liquid-gas transition at the critical point, m measures the density difference. For a superconductor, m is a complex amplitude related to the Cooper pair density. The specific physics differs, but the mathematical structure of the free energy expansion is the same.

The free energy takes the form F(m) = f₀ + α(T)m² + βm⁴ + ... where odd powers are excluded by symmetry (the system looks the same if m → −m). The equilibrium value of m is found by minimizing: dF/dm = 2αm + 4βm³ = 0. When α > 0, the only minimum is at m = 0 — the disordered phase. When α < 0, two symmetric minima appear at m = ±√(−α/2β) — the ordered phase with spontaneous symmetry breaking. The **phase transition** occurs when α changes sign, which Landau assumed happens linearly in temperature: α(T) = a(T − T_c). The equilibrium order parameter then scales as m ∝ (T_c − T)^{1/2} just below T_c, giving a **critical exponent** β = 1/2 (using the conventional β notation for exponents, not the β coefficient in F).

This is the power of the approach: a single framework with two parameters (α and β in F) predicts not just that a transition happens, but the precise temperature dependence of all thermodynamic quantities near T_c. The specific heat shows a discontinuous jump at T_c, the susceptibility diverges as χ ∝ |T − T_c|^{−1}, and the equation of state takes a universal form at criticality. Different physical systems — magnets, superfluids, binary alloys — share these same exponents within Landau theory, a first glimpse of **universality**: the idea that systems with the same symmetry breaking pattern have the same critical behavior regardless of microscopic details.

Landau theory fails very close to T_c because it ignores fluctuations — spatial variations in m that become large and correlated near the critical point. This is quantified by the **Ginzburg criterion**: fluctuations are negligible when the correlation length is small compared to atomic scales, which holds away from T_c. Right at T_c, fluctuations dominate and the mean-field Landau exponents (β = 1/2, γ = 1) are replaced by non-classical values. Correcting this failure is what drives the renormalization group (your next topic), which can be understood as a systematic method for integrating out fluctuations on successively longer length scales and tracking how the effective Landau parameters evolve as you zoom out.
