---
id: landau-theory-phase-transitions
title: Landau Theory of Phase Transitions
domain: physics
course: statistical-mechanics
prerequisites:
- id: free-energy-thermodynamic-relations
  type: hard
builds-toward:
- renormalization-group-scaling
- scaling-invariance-universality
tags:
- landau-theory
- free-energy-expansion
- ginzburg-landau
stage: advanced
status: draft
---

# Landau Theory of Phase Transitions

## Core Idea
Landau theory expands the free energy F as a power series in the order parameter m near criticality: F = f₀ + αm² + βm⁴ + .... The coefficients α(T) and β determine the phase diagram and critical exponents. Though it neglects fluctuations (failing near T_c), Landau theory is remarkably predictive and provides a unified framework for diverse transitions.

## Explainer

You know from **free energy and thermodynamic relations** that a system in equilibrium minimizes its free energy F at fixed temperature and volume (or minimizes G at fixed T and P). Landau's insight was to ask: what happens to F as you approach a phase transition? Rather than computing F from microscopic details, he wrote it as a power series in a single key variable called the **order parameter** m, which measures how ordered the system is. For a ferromagnet, m is the average magnetization — zero in the disordered phase, nonzero below the Curie temperature. For a liquid-gas transition at the critical point, m measures the density difference. For a superconductor, m is a complex amplitude related to the Cooper pair density. The specific physics differs, but the mathematical structure of the free energy expansion is the same.

The free energy takes the form F(m) = f₀ + α(T)m² + βm⁴ + ... where odd powers are excluded by symmetry (the system looks the same if m → −m). The equilibrium value of m is found by minimizing: dF/dm = 2αm + 4βm³ = 0. When α > 0, the only minimum is at m = 0 — the disordered phase. When α < 0, two symmetric minima appear at m = ±√(−α/2β) — the ordered phase with spontaneous symmetry breaking. The **phase transition** occurs when α changes sign, which Landau assumed happens linearly in temperature: α(T) = a(T − T_c). The equilibrium order parameter then scales as m ∝ (T_c − T)^{1/2} just below T_c, giving a **critical exponent** β = 1/2 (using the conventional β notation for exponents, not the β coefficient in F).

This is the power of the approach: a single framework with two parameters (α and β in F) predicts not just that a transition happens, but the precise temperature dependence of all thermodynamic quantities near T_c. The specific heat shows a discontinuous jump at T_c, the susceptibility diverges as χ ∝ |T − T_c|^{−1}, and the equation of state takes a universal form at criticality. Different physical systems — magnets, superfluids, binary alloys — share these same exponents within Landau theory, a first glimpse of **universality**: the idea that systems with the same symmetry breaking pattern have the same critical behavior regardless of microscopic details.

Landau theory fails very close to T_c because it ignores fluctuations — spatial variations in m that become large and correlated near the critical point. This is quantified by the **Ginzburg criterion**: fluctuations are negligible when the correlation length is small compared to atomic scales, which holds away from T_c. Right at T_c, fluctuations dominate and the mean-field Landau exponents (β = 1/2, γ = 1) are replaced by non-classical values. Correcting this failure is what drives the renormalization group (your next topic), which can be understood as a systematic method for integrating out fluctuations on successively longer length scales and tracking how the effective Landau parameters evolve as you zoom out.
