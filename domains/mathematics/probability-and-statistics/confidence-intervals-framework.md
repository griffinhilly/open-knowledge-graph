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
builds-toward:
- confidence-intervals-means
- confidence-intervals-proportions
tags:
- inference
- confidence-intervals
- estimation
stage: formal-systems
status: draft
---

# Confidence Intervals: General Framework

## Core Idea
A confidence interval is an interval estimate of a parameter with specified confidence level. A 95% CI means that if we repeated sampling, 95% of intervals constructed this way would contain the true parameter. The interval is: estimate ± (critical value) × (standard error).

## How It's Best Learned
Simulate repeated sampling and construct CIs to verify coverage. Understand that confidence level is about the method, not the specific interval. Explore how sample size, confidence level, and variability affect interval width.

## Explainer

You've studied **sampling distributions** — the distribution of a statistic like the sample mean X̄ across many repeated samples — and **standard errors**, which measure how spread out those sampling distributions are. A confidence interval is the next step: instead of reporting a single point estimate of an unknown parameter, you report a range of plausible values and attach a number to how reliably that range captures the truth. The framework applies to any estimator with a known or approximated sampling distribution.

The recipe has three components: an **estimator** (say X̄ for the population mean μ), a **standard error** (SE = σ/√n, or s/√n when σ is unknown and estimated from the sample), and a **critical value** (z_{α/2} from the standard normal, or t_{α/2,n-1} from the t-distribution). The interval is: estimate ± (critical value) × (standard error). For a 95% CI for a normal mean with known σ, this gives X̄ ± 1.96 × σ/√n, because 95% of standard normal draws fall within ±1.96 standard deviations of the mean. The critical value sets the width in "standard error units"; the standard error converts those units back to the scale of the data.

The confidence level interpretation is subtle and is the source of persistent confusion. A 95% CI does **not** mean "there is a 95% probability that μ lies in this specific interval." The parameter μ is a fixed (though unknown) number; it either is or isn't in the interval. The interval itself is random — it depends on the sample drawn. The correct statement is: the *procedure* produces intervals that contain μ in 95% of repeated applications. If you ran the study 100 times and built 100 intervals, roughly 95 would capture μ and 5 would not. Once you observe a specific interval, say [2.1, 3.4], you cannot assign a probability to it post-hoc; the 95% refers to the long-run performance of the method, not to the single realized interval.

The width of the interval is controlled by three factors: the **confidence level** (higher confidence → larger critical value → wider interval), the **sample size** (larger n → smaller SE = σ/√n → narrower interval), and the **population variability** (larger σ → wider interval). These tradeoffs are the practical content of the framework: to achieve both high confidence and narrow intervals, you must increase the sample size, because it is the only factor you typically control. This general template — estimator ± critical value × SE — applies directly to confidence intervals for proportions, differences of means, regression coefficients, and beyond. Only the sampling distribution and critical value change from case to case; the logic of the construction is always the same.
