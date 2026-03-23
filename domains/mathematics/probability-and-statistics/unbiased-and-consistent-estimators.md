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
status: validated
---

# Unbiased and Consistent Estimators

## Core Idea
An estimator is unbiased if its expected value equals the parameter: E[θ̂] = θ. An estimator is consistent if it converges in probability to the parameter as n → ∞. Unbiasedness is a finite-sample property; consistency is asymptotic.

## How It's Best Learned
Prove unbiasedness and consistency for sample mean and sample variance. Compare estimators: sample variance (unbiased but inconsistent-adjacent concept) versus MLE. Understand why both properties matter.

## Common Misconceptions
Thinking unbiasedness implies consistency or vice versa. Assuming all standard estimators are unbiased. Confusing 'unbiased' with 'accurate' (unbiased estimators can have high variance).

## Questions

```yaml
- question: "An estimator θ̂ is defined as 'always return the first observation X₁, regardless of how many observations are collected.' Which properties does this estimator have?"
  type: multiple-choice
  options:
    - "It is both unbiased and consistent"
    - "It is unbiased but not consistent"
    - "It is consistent but not unbiased"
    - "It is neither unbiased nor consistent"
  answer: 1
  explanation: "E[X₁] = μ for any sample size n, so the estimator is unbiased — it hits the true mean on average. But its distribution never concentrates around μ as n grows; it always has variance σ². Consistency requires P(|θ̂ − θ| > ε) → 0 as n → ∞, which fails here because no data beyond X₁ is ever used. This is the clearest demonstration that unbiasedness does not imply consistency."

- question: "The MLE for a normal distribution's variance divides by n rather than n−1. How would you characterize this estimator?"
  type: multiple-choice
  options:
    - "Unbiased and consistent — MLE guarantees both properties in large samples"
    - "Biased and inconsistent — the n denominator creates error that never disappears"
    - "Biased but consistent — the bias is −σ²/n which shrinks to zero as n grows"
    - "Unbiased but inconsistent — the large-sample properties of MLE correct the bias"
  answer: 2
  explanation: "The MLE variance estimator has E[θ̂] = (n−1)σ²/n ≠ σ², so it is biased by −σ²/n at every finite n. But as n → ∞, this bias shrinks to 0 and the variance of the estimator also shrinks — so it converges in probability to σ². This is the canonical example of a consistent but biased estimator, showing directly that consistency does not require unbiasedness."

- question: "An unbiased estimator is always more accurate than a biased estimator for the same parameter."
  type: true-false
  answer: false
  explanation: "Unbiasedness means E[θ̂] = θ — on average, you're right. But an unbiased estimator can have very high variance, meaning individual estimates scatter widely around the true value. A slightly biased estimator with much lower variance can produce estimates consistently closer to the truth in practice. Accuracy in the sense of mean squared error depends on both bias and variance (MSE = Bias² + Variance), and reducing variance sometimes justifies accepting some bias."

- question: "An estimator can be unbiased at every fixed sample size n while still failing to converge to the true parameter as n → ∞."
  type: true-false
  answer: true
  explanation: "The 'always return X₁' estimator demonstrates this. It is unbiased for every n (E[X₁] = μ regardless of sample size), but its distribution never concentrates around μ — its variance is always σ². Consistency requires the distribution to collapse around the true value as n grows; unbiasedness only requires the mean of that distribution to be correct at each fixed n. These are completely different requirements."

- question: "Why are unbiasedness and consistency described as 'independent' properties? Give an example showing that one does not imply the other."
  type: short-answer
  answer: "They are independent because each concerns a different aspect of an estimator's behavior at different scales. Unbiasedness is a finite-sample property: E[θ̂] = θ at each fixed n. Consistency is asymptotic: the estimator converges in probability to θ as n → ∞. Example of unbiased but inconsistent: θ̂ = X₁ (always use the first observation) — E[X₁] = μ for all n, but its variance never shrinks. Example of consistent but biased: MLE for variance (divides by n) has bias −σ²/n → 0, so it converges even though it's biased at every finite n."
  explanation: "The independence of these properties is practically important: in small-sample settings, unbiasedness may matter more (you can't wait for asymptotics); in large-sample settings, consistency and efficiency (asymptotic variance) often matter more than finite-sample unbiasedness."
```

## Explainer

Your prerequisite on estimator properties introduced unbiasedness and consistency as two separate desiderata. Here we go deeper into what each property really means, why they are independent of each other, and why that independence matters enormously in practice.

**Unbiasedness** is a statement about averages over repeated samples of fixed size n. An estimator θ̂ is unbiased if E[θ̂] = θ for every possible true value of θ — not just one particular θ, but for all of them. The sample mean X̄ satisfies this: no matter what the true mean μ is, averaging over all datasets of size n gives exactly μ. The corrected sample variance S² = Σ(Xᵢ − X̄)²/(n−1) is unbiased for σ² — the (n−1) denominator exists precisely to fix the bias introduced by using X̄ instead of the unknown μ. Had we divided by n instead, we would get a **biased** estimator: E[Σ(Xᵢ − X̄)²/n] = (n−1)σ²/n < σ². The bias is −σ²/n, which shrinks as n grows.

**Consistency** is a statement about what happens as n → ∞. An estimator is consistent if for any ε > 0, P(|θ̂ − θ| > ε) → 0 as n grows. Intuitively: with enough data, you will almost certainly be within any specified error tolerance. Consistency does not require unbiasedness — the biased MLE of σ² (dividing by n) is consistent, because the bias −σ²/n → 0. More generally, an estimator is consistent whenever its bias shrinks to zero and its variance shrinks to zero.

The two properties are genuinely independent. Construct a pathological example: take the estimator "θ̂ = X₁ always, regardless of n" — this uses only the first observation and discards all other data. It may be unbiased (E[X₁] = μ), but it is not consistent: its distribution never concentrates around μ as n grows. Conversely, take θ̂ = X̄ + c/n for any constant c ≠ 0: this is biased (E[θ̂] = μ + c/n ≠ μ) but consistent (bias and variance both → 0). The lesson is that unbiasedness is a finite-sample guarantee — "on average, I'm right at this sample size" — while consistency is an asymptotic guarantee — "I'll converge to the truth with enough data." Both are valuable; neither implies the other.

In practice, the distinction matters most when evaluating maximum likelihood estimators. MLEs are typically consistent and asymptotically efficient (they achieve the Cramér-Rao bound as n → ∞), but they are often biased at finite samples. This is an acceptable tradeoff in large-sample settings. When samples are small, unbiasedness may be more important — you cannot wait for asymptotics to rescue you. The deeper point, connecting to your upcoming work on confidence intervals, is that neither property alone tells you everything: an unbiased estimator with high variance gives wide confidence intervals; a consistent estimator with slow convergence may behave poorly at any realistic sample size. True evaluation requires considering the full sampling distribution, not just bias or consistency in isolation.
