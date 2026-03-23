---
id: confidence-intervals-proportions-theory
title: Confidence Intervals for Proportions
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: binomial-distribution-properties
  type: hard
- id: central-limit-theorem-theory
  type: hard
builds-toward:
- hypothesis-testing-fundamentals
tags:
- confidence-interval
- proportions
stage: formal-systems
status: validated
---

# Confidence Intervals for Proportions

## Core Idea
Sample proportion p̂=X/n has approximately N(p, p(1−p)/n) distribution when np≥10 and n(1−p)≥10. CI: p̂±z_{α/2}√(p̂(1−p̂)/n). Exact methods (Clopper-Pearson) preferred when normality conditions fail.

## Questions

```yaml
- question: "A researcher finds 3 infections among 80 people surveyed (p̂ ≈ 0.0375). Should they use the standard Normal-based confidence interval formula?"
  type: multiple-choice
  options:
    - "Yes — the sample size of 80 is large enough for the Normal approximation"
    - "No — np = 80 × 0.0375 = 3, which is less than 10, so the Clopper-Pearson exact method is preferred"
    - "Yes — as long as n > 30, the CLT guarantees the Normal approximation is valid"
    - "No — you need at least n = 1000 before any confidence interval method is valid for proportions"
  answer: 1
  explanation: "The condition for using the Normal-based formula is np ≥ 10 AND n(1−p) ≥ 10. Here np = 3, which fails the condition. With so few expected successes, the Binomial distribution is heavily right-skewed — the Normal approximation is poor and the resulting interval may have much less than the nominal 95% coverage. The Clopper-Pearson interval uses the Binomial distribution directly and is appropriate when the Normal approximation conditions fail. The '30 observations' rule of thumb applies to means, not proportions."

- question: "A 95% confidence interval for a proportion is computed as (0.42, 0.58). Which interpretation is correct?"
  type: multiple-choice
  options:
    - "There is a 95% probability that the true population proportion is between 0.42 and 0.58"
    - "95% of the population falls between 0.42 and 0.58"
    - "If this sampling procedure were repeated many times, 95% of the resulting intervals would contain the true proportion"
    - "The sample proportion p̂ equals 0.50 with 95% certainty"
  answer: 2
  explanation: "The correct frequentist interpretation refers to the procedure, not this specific interval. The true proportion is fixed (not random), so it either is or isn't in (0.42, 0.58) — we just don't know which. The '95%' refers to the long-run performance of the method: 95% of intervals constructed this way will capture the true p. Option A is the most common misconception — treating a fixed parameter as if it has a probability distribution relative to a single computed interval."

- question: "The margin of error for a 95% confidence interval for a proportion is maximized when p̂ = 0.5."
  type: true-false
  answer: true
  explanation: "The margin of error is z_{α/2} √(p̂(1−p̂)/n). The term p̂(1−p̂) is maximized when p̂ = 0.5, giving 0.5 × 0.5 = 0.25. Any other value of p̂ gives a smaller product: e.g., 0.1 × 0.9 = 0.09, and 0.9 × 0.1 = 0.09. This is why a sample size calculated assuming p̂ = 0.5 is the conservative (largest) choice — it guarantees sufficient precision regardless of what the true proportion turns out to be."

- question: "Doubling the sample size halves the margin of error in a confidence interval for a proportion."
  type: true-false
  answer: false
  explanation: "The margin of error is proportional to 1/√n, not 1/n. Doubling n replaces √n with √(2n) = √2 · √n, reducing the margin by a factor of √2 ≈ 1.41 — a reduction of about 29%, not 50%. To halve the margin of error, you must quadruple the sample size. This square-root relationship means precision is expensive: each additional decimal place of accuracy requires a 100× increase in sample size."

- question: "Why do we substitute p̂ for p in the standard error formula √(p(1−p)/n) when constructing a confidence interval, and what does this introduce?"
  type: short-answer
  answer: "We substitute p̂ because p — the true population proportion — is unknown. That is precisely what we are trying to estimate. Using p̂ in its place produces an estimated standard error: SE = √(p̂(1−p̂)/n). This introduces additional uncertainty, since p̂ itself is a random variable that fluctuates across samples. In large samples, p̂ is close to p and this substitution works well. In small samples or when p is near 0 or 1, the approximation degrades, which is part of why the Normal-based interval requires the conditions np ≥ 10 and n(1−p) ≥ 10."
  explanation: "This substitution is sometimes called the 'plug-in principle' and is a common technique in statistics. The resulting interval is called the Wald interval. Its coverage can be poor for small n or extreme p precisely because the estimated SE is unreliable there. The Clopper-Pearson interval avoids this by inverting exact Binomial tail probabilities without needing to estimate the standard error from the data."
```

## Explainer

You know from the Central Limit Theorem that sample means of i.i.d. observations are approximately normally distributed for large n. A sample proportion p̂ = X/n is a special case: X counts successes in n Bernoulli trials, so X ~ Binomial(n, p). Each trial contributes either 0 or 1 to the sum, and p̂ is the mean of these 0-1 observations. By the CLT, p̂ ≈ N(p, p(1−p)/n) — the true proportion p is the mean of the Bernoulli, and p(1−p) is its variance, so the standard error of p̂ is √(p(1−p)/n).

The confidence interval formula follows directly from this approximation. A 95% confidence interval for a Normal mean is point estimate ± 1.96 × (standard error). Since we don't know p (that's what we're estimating), we plug in p̂ in its place: CI = p̂ ± z_{α/2} √(p̂(1−p̂)/n). Here z_{α/2} is the z-critical value for the desired confidence level — 1.96 for 95%, 2.576 for 99%. The **margin of error** is the ± part: it tells you the half-width of the interval.

The conditions np ≥ 10 and n(1−p) ≥ 10 (sometimes stated as np ≥ 5) ensure the Binomial is well-approximated by the Normal. Intuitively, if p = 0.01 and n = 50, then you'd expect only 0.5 successes on average — the distribution is heavily skewed toward zero, and the Normal approximation is poor. These conditions require enough expected successes *and* expected failures for the distribution to look roughly symmetric and bell-shaped. When they fail, the Normal-based interval can have poor **coverage** — the actual proportion of intervals containing the true p may be much less than the nominal 95%.

In that case, the **Clopper-Pearson interval** (also called the "exact" binomial interval) uses the Binomial distribution directly rather than the Normal approximation. It constructs the interval by finding the values of p that make the observed count X neither too extreme in the lower tail nor the upper tail. Clopper-Pearson is conservative — its actual coverage is always at least the nominal level — but it tends to be wider than necessary. This is the fundamental tradeoff: the approximate Normal interval is narrower and simpler but unreliable for small n or extreme p; the exact interval is always valid but wider.

A useful fact: the margin of error is maximized when p̂ = 0.5, giving maximum margin = z_{α/2} / (2√n). For a 95% CI and n = 1000, this is approximately 1.96/(2·31.6) ≈ 0.031 — about 3 percentage points. This is why political polls with "margin of error ±3%" typically use roughly 1,000 respondents. Doubling the precision (halving the margin) requires quadrupling n — the square root in the denominator means precision is expensive to buy with sample size alone.
