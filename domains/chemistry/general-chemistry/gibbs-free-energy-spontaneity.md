---
id: gibbs-free-energy-spontaneity
title: Gibbs Free Energy and Spontaneity
domain: chemistry
course: general-chemistry
prerequisites:
- id: entropy-and-gibbs-free-energy
  type: hard
- id: thermochemistry-enthalpy
  type: soft
builds-toward:
- chemical-equilibrium
- electrochemistry-basics
tags:
- Gibbs-free-energy
- spontaneity
- delta-G
- enthalpy-entropy-temperature
- exergonic
- endergonic
- equilibrium-constant-relation
stage: abstract-reasoning
status: draft
---
# Gibbs Free Energy and Spontaneity

## Core Idea
The Gibbs free energy change, ΔG = ΔH − TΔS, determines whether a process is thermodynamically spontaneous at constant temperature and pressure. A reaction is spontaneous when ΔG < 0 (exergonic) and non-spontaneous when ΔG > 0 (endergonic). When ΔG = 0, the system is at equilibrium. The interplay of enthalpy and entropy creates four categories: reactions that are always spontaneous (ΔH < 0, ΔS > 0), never spontaneous (ΔH > 0, ΔS < 0), spontaneous only at high temperature (ΔH > 0, ΔS > 0), or spontaneous only at low temperature (ΔH < 0, ΔS < 0). The standard free energy change is related to the equilibrium constant by ΔG° = −RT ln K.

## How It's Best Learned
Classify reactions into the four ΔH/ΔS categories and predict the temperature dependence of spontaneity. Calculate the crossover temperature (T = ΔH/ΔS) where spontaneity switches. Practice connecting ΔG° to K to understand why large negative ΔG° means products are heavily favored at equilibrium.

## Common Misconceptions
- Spontaneous does not mean fast. Thermodynamic spontaneity says nothing about rate — diamond converting to graphite is spontaneous but imperceptibly slow.
- ΔG° (standard conditions) and ΔG (actual conditions) are different. A reaction with positive ΔG° can still proceed forward if concentrations are far from equilibrium such that ΔG = ΔG° + RT ln Q is negative.

## Questions

```yaml
- question: "A reaction has ΔH = +50 kJ/mol and ΔS = +200 J/(mol·K). At what temperature range is this reaction spontaneous?"
  type: multiple-choice
  options: ["Never spontaneous", "Always spontaneous", "Spontaneous only at low temperatures", "Spontaneous only at high temperatures"]
  answer: 3
  explanation: "ΔG = ΔH − TΔS. With ΔH > 0 and ΔS > 0, ΔG = positive − T(positive). As T increases, the −TΔS term grows more negative and eventually dominates, making ΔG < 0. The crossover temperature is T = ΔH/ΔS = 50,000 J / 200 J·K⁻¹ = 250 K; above this temperature, the reaction is spontaneous."

- question: "A reaction is thermodynamically spontaneous (ΔG < 0), so it must proceed at a measurable rate under ordinary conditions."
  type: true-false
  answer: false
  explanation: "Spontaneity (ΔG < 0) describes thermodynamic favorability — the direction a system would eventually reach equilibrium — but says nothing about the rate. The conversion of diamond to graphite is spontaneous under standard conditions, yet it is immeasurably slow. Kinetics and thermodynamics are independent: a reaction can be thermodynamically spontaneous yet kinetically inert due to a high activation energy barrier."

- question: "What does it mean for a chemical reaction when ΔG = 0?"
  type: short-answer
  answer: "The reaction is at equilibrium — the forward and reverse reactions proceed at equal rates, and there is no net change in the amounts of reactants or products."
  explanation: "ΔG = 0 is the condition for thermodynamic equilibrium. It does not mean nothing is happening; both forward and reverse reactions continue, but at equal rates. The relationship ΔG° = −RT ln K connects the standard free energy to the equilibrium constant, showing that when ΔG° = 0, K = 1 (products and reactants equally favored at standard conditions)."
```

## Explainer

The Gibbs free energy is the master variable for predicting whether a chemical reaction will proceed spontaneously at constant temperature and pressure — which covers virtually all laboratory and biological situations. The key equation is ΔG = ΔH − TΔS. This expression combines two competing tendencies: systems tend toward lower enthalpy (releasing energy to surroundings, ΔH < 0) and toward higher entropy (greater disorder, ΔS > 0). A reaction is spontaneous when ΔG < 0, meaning the combined effect of enthalpy and entropy favors the products.

The four combinations of ΔH and ΔS sign tell you everything about temperature dependence. When ΔH < 0 and ΔS > 0, both terms drive ΔG negative — the reaction is spontaneous at all temperatures. When ΔH > 0 and ΔS < 0, both terms fight against spontaneity — the reaction never proceeds spontaneously. The interesting cases involve a sign conflict: when ΔH > 0 and ΔS > 0, only the entropy term becomes favorable, but it needs a large enough T to overcome the unfavorable enthalpy — so spontaneity kicks in above a crossover temperature T = ΔH/ΔS. The reverse applies when ΔH < 0 and ΔS < 0. Working through these four cases with the equation, rather than memorizing them, builds genuine understanding.

The most important misconception to clear up: spontaneous does not mean fast. Thermodynamics describes which direction a system would eventually go if given infinite time; kinetics describes how quickly it gets there. Diamond is thermodynamically less stable than graphite at room temperature and pressure — its conversion to graphite is spontaneous — yet the process is so kinetically slow that diamonds persist indefinitely. Similarly, many combustion reactions are highly spontaneous (large negative ΔG) but require activation energy to initiate. Never conflate ΔG with reaction rate.

The standard free energy change ΔG° and the equilibrium constant K are linked by ΔG° = −RT ln K. This relationship is enormously powerful: it means you can calculate K from tabulated thermodynamic data, or predict whether products or reactants are favored at equilibrium from ΔG°. A large negative ΔG° corresponds to K ≫ 1 (products heavily favored); a large positive ΔG° corresponds to K ≪ 1 (reactants heavily favored). When ΔG° = 0, K = 1, meaning products and reactants are present in roughly equal amounts at equilibrium.

Finally, notice that ΔG (not ΔG°) is what governs whether a reaction proceeds under actual conditions. ΔG = ΔG° + RT ln Q, where Q is the reaction quotient. Even if ΔG° is positive, the reaction can still proceed forward if the system is far from equilibrium (Q ≪ K), making the RT ln Q term sufficiently negative to overcome ΔG°. This is why reactions proceed even when they appear "thermodynamically unfavorable" — the standard state is rarely the actual state.
