---
id: propensity-score-methods-research-methods-social-science
title: Propensity Score Methods
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: causal-inference-observational-data
  type: hard
- id: logistic-regression-binary-outcomes
  type: hard
- id: probability-distributions
  type: hard
- id: conditional-distributions-of-random-variables
  type: hard
- id: probability-mass-functions
  type: soft
- id: conditional-probability
  type: soft
- id: probability-axioms
  type: soft
- id: logistic-regression-binary-categorical
  type: soft
- id: probability-density-functions
  type: hard
tags:
- propensity-score
- matching
- stratification
- weighting
stage: expert
status: draft
---

# Propensity Score Methods

## Core Idea
Introduces propensity score methods to balance treatment and control groups in observational studies by matching on probability of treatment. Covers PS estimation, matching algorithms (1:1, caliper, replacement), stratification, inverse probability weighting, and sensitivity analysis for hidden bias.

## How It's Best Learned
Estimate propensity scores, create balance diagnostics before/after matching, try different matching algorithms, conduct sensitivity analysis with hidden bias parameters.

## Common Misconceptions
- Matching on propensity scores solves confounding
- Perfect balance is achievable and necessary
- Propensity score matching always improves inference

## Questions

```yaml
- question: "A researcher matches treated and control participants on their propensity scores, achieves excellent balance on all measured covariates, and concludes she has eliminated confounding. What untestable assumption is her causal interpretation resting on?"
  type: multiple-choice
  options:
    - "That her logistic regression model for the propensity score has a sufficiently high C-statistic"
    - "That the treated and control groups are equal in size after matching"
    - "That there are no unobserved variables that predict both treatment selection and the outcome (conditional independence)"
    - "That propensity scores were estimated on the log-odds scale rather than the probability scale"
  answer: 2
  explanation: "Propensity score matching removes bias from *observed* confounders only. The conditional independence assumption — also called ignorability — states that treatment assignment is independent of potential outcomes given the observed covariates. If unobserved variables (e.g., motivation, social connections) predict both who receives treatment and what outcomes they would have, those biases persist after matching. This assumption is untestable from the data itself, which is why sensitivity analysis (Rosenbaum bounds) is essential: it asks how strong an unobserved confounder would need to be to overturn the conclusion."

- question: "A propensity score model includes many covariates and achieves excellent predictive accuracy (AUC = 0.94) but shows poor covariate balance in diagnostic checks. What should the researcher conclude and do?"
  type: multiple-choice
  options:
    - "The model is excellent; AUC of 0.94 indicates strong causal identification"
    - "The goal of propensity score estimation is covariate balance, not predictive accuracy — high AUC can indicate near-perfect separation that makes matching impossible, so the model should be revised"
    - "Switch to inverse probability weighting, which performs better when AUC is high"
    - "Add more covariates to increase AUC toward 1.0 for better balance"
  answer: 1
  explanation: "This is the central paradox of propensity score estimation. A high-AUC model means the model can perfectly predict who received treatment — which often means propensity scores are pushed toward 0 and 1 (near-perfect separation). These extreme scores create poor overlap between treated and control groups, making good matches impossible and IPW unstable. The goal is adequate covariate balance (measured by standardized mean differences), not predictive accuracy. Sometimes dropping covariates that perfectly predict treatment improves balance and downstream causal inference."

- question: "By default, propensity score matching estimates the average treatment effect on the treated (ATT) — the effect for those who actually received treatment — rather than the average treatment effect (ATE) for the full population."
  type: true-false
  answer: true
  explanation: "1:1 nearest-neighbor matching finds comparison units for treated units, which means the estimand is naturally the ATT: what was the effect of treatment for the treated group? This is often the policy-relevant question ('was this program effective for the people it actually served?') but it is not the same as ATE ('what would happen if we assigned everyone to treatment?'). To estimate ATE, you need comparison units that represent the untreated population, which may require different matching strategies or IPW targeting ATE rather than ATT."

- question: "Propensity score matching eliminates the need for sensitivity analysis because conditioning on observed covariates removes the threat of hidden confounding."
  type: true-false
  answer: false
  explanation: "This is the most dangerous misconception about propensity scores. Conditioning on observed covariates only balances those covariates — it cannot address unobserved variables that predict both treatment and outcome. The conditional independence assumption (no hidden confounders) is untestable from the data, so the researcher cannot know whether it holds. Sensitivity analysis (Rosenbaum bounds) is essential precisely because it quantifies how much hidden bias would be needed to overturn the finding. A fragile finding — one that would be overturned by a small unobserved confounder — should be interpreted with much more caution."

- question: "Why is the goal of propensity score estimation covariate balance rather than predictive accuracy, and how does this affect model-building strategy?"
  type: short-answer
  answer: "The purpose of the propensity score is not to predict treatment accurately but to create a matched or weighted sample in which treated and control groups look similar on observed covariates — mimicking the balance that randomization would produce. A high-accuracy model can actually hurt this goal if it achieves accuracy by identifying variables that perfectly separate treated from control units (poor overlap), making good matches impossible. Model-building strategy should be guided by balance diagnostics: estimate propensity scores, check standardized mean differences before and after matching, revise the model if balance is inadequate, and iterate. The model is a means to balance, not an end in itself."
  explanation: "This reframing — from 'predict treatment' to 'achieve balance' — changes what 'a good model' means entirely. Adding irrelevant predictors that happen to separate groups will increase AUC but harm balance and downstream causal inference. The workflow is diagnostic and iterative: balance checks should be run after each modeling choice, not just at the end."
```

## Explainer

From your study of causal inference in observational data, you know the central problem: people select into treatments for reasons correlated with outcomes, creating confounding. In a randomized experiment, random assignment breaks this link — treated and control groups are balanced on all variables, observed and unobserved. In observational studies you cannot randomize, so the goal is to construct a comparison that mimics what randomization would have produced. **Propensity score methods** are one strategy for doing this by balancing observed covariates between treatment and control groups.

The **propensity score** is a single summary: the probability that a unit receives treatment given its observed covariates, P(T=1 | X). You already know how to estimate this — it is a logistic regression predicting treatment assignment from the set of confounding variables. The crucial theoretical result (Rosenbaum and Rubin, 1983) is that if you condition on the propensity score, treatment assignment is independent of the covariates — you don't need to match or control for each covariate separately. Instead of finding an exact match in a high-dimensional covariate space, you collapse the problem to one dimension. This dimension-reduction property is what makes propensity scores practically valuable.

There are four main ways to use the propensity score. **1:1 nearest-neighbor matching** pairs each treated unit to the control unit with the closest propensity score; **caliper matching** restricts matches to be within a fixed distance of each other, improving balance at the cost of dropping poor matches; **stratification** divides the propensity score into quantiles and compares outcomes within strata; **inverse probability weighting (IPW)** re-weights the sample so that the distribution of covariates in the weighted comparison group mirrors the treated group. Each approach makes different tradeoffs between bias reduction, variance, and sample retention. IPW retains the full sample but can be unstable when propensity scores are very close to 0 or 1 — a problem sometimes addressed by trimming or stabilizing weights.

**Balance diagnostics** are essential and should drive your workflow: estimate propensity scores, check balance (via standardized mean differences and overlap plots), revise the model if balance is poor, then check balance again. The goal is not a high-accuracy propensity score model — it is adequate covariate balance. Paradoxically, adding more predictors to the propensity model doesn't always improve balance, and can sometimes hurt it. The estimand also matters: propensity matching estimates the **average treatment effect on the treated (ATT)** by default — what the effect of treatment was for those who actually received it — rather than the average treatment effect (ATE) for the whole population.

The deepest limitation is the **conditional independence assumption** (also called ignorability or no hidden confounding): treatment assignment is independent of potential outcomes given observed covariates. This assumption is untestable from the data. If there are unobserved confounders — variables that predict both treatment and outcome — propensity score matching does not eliminate the bias from those variables. **Sensitivity analysis** (Rosenbaum bounds) asks how strong an unobserved confounder would need to be to overturn your conclusion. A finding that is sensitive to small departures from ignorability should be treated as fragile. Propensity score methods are not a substitute for a good research design; they are a tool for squeezing the most valid inference from observational data given the design you have.
