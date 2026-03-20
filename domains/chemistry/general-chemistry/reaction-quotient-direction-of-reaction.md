---
id: reaction-quotient-direction-of-reaction
title: Reaction Quotient (Q) and Equilibrium Direction
domain: chemistry
course: general-chemistry
prerequisites:
- id: equilibrium-expression-kc-kp-constants
  type: hard
builds-toward:
- le-chatelier-principle-applications
tags:
- reaction-quotient
- q
- direction
- equilibrium
stage: advanced
status: draft
---

# Reaction Quotient (Q) and Equilibrium Direction

## Core Idea
The reaction quotient Q has the same form as K but uses current (non-equilibrium) concentrations or pressures. Comparing Q to K predicts the shift needed to reach equilibrium: if Q < K, the reaction proceeds forward; if Q > K, it shifts backward. When Q = K, the system is at equilibrium.

## Explainer

You already know how to write an equilibrium expression and what the equilibrium constant K represents — it is the ratio of product concentrations to reactant concentrations that a system settles into at equilibrium. The **reaction quotient Q** uses exactly the same mathematical expression, but you plug in whatever concentrations or pressures the system happens to have right now, whether or not it has reached equilibrium. Think of K as the destination and Q as your current GPS coordinates: comparing the two tells you which direction you need to travel.

The comparison rule is straightforward. If **Q < K**, the ratio of products to reactants is too small — the system has not yet made enough products. The reaction will proceed in the forward direction, converting reactants into products, until Q rises to equal K. If **Q > K**, there are too many products relative to what equilibrium demands, so the reaction runs in reverse, converting products back into reactants, until Q falls to match K. When **Q = K**, the system is already at equilibrium and no net change occurs.

A concrete example makes this tangible. Consider the reaction N₂ + 3H₂ ⇌ 2NH₃ with Kc = 0.50 at a given temperature. Suppose you measure [N₂] = 1.0 M, [H₂] = 1.0 M, and [NH₃] = 2.0 M. Then Q = (2.0)² / ((1.0)(1.0)³) = 4.0. Since Q = 4.0 > K = 0.50, there is too much ammonia relative to equilibrium. The reaction shifts in reverse — ammonia decomposes back into nitrogen and hydrogen — until Q decreases to 0.50.

The power of Q is that it works for any snapshot of a reaction mixture. You can mix arbitrary amounts of reactants and products, calculate Q, and immediately predict which way the reaction will shift without running the experiment. This is especially useful in industrial chemistry and biochemistry, where conditions are constantly changing and systems rarely sit at equilibrium. Every time you add or remove a substance from a reaction mixture, Q changes instantly while K stays fixed (at constant temperature), and the comparison tells you exactly how the system will respond.
