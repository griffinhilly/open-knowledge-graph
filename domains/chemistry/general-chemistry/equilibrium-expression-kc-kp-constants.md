---
id: equilibrium-expression-kc-kp-constants
title: 'Equilibrium Constants: Kc and Kp'
domain: chemistry
course: general-chemistry
prerequisites:
- id: chemical-equilibrium
  type: hard
- id: gas-laws
  type: soft
- id: solving-multi-step-equations
  type: soft
- id: exponential-functions-and-graphs
  type: soft
builds-toward:
- reaction-quotient-direction-of-reaction
- le-chatelier-principle-applications
tags:
- kc
- kp
- equilibrium-constant
- equilibrium
stage: formal-systems
status: validated
---

# Equilibrium Constants: Kc and Kp

## Core Idea
The equilibrium constant Kc is expressed in terms of molar concentrations; Kp is expressed in terms of partial pressures (for gaseous equilibria). The two are related by Kp = Kc(RT)^Δn, where Δn is the change in moles of gas. Both are temperature-dependent and dimensionless (or have derived units depending on stoichiometry).

## Common Misconceptions
Thinking Kc and Kp are the same or that they have the same numerical value. Forgetting that only gases contribute to Kp, and only solutes contribute to Kc (water is typically omitted).

## Questions

```yaml
- question: "For the reaction N₂(g) + 3H₂(g) ⇌ 2NH₃(g), what is the value of Δn used in Kp = Kc(RT)^Δn?"
  type: multiple-choice
  options: ["-2", "+2", "-4", "+4"]
  answer: 0
  explanation: "Δn = moles of gaseous products − moles of gaseous reactants = 2 − (1 + 3) = −2. This negative Δn means Kp < Kc for this reaction at any temperature above 0 K, because (RT)^−2 is less than 1."

- question: "When writing Kc for a reaction that involves a solid reactant (e.g., CaCO₃(s) ⇌ CaO(s) + CO₂(g)), the concentration of CaCO₃ must appear in the denominator of the equilibrium expression."
  type: true-false
  answer: false
  explanation: "Pure solids and pure liquids are omitted from equilibrium expressions because their concentrations are constant (their 'concentration' is absorbed into the value of K). Only gases and dissolved solutes appear. For this reaction, Kc = [CO₂] and Kp = P(CO₂)."

- question: "Why are Kc and Kp numerically different for most reactions, even though they describe the same equilibrium?"
  type: short-answer
  answer: "Kc measures concentrations in mol/L while Kp measures partial pressures in atm (or Pa). They are related by Kp = Kc(RT)^Δn, where Δn is the change in moles of gas. Unless Δn = 0, the (RT)^Δn factor shifts the numerical value, so the two constants differ."
  explanation: "The conversion factor (RT)^Δn bridges the concentration and pressure scales. When Δn = 0 (equal moles of gas on both sides), Kp = Kc. For all other reactions the two constants diverge in proportion to temperature and the imbalance in gas moles."
```

## Explainer

When you studied chemical equilibrium, you learned that reversible reactions reach a state where the forward and reverse rates are equal — and that the ratio of product concentrations to reactant concentrations at equilibrium is constant at a given temperature. Kc and Kp are both ways of expressing that ratio; the difference is only in what units you use to measure "how much."

Kc uses molar concentrations (mol/L). For a general reaction aA + bB ⇌ cC + dD, the expression is Kc = [C]^c[D]^d / ([A]^a[B]^b). The brackets denote equilibrium concentrations. Notice that every concentration is raised to its stoichiometric coefficient — that exponent comes directly from the rate-law derivation underpinning equilibrium. A large Kc means products are heavily favored at equilibrium; a small Kc means reactants dominate.

Kp applies specifically to gaseous equilibria and replaces concentrations with partial pressures. Since the ideal gas law tells you P = nRT/V = (n/V)RT = [gas]·RT, you can convert between the two: Kp = Kc(RT)^Δn, where Δn is the change in moles of gas (products minus reactants). If Δn = 0 (same number of gas moles on each side), Kp equals Kc. If more moles of gas are produced, Kp > Kc; if fewer, Kp < Kc. Tracking the sign of Δn is one of the most error-prone steps — count carefully.

A critical rule often forgotten: pure solids and pure liquids do not appear in equilibrium expressions. The reason is that their "concentration" is essentially fixed (determined by their density, which barely changes), so it is folded into the constant K itself. Only gaseous species enter Kp, and only dissolved species enter Kc. In heterogeneous equilibria — reactions mixing phases — this distinction is essential to writing a correct expression.

Both constants are temperature-dependent but pressure-independent. Adding or removing reactants shifts the position of equilibrium (the reaction quotient Q changes) but does not change K itself. This is the foundation for Le Chatelier's principle, which you will explore next: K stays fixed while Q adjusts until it again equals K.

