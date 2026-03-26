---
id: point-estimators-properties
title: Properties of Point Estimators
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: expected-value
  type: hard
builds-toward:
- unbiased-and-consistent-estimators
- maximum-likelihood-estimation-intro
tags:
- estimation
- properties
- bias
stage: formal-systems
status: validated
---

# Properties of Point Estimators

## Core Idea
Point estimators have properties including: unbiasedness (E[θ̂] = θ), consistency (θ̂ → θ as n→∞), efficiency (low variance), and robustness. Comparing estimators by these properties helps choose between alternatives.

## How It's Best Learned
Calculate bias and variance of simple estimators analytically. Compare sample mean and sample median as estimators of location. Examine how efficiency changes with sample size or distribution shape.

## Questions

```yaml
- question: "An estimator θ̂ satisfies E[θ̂] = θ + 5/n for all sample sizes n. Which of the following is correct?"
  type: multiple-choice
  options:
    - "θ̂ is biased at every finite n, but consistent — the bias 5/n shrinks to zero as n → ∞"
    - "θ̂ is both biased and inconsistent — it never equals θ exactly"
    - "θ̂ is unbiased — the formula shows it equals θ plus a correction term"
    - "θ̂ is unbiased and consistent because the correction term is small for large n"
  answer: 0
  explanation: "Bias = E[θ̂] − θ = 5/n ≠ 0 for any finite n, so θ̂ is biased. But as n → ∞, the bias 5/n → 0, and if the variance also shrinks appropriately, θ̂ converges in probability to θ — making it consistent. This demonstrates that unbiasedness and consistency are distinct properties: an estimator can be biased at every finite sample size yet still be consistent."

- question: "You are estimating average income in a city that includes a few billionaires. Which statement best captures the robustness-efficiency tradeoff between the sample mean and median?"
  type: multiple-choice
  options:
    - "The sample median is robust to the billionaires' extreme values but less efficient than the sample mean if income were normally distributed"
    - "The sample mean is robust because averaging spreads the effect of extreme values across all observations"
    - "The sample median is strictly better than the sample mean — more efficient and more robust in every real-world setting"
    - "Neither estimator is affected by extreme values once the sample is large enough"
  answer: 0
  explanation: "The sample mean is efficient under normality (minimum variance among unbiased estimators) but is sensitive to outliers — a single billionaire can drastically pull the mean away from the typical income. The sample median, depending only on the middle rank, is unaffected by how extreme the outliers are. The tradeoff: efficiency under the assumed model (mean) vs. safety when the model is violated (median). In income data, where skewness is severe, robustness often matters more."

- question: "An estimator can be consistent without being unbiased at any finite sample size."
  type: true-false
  answer: true
  explanation: "True. Consistency is an asymptotic property: the estimator converges in probability to the true parameter as n → ∞. This is compatible with having nonzero bias at every finite n, as long as the bias shrinks to zero sufficiently fast (and variance also shrinks). For example, an estimator with E[θ̂] = θ + 1/n and Var[θ̂] → 0 is biased for every n yet consistent. Unbiasedness (E[θ̂] = θ for all n) and consistency are independent properties."

- question: "An unbiased estimator is generally consistent."
  type: true-false
  answer: false
  explanation: "False. Unbiasedness means E[θ̂] = θ at every sample size — the estimator aims correctly on average. But it says nothing about whether estimates cluster more tightly around θ as n grows. An unbiased estimator could have constant or even growing variance, meaning larger samples provide no additional accuracy. Consistency requires both that the estimator aims at θ and that its variance shrinks to zero as n → ∞. Unbiasedness guarantees the aim; it does not guarantee convergence."

- question: "Explain in your own words why an unbiased estimator is not necessarily consistent."
  type: short-answer
  answer: "Unbiasedness means the estimator is correct on average — its expected value equals the true parameter — but it does not constrain how spread out individual estimates are or whether that spread decreases with more data. An estimator could be perfectly centered (no bias) yet have high variance that stays constant as n grows, so collecting more data still leaves you with highly variable estimates. Consistency requires that as n increases, the estimates concentrate around the true value (variance → 0). Unbiasedness addresses the center; consistency addresses the spread."
  explanation: "The clearest way to see this is to construct a counterexample: define θ̂ = X₁ (just the first observation, ignoring the rest). E[θ̂] = μ (unbiased), but Var[θ̂] = σ² regardless of n — it never shrinks. This estimator is unbiased but inconsistent. Real estimators rarely behave this pathologically, but the conceptual distinction matters for understanding what large samples can and cannot guarantee."
```

## Explainer

An estimator is just a recipe — a function of your data that produces a guess for an unknown parameter. Before you can compare two recipes, you need a vocabulary for what "good" means. That vocabulary is the four key properties: unbiasedness, consistency, efficiency, and robustness.

**Unbiasedness** is the most intuitive. An estimator θ̂ is unbiased if, on average over all possible datasets of a given size, it lands exactly on the true parameter: E[θ̂] = θ. Think of it like a scale that, even if individual readings fluctuate, averages out to the true weight. The sample mean X̄ is the classic unbiased estimator of the population mean μ — you can verify this directly using your prerequisite knowledge of expected value: E[X̄] = E[(X₁ + ... + Xₙ)/n] = nμ/n = μ. The **bias** of an estimator is the signed difference E[θ̂] − θ; unbiasedness means bias equals zero.

**Consistency** captures a different desirable behavior: as your sample grows, does θ̂ get closer and closer to θ? A consistent estimator converges in probability to the true parameter as n → ∞. This is an asymptotic property, unlike unbiasedness which applies at every sample size. Most well-behaved estimators are both unbiased and consistent, but they can be decoupled — an estimator can be unbiased at every n yet inconsistent (high variance that never shrinks), or biased at every finite n yet consistent (bias shrinks to zero as n grows).

**Efficiency** asks: among all unbiased estimators, which has the smallest variance? A more efficient estimator wastes less information — it extracts more signal from the same data. The **Cramér-Rao lower bound** establishes the minimum possible variance any unbiased estimator can achieve, and an estimator that achieves this bound is called **efficient**. For example, when data is normally distributed, the sample mean is the efficient estimator of μ — no unbiased estimator can do better with the same data. The sample median is also unbiased for μ (by symmetry) but has higher variance, making it less efficient in the normal case.

**Robustness** is the practical counterpart to efficiency: how badly does the estimator perform when assumptions are violated? The sample mean is efficient under normality but sensitive to outliers — a single extreme value can drag it far from the bulk of the data. The sample median, though less efficient under normality, is **robust**: its value depends only on the middle rank, so outliers cause no damage. Choosing among estimators always involves navigating this tradeoff between efficiency (optimal under the assumed model) and robustness (safe when the model is wrong). Real statistical practice requires knowing which property matters more for the problem at hand.
