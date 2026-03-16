---
id: ordered-choice-models
title: 'Ordered Choice Models: Ordered Logit and Probit'
domain: economics
course: econometrics
prerequisites:
- id: logit-probit-models
  type: hard
- id: maximum-likelihood-econometrics
  type: hard
tags:
- ordered-choice
- ordinal
- logit
- probit
stage: formal-systems
status: draft
---

# Ordered Choice Models: Ordered Logit and Probit

## Core Idea
Ordered logit and probit apply when the dependent variable has more than two ordered categories (e.g., satisfaction from 1-5). These models assume a latent continuous variable with threshold values determining the observed ordinal outcome.

## Explainer

From your study of logit and probit, you know how to model binary outcomes: a latent index y* = Xβ + ε crosses a single threshold to produce a 0 or 1. **Ordered choice models** extend this logic to outcomes with more than two ordered categories. The key word is *ordered*: the categories have a natural ranking (strongly disagree < disagree < neutral < agree < strongly agree; or bond ratings AAA > AA > A > ...) but the distances between categories are not assumed to be equal. You can't treat these as OLS outcomes because forcing equal spacing on ordinal categories imposes false precision — the gap between "disagree" and "neutral" need not equal the gap between "neutral" and "agree."

The architecture is a **latent variable model with multiple thresholds**. There is still an unobserved continuous variable y* = Xβ + ε representing the underlying propensity (satisfaction, creditworthiness, pain severity). But now there are J−1 thresholds μ₁ < μ₂ < ... < μ_{J-1} that partition the real line into J intervals. The observed outcome is category j whenever μ_{j-1} < y* ≤ μ_j. The thresholds are estimated alongside the β coefficients by maximum likelihood. Because the thresholds are free parameters, the model lets the data determine how wide each "band" is, rather than imposing equal spacing as OLS would implicitly require.

Interpretation requires care. As in binary logit/probit, the coefficients β tell you the direction of effect: a positive β_k means that increasing x_k shifts y* upward, making higher categories more probable. But the marginal effect on any specific category is non-monotone — a positive shift can increase the probability of the highest category, decrease the probability of middle categories, and increase the probability of the lowest category simultaneously, depending on where the probability mass is concentrated. This is why you should compute **marginal effects** for each category rather than simply citing the coefficient. For ordered logit, the latent error follows a logistic distribution (so the cumulative probabilities use the logistic CDF); for ordered probit, it follows a standard normal. The choice rarely matters much in practice, but both are estimated by maximum likelihood, which you already know how to work with.

The proportional odds assumption (sometimes called the parallel regression assumption) is a key identifying restriction in ordered logit: the β coefficients are the same across all thresholds — only the intercepts differ. This means a one-unit increase in x shifts the latent index by the same amount regardless of which threshold you're comparing. This is a testable restriction, and when it fails, you may need a generalized ordered logit that allows the slopes to vary across thresholds. Think of ordered choice models as a principled bridge between binary discrete models (too few categories) and OLS (assumes cardinal, continuously distributed outcomes) — they occupy the middle ground that much real survey and administrative data actually inhabits.
