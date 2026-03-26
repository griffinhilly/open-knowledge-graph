---
id: electrochemistry-nernst-equation
title: Electrochemistry and the Nernst Equation
domain: chemistry
course: physical-chemistry
prerequisites:
- id: electrochemistry-basics
  type: hard
- id: thermochemistry-enthalpy
  type: soft
tags:
- electrochemistry
- nernst
- potential
- cell
stage: formal-systems
status: validated
---

# Electrochemistry and the Nernst Equation

## Core Idea
The Nernst equation E = E° - (RT/nF) ln(Q) relates electrochemical cell potential to the reaction quotient Q, showing how electrode potential varies with concentration. Standard cell potentials (E°) are linked to Gibbs free energy through ΔG° = -nFE°, connecting electrochemistry to thermodynamics. At equilibrium (E = 0), the equation determines the equilibrium constant. The Nernst equation explains how battery voltage drops under load and how pH affects redox potentials.

## Questions

```yaml
- question: "A galvanic cell starts with all reactants and products at standard conditions (E = E°). As the cell operates, products accumulate and reactant concentrations fall. What happens to the measured cell potential?"
  type: multiple-choice
  options:
    - "The cell potential increases, because the products are driving the reaction forward more strongly"
    - "The cell potential stays the same until equilibrium, then suddenly drops to zero"
    - "The cell potential decreases continuously as Q increases, approaching zero as the cell reaches equilibrium"
    - "The cell potential oscillates because the Nernst equation contains a logarithm, which alternates sign as Q passes through 1"
  answer: 2
  explanation: "As the cell operates, products accumulate and reactants are consumed, so the reaction quotient Q increases. In the Nernst equation E = E° − (RT/nF) ln Q, a rising Q means the ln Q term grows more positive, and E falls. This continuous decrease reflects the diminishing thermodynamic driving force as the system approaches equilibrium. At equilibrium, Q = K and E = 0 — the cell can no longer do electrical work. Option A inverts the logic; more products means less driving force, not more. The drop to zero is gradual, not sudden (option B)."

- question: "For a cell reaction with n = 2 and E° = +0.50 V at 25°C, what is the relationship between E° and the equilibrium constant K?"
  type: multiple-choice
  options:
    - "K cannot be determined from E° alone; the reaction quotient Q is also needed"
    - "E° = (RT/nF) ln K, so K = exp(nFE°/RT) ≈ 10^(nE°/0.05916) ≈ 10^17, strongly favoring products"
    - "E° = ΔG°/nF, so K = E° × nF, which has units of joules per mole"
    - "K = 1/E° for standard conditions, so a higher voltage means a smaller equilibrium constant"
  answer: 1
  explanation: "At equilibrium, E = 0 and Q = K. Setting E = 0 in the Nernst equation gives 0 = E° − (RT/nF) ln K, which rearranges to E° = (RT/nF) ln K. For E° = +0.50 V and n = 2 at 25°C: ln K = nFE°/RT = 2 × 0.50/0.02569 ≈ 38.9, so K ≈ e^38.9 ≈ 10^16–17. A positive E° corresponds to K > 1; the larger E°, the more overwhelmingly products are favored. This connection between measured voltage and equilibrium thermodynamics — bridging electrochemistry and the ΔG = ΔG° + RT ln Q framework — is the deepest insight of the Nernst equation."

- question: "A standard cell potential E° > 0 implies that the equilibrium constant K > 1 for the cell reaction, meaning products are thermodynamically favored at equilibrium."
  type: true-false
  answer: true
  explanation: "From E° = (RT/nF) ln K, a positive E° requires ln K > 0, which means K > 1. This is also consistent with ΔG° = −nFE°: a positive E° gives a negative ΔG°, which means the reaction is spontaneous under standard conditions and products are favored at equilibrium. The quantitative connection (E° ≈ 0.05916/n × log K at 25°C) shows that even a modest positive E°, say 0.3 V with n = 1, gives K ≈ 10^5. Electrochemistry and thermodynamics are not separate frameworks — they are the same framework expressed in different units."

- question: "The Nernst equation mainly applies to cells operating at non-standard concentrations; under standard conditions (most activities = 1), a separate equation is expected to be used."
  type: true-false
  answer: false
  explanation: "The Nernst equation is universally valid. Under standard conditions, all activities equal 1, so Q = 1 and ln Q = 0. The Nernst equation then reduces to E = E° − 0 = E°. Standard conditions are simply a special case, not a separate regime requiring a different equation. This is analogous to ΔG = ΔG° + RT ln Q: when Q = 1, ΔG = ΔG°. The Nernst equation is the most general statement; standard conditions are the simplification you use when concentrations happen to be 1 M."

- question: "A battery is observed to have a lower voltage than its nominal (standard) rated potential after extended use. Use the Nernst equation to explain mechanistically why this occurs."
  type: short-answer
  answer: "As a battery discharges, the cell reaction consumes reactants and produces products, continuously increasing the reaction quotient Q. In the Nernst equation E = E° − (RT/nF) ln Q, a larger Q increases the subtracted term, directly reducing E. The cell potential thus falls progressively from E° toward zero as Q rises toward the equilibrium constant K. When E = 0, Q = K and the battery is exhausted — it can no longer drive current because there is no thermodynamic driving force remaining. The battery is not 'broken'; it has simply reached chemical equilibrium."
  explanation: "This mechanistic explanation unifies the everyday observation (batteries run down) with the thermodynamic framework (cells approach equilibrium). It also explains why rechargeable batteries work: forcing current through the cell in reverse drives Q back below K, restoring reactant concentrations and rebuilding the voltage. The same logic explains concentration cells — two identical electrodes in solutions of different concentration generate voltage purely from the Q imbalance, with no net chemical reaction."
```

## Explainer

From electrochemistry basics, you know that a galvanic cell generates voltage by separating oxidation and reduction into two half-cells, and that standard reduction potentials (E°) measured under standard conditions (1 M, 1 atm, 25°C) let you predict which direction electrons flow. But real cells rarely operate at standard conditions — concentrations change as the cell discharges, temperatures vary, and pH shifts. The **Nernst equation** tells you the actual cell potential under any set of conditions.

The equation is E = E° − (RT/nF) ln Q, where R is the gas constant, T is absolute temperature, n is the number of electrons transferred, F is Faraday's constant (96,485 C/mol), and Q is the **reaction quotient** — the same ratio of product to reactant activities you use in equilibrium thermodynamics. At 25°C, the prefactor RT/F simplifies to 0.02569 V, giving the common form E = E° − (0.02569/n) ln Q, or equivalently E = E° − (0.05916/n) log Q when using base-10 logarithms. The equation says that as products accumulate (Q increases), the driving force for the reaction decreases and the cell potential drops — exactly what you observe as a battery discharges.

The deep connection here is thermodynamic: the Nernst equation is really just **ΔG = ΔG° + RT ln Q** rewritten in electrical terms, using the relationship ΔG = −nFE. At standard conditions (Q = 1), E equals E° and ΔG equals ΔG°. At equilibrium (Q = K), E = 0 and ΔG = 0, which gives the powerful result E° = (RT/nF) ln K — the standard cell potential directly determines the equilibrium constant. A cell with E° = +0.50 V and n = 2 has K ≈ 10¹⁷, meaning the reaction overwhelmingly favors products. This bridges the gap between the voltage you measure with a multimeter and the thermodynamic favorability of the underlying chemistry.

A particularly important application is pH-dependent electrochemistry. Many half-reactions involve H⁺ ions, so their potentials shift with pH. The hydrogen electrode potential, for instance, changes by −0.05916 V per unit increase in pH at 25°C. This is the basis of pH meters — they are simply electrochemical cells whose voltage varies linearly with hydrogen ion concentration. The Nernst equation also explains concentration cells, where two identical electrodes dipped in solutions of different concentration generate a voltage purely from the concentration difference, with no net chemical change at standard conditions.
