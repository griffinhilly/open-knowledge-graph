---
id: asymptotic-normality-of-mle
title: Asymptotic Normality of the MLE
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: maximum-likelihood-estimation-theory
  type: hard
- id: central-limit-theorem-rigorous
  type: hard
- id: fisher-information
  type: soft
builds-toward:
- confidence-intervals-rigorous
tags:
- mle
- asymptotics
- normal-approximation
stage: advanced
status: validated
---

# Asymptotic Normality of the MLE

## Core Idea
Under regularity conditions, √n(θ̂_n - θ) converges in distribution to N(0, I(θ)^{-1}), so θ̂_n ≈ N(θ, I(θ)^{-1}/n) for large n. The convergence rate is √n and the asymptotic variance achieves the Cramér-Rao lower bound (asymptotic efficiency). This enables construction of confidence intervals and hypothesis tests.

## Questions

```yaml
- question: "A researcher uses two estimators for the same parameter θ. For large samples, the MLE achieves asymptotic variance I(θ)^{-1}/n. Estimator B achieves variance 2·I(θ)^{-1}/n. What does 'asymptotic efficiency' of the MLE mean in this context?"
  type: multiple-choice
  options:
    - "The MLE is faster to compute than estimator B"
    - "The MLE converges to θ at rate √n while estimator B converges at rate n"
    - "No unbiased estimator can achieve smaller asymptotic variance than the MLE, so estimator B is suboptimal"
    - "The MLE's asymptotic variance does not depend on the sample size"
  answer: 2
  explanation: "Asymptotic efficiency means the MLE achieves the Cramér-Rao lower bound asymptotically — the minimum variance any unbiased estimator can achieve for large n. Estimator B's variance of 2·I(θ)^{-1}/n is twice the minimum, making it asymptotically inefficient. This is a strong optimality result: in the large-sample limit, no unbiased estimator can improve on the MLE's variance."

- question: "Under regularity conditions, √n(θ̂_n − θ) → N(0, I(θ)^{-1}). A statistician has n = 400, θ̂_n = 3.0, and I(θ̂_n) = 16. Which expression gives the approximate 95% confidence interval?"
  type: multiple-choice
  options:
    - "3.0 ± 1.96 × 16"
    - "3.0 ± 1.96 / √(400 × 16)"
    - "3.0 ± 1.96 × 1/√16"
    - "3.0 ± 1.96 / √400"
  answer: 1
  explanation: "The asymptotic standard error of θ̂_n is 1/√(n·I(θ̂_n)) = 1/√(400 × 16) = 1/80 = 0.0125. The 95% CI is θ̂_n ± 1.96/√(n·I(θ̂_n)) = 3.0 ± 0.0245. Option D ignores the Fisher information; option C ignores n; option A uses I directly as the standard deviation, which is wrong. Higher Fisher information makes the interval much narrower — reflecting that this data is highly informative about θ."

- question: "The asymptotic normality theorem implies that θ̂_n is exactly normally distributed for any sample size n, provided the model is correctly specified."
  type: true-false
  answer: false
  explanation: "Asymptotic normality is a large-sample (n → ∞) approximation, not an exact finite-sample result. For any fixed n, θ̂_n may have a distribution very different from normal — skewed, heavy-tailed, or bounded — depending on the model. The theorem says the distribution converges to normal as n → ∞. In practice, how large n must be for the approximation to be adequate depends on the model and is an empirical question."

- question: "Higher Fisher information at the true parameter θ implies the MLE will be more precisely estimated asymptotically, since the asymptotic variance is I(θ)^{-1}/n."
  type: true-false
  answer: true
  explanation: "Fisher information measures how sensitive the log-likelihood is to changes in θ — equivalently, how much information the data carries about θ. Higher I(θ) means more curvature of the log-likelihood around the true value, so the MLE is more tightly concentrated around θ. The asymptotic variance I(θ)^{-1}/n is inversely proportional to I(θ), so higher information → smaller variance → more precise estimates. This is why experiments are designed to maximize Fisher information."

- question: "Why does the Fisher information appear in the asymptotic variance of the MLE? What would it mean for inference if a parameter had very low Fisher information?"
  type: short-answer
  answer: "Fisher information I(θ) = E[(∂log f/∂θ)²] is the variance of the score function — it measures how sharply the log-likelihood peaks at the true value. In the asymptotic normality proof, the numerator (scaled score) converges to N(0, I(θ)) via the CLT, and the denominator (scaled observed information) converges to I(θ). The resulting ratio has variance I(θ)^{-1}. Low Fisher information means the log-likelihood is nearly flat near θ — many parameter values fit the data about equally well — so the MLE is imprecise, confidence intervals are wide, and hypothesis tests have low power."
  explanation: "The connection between information and precision is the deep insight here. Fisher information quantifies what the data can tell us about θ. A nearly flat likelihood surface (low I(θ)) means the data doesn't strongly favor any particular parameter value; a sharply peaked surface (high I(θ)) pins down θ precisely. This is why the asymptotic variance is I(θ)^{-1}/n — information and variance are reciprocals of each other."
```

## Explainer

From the **Central Limit Theorem** (rigorous version), you know that the sample mean of i.i.d. random variables, properly scaled, converges to a normal distribution. The asymptotic normality of the MLE is the same phenomenon applied not to a simple average but to the maximizer of the log-likelihood. The result says: as the sample size n grows, the MLE θ̂_n behaves approximately like a normal random variable centered at the true parameter θ, with variance shrinking at rate 1/n. More precisely, the scaled deviation √n(θ̂_n − θ) converges in distribution to N(0, I(θ)⁻¹), where I(θ) is the **Fisher information** at the true parameter.

The proof sketch connects your prerequisites. The score function ∂log L/∂θ equals zero at the MLE (it is the first-order condition). Taylor-expanding the score around the true θ and rearranging gives: √n(θ̂_n − θ) ≈ [−(1/n)∂²log L/∂θ²]⁻¹ · [(1/√n)∂log L/∂θ]. The numerator — the scaled score — is a sum of i.i.d. terms with mean zero and variance I(θ), so by the CLT it converges to N(0, I(θ)). The denominator — the scaled observed Fisher information — converges to I(θ) by the law of large numbers. The ratio converges to N(0, I(θ)⁻¹). This argument is heuristic; the rigorous version requires regularity conditions (twice-differentiable log-likelihood, compact parameter space, identifiability) to justify the interchange of limit and differentiation.

The **Fisher information** I(θ) = E[(∂log f(X;θ)/∂θ)²] is the variance of the score — it measures how sensitively the log-likelihood changes as θ moves. High Fisher information means the data is very informative about θ, so the MLE can pin down θ precisely: the asymptotic variance I(θ)⁻¹ is small. Low Fisher information means the data carries little signal about θ, and the MLE's variance is large. This is not accidental — the **Cramér-Rao lower bound** says no unbiased estimator can have variance below I(θ)⁻¹/n. The MLE achieves this lower bound asymptotically, making it **asymptotically efficient**: in the large-sample limit, no competing estimator can have smaller variance.

This result is the workhorse of frequentist inference. Because θ̂_n ≈ N(θ, I(θ̂_n)⁻¹/n) for large n, you can construct approximate **confidence intervals**: θ̂_n ± z_{α/2} / √(n · I(θ̂_n)). You can test hypotheses using Wald statistics: n(θ̂_n − θ₀)² · I(θ̂_n) ≈ χ²(1) under H₀: θ = θ₀. The entire architecture of large-sample likelihood inference rests on this one asymptotic distribution result — it converts the MLE from a point estimate into a gateway to intervals and tests.
