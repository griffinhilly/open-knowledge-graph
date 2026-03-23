---
id: solution-concentration
title: Solution Concentration
domain: chemistry
course: general-chemistry
prerequisites:
- id: stoichiometry-calculations
  type: hard
- id: mole-concept
  type: hard
- id: intermolecular-forces
  type: soft
builds-toward:
- colligative-properties
- acid-base-chemistry
- ph-and-acid-base-calculations
tags:
- molarity
- molality
- dilution
- solubility
- percent-composition
- solution
stage: formal-systems
status: validated
---
# Solution Concentration

## Core Idea
Concentration describes the amount of solute dissolved per unit of solution or solvent. Molarity (M = mol solute / L solution) is the most common laboratory unit. Molality (m = mol solute / kg solvent) is temperature-independent and used for colligative property calculations. Dilution decreases concentration while conserving moles of solute: M₁V₁ = M₂V₂. Understanding concentration is prerequisite to virtually all solution-phase chemistry, from reaction stoichiometry to equilibrium to acid-base calculations.

## How It's Best Learned
Practice preparing solutions by calculation and mentally distinguishing solution volume (for molarity) from solvent mass (for molality). Work dilution problems both algebraically and conceptually. Connect solution concentration to reaction stoichiometry through aqueous titration calculations.

## Common Misconceptions
- Molarity is defined in terms of solution volume, not solvent volume — adding solute changes the total volume of the solution.
- 'Concentrated' is qualitative; two solutions can both be 'concentrated' but have different molarities. Always specify units when precision is required.

## Questions

```yaml
- question: "To prepare a 1.0 M NaCl solution, you dissolve 1 mol of NaCl in which of the following?"
  type: multiple-choice
  options:
    - "Exactly 1.0 L of water"
    - "Exactly 1.0 kg of water"
    - "Enough water so that the total volume of solution equals 1.0 L"
    - "Any amount of water, then adjust pH to 7"
  answer: 2
  explanation: "Molarity is defined as moles of solute per liter of *solution*, not per liter of solvent. You dissolve the solute, then add solvent until the total solution volume reaches 1.0 L. Adding 1 mol to 1.0 L of water would give slightly more than 1.0 L of solution, yielding a molarity slightly less than 1.0 M."

- question: "Molality is preferred over molarity for colligative property calculations because molality does not change when temperature changes."
  type: true-false
  answer: true
  explanation: "Molality is defined as moles of solute per kilogram of *solvent* (a mass). Mass does not change with temperature. Molarity uses solution *volume*, which expands or contracts as temperature changes, so the same solution has a slightly different molarity at different temperatures. For colligative properties, which depend only on the ratio of solute to solvent particles, molality is the temperature-independent choice."

- question: "A student dilutes 25.0 mL of a 4.0 M HCl solution to a total volume of 100.0 mL. What is the concentration of the diluted solution?"
  type: short-answer
  answer: "1.0 M"
  explanation: "Dilution conserves moles of solute: M₁V₁ = M₂V₂. Substituting: (4.0 M)(25.0 mL) = M₂(100.0 mL), so M₂ = 100/100 = 1.0 M. The moles of HCl have not changed — they are now spread through a four-times-larger volume."
```

## Explainer

You already know how to count atoms and molecules using moles, and how to balance and scale chemical reactions through stoichiometry. Solution concentration is the bridge between those abstract mole calculations and the actual quantities you measure in a lab. When a reaction happens in solution, you cannot weigh out the reactants directly — you measure volumes of liquid. Concentration is what lets you convert between "mL of solution dispensed" and "moles of reactant delivered."

The most important unit is molarity (M): moles of solute divided by liters of *solution*. The critical word is solution — the total volume after dissolving, not the volume of solvent you started with. If you dissolve 58.4 g of NaCl (1 mol) in water and dilute to a final volume of 1.00 L, you have a 1.00 M solution. If you added it to 1.00 L of water and the final volume became 1.002 L, you would actually have a 0.998 M solution. In practice, the difference is tiny, but the principle matters: always make up to volume, not add to volume.

Molality (m) is an alternative unit — moles of solute per kilogram of *solvent* (not solution). Because it uses mass rather than volume, it is unaffected by temperature. A 1.0 m NaCl solution measured at 25 °C is still exactly 1.0 m at 50 °C, even though its volume (and therefore its molarity) has slightly changed. This makes molality the correct unit for colligative property calculations, where the relevant quantity is the ratio of solute particles to solvent particles.

Dilution is the most common lab operation, and it has a beautifully simple conservation law: moles of solute are the same before and after. Since moles = M × V, dilution obeys M₁V₁ = M₂V₂. If you take 25 mL of a 4.0 M stock solution and add water to reach 100 mL, you have not created or destroyed any HCl molecules — you have just spread the same moles through a larger volume. This equation works in any consistent volume unit, as long as both volumes use the same unit.

Finally, avoid confusing "concentrated" (a qualitative description meaning relatively high solute amount) with a specific molarity. Concentrated sulfuric acid is about 18 M; concentrated HCl is about 12 M. These are chemically very different concentrations, both casually called "concentrated." In quantitative work, always state the molarity explicitly.


