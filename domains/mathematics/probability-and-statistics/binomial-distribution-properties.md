---
id: binomial-distribution-properties
title: 'Binomial Distribution: Properties and Applications'
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: binomial-distribution
  type: soft
- id: independence-of-events
  type: hard
builds-toward:
- normal-distribution-approximation
- hypothesis-testing-fundamentals
tags:
- binomial
stage: formal-systems
status: validated
---

# Binomial Distribution: Properties and Applications

## Core Idea
Binomial B(n,p): the number of successes in n independent trials with success probability p. PMF: P(X=k)=C(n,k)p^k(1−p)^{n-k}. E[X]=np, Var(X)=np(1−p). Used for count data and proportions; approximated by normal for large np and n(1−p).

## Questions

```yaml
- question: "A researcher models the number of left-handed people in a sample of 15 (p = 0.08) as Binomial(15, 0.08). A colleague suggests approximating with a normal distribution for easier calculation. Is this appropriate?"
  type: multiple-choice
  options:
    - "Yes — the normal approximation is valid whenever n ≥ 15"
    - "Yes — the normal approximation is always valid for binomial distributions"
    - "No — with p = 0.08, np = 1.2 and the distribution is strongly right-skewed; the Poisson approximation (λ = np) is more appropriate here"
    - "No — no approximations are valid for the binomial; the exact PMF must always be used"
  answer: 2
  explanation: "The normal approximation requires both np ≥ 10 and n(1−p) ≥ 10. Here np = 15 × 0.08 = 1.2, far below 10. The distribution is strongly right-skewed, and the normal assumption would badly misrepresent it. When p is small and n is moderate, the Poisson approximation with λ = np is much more accurate. Option D is overly restrictive — approximations are often valid and useful, just not the normal one in this case."

- question: "Why is the variance of the Binomial(n, p) distribution equal to np(1−p) and not simply np?"
  type: multiple-choice
  options:
    - "The (1−p) term is a correction for the trials that result in failure rather than success"
    - "Each Bernoulli trial has variance p(1−p), and because trials are independent, their variances add: Var(X) = n × p(1−p)"
    - "The formula is derived from subtracting the mean squared from E[X²] and involves a complex integral"
    - "The variance formula is empirical — it was observed to fit data and then adopted as a definition"
  answer: 1
  explanation: "X = B₁ + B₂ + ... + Bₙ where each Bᵢ is Bernoulli(p). A Bernoulli trial has variance E[B²] − (E[B])² = p − p² = p(1−p). Because trials are independent, variances add: Var(X) = n × p(1−p). Independence is essential here — unlike expectation (which is linear regardless of dependence), variance only adds when variables are independent. Option C is a mechanical description of the calculation, not the conceptual reason."

- question: "The variance of a Binomial(n, p) distribution is maximized when p = 0.5 and decreases toward zero as p approaches 0 or 1."
  type: true-false
  answer: true
  explanation: "Var(X) = np(1−p), and the factor p(1−p) is a downward-opening parabola in p, with maximum at p = 0.5 (giving p(1−p) = 0.25) and minimum of 0 at p = 0 and p = 1. Intuitively: if an event is near-certain or near-impossible, there is little variability in the count — outcomes are predictable. Maximum uncertainty occurs when success and failure are equally likely."

- question: "The normal approximation to a binomial distribution is accurate whenever n is large, regardless of the value of p."
  type: true-false
  answer: false
  explanation: "The normal approximation requires both np ≥ 10 and n(1−p) ≥ 10. If p is very small (e.g., p = 0.001), even n = 1000 gives np = 1, and the distribution is extremely right-skewed — far from normal. In this regime, the Poisson approximation (λ = np) is more accurate. Large n alone is insufficient; the distribution must be reasonably balanced, which requires both np and n(1−p) to be large."

- question: "The mean E[X] = np can be derived using linearity of expectation — and this derivation works even if the trials are not independent. Explain why independence is NOT required for the mean, but IS required for the variance."
  type: short-answer
  answer: "Linearity of expectation states E[A + B] = E[A] + E[B] for any random variables A and B, regardless of dependence. So E[X] = E[B₁ + ... + Bₙ] = E[B₁] + ... + E[Bₙ] = np, with no independence assumption needed. For variance, the corresponding rule Var(A + B) = Var(A) + Var(B) only holds when A and B are uncorrelated (and for independence in particular). If trials were positively correlated — e.g., in a cluster sampling scheme where knowing one person is left-handed increases the probability their sibling is — the true variance would exceed np(1−p). Independence ensures the trials don't 'pull' each other, allowing variances to simply add."
  explanation: "This distinction matters practically: if you incorrectly assume independence when designing a study (e.g., sampling family members), you will underestimate variance and produce confidence intervals that are too narrow, leading to false precision."
```

## Explainer

You already know the binomial distribution describes counting successes in independent trials. Now the goal is to build genuine intuition for *why* the mean and variance take their specific forms, and when the binomial distribution can be approximated by other distributions — intuition that will serve you in hypothesis testing and beyond.

The **mean** E[X] = np has a beautifully simple justification through your knowledge of independence of events. Each trial is a Bernoulli random variable Bᵢ with mean p. Since X = B₁ + B₂ + ... + Bₙ and the expected value of a sum is the sum of expected values (linearity of expectation holds regardless of dependence), E[X] = E[B₁] + ... + E[Bₙ] = np. No special tricks needed. The **variance** Var(X) = np(1−p) follows from the same decomposition: because the trials are independent, the variance of their sum equals the sum of their variances, and each Bernoulli trial has variance p(1−p). So Var(X) = np(1−p).

The shape of the binomial distribution changes dramatically with p. When p = 0.5, the distribution is perfectly symmetric. When p is close to 0, the distribution is strongly right-skewed — most of the probability sits near 0, with a long right tail. When p is close to 1, it's left-skewed. The **spread** np(1−p) is maximized at p = 0.5 and shrinks toward zero as p approaches 0 or 1 — which makes intuitive sense, since near-certain or near-impossible events leave little room for variability. The product np(1−p) is the binomial's signature: it appears in confidence interval formulas, standard error formulas for proportions, and power calculations, so recognizing it is a frequently useful skill.

The normal approximation works well when both np and n(1−p) are large (a common rule of thumb is both ≥ 10). The reasoning is the **Central Limit Theorem**: X is a sum of n independent, identically distributed Bernoulli trials, and the CLT says that such sums become approximately normal as n grows. The approximation breaks down when p is very small and n is moderate — in that regime, the **Poisson distribution** (with λ = np) is a better approximation. These two limiting cases — normal for balanced, large-n situations; Poisson for rare events — divide most binomial applications in practice, and knowing which approximation applies is as important as knowing the exact formula.
