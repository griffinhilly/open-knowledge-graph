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
stage: formal-systems
status: validated
---

# Le Chatelier's Principle and Equilibrium Shifts

## Core Idea
Le Chatelier's principle states that when a stress is applied to a system at equilibrium, the system shifts to counteract that stress. Stresses include concentration, temperature, and pressure changes.

## How It's Best Learned
Apply the principle qualitatively to predict shifts, then verify with K and Q calculations.

## Common Misconceptions
Thinking the system always shifts left or right; forgetting that K changes with temperature.

## Questions

```yaml
- question: "A student adds a catalyst to the equilibrium reaction N₂ + 3H₂ ⇌ 2NH₃ to increase ammonia yield. What actually happens?"
  type: multiple-choice
  options:
    - "The equilibrium shifts toward products, increasing the concentration of NH₃ at equilibrium"
    - "The equilibrium shifts toward reactants, which then shift back, eventually settling at higher NH₃"
    - "The equilibrium position is unchanged — the catalyst speeds up both forward and reverse reactions equally, so the system reaches the same equilibrium faster"
    - "The equilibrium constant K increases, giving a higher yield of NH₃"
  answer: 2
  explanation: "A catalyst lowers the activation energy for both the forward and reverse reactions by the same amount. Since both rates increase equally, the ratio of forward to reverse rate — and therefore the equilibrium constant K — is unchanged. The equilibrium position (the concentrations at equilibrium) does not shift. What does change is how quickly equilibrium is reached. This is a very common misconception: catalysts affect kinetics (rate), not thermodynamics (equilibrium position or K). To increase NH₃ yield, you would need to remove NH₃ as it forms, increase pressure, or lower the temperature."

- question: "The Haber process (N₂ + 3H₂ ⇌ 2NH₃, exothermic) is run at elevated temperature in practice, even though this shifts equilibrium toward reactants. What does this reveal about Le Chatelier's principle?"
  type: multiple-choice
  options:
    - "Le Chatelier's principle is wrong — temperature does not affect equilibrium position"
    - "Le Chatelier's principle correctly predicts that yield decreases, but higher temperature is used anyway because the rate is too slow at low temperature — kinetics and equilibrium are separate considerations"
    - "Le Chatelier's principle predicts that elevated temperature increases yield for exothermic reactions"
    - "The Haber process is endothermic, so elevated temperature correctly shifts toward products"
  answer: 1
  explanation: "Le Chatelier's principle is correct: raising temperature for an exothermic reaction shifts equilibrium toward reactants, decreasing K and reducing equilibrium yield. In practice, Haber plants use elevated temperature (~400°C) because at lower temperatures the reaction is too slow to be commercially viable even with a catalyst. This illustrates a crucial point: Le Chatelier's principle describes equilibrium position (thermodynamics), while reaction rate is a kinetics question. Industrial chemistry often involves optimizing the trade-off between yield (favored by low temperature) and rate (favored by high temperature)."

- question: "Adding an inert gas like argon at constant volume to a gaseous equilibrium shifts the position of equilibrium toward the side with fewer moles of gas."
  type: true-false
  answer: false
  explanation: "Adding an inert gas at constant volume does NOT shift the equilibrium. Le Chatelier's pressure argument applies when the total pressure changes the partial pressures of the reacting gases. An inert gas at constant volume increases total pressure but does not change the partial pressures of N₂, H₂, or NH₃ — those remain determined by their own concentrations, which haven't changed. Since the partial pressures of reactants and products are unchanged, Q = K still holds and there is no shift. The confusion arises from conflating total pressure with the partial pressures of reactive species."

- question: "For an exothermic reaction at equilibrium, raising the temperature causes the equilibrium constant K to decrease."
  type: true-false
  answer: true
  explanation: "Temperature is the one stress that actually changes K. For an exothermic reaction, heat is a product: reactants ⇌ products + heat. Raising temperature adds 'heat,' and the system shifts to consume it — toward reactants — lowering the concentration ratio of products to reactants and therefore decreasing K. This is fundamentally different from concentration or pressure changes, which shift the position of equilibrium (changing concentrations) without altering K. The van't Hoff equation (d ln K / dT = ΔH°/RT²) formalizes this: exothermic ΔH° < 0 means K decreases as T increases."

- question: "How is a temperature change fundamentally different from a concentration change in its effect on chemical equilibrium? Why does this distinction matter?"
  type: short-answer
  answer: "A concentration change shifts the position of equilibrium — it changes the equilibrium concentrations — but does not change the equilibrium constant K. The system reaches a new state where Q returns to the unchanged value of K. A temperature change actually changes K itself, because temperature affects the intrinsic thermodynamics of the reaction (the Gibbs energy of the system). For an exothermic reaction, raising temperature decreases K; for an endothermic reaction, it increases K. This matters because K determines the maximum possible yield — changing concentration can optimize around a fixed yield ceiling, but changing temperature moves the ceiling itself."
  explanation: "This distinction is practically important in industrial chemistry. You can drive a reaction forward by removing products (Le Chatelier: concentration stress, no change to K) — this is exploited in continuous-flow reactors. But to achieve a fundamentally different equilibrium yield, you must change the temperature, which comes at a kinetic cost. Understanding whether a stress changes K or merely Q is the key to distinguishing thermodynamic from kinetic optimization."
```

## Explainer

From chemical equilibrium, you know that reversible reactions reach a state where the forward and reverse rates are equal, and the ratio of product to reactant concentrations is described by the equilibrium constant K. Le Chatelier's principle gives you a powerful qualitative tool for predicting what happens when you disturb that balance: **when a system at equilibrium is subjected to a stress, it shifts in the direction that partially counteracts the stress**. The word "partially" is important — the system never fully undoes the change, it just moves toward a new equilibrium that lessens the disturbance.

There are three main types of stress. First, **concentration changes**: if you add more reactant, the system shifts toward products to consume some of the added material; if you remove a product, the system also shifts forward to replenish it. Think of it as a seesaw — pile weight on one side and the balance tips the other way. For example, in the Haber process (N₂ + 3H₂ ⇌ 2NH₃), removing ammonia as it forms drives the reaction forward, increasing yield. Second, **pressure changes** (for gaseous equilibria): increasing pressure shifts the equilibrium toward the side with fewer moles of gas, because that reduces the total number of gas molecules and partially relieves the pressure increase. In the Haber process, 4 moles of gas on the left become 2 on the right, so high pressure favors ammonia production — which is why industrial Haber plants operate at 150–300 atm.

Third, **temperature changes** — and this is where students most often make errors, because temperature is the one stress that actually changes the value of K. You must treat heat as a participant: for an exothermic reaction, heat is effectively a product (reactants → products + heat). Raising the temperature adds "heat," so the system shifts to consume it — toward reactants — and K decreases. For an endothermic reaction, heat is a reactant, so raising temperature shifts the equilibrium toward products and K increases. This is fundamentally different from concentration and pressure changes, which shift the position of equilibrium without changing K.

One critical clarification: **adding a catalyst does not shift equilibrium**. A catalyst speeds up both the forward and reverse reactions equally, so the system reaches equilibrium faster but at the same position. Similarly, adding an inert gas at constant volume does not change the partial pressures of the reacting gases, so there is no shift. Le Chatelier's principle is not a fundamental law but a useful heuristic — for quantitative predictions, you compare the reaction quotient Q to K, which you will study next. But as a quick reasoning tool for predicting the direction of change, Le Chatelier's principle is indispensable.
