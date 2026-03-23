---
id: gas-mixture-thermodynamics-daltons
title: Gas Mixture Thermodynamics and Dalton's Law
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: gas-mixtures-partial-pressures-daltons-law
  type: hard
- id: ideal-real-gas-equations-state
  type: soft
builds-toward:
- partial-molar-properties-mixtures
- humid-air-thermodynamic-properties
- combustion-stoichiometry-energy-release
tags:
- mixtures
- daltons-law
- partial-pressure
- mole-fraction
stage: formal-systems
status: validated
---

# Gas Mixture Thermodynamics and Dalton's Law

## Core Idea
For ideal gases, Dalton's law states total pressure P = Σ P_i (partial pressures), and mole fraction x_i = P_i/P. Mixture properties are molar averages: M_mix = Σ x_i*M_i, R_mix = R_u/M_mix, c_p,mix = Σ x_i*c_p,i. For real gases this becomes complex; mixing rules depend on the equation of state. Combustion, HVAC, and gas separation all rely on mixture thermodynamics.

## Questions

```yaml
- question: "A gas mixture is 21% O₂ and 79% N₂ by mole at sea level (total pressure 100 kPa). A climber ascends to high altitude where total pressure is 60 kPa. What is the mole fraction of O₂ at altitude?"
  type: multiple-choice
  options:
    - "12.6% — because reduced pressure compresses the mole fraction proportionally"
    - "Still 21% — mole fraction is a ratio of amounts, unaffected by total pressure"
    - "35% — O₂ is heavier than N₂ and concentrates at lower pressures"
    - "Cannot be determined without knowing the temperature at altitude"
  answer: 1
  explanation: "Mole fraction x_i = n_i / n_total depends only on the relative amounts of each component, not on the total pressure. The same number of O₂ molecules and N₂ molecules are present in a given parcel of air regardless of altitude — the composition hasn't changed. What does change is the partial pressure of O₂: P_O₂ = 0.21 × 60 kPa = 12.6 kPa, down from 21 kPa at sea level. It is this drop in partial pressure (not mole fraction) that reduces oxygen availability and causes altitude sickness."

- question: "Dry air is 21% O₂ (M = 32 g/mol) and 79% N₂ (M = 28 g/mol) by mole. What is the mixture molecular weight of air?"
  type: multiple-choice
  options:
    - "30 g/mol — the simple average of 32 and 28"
    - "28.84 g/mol — the mole-fraction-weighted average: 0.21×32 + 0.79×28"
    - "32 g/mol — the heavier component dominates the mixture molecular weight"
    - "60 g/mol — molecular weights add for a two-component mixture"
  answer: 1
  explanation: "Mixture molecular weight is M_mix = Σ x_i M_i = 0.21×32 + 0.79×28 = 6.72 + 22.12 = 28.84 g/mol. This is a mole-fraction-weighted average, not a simple average (which would give 30). Because N₂ has a much larger mole fraction (0.79 vs 0.21), the mixture molecular weight is pulled closer to M_N₂ = 28. This value of ~28.84 g/mol gives the familiar specific gas constant for air: R_air = 8314 / 28.84 ≈ 287 J/(kg·K)."

- question: "For an ideal gas mixture, the partial pressure of a component equals the pressure that component would exert if it alone occupied the entire volume at the same temperature."
  type: true-false
  answer: true
  explanation: "This is Dalton's law and follows directly from ideal gas behavior: each component acts independently, with no intermolecular interactions between unlike molecules. If component i alone were in the container at the same T and volume V, it would exert P_i = n_i R_u T / V. Summing over all components gives P_total = n_total R_u T / V, so P_i/P_total = n_i/n_total = x_i. Thus partial pressure, volume fraction, and mole fraction are all identical for ideal gas mixtures."

- question: "As elevation increases, the percentage of oxygen in the air decreases, which is why breathing becomes harder at high altitude."
  type: true-false
  answer: false
  explanation: "The mole fraction of oxygen in dry air is approximately 21% at all elevations — the composition of the atmosphere doesn't change with altitude. What decreases is the total atmospheric pressure, and with it, the partial pressure of oxygen: P_O₂ = 0.21 × P_total. At high altitude, P_total is much lower, so P_O₂ is lower, meaning less oxygen is available per breath. The difficulty breathing is caused by reduced oxygen partial pressure, not reduced oxygen percentage."

- question: "Why does altitude affect a climber's ability to breathe, even though the mole fraction of oxygen in air stays constant at about 21%?"
  type: short-answer
  answer: "Oxygen transport in the body depends on partial pressure, not mole fraction. Hemoglobin in the lungs picks up oxygen based on P_O₂ in the alveoli. At altitude, total atmospheric pressure falls, so P_O₂ = 0.21 × P_total also falls — there are fewer oxygen molecules per breath even though the proportion remains the same. Lower P_O₂ means hemoglobin is less saturated with oxygen after each breath, reducing oxygen delivery to tissues."
  explanation: "This is why the mole fraction vs. partial pressure distinction matters physiologically. A climber at 5,500 m (half sea-level pressure) breathes air that is still 21% O₂, but the partial pressure is only ~10.6 kPa instead of ~21.3 kPa — about half. The hemoglobin-oxygen dissociation curve tells us saturation drops substantially at lower partial pressures, which is the mechanism underlying altitude sickness and acclimatization."
```

## Explainer

Your prerequisite on partial pressures established the central fact about ideal gas mixtures: each component behaves as if it were alone in the container, occupying the full volume at the temperature of the mixture. **Dalton's law** formalizes this as P_total = Σ P_i, where each **partial pressure** P_i = x_i × P_total is the pressure that component i would exert if it alone occupied the volume at the same temperature. The **mole fraction** x_i = n_i/n_total is the key composition variable — it is simultaneously the volume fraction and the partial-pressure fraction for ideal gases.

The mixture properties you need for thermodynamic calculations follow from treating the mixture as a single pure substance with molar-averaged properties. The **mixture molecular weight** M_mix = Σ x_i M_i is a straightforward molar average — heavier components pull it up, lighter ones pull it down. From M_mix you get the specific gas constant R_mix = R_u / M_mix (where R_u = 8.314 J/mol·K is the universal gas constant), which you can plug directly into the ideal gas law PV = m R_mix T to work in mass-based units. Similarly, the **mixture heat capacity** c_p,mix = Σ x_i c_p,i lets you compute enthalpy changes for the mixture just as you would for a pure gas. All of this works because ideal gas components do not interact — mixing them does not change their individual enthalpies, internal energies, or entropies beyond the entropy of mixing (which matters for chemical equilibrium but not for energy balances in most engineering calculations).

A practical example anchors the arithmetic. Dry air is approximately 21% O₂ and 79% N₂ by mole. The mixture molecular weight is M_air = 0.21×32 + 0.79×28 = 6.72 + 22.12 = 28.84 g/mol, giving R_air = 8314/28.84 ≈ 287 J/(kg·K) — the familiar specific gas constant for air. The partial pressure of O₂ at sea level (101.3 kPa) is 0.21 × 101.3 = 21.3 kPa. This is why oxygen partial pressure matters for aviation physiology and why altitude affects combustion — as you climb, P_total falls and with it P_O₂, reducing oxygen availability even though the mole fraction stays the same.

For **real gas mixtures**, the ideal treatment breaks down because intermolecular forces between unlike species differ from forces between like species, producing volume and enthalpy changes on mixing. Real gas equations of state like van der Waals or Peng-Robinson require **mixing rules** for their parameters — empirical or theoretically motivated formulas for the cross-interaction parameters a_ij (attraction) and b_ij (size). These are more involved and depend on the specific gas pair. For engineering work at moderate pressures (combustion products below ~10 bar, HVAC systems at atmospheric conditions), the ideal mixture treatment is accurate to within a few percent and is almost universally used. Real-gas corrections become important in natural gas pipelines at high pressure, supercritical processes, and precision measurements where small departures from ideality matter.
