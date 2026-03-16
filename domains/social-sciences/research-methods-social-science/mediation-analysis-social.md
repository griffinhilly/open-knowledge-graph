---
id: mediation-analysis-social
title: Mediation and Indirect Effects Analysis
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: linear-regression-social-science
  type: hard
- id: research-design-advanced
  type: soft
- id: matrices-intro
  type: soft
- id: linear-regression
  type: soft
- id: partial-derivatives-basics
  type: soft
- id: partial-derivatives
  type: soft
builds-toward:
- conditional-indirect-effects
- dynamic-mediation-models
tags:
- mechanisms
- indirect-effects
- pathways
- causal-process
stage: advanced
status: draft
---

# Mediation and Indirect Effects Analysis

## Core Idea
Mediation analysis decomposes a causal effect into direct effects (X→Y) and indirect effects operating through a mediator (X→M→Y). Understanding mechanisms requires identifying the causal pathway through which an independent variable influences an outcome. Modern mediation analysis uses causal inference frameworks: the natural indirect effect (NIE) and direct effect (NDE) are defined under counterfactual logic, accounting for treatment-mediator interactions and sequential ignorability assumptions.

## Explainer

From your linear regression background, you know that regression estimates the average relationship between a predictor and an outcome while holding other variables constant. Mediation analysis takes the next step: instead of just asking *whether* X affects Y, it asks *how* — through what pathway does the effect travel? This distinction between "does it work?" and "how does it work?" is the difference between establishing an effect and understanding a mechanism.

The basic setup has three variables. You have an independent variable X (a treatment, policy, or cause), an outcome Y, and a **mediator** M — an intermediate variable that lies on the causal path from X to Y. For example: does attending college increase lifetime earnings (X→Y)? Part of that effect might operate directly (employers value degrees per se), and part might operate through the skills and networks college develops (X→M→Y). Mediation analysis partitions the total effect into these pieces. The **direct effect** is the effect of X on Y that does not go through M. The **indirect effect** is the portion that travels through M. The two sum to the total effect.

The classical approach (Baron and Kenny's "causal steps" procedure) estimated these pieces using a series of regression equations: regress M on X, regress Y on X and M, and interpret coefficients. The indirect effect equals the product of two coefficients — the effect of X on M and the effect of M on Y controlling for X. This product-of-coefficients approach is still the core computational intuition. But modern mediation analysis, built on the **counterfactual framework** you may recognize from causal inference, is considerably more demanding. It requires **sequential ignorability**: X must be effectively randomized (no unmeasured confounders of X→Y), and M must also be effectively randomized conditional on X (no unmeasured confounders of M→Y). In observational research, neither assumption is easily satisfied, which is why mediation claims from purely observational data are often overstated.

The modern definitions of the **natural direct effect** (NDE) and **natural indirect effect** (NIE) handle the case where X modifies the effect of M on Y — that is, when the pathway through M works differently depending on the value of X. In this interaction case, the simple product-of-coefficients formula gives misleading results; counterfactual definitions correctly partition the total effect. In practice, this means testing for X×M interactions and using bootstrapping to construct confidence intervals for indirect effects, since the product of two regression coefficients doesn't follow a simple known distribution. The upshot for applied research: mediation analysis is a powerful tool for investigating mechanisms, but its causal interpretation requires strong assumptions that should be stated explicitly and probed with sensitivity analyses rather than assumed away.
