---
id: dsge-models
title: 'DSGE Models: Dynamic Stochastic General Equilibrium'
domain: economics
course: advanced-macroeconomics
prerequisites:
- id: new-keynesian-framework
  type: hard
- id: phillips-curve-new-keynesian
  type: hard
- id: constrained-optimization-lagrange
  type: soft
- id: eigenvalues-eigenvectors
  type: soft
- id: systems-of-first-order-linear-odes
  type: hard
- id: eigenvalues-and-eigenvectors
  type: hard
- id: linear-transformations
  type: soft
- id: systems-of-linear-equations
  type: soft
- id: matrix-operations
  type: soft
builds-toward:
- monetary-policy-transmission
- fiscal-multipliers-macro
tags:
- dsge
- general-equilibrium
- stochastic
stage: advanced
status: draft
---

# DSGE Models: Dynamic Stochastic General Equilibrium

## Core Idea
DSGE models integrate microeconomic optimization with macroeconomic outcomes under uncertainty. Households and firms solve dynamic problems subject to constraints and expectations; aggregate equilibrium clears markets while agents are subject to exogenous shocks. DSGE models allow simulation of policy experiments and analysis of how shocks propagate through the economy. They form the baseline framework for modern central bank analysis of monetary policy and represent the state-of-the-art tool for macroeconomic forecasting and policy evaluation.

## Questions

```yaml
- question: "A central bank wants to evaluate how GDP and inflation would respond if it adopted a more aggressive interest rate rule. A colleague suggests using a DSGE model instead of a historical VAR model. What is the main advantage of the DSGE approach for this specific question?"
  type: multiple-choice
  options:
    - "DSGE models are more accurate because they incorporate more historical data"
    - "DSGE models are built from optimization problems, so their structure doesn't change when the policy rule changes"
    - "DSGE models are simpler and faster to estimate than reduced-form models"
    - "DSGE models use machine learning to identify causal relationships from observed patterns"
  answer: 1
  explanation: "This is the Lucas critique in action. Reduced-form VAR models estimate statistical relationships from historical behavior under the *existing* policy rule. If the rule changes, agents adjust their behavior, invalidating those historical correlations. DSGE models derive behavioral equations from household and firm optimization, so agent behavior is re-derived for any policy rule — the model's structure doesn't assume the old rule will continue. This is why central banks use DSGE models specifically for policy experiments."

- question: "After log-linearizing a DSGE model, an economist finds that the matrix A has 3 explosive eigenvalues. The model has 2 forward-looking (jump) variables. What do the Blanchard-Kahn conditions imply?"
  type: multiple-choice
  options:
    - "The model has a unique stable solution — more explosive eigenvalues ensure faster convergence"
    - "The model is indeterminate — too few explosive eigenvalues relative to jump variables"
    - "The model has no stable solution — there are more explosive eigenvalues than forward-looking variables"
    - "The eigenvalue count is irrelevant; only the sign of the largest eigenvalue matters"
  answer: 2
  explanation: "The Blanchard-Kahn conditions require the number of explosive eigenvalues to equal the number of forward-looking variables exactly. Here 3 explosive eigenvalues exceed 2 forward-looking variables — the 'too many' case, which means no stable solution exists. If there were too few explosive eigenvalues (fewer than jump variables), the solution would be indeterminate (infinitely many). This is a direct application of eigenvalue analysis: the model's solvability depends on the spectral structure of A."

- question: "A DSGE model's behavioral equations remain valid for policy analysis even after a major policy regime change."
  type: true-false
  answer: true
  explanation: "This is precisely the appeal of DSGE models. Because behavioral equations come from household utility maximization and firm profit maximization — not from fitting historical data under a specific regime — they reflect deep structural parameters (preferences, technology) that don't change when policy changes. A new Taylor rule changes only the policy block; the Euler equation and Phillips curve are re-derived from the same optimization, not re-estimated. This is what makes DSGE models uniquely suited for policy experiments."

- question: "The 2008 financial crisis confirmed that standard DSGE models were well-specified for capturing systemic financial risk."
  type: true-false
  answer: false
  explanation: "The crisis exposed critical limitations. Standard DSGE models with representative agents cannot capture heterogeneous household balance sheets or wealth inequality. Rational expectations frameworks struggle with the sudden belief shifts that characterize crises. Most importantly, financial frictions were omitted — the standard model treated the financial sector as a veil that didn't affect real outcomes. The crisis catalyzed research into models with financial frictions (Bernanke-Gertler-Gilchrist) and heterogeneous agents (HANK), precisely because the standard framework missed what mattered most."

- question: "What is the Lucas critique, and why do DSGE models claim to be immune to it?"
  type: short-answer
  answer: "The Lucas critique argues that reduced-form econometric models estimated under one policy regime fail when policy changes, because agents adjust their behavior to the new rule, invalidating historical correlations. DSGE models claim immunity because they derive behavioral equations from explicit optimization — households maximize lifetime utility, firms maximize profits — so the equations reflect structural preferences and technology, not policy-dependent patterns. When the policy rule changes in the model, only the policy block changes; household and firm equations remain valid because they come from the same optimization problem regardless of the rule."
  explanation: "The key distinction is between 'structural' parameters (preference curvature, production technology) that are policy-invariant, and 'reduced-form' correlations that shift with policy. DSGE models are structural in this sense. The caveat: immunity holds only if the structural assumptions are correct. Mis-specified structural forms (wrong utility function, wrong market structure) produce their own bias that survives regime changes — the model is structurally wrong rather than structurally right but policy-sensitive."
```

## Explainer

You already know the New Keynesian framework and the Phillips curve relationship between inflation and output. DSGE models are the formal machinery that makes these ideas rigorous and quantitatively operational. The name itself is the roadmap: **Dynamic** means agents make decisions over time, weighing today against tomorrow. **Stochastic** means the economy is hit by random shocks — technology changes, oil price spikes, shifts in consumer confidence. **General Equilibrium** means all markets (goods, labor, bonds) clear simultaneously, and every agent's choices are consistent with every other agent's choices.

A canonical DSGE model has three blocks. The **household block** specifies a representative consumer who maximizes lifetime utility over consumption and leisure, subject to a budget constraint. This yields an Euler equation — the intertemporal optimality condition you know from constrained optimization — linking today's consumption to expected future consumption and the real interest rate. The **firm block** specifies producers who set prices, often with Calvo-style staggered pricing (only a random fraction of firms can adjust prices each period), generating the New Keynesian Phillips curve as an equilibrium relationship. The **policy block** specifies a central bank following a Taylor-type rule, raising interest rates when inflation or output exceeds target. Together, these three blocks — typically expressed as a system of linearized difference equations — fully determine the dynamic response of output, inflation, and interest rates to any shock.

Solving the model requires the linear algebra from your prerequisites. After log-linearizing around a steady state, the model reduces to a system of the form **E_t[x_{t+1}] = A·x_t + B·ε_t**, where x is the vector of state variables and ε represents shocks. The eigenvalues of the matrix A determine whether the system has a unique stable solution — the **Blanchard-Kahn conditions** require exactly as many explosive eigenvalues as there are forward-looking (jump) variables. This is where your knowledge of eigenvalues and systems of linear equations pays off directly: checking these conditions and computing impulse response functions is fundamentally an exercise in matrix algebra.

The power of DSGE models lies in **counterfactual policy analysis**. Because the model is built from optimization problems, its structure does not change when policy changes — unlike reduced-form statistical models, which suffer from the Lucas critique. You can ask: "What would happen to inflation if the central bank responded more aggressively to output gaps?" and get an answer that accounts for how households and firms would adjust their behavior to the new rule. This is why central banks from the Federal Reserve to the ECB maintain large DSGE models as core tools. The limitation is that the models' predictions are only as good as their assumptions — the representative agent, rational expectations, and specific functional forms — and the 2008 crisis exposed how much standard DSGE models missed by omitting financial frictions and heterogeneous agents.
