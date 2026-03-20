---
id: le-chatelier-principle-applications
title: Le Chatelier's Principle and Equilibrium Shifts
domain: chemistry
course: general-chemistry
prerequisites:
- id: reaction-quotient-direction-of-reaction
  type: hard
builds-toward:
- buffer-chemistry-le-chatelier-application
tags:
- le-chatelier
- equilibrium
- stress
- shift
stage: advanced
status: draft
---

# Le Chatelier's Principle and Equilibrium Shifts

## Core Idea
Le Chatelier's principle states that when a stress (change in concentration, pressure, or temperature) is applied to a system at equilibrium, the equilibrium shifts to counteract that stress. Temperature changes alter K; pressure and concentration changes shift the position without changing K. This principle predicts how equilibrium systems respond to external changes.

## How It's Best Learned
For each type of stress (concentration, pressure, temperature), predict the direction of shift and verify using Q and K reasoning.

## Explainer

You already understand the reaction quotient Q and the equilibrium constant K, and you know that when Q < K the reaction proceeds forward, when Q > K it proceeds in reverse, and when Q = K the system is at equilibrium. Le Chatelier's principle is a qualitative shortcut that predicts the same outcomes: when you disturb an equilibrium, the system shifts in the direction that partially counteracts the disturbance. The word "partially" is essential — the system never fully restores the original conditions; it reaches a new equilibrium that reduces the stress.

**Concentration changes** are the most intuitive. Consider the equilibrium N₂ + 3H₂ ⇌ 2NH₃. If you add more N₂, you have temporarily increased the numerator's reactant — in Q terms, Q drops below K because the denominator has grown relative to the product term. The system responds by consuming some of the added N₂ and producing more NH₃ until Q = K again. If you remove NH₃ (by condensing it out, as is done industrially), the effect is similar: the product concentration drops, Q falls below K, and the equilibrium shifts forward. The key insight is that K itself does not change — only the position of equilibrium shifts to restore Q = K.

**Pressure changes** affect gaseous equilibria and are best understood by counting moles of gas on each side. In the Haber reaction, there are 4 moles of gas on the left (1 N₂ + 3 H₂) and 2 on the right (2 NH₃). Increasing pressure (by decreasing volume) favors the side with fewer gas moles — the system shifts toward NH₃ because producing 2 moles from 4 reduces the total number of gas particles and thus the pressure. If the reaction has equal moles of gas on both sides, pressure changes have no effect on equilibrium position. Adding an inert gas at constant volume does not shift equilibrium because it does not change the concentrations of any reactant or product.

**Temperature changes** are unique because they actually change the value of K. For an exothermic reaction (ΔH < 0), you can think of heat as a product: N₂ + 3H₂ ⇌ 2NH₃ + heat. Raising the temperature adds "heat" to the product side, and the equilibrium shifts left to consume that excess — K decreases. For an endothermic reaction, heat is effectively a reactant, so raising temperature shifts the equilibrium forward and increases K. This is the one stress that changes both the position of equilibrium and the equilibrium constant itself. Knowing whether your reaction is exothermic or endothermic is therefore essential for predicting the temperature response — a distinction the other stresses don't require.
