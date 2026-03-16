---
id: matching-estimators-causal-inference
title: 'Matching Estimators: Nearest Neighbor and Kernel Methods'
domain: economics
course: econometrics
prerequisites:
- id: propensity-score-matching
  type: hard
- id: treatment-effect-estimation
  type: hard
builds-toward:
- difference-in-differences
tags:
- causal-inference
- matching
- nonparametric
stage: formal-systems
status: draft
---

# Matching Estimators: Nearest Neighbor and Kernel Methods

## Core Idea
Matching estimators (nearest neighbor, kernel, local polynomial) estimate treatment effects nonparametrically by comparing outcomes between treated and control units with similar covariates. These methods avoid functional form assumptions but require sufficient overlap in covariate distributions and careful choice of bandwidth or neighborhood size.

## Explainer

From your prerequisite work on propensity score matching and treatment effect estimation, you know the fundamental causal inference problem: we observe each person in either the treated or control state, never both. The **counterfactual** — what a treated person's outcome would have been without treatment — must be constructed by finding appropriate comparisons in the control group. Propensity score matching compressed all the covariates into a single number (the predicted probability of treatment) and matched on that scalar. Matching estimators take a more direct approach: compare treated units to control units that look similar on the covariates themselves, without the intermediate step of modelling selection into treatment.

**Nearest neighbor matching** is the most intuitive version. For each treated unit, find the control unit (or k nearest control units) with the most similar covariate vector — "nearest" in some distance metric, typically Euclidean distance in covariate space or the Mahalanobis distance which accounts for correlations among covariates. The estimated treatment effect for that unit is the difference between its observed outcome and the average outcome of its matched controls. Aggregate across all treated units to get the **Average Treatment Effect on the Treated (ATT)**. The approach is nonparametric: you never specify how the outcome relates to the covariates. The estimate is driven purely by the comparison of similar units.

**Kernel matching** generalizes this by giving every control unit a weight when constructing the counterfactual for a treated unit, with weights declining as covariate distance grows. Rather than a sharp cutoff (take the k nearest neighbors), kernel matching uses a smooth weighting function. The **bandwidth** controls how quickly the weights decay: small bandwidth means only very close controls matter (low bias, high variance); large bandwidth averages over more controls (low variance, higher bias if distant controls are genuinely different). **Local polynomial matching** is a further refinement that fits a local regression surface to the control units' outcomes rather than simply averaging them, improving bias when covariates have real predictive power.

All matching estimators rest on the **conditional independence assumption (CIA)**: conditional on observed covariates, treatment assignment is as good as random. This is the same identifying assumption as propensity score matching — both require that you have measured all the variables that jointly determine selection and outcomes. Where matching methods add value is in robustness to misspecification: if you are wrong about the functional form linking covariates to outcomes, a parametric regression will be biased even if CIA holds, but a nonparametric matching estimator adjusts without needing the form specified. The cost is the **overlap requirement** — matching only works where there are control units comparable to treated units. If high-covariate-value treated units have no near-control counterparts (a failure of **common support**), estimates in those regions are unreliable or extrapolated, and the comparison between matching and regression estimates is itself a useful robustness diagnostic.
