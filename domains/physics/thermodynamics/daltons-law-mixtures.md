---
id: daltons-law-mixtures
title: Dalton's Law of Partial Pressures
domain: physics
course: thermodynamics
prerequisites:
- id: ideal-gas-law
  type: hard
tags:
- gas-mixtures
- partial-pressure
- ideal-gas
stage: formal-systems
status: draft
---

# Dalton's Law of Partial Pressures

## Core Idea
Dalton's law states that the total pressure exerted by a mixture of ideal gases equals the sum of the partial pressures each gas would exert if it occupied the volume alone. This implies gases in a mixture behave independently and each obeys the ideal gas law with its own mole fraction.

## Questions

```yaml
- question: "A container holds 0.5 mol N₂ and 0.5 mol O₂ at a total pressure of 100 kPa. What is the partial pressure of N₂?"
  type: multiple-choice
  options:
    - "100 kPa — N₂ is the primary gas so it accounts for all the pressure"
    - "50 kPa — N₂'s mole fraction is 0.5, so its partial pressure is 0.5 × 100 kPa"
    - "25 kPa — the total pressure is split by molecular weight, not mole fraction"
    - "75 kPa — O₂ is heavier and contributes less, so N₂ contributes more"
  answer: 1
  explanation: "Partial pressure equals mole fraction times total pressure: Pₙ₂ = xₙ₂ × P_total = 0.5 × 100 = 50 kPa. The mole fraction (ratio of moles of one species to total moles) is the correct weighting factor — molecular weight does not enter into it. This follows directly from the ideal gas law applied to each species independently: Pᵢ = nᵢRT/V."

- question: "You replace 0.5 mol O₂ in a sealed container with 0.5 mol CO₂, keeping temperature and volume constant. How does the total pressure change?"
  type: multiple-choice
  options:
    - "It increases — CO₂ molecules are heavier, so they exert more pressure"
    - "It decreases — CO₂ and O₂ interact, reducing the partial pressures"
    - "It stays the same — total pressure depends only on total moles, T, and V, not on which gases are present"
    - "It increases slightly — adding a polyatomic gas always raises pressure"
  answer: 2
  explanation: "From P_total = n_total·RT/V, pressure depends on total moles, temperature, and volume — not on the identity of the gas molecules, as long as they behave ideally. Swapping 0.5 mol O₂ for 0.5 mol CO₂ leaves n_total unchanged, so P_total is unchanged. This is a direct consequence of molecular independence: each mole of ideal gas contributes identically to total pressure regardless of species."

- question: "The partial pressure of a gas in a mixture equals the pressure it would exert if it alone occupied the same volume at the same temperature."
  type: true-false
  answer: true
  explanation: "This is the definition of partial pressure: Pᵢ = nᵢRT/V. It is the pressure species i would exert in the container all by itself. Dalton's law then says total pressure is the sum of all such partial pressures — which follows because ideal gas molecules are completely indifferent to the presence of other species."

- question: "Two gases that react chemically with each other can still be analyzed using Dalton's law of partial pressures, as long as both gases are ideal."
  type: true-false
  answer: false
  explanation: "Dalton's law requires that the gases do not react. If they react, the mixture composition changes over time and you no longer have the original species at independent partial pressures — the chemical transformation alters the number of moles of each component. The assumption of molecular independence (the basis of Dalton's law) applies to non-reacting mixtures; ideal-gas behavior alone is not sufficient."

- question: "Why does the presence of one ideal gas have no effect on the pressure exerted by another ideal gas in the same container?"
  type: short-answer
  answer: "Ideal gas molecules are modeled as point particles with no intermolecular forces — they interact only through elastic collisions. Because molecules of gas A exert no attractive or repulsive forces on molecules of gas B, each species contributes to wall pressure exactly as if the other were absent. The pressure from each species depends only on its own mole count, temperature, and volume."
  explanation: "This molecular independence is the microscopic justification for Dalton's law. When intermolecular forces become significant (high pressure, polar gases), this independence breaks down and Dalton's law fails — real gas equations of state are needed instead."
```

## Explainer

From your study of the ideal gas law, you know that for a single pure gas: PV = nRT, where n is the number of moles. Pressure arises from the collective momentum transfer of gas molecules colliding with container walls. In an ideal gas, molecules are treated as point particles with no intermolecular forces — they interact only through elastic collisions. This last assumption is the key to understanding what happens when you mix two ideal gases in the same container.

Because ideal gas molecules have no intermolecular forces, the molecules of gas A are completely unaffected by the presence of molecules of gas B. Each species bounces around and hits the walls exactly as if the other species weren't there. The pressure contribution from species A depends only on how many A molecules there are and how fast they're moving — the B molecules are invisible to them. This independence is the molecular justification for Dalton's law: the total pressure is just the sum of contributions from each species, as if each were alone.

The **partial pressure** of species i is defined as Pᵢ = nᵢRT/V — the pressure that species i would exert alone in the same volume at the same temperature. Since P_total = ΣPᵢ = (Σnᵢ)RT/V = n_total·RT/V, the total pressure satisfies the ideal gas law with the total number of moles. The **mole fraction** xᵢ = nᵢ/n_total allows a clean rewrite: Pᵢ = xᵢ · P_total. For example, dry air is approximately 78% nitrogen and 21% oxygen by mole fraction. At atmospheric pressure (101.3 kPa), the partial pressure of N₂ is about 79 kPa and O₂ is about 21 kPa. These partial pressures are directly relevant to physiology — it is the partial pressure of O₂ in the alveoli that drives oxygen into the blood, not the total atmospheric pressure.

Dalton's law simplifies many practical calculations. When collecting a gas over water (a common lab technique), the collected gas is saturated with water vapor. The total pressure is P_gas + P_water vapor. Knowing the saturation vapor pressure at the collection temperature (from tables), you subtract it to find the partial pressure of the collected gas, then use PV = nRT to find the moles. Similarly, in respiratory physiology, scuba diving, and industrial gas handling, tracking partial pressures is essential — oxygen toxicity and nitrogen narcosis are partial-pressure effects, independent of whether other gases are present.

Dalton's law fails when the ideal gas approximation breaks down: at high pressures where molecular volumes and intermolecular attractions become significant, or when the gases react chemically. At high pressure, the molecules of different species do interact — through van der Waals forces or steric repulsion — and the partial pressures no longer add independently. Real gas equations of state (van der Waals, Peng-Robinson) introduce correction terms that capture these deviations. Dalton's law also cannot apply to gases that react, since the resulting mixture is chemically different from the components. But for ideal or nearly-ideal gases at moderate conditions, it is exact and extremely useful.


