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
status: validated
---

# Propensity Score Matching for Observational Studies

## Core Idea
Propensity score matching (PSM) estimates the probability of treatment given covariates, then matches treated and untreated units with similar propensity scores. This balances pre-treatment characteristics, reducing selection bias when unconfoundedness (no unmeasured confounders) holds.

## Questions

```yaml
- question: "A researcher uses propensity score matching to study a job training program's effect on earnings. After matching, treated and untreated units have very similar observed characteristics (age, education, prior earnings). Can she now conclude her treatment effect estimate is unbiased?"
  type: multiple-choice
  options:
    - "Yes — matching on the propensity score controls for all sources of selection bias in observational data"
    - "Not necessarily — PSM removes bias from observed covariates, but unobserved confounders such as motivation or ability can still bias the estimate"
    - "Yes, but only if she used caliper matching rather than nearest-neighbor matching to avoid bad matches"
    - "Not yet — she also needs to verify that the propensity model has a high pseudo-R² to confirm the model captures selection correctly"
  answer: 1
  explanation: "PSM's validity rests on the unconfoundedness assumption: treatment assignment is independent of potential outcomes conditional on observed covariates X. If there is any unmeasured variable that affects both who gets treated and what their outcome would be — like motivation in a job training study — PSM does not remove that source of bias. Covariate balance in the matched sample confirms that observed variables are balanced; it says nothing about unobserved ones. This is PSM's fundamental limitation."

- question: "The Rosenbaum-Rubin theorem justifies using a single propensity score e(X) rather than matching on all covariates simultaneously. What does this theorem actually say?"
  type: multiple-choice
  options:
    - "Logistic regression always provides a more accurate propensity estimate than matching on individual covariates"
    - "If unconfoundedness holds conditional on covariates X, it also holds conditional on just the scalar propensity score P(D=1|X), so matching on one number is sufficient"
    - "The propensity score is a sufficient statistic for estimating the treatment effect itself, not just for balancing covariates"
    - "Matching on more covariates always improves balance, so the propensity score is only a computational convenience"
  answer: 1
  explanation: "Rosenbaum and Rubin (1983) proved a dimensionality reduction result: if (Y(0), Y(1)) ⊥ D | X (unconfoundedness), then (Y(0), Y(1)) ⊥ D | e(X). The propensity score inherits the balancing property of the full covariate vector. This is why you can collapse 20 covariates into one number without losing the theoretical guarantee — provided unconfoundedness holds. The propensity score is not a sufficient statistic for the treatment effect itself."

- question: "Propensity score matching can eliminate all sources of selection bias — including bias from unmeasured confounders — as long as the propensity model includes many observed covariates."
  type: true-false
  answer: false
  explanation: "PSM only addresses selection bias from observed covariates. If an unobserved variable (e.g., innate ability, social connections, health status) affects both who gets treated and what the outcome would be, PSM cannot remove that bias regardless of how rich the observed covariate set is. This is not a limitation of any specific implementation — it is a fundamental constraint of all matching methods on observational data."

- question: "After propensity score matching, checking covariate balance in the matched sample is more informative than evaluating the propensity model's statistical fit (e.g., pseudo-R² or AUC)."
  type: true-false
  answer: true
  explanation: "The goal of PSM is covariate balance in the matched sample, not a well-fitting model. A propensity model can have good predictive performance yet leave substantial imbalance after matching (e.g., if it mispredicts for certain subgroups). Conversely, even a misspecified model might achieve good balance by chance. Balance must be directly checked using standardized mean differences or distributional comparisons before and after matching."

- question: "What does the 'common support' assumption require in propensity score matching, and what goes wrong when it is violated?"
  type: short-answer
  answer: "Common support requires that for every value of the propensity score observed among treated units, there are also untreated units with the same (or similar) score. When violated — when treated units have propensity scores in a range with no control units — matching either extrapolates (finds the 'closest' but still very different control) or forces researchers to discard treated units with no valid match, changing the estimand."
  explanation: "Without common support, matching is making comparisons that are not empirically grounded — you are asking 'what would this high-probability-of-treatment unit have looked like as a control?' when there are no comparable controls in the data. This produces estimates that depend heavily on the functional form of the propensity model rather than actual observed comparisons. Visualizing the distribution of propensity scores for treated and control groups reveals overlap; trimming or restricting to the region of common support limits the analysis to defensible comparisons."
```

## Explainer

The core problem of causal inference — which you've studied — is that the units who receive a treatment and those who don't are often systematically different in ways that also affect the outcome. This is **selection bias**: people who take a job training program may be more motivated; firms that adopt a new technology may already be more productive. A naive comparison of treated and untreated outcomes conflates the treatment effect with these pre-existing differences. Randomized experiments solve this by construction, but observational data requires a different approach. Propensity score matching is one of the most widely used tools for doing so.

The **propensity score** e(X) is defined as the probability that a unit receives treatment given its observed covariates X: e(X) = P(D = 1 | X). The key insight, due to Rosenbaum and Rubin (1983), is a dimensionality reduction result: if unconfoundedness holds — meaning that conditional on X, treatment assignment is independent of potential outcomes — then conditioning on the propensity score alone is sufficient to remove selection bias. Instead of matching on twenty covariates simultaneously, you can collapse them into a single number and match on that. In practice, you typically estimate e(X) using logistic regression of treatment status on pre-treatment covariates, then generate a predicted probability for each unit.

Matching then proceeds by pairing each treated unit with one or more control units that have similar propensity scores. Common approaches include **nearest-neighbor matching** (find the control unit with the closest score), **caliper matching** (only match within a specified tolerance to avoid bad matches), and **kernel matching** (weight all control units by their score distance). After matching, you compare outcomes between matched treated and control units — this comparison approximates the counterfactual "what would have happened to the treated unit if it had not been treated?" The resulting estimate is called the **Average Treatment Effect on the Treated (ATT)**.

Two diagnostics are critical after matching. First, check **covariate balance**: does the matched sample actually have similar covariate distributions between treated and controls? Standardized mean differences before and after matching should be substantially smaller after. This is the whole point of the exercise. Second, assess **common support**: propensity score matching only works where there are both treated and untreated units with similar scores. If treated units have very high scores and controls all have very low scores, matching is extrapolating into regions without genuine comparisons. The fundamental limitation of PSM — and all matching methods — is that it cannot control for unobserved confounders. If there is some unmeasured variable that affects both treatment selection and the outcome, the matched estimates remain biased. Sensitivity analysis (e.g., Rosenbaum bounds) can characterize how much hidden bias would need to exist to overturn your findings.
