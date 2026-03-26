---
id: propensity-score-analysis
title: Propensity Score Analysis
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: confounding-epidemiology
  type: hard
- id: multivariable-regression-epi
  type: hard
- id: propensity-score-methods-epidemiology
  type: soft
- id: mediation-analysis-pathways
  type: soft
builds-toward:
- inverse-probability-weighting
- g-estimation-causal-effects
tags:
- causal-inference
- confounding
- observational-studies
stage: expert
status: validated
---
# Propensity Score Analysis

## Core Idea
Propensity score analysis estimates the probability that an individual receives an exposure conditional on observed confounders. By matching, stratifying, or weighting on propensity scores, analysts can simulate randomization and reduce confounding bias in observational studies without explicitly adjusting for every confounder.

## How It's Best Learned
Start with a simple observational dataset and manually calculate propensity scores using logistic regression, then compare crude vs. adjusted estimates. Practice with real data using matching and weighting approaches in sequence.

## Common Misconceptions
- Propensity scores eliminate all confounding (they only control measured confounders). - Using propensity scores requires 1:1 matching (matching is one option; weighting and stratification are alternatives). - Overlap/common support is not required (perfect overlap is ideal but not always necessary).

## Questions

```yaml
- question: "A study uses propensity score matching to estimate the effect of a new medication on outcomes. After careful analysis, investigators achieve excellent covariate balance between matched treated and untreated patients. Which conclusion is warranted?"
  type: multiple-choice
  options:
    - "The analysis has effectively controlled for all confounding, and the estimate can be interpreted causally"
    - "Confounding due to the matched covariates has been reduced, but unmeasured confounders remain a threat to causal inference"
    - "The analysis is equivalent to a randomized trial and requires no further sensitivity analysis"
    - "Propensity score matching is superior to regression adjustment here because it requires no model for the outcome"
  answer: 1
  explanation: "Propensity scores balance measured covariates — 'excellent balance' confirms this worked. But unmeasured confounders are untouched; the identifying assumption (no unmeasured confounding / exchangeability) cannot be verified from balance checks alone. Option A is the most common over-claim. Option C is false: even a well-executed propensity score analysis is not equivalent to randomization, which also balances unmeasured confounders."

- question: "Which statement correctly distinguishes propensity score matching from inverse probability weighting (IPW)?"
  type: multiple-choice
  options:
    - "Matching and IPW make different causal assumptions; matching requires no unmeasured confounders while IPW does not"
    - "Matching discards unmatched subjects and estimates the effect in the matched sample; IPW retains all subjects by up-weighting surprising treatment assignments"
    - "Stratification is always preferred because it uses all subjects without altering their weights"
    - "IPW is the only method that achieves true covariate balance; matching and stratification only approximate it"
  answer: 1
  explanation: "All three methods rest on the same identifying assumption — no unmeasured confounding. The difference is implementation: matching pairs subjects by propensity score and discards unmatched ones; IPW keeps all subjects but assigns higher weights to those whose treatment assignment was 'surprising' given their covariates, creating a pseudo-population where treatment is independent of measured confounders. None is universally preferred — the choice depends on data structure and the causal estimand of interest."

- question: "Propensity score analysis eliminates the need for the 'no unmeasured confounding' assumption that is required in standard regression adjustment."
  type: true-false
  answer: false
  explanation: "This is the most important misconception about propensity scores. Both propensity score methods and regression adjustment require the same identifying assumption: all confounders are measured and included in the model. Propensity score analysis offers advantages in transparency, covariate balance checking, and handling high-dimensional covariates — but it does not address unmeasured confounding. It is a different tool, not a stronger one in terms of causal identification."

- question: "After propensity score matching, achieving near-zero standardized mean differences for most covariates is evidence that the propensity score model was correctly specified."
  type: true-false
  answer: false
  explanation: "Balance is a property of the matched sample, not proof of correct model specification. A misspecified propensity score model can still produce good balance on observed covariates in practice. Balance should always be checked, but good balance cannot rule out model misspecification — and more importantly, it says nothing about whether unmeasured confounders are balanced between groups."

- question: "Why can't propensity score analysis substitute for randomization, even when the analysis is perfectly executed?"
  type: short-answer
  answer: "Randomization ensures that both measured and unmeasured confounders are balanced between treatment groups, by design. Propensity score analysis can only balance measured confounders — variables that were recorded and included in the propensity score model. Any confounder absent from the data is untouched. Perfect execution means the measured confounders are well-balanced, but the identifying assumption (no unmeasured confounding) remains a substantive claim about the data-generating process that cannot be verified from the data."
  explanation: "This asymmetry is fundamental to observational research. Randomization buys unconditional independence between treatment and potential outcomes. Propensity scores buy conditional independence given measured covariates — but only if those covariates capture all confounding. The method's value is in transparency and sometimes better finite-sample performance relative to outcome regression, not in loosening the causal assumptions."
```

## Explainer

From your study of confounding and multivariable regression, you know the core problem in observational research: people who receive an exposure are systematically different from those who do not, and those differences — not the exposure itself — may explain the outcome. In a randomized trial, random assignment ensures that exposed and unexposed groups are on average identical on every measured and unmeasured characteristic. Propensity score analysis is an attempt to approximate that balance in observational data — but only for measured confounders.

The **propensity score** is the predicted probability that a subject received the exposure, given their observed covariates. You estimate it using logistic regression: outcome = exposure (1/0), predictors = all measured confounders (age, sex, comorbidities, socioeconomic status, etc.). The output is a single number between 0 and 1 for each subject. The intuition: two subjects with the same propensity score have the same probability of being exposed given their measured characteristics, so any actual difference in their exposure status looks like it could have been random. Conditioning on the propensity score therefore mimics randomization on the measured covariates — it "balances" the groups without requiring you to model the relationship between each individual confounder and the outcome.

There are three main implementation strategies. **Propensity score matching** pairs each exposed subject with one (or more) unexposed subjects who have a similar propensity score, then analyzes only the matched set. This is intuitive and produces a balanced sample but discards unmatched subjects, potentially reducing precision and generalizability. **Inverse probability weighting (IPW)** keeps all subjects but up-weights those whose treatment assignment was "surprising" (an exposed person with low propensity, or an unexposed person with high propensity). This creates a pseudo-population in which exposure is independent of the confounders, and you analyze it as if it were a randomized trial. **Stratification** divides subjects into quantiles of propensity score (typically quintiles) and estimates the exposure effect within each stratum, then pools. All three approaches require checking **balance** after adjustment — the measured confounders should be similar between groups within propensity score strata. Standardized mean differences are the standard check; a successful analysis should show differences near zero for all covariates.

The key limitation to internalize: propensity scores control only **measured** confounders. Unmeasured confounders remain unaddressed, just as in conventional regression. Propensity scores are not a substitute for randomization — they are a more transparent and sometimes more flexible tool for covariate adjustment than outcome regression, but they make the same identifying assumption: **no unmeasured confounding** (also called exchangeability or ignorability). Where propensity scores offer a genuine advantage over regression is in situations with many covariates relative to outcomes (where outcome models can overfit), or when the researcher wants to separate the "design" stage (building the balanced comparison groups) from the "analysis" stage (estimating effects), improving transparency about which decisions were made before examining outcomes. Understanding these tradeoffs prepares you for the more general methods — instrumental variables, g-estimation, and doubly robust estimators — that build directly on propensity score foundations.
