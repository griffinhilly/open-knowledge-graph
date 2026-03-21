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

## Questions

```yaml
- question: "For the reaction A ⇌ 2B, Kc = 10. A student measures [A] = 0.5 M and [B] = 3.0 M, calculates Q = (3.0)²/(0.5) = 18, and concludes 'Q > K, but since we need more products, the reaction will proceed forward.' What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "The student calculated Q incorrectly; the correct value is less than 10"
    - "The student's conclusion is backwards: Q > K means there are too many products relative to equilibrium, so the reaction proceeds in reverse"
    - "The student is correct — when Q > K, there is room to make more products"
    - "The comparison Q vs K only applies at standard conditions; at arbitrary concentrations you must use ΔG directly"
  answer: 1
  explanation: "When Q > K, the ratio of products to reactants is already too high compared to what equilibrium demands. The reaction must shift in reverse — converting products back to reactants — until Q falls to match K. The student confused the direction: Q > K does NOT mean 'need more products,' it means 'already have too many products.' The K value is the target; Q is where you are. If your coordinates (Q) are higher than the destination (K), you must move backward, not forward."

- question: "A reaction has Kc = 0.001 at a given temperature. You mix only reactants (no products) and measure Q = 0. What does this tell you about the direction the reaction will proceed?"
  type: multiple-choice
  options:
    - "The reaction will not proceed because Kc is very small, meaning products are heavily disfavored"
    - "The reaction will proceed in the forward direction because Q < K, regardless of how small K is"
    - "The reaction will proceed in reverse because Kc < 1 means reactants are favored"
    - "The comparison is undefined when Q = 0 because you cannot divide by zero"
  answer: 1
  explanation: "When Q < K, the reaction always proceeds forward — regardless of how small K is. Q = 0 (no products present) is always less than any positive K, so the forward reaction will occur. It will produce very little product (since K is tiny, only a small amount of products will be present at equilibrium), but it will proceed forward nonetheless. The magnitude of K tells you where equilibrium lies (favoring reactants or products), but the direction of approach is determined by comparing Q to K, and Q < K always means forward."

- question: "The equilibrium constant K changes whenever you add more reactant to a reaction mixture at constant temperature."
  type: true-false
  answer: false
  explanation: "K is determined solely by temperature — it is a property of the reaction at a given temperature, not of the specific amounts of reactants and products present. Adding more reactant changes Q (the reaction quotient) immediately, but K stays fixed. The new Q < K comparison then drives the reaction forward until Q rises back to K. This is the power of the Q vs K framework: K is the destination, and adding or removing substances changes Q (your current position) while K (the destination) remains constant. Only changing the temperature changes K."

- question: "Calculating Q requires knowing which concentrations or pressures the reaction mixture has right now, and gives the same numerical value as K only when the system is at equilibrium."
  type: true-false
  answer: true
  explanation: "Correct. Q and K use identical mathematical expressions — products over reactants, raised to stoichiometric powers — but Q uses whatever concentrations or pressures the system has at the moment of measurement, while K uses only the equilibrium concentrations. At any non-equilibrium state, Q ≠ K. Q = K is the definition of equilibrium: it is the one concentration ratio where no net forward or reverse reaction occurs. Before equilibrium, Q ≠ K, and the sign of (K − Q) tells you the direction the system will shift."

- question: "Explain why K is called the 'destination' and Q is called the 'current position' of a reaction, and how this comparison predicts the direction of reaction."
  type: short-answer
  answer: "K is fixed at a given temperature — it represents the unique ratio of products to reactants that the system will always settle into at equilibrium, no matter what you start with. It is the destination because every reaction mixture, regardless of initial composition, moves toward Q = K. Q is calculated from the current (non-equilibrium) concentrations, so it tells you where the system is right now on its journey toward K. If Q < K, the current product-to-reactant ratio is too low — the system must make more products to reach K, so the forward reaction dominates. If Q > K, the ratio is too high — the system must consume products and regenerate reactants, so the reverse reaction dominates. When Q = K, the system has arrived at its destination and no net change occurs."
  explanation: "The GPS analogy captures the practical power of Q: you don't need to run the experiment to know which way it will go. Mix any arbitrary amounts of reactants and products, calculate Q from those concentrations, compare to K, and the direction follows immediately. This is especially useful in industrial chemistry (where conditions change constantly), biochemistry (where reactions are rarely at equilibrium in living cells), and analytical chemistry (where predicting precipitation or dissolution requires knowing whether Q exceeds the solubility product K_sp)."
```

## Explainer

You already know how to write an equilibrium expression and what the equilibrium constant K represents — it is the ratio of product concentrations to reactant concentrations that a system settles into at equilibrium. The **reaction quotient Q** uses exactly the same mathematical expression, but you plug in whatever concentrations or pressures the system happens to have right now, whether or not it has reached equilibrium. Think of K as the destination and Q as your current GPS coordinates: comparing the two tells you which direction you need to travel.

The comparison rule is straightforward. If **Q < K**, the ratio of products to reactants is too small — the system has not yet made enough products. The reaction will proceed in the forward direction, converting reactants into products, until Q rises to equal K. If **Q > K**, there are too many products relative to what equilibrium demands, so the reaction runs in reverse, converting products back into reactants, until Q falls to match K. When **Q = K**, the system is already at equilibrium and no net change occurs.

A concrete example makes this tangible. Consider the reaction N₂ + 3H₂ ⇌ 2NH₃ with Kc = 0.50 at a given temperature. Suppose you measure [N₂] = 1.0 M, [H₂] = 1.0 M, and [NH₃] = 2.0 M. Then Q = (2.0)² / ((1.0)(1.0)³) = 4.0. Since Q = 4.0 > K = 0.50, there is too much ammonia relative to equilibrium. The reaction shifts in reverse — ammonia decomposes back into nitrogen and hydrogen — until Q decreases to 0.50.

The power of Q is that it works for any snapshot of a reaction mixture. You can mix arbitrary amounts of reactants and products, calculate Q, and immediately predict which way the reaction will shift without running the experiment. This is especially useful in industrial chemistry and biochemistry, where conditions are constantly changing and systems rarely sit at equilibrium. Every time you add or remove a substance from a reaction mixture, Q changes instantly while K stays fixed (at constant temperature), and the comparison tells you exactly how the system will respond.
