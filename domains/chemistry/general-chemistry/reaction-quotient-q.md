---
id: reaction-quotient-q
title: Reaction Quotient (Q) and Equilibrium Comparison
domain: chemistry
course: general-chemistry
prerequisites:
- id: chemical-equilibrium
  type: hard
- id: le-chatelier-principle
  type: hard
tags:
- reaction quotient
- Q vs K
- equilibrium state
stage: formal-systems
status: validated
---

# Reaction Quotient (Q) and Equilibrium Comparison

## Core Idea
The reaction quotient Q has the same form as the equilibrium constant K but uses current concentrations. Comparing Q to K predicts whether the system will shift forward or backward to reach equilibrium.

## How It's Best Learned
Calculate Q for various concentration sets and predict the direction of shift.

## Questions

```yaml
- question: "For the reaction A(g) ⇌ B(g), K = 10. You measure [A] = 2 M and [B] = 30 M. What happens next?"
  type: multiple-choice
  options:
    - "The reaction shifts forward because products are present in large amounts"
    - "The reaction shifts in reverse because Q (= 15) is greater than K (= 10)"
    - "The reaction is at equilibrium because both species are present"
    - "The reaction shifts forward because more reactant must be consumed"
  answer: 1
  explanation: "Q = [B]/[A] = 30/2 = 15. Since Q > K (15 > 10), the product-to-reactant ratio exceeds the equilibrium ratio — there are too many products relative to where the system needs to end up. The reaction runs in reverse, consuming B and regenerating A, until Q falls back to 10. Options A and D describe the opposite direction; option C confuses 'both species present' with Q = K."

- question: "A reaction is at equilibrium (Q = K). A student adds excess product, then claims 'the equilibrium constant K has increased because there are more products.' What is the correct analysis?"
  type: multiple-choice
  options:
    - "The student is correct; more products always increase K"
    - "K depends only on temperature and is unchanged; adding product raises Q above K, so the reaction shifts in reverse until Q falls back to K"
    - "Adding product shifts the reaction forward, so both Q and K increase equally"
    - "K increases only when temperature rises; concentration changes increase Q but not K"
  answer: 1
  explanation: "K is a thermodynamic constant that depends only on temperature, not on concentrations. Adding product increases Q (more products in the numerator) above the fixed K value, making Q > K. This drives the reverse reaction until equilibrium is restored at Q = K. Option D gets part of it right (K depends on T) but implies concentration can't change Q — it can and does, which is the whole point of the Q framework."

- question: "Q and K use the same mathematical expression (products over reactants raised to stoichiometric powers), but K is only meaningful at the equilibrium state."
  type: true-false
  answer: true
  explanation: "Q and K are calculated identically, but Q can be computed at any instant using current concentrations. K is the specific value that Q takes when the system has reached equilibrium. K is fixed for a given temperature; Q changes as concentrations change. The power of Q is precisely that it can be evaluated before equilibrium to predict the direction of change."

- question: "If Q < K for a reaction, the system is already at equilibrium and no net change occurs."
  type: true-false
  answer: false
  explanation: "Q < K means the product-to-reactant ratio is currently below the equilibrium ratio — there are too many reactants relative to equilibrium. The forward reaction will proceed to generate more products, increasing Q until it equals K. Q = K is the equilibrium condition; Q < K and Q > K both indicate that the system is NOT at equilibrium."

- question: "A system is at equilibrium. More reactant is added. Using Q and K, explain why the forward reaction now proceeds."
  type: short-answer
  answer: "Adding reactant increases the denominator in the Q expression, making Q smaller than K. Since Q < K, the product-to-reactant ratio is now below the equilibrium ratio — the system has 'too many' reactants relative to where it needs to end up. The forward reaction runs to consume reactants and produce products, raising Q back toward K."
  explanation: "This question connects Q directly to Le Chatelier's principle. Le Chatelier says the system shifts to relieve the stress of added reactant — but Q vs. K shows why quantitatively. The addition lowers Q below K, and the forward reaction is the only way to restore Q = K. Every Le Chatelier prediction is a Q-vs-K comparison in disguise."
```

## Explainer

You already know that a chemical reaction at equilibrium has a fixed ratio of product to reactant concentrations described by the equilibrium constant **K**. The reaction quotient **Q** uses the exact same mathematical expression — products over reactants, each raised to their stoichiometric coefficients — but Q can be calculated at any moment, not just at equilibrium. Think of K as the destination and Q as your current GPS coordinates: by comparing the two, you know which direction you need to travel.

When **Q < K**, the ratio of products to reactants is too small compared to equilibrium. The system has "too many" reactants relative to where it needs to end up, so the reaction shifts forward (toward products) to increase the numerator and decrease the denominator until Q rises to equal K. When **Q > K**, the opposite is true — there are "too many" products, and the reaction shifts in reverse to consume products and regenerate reactants until Q falls back to K. When **Q = K**, the system is already at equilibrium and no net change occurs.

This framework connects directly to Le Chatelier's principle, which you studied previously. When you add more reactant to a system at equilibrium, you are effectively decreasing Q (the denominator grows). Le Chatelier says the system shifts forward to relieve that stress — and now you can see why quantitatively: Q dropped below K, so the forward reaction runs until the ratio is restored. Similarly, removing product lowers Q, driving the forward reaction. Every Le Chatelier prediction can be recast as a Q-versus-K comparison.

The power of Q is that it gives you a quantitative prediction tool, not just a qualitative one. Given actual concentrations and a known K value, you can calculate Q, compare it to K, and state definitively which direction the reaction will proceed. This becomes essential in solubility problems (comparing the ion product Q to the solubility product Ksp), electrochemistry (the Nernst equation relates cell potential to Q), and any situation where you need to assess whether a system has reached equilibrium or predict what will happen next.
