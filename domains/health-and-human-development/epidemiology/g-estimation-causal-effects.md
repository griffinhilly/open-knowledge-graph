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
stage: advanced
status: draft
---

# G-Estimation and Structural Nested Models

## Core Idea
G-estimation estimates causal effects in the presence of baseline and time-varying confounding by parameterizing the structural relationship between exposure and outcome, then using estimating equations to find parameter values such that residuals are uncorrelated with exposure history, thereby identifying unconfounded effects.

## Explainer

From the counterfactual framework, you know that a causal effect is defined as the contrast between potential outcomes: Y(1) − Y(0), what would have happened with versus without exposure. From directed acyclic graphs, you know how to identify confounders — variables that affect both exposure and outcome and must be controlled to block backdoor paths. **G-estimation** handles a setting that breaks standard regression-based confounding control: **time-varying exposure** with **time-varying confounding**, where past exposure affects both current confounders and future outcomes.

The problem with standard regression in this setting is subtle but fundamental. Suppose exposure A is measured repeatedly over time, and covariate L — say, disease severity — is both a confounder of the effect of A on outcome Y and a mediator of the effect of prior A on future L. If you adjust for L in a standard regression to block confounding, you simultaneously block part of the causal pathway through which A operates — you create **collider stratification bias** by conditioning on a variable that is itself caused by prior treatment. On a DAG: A(t−1) → L(t) → A(t), and L(t) → Y, but A(t−1) also → Y directly. Adjusting for L(t) in a regression of Y on A(t) controls confounding from L(t) to A(t), but opens a backdoor path through A(t−1). Standard regression cannot simultaneously control both; the g-methods were developed specifically to break this impasse.

G-estimation's approach is to write a **structural nested model** that parameterizes the counterfactual relationship directly. The model specifies: if we removed all treatment from time t onward, what would the outcome Y₀ be, as a function of observed Y and the observed exposure history? The causal parameter ψ appears in this mapping: Y₀ = Y − ψ·A (in a simplified linear case), where Y₀ is the "de-treated" outcome. If ψ is the true causal effect, then Y₀ — the outcome we would have observed under no treatment — should be independent of the actual exposure A, once we condition on past covariates L. G-estimation finds the value of ψ that achieves this independence condition by solving **estimating equations**: typically, regressing A on past L to build a propensity model, then finding the ψ that makes the residual of the de-treated outcome uncorrelated with (centered) A. When that correlation is zero, ψ is identified. The key technical requirement is **no unmeasured confounders** conditional on the past covariate history — the same identifying assumption as other g-methods, but now applied at each time point across the treatment sequence. G-estimation is particularly valuable in clinical epidemiology: studying the longitudinal effect of a treatment whose dosing is adjusted in response to disease markers that are themselves outcomes of prior treatment is exactly the setting where simpler methods fail and structural nested models succeed.
