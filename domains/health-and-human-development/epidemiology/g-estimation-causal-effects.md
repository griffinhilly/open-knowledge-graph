---
id: g-estimation-causal-effects
title: G-Estimation and Structural Nested Models
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: counterfactual-framework
  type: hard
- id: directed-acyclic-graphs
  type: hard
builds-toward:
- marginal-structural-models
- time-varying-confounders
tags:
- causal-inference
- structural-models
- effect-estimation
stage: expert
status: draft
---

# G-Estimation and Structural Nested Models

## Core Idea
G-estimation estimates causal effects in the presence of baseline and time-varying confounding by parameterizing the structural relationship between exposure and outcome, then using estimating equations to find parameter values such that residuals are uncorrelated with exposure history, thereby identifying unconfounded effects.

## Questions

```yaml
- question: "A researcher studies the effect of antiretroviral therapy (ART) on mortality in HIV patients. ART dosing is adjusted over time based on CD4 count, which is also an independent predictor of mortality. The researcher adjusts for CD4 count in a standard regression of mortality on ART dose. What is the primary problem with this approach?"
  type: multiple-choice
  options:
    - "CD4 count is a mediator, so it must be excluded from any regression model"
    - "Adjusting for CD4 count creates collider stratification bias: it blocks the confounding path from CD4 to ART, but simultaneously opens a backdoor path through prior ART that distorts the effect estimate"
    - "Standard regression cannot handle continuous exposures like ART dose"
    - "CD4 count is not a valid confounder because it is measured after treatment begins"
  answer: 1
  explanation: "The classic failure of standard regression with time-varying confounders: CD4 is a confounder of the ART-mortality relationship at time t (must be controlled), but it is also a mediator of prior ART's effect (controlling for it blocks part of the causal pathway and opens a backdoor through past ART). Option 0 is wrong — mediation doesn't automatically call for exclusion. G-methods were developed specifically to handle this impasse."

- question: "In G-estimation with a structural nested model, how is the causal parameter ψ identified from observed data?"
  type: multiple-choice
  options:
    - "By regressing the outcome on exposure and all measured covariates in a single multivariable model"
    - "By finding the value of ψ that makes the 'de-treated' potential outcome independent of the observed exposure, conditional on the covariate history"
    - "By matching treated and untreated individuals on all baseline characteristics"
    - "By inverting the propensity score to create an exposure-weighted pseudo-population"
  answer: 1
  explanation: "The structural nested model specifies a mapping from observed Y to Y₀ (the outcome under no treatment) as a function of ψ. G-estimation finds the ψ where Y₀ is uncorrelated with exposure conditional on past covariates — the independence condition that identifies the causal effect. Options 0 and 2 describe standard regression and matching, which fail in this setting. Option 3 describes inverse probability weighting, a different g-method."

- question: "G-estimation can estimate the causal effect of a time-varying treatment even when a time-varying covariate is simultaneously a confounder of the current exposure-outcome relationship and a consequence of prior exposure."
  type: true-false
  answer: true
  explanation: "This is precisely what G-estimation was designed for. By parameterizing the counterfactual directly (the structural nested model) and solving for the ψ that achieves the independence condition, G-estimation avoids the need to adjust for the problematic covariate in a regression — sidestepping the collider stratification bias that standard adjustment would introduce."

- question: "In the presence of time-varying confounders, including all measured covariates in a standard multivariable regression at each time point is a valid strategy for estimating the causal effect of a time-varying treatment."
  type: true-false
  answer: false
  explanation: "This is the central misconception. When a time-varying covariate is both a confounder of the current treatment effect AND a consequence of prior treatment, adjusting for it in standard regression blocks part of the causal pathway and opens collider-induced backdoor paths. G-methods (G-estimation, marginal structural models, G-computation) were developed to handle this structural problem, which cannot be solved by simply 'adding more covariates' to a regression."

- question: "Why does time-varying confounding that is also time-varying mediation break standard regression-based confounding control, and what is the key move G-estimation makes to work around this?"
  type: short-answer
  answer: "Standard regression forces a choice: adjust for the covariate (controls confounding but blocks the causal path and induces collider bias) or don't adjust (leaves confounding uncontrolled). G-estimation avoids this by not adjusting for the covariate in a regression at all. Instead, it writes a structural nested model for the counterfactual outcome under no treatment (Y₀ = Y − ψ·A), then finds the ψ such that Y₀ is independent of A given past covariate history — using the covariate only in a propensity model for A, not in a direct outcome regression."
  explanation: "The key insight is that G-estimation separates the two uses of the covariate: it models the covariate's relationship to exposure (propensity) to achieve the independence condition, without conditioning on it as a predictor of outcome. This breaks the vicious cycle that standard regression cannot escape."
```

## Explainer

From the counterfactual framework, you know that a causal effect is defined as the contrast between potential outcomes: Y(1) − Y(0), what would have happened with versus without exposure. From directed acyclic graphs, you know how to identify confounders — variables that affect both exposure and outcome and must be controlled to block backdoor paths. **G-estimation** handles a setting that breaks standard regression-based confounding control: **time-varying exposure** with **time-varying confounding**, where past exposure affects both current confounders and future outcomes.

The problem with standard regression in this setting is subtle but fundamental. Suppose exposure A is measured repeatedly over time, and covariate L — say, disease severity — is both a confounder of the effect of A on outcome Y and a mediator of the effect of prior A on future L. If you adjust for L in a standard regression to block confounding, you simultaneously block part of the causal pathway through which A operates — you create **collider stratification bias** by conditioning on a variable that is itself caused by prior treatment. On a DAG: A(t−1) → L(t) → A(t), and L(t) → Y, but A(t−1) also → Y directly. Adjusting for L(t) in a regression of Y on A(t) controls confounding from L(t) to A(t), but opens a backdoor path through A(t−1). Standard regression cannot simultaneously control both; the g-methods were developed specifically to break this impasse.

G-estimation's approach is to write a **structural nested model** that parameterizes the counterfactual relationship directly. The model specifies: if we removed all treatment from time t onward, what would the outcome Y₀ be, as a function of observed Y and the observed exposure history? The causal parameter ψ appears in this mapping: Y₀ = Y − ψ·A (in a simplified linear case), where Y₀ is the "de-treated" outcome. If ψ is the true causal effect, then Y₀ — the outcome we would have observed under no treatment — should be independent of the actual exposure A, once we condition on past covariates L. G-estimation finds the value of ψ that achieves this independence condition by solving **estimating equations**: typically, regressing A on past L to build a propensity model, then finding the ψ that makes the residual of the de-treated outcome uncorrelated with (centered) A. When that correlation is zero, ψ is identified. The key technical requirement is **no unmeasured confounders** conditional on the past covariate history — the same identifying assumption as other g-methods, but now applied at each time point across the treatment sequence. G-estimation is particularly valuable in clinical epidemiology: studying the longitudinal effect of a treatment whose dosing is adjusted in response to disease markers that are themselves outcomes of prior treatment is exactly the setting where simpler methods fail and structural nested models succeed.
