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

## Explainer

From the distribution of the sample mean, you know that if X₁, ..., Xₙ are i.i.d. with mean μ and standard deviation σ, then X̄ is approximately normal with mean μ and standard error σ/√n. From z-scores, you know how to standardize: Z = (X̄ − μ)/(σ/√n) ~ N(0,1). A **confidence interval** for μ reverses this: instead of computing a probability given μ, you construct a random interval that captures μ with specified probability.

Start with the case where σ is known. Since Z ~ N(0,1), you know P(−z_{α/2} ≤ Z ≤ z_{α/2}) = 1 − α, where z_{α/2} is the value cutting off area α/2 in each tail. Substitute Z = (X̄ − μ)/(σ/√n) and rearrange to isolate μ: P(X̄ − z_{α/2}·σ/√n ≤ μ ≤ X̄ + z_{α/2}·σ/√n) = 1 − α. The interval [X̄ ± z_{α/2}·σ/√n] is the **z-interval**. For 95% confidence, z_{α/2} ≈ 1.96, giving roughly X̄ ± 2 standard errors. The margin of error σ/√n shrinks as n grows — more data means a tighter interval, as expected.

When σ is unknown (the realistic case), you replace it with the sample standard deviation s. This changes the distribution: the quantity (X̄ − μ)/(s/√n) follows a **t-distribution** with n−1 degrees of freedom, not a standard normal. The t-distribution is symmetric and bell-shaped like the normal but has heavier tails, especially when n is small, reflecting the additional uncertainty from estimating σ. As n increases, the t-distribution approaches N(0,1), and the t-interval approaches the z-interval. The t-interval [X̄ ± t_{n-1, α/2}·s/√n] is the correct formula for practice whenever σ is unknown.

The most critical conceptual point: the confidence level describes the *procedure*, not any specific computed interval. Once you observe data and compute, say, [3.1, 4.7], the parameter μ either is or is not in that interval — there is no probability about it. "95% confidence" means that if you repeated the entire process (new sample, new CI) many times, 95% of the resulting intervals would contain μ. The interval is the random object; μ is fixed. Holding this picture clearly — the interval moves across repetitions, μ stays put — prevents the most common misinterpretation and builds the right foundation for hypothesis testing.
