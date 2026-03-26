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
stage: advanced
status: validated
---

# Ordered Choice Models: Ordered Logit and Probit

## Core Idea
Ordered logit and probit apply when the dependent variable has more than two ordered categories (e.g., satisfaction from 1-5). These models assume a latent continuous variable with threshold values determining the observed ordinal outcome.

## Questions

```yaml
- question: "A researcher wants to model customer satisfaction ratings (1=very dissatisfied, 2=dissatisfied, 3=neutral, 4=satisfied, 5=very satisfied) as a function of price and service quality. Why is OLS inappropriate here?"
  type: multiple-choice
  options:
    - "OLS cannot handle more than two outcome categories"
    - "OLS treats the categories as having equal spacing, which imposes false precision on ordinal data"
    - "OLS always predicts values outside the 1–5 range for this type of data"
    - "Satisfaction data always violates the OLS normality assumption"
  answer: 1
  explanation: "The core problem is equal spacing: OLS treats a one-unit move from 3 to 4 as identical in magnitude to a move from 1 to 2. For ordinal categories, there is no guarantee these gaps are equal in the underlying construct. Ordered probit/logit avoids this by estimating where threshold parameters fall on a latent continuous scale, letting the data determine the spacing. OLS can handle multiple categories technically; the problem is interpretive, not mechanical."

- question: "In an ordered logit model of bond credit ratings (AAA, AA, A, BBB, ...), a firm's leverage ratio has a positive coefficient. A ratings analyst concludes: 'Higher leverage increases the probability of every higher-quality rating.' This interpretation is:"
  type: multiple-choice
  options:
    - "Correct — a positive coefficient shifts probability toward all higher categories"
    - "Incorrect — a positive coefficient on leverage would shift probability toward lower-quality (worse) ratings"
    - "Incorrect — the coefficient's sign cannot be interpreted without computing marginal effects"
    - "Correct only if the proportional odds assumption holds"
  answer: 1
  explanation: "The analyst has the direction right but the logic wrong in a subtle way. A positive coefficient on leverage shifts the latent index y* upward — but whether that moves probability toward higher or lower rating categories depends on how ratings are coded. More importantly, a coefficient shift does NOT increase probability for all categories simultaneously: middle categories can actually lose probability while the tails gain. The marginal effect of a variable on the probability of any specific category can be positive, negative, or non-monotone. The analyst should compute marginal effects for each category, not rely on the coefficient's sign alone."

- question: "The proportional odds assumption in ordered logit requires that the effect of each predictor on the latent index is the same regardless of which threshold is being crossed."
  type: true-false
  answer: true
  explanation: "This is exactly the parallel regression (proportional odds) assumption: the β coefficients are constant across all thresholds. Intuitively, a one-unit increase in x shifts the latent propensity by β regardless of whether you're comparing 'category 1 vs. 2+' or 'categories 1–4 vs. 5.' Only the intercepts (threshold values μ) differ across comparisons. When this assumption fails — when the effect of a predictor changes depending on which transition you're examining — you need a generalized ordered logit with threshold-specific slopes."

- question: "In ordered logit, a variable with a positive coefficient generally increases the probability of the highest outcome category."
  type: true-false
  answer: false
  explanation: "This is only guaranteed for the extreme top category under specific distributional conditions. For middle categories, the marginal effect is non-monotone: a positive shift in the latent index can *decrease* the probability of an intermediate category while increasing the probabilities of the top and bottom extremes simultaneously, or it can increase the probability of high categories while decreasing low ones. The direction depends on where probability mass is concentrated relative to the threshold locations. Always compute category-specific marginal effects."

- question: "Why can a positive coefficient in an ordered probit model actually decrease the probability of some categories, and what should be reported instead of just the coefficient?"
  type: short-answer
  answer: "A positive coefficient shifts the entire latent distribution upward, moving probability mass from low categories toward high categories. Middle categories can lose probability from both ends — the lower threshold steals from them below while the upper threshold steals from above. The net effect on any specific middle category depends on the shape of the distribution and threshold locations. Instead of just reporting β, researchers should compute and report marginal effects: the change in the predicted probability of each outcome category for a one-unit change in the predictor."
  explanation: "This non-monotonicity is one of the most commonly misunderstood aspects of ordered choice models. It is analogous to the logic in multinomial models where adding a covariate can increase probability for distant categories while reducing it for adjacent ones. The coefficient β answers 'which direction does the latent propensity shift?' but marginal effects answer the policy-relevant question: 'by how much does the probability of each outcome change?'"
```

## Explainer

From your study of logit and probit, you know how to model binary outcomes: a latent index y* = Xβ + ε crosses a single threshold to produce a 0 or 1. **Ordered choice models** extend this logic to outcomes with more than two ordered categories. The key word is *ordered*: the categories have a natural ranking (strongly disagree < disagree < neutral < agree < strongly agree; or bond ratings AAA > AA > A > ...) but the distances between categories are not assumed to be equal. You can't treat these as OLS outcomes because forcing equal spacing on ordinal categories imposes false precision — the gap between "disagree" and "neutral" need not equal the gap between "neutral" and "agree."

The architecture is a **latent variable model with multiple thresholds**. There is still an unobserved continuous variable y* = Xβ + ε representing the underlying propensity (satisfaction, creditworthiness, pain severity). But now there are J−1 thresholds μ₁ < μ₂ < ... < μ_{J-1} that partition the real line into J intervals. The observed outcome is category j whenever μ_{j-1} < y* ≤ μ_j. The thresholds are estimated alongside the β coefficients by maximum likelihood. Because the thresholds are free parameters, the model lets the data determine how wide each "band" is, rather than imposing equal spacing as OLS would implicitly require.

Interpretation requires care. As in binary logit/probit, the coefficients β tell you the direction of effect: a positive β_k means that increasing x_k shifts y* upward, making higher categories more probable. But the marginal effect on any specific category is non-monotone — a positive shift can increase the probability of the highest category, decrease the probability of middle categories, and increase the probability of the lowest category simultaneously, depending on where the probability mass is concentrated. This is why you should compute **marginal effects** for each category rather than simply citing the coefficient. For ordered logit, the latent error follows a logistic distribution (so the cumulative probabilities use the logistic CDF); for ordered probit, it follows a standard normal. The choice rarely matters much in practice, but both are estimated by maximum likelihood, which you already know how to work with.

The proportional odds assumption (sometimes called the parallel regression assumption) is a key identifying restriction in ordered logit: the β coefficients are the same across all thresholds — only the intercepts differ. This means a one-unit increase in x shifts the latent index by the same amount regardless of which threshold you're comparing. This is a testable restriction, and when it fails, you may need a generalized ordered logit that allows the slopes to vary across thresholds. Think of ordered choice models as a principled bridge between binary discrete models (too few categories) and OLS (assumes cardinal, continuously distributed outcomes) — they occupy the middle ground that much real survey and administrative data actually inhabits.
