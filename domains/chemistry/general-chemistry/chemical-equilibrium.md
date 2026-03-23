---
id: chemical-equilibrium
title: Chemical Equilibrium
domain: chemistry
course: general-chemistry
prerequisites:
- id: stoichiometry-calculations
  type: hard
- id: thermochemistry-enthalpy
  type: soft
- id: logarithms-intro
  type: soft
- id: entropy-and-gibbs-free-energy
  type: soft
builds-toward:
- acid-base-chemistry
- ph-and-acid-base-calculations
- chemical-kinetics
tags:
- equilibrium-constant
- Kc
- Kp
- Le-Chateliers-principle
- ICE-table
- reaction-quotient
stage: formal-systems
status: validated
---
# Chemical Equilibrium

## Core Idea
Many chemical reactions are reversible — they proceed in both forward and reverse directions simultaneously until the net rates equalize at equilibrium. The equilibrium constant K is the ratio of product concentrations to reactant concentrations, each raised to their stoichiometric coefficients. Le Chatelier's principle states that a system at equilibrium shifts to counteract any applied stress (change in concentration, pressure, or temperature). The reaction quotient Q, compared to K, indicates whether a system will shift forward (Q < K), backward (Q > K), or is already at equilibrium (Q = K).

## How It's Best Learned
Practice ICE (Initial-Change-Equilibrium) tables to solve for equilibrium concentrations. Apply Le Chatelier's principle qualitatively to predict shifts for various stresses. Use the small x approximation when Ka is very small relative to initial concentration, but verify its validity.

## Common Misconceptions
- 'Equilibrium' does not mean equal concentrations of reactants and products — it means the forward and reverse rates are equal. Products can greatly predominate (large K) or reactants can predominate (small K).
- Temperature changes the value of K itself; all other stresses (concentration, pressure) shift the position of equilibrium but leave K unchanged.

## Questions

```yaml
- question: "For the reaction N₂ + 3H₂ ⇌ 2NH₃ at equilibrium, you suddenly increase the concentration of H₂. What happens to Q and the direction of shift?"
  type: multiple-choice
  options:
    - "Q increases above K, so the reaction shifts in reverse (toward reactants)"
    - "Q decreases below K, so the reaction shifts forward (toward products)"
    - "K increases to match the new conditions, so there is no shift"
    - "Q equals K still, because equilibrium is self-correcting"
  answer: 1
  explanation: "Adding a reactant makes Q smaller than K (more reactants relative to products compared to the equilibrium ratio). The system shifts forward to restore Q = K. K itself is unaffected — only temperature changes K."

- question: "A reaction at equilibrium has K = 0.001, meaning the reactants are strongly favored. If you add more product, the system will shift forward (toward more product) to maintain equilibrium."
  type: true-false
  answer: false
  explanation: "Adding product increases Q above K, so the system shifts in reverse (toward reactants) to reduce Q back to K. When Q > K the system always shifts backward. The small value of K (0.001) already tells you reactants predominate; adding more product makes the imbalance worse and the reverse shift corrects it."

- question: "A student claims 'a reaction is at equilibrium when the concentrations of reactants and products are equal.' What is wrong with this statement?"
  type: short-answer
  answer: "Equilibrium means the forward and reverse reaction rates are equal, not that concentrations are equal. The equilibrium concentrations are determined by K, which can be very large (products dominate) or very small (reactants dominate)."
  explanation: "This is the most common equilibrium misconception. K = [products]/[reactants] can take any positive value. Only when K = 1 are the equilibrium concentrations roughly equal. The defining feature of equilibrium is equal rates, not equal amounts."
```

## Explainer

Chemical equilibrium is one of the most conceptually rich ideas in general chemistry because it forces you to think about reactions as ongoing, two-directional processes rather than one-way events. When you mix nitrogen and hydrogen gas at high temperature, both the forward reaction (making ammonia) and the reverse reaction (decomposing ammonia) happen simultaneously. Equilibrium is reached when the rate of the forward reaction equals the rate of the reverse reaction — not when the reaction "stops."

The equilibrium constant K captures the outcome of this balance. For a reaction aA + bB ⇌ cC + dD, the equilibrium expression is K = [C]^c[D]^d / [A]^a[B]^b, where the brackets denote molar concentrations at equilibrium and the exponents are the stoichiometric coefficients. K is a fixed number at a given temperature — large K means products predominate at equilibrium, small K means reactants predominate. Notice that K depends only on temperature; changing concentrations or pressure shifts where equilibrium sits but does not change the value of K.

Le Chatelier's principle is the conceptual shortcut: any stress applied to a system at equilibrium will be "counteracted" by a shift in the equilibrium position. If you add reactant, the system shifts forward. If you remove product, the system shifts forward. If you increase pressure (in a gas-phase reaction), the system shifts toward the side with fewer moles of gas. The mathematical reason this works is the reaction quotient Q. At any moment, Q = [products]/[reactants] using current (not equilibrium) concentrations. If Q < K, the system shifts forward; if Q > K, it shifts in reverse; if Q = K, it is at equilibrium.

ICE tables give you a systematic way to calculate equilibrium concentrations. Set up rows for Initial concentration, Change in concentration (−x for reactants, +x for products, scaled by stoichiometry), and Equilibrium concentration. Substitute the equilibrium row into the K expression and solve for x. When K is very small (≤ 10⁻⁴), the "small x approximation" lets you drop x from sums and differences, simplifying the algebra — but always check that x is indeed small relative to the initial concentrations after solving.

One crucial distinction: temperature is unique among the stresses you can apply. Adding more reactant, changing pressure, or introducing an inert gas shifts the position of equilibrium but leaves K unchanged. Changing temperature actually changes the value of K — it alters the equilibrium constant itself. Whether K increases or decreases with temperature depends on whether the forward reaction is endothermic or exothermic, which connects this topic directly to thermodynamics.
