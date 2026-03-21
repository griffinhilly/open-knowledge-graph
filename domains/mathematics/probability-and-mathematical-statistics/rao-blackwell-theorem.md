---
id: rao-blackwell-theorem
title: Rao-Blackwell Theorem
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: umvue
  type: soft
- id: conditional-expectation
  type: hard
- id: sufficient-statistics
  type: hard
builds-toward:
- bayesian-point-estimation
tags:
- rao-blackwell
- unbiased-estimation
- statistics
stage: advanced
status: draft
---

# Rao-Blackwell Theorem

## Core Idea
If T is an unbiased estimator of θ and S is a sufficient statistic, then φ = E[T|S] is unbiased for θ and Var(φ) ≤ Var(T). This theorem shows how to improve unbiased estimators by conditioning on sufficient statistics. Combined with completeness, it yields UMVUEs.

## Questions

```yaml
- question: "You have an unbiased estimator T of the mean μ of a normal distribution, and S = X̄ is the sufficient statistic. After Rao-Blackwellization, φ = E[T | X̄]. Which claim about φ is correct?"
  type: multiple-choice
  options:
    - "φ is biased because conditioning on S changes the expected value of T"
    - "φ has higher variance than T because averaging over the conditioning introduces extra randomness"
    - "φ is unbiased with variance ≤ Var(T); if T = X₁, then φ = X̄ with variance σ²/n instead of σ²"
    - "φ equals T with probability one, so the theorem has no content in this case"
  answer: 2
  explanation: "The law of total expectation preserves unbiasedness: E[φ] = E[E[T|S]] = E[T] = μ. The variance decomposition Var(T) = Var(E[T|S]) + E[Var(T|S)] shows variance can only decrease or stay the same — the extra term E[Var(T|S)] is the noise in T irrelevant to θ. In the normal example, E[X₁ | X̄] = X̄, reducing variance from σ² to σ²/n. Option A mistakes the law of total expectation; option B reverses the variance inequality."

- question: "What role does the sufficient statistic play in the Rao-Blackwell argument?"
  type: multiple-choice
  options:
    - "It provides a lower bound on the variance of any unbiased estimator"
    - "It captures all parameter information in the data, so conditioning on it removes noise irrelevant to θ without losing signal"
    - "It automatically guarantees the conditioned estimator will be the UMVUE without any additional assumptions"
    - "It replaces the unknown parameter θ with a known quantity, enabling exact variance calculations"
  answer: 1
  explanation: "Sufficiency means the conditional distribution of the data given S does not depend on θ — S has already extracted all the θ-relevant information. So conditioning T on S averages away the part of T's variability that is unrelated to θ (the 'bad variance'), while keeping the part that tracks θ (the 'good variance'). Option C is wrong: completeness of S is additionally required for the result to be the UMVUE (Lehmann-Scheffé theorem)."

- question: "If T is an unbiased estimator and S is a sufficient statistic, then E[T|S] has variance no greater than Var(T)."
  type: true-false
  answer: true
  explanation: "This follows directly from the variance decomposition: Var(T) = Var(E[T|S]) + E[Var(T|S)]. Since E[Var(T|S)] ≥ 0, we have Var(E[T|S]) ≤ Var(T). Equality holds when T is already a function of S — when no irrelevant noise exists to remove. This is the core guarantee of the Rao-Blackwell theorem."

- question: "The Rao-Blackwell theorem guarantees that conditioning any unbiased estimator on a sufficient statistic always produces the UMVUE."
  type: true-false
  answer: false
  explanation: "Rao-Blackwellization guarantees an improvement (or no change) in variance, but the result is the UMVUE only when the sufficient statistic is also complete. The Lehmann-Scheffé theorem provides the extra step: if the sufficient statistic is complete, then any unbiased function of it is the unique UMVUE. Without completeness, the conditioned estimator may be improvable further, and multiple different unbiased functions of S with different variances could exist."

- question: "Explain intuitively why conditioning an unbiased estimator T on a sufficient statistic S reduces variance."
  type: short-answer
  answer: "Any estimator T has two kinds of variability: fluctuations that carry information about θ (captured by S) and random noise unrelated to θ. Since S extracts all the θ-relevant information, E[T|S] averages away the irrelevant noise while preserving the signal. The variance decomposition makes this precise: Var(T) = Var(E[T|S]) + E[Var(T|S)], where E[Var(T|S)] is the 'wasted variance' not connected to θ. Conditioning eliminates this term."
  explanation: "The intuition is that T is doing two jobs: tracking θ and varying randomly for reasons unrelated to θ. A sufficient statistic has already done the first job optimally. Conditioning T on S extracts only what T knows about θ, discarding the rest. The result is an estimator with the same expected value but smaller variance — the same signal with less noise."
```

## Explainer

You've studied **sufficient statistics** — statistics S(X) that capture all the information in the data about the parameter θ, in the sense that the conditional distribution of the data given S does not depend on θ. You've also studied **conditional expectation** — E[T|S], the expected value of T after averaging over everything not captured by S. The Rao-Blackwell theorem puts these together: if you start with any unbiased estimator T and condition it on a sufficient statistic S, you get a new estimator that is at least as good, and often better.

The construction is this: define φ(S) = E[T|S]. Three properties follow immediately. First, **unbiasedness is preserved**: E[φ(S)] = E[E[T|S]] = E[T] = θ by the law of total expectation. Second, **φ depends only on S**: since S is sufficient, conditioning on S yields a distribution free of θ, so the conditional expectation is a well-defined function of S alone. Third, **variance cannot increase**: by the variance decomposition formula, Var(T) = Var(E[T|S]) + E[Var(T|S)] = Var(φ) + E[Var(T|S)] ≥ Var(φ). The extra term E[Var(T|S)] is the "noise" in T that is unrelated to θ — conditioning removes it.

The intuition is that any unbiased estimator T contains two kinds of variability: fluctuations that carry information about θ (good variance) and fluctuations that are irrelevant noise (bad variance). The sufficient statistic S has already extracted all the information. Conditioning T on S averages away the irrelevant noise while preserving the signal, producing an estimator with the same mean but lower variance. A simple example: suppose you want to estimate the mean of a normal population, and T is just the first observation X₁ — unbiased but high-variance. The sufficient statistic for this model is the sample mean X̄. Then E[X₁ | X̄] = X̄, and the Rao-Blackwellized estimator is the sample mean itself, which has variance σ²/n instead of σ².

Combined with **completeness** of the sufficient statistic, the theorem yields the UMVUE (Uniformly Minimum Variance Unbiased Estimator) via the Lehmann-Scheffé theorem: if a complete sufficient statistic S exists and you condition any unbiased estimator on S, the result is the unique UMVUE — no unbiased estimator can have smaller variance for any value of θ. The Rao-Blackwell theorem is the engine: start with any unbiased estimator (easy to find), condition on the sufficient statistic (always improves or maintains variance), and completeness guarantees the result is optimal.
