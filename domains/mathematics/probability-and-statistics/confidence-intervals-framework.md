---
id: confidence-intervals-framework
title: 'Confidence Intervals: General Framework'
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: sampling-distributions
  type: hard
- id: standard-error-of-estimators
  type: hard
- id: central-limit-theorem-theory
  type: hard
builds-toward:
- confidence-intervals-means
- confidence-intervals-proportions
tags:
- inference
- confidence-intervals
- estimation
stage: formal-systems
status: validated
---

# Confidence Intervals: General Framework

## Core Idea
A confidence interval is an interval estimate of a parameter with specified confidence level. A 95% CI means that if we repeated sampling, 95% of intervals constructed this way would contain the true parameter. The interval is: estimate ± (critical value) × (standard error).

## How It's Best Learned
Simulate repeated sampling and construct CIs to verify coverage. Understand that confidence level is about the method, not the specific interval. Explore how sample size, confidence level, and variability affect interval width.

## Questions

```yaml
- question: "A researcher reports: 'The 95% confidence interval for the average daily step count is [7,200, 8,400].' Which interpretation is correct?"
  type: multiple-choice
  options:
    - "There is a 95% probability that the true population mean is between 7,200 and 8,400"
    - "95% of individuals in the population take between 7,200 and 8,400 steps per day"
    - "If this study were repeated many times, 95% of the resulting intervals would contain the true population mean"
    - "The sample mean has a 95% chance of lying between 7,200 and 8,400"
  answer: 2
  explanation: "The correct interpretation describes the long-run performance of the procedure, not a probability about this specific interval. The parameter (true mean) is a fixed number — it either is or isn't in [7,200, 8,400]. We can't assign it a probability post-hoc. The 95% refers to what would happen across many repetitions of the study: 95% of intervals constructed this way would contain the true mean. Option A is the most common wrong interpretation and is subtly but fundamentally incorrect."

- question: "A researcher wants a narrower confidence interval without reducing the confidence level from 95%. Which change achieves this?"
  type: multiple-choice
  options:
    - "Use a higher critical value (e.g., z = 2.33 instead of 1.96)"
    - "Increase the sample size"
    - "Decrease the confidence level to 90% while keeping interpretation the same"
    - "Report the interval in different units to make it appear narrower"
  answer: 1
  explanation: "The interval width is estimate ± critical_value × SE, where SE = σ/√n. Increasing sample size n decreases SE proportionally, directly narrowing the interval. The confidence level controls the critical value — increasing it to 99% widens the interval. The population variability σ is fixed and outside the researcher's control. Larger sample size is the only practical lever for achieving both high confidence and narrow intervals simultaneously."

- question: "Once a specific confidence interval has been calculated — say [2.1, 3.4] — it is correct to say there is a 95% probability that the true population mean lies within that interval."
  type: true-false
  answer: false
  explanation: "After the interval is computed, there is no randomness left to assign probability to. The true mean μ is a fixed constant; [2.1, 3.4] is a fixed interval. Either μ ∈ [2.1, 3.4] or μ ∉ [2.1, 3.4] — the probability is 1 or 0, not 0.95. The 95% describes the procedure: before sampling, the probability that the (random) interval will cover μ is 95%. Once you observe the specific interval, the probabilistic statement no longer applies to it. This distinction is subtle but fundamental to frequentist inference."

- question: "A 99% confidence interval is always wider than a 95% confidence interval computed from the same data, all else being equal."
  type: true-false
  answer: true
  explanation: "Higher confidence requires a larger critical value. For a 95% CI, z = 1.96; for a 99% CI, z = 2.576. The interval is estimate ± critical_value × SE, so a larger critical value produces a wider interval from the same data. This reflects the fundamental tradeoff: to be more confident of capturing the parameter, you must sacrifice precision (narrowness). There is no way to increase confidence without widening the interval, short of collecting more data."

- question: "Explain why it is incorrect to say 'there is a 95% probability that μ lies in [2.1, 3.4]' once a specific interval has been computed from a sample."
  type: short-answer
  answer: "The parameter μ is a fixed (though unknown) constant — it does not have a probability distribution under frequentist statistics. The specific interval [2.1, 3.4] is also fixed once computed. Either μ is in the interval or it isn't. The 95% describes the sampling procedure: before collecting data, 95% of all intervals the procedure could generate would contain μ. Once a specific interval is realized, that probabilistic statement applies to the method, not to the particular interval."
  explanation: "The confusion arises from treating a fixed unknown parameter as random. In frequentist statistics, probability applies to the behavior of estimators and intervals across repeated sampling — not to fixed but unknown quantities. The correct framing is: 'This interval was produced by a method that works 95% of the time.' Not: 'This particular interval has a 95% chance of being correct.' Bayesian credible intervals do allow direct probability statements about parameters, but they require a prior distribution and answer a different question."
```

## Explainer

You've studied **sampling distributions** — the distribution of a statistic like the sample mean X̄ across many repeated samples — and **standard errors**, which measure how spread out those sampling distributions are. A confidence interval is the next step: instead of reporting a single point estimate of an unknown parameter, you report a range of plausible values and attach a number to how reliably that range captures the truth. The framework applies to any estimator with a known or approximated sampling distribution.

The recipe has three components: an **estimator** (say X̄ for the population mean μ), a **standard error** (SE = σ/√n, or s/√n when σ is unknown and estimated from the sample), and a **critical value** (z_{α/2} from the standard normal, or t_{α/2,n-1} from the t-distribution). The interval is: estimate ± (critical value) × (standard error). For a 95% CI for a normal mean with known σ, this gives X̄ ± 1.96 × σ/√n, because 95% of standard normal draws fall within ±1.96 standard deviations of the mean. The critical value sets the width in "standard error units"; the standard error converts those units back to the scale of the data.

The confidence level interpretation is subtle and is the source of persistent confusion. A 95% CI does **not** mean "there is a 95% probability that μ lies in this specific interval." The parameter μ is a fixed (though unknown) number; it either is or isn't in the interval. The interval itself is random — it depends on the sample drawn. The correct statement is: the *procedure* produces intervals that contain μ in 95% of repeated applications. If you ran the study 100 times and built 100 intervals, roughly 95 would capture μ and 5 would not. Once you observe a specific interval, say [2.1, 3.4], you cannot assign a probability to it post-hoc; the 95% refers to the long-run performance of the method, not to the single realized interval.

The width of the interval is controlled by three factors: the **confidence level** (higher confidence → larger critical value → wider interval), the **sample size** (larger n → smaller SE = σ/√n → narrower interval), and the **population variability** (larger σ → wider interval). These tradeoffs are the practical content of the framework: to achieve both high confidence and narrow intervals, you must increase the sample size, because it is the only factor you typically control. This general template — estimator ± critical value × SE — applies directly to confidence intervals for proportions, differences of means, regression coefficients, and beyond. Only the sampling distribution and critical value change from case to case; the logic of the construction is always the same.
