---
id: thermochemistry-heat-and-energy
title: 'Thermochemistry: Enthalpy and Heat of Reaction'
domain: chemistry
course: general-chemistry
prerequisites:
- id: states-of-matter-phase-changes
  type: soft
- id: energy-conservation
  type: soft
builds-toward:
- oxidation-reduction-reactions
tags:
- thermochemistry
- enthalpy
- exothermic
- endothermic
- heat
stage: formal-systems
status: validated
---

# Thermochemistry: Enthalpy and Heat of Reaction

## Core Idea
Thermochemistry studies heat changes during chemical reactions. Enthalpy (H) is the heat content at constant pressure. Exothermic reactions release heat (ΔH < 0); endothermic reactions absorb heat (ΔH > 0). Standard enthalpy of reaction (ΔH°rxn) quantifies heat released or absorbed. Hess's law allows calculation of reaction enthalpies from other reactions.

## Questions

```yaml
- question: "When ammonium nitrate dissolves in water, the solution becomes noticeably cold. What does this tell you about the enthalpy change, and what is happening energetically?"
  type: multiple-choice
  options:
    - "ΔH < 0 — the reaction is exothermic and releases heat, cooling the surroundings"
    - "ΔH > 0 — the reaction is endothermic and absorbs heat from the surroundings, making them feel cold"
    - "ΔH = 0 — the temperature change is a physical change, not a chemical one, so enthalpy is unchanged"
    - "ΔH < 0 — the solution cools because dissolved ions have less energy than solid ammonium nitrate"
  answer: 1
  explanation: "When the solution gets cold, it is losing heat to the reaction — the reaction is absorbing thermal energy from the surroundings. From the system's perspective (the dissolving process), energy flows in, so ΔH > 0 (endothermic). This is the basis of instant cold packs. Option A is the classic reversal error: exothermic reactions release heat and warm the surroundings, not cool them. The sign convention is always from the system's viewpoint: positive ΔH means the system absorbed energy, leaving the surroundings cooler."

- question: "You want ΔH for: C(s) + O₂(g) → CO₂(g). You have: (1) C(s) + ½O₂(g) → CO(g), ΔH₁ = −110 kJ; (2) CO(g) + ½O₂(g) → CO₂(g), ΔH₂ = −283 kJ. What is ΔH for the target reaction?"
  type: multiple-choice
  options:
    - "−173 kJ (ΔH₂ − ΔH₁)"
    - "−393 kJ (ΔH₁ + ΔH₂)"
    - "+393 kJ (reversing the sum)"
    - "−283 kJ (only the final step matters)"
  answer: 1
  explanation: "Adding reactions (1) and (2) gives: C(s) + ½O₂ + CO(g) + ½O₂ → CO(g) + CO₂(g). The CO(g) cancels, leaving C(s) + O₂(g) → CO₂(g) — exactly the target. Because enthalpy is a state function, ΔH adds: −110 + (−283) = −393 kJ. This is Hess's Law in action: the path doesn't matter, only the initial and final states. Option A is the subtraction error; option D ignores the first step entirely."

- question: "Enthalpy is a state function, meaning the value of ΔH for a reaction is the same whether it occurs in one step or through a series of intermediate reactions."
  type: true-false
  answer: true
  explanation: "This is precisely what makes Hess's Law work. Because enthalpy depends only on the current state of the system (pressure, temperature, composition) and not on how the system arrived at that state, ΔH between two states is path-independent. Whether combustion of carbon proceeds directly to CO₂ or goes through CO first, the total enthalpy change is the same. This allows chemists to calculate ΔH for reactions that are too slow, dangerous, or complex to measure directly."

- question: "A reaction with ΔH = −500 kJ will necessarily proceed faster than a reaction with ΔH = −50 kJ."
  type: true-false
  answer: false
  explanation: "Enthalpy change (ΔH) describes thermodynamics — the difference in energy between products and reactants — not kinetics (how fast the reaction proceeds). Reaction rate is determined by the activation energy (the energy barrier between reactants and the transition state), not by ΔH. Many reactions with very large negative ΔH are extremely slow at room temperature (e.g., iron rusting, wood spontaneously combusting in air). A catalyst speeds up a reaction without changing ΔH. Thermodynamics and kinetics are independent."

- question: "Explain the difference between heat and temperature, and describe how a calorimetry experiment uses q = mcΔT to measure the enthalpy change of a reaction."
  type: short-answer
  answer: "Heat (q) is energy transferred between objects due to a temperature difference, measured in joules. Temperature is the average kinetic energy of particles in an object, measured in °C or K. In calorimetry, a reaction occurs in a known mass (m) of water or solution with known specific heat capacity (c). The temperature change (ΔT) of the water is measured. q = mcΔT gives the heat absorbed or released by the water, which equals (with sign reversed) the heat released or absorbed by the reaction. This connects the abstract concept of ΔH to a measurable physical change."
  explanation: "The key distinction is that heat is a process (energy in transit) while temperature is a property (a state of matter). A large swimming pool at 20°C contains far more thermal energy than a cup of boiling water, but the cup is at higher temperature. Calorimetry exploits q = mcΔT to make ΔH measurable: the reaction transfers heat to or from the calorimeter, and we observe the temperature change that results. The water acts as a thermometric gauge — its temperature change is the observable proxy for the invisible enthalpy change of the chemical reaction."
```

## Explainer

From your study of energy conservation, you know that energy is neither created nor destroyed — it only changes form. In chemistry, the form we care about most is **heat**, the energy transferred between a system and its surroundings due to a temperature difference. Thermochemistry puts numbers on that transfer. When methane burns in your stove, the reaction CH₄ + 2O₂ → CO₂ + 2H₂O releases 890 kJ of heat per mole of methane. That number — the **enthalpy of reaction** (ΔH°rxn) — is negative because the system loses energy to the surroundings. The surroundings (your pot of water) get hotter; the reaction is **exothermic**.

**Enthalpy** (H) is defined as the heat content of a system at constant pressure, which is the condition for most bench-top and biological reactions. We never measure H directly — we measure changes in it. When ΔH is negative, products sit at a lower energy than reactants and the difference escapes as heat. When ΔH is positive, the reaction is **endothermic**: it absorbs heat from the surroundings, and dissolving ammonium nitrate in water (the basis of instant cold packs) is a familiar example. The sign convention is critical — ΔH is always stated from the system's perspective: negative means the system released energy, positive means it absorbed energy.

The most powerful tool in thermochemistry is **Hess's law**: because enthalpy is a state function, ΔH for a reaction depends only on the initial and final states, not on the path taken between them. This means you can calculate the enthalpy of a reaction you cannot easily measure by combining reactions whose enthalpies you do know. If you can add, reverse, or scale chemical equations so they sum to your target reaction, the corresponding ΔH values add, reverse sign, or scale in exactly the same way. Standard enthalpies of formation (ΔH°f) exploit this principle systematically: every compound's formation enthalpy is measured relative to its constituent elements in their standard states, so ΔH°rxn = Σ ΔH°f(products) − Σ ΔH°f(reactants). This single equation lets you calculate the heat of any reaction from tabulated formation data.

Understanding thermochemistry also requires distinguishing between heat and temperature. Heat (q) is energy in transit, measured in joules or kilojoules. Temperature is a measure of the average kinetic energy of particles. The relationship between them is q = mcΔT, where m is mass, c is specific heat capacity, and ΔT is the temperature change. Calorimetry experiments use this equation to measure q for a reaction by observing the temperature change in a known mass of water or solution. This is the experimental bridge between the abstract concept of enthalpy and the physical observation of temperature change in the lab.
