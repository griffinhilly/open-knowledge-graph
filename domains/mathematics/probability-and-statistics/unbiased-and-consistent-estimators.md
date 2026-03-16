---
id: unbiased-and-consistent-estimators
title: Unbiased and Consistent Estimators
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: point-estimators-properties
  type: hard
builds-toward:
- confidence-intervals-framework
tags:
- estimation
- unbiased
- consistency
stage: formal-systems
status: draft
---

# Unbiased and Consistent Estimators

## Core Idea
An estimator is unbiased if its expected value equals the parameter: E[θ̂] = θ. An estimator is consistent if it converges in probability to the parameter as n → ∞. Unbiasedness is a finite-sample property; consistency is asymptotic.

## How It's Best Learned
Prove unbiasedness and consistency for sample mean and sample variance. Compare estimators: sample variance (unbiased but inconsistent-adjacent concept) versus MLE. Understand why both properties matter.

## Common Misconceptions
Thinking unbiasedness implies consistency or vice versa. Assuming all standard estimators are unbiased. Confusing 'unbiased' with 'accurate' (unbiased estimators can have high variance).

## Explainer

Your prerequisite on estimator properties introduced unbiasedness and consistency as two separate desiderata. Here we go deeper into what each property really means, why they are independent of each other, and why that independence matters enormously in practice.

**Unbiasedness** is a statement about averages over repeated samples of fixed size n. An estimator θ̂ is unbiased if E[θ̂] = θ for every possible true value of θ — not just one particular θ, but for all of them. The sample mean X̄ satisfies this: no matter what the true mean μ is, averaging over all datasets of size n gives exactly μ. The corrected sample variance S² = Σ(Xᵢ − X̄)²/(n−1) is unbiased for σ² — the (n−1) denominator exists precisely to fix the bias introduced by using X̄ instead of the unknown μ. Had we divided by n instead, we would get a **biased** estimator: E[Σ(Xᵢ − X̄)²/n] = (n−1)σ²/n < σ². The bias is −σ²/n, which shrinks as n grows.

**Consistency** is a statement about what happens as n → ∞. An estimator is consistent if for any ε > 0, P(|θ̂ − θ| > ε) → 0 as n grows. Intuitively: with enough data, you will almost certainly be within any specified error tolerance. Consistency does not require unbiasedness — the biased MLE of σ² (dividing by n) is consistent, because the bias −σ²/n → 0. More generally, an estimator is consistent whenever its bias shrinks to zero and its variance shrinks to zero.

The two properties are genuinely independent. Construct a pathological example: take the estimator "θ̂ = X₁ always, regardless of n" — this uses only the first observation and discards all other data. It may be unbiased (E[X₁] = μ), but it is not consistent: its distribution never concentrates around μ as n grows. Conversely, take θ̂ = X̄ + c/n for any constant c ≠ 0: this is biased (E[θ̂] = μ + c/n ≠ μ) but consistent (bias and variance both → 0). The lesson is that unbiasedness is a finite-sample guarantee — "on average, I'm right at this sample size" — while consistency is an asymptotic guarantee — "I'll converge to the truth with enough data." Both are valuable; neither implies the other.

In practice, the distinction matters most when evaluating maximum likelihood estimators. MLEs are typically consistent and asymptotically efficient (they achieve the Cramér-Rao bound as n → ∞), but they are often biased at finite samples. This is an acceptable tradeoff in large-sample settings. When samples are small, unbiasedness may be more important — you cannot wait for asymptotics to rescue you. The deeper point, connecting to your upcoming work on confidence intervals, is that neither property alone tells you everything: an unbiased estimator with high variance gives wide confidence intervals; a consistent estimator with slow convergence may behave poorly at any realistic sample size. True evaluation requires considering the full sampling distribution, not just bias or consistency in isolation.
