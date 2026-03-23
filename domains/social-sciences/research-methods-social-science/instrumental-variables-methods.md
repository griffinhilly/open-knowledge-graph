---
id: instrumental-variables-methods
title: Instrumental Variables Estimation
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: causal-inference-observational-data
  type: hard
- id: linear-regression-social-science
  type: hard
- id: matrix-inverses
  type: hard
- id: linear-systems-notation
  type: hard
- id: matrices-intro
  type: soft
- id: linear-transformation-definition
  type: soft
- id: linear-regression
  type: hard
- id: matrix-multiplication
  type: hard
tags:
- instrumental-variables
- endogeneity
- two-stage-least-squares
- IV-validity
stage: expert
status: draft
---

# Instrumental Variables Estimation

## Core Idea
Introduces instrumental variables as a solution to endogeneity when confounders are unobserved. Covers IV assumptions (relevance, exclusion restriction), two-stage least squares estimation, instrument validity testing, and weak instrument problems with examples from social research.

## How It's Best Learned
Identify potential instruments in published studies, design IV estimations with real data, test instrument strength and validity assumptions, practice interpreting TSLS results.

## Common Misconceptions
- Valid instruments are easy to find
- Relevance is testable but exclusion restriction is not
- Any variable correlated with treatment can be an instrument

## Questions

```yaml
- question: "A researcher uses a patient's distance from the nearest hospital as an instrument for whether they received a surgical procedure, aiming to estimate the procedure's causal effect on survival. Distance correlates strongly with procedure receipt. What is the most important assumption that must hold — and cannot be statistically verified?"
  type: multiple-choice
  options:
    - "Distance must be uncorrelated with the procedure itself, so that it only affects survival directly"
    - "Distance must affect survival only through whether the patient received the procedure, not through any other channel"
    - "Distance must be randomly assigned across patients, like a lottery"
    - "Distance must be measured without error to avoid attenuation bias in the first stage"
  answer: 1
  explanation: "This is the exclusion restriction — the instrument must affect the outcome only through the treatment. Distance could plausibly violate this: patients farther from hospitals might also live in rural areas with worse diet, less emergency care access, or delayed diagnoses, affecting survival through channels other than whether they received this particular procedure. This assumption cannot be tested statistically — it must be defended with theory and contextual knowledge. The relevance assumption (distance predicts procedure receipt) CAN be tested with an F-statistic."

- question: "A study uses two-stage least squares (2SLS) to estimate the effect of military service on lifetime earnings, using Vietnam draft lottery numbers as the instrument. The IV estimate is 0.15 (15% earnings reduction per year of service). What does this number represent?"
  type: multiple-choice
  options:
    - "The average effect of military service on earnings for all men in the draft-eligible cohort"
    - "The average effect of military service on earnings for men whose service status was actually changed by their lottery number"
    - "The effect of a one-unit increase in lottery number on lifetime earnings"
    - "The total earnings effect for the full population of veterans, controlling for observable confounders"
  answer: 1
  explanation: "IV estimates the Local Average Treatment Effect (LATE) — the causal effect only for 'compliers': men who served because they got a low lottery number and would not have served otherwise. Men who would have served regardless of their number ('always-takers') and men who never served regardless ('never-takers') are not identified by the instrument. The LATE may differ substantially from the Average Treatment Effect (ATE) for the full population, which is why external validity must always be discussed in IV studies."

- question: "The relevance assumption in instrumental variables — that the instrument is correlated with the treatment — can be empirically tested."
  type: true-false
  answer: true
  explanation: "Yes — relevance is testable. You regress the treatment variable on the instrument in the first stage and examine the F-statistic. The conventional rule of thumb is F > 10; instruments with F < 10 are 'weak' and produce IV estimates that are biased toward the OLS estimate and have unreliable confidence intervals. The exclusion restriction, by contrast, is fundamentally untestable — you cannot observe all the pathways through which an instrument might affect the outcome, so it must be argued on substantive grounds."

- question: "When a valid instrument exists, the IV estimator recovers the same causal parameter as a randomized controlled trial with full compliance — that is, the average treatment effect (ATE) for the entire target population."
  type: true-false
  answer: false
  explanation: "IV estimates the Local Average Treatment Effect (LATE), not the ATE. It identifies the causal effect only for 'compliers' — the subgroup whose treatment status changes in response to the instrument. A randomized trial with full compliance estimates the ATE for the full sample. LATE and ATE coincide only in the special case where treatment effects are homogeneous (the same for everyone). In practice, compliers are often a specific subpopulation (e.g., draft lottery compliers are men with low lottery numbers on the margin of service), limiting generalizability."

- question: "Why is it problematic to use a variable that is correlated with the treatment as an instrument, even if it is strongly correlated, without verifying the exclusion restriction?"
  type: short-answer
  answer: "A strong correlation with treatment only satisfies relevance — one of two requirements. The exclusion restriction requires the instrument to affect the outcome solely through the treatment. If the instrument also affects the outcome through other pathways (direct effects or through unmeasured confounders), the IV estimate is biased — it no longer isolates the causal effect of treatment, instead picking up the instrument's own direct effect on the outcome. Strong relevance with a violated exclusion restriction can give precise but deeply wrong estimates, which may be worse than a confounded OLS estimate."
  explanation: "Many variables are correlated with treatment and seem like convenient instruments without actually satisfying the exclusion restriction. Socioeconomic indicators, geographic variables, and birth-date proxies often have multiple causal pathways to the outcome. The discipline of IV analysis is largely the discipline of constructing a credible argument that the exclusion restriction holds — and recognizing when no such argument is available."
```

## Explainer

You already know from linear regression that the ordinary least squares (OLS) estimator finds the line minimizing prediction error. And from causal inference in observational data, you know the central problem: OLS gives unbiased estimates *only* if the error term is uncorrelated with the treatment variable. When unmeasured confounders simultaneously affect the treatment and outcome, the regression coefficient is **endogenous** — it captures both the causal effect and the confounding, making it impossible to isolate either from the other.

The **instrumental variables (IV)** strategy solves this by finding a third variable — the **instrument** — that affects the treatment but affects the outcome *only through* the treatment. Think of a natural experiment: the Vietnam War draft lottery assigned military service by birth date. Birth date is essentially random with respect to earnings (it's not a confounder), yet it affected who served. Economists use birth date as an instrument for military service to estimate the causal effect of service on lifetime earnings. The instrument creates exogenous variation in the treatment — variation not contaminated by unobserved confounders.

This logic formalizes into two conditions. **Relevance** means the instrument must actually predict the treatment — the correlation between instrument and treatment must be nonzero and ideally strong. You can test this: regress treatment on instrument and check the F-statistic; a rule of thumb is F > 10. **The exclusion restriction** says the instrument affects the outcome only through the treatment, not through any other channel. This is *untestable* — it must be defended on theoretical and contextual grounds. A weak exclusion restriction argument is the most common fatal flaw in IV studies.

**Two-Stage Least Squares (2SLS)** is the standard estimator. In stage 1, regress treatment on the instrument to extract only the exogenous variation in treatment. In stage 2, regress outcome on the stage-1 fitted values — the "clean" part of treatment variation. The matrix algebra you know makes this tractable: the 2SLS estimator is (Z'X)⁻¹Z'y, where Z is the instrument matrix, X the treatment, and y the outcome. In practice, software handles this, but understanding the algebra clarifies what's being estimated: only the variation in treatment driven by the instrument identifies the causal effect.

There is a crucial limitation: IV estimates **Local Average Treatment Effects (LATE)** — the causal effect only for the subgroup whose treatment status was actually changed by the instrument (called "compliers"). People who always take the treatment regardless of the instrument, or never do regardless, are not informative for the 2SLS estimate. This means IV findings may not generalize to the full population. The tradeoff is real: IV gives you cleaner causal identification than OLS, but at the cost of estimating an effect for a sometimes-narrow, sometimes-uncharacterized subgroup.
