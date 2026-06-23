---
id: thermochemistry-enthalpy
title: Thermochemistry and Enthalpy
domain: chemistry
course: general-chemistry
prerequisites:
- id: chemical-equations-and-balancing
  type: hard
- id: stoichiometry-calculations
  type: soft
- id: gas-stoichiometry
  type: soft
- id: conservation-of-energy
  type: hard
- id: energy-in-chemical-reactions
  type: soft
builds-toward:
- entropy-and-gibbs-free-energy
- chemical-equilibrium
tags:
- enthalpy
- Hesss-law
- heat-of-formation
- thermochemical-equation
- bond-enthalpy
- exothermic
- endothermic
stage: formal-systems
status: validated
---
# Thermochemistry and Enthalpy

## Core Idea
Thermochemistry studies the heat exchanged in chemical reactions. Enthalpy (H) is a state function; at constant pressure, ΔH equals heat flow: ΔH < 0 for exothermic reactions (heat released) and ΔH > 0 for endothermic. Hess's law states that ΔH for a reaction is path-independent — it equals the sum of ΔH values for any sequence of steps that add up to the overall reaction. Standard enthalpies of formation (ΔHf°) — enthalpy change for forming one mole of a compound from elements in standard state — provide a systematic table-based method: ΔH°rxn = ΣΔHf°(products) − ΣΔHf°(reactants).

## How It's Best Learned
Practice Hess's law by combining given equations algebraically (reversing equations changes sign of ΔH; multiplying changes magnitude proportionally). Use formation enthalpy tables with the products-minus-reactants formula. Connect to calorimetry through q = mcΔT.

## Common Misconceptions
- Enthalpy is not the total energy of a system — it is internal energy plus a PV correction term. At constant pressure, ΔH equals heat, but not at constant volume.
- An exothermic reaction (ΔH < 0) releases heat to the surroundings, making the surroundings feel warm — the system loses energy.

## Questions

```yaml
- question: "Given that A → B has ΔH = +50 kJ/mol and B → C has ΔH = −80 kJ/mol, what is ΔH for the overall reaction A → C?"
  type: multiple-choice
  options: ["+130 kJ/mol", "−130 kJ/mol", "−30 kJ/mol", "+30 kJ/mol"]
  answer: 2
  explanation: "By Hess's Law, ΔH values add when reactions are combined in sequence. A → B → C gives ΔH = (+50) + (−80) = −30 kJ/mol. Because enthalpy is a state function, only the initial state (A) and final state (C) matter — the intermediate (B) and the path taken are irrelevant."

- question: "In an exothermic reaction, the reacting system gains heat and increases in temperature."
  type: true-false
  answer: false
  explanation: "This reverses what actually happens. In an exothermic reaction (ΔH < 0), the system releases heat to the surroundings. It is the surroundings — such as the water in a calorimeter — that increase in temperature. The system loses energy. A common confusion is equating 'the beaker gets hot' with 'the reaction is gaining energy,' when in fact the beaker is the surroundings absorbing the released heat."

- question: "Write the formula for calculating ΔH°rxn from standard enthalpies of formation, and explain why elements in standard state do not appear in the final calculation."
  type: short-answer
  answer: "ΔH°rxn = ΣΔHf°(products) − ΣΔHf°(reactants). Elements in standard state have ΔHf° = 0 by definition, so they cancel out of the sum."
  explanation: "The formula is an application of Hess's Law: you conceptually decompose reactants into their elements (reversing formation reactions, changing signs) and then form products from those elements. The formation enthalpy of an element in its standard state is defined as zero because no reaction is needed to produce it. This cancellation means only compound formation enthalpies contribute to ΔH°rxn."
```

## Explainer

Thermochemistry is the study of how energy flows when chemical reactions occur. The central concept is enthalpy (H), a thermodynamic state function designed to capture heat exchange at constant pressure. You don't need to know the absolute value of H for any substance — what matters is the change, ΔH, between products and reactants. When ΔH < 0, the system releases heat to the surroundings (exothermic — like combustion); when ΔH > 0, it absorbs heat from the surroundings (endothermic — like dissolving ammonium nitrate in water). The sign convention is always from the system's perspective: negative means energy leaves the system.

One key subtlety: enthalpy is not the total energy of a system. Formally, H = U + PV, where U is internal energy and PV is a pressure-volume correction. At constant pressure (most lab reactions open to the atmosphere), ΔH equals q, the heat transferred. This is why you can connect thermochemistry to calorimetry — q = mcΔT gives you the heat absorbed by the surroundings, which equals −ΔH for the reaction. At constant volume (a sealed bomb calorimeter), the situation is different: ΔH ≠ q because there is no PV work. Keeping track of conditions matters.

Hess's Law is the most practically useful tool in this topic: because enthalpy is a state function, ΔH depends only on initial and final states, not on the path. You can combine thermochemical equations algebraically. Reverse a reaction and its ΔH changes sign. Multiply a reaction by a scalar and its ΔH scales by the same factor. Add reactions step by step until they sum to your target reaction, and sum the ΔH values — the result is ΔH for the overall reaction. Hess's Law lets you calculate enthalpies for reactions that are difficult or impossible to measure directly.

Standard enthalpies of formation (ΔHf°) give you a systematic, table-based approach that is essentially Hess's Law pre-packaged. A formation enthalpy is the ΔH for forming one mole of a compound from its constituent elements in standard state. Elements in standard state have ΔHf° = 0 by definition. The formula ΔH°rxn = ΣΔHf°(products) − ΣΔHf°(reactants) works by conceptually decomposing reactants into elements and then assembling products from those elements, with the element steps canceling to zero.

A persistent sign-confusion error: exothermic reactions have negative ΔH, and students sometimes think the system is 'losing energy' in a bad or incomplete sense. Think of it via conservation of energy: the bonds in the products store less chemical energy than the bonds in the reactants, and the difference is released as heat. The system's energy decreases; the surroundings' energy increases by the same amount. Total energy is conserved — fully consistent with the first law of thermodynamics. The negative sign on ΔH is not a deficit; it is a direction indicator showing which way heat flows.
