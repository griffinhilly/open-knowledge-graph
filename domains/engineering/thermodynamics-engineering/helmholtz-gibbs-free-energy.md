---
id: helmholtz-gibbs-free-energy
title: 'Helmholtz and Gibbs Free Energy: Maximum Work'
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: legendre-transformations-thermodynamics
  type: hard
- id: second-law-thermodynamics-entropy
  type: hard
builds-toward:
- chemical-equilibrium-reaction-analysis
tags:
- helmholtz
- gibbs
- free-energy
- available-work
- spontaneity
stage: formal-systems
status: validated
---

# Helmholtz and Gibbs Free Energy: Maximum Work

## Core Idea
Helmholtz free energy A = U - TS represents maximum useful work for systems at constant T and V; Gibbs free energy G = H - TS for constant T and P. Both decrease for spontaneous processes; equilibrium occurs at minimum G or A. Negative ΔG indicates spontaneous reaction; ΔG° = -RT ln(K_p) relates standard state free energy to the equilibrium constant.

## Questions

```yaml
- question: "A reaction has ΔG° = +20 kJ/mol at 298 K. Which statement is most accurate?"
  type: multiple-choice
  options:
    - "The reaction is thermodynamically impossible and will never proceed in the forward direction under any conditions"
    - "At standard conditions the reverse reaction is spontaneous, but the forward reaction can still proceed spontaneously if the reaction quotient Q is less than K_eq"
    - "The system is at equilibrium under standard conditions because ΔG° represents the equilibrium free energy"
    - "The reaction is spontaneous because the positive sign indicates energy is being released to the system"
  answer: 1
  explanation: "ΔG° is the free energy change at standard conditions (all species at 1 bar, 298 K). A positive ΔG° means the reverse reaction is spontaneous from standard state, and K_eq < 1. But ΔG = ΔG° + RT ln(Q) — if Q < K_eq (e.g., starting with pure reactants and no products), ΔG can be negative even when ΔG° is positive, and the reaction proceeds forward. ΔG° governs the equilibrium position; actual spontaneity at non-standard conditions depends on both ΔG° and Q."

- question: "An engineer analyzes an isothermal process occurring inside a sealed rigid vessel (constant T and V). Which thermodynamic potential determines the maximum work available from this process?"
  type: multiple-choice
  options:
    - "Gibbs free energy G = H − TS, because it applies to all isothermal processes regardless of volume constraint"
    - "Helmholtz free energy A = U − TS, because constant temperature and volume is the natural domain of A, and −ΔA equals maximum work"
    - "Enthalpy H, because the process occurs at constant pressure inside the rigid container"
    - "Either A or G can be used interchangeably at constant temperature"
  answer: 1
  explanation: "The choice of free energy depends on the constraints. At constant T and V, Helmholtz free energy A is the correct potential: dA ≤ 0 for spontaneous processes, and −ΔA gives the maximum useful work extractable. At constant T and P (the more common engineering case), Gibbs free energy G applies and −ΔG gives maximum non-PV work. Using G for a constant-volume process introduces a PV term that doesn't correspond to any physical work in the system."

- question: "At equilibrium, ΔG = 0, not ΔG < 0; a negative ΔG indicates that the system has not yet reached equilibrium and will spontaneously move toward it."
  type: true-false
  answer: true
  explanation: "ΔG = 0 is the condition for equilibrium at constant T and P — the system has minimized its Gibbs free energy. ΔG < 0 means the system can still lower its free energy by converting more reactants to products, so the forward reaction proceeds spontaneously. ΔG > 0 means the reverse is spontaneous. The common error is thinking 'spontaneous' and 'at equilibrium' are synonymous — they are not. Equilibrium is the state toward which spontaneous processes drive the system."

- question: "A reaction with ΔG < 0 will proceed to completion, consuming all reactants and converting them entirely to products."
  type: true-false
  answer: false
  explanation: "ΔG < 0 (at standard conditions, ΔG°) means products are favored at equilibrium — K_eq > 1. But this does not mean complete conversion. The reaction proceeds until ΔG = 0 (equilibrium), at which point both reactants and products are present. How far it goes depends on the magnitude of K_eq: a very large K means nearly complete conversion, but true completion (K → ∞) is only asymptotically approached. ΔG < 0 indicates direction and tendency, not completion."

- question: "Why can Gibbs free energy determine whether a process is spontaneous without explicitly tracking the entropy change of the surroundings?"
  type: short-answer
  answer: "For a process at constant T and P, the heat exchanged with the surroundings equals the enthalpy change: q_p = ΔH. This heat transfer changes the surroundings' entropy by ΔS_surr = −ΔH/T. The second law requires ΔS_total = ΔS_sys + ΔS_surr ≥ 0, which becomes ΔS_sys − ΔH/T ≥ 0, or equivalently ΔH − TΔS_sys ≤ 0. Defining G = H − TS, this is just ΔG ≤ 0. Gibbs free energy bundles both the system's entropy gain and the surroundings' entropy cost into a single system-property quantity, so you only need to track the system."
  explanation: "This is the practical power of free energy: it converts the second law from a statement about the entire universe into a criterion applied only to the system. No explicit accounting of the surroundings is required — their contribution is embedded in the enthalpy term ΔH."
```

## Explainer

You already know from the second law and entropy that spontaneous processes increase total entropy (system plus surroundings), and from Legendre transformations that you can recast thermodynamic relations by switching independent variables. The free energies bring both ideas together in a remarkably practical form: they tell you whether a process will happen spontaneously **without** explicitly tracking the entropy of the surroundings.

The argument is as follows. For a system at constant temperature in contact with a heat reservoir, the Clausius inequality gives dS_total = dS_system + dS_surroundings ≥ 0. The surroundings exchange heat reversibly, so dS_surroundings = −dQ_system/T. Substituting and rearranging: dU − T·dS ≤ 0 at constant T and V (no boundary work). Define **Helmholtz free energy** A = U − TS. Then dA ≤ 0 at constant T and V — the Helmholtz free energy can only decrease or stay constant. It reaches its minimum at equilibrium. A is also equal to the maximum work a system can do in an isothermal, constant-volume process: W_max = −ΔA. The "free" energy is literally the energy free to do work after entropy costs are paid to the environment.

Most engineering systems operate at constant temperature and pressure, not constant volume. For these, the relevant potential is **Gibbs free energy** G = H − TS = U + PV − TS. By the same argument, dG ≤ 0 at constant T and P — G is minimized at equilibrium. This is why G is the central quantity in chemistry and chemical engineering: reactions in open vessels at atmospheric pressure happen at constant T and P. ΔG < 0 means spontaneous; ΔG > 0 means the reverse reaction is spontaneous; ΔG = 0 means equilibrium.

The quantitative link to equilibrium constants comes from the standard-state relation **ΔG° = −RT ln(K_p)**. The standard free energy change ΔG° measures the free energy difference when all reactants and products are at standard conditions (1 bar, 298 K). K_p is the equilibrium constant in terms of partial pressures. If ΔG° is large and negative, K_p ≫ 1 — products are strongly favored at equilibrium. If ΔG° is large and positive, K_p ≪ 1 — reactants dominate. A system not at equilibrium has ΔG = ΔG° + RT ln(Q), where Q is the reaction quotient; the system moves spontaneously in whichever direction reduces G until Q = K_p and ΔG = 0. This framework transforms the second law from a qualitative principle ("entropy increases") into a quantitative engineering tool for predicting reaction extents, phase boundaries, and material stability.
