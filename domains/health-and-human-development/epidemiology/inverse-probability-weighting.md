---
id: inverse-probability-weighting
title: Inverse Probability Weighting
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: propensity-score-analysis
  type: hard
- id: stratification-and-adjustment
  type: soft
builds-toward:
- marginal-structural-models
- g-estimation-causal-effects
tags:
- causal-inference
- confounding
- weighting
- marginal-effects
stage: expert
status: validated
---

# Inverse Probability Weighting

## Core Idea
Inverse probability weighting (IPW) constructs weights so that the weighted sample is pseudo-randomized with respect to measured confounders. IPW directly produces marginal (population-average) treatment effects and is particularly useful for survival and time-to-event analyses where standard adjustment would be biased.

## Questions

```yaml
- question: "A patient receives treatment despite having a propensity score of 0.05 (very unlikely to be treated given their covariates). What is their approximate IPW weight, and what does it represent?"
  type: multiple-choice
  options:
    - "Weight ≈ 0.05; they receive a small weight because they were unlikely to be treated"
    - "Weight ≈ 20; they receive a large weight because they are unusual among the treated and represent many similar patients who were not treated"
    - "Weight ≈ 1; all treated patients receive the same weight regardless of propensity score"
    - "Weight ≈ 0.95; the weight is based on the probability of not being treated"
  answer: 1
  explanation: "The IPW weight for a treated patient is 1/propensity_score = 1/0.05 = 20. This large weight reflects that this patient is a rare treated individual among a pool of people who mostly went untreated. In the reweighted pseudo-population, they 'stand in for' many similar patients. This is the core mechanism: unusual treated patients receive high weights to make the treated group resemble the overall population, removing confounding by measured covariates."

- question: "A regression model estimates the effect of a drug conditional on specific covariate values (age, sex, comorbidities). An IPW analysis estimates the marginal effect. Why might a clinician prefer the marginal estimate for a policy decision?"
  type: multiple-choice
  options:
    - "Because marginal effects are always larger and more convincing to policymakers"
    - "Because conditional effects assume covariates are measured without error, which is rarely true"
    - "Because the marginal effect answers 'what if everyone in the population received this drug?' — the relevant question for population-level policy"
    - "Because regression cannot adjust for confounding, while IPW can"
  answer: 2
  explanation: "The marginal effect averages over the entire population distribution of covariates — it answers 'what would happen at the population level if we treated everyone versus no one?' A conditional effect from regression holds covariates fixed and asks 'what is the effect for someone with exactly these covariate values?' For policy decisions (e.g., whether to approve a drug for a population), the marginal effect is the appropriate target. Both regression and IPW adjust for confounding; the difference is the *type* of effect estimated."

- question: "IPW with correctly estimated propensity scores removes confounding by both measured and unmeasured variables."
  type: true-false
  answer: false
  explanation: "IPW only adjusts for *measured* confounders — those included in the propensity score model. If important confounders are unmeasured and therefore absent from the model, the propensity score is misspecified, the weights do not achieve the intended balance, and bias persists regardless of how well the weighting balances observed covariates. This is the fundamental limitation shared with all propensity score methods and observational causal inference generally."

- question: "Stabilized IPW weights reduce variance compared to raw weights without introducing bias into the treatment effect estimate."
  type: true-false
  answer: true
  explanation: "Stabilized weights are formed by multiplying the raw weight (1/P[T=t|X]) by the marginal probability of receiving that treatment P[T=t]. This bounds the weights from above and reduces their variance without introducing systematic bias, because the stabilizing factor is the same for everyone in a given treatment group and cancels out in the weighted estimator. The trade-off is that stabilized weights don't fully eliminate confounding if the marginal model is misspecified, but in practice they are strongly preferred over raw weights whenever weight instability is a concern."

- question: "Why do extreme propensity scores (near 0 or 1) create problems for IPW, and what is the intuition behind stabilized weights as a solution?"
  type: short-answer
  answer: "When a propensity score is near 0 or 1, treatment was nearly deterministic — everyone in that region either always got treatment or never did. The inverse weight (1/p or 1/(1-p)) becomes very large, so a handful of observations can dominate the entire analysis, inflating variance and making the estimate sensitive to those few data points. Stabilized weights multiply the raw weight by the marginal probability of treatment P(T=t), which caps the maximum possible weight at the ratio of marginal to conditional treatment probabilities. This reduces the range of weights while preserving their confounder-balancing property."
  explanation: "The deeper issue is positivity: IPW requires that every individual has a non-zero probability of receiving each treatment level (the positivity assumption). Near violations of positivity — propensity scores near 0 or 1 — don't break the method theoretically but create practical instability. Stabilized weights are a principled fix: they bound the weights while remaining unbiased under correct model specification, and diagnostics (plotting weight distribution, examining max weight, checking effective sample size) help identify when instability is severe enough to invalidate the analysis."
```

## Explainer

From your study of propensity score analysis, you know that the core challenge in observational research is that treatment assignment is not random — sicker patients get different treatments than healthier ones, and that confounding distorts naive comparisons. Propensity scores summarize this imbalance by estimating each person's probability of receiving treatment given their measured covariates. **Inverse probability weighting** uses those probabilities differently from matching or stratification: instead of discarding or subgrouping observations, it reweights every observation to create a synthetic sample where treatment looks as if it had been assigned independently of measured confounders.

The intuition is borrowed from survey sampling, a field you may recognize from your study of stratification and adjustment. In a stratified survey, respondents from undersampled strata are upweighted to make the sample representative. IPW applies the same logic to treatment groups: someone who received treatment despite a low predicted probability of doing so is unusual among treated people, so they receive a high weight — they are "lending" their contribution to the comparison. Someone who received treatment with very high predicted probability is unremarkable and receives a low weight. After weighting, the distribution of covariates is balanced between treated and untreated groups, mimicking what would happen in a randomized trial. The weighted estimator then simply takes weighted means in each group and differences them.

The resulting effect estimate is a **marginal treatment effect** — averaged over the entire population distribution of covariates, not conditional on holding specific covariates fixed as in regression adjustment. This distinction matters practically: a conditional effect (from a regression model) asks "what is the effect for a person with covariate values X?" A marginal effect asks "what would the average outcome be if we gave everyone the treatment versus no one?" For clinical and policy decisions — what happens at the population level — the marginal effect is often the target of interest.

The key vulnerability of IPW is **weight instability**. When some individuals have propensity scores near 0 or 1 — meaning their treatment was nearly deterministic — their inverse probability weights become very large. A handful of observations with extreme weights can dominate the analysis and inflate variance dramatically. Stabilized weights (multiplying the raw weight by the marginal probability of treatment in the overall population) reduce this instability without introducing bias. Checking the weight distribution — plotting it, examining the maximum, and verifying that no small group of observations carries disproportionate influence — is a required diagnostic step. IPW also inherits the propensity score's limitation: it only adjusts for *measured* confounders. If important confounders are unmeasured, the pseudo-randomization is incomplete, and bias persists regardless of how well the weights balance observed covariates.
