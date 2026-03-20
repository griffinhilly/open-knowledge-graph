---
id: le-chatelier-principle
title: Le Chatelier's Principle and Equilibrium Shifts
domain: chemistry
course: general-chemistry
prerequisites:
- id: chemical-equilibrium
  type: hard
builds-toward:
- reaction-quotient
- solubility-equilibria
tags:
- equilibrium shift
- stress on equilibrium
- perturbation
stage: advanced
status: draft
---

# Le Chatelier's Principle and Equilibrium Shifts

## Core Idea
Le Chatelier's principle states that when a stress is applied to a system at equilibrium, the system shifts to counteract that stress. Stresses include concentration, temperature, and pressure changes.

## How It's Best Learned
Apply the principle qualitatively to predict shifts, then verify with K and Q calculations.

## Common Misconceptions
Thinking the system always shifts left or right; forgetting that K changes with temperature.

## Explainer

From chemical equilibrium, you know that reversible reactions reach a state where the forward and reverse rates are equal, and the ratio of product to reactant concentrations is described by the equilibrium constant K. Le Chatelier's principle gives you a powerful qualitative tool for predicting what happens when you disturb that balance: **when a system at equilibrium is subjected to a stress, it shifts in the direction that partially counteracts the stress**. The word "partially" is important — the system never fully undoes the change, it just moves toward a new equilibrium that lessens the disturbance.

There are three main types of stress. First, **concentration changes**: if you add more reactant, the system shifts toward products to consume some of the added material; if you remove a product, the system also shifts forward to replenish it. Think of it as a seesaw — pile weight on one side and the balance tips the other way. For example, in the Haber process (N₂ + 3H₂ ⇌ 2NH₃), removing ammonia as it forms drives the reaction forward, increasing yield. Second, **pressure changes** (for gaseous equilibria): increasing pressure shifts the equilibrium toward the side with fewer moles of gas, because that reduces the total number of gas molecules and partially relieves the pressure increase. In the Haber process, 4 moles of gas on the left become 2 on the right, so high pressure favors ammonia production — which is why industrial Haber plants operate at 150–300 atm.

Third, **temperature changes** — and this is where students most often make errors, because temperature is the one stress that actually changes the value of K. You must treat heat as a participant: for an exothermic reaction, heat is effectively a product (reactants → products + heat). Raising the temperature adds "heat," so the system shifts to consume it — toward reactants — and K decreases. For an endothermic reaction, heat is a reactant, so raising temperature shifts the equilibrium toward products and K increases. This is fundamentally different from concentration and pressure changes, which shift the position of equilibrium without changing K.

One critical clarification: **adding a catalyst does not shift equilibrium**. A catalyst speeds up both the forward and reverse reactions equally, so the system reaches equilibrium faster but at the same position. Similarly, adding an inert gas at constant volume does not change the partial pressures of the reacting gases, so there is no shift. Le Chatelier's principle is not a fundamental law but a useful heuristic — for quantitative predictions, you compare the reaction quotient Q to K, which you will study next. But as a quick reasoning tool for predicting the direction of change, Le Chatelier's principle is indispensable.
