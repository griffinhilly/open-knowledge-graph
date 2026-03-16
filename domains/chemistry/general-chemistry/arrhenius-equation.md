---
id: arrhenius-equation
title: The Arrhenius Equation and Activation Energy
domain: chemistry
course: general-chemistry
prerequisites:
- id: exponential-functions-and-graphs
  type: soft
- id: logarithms-intro
  type: soft
- id: natural-logarithm-and-e
  type: soft
tags:
- activation-energy
- frequency-factor
- temperature-dependence
- catalyst
- transition-state
- collision-theory
stage: formal-systems
status: validated
---

# The Arrhenius Equation and Activation Energy

## Core Idea
The Arrhenius equation k = Ae^(−Ea/RT) quantifies how the rate constant k depends on temperature T and activation energy Ea — the minimum energy required for a productive collision. Higher activation energy means fewer molecules have sufficient energy to react, producing a smaller k and slower reaction. Catalysts increase reaction rate by providing an alternative mechanism with lower activation energy, without being consumed. Taking the natural log gives ln k = ln A − Ea/RT, a linear equation used to determine Ea from rate constants measured at two or more temperatures.

## How It's Best Learned
Plot ln k vs. 1/T for experimental data and extract activation energy from the slope (−Ea/R). Use the two-temperature Arrhenius equation to calculate how much a rate changes with a 10°C increase. Connect to collision theory: molecules need both sufficient energy (activation energy) and correct orientation (frequency factor A) to react.

## Common Misconceptions
- Catalysts lower activation energy and thus change k and the reaction rate, but do not change ΔG, ΔH, or the equilibrium constant K — they affect kinetics, not thermodynamics.
- The rule that reaction rate doubles for every 10°C increase is a rough approximation; the actual factor depends on activation energy and the temperature range in question.

## Questions

```yaml
- question: "Two reactions have the same frequency factor A. Reaction X has Ea = 40 kJ/mol; Reaction Y has Ea = 80 kJ/mol. At the same temperature, which reaction is faster and why?"
  type: multiple-choice
  options:
    - "Reaction X, because lower activation energy means a greater fraction of collisions have sufficient energy to react"
    - "Reaction Y, because higher activation energy means the transition state releases more energy when products form"
    - "Reaction X, because the frequency factor dominates and A is the same for both"
    - "Reaction Y, because more energy input means more molecules are activated per unit time"
  answer: 0
  explanation: "In the Arrhenius equation k = Ae^(-Ea/RT), a larger Ea makes the exponent more negative, which makes e^(-Ea/RT) smaller and therefore k smaller. Physically, the Boltzmann factor e^(-Ea/RT) represents the fraction of molecular collisions with enough energy to overcome the activation barrier — lower Ea means a larger fraction clears the bar. With equal A, Reaction X has a larger k and is faster."

- question: "Adding a catalyst to a reaction increases the rate by raising the temperature of the reaction mixture, which increases the average kinetic energy of the molecules."
  type: true-false
  answer: false
  explanation: "Catalysts do not raise the temperature of a reaction. They provide an alternative reaction pathway with a lower activation energy Ea. At the same temperature, a smaller Ea makes the Boltzmann factor e^(-Ea/RT) larger, increasing k. Temperature and activation energy are two independent ways to change k in the Arrhenius equation. Confusing these two mechanisms is a common error — a catalyst affects Ea (and often A), not T."

- question: "A student plots ln k versus 1/T for a reaction and measures a slope of −9600 K. What is the activation energy in kJ/mol? (R = 8.314 J/mol·K)"
  type: short-answer
  answer: "Ea ≈ 79.8 kJ/mol. From the linearized Arrhenius equation ln k = ln A − (Ea/R)(1/T), the slope equals −Ea/R. Therefore Ea = −slope × R = 9600 K × 8.314 J/mol·K = 79,814 J/mol ≈ 79.8 kJ/mol."
  explanation: "The linearized form is the practical tool for extracting Ea from experimental data. The slope of a ln k vs 1/T plot is always −Ea/R (negative because higher temperature means lower 1/T and higher k). Multiplying the magnitude of the slope by R converts from units of K to J/mol. Dividing by 1000 converts to kJ/mol, the conventional unit for activation energies."
```

## Explainer

When you studied chemical kinetics and rate laws, you learned that the rate constant k determines how fast a reaction proceeds. But k itself depends on temperature in a way that rate law expressions do not reveal. The Arrhenius equation fills this gap: k = Ae^(−Ea/RT). It says that k is exponentially sensitive to both the activation energy Ea and the temperature T — two levers with very different physical meanings.

The activation energy Ea is the minimum energy a colliding pair of molecules must have to successfully react and form products. Even when two reactant molecules collide with the right orientation, most collisions fail because the molecules do not have enough kinetic energy to distort bonds to the transition state geometry. The Boltzmann factor e^(−Ea/RT) is the fraction of all collisions that do have sufficient energy. Because this is an exponential function, even modest increases in Ea produce dramatic decreases in k — this is why a reaction with Ea = 80 kJ/mol can be millions of times slower than one with Ea = 40 kJ/mol at the same temperature. The pre-exponential factor A (also called the frequency factor) captures both how often molecules collide and what fraction of those collisions have the correct geometric orientation; it is roughly constant over small temperature ranges.

Taking the natural log of both sides gives the linearized form: ln k = ln A − (Ea/R)(1/T). This is a straight line with slope −Ea/R when you plot ln k on the y-axis and 1/T on the x-axis. This is the workhorse equation for experimentalists: measure k at several temperatures, plot the data, fit a line, and read off Ea from the slope. The two-temperature version, ln(k₂/k₁) = (Ea/R)(1/T₁ − 1/T₂), lets you predict how much the rate constant changes across a temperature range — a critical calculation in both laboratory design and industrial process engineering.

Catalysts enter the picture through Ea. A catalyst provides an alternative mechanistic pathway that connects the same reactants to the same products but passes through a lower-energy transition state. Because Ea is smaller, the Boltzmann factor e^(−Ea/RT) is larger, and k increases — even though the temperature has not changed. Crucially, a catalyst changes only the kinetics. The thermodynamic quantities ΔG, ΔH, and the equilibrium constant K depend only on the difference in energy between reactants and products, which the catalyst does not touch. A reaction that is thermodynamically unfavorable cannot be forced to completion by a catalyst; it can only reach equilibrium faster.

One practical caution: the "rate doubles for every 10°C" rule is a handy approximation but not a law. The actual factor from a 10°C increase depends on Ea and the starting temperature. At high activation energies or low temperatures, the rate can increase far more than twofold per 10°C. When precision matters — drug stability studies, enzyme kinetics, industrial reactors — always use the full Arrhenius calculation rather than the rule of thumb.
