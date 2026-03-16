---
id: gibbs-free-energy
title: Gibbs Free Energy
domain: physics
course: statistical-mechanics
prerequisites:
- id: helmholtz-free-energy
  type: hard
- id: thermodynamic-processes
  type: soft
builds-toward:
- phase-transitions-first-and-second-order
tags:
- thermodynamic-potential
- free-energy
- phase-transitions
stage: advanced
status: draft
---

# Gibbs Free Energy

## Core Idea
Gibbs free energy G = H − TS = U + PV − TS is the natural thermodynamic potential at constant T and P. Equilibrium occurs at minimum G; phase transitions occur when Gibbs energies of competing phases are equal. It governs chemical reactions and phase behavior under constant pressure.

## Explainer

You already know the Helmholtz free energy F = U − TS, which is the natural thermodynamic potential when you control temperature and volume. But most chemistry and much of physics happens at fixed temperature *and* fixed pressure — think of reactions open to the atmosphere, or water boiling at sea level. For those conditions, you need a different potential. The **Gibbs free energy** G = H − TS = U + PV − TS is constructed by adding the PV term to Helmholtz, turning the natural variables from (T, V) to (T, P). The shift is a **Legendre transform** — the same mathematical trick that converts the Lagrangian to the Hamiltonian in mechanics, swapping a variable for its conjugate.

The physical meaning of G follows directly. For a process at constant T and P, the second law requires that the total entropy of system plus surroundings increases. Working through this constraint, you find that spontaneous processes at constant T and P must have dG ≤ 0. The system relaxes toward the state of **minimum Gibbs free energy**. Equilibrium occurs when dG = 0 — no more free energy can be extracted. This is the condition that chemical reactions and phase transitions satisfy at equilibrium.

Phase transitions become transparent in the Gibbs framework. At the melting point of ice, for example, both liquid water and solid ice are present simultaneously. This is only possible if their Gibbs free energies are equal: G_liquid(T_m, P) = G_solid(T_m, P). Below T_m the solid has lower G and is stable; above T_m the liquid wins. The transition temperature is exactly where the two G curves cross. For a **first-order transition**, the crossing has a kink — the first derivative of G (which gives entropy S = −(∂G/∂T)_P and volume V = (∂G/∂P)_T) is discontinuous, producing latent heat and a volume jump. For a **second-order transition**, G is continuous through the crossing but curves in a way that changes the second derivatives (heat capacity, compressibility), with no latent heat.

The decomposition G = H − TS captures the competition between energy and entropy. A reaction that releases enthalpy (exothermic, ΔH < 0) tends to lower G, making it spontaneous. A reaction that produces more disorder (ΔS > 0) also lowers G, especially at high temperature where the TS term dominates. This competition explains why some endothermic reactions still proceed spontaneously at high enough temperature — entropy wins — and why others that release heat are still suppressed at high temperature because they reduce entropy. The formula ΔG = ΔH − TΔS quantifies the tug-of-war between enthalpy and entropy that governs equilibrium in chemistry, materials science, and biology.
