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
stage: advanced
status: draft
---

# Rate Laws and Reaction Order Determination

## Core Idea
A rate law relates reaction rate to reactant concentrations: rate = k[A]^m[B]^n, where m and n are orders determined experimentally (not from stoichiometry). Overall order is m + n. Zero-order reactions have constant rate; first-order rates depend linearly on concentration; second-order rates depend on concentration squared. Rate laws reveal reaction mechanism insights.

## Explainer

A **rate law** is a mathematical equation that tells you exactly how the speed of a reaction depends on the concentrations of the reactants. For a reaction involving reactants A and B, the rate law takes the form rate = k[A]^m[B]^n, where k is the **rate constant** (which depends on temperature), the square brackets denote concentration, and the exponents m and n are the **reaction orders** with respect to each reactant. The critical point — and the one that surprises many students — is that these orders must be determined experimentally. You cannot simply read them off the balanced equation's coefficients. A reaction like 2NO₂ → 2NO + O₂ might be second-order in NO₂, but it could also be first-order or zero-order; only experiments can tell you.

The standard experimental approach is the **method of initial rates**. You run the reaction multiple times, each time changing the starting concentration of only one reactant while holding the others constant, and measure the initial rate of each trial. By comparing how the rate changes when you change a concentration, you can deduce the order. If doubling [A] doubles the rate, the reaction is first-order in A (m = 1). If doubling [A] quadruples the rate, it is second-order in A (m = 2). If doubling [A] has no effect on the rate, it is zero-order in A (m = 0). You apply this logic to each reactant separately, then combine the results to write the complete rate law.

Once you know the orders, you can determine the rate constant k by substituting any one trial's data into the rate law and solving. The **overall reaction order** is the sum of the individual orders (m + n), and it determines the units of k — which is a useful check on your work. For a first-order reaction (overall order 1), k has units of s⁻¹; for second-order (overall order 2), k has units of M⁻¹s⁻¹. Each order also has a characteristic **integrated rate law** that describes how concentration changes over time: first-order gives exponential decay (ln[A] vs. t is linear), second-order gives 1/[A] vs. t as linear, and zero-order gives [A] vs. t as linear. Plotting your data in these different forms and seeing which gives a straight line is another way to determine order experimentally.

The deeper significance of rate laws is that they provide evidence about **reaction mechanisms** — the actual sequence of molecular-level steps by which reactants become products. The rate law reflects the slowest (rate-determining) step of the mechanism, not the overall balanced equation. This is precisely why you cannot deduce orders from stoichiometric coefficients: the balanced equation shows the net transformation but hides the stepwise molecular pathway. When the experimentally determined rate law matches the rate law predicted by a proposed mechanism's slow step, that is evidence (though not proof) that the mechanism is correct. This connection between macroscopic rate measurements and molecular-level events is one of the most powerful ideas in chemical kinetics.
