---
id: asymptotic-normality-mle
title: Asymptotic Normality of MLEs
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: consistency-of-estimators
  type: hard
- id: central-limit-theorem-rigorous
  type: hard
- id: fisher-information
  type: hard
builds-toward:
- umvue
- confidence-intervals-rigorous-theory
tags:
- asymptotic-normality
- mle
- asymptotics
stage: expert
status: validated
---

# Asymptotic Normality of MLEs

## Core Idea
Under regularity conditions, √n(θ̂ₙ - θ) converges in distribution to N(0, 1/I(θ)), where I(θ) is Fisher information. This shows MLEs are asymptotically normal and efficient (achieving the Cramer-Rao bound asymptotically). Asymptotic normality enables hypothesis tests and confidence intervals for MLEs.

## Questions

```yaml
- question: "A statistician fits an MLE to data from a Uniform(0, θ) distribution and uses √n(θ̂_n − θ) → N(0, 1/I(θ)) to construct a confidence interval. Why is this reasoning invalid?"
  type: multiple-choice
  options:
    - "The MLE for Uniform(0, θ) is biased, and asymptotic normality applies only to unbiased estimators"
    - "The Uniform(0, θ) model violates the regularity conditions for asymptotic normality — the support depends on θ, the log-likelihood is not differentiable at the boundary, and the MLE converges at rate n (not √n) to a non-normal limit"
    - "The Cramér-Rao bound is undefined for uniform distributions, making the variance formula 1/I(θ) inapplicable"
    - "The Fisher information for Uniform(0, θ) is infinite, which makes the asymptotic variance undefined"
  answer: 1
  explanation: "The standard asymptotic normality theorem requires regularity conditions including: support of the distribution must not depend on the parameter, and the log-likelihood must be twice differentiable. For Uniform(0, θ), the support [0, θ] changes with θ — the boundary of the sample space moves. The MLE is the maximum order statistic X_(n), which converges at rate n (not √n) to an exponential distribution. This is a classic exception illustrating why the regularity conditions are not merely technical fine print — their failure changes both the rate and the limit distribution."

- question: "The statement that the MLE is 'asymptotically efficient' means:"
  type: multiple-choice
  options:
    - "No estimator can have lower variance than the MLE for any sample size, including small samples"
    - "The MLE achieves exactly the Cramér-Rao lower bound in all finite samples under the model assumptions"
    - "Among all consistent, asymptotically normal estimators, the MLE achieves the smallest possible asymptotic variance — equal to 1/(nI(θ)) — in the limit as n → ∞"
    - "The MLE converges to the true parameter faster than any other estimator for all distributions"
  answer: 2
  explanation: "Asymptotic efficiency is a large-sample statement. The Cramér-Rao bound 1/(nI(θ)) is the minimum variance for unbiased estimators; the MLE saturates this bound in the limit. However, in finite samples, the MLE can be outperformed by other estimators, may be biased, and may not attain the bound. Options A and B are incorrect because they assert finite-sample properties that the asymptotic result does not guarantee. The qualifier 'asymptotically' carries the entire weight of the claim."

- question: "The asymptotic normality of the MLE follows, via a Taylor expansion of the score function, from applying the central limit theorem to individual score contributions ℓ'(θ; Xᵢ), which have mean zero and variance I(θ) under regularity conditions."
  type: true-false
  answer: true
  explanation: "The proof structure is exactly this: the score function S_n(θ) = Σ ℓ'(θ; Xᵢ) is a sum of i.i.d. terms with E[ℓ'(θ;X)] = 0 and Var[ℓ'(θ;X)] = I(θ). By the CLT, (1/√n)S_n(θ) → N(0, I(θ)). A Taylor expansion around the MLE, combined with the WLLN applied to the second derivative (which converges to −I(θ)), yields √n(θ̂_n − θ) → N(0, 1/I(θ)). The CLT is applied to the score function — not the log-likelihood directly — and this is the key structural step."

- question: "If the MLE is asymptotically normal with variance 1/(nI(θ)), then it achieves the Cramér-Rao lower bound in finite samples."
  type: true-false
  answer: false
  explanation: "Asymptotic normality and efficiency are limit statements — they describe behavior as n → ∞, not at any fixed sample size. In finite samples, the MLE may be biased, may not attain the Cramér-Rao bound, and may be outperformed by other estimators. The practical significance of asymptotic efficiency is that for sufficiently large n, no consistent asymptotically normal estimator can systematically beat the MLE in variance. The word 'asymptotically' is not decorative — it is the entire content of the claim."

- question: "What is the significance of Fisher information I(θ) appearing as the asymptotic variance in √n(θ̂_n − θ) → N(0, 1/I(θ)), and what does this tell us about the MLE relative to other estimators?"
  type: short-answer
  answer: "Fisher information quantifies how much information each observation carries about θ; the Cramér-Rao bound states that no unbiased estimator can have variance below 1/(nI(θ)). The fact that the MLE's asymptotic variance is exactly 1/I(θ) means the MLE saturates this bound in the limit — it extracts the maximum possible statistical information from the data. Among all consistent, asymptotically normal estimators, no other estimator can achieve a smaller asymptotic variance. This makes the MLE asymptotically optimal in a precise sense."
  explanation: "The Fisher information appears naturally from the proof: the variance of the score function is I(θ), and the WLLN tells us the second derivative of the log-likelihood converges to −I(θ). The ratio of these two quantities gives 1/I(θ) as the asymptotic variance — a consequence of the mathematical structure of maximum likelihood, not a coincidence. The Cramér-Rao bound and the MLE's limit variance are the same quantity because the score function is both the ingredient of the CLT in the proof and the definition of Fisher information."
```

## Explainer

Your three prerequisites each contribute something essential here. From **consistency of estimators**, you know θ̂_n → θ in probability as n → ∞ — the MLE converges to the true parameter. From the **central limit theorem (rigorous)**, you know that properly normalized sums of i.i.d. random variables converge in distribution to a normal. From **Fisher information** I(θ), you know it quantifies how much information each observation carries about θ, and that the Cramér-Rao bound says no unbiased estimator can have variance less than 1/(n I(θ)). Asymptotic normality of MLEs ties all three together: not only does the MLE converge, but the normalized deviation √n(θ̂_n − θ) has a specific, computable limiting distribution — N(0, 1/I(θ)).

The proof sketch is a Taylor expansion of the **score function** S(θ) = ∂/∂θ log L(θ; X₁,…,X_n) = Σᵢ ℓ'(θ; Xᵢ). At the MLE θ̂_n, the score is zero by definition. Taylor-expanding around the true θ: Σ ℓ'(θ; Xᵢ) + (θ̂_n − θ) Σ ℓ''(θ; Xᵢ) ≈ 0. Solving for (θ̂_n − θ): it equals −(Σ ℓ'(θ; Xᵢ)) / (Σ ℓ''(θ; Xᵢ)). The numerator, normalized by 1/√n, converges to N(0, I(θ)) by the CLT (since E[ℓ'(θ;X)] = 0 and Var[ℓ'(θ;X)] = I(θ)). The denominator divided by n converges to −I(θ) by the WLLN and the identity E[ℓ''(θ;X)] = −I(θ). After normalization, the ratio converges in distribution to N(0, 1/I(θ)).

The result says the MLE is **asymptotically efficient**: among all consistent, asymptotically normal estimators, it achieves the smallest possible asymptotic variance — exactly the Cramér-Rao bound. This is not a finite-sample claim; small samples can behave poorly. But for large n, no estimator can systematically beat the MLE in variance. The practical payoff is immediate: since √n(θ̂_n − θ) ≈ N(0, 1/I(θ)), an approximate 95% confidence interval for θ is θ̂_n ± 1.96/√(n·Î(θ)), where Î(θ) is Fisher information evaluated at the MLE.

Understanding the regularity conditions that support this result is as important as the result itself. The conditions — differentiability of the log-likelihood, identifiability of θ, finite Fisher information, interchange of differentiation and integration — can fail. When they do, for example with the Uniform(0, θ) model where the MLE is the maximum order statistic, the MLE may converge at a rate different from √n and to a non-normal limit distribution. Asymptotic normality is the generic case, but its exceptions teach you what makes estimation problems genuinely hard.
