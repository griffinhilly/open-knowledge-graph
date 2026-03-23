---
id: marginal-structural-models
title: Marginal Structural Models for Longitudinal Data
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: time-varying-confounders
  type: hard
- id: inverse-probability-weighting
  type: hard
tags:
- longitudinal-analysis
- marginal-models
- causal-inference
- time-varying-treatment
stage: expert
status: draft
---

# Marginal Structural Models for Longitudinal Data

## Core Idea
Marginal structural models estimate causal effects of time-varying exposures on outcomes in the presence of time-varying confounding affected by prior exposure. MSMs use inverse probability weighting of observed outcomes on exposure history, producing marginal treatment effects analogous to those from a randomized experiment following the observed exposure pattern.

## Questions

```yaml
- question: "In an HIV cohort study, CD4 count is measured at every visit. CD4 predicts both ART receipt (doctors prescribe when CD4 is low) and mortality (low CD4 signals disease progression). A researcher includes CD4 as a covariate in a standard Cox regression to estimate the causal effect of ART on survival. What is the fundamental problem with this approach?"
  type: multiple-choice
  options:
    - "Including CD4 is fine as long as the model uses robust standard errors to handle correlation"
    - "CD4 is affected by prior ART, so conditioning on it blocks part of the causal pathway — but omitting it leaves confounding; standard regression cannot resolve this dilemma"
    - "CD4 is not a true confounder because it is an intermediate variable, so it should always be excluded"
    - "The problem is measurement error in CD4, not the causal structure — better measurement would fix the bias"
  answer: 1
  explanation: "This is the defining challenge of time-varying confounding affected by prior exposure. CD4 is simultaneously a confounder (it predicts treatment and outcome) and a mediator (prior ART raises CD4). Conditioning on it blocks part of the causal effect of ART on mortality; omitting it leaves the confounding unaddressed. Standard regression, regardless of complexity or model choice, cannot handle this structure. The correct diagnosis is option B — the problem is causal, not statistical."

- question: "In a marginal structural model, inverse probability weighting creates a 'pseudo-population.' What is the key property of this pseudo-population that enables causal inference?"
  type: multiple-choice
  options:
    - "Every patient receives the same weight, eliminating all individual variation in the data"
    - "All patients are assigned the most common treatment, making groups directly comparable"
    - "Treatment assignment is no longer associated with measured confounders — it is as if treatment were randomly assigned"
    - "Patients with extreme covariate values are excluded to reduce variance"
  answer: 2
  explanation: "The IPT weights rebalance the data so that, within the weighted pseudo-population, confounders no longer predict treatment. A person with low CD4 who received ART (the expected treatment) gets a low weight; a person with high CD4 who received ART (unexpected) gets a high weight. The result is a dataset where CD4 no longer distinguishes who got ART — mimicking the covariate balance you would expect from randomization. You can then fit a standard regression model in this weighted dataset and obtain a consistent causal estimate."

- question: "A marginal structural model estimates the 'marginal' causal effect of a treatment, meaning the effect is averaged over the distribution of confounders in the target population rather than being conditional on specific covariate values."
  type: true-false
  answer: true
  explanation: "The word 'marginal' in MSM refers specifically to this marginalization: the estimated effect is not 'the effect of treatment for patients with CD4 = 200' but the effect averaged across all patients in the study population with their observed covariate distributions. This is distinct from conditional models, which estimate effects holding covariates at specific values. The marginal treatment effect is analogous to what you would observe in a randomized trial — it is the population-average treatment effect."

- question: "When time-varying confounders are present, a researcher who adds enough covariates and interaction terms to a standard regression model will eventually obtain an unbiased estimate of the causal effect of a time-varying treatment."
  type: true-false
  answer: false
  explanation: "This is a common misconception. The problem is not model mis-specification in the usual sense — it is structural. When a confounder is affected by prior treatment, conditioning on it (regardless of how flexibly the model is specified) partially blocks the causal pathway you are trying to estimate. No amount of additional covariates or interaction terms fixes a structural problem in the causal graph. Marginal structural models with IPT weighting are specifically designed to handle this structure; standard regression models are not."

- question: "Why does conditioning on a time-varying confounder that is affected by prior exposure create bias in a standard regression model, even though failing to condition on it also creates bias? How do marginal structural models escape this dilemma?"
  type: short-answer
  answer: "If you condition on the confounder (e.g., CD4), you partially block the causal path from prior treatment to the outcome, inducing 'collider bias' by conditioning on a downstream effect of treatment. If you omit it, the confounder creates classical confounding bias. You are stuck either way. MSMs escape this by using IPT weighting to remove the association between confounders and treatment assignment before fitting any regression — the confounder is 'balanced away' in the pseudo-population rather than conditioned on in the model."
  explanation: "The key is that IPT weighting acts on the treatment mechanism rather than the outcome model. By reweighting observations to make treatment independent of confounders, MSMs achieve the effect of randomization without conditioning on the confounders in the regression. The confounder is no longer a predictor of treatment in the weighted data, so it is no longer a source of confounding — and because it was never included as a covariate in the outcome model, it cannot block the causal pathway either."
```

## Explainer

Marginal structural models solve a problem that trips up standard regression: what happens when a confounder is itself affected by prior treatment? You know from time-varying confounders that this structure creates a **causal feedback loop** — and you know from inverse probability weighting that we can rebalance covariates by reweighting observations. MSMs combine these two ideas into a unified framework for estimating causal effects of dynamic treatment regimes.

To see why standard regression fails, consider an HIV cohort where patients move on and off antiretroviral therapy (ART) over time, and CD4 count is measured at each visit. CD4 count is a time-varying confounder: lower CD4 predicts both *receiving* ART (doctors prescribe it when immune function drops) and *worse outcomes* (lower CD4 directly indicates disease progression). To control for confounding, you want to adjust for CD4. But CD4 is also affected by *prior* ART — treatment raises CD4 counts. If you condition on CD4 in a regression model, you are partially conditioning on the effect of prior treatment, which **blocks part of the causal pathway** you're trying to estimate. You can't include CD4 without bias, but you can't omit it without confounding. This is the dilemma that time-varying confounding affected by prior exposure creates, and it is not fixable with standard regression regardless of model complexity.

The **marginal structural model** solves this by constructing a **pseudo-population** in which treatment assignment is independent of measured confounders. The idea: assign each person at each time point a weight equal to the inverse of their probability of receiving the treatment they actually received, given their covariate history. A person with low CD4 who received ART (the "expected" treatment) gets a low weight; a person with high CD4 who received ART (counter to expectation) gets a high weight. In the weighted pseudo-population, CD4 no longer predicts treatment (because the weighting balances it), so it is no longer a confounder — it's as if the treatment were assigned randomly. You can now fit a simple regression model (the marginal structural model) in this weighted dataset and obtain a consistent estimate of the causal effect of the treatment regime. The word "marginal" refers to the fact that the model estimates effects **marginalized over** the distribution of confounders in the target population — not conditional on any specific confounder value, which is what standard models estimate.

Two practical concerns govern MSM implementation. First, **weight stabilization**: raw IPT weights can be highly variable (extreme weights for unusual treatment-covariate combinations), inflating variance. Stabilized weights (multiplying numerator and denominator by marginal treatment probabilities) reduce this problem substantially. Second, **positivity assumption**: IPT weighting requires that every combination of covariates and treatment history has nonzero probability of receiving either treatment. If there are covariate regions where doctors would never prescribe or never withhold treatment, the denominator probability approaches zero and weights explode — this is the practical version of the positivity violation you need to diagnose. Diagnostic checks (trimming weights at extreme percentiles, plotting weight distributions) are essential before trusting MSM results.
