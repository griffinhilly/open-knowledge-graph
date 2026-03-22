---
id: panel-data-fixed-effects
title: Fixed and Random Effects Models
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: longitudinal-data-analysis
  type: hard
- id: multilevel-modeling-hierarchical
  type: soft
- id: linear-regression
  type: hard
builds-toward:
- dynamic-panel-models
- system-gmm-estimators
tags:
- panel-methods
- causal
- confounding
- estimators
stage: advanced
status: draft
---

# Fixed and Random Effects Models

## Core Idea
Fixed-effects estimators use within-unit variation to identify causal effects while removing time-invariant confounds (e.g., personality, geographic characteristics). Random-effects models assume unit-level heterogeneity is uncorrelated with predictors, allowing estimation of between-unit and within-unit effects. The choice between fixed and random effects depends on research assumptions: fixed effects trades precision for robustness when time-invariant confounds are suspected.

## Questions

```yaml
- question: "A researcher wants to estimate the effect of sleep quality on academic performance using a panel dataset of students observed over four semesters. She suspects that students' baseline conscientiousness — a time-invariant trait — is correlated with both sleep habits and grades. Which estimator should she prefer?"
  type: multiple-choice
  options:
    - "Random effects — it is more efficient and uses all available variation"
    - "Fixed effects — it eliminates all time-invariant confounders including conscientiousness"
    - "Ordinary least squares — it uses the most data and is unbiased if controls are included"
    - "Random effects — it estimates both between- and within-student effects simultaneously"
  answer: 1
  explanation: "When time-invariant confounders are suspected to be correlated with the predictor, fixed effects is the appropriate choice. By estimating the effect from within-student variation only — comparing each student to themselves across semesters — the fixed-effects model eliminates conscientiousness and every other stable trait that might bias the estimate. Random effects (options A and D) requires that the unit-level heterogeneity (conscientiousness) be uncorrelated with the predictor (sleep quality), an assumption that is almost certainly violated here. OLS (option C) does nothing to address the omitted variable."

- question: "A researcher runs a fixed-effects panel regression on a dataset of workers and finds no estimated effect for 'biological sex' on wages. What is the most likely explanation?"
  type: multiple-choice
  options:
    - "Sex has no effect on wages — the fixed-effects model has correctly identified this"
    - "The model is misspecified; sex should be included as an interaction term instead"
    - "Sex is a time-invariant variable and is absorbed into the unit fixed effects, making its coefficient unidentifiable"
    - "The sample size is too small to detect the effect of sex"
  answer: 2
  explanation: "Fixed-effects models eliminate all variation that does not change within units over time. Since biological sex is time-invariant for virtually all workers in a typical sample, it is perfectly collinear with the unit fixed effects and drops out of the estimation. This is not a substantive finding — it is a mechanical consequence of the estimator. If the researcher wants to estimate the effect of time-invariant variables, they must use random effects (with its stronger assumptions) or a different research design such as an instrumental variables approach."

- question: "A fixed-effects model eliminates all forms of omitted variable bias, making it the gold standard estimator for causal inference in panel data."
  type: true-false
  answer: false
  explanation: "Fixed effects eliminates bias from time-invariant confounders only — characteristics of the unit that do not change over the observation period. Time-varying confounders (variables that change within units and are correlated with both the predictor and outcome) are not addressed by fixed effects. For example, if workers' motivation fluctuates over time in ways that also affect their training participation and earnings, fixed effects does not remove that bias. Fixed effects is a powerful tool against one specific class of confounding, not a general solution to all causal inference problems."

- question: "Random-effects models produce biased estimates when unit-level heterogeneity is correlated with the predictors in the model."
  type: true-false
  answer: true
  explanation: "This is the critical assumption underlying random-effects estimation. The random-effects model treats unit-level heterogeneity as a random variable drawn from a distribution, rather than estimating a separate intercept per unit. This gains efficiency but requires that the random unit effect be uncorrelated with the predictors. When this assumption is violated — as it often is in social science, where stable individual traits simultaneously influence predictor assignment and outcomes — random-effects estimates are inconsistent in the same way as ordinary regression with omitted variables. The Hausman test detects this by comparing fixed and random effects estimates."

- question: "What is the Hausman test and when should it lead you to prefer fixed effects over random effects?"
  type: short-answer
  answer: "The Hausman test compares the coefficient estimates from fixed and random effects models. Under the null hypothesis that random effects is appropriate (i.e., unit-level heterogeneity is uncorrelated with predictors), both estimators should yield similar estimates. If the estimates differ substantially, the random-effects assumption is violated — the unit effects are correlated with the predictors — and fixed effects is preferred because it remains consistent under that violation. When the Hausman test rejects the null, random effects estimates are biased; fixed effects, though less efficient, gives the correct causal estimate from within-unit variation."
  explanation: "The intuition is that fixed effects is always consistent when unit-level variation is the concern, but costs precision by discarding between-unit variation. Random effects is more efficient but adds the strong assumption that the unit effects are exogenous. The Hausman test uses the difference in estimates as a diagnostic: if fixed and random effects agree closely, the exogeneity assumption is plausible and random effects is fine. If they diverge, something the unit fixed effects are absorbing is correlated with the predictor — and you need fixed effects to get an unbiased answer."
```

## Explainer

You already know from linear regression that omitted variables bias coefficient estimates — if a variable is correlated with both your predictor and your outcome, and you leave it out, your estimate is wrong. From longitudinal data analysis, you know that panel data tracks the same units over time. Fixed-effects models exploit that panel structure to eliminate an entire category of omitted variable bias: everything about a unit that does not change over time.

To see why, imagine you want to estimate the effect of job training programs on earnings, using a dataset of workers observed over five years. The problem is that motivated workers might both seek out training and have higher earnings regardless. Motivation is a confound — and it is very hard to measure directly. A **fixed-effects** model handles this by, in effect, giving each worker their own intercept. The estimation is done entirely from *changes within each worker over time*. Did workers earn more in years when they had training compared to years when they did not? Motivation, ability, and every other stable individual characteristic cancel out because they affect all observations for that worker equally. What remains is the within-worker variation — the signal you actually want.

The mechanics translate to your regression knowledge: a fixed-effects model is equivalent to including a dummy variable for every unit (or equivalently, demeaning all variables by subtracting each unit's mean). The coefficient on your predictor of interest then captures the within-unit effect. The cost is that you cannot estimate effects of any variable that does not change within units — time-invariant variables like gender or country of birth are absorbed into the unit fixed effects and disappear from the estimation. You also need enough within-unit variation; if training status rarely changes for most workers, you have little data to identify the effect.

**Random effects** models take a different approach: they model the unit-level heterogeneity as a random variable drawn from a distribution, rather than estimating a separate parameter for each unit. This allows you to estimate effects of time-invariant variables and produces more precise estimates — but only if the unit-level heterogeneity is *uncorrelated* with your predictors. In the training example, that means assuming workers' motivation is unrelated to whether they receive training. If that assumption is wrong (and it usually is in social science), random effects estimates are biased in the same way as ordinary regression. The **Hausman test** formalizes this choice: it compares fixed and random effects estimates, and if they differ substantially, the random effects assumption is violated and fixed effects is preferred.

The deeper insight is that fixed effects is not really a "model" in the usual sense — it is a research design choice about which variation to use. By restricting attention to within-unit variation and discarding between-unit variation, you gain protection against a broad class of confounds at the cost of external generalizability. A fixed-effects estimate tells you what happened *within* observed units over time, not necessarily what would happen in a new unit. Understanding this scope condition — what the estimate does and does not represent — is as important as understanding how to run the estimator.
