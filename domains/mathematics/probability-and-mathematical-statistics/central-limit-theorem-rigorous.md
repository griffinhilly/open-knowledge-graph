---
id: central-limit-theorem-rigorous
title: Central Limit Theorem (Rigorous via Characteristic Functions)
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: characteristic-functions
  type: hard
- id: convergence-in-distribution
  type: hard
- id: multivariate-normal-distribution
  type: soft
- id: strong-law-of-large-numbers
  type: soft
builds-toward:
- maximum-likelihood-estimation-theory
- confidence-intervals-rigorous-theory
- asymptotic-normality-mle
tags:
- central-limit-theorem
- limit-theorems
- probability
stage: expert
status: validated
---
# Central Limit Theorem (Rigorous via Characteristic Functions)

## Core Idea
If {Xₙ} are i.i.d. with mean μ and variance σ², then (Sₙ - nμ)/(σ√n) converges in distribution to N(0,1). The rigorous proof uses characteristic functions: φₙ(t/√n) → e^{-t²/2} for all t. The CLT explains why the normal distribution is ubiquitous—sums of many independent random variables are approximately normal regardless of the original distribution.

## How It's Best Learned
Prove the CLT using characteristic functions. Apply the CLT to non-normal parent distributions to verify the approximation. Use the CLT to justify normal approximations in statistical inference.

## Common Misconceptions
- Thinking the CLT applies without finite variance; finite variance is required. - Assuming convergence means they are equal for all n; it is only in the limit. - Forgetting that convergence is in distribution, not almost sure.

## Questions

```yaml
- question: "The Cauchy distribution has a well-defined median but no finite variance. What does the CLT predict for the behavior of the standardized sum of n i.i.d. Cauchy variables as n → ∞?"
  type: multiple-choice
  options:
    - "By the CLT, the standardized sum converges to a standard normal distribution for large enough n"
    - "The standardized sum does not converge to a normal; it converges to another Cauchy distribution, because the finite variance condition of the CLT is violated"
    - "The CLT applies as long as the distribution has a finite mean, regardless of variance"
    - "The sum converges to a normal only if n exceeds some threshold that depends on the Cauchy scale parameter"
  answer: 1
  explanation: "The finite variance condition is not a technicality — it is load-bearing. The characteristic function proof requires the Taylor expansion φ_X(t/√n) = 1 − t²/(2n) + o(1/n), which depends on the second moment E[X²] being finite. For the Cauchy distribution, E[X²] is infinite; the second-order term in the Taylor expansion does not exist; and the argument that (1 − t²/2n)ⁿ → e^{−t²/2} fails entirely. Sums of Cauchy variables rescaled by n converge to another Cauchy, not to a normal. Options A and C state the misconception directly."

- question: "A statistics instructor says: 'The CLT means that if we repeatedly measure the same person's height, those individual measurements will be approximately normally distributed for large samples.' A student objects. Who is correct?"
  type: multiple-choice
  options:
    - "The instructor is correct — the CLT applies to any set of repeated measurements"
    - "The student is correct — the CLT is a statement about the distribution of sample means or standardized sums across many samples, not about the distribution of individual observations, which remain distributed according to their own distribution"
    - "Both are correct, since individual measurements have decreasing variance and thus approach normality"
    - "The instructor is correct if and only if the measurement errors happen to be normally distributed"
  answer: 1
  explanation: "The CLT says: the standardized sum (Sₙ − nμ)/(σ√n) converges in distribution to N(0,1). This is a statement about the distribution of the SUM across many independent replications — the sampling distribution. Individual observations Xᵢ remain drawn from whatever distribution X follows, whether normal or not. If heights follow a skewed distribution, repeated measurements of one person still follow that skewed distribution. The CLT's normality emerges only at the level of the aggregate."

- question: "If {Xₙ} are i.i.d. with finite variance, the Central Limit Theorem guarantees that for large n, each individual Xᵢ is approximately normally distributed."
  type: true-false
  answer: false
  explanation: "The CLT is a statement about the distribution of the standardized SUM (or equivalently the sample mean), not about individual observations. Each Xᵢ retains the distribution it was drawn from — exponential, uniform, Poisson, or anything else — regardless of n. What converges to normality is the distribution of (Sₙ − nμ)/(σ√n) as n → ∞. This distinction is crucial: 'the sampling distribution of the mean is approximately normal' is very different from 'individual observations are approximately normal.'"

- question: "In the characteristic function proof of the CLT, the finite variance assumption is essential because the proof requires the second-order term in the Taylor expansion of φ_X(t/√n), which only exists when E[X²] is finite."
  type: true-false
  answer: true
  explanation: "The proof expands φ_X(s) ≈ 1 − s²/2 + o(s²) around s = 0, using the fact that φ_X''(0) = −E[X²] = −σ² (after centering). This gives φ_X(t/√n) = 1 − t²/(2n) + o(1/n), which when raised to the n-th power yields e^{−t²/2}. If E[X²] is infinite, the second derivative of φ_X at 0 does not exist, the Taylor expansion has no t² term, and the entire argument collapses. Heavy-tailed distributions without finite variance produce sums that converge to stable distributions, not the normal."

- question: "Explain the distinction between 'convergence in distribution' and 'almost sure convergence,' and describe what the CLT's mode of convergence means for statistical inference."
  type: short-answer
  answer: "Almost sure convergence means the actual values of the random variables converge to the limit with probability 1 — the sequence of numbers Xₙ(ω) → L(ω) for almost every sample path ω. Convergence in distribution is weaker: only the CDFs converge, F_n(x) → F(x) at all continuity points of F. The individual random variables need not converge at all. The CLT uses convergence in distribution: the distribution of (Sₙ − nμ)/(σ√n) approaches the standard normal CDF, but individual observations remain distributed according to whatever their original distribution is. For inference, this means: for large n, you can use normal critical values (z-tables) to construct confidence intervals or perform hypothesis tests about sample means, because the sampling distribution of the mean is approximately normal. The approximation improves with n but is never exact unless the original distribution is normal."
  explanation: "Understanding the mode of convergence prevents two common errors: (1) thinking the CLT implies individual observations become normal (they don't), and (2) thinking the CLT gives exact rather than asymptotic results. The correct use is always: 'For large n, the sampling distribution of the mean is approximately N(μ, σ²/n),' and inference using this approximation is valid asymptotically."
```

## Explainer

You've studied **characteristic functions** — φ_X(t) = E[e^{itX}] — which encode all the distributional information about a random variable and behave nicely under sums (the characteristic function of a sum of independent variables is the product of their characteristic functions). You've also studied **convergence in distribution**, where a sequence of CDFs converges to a limiting CDF. The rigorous CLT proof combines these: it shows that the characteristic function of the standardized sum converges pointwise to e^{−t²/2}, the characteristic function of the standard normal, and then invokes the continuity theorem to conclude distributional convergence.

Here is the proof in outline. Without loss of generality, center and scale so that each Xᵢ has mean 0 and variance 1. The standardized sum is Sₙ/√n. Its characteristic function is φ_{Sₙ/√n}(t) = [φ_X(t/√n)]ⁿ. Now expand φ_X around 0: since E[X] = 0 and E[X²] = 1, the Taylor expansion gives φ_X(s) = 1 − s²/2 + o(s²). Substituting s = t/√n: φ_X(t/√n) = 1 − t²/(2n) + o(1/n). Raising to the n-th power: (1 − t²/(2n) + o(1/n))ⁿ → e^{−t²/2} for each fixed t. The **continuity theorem** then says: if the characteristic functions converge pointwise to the characteristic function of a distribution, the distributions converge in distribution. The standard normal has characteristic function e^{−t²/2}, so the result follows.

The **finite variance** condition is essential, not a mere technicality. The variance σ² appears as the coefficient in the Taylor expansion of φ_X: if variance is infinite, the second-order term is missing, the Taylor argument collapses, and the sum does not converge to a normal distribution. Instead, sums of heavy-tailed variables with infinite variance converge to **stable distributions** (of which the normal is a special case). The Cauchy distribution — whose variance is infinite — is the canonical example: sums of Cauchy variables rescaled by n give another Cauchy, not a normal. The CLT's universality is precisely bounded by the finite variance assumption.

Convergence **in distribution** — not almost sure, not in probability — is the correct mode here. The CLT says the *distribution* of (Sₙ − nμ)/(σ√n) approaches the standard normal. Individual observations remain drawn from whatever distribution they came from; what changes is the shape of the sampling distribution of the sum (or average). This is why "the CLT applies" in statistics means you can use normal critical values for large-sample inference: the sampling distribution of the sample mean is approximately normal. The approximation improves as n grows, but it is never exact for finite n (unless the original distribution is normal). Understanding this distinction — that the CLT is a statement about distributions, not individual outcomes — is the key to applying it correctly.
