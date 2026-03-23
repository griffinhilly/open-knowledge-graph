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
stage: expert
status: draft
---

# Gibbs Free Energy

## Core Idea
Gibbs free energy G = H − TS = U + PV − TS is the natural thermodynamic potential at constant T and P. Equilibrium occurs at minimum G; phase transitions occur when Gibbs energies of competing phases are equal. It governs chemical reactions and phase behavior under constant pressure.

## Questions

```yaml
- question: "A reaction has ΔH = +80 kJ/mol and ΔS = +200 J/(mol·K). At what temperatures is this reaction spontaneous?"
  type: multiple-choice
  options:
    - "Never — endothermic reactions cannot be spontaneous because they increase the system's energy"
    - "Only at very low temperatures, where entropy changes are negligible"
    - "Above T = 400 K, where the TΔS term exceeds ΔH"
    - "At all temperatures, because positive ΔS always guarantees spontaneity"
  answer: 2
  explanation: "ΔG = ΔH − TΔS. For spontaneity, ΔG < 0. With ΔH = +80,000 J/mol and ΔS = +200 J/(mol·K), ΔG < 0 requires T > 80,000/200 = 400 K. Above this temperature, the entropy term TΔS dominates and ΔG goes negative. Option A embodies the key misconception: endothermic reactions can be spontaneous when entropy increases enough. The TS term in G is precisely what allows entropy to overcome unfavorable enthalpy at high temperatures."

- question: "At the melting point T_m of ice, solid ice and liquid water coexist at equilibrium under constant pressure. What can be said about their Gibbs free energies?"
  type: multiple-choice
  options:
    - "G_liquid < G_solid, which is why melting is spontaneous"
    - "G_solid < G_liquid, which is why the solid phase remains present"
    - "G_solid = G_liquid at T_m; neither phase is preferred"
    - "G is undefined at a phase transition because entropy is discontinuous"
  answer: 2
  explanation: "Phase equilibrium is the condition G_solid = G_liquid. If G_liquid were lower, all the ice would melt; if G_solid were lower, all the water would freeze. Coexistence requires equality. Below T_m the solid has lower G and is stable; above T_m the liquid wins. The transition point is exactly where the two G curves cross. This is the Gibbs criterion for phase equilibrium, and it makes phase transitions transparent: you just find where two G surfaces intersect."

- question: "A reaction releases heat (ΔH < 0). This guarantees the reaction is spontaneous at all temperatures."
  type: true-false
  answer: false
  explanation: "ΔG = ΔH − TΔS. Even with ΔH < 0, if ΔS is also negative (the reaction decreases disorder), then at high temperatures TΔS becomes a large positive number, making ΔG = ΔH − TΔS positive. A classic example: crystallization releases heat (ΔH < 0) but greatly reduces entropy (ΔS < 0), so it becomes non-spontaneous above a certain temperature. Spontaneity requires the full ΔG criterion; enthalpy alone is not sufficient."

- question: "The Gibbs free energy G is the appropriate thermodynamic potential for processes occurring at constant temperature and pressure."
  type: true-false
  answer: true
  explanation: "Different fixed conditions call for different natural potentials. At constant T and V, use Helmholtz free energy F = U − TS. At constant T and P — the usual condition for chemistry open to the atmosphere and for most biological processes — use G = H − TS = U + PV − TS. At constant T and P, spontaneous processes decrease G, and equilibrium occurs at minimum G. This is why G dominates chemistry and biochemistry: lab reactions and living cells both operate under approximately constant pressure."

- question: "Why can an endothermic reaction (ΔH > 0) still proceed spontaneously? What determines whether it will?"
  type: short-answer
  answer: "Spontaneity is governed by ΔG = ΔH − TΔS, not by ΔH alone. If the reaction increases entropy (ΔS > 0), then at sufficiently high temperature the term TΔS becomes large, making ΔG = ΔH − TΔS negative even when ΔH is positive. The crossover temperature is T = ΔH/ΔS; above this temperature, entropy wins the competition with enthalpy and the reaction proceeds spontaneously."
  explanation: "This captures the central conceptual insight of Gibbs free energy: it collapses the two-law requirement — minimize energy (enthalpy) and maximize entropy — into a single temperature-weighted competition. At low temperatures enthalpy dominates; at high temperatures entropy dominates. G quantifies exactly which effect wins at any given T and P."
```

## Explainer

You already know the Helmholtz free energy F = U − TS, which is the natural thermodynamic potential when you control temperature and volume. But most chemistry and much of physics happens at fixed temperature *and* fixed pressure — think of reactions open to the atmosphere, or water boiling at sea level. For those conditions, you need a different potential. The **Gibbs free energy** G = H − TS = U + PV − TS is constructed by adding the PV term to Helmholtz, turning the natural variables from (T, V) to (T, P). The shift is a **Legendre transform** — the same mathematical trick that converts the Lagrangian to the Hamiltonian in mechanics, swapping a variable for its conjugate.

The physical meaning of G follows directly. For a process at constant T and P, the second law requires that the total entropy of system plus surroundings increases. Working through this constraint, you find that spontaneous processes at constant T and P must have dG ≤ 0. The system relaxes toward the state of **minimum Gibbs free energy**. Equilibrium occurs when dG = 0 — no more free energy can be extracted. This is the condition that chemical reactions and phase transitions satisfy at equilibrium.

Phase transitions become transparent in the Gibbs framework. At the melting point of ice, for example, both liquid water and solid ice are present simultaneously. This is only possible if their Gibbs free energies are equal: G_liquid(T_m, P) = G_solid(T_m, P). Below T_m the solid has lower G and is stable; above T_m the liquid wins. The transition temperature is exactly where the two G curves cross. For a **first-order transition**, the crossing has a kink — the first derivative of G (which gives entropy S = −(∂G/∂T)_P and volume V = (∂G/∂P)_T) is discontinuous, producing latent heat and a volume jump. For a **second-order transition**, G is continuous through the crossing but curves in a way that changes the second derivatives (heat capacity, compressibility), with no latent heat.

The decomposition G = H − TS captures the competition between energy and entropy. A reaction that releases enthalpy (exothermic, ΔH < 0) tends to lower G, making it spontaneous. A reaction that produces more disorder (ΔS > 0) also lowers G, especially at high temperature where the TS term dominates. This competition explains why some endothermic reactions still proceed spontaneously at high enough temperature — entropy wins — and why others that release heat are still suppressed at high temperature because they reduce entropy. The formula ΔG = ΔH − TΔS quantifies the tug-of-war between enthalpy and entropy that governs equilibrium in chemistry, materials science, and biology.
