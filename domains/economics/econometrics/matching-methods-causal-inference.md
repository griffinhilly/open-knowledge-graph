---
id: matching-methods-causal-inference
title: Matching Methods for Causal Inference
domain: economics
course: econometrics
prerequisites:
- id: causal-inference-econometrics
  type: hard
- id: potential-outcomes-framework
  type: hard
builds-toward:
- propensity-score-methods
tags:
- matching
- causal-inference
- observational
stage: formal-systems
status: draft
---

# Matching Methods for Causal Inference

## Core Idea
Matching estimators pair treated and control units with similar pre-treatment characteristics. Nearest-neighbor, caliper, and kernel matching select matches differently, balancing bias and variance in treatment effect estimation.

## Questions

```yaml
- question: "A researcher uses nearest-neighbor matching on age, income, and education to estimate the effect of a job training program. She finds a positive employment effect. Why might this estimate still be biased even if the matching is done correctly?"
  type: multiple-choice
  options:
    - "Nearest-neighbor matching always produces upward bias regardless of which covariates are used"
    - "The estimate may be biased if an unobserved characteristic — such as motivation or prior job-search intensity — predicts both who enters the program and later employment outcomes"
    - "The estimate is unbiased as long as matched pairs have identical values on all three measured covariates"
    - "Bias arises only with caliper matching, not nearest-neighbor matching"
  answer: 1
  explanation: "Matching eliminates confounding only from *observed* covariates. If an unobserved variable — motivation, innate ability, health consciousness — predicts both who selects into treatment and the outcome, matching on age, income, and education cannot remove this bias. The conditional independence assumption (CIA) requires that conditional on measured X, treatment is independent of potential outcomes. Unobserved confounders violate this assumption, and no matching algorithm can detect or correct for them. This is the fundamental limitation all matching methods share."

- question: "Caliper matching typically produces a smaller analysis sample than nearest-neighbor matching because:"
  type: multiple-choice
  options:
    - "Caliper matching uses fewer control units per treated unit by design"
    - "Treated units whose nearest control unit falls outside the distance threshold are dropped from the analysis entirely"
    - "Caliper matching requires exact covariate matches, which are rare in finite samples"
    - "Caliper matching weights control units, reducing the effective sample size"
  answer: 1
  explanation: "Caliper matching sets a maximum allowable distance between matched pairs. Treated units without a sufficiently close control unit are excluded from the analysis entirely — they have no adequate counterfactual. This is the cost of the caliper's benefit: it removes poor matches that would introduce bias, but the remaining matched sample may not represent all treated units, potentially creating a different kind of selection problem. Nearest-neighbor matching keeps all treated units (lower variance, potentially higher bias from bad matches); caliper sacrifices sample size to control match quality."

- question: "Nearest-neighbor matching can produce consistent estimates of the average treatment effect in large samples, even when the nearest neighbor is not a perfect match on all covariates."
  type: true-false
  answer: true
  explanation: "Matching estimators are consistent under the conditional independence assumption: as the sample grows, nearest neighbors become closer in covariate space, and the bias from imperfect matches shrinks toward zero. In large samples with sufficient covariate overlap, the estimator converges to the true treatment effect. Perfect exact matching is not required for consistency — it is only required that the CIA holds and that the support of treated and control covariate distributions overlap. This is why nearest-neighbor matching is a valid estimator despite rarely finding exact matches."

- question: "Matching methods can eliminate confounding bias even from unobserved variables, provided the researcher matches on enough observed characteristics to make the treated and control groups comparable."
  type: true-false
  answer: false
  explanation: "This is the critical misconception about matching. Matching can only remove confounding from variables that are *observed and included* in the procedure. The CIA requires that potential outcomes are independent of treatment conditional on observed X — but if an unobserved variable U affects both treatment and outcomes, matching on X cannot remove U's influence regardless of how many observed characteristics are included. Adding more observed covariates does not compensate for missing unobserved ones. The CIA is fundamentally untestable precisely because it makes claims about unobserved quantities."

- question: "What is the conditional independence assumption (CIA) in matching, and why is it fundamentally untestable?"
  type: short-answer
  answer: "The CIA states that conditional on observed pre-treatment covariates X, treatment assignment is independent of potential outcomes: Y(0), Y(1) ⊥ D | X. It requires that among units with the same X values, who receives treatment is unrelated to what their outcomes would have been. It is fundamentally untestable because it makes claims about counterfactual outcomes — we never observe Y(0) for treated units or Y(1) for control units. If an unobserved confounder exists, we cannot see it in the data, so we cannot verify that conditioning on X is sufficient."
  explanation: "Researchers assess the CIA's plausibility indirectly rather than testing it directly: by arguing the economic mechanism behind selection, running placebo tests (checking whether the estimator finds spurious 'effects' on pre-treatment outcomes), conducting Rosenbaum sensitivity analyses, and checking whether estimates are stable across different covariate specifications. A stable estimate and clean placebo tests increase confidence, but they cannot prove the CIA. The assumption ultimately rests on a judgment about whether the available data captures all important selection factors."
```

## Explainer

From the potential outcomes framework, you know the **fundamental problem of causal inference**: each unit is either treated or untreated — you never observe both Y(1) and Y(0) for the same person at the same time. To estimate the average treatment effect (ATT or ATE), you need to approximate the counterfactual: what would treated units have experienced if they hadn't been treated? Matching builds this counterfactual by substituting control units that look similar to the treated unit before treatment. The logic is simple: if two students have identical test scores, family income, and prior grades, and one goes to a private school while the other doesn't, the latter is a reasonable counterfactual for the former.

The key assumption that makes matching valid is **conditional independence** (also called "selection on observables" or the CIA): conditional on observable pre-treatment characteristics X, treatment assignment is independent of potential outcomes. Written as Y(0), Y(1) ⊥ D | X. In plain language: once you account for all the measured covariates, treated and untreated units with the same X values are similar enough that any difference in outcomes can be attributed to the treatment. This is a strong assumption — it fails whenever important confounders are unobserved — but in settings where you have rich administrative data (detailed demographics, prior outcomes, institutional records), it is often plausible.

The three matching algorithms differ in how they select the counterfactual comparison. **Nearest-neighbor matching** pairs each treated unit with the single control unit closest in covariate space (often using Euclidean distance or Mahalanobis distance). It's computationally simple and unbiased in large samples but can produce poor matches when the nearest neighbor is still far away. **Caliper matching** imposes a maximum distance threshold: treated units without a sufficiently close match are dropped from the analysis entirely. This reduces bias from bad matches but can shrink the sample significantly, potentially introducing selection if the matched sample is unrepresentative of all treated units. **Kernel matching** weights every control unit by a kernel function of its distance to the treated unit — nearby controls receive high weight, distant controls near-zero weight. It uses more data than nearest-neighbor, reducing variance, but the choice of kernel bandwidth introduces a smoothing decision.

The bias-variance tradeoff across these methods follows a clear pattern. One-to-one nearest-neighbor matching is low-bias (when matches are good) but high-variance (few observations, noisy estimates). Kernel matching is lower variance but can introduce bias when distant, poor matches receive positive weight. Caliper matching controls bias by removing bad matches, at the cost of external validity. Practitioners often run multiple methods as a robustness check: if treatment effect estimates are similar across methods, the result is less sensitive to the specific matching algorithm chosen.

The critical limitation of all matching methods is that they handle **observed confounding** only. If there is an unobserved variable that predicts both treatment selection and outcomes — innate ability in education studies, health consciousness in nutrition studies, location quality in housing studies — matching on observed characteristics cannot eliminate this bias. The identifying assumption is untestable directly; researchers typically assess it with placebo tests, sensitivity analyses (like Rosenbaum bounds), and by arguing the economic mechanism behind selection. When unobserved confounding is a serious concern, matching should be combined with or replaced by methods that exploit external variation, such as instrumental variables or difference-in-differences.
