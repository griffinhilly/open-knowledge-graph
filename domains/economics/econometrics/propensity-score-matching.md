---
id: propensity-score-matching
title: Propensity Score Matching for Observational Studies
domain: economics
course: econometrics
prerequisites:
- id: causal-inference-econometrics
  type: hard
- id: selection-bias-econometrics
  type: hard
builds-toward:
- treatment-effect-estimation
tags:
- causal-inference
- matching
- observational
stage: formal-systems
status: draft
---

# Propensity Score Matching for Observational Studies

## Core Idea
Propensity score matching (PSM) estimates the probability of treatment given covariates, then matches treated and untreated units with similar propensity scores. This balances pre-treatment characteristics, reducing selection bias when unconfoundedness (no unmeasured confounders) holds.

## Explainer

The core problem of causal inference — which you've studied — is that the units who receive a treatment and those who don't are often systematically different in ways that also affect the outcome. This is **selection bias**: people who take a job training program may be more motivated; firms that adopt a new technology may already be more productive. A naive comparison of treated and untreated outcomes conflates the treatment effect with these pre-existing differences. Randomized experiments solve this by construction, but observational data requires a different approach. Propensity score matching is one of the most widely used tools for doing so.

The **propensity score** e(X) is defined as the probability that a unit receives treatment given its observed covariates X: e(X) = P(D = 1 | X). The key insight, due to Rosenbaum and Rubin (1983), is a dimensionality reduction result: if unconfoundedness holds — meaning that conditional on X, treatment assignment is independent of potential outcomes — then conditioning on the propensity score alone is sufficient to remove selection bias. Instead of matching on twenty covariates simultaneously, you can collapse them into a single number and match on that. In practice, you typically estimate e(X) using logistic regression of treatment status on pre-treatment covariates, then generate a predicted probability for each unit.

Matching then proceeds by pairing each treated unit with one or more control units that have similar propensity scores. Common approaches include **nearest-neighbor matching** (find the control unit with the closest score), **caliper matching** (only match within a specified tolerance to avoid bad matches), and **kernel matching** (weight all control units by their score distance). After matching, you compare outcomes between matched treated and control units — this comparison approximates the counterfactual "what would have happened to the treated unit if it had not been treated?" The resulting estimate is called the **Average Treatment Effect on the Treated (ATT)**.

Two diagnostics are critical after matching. First, check **covariate balance**: does the matched sample actually have similar covariate distributions between treated and controls? Standardized mean differences before and after matching should be substantially smaller after. This is the whole point of the exercise. Second, assess **common support**: propensity score matching only works where there are both treated and untreated units with similar scores. If treated units have very high scores and controls all have very low scores, matching is extrapolating into regions without genuine comparisons. The fundamental limitation of PSM — and all matching methods — is that it cannot control for unobserved confounders. If there is some unmeasured variable that affects both treatment selection and the outcome, the matched estimates remain biased. Sensitivity analysis (e.g., Rosenbaum bounds) can characterize how much hidden bias would need to exist to overturn your findings.
