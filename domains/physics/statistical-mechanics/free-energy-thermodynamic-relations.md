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
stage: expert
status: validated
---

# Free Energy and Thermodynamic Relations from Partition Functions

## Core Idea
Helmholtz (F) and Gibbs (G) free energies are natural thermodynamic potentials for the canonical and constant-pressure ensembles. They connect statistical mechanics to measurable thermodynamic quantities through Maxwell relations and are minimized at equilibrium, making them central to understanding phase transitions and stability.

## Questions

```yaml
- question: "A chemical reaction releases heat (ΔE < 0) but decreases the entropy of the system (ΔS < 0). At very high temperatures, what happens to the spontaneity of this reaction?"
  type: multiple-choice
  options:
    - "It becomes more spontaneous — releasing heat always drives a process forward"
    - "Temperature is irrelevant — only ΔE determines spontaneity"
    - "It becomes disfavored — the −TΔS term grows with temperature and, since ΔS < 0, it adds a large positive contribution to ΔF that overwhelms the negative ΔE"
    - "It remains spontaneous at all temperatures since both ΔE and ΔS have the same sign"
  answer: 2
  explanation: "The Helmholtz free energy change is ΔF = ΔE − TΔS. When ΔS < 0, the term −TΔS is positive. At low T this contribution is small, so ΔE < 0 dominates and the reaction is favored. At high T, −TΔS grows large and can overwhelm ΔE, making ΔF > 0 — the reaction becomes disfavored. This is why temperature determines which tendency wins: at low T, energy wins; at high T, entropy wins. Free energy is the correct quantity for spontaneity, not energy alone."

- question: "Once the Helmholtz free energy F is known as a function of T and V, what range of thermodynamic properties can be derived from it?"
  type: multiple-choice
  options:
    - "Only average energy — no other equilibrium quantities follow from F alone"
    - "Only entropy and pressure — energy requires a separate calculation"
    - "Virtually all equilibrium thermodynamic properties: entropy, pressure, average energy, heat capacity, and Maxwell relations connecting otherwise inaccessible derivatives"
    - "F gives information about kinetic rates but not equilibrium properties"
  answer: 2
  explanation: "F = −kBT ln Z is the bridge between the microscopic partition function and macroscopic thermodynamics. From F(T, V) you can derive: entropy S = −(∂F/∂T)_V, pressure P = −(∂F/∂V)_T, average energy ⟨E⟩ = F + TS, heat capacity C_V = −T(∂²F/∂T²)_V, and Maxwell relations such as (∂S/∂V)_T = (∂P/∂T)_V. One equation — F = −kBT ln Z — unlocks essentially the entire equilibrium thermodynamic description of the system."

- question: "A system at constant temperature and volume spontaneously evolves toward minimizing its internal energy, not its free energy."
  type: true-false
  answer: false
  explanation: "At constant T and V, a system minimizes the Helmholtz free energy F = E − TS, not internal energy E alone. An entropy-increasing process (ΔS > 0) can be spontaneous even if it costs energy, because the −TΔS contribution to ΔF can be negative enough to make ΔF < 0 overall. Energy minimization governs only an isolated system at absolute zero, where entropy plays no role. At any finite temperature, entropy competes with energy, and free energy is the correct criterion for equilibrium."

- question: "At the melting point of ice (0°C and 1 atm), the Gibbs free energies of the solid and liquid phases are equal."
  type: true-false
  answer: true
  explanation: "Phase coexistence occurs when both phases have equal Gibbs free energy per particle (equal chemical potential μ). At 0°C and 1 atm, ice and liquid water coexist in thermodynamic equilibrium — meaning G_solid = G_liquid exactly. Below 0°C, G_solid < G_liquid and ice is stable; above 0°C, G_liquid < G_solid and liquid is stable. The melting point is precisely the temperature where these free energies cross, reflecting the competition between the energy cost of melting and the entropy gain of the liquid phase."

- question: "Why does ice melt above 0°C even though melting requires absorbing energy from the surroundings? Explain using free energy."
  type: short-answer
  answer: "Melting costs energy (latent heat is positive, ΔH > 0), but liquid water has much higher entropy than ice — molecules are disordered and mobile rather than locked in a crystal lattice. The Gibbs free energy change is ΔG = ΔH − TΔS. At temperatures above 0°C, TΔS is large enough to outweigh ΔH, making ΔG < 0 and melting spontaneous. Below 0°C, TΔS is insufficient, ΔG > 0, and the ordered crystal phase is stable."
  explanation: "Free energy is the competition between energy and entropy, with temperature as the weighting factor. At low T, energy wins and the crystal is stable. At high T, entropy wins and the disordered liquid is stable. The crossover — the melting point — is exactly where ΔG = 0: the energetic cost of disrupting the crystal is precisely offset by the entropic gain of disordering the molecules. This is why ice and water coexist in equilibrium only at 0°C and not above or below it."
```

## Explainer

From the canonical partition function Z = Σ exp(−βEᵢ), you can compute the average energy ⟨E⟩ = −∂ ln Z/∂β and entropy S = kB ln Z + ⟨E⟩/T. The **Helmholtz free energy** F = ⟨E⟩ − TS is simply the combination that emerges from this: F = −kBT ln Z. This single equation is the bridge between statistical mechanics and thermodynamics — once you have Z, you have F, and from F you can derive essentially every equilibrium thermodynamic property.

Why is F called a "free" energy? The name reflects the competition between energy and entropy. A system at constant temperature and volume spontaneously evolves to minimize F, not to minimize energy alone. An exothermic process (ΔE < 0) is favorable, but so is an entropy-increasing process (ΔS > 0) because −TΔS also lowers F. When these tendencies conflict — say, a process that releases heat but decreases entropy — the question of which wins depends on temperature. At high T, the TΔS term dominates and entropy wins; at low T, energy wins. This is why ice melts above 0°C (entropy gain of liquid water overwhelms the energy cost) and freezes below it.

The **Gibbs free energy** G = F + PV = ⟨E⟩ − TS + PV is the natural potential for constant-pressure, constant-temperature conditions — the conditions of most chemical and biological processes. It is minimized at equilibrium under these constraints. The condition for phase coexistence (the topic of phase equilibrium) is G_liquid = G_solid (equal Gibbs free energies per particle, i.e., equal chemical potentials μ = ∂G/∂N). Maxwell relations follow from the second-order mixed partial derivatives of these potentials. For example, from dF = −SdT − PdV, the Maxwell relation (∂S/∂V)_T = (∂P/∂T)_V connects an entropy derivative (hard to measure directly) to a pressure derivative (easy to measure). These relations are among the most practically useful results in thermodynamics.

For phase transitions, free energies are indispensable. A first-order transition occurs when two phases have equal G but the system discontinuously jumps between two minima — there is a **latent heat** and coexistence. A second-order (continuous) transition occurs when the minimum of the free energy evolves continuously but the shape of the free energy landscape changes qualitatively at Tc — this is exactly the **order parameter** picture you will develop in Landau theory. Free energy as a function of the order parameter, F(M, T), is the Landau free energy, and minimizing it gives the equilibrium order parameter. The entire language of phase transitions is built on free energies, so mastering F and G here is prerequisite to that entire framework.
