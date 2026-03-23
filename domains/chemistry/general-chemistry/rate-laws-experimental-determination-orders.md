---
id: rate-laws-experimental-determination-orders
title: Rate Laws and Reaction Order Determination
domain: chemistry
course: general-chemistry
prerequisites:
- id: rate-law-determination
  type: soft
- id: logarithm-properties
  type: soft
- id: exponential-functions-and-graphs
  type: soft
builds-toward:
- reaction-mechanisms-elementary-steps
tags:
- rate-law
- order
- kinetics
- experimental
stage: formal-systems
status: validated
---

# Rate Laws and Reaction Order Determination

## Core Idea
A rate law relates reaction rate to reactant concentrations: rate = k[A]^m[B]^n, where m and n are orders determined experimentally (not from stoichiometry). Overall order is m + n. Zero-order reactions have constant rate; first-order rates depend linearly on concentration; second-order rates depend on concentration squared. Rate laws reveal reaction mechanism insights.

## Questions

```yaml
- question: "A student writes the rate law for 2A + B → C as rate = k[A]²[B], arguing that the stoichiometric coefficients give the reaction orders. Why is this reasoning incorrect?"
  type: multiple-choice
  options:
    - "Stoichiometric coefficients determine the units of the rate constant k, not the exponents in the rate law"
    - "Reaction orders must be determined experimentally because they reflect the rate-determining step of the mechanism, which is not visible in the balanced equation"
    - "The student should have used the equilibrium constant expression to find the exponents"
    - "Balanced equations can give reaction orders only for elementary reactions, and all reactions are elementary"
  answer: 1
  explanation: "The balanced equation shows the net stoichiometry — the overall transformation — but hides the step-by-step molecular pathway. A rate law reflects what happens in the rate-determining (slowest) elementary step, which may involve only a subset of the reactants, or different stoichiometric ratios than the overall equation. A reaction like 2NO₂ → 2NO + O₂ is experimentally second-order in NO₂, which happens to match the coefficient — but this agreement is coincidental for many reactions. The only way to know the orders is to measure them."

- question: "In a method-of-initial-rates experiment, keeping [B] constant while doubling [A] causes the initial rate to quadruple. What is the order with respect to A?"
  type: multiple-choice
  options:
    - "Zero-order (m = 0), because the rate doubled when concentration doubled"
    - "First-order (m = 1), because the rate increased by a factor of two per unit concentration"
    - "Second-order (m = 2), because rate ∝ [A]², so doubling [A] multiplies rate by 2² = 4"
    - "Third-order (m = 3), because the rate increase exceeds a factor of two"
  answer: 2
  explanation: "The method of initial rates works by comparing rate ratios to concentration ratios. If rate = k[A]^m and doubling [A] quadruples the rate: 4 = 2^m, so m = 2. This is the diagnostic signature of second-order kinetics. First-order would show a doubling of rate when [A] doubles; zero-order would show no rate change; third-order would produce an 8-fold rate increase. Each order has a characteristic factor relating concentration change to rate change."

- question: "For a first-order reaction, tripling the concentration of the reactant will triple the reaction rate."
  type: true-false
  answer: true
  explanation: "By definition, a first-order reaction has rate = k[A]¹, so rate is directly proportional to concentration. Tripling [A] multiplies the rate by exactly 3. This linear proportionality is the defining property of first-order kinetics. It contrasts with second-order (rate scales as [A]², so tripling [A] increases rate 9-fold) and zero-order (rate is independent of concentration, so tripling [A] has no effect on rate)."

- question: "The overall reaction order of a multi-step reaction equals the sum of the stoichiometric coefficients of the reactants in the balanced equation."
  type: true-false
  answer: false
  explanation: "Overall reaction order is the sum of the exponents in the experimentally determined rate law, not the stoichiometric coefficients. For example, the reaction H₂ + I₂ → 2HI is first-order in H₂ and first-order in I₂ (overall second-order), which happens to match the coefficients — but this is not always the case. The reaction 2NO₂ → 2NO + O₂ is second-order in NO₂ (coefficient 2) for this particular mechanism, but a different mechanism would give a different order. Orders come from experiment and mechanism, not from the balanced equation."

- question: "Why can't you determine a reaction's rate law from its balanced equation, and what does the experimentally determined rate law reveal about the reaction mechanism?"
  type: short-answer
  answer: "The balanced equation shows the overall net transformation but conceals the stepwise molecular pathway. A multi-step mechanism has a rate-determining (slowest) step, and the rate law reflects only that step — the concentrations and stoichiometry of species involved in the slow step appear in the rate law, regardless of what the overall balanced equation looks like. For example, a reaction with stoichiometry A + B → C might have a slow step involving only A (making it first-order in A and zero-order in B), or a slow step involving A + A (making it second-order in A). Only experiments can reveal which step is rate-limiting and what species participate in it. When the experimental rate law matches the rate law predicted by a proposed mechanism's slow step, it provides evidence (not proof) that the mechanism is correct."
  explanation: "This connection between the macroscopic rate law and the microscopic mechanism is one of the deepest insights in chemical kinetics: observable bulk rate behavior encodes information about unobservable molecular events. Rate laws thus serve as 'fingerprints' for reaction mechanisms — the experimental data constrain which mechanisms are plausible."
```

## Explainer

A **rate law** is a mathematical equation that tells you exactly how the speed of a reaction depends on the concentrations of the reactants. For a reaction involving reactants A and B, the rate law takes the form rate = k[A]^m[B]^n, where k is the **rate constant** (which depends on temperature), the square brackets denote concentration, and the exponents m and n are the **reaction orders** with respect to each reactant. The critical point — and the one that surprises many students — is that these orders must be determined experimentally. You cannot simply read them off the balanced equation's coefficients. A reaction like 2NO₂ → 2NO + O₂ might be second-order in NO₂, but it could also be first-order or zero-order; only experiments can tell you.

The standard experimental approach is the **method of initial rates**. You run the reaction multiple times, each time changing the starting concentration of only one reactant while holding the others constant, and measure the initial rate of each trial. By comparing how the rate changes when you change a concentration, you can deduce the order. If doubling [A] doubles the rate, the reaction is first-order in A (m = 1). If doubling [A] quadruples the rate, it is second-order in A (m = 2). If doubling [A] has no effect on the rate, it is zero-order in A (m = 0). You apply this logic to each reactant separately, then combine the results to write the complete rate law.

Once you know the orders, you can determine the rate constant k by substituting any one trial's data into the rate law and solving. The **overall reaction order** is the sum of the individual orders (m + n), and it determines the units of k — which is a useful check on your work. For a first-order reaction (overall order 1), k has units of s⁻¹; for second-order (overall order 2), k has units of M⁻¹s⁻¹. Each order also has a characteristic **integrated rate law** that describes how concentration changes over time: first-order gives exponential decay (ln[A] vs. t is linear), second-order gives 1/[A] vs. t as linear, and zero-order gives [A] vs. t as linear. Plotting your data in these different forms and seeing which gives a straight line is another way to determine order experimentally.

The deeper significance of rate laws is that they provide evidence about **reaction mechanisms** — the actual sequence of molecular-level steps by which reactants become products. The rate law reflects the slowest (rate-determining) step of the mechanism, not the overall balanced equation. This is precisely why you cannot deduce orders from stoichiometric coefficients: the balanced equation shows the net transformation but hides the stepwise molecular pathway. When the experimentally determined rate law matches the rate law predicted by a proposed mechanism's slow step, that is evidence (though not proof) that the mechanism is correct. This connection between macroscopic rate measurements and molecular-level events is one of the most powerful ideas in chemical kinetics.
