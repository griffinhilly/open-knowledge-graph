---
id: free-energy-thermodynamic-relations
title: Free Energy and Thermodynamic Relations from Partition Functions
domain: physics
course: statistical-mechanics
prerequisites:
- id: partition-function-fundamentals
  type: hard
- id: canonical-partition-function
  type: hard
- id: second-law-of-thermodynamics
  type: soft
builds-toward:
- phase-transition-equilibrium
- critical-phenomena-statmech
- landau-theory-phase-transitions
tags:
- free-energy
- helmholtz
- gibbs
- thermodynamic-potentials
stage: advanced
status: draft
---

# Free Energy and Thermodynamic Relations from Partition Functions

## Core Idea
Helmholtz (F) and Gibbs (G) free energies are natural thermodynamic potentials for the canonical and constant-pressure ensembles. They connect statistical mechanics to measurable thermodynamic quantities through Maxwell relations and are minimized at equilibrium, making them central to understanding phase transitions and stability.

## Explainer

From the canonical partition function Z = Σ exp(−βEᵢ), you can compute the average energy ⟨E⟩ = −∂ ln Z/∂β and entropy S = kB ln Z + ⟨E⟩/T. The **Helmholtz free energy** F = ⟨E⟩ − TS is simply the combination that emerges from this: F = −kBT ln Z. This single equation is the bridge between statistical mechanics and thermodynamics — once you have Z, you have F, and from F you can derive essentially every equilibrium thermodynamic property.

Why is F called a "free" energy? The name reflects the competition between energy and entropy. A system at constant temperature and volume spontaneously evolves to minimize F, not to minimize energy alone. An exothermic process (ΔE < 0) is favorable, but so is an entropy-increasing process (ΔS > 0) because −TΔS also lowers F. When these tendencies conflict — say, a process that releases heat but decreases entropy — the question of which wins depends on temperature. At high T, the TΔS term dominates and entropy wins; at low T, energy wins. This is why ice melts above 0°C (entropy gain of liquid water overwhelms the energy cost) and freezes below it.

The **Gibbs free energy** G = F + PV = ⟨E⟩ − TS + PV is the natural potential for constant-pressure, constant-temperature conditions — the conditions of most chemical and biological processes. It is minimized at equilibrium under these constraints. The condition for phase coexistence (the topic of phase equilibrium) is G_liquid = G_solid (equal Gibbs free energies per particle, i.e., equal chemical potentials μ = ∂G/∂N). Maxwell relations follow from the second-order mixed partial derivatives of these potentials. For example, from dF = −SdT − PdV, the Maxwell relation (∂S/∂V)_T = (∂P/∂T)_V connects an entropy derivative (hard to measure directly) to a pressure derivative (easy to measure). These relations are among the most practically useful results in thermodynamics.

For phase transitions, free energies are indispensable. A first-order transition occurs when two phases have equal G but the system discontinuously jumps between two minima — there is a **latent heat** and coexistence. A second-order (continuous) transition occurs when the minimum of the free energy evolves continuously but the shape of the free energy landscape changes qualitatively at Tc — this is exactly the **order parameter** picture you will develop in Landau theory. Free energy as a function of the order parameter, F(M, T), is the Landau free energy, and minimizing it gives the equilibrium order parameter. The entire language of phase transitions is built on free energies, so mastering F and G here is prerequisite to that entire framework.
