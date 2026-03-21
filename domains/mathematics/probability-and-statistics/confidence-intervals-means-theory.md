---
id: confidence-intervals-means-theory
title: Confidence Intervals for Population Means
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: standard-normal-z-scores-theory
  type: hard
- id: distribution-of-sample-mean-theory
  type: hard
builds-toward:
- hypothesis-testing-fundamentals
tags:
- confidence-interval
stage: formal-systems
status: draft
---

# Confidence Intervals for Population Means

## Core Idea
A 100(1−α)% CI for μ: X̄±z_{α/2}(σ/√n) when σ known, or X̄±t_{n-1,α/2}(s/√n) when unknown. Interpretation: 100(1−α)% of repeated CIs contain μ, NOT P(μ in CI)=1−α (μ is fixed, CI is random). t-distribution used because s estimates σ.

## Questions

```yaml
- question: "A researcher computes a 95% CI for a population mean and gets [3.1, 4.7]. She says: 'There is a 95% probability that μ is between 3.1 and 4.7.' What is wrong with this statement?"
  type: multiple-choice
  options:
    - "Nothing — this is the correct interpretation of a 95% confidence interval"
    - "The interval should be wider because 95% is too narrow a confidence level"
    - "μ is a fixed (unknown) constant, not a random variable, so it cannot have a probability of being in any interval"
    - "She should say 'certainty' rather than 'probability' since the data was collected"
  answer: 2
  explanation: "The critical error is treating μ as random. μ is a fixed (though unknown) parameter — it either is or is not in [3.1, 4.7], with probability 1 or 0 respectively. The 95% refers to the *procedure*: if you repeated the sampling and CI-construction many times, 95% of the resulting intervals would contain μ. The interval [3.1, 4.7] is one realized value of a random interval; once observed, the randomness is gone. 'Confidence' lives at the level of the method, not any particular interval."

- question: "Why do we use the t-distribution instead of the standard normal when σ is unknown?"
  type: multiple-choice
  options:
    - "The t-distribution is simpler to compute and gives the same results for large samples"
    - "Using sample standard deviation s introduces additional uncertainty, so the standardized quantity follows a t-distribution with heavier tails"
    - "The normal distribution cannot handle sample sizes smaller than 30"
    - "The t-distribution corrects for bias in the sample mean X̄"
  answer: 1
  explanation: "When σ is replaced by s, the standardized quantity (X̄ − μ)/(s/√n) no longer follows N(0,1) — it follows a t-distribution with n−1 degrees of freedom. The t has heavier tails than the normal because s itself is a random variable that adds uncertainty. This produces wider intervals (more conservative) for small n, appropriately reflecting that we estimated σ from the data. As n increases, s → σ and the t approaches the normal. Option C describes a common rule-of-thumb heuristic, not the statistical reason."

- question: "Once you have computed a specific 95% confidence interval from your data, there is a 95% probability that μ falls within it."
  type: true-false
  answer: false
  explanation: "This is the most widespread misinterpretation of confidence intervals. Once the interval is computed, μ either is or is not inside it — the probability is 1 or 0, not 95%. The 95% describes the long-run frequency with which the *procedure* captures μ: if you drew many samples and computed a CI from each, 95% of those intervals would contain μ. The randomness is in the interval (which varies across samples), not in μ (which is fixed). Holding this picture clearly is essential preparation for hypothesis testing."

- question: "Increasing the sample size narrows the confidence interval for a given confidence level, all else being equal."
  type: true-false
  answer: true
  explanation: "The margin of error in a CI is proportional to σ/√n (or s/√n for the t-interval). As n increases, √n grows, so the margin of error shrinks and the interval narrows. This reflects the statistical intuition that more data provides more precise estimates of μ. Note that to halve the margin of error, you need to quadruple the sample size, since the improvement scales as √n."

- question: "What does '95% confidence' actually mean as a statement about the procedure for constructing confidence intervals?"
  type: short-answer
  answer: "A 95% confidence level means that if you were to repeat the entire procedure many times — draw a new random sample, compute X̄ and s, and construct the interval — 95% of the resulting intervals would contain the true population mean μ. The confidence is a property of the method, not of any single interval. Any specific computed interval either contains μ or it doesn't; we simply cannot know which. The 95% is a guarantee about long-run performance: out of 100 such intervals constructed under the same procedure, approximately 95 will capture μ."
  explanation: "This frequentist interpretation is the correct one. The common error is to assign probability to μ's location, as if μ were random. Instead, μ is fixed and the interval is random (it changes every time you sample). The confidence level quantifies how often the random interval succeeds in capturing the fixed target. This framing directly supports hypothesis testing, where the same logic applies: the p-value is about the behavior of test statistics across samples, not about the probability of a hypothesis being true."
```

## Explainer

From the distribution of the sample mean, you know that if X₁, ..., Xₙ are i.i.d. with mean μ and standard deviation σ, then X̄ is approximately normal with mean μ and standard error σ/√n. From z-scores, you know how to standardize: Z = (X̄ − μ)/(σ/√n) ~ N(0,1). A **confidence interval** for μ reverses this: instead of computing a probability given μ, you construct a random interval that captures μ with specified probability.

Start with the case where σ is known. Since Z ~ N(0,1), you know P(−z_{α/2} ≤ Z ≤ z_{α/2}) = 1 − α, where z_{α/2} is the value cutting off area α/2 in each tail. Substitute Z = (X̄ − μ)/(σ/√n) and rearrange to isolate μ: P(X̄ − z_{α/2}·σ/√n ≤ μ ≤ X̄ + z_{α/2}·σ/√n) = 1 − α. The interval [X̄ ± z_{α/2}·σ/√n] is the **z-interval**. For 95% confidence, z_{α/2} ≈ 1.96, giving roughly X̄ ± 2 standard errors. The margin of error σ/√n shrinks as n grows — more data means a tighter interval, as expected.

When σ is unknown (the realistic case), you replace it with the sample standard deviation s. This changes the distribution: the quantity (X̄ − μ)/(s/√n) follows a **t-distribution** with n−1 degrees of freedom, not a standard normal. The t-distribution is symmetric and bell-shaped like the normal but has heavier tails, especially when n is small, reflecting the additional uncertainty from estimating σ. As n increases, the t-distribution approaches N(0,1), and the t-interval approaches the z-interval. The t-interval [X̄ ± t_{n-1, α/2}·s/√n] is the correct formula for practice whenever σ is unknown.

The most critical conceptual point: the confidence level describes the *procedure*, not any specific computed interval. Once you observe data and compute, say, [3.1, 4.7], the parameter μ either is or is not in that interval — there is no probability about it. "95% confidence" means that if you repeated the entire process (new sample, new CI) many times, 95% of the resulting intervals would contain μ. The interval is the random object; μ is fixed. Holding this picture clearly — the interval moves across repetitions, μ stays put — prevents the most common misinterpretation and builds the right foundation for hypothesis testing.
