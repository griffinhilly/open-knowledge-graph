---
id: matching-estimators-causal-inference
title: 'Matching Estimators: Nearest Neighbor and Kernel Methods'
domain: economics
course: econometrics
prerequisites:
- id: propensity-score-methods
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
status: validated
---

# Matching Estimators: Nearest Neighbor and Kernel Methods

## Core Idea
Matching estimators (nearest neighbor, kernel, local polynomial) estimate treatment effects nonparametrically by comparing outcomes between treated and control units with similar covariates. These methods avoid functional form assumptions but require sufficient overlap in covariate distributions and careful choice of bandwidth or neighborhood size.

## Questions

```yaml
- question: "A researcher uses nearest-neighbor matching on age, education, and prior earnings to estimate the effect of a job training program. What assumption is required for this estimate to be causally valid?"
  type: multiple-choice
  options:
    - "The matched pairs must be exactly identical on all covariates — any distance in covariate space invalidates the comparison"
    - "Conditional on age, education, and prior earnings, assignment to the training program is as good as random — no unobserved variables jointly determine selection and outcomes"
    - "The training program must have been randomly assigned before the matching procedure was applied"
    - "The outcome variable must be uncorrelated with all measured covariates"
  answer: 1
  explanation: "Matching estimators are nonparametric — they avoid functional form assumptions — but they still require the conditional independence assumption (CIA): once you control for observed covariates, treatment assignment is as good as random. If there are unobserved confounders (e.g., motivation) that predict both who seeks training and later earnings, matching on observables cannot remove that bias. Matching is not a substitute for randomization; it is a way to approximate randomization when selection depends only on observed variables."

- question: "Compared to narrow-bandwidth kernel matching, wide-bandwidth kernel matching will tend to:"
  type: multiple-choice
  options:
    - "Decrease both bias and variance — more data is always better"
    - "Decrease variance (by averaging over more control units) but increase bias (by including control units that are genuinely dissimilar to the treated unit)"
    - "Increase variance because distant units introduce noise, with no effect on bias"
    - "Produce identical estimates — kernel matching is invariant to bandwidth choice"
  answer: 1
  explanation: "This is the classic bias-variance tradeoff in nonparametric estimation. A narrow bandwidth uses only very close control units as comparisons — these are genuinely similar (low bias), but there may be few of them (high variance). A wide bandwidth averages over many control units — reducing variance — but includes units with meaningfully different covariate values that may have different potential outcomes, introducing bias. Optimal bandwidth selection balances these two forces, typically by cross-validation or asymptotic bias/variance formulas."

- question: "Matching estimators can produce biased treatment effect estimates even when matching is done correctly, if there are unobserved variables that jointly determine both treatment assignment and outcomes."
  type: true-false
  answer: true
  explanation: "This is the core limitation of all matching methods (and of all selection-on-observables strategies). Matching eliminates bias due to observed confounders by constructing comparable treatment and control groups on measured characteristics. But if an unobserved variable — such as motivation, ability, or social connections — influences both who selects into treatment and what outcomes they achieve, the treated and control units are still systematically different in that unobserved dimension. No amount of careful matching on observables can remove bias from unobservables."

- question: "Because matching estimators are nonparametric, they require no identifying assumptions about the treatment assignment process — matching automatically produces causal estimates regardless of how units came to be treated."
  type: true-false
  answer: false
  explanation: "Nonparametric refers to not assuming a functional form for the outcome equation — not to freedom from identifying assumptions. Matching estimators still require the conditional independence assumption (CIA): given the observed covariates, treatment is as good as random. They also require the overlap (common support) condition: for every treated unit, comparable control units must exist. These identifying assumptions are the same as in propensity score matching; what matching estimators add is robustness to misspecification of the outcome model, not elimination of the need for a credible identification strategy."

- question: "What is the common support (overlap) requirement in matching, and what problem arises when it fails?"
  type: short-answer
  answer: "Common support requires that for every treated unit, there exist control units with similar covariate values — the covariate distributions of treated and control groups must overlap. When common support fails, some treated units have no genuine comparisons in the control group. The estimator must either extrapolate (comparing to distant, dissimilar control units, introducing bias), exclude those units (which changes the estimand — you are now estimating the treatment effect only for units with good matches, not for all treated units), or fail with very high variance. Failures of common support are often worst precisely for treated units at the extremes of the covariate distribution, where treatment effects may be largest."
  explanation: "The overlap condition is the matching analogue of the positivity assumption in causal inference: every unit must have some nonzero probability of receiving either treatment or control. Without it, counterfactual comparisons are not empirically grounded — you are asking 'what would this type of unit look like untreated?' when no untreated units of that type exist in the data. This is why comparing the covariate distributions of treated and control groups visually before estimating is a crucial diagnostic step."
```

## Explainer

From your prerequisite work on propensity score matching and treatment effect estimation, you know the fundamental causal inference problem: we observe each person in either the treated or control state, never both. The **counterfactual** — what a treated person's outcome would have been without treatment — must be constructed by finding appropriate comparisons in the control group. Propensity score matching compressed all the covariates into a single number (the predicted probability of treatment) and matched on that scalar. Matching estimators take a more direct approach: compare treated units to control units that look similar on the covariates themselves, without the intermediate step of modelling selection into treatment.

**Nearest neighbor matching** is the most intuitive version. For each treated unit, find the control unit (or k nearest control units) with the most similar covariate vector — "nearest" in some distance metric, typically Euclidean distance in covariate space or the Mahalanobis distance which accounts for correlations among covariates. The estimated treatment effect for that unit is the difference between its observed outcome and the average outcome of its matched controls. Aggregate across all treated units to get the **Average Treatment Effect on the Treated (ATT)**. The approach is nonparametric: you never specify how the outcome relates to the covariates. The estimate is driven purely by the comparison of similar units.

**Kernel matching** generalizes this by giving every control unit a weight when constructing the counterfactual for a treated unit, with weights declining as covariate distance grows. Rather than a sharp cutoff (take the k nearest neighbors), kernel matching uses a smooth weighting function. The **bandwidth** controls how quickly the weights decay: small bandwidth means only very close controls matter (low bias, high variance); large bandwidth averages over more controls (low variance, higher bias if distant controls are genuinely different). **Local polynomial matching** is a further refinement that fits a local regression surface to the control units' outcomes rather than simply averaging them, improving bias when covariates have real predictive power.

All matching estimators rest on the **conditional independence assumption (CIA)**: conditional on observed covariates, treatment assignment is as good as random. This is the same identifying assumption as propensity score matching — both require that you have measured all the variables that jointly determine selection and outcomes. Where matching methods add value is in robustness to misspecification: if you are wrong about the functional form linking covariates to outcomes, a parametric regression will be biased even if CIA holds, but a nonparametric matching estimator adjusts without needing the form specified. The cost is the **overlap requirement** — matching only works where there are control units comparable to treated units. If high-covariate-value treated units have no near-control counterparts (a failure of **common support**), estimates in those regions are unreliable or extrapolated, and the comparison between matching and regression estimates is itself a useful robustness diagnostic.
