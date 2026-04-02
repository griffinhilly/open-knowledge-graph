---
id: confidence-intervals-rigorous-theory
title: Confidence Intervals (Rigorous Theory)
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: asymptotic-normality-mle
  type: hard
- id: uniformly-most-powerful-tests
  type: soft
builds-toward:
- bayesian-inference-foundations
tags:
- confidence-intervals
- interval-estimation
- statistics
stage: expert
status: validated
---

# Confidence Intervals (Rigorous Theory)

## Core Idea
A (1-α) confidence interval [L(X), U(X)] for θ satisfies P(L(X) ≤ θ ≤ U(X)) = 1 - α. Confidence intervals can be inverted from hypothesis tests: the (1-α) CI is {θ: θ is not rejected at level α}. Shortest confidence intervals use the critical region from the UMP test. Asymptotic CIs rely on asymptotic normality of estimators.

## Questions

```yaml
- question: "After computing a 95% CI from her data, a statistician reports: 'There is a 95% probability that the true parameter μ lies between 2.1 and 4.7.' What is wrong with this statement?"
  type: multiple-choice
  options:
    - "Nothing — a 95% CI is defined as an interval that contains the true parameter with probability 0.95"
    - "Once the data are observed and the interval [2.1, 4.7] is realized, μ is fixed and either is or is not in the interval — the 95% describes the procedure across repeated experiments, not this specific realized interval"
    - "The statement should say 'at least 95% probability' because the coverage guarantee is a lower bound"
    - "The CI should have been expressed as a probability about the estimator, not the parameter"
  answer: 1
  explanation: "This is the most common misinterpretation of confidence intervals. In the frequentist framework, θ is a fixed (unknown) constant — it has no probability distribution. Once the interval is computed from observed data, it either contains θ (probability 1) or it doesn't (probability 0). The 95% is a property of the *procedure* L(X), U(X): if we repeated the experiment infinitely many times and computed CIs each time, 95% of those intervals would contain θ. The realized interval [2.1, 4.7] is one draw from that procedure."

- question: "Using the test inversion principle, a statistician finds that the data fail to reject H₀: θ = 4.0 but do reject H₀: θ = 3.5 and H₀: θ = 6.2, all at the 5% level. What follows about the 95% confidence interval?"
  type: multiple-choice
  options:
    - "The CI is [3.5, 6.2] — it spans from the boundary of rejection to rejection"
    - "θ = 4.0 lies inside the 95% CI; θ = 3.5 and θ = 6.2 lie outside (or on the boundary)"
    - "The CI cannot be determined from test decisions alone; it must be computed directly from the data"
    - "The CI is a single point at θ = 4.0 because only that value is not rejected"
  answer: 1
  explanation: "Test inversion is exact: the (1−α) CI is precisely the set C(X) = {θ₀ : H₀: θ = θ₀ is not rejected at level α}. If θ = 4.0 is not rejected but θ = 3.5 and θ = 6.2 are, then 4.0 ∈ C(X) and 3.5, 6.2 ∉ C(X). This is the direct connection between hypothesis testing and confidence intervals — they are two sides of the same inference, not separate procedures."

- question: "A confidence interval [L(X), U(X)] is a random interval because L and U are functions of the random data X; the parameter θ is fixed and unknown."
  type: true-false
  answer: true
  explanation: "This is the essential conceptual point. L(X) and U(X) are statistics — they vary from sample to sample. The parameter θ does not move. The probability statement P(L(X) ≤ θ ≤ U(X)) = 1−α describes the distribution of the *interval* across hypothetical repetitions of the experiment, with θ held fixed. Confusing which element is random (the interval, not the parameter) leads to the common misinterpretation that any particular CI has a 95% chance of containing θ."

- question: "When a statistician says a 95% CI 'covers' the true parameter, she means that the interval would contain the true θ for 95% of most possible true parameter values."
  type: true-false
  answer: false
  explanation: "Coverage probability is not a statement across parameter values — it is a statement across repeated experiments. Specifically, P_θ(L(X) ≤ θ ≤ U(X)) ≥ 1−α must hold for *every* θ, not just 95% of them. 'Coverage' means: if the true parameter is θ (whatever it is), and you repeat the sampling procedure many times, at least 95% of the resulting intervals will contain θ. The probability is over the randomness in X, not over θ."

- question: "Explain the test inversion principle: how does inverting a level-α hypothesis test produce a valid (1−α) confidence set? Why does the validity of the CI follow directly from the level guarantee of the test?"
  type: short-answer
  answer: "For each candidate parameter value θ₀, run the level-α test of H₀: θ = θ₀ with acceptance region A(θ₀). Define the confidence set C(X) = {θ₀ : X ∈ A(θ₀)} — all values not rejected by the data. Then P_θ(θ ∈ C(X)) = P_θ(X ∈ A(θ)) = 1 − α, because A(θ) is exactly the set of data outcomes where H₀: θ = θ is accepted, which happens with probability 1−α by the level guarantee. The CI validity follows directly: no new derivation is needed beyond the test's level property."
  explanation: "This makes the CI-test duality exact rather than merely analogical. The acceptance region A(θ₀) and the confidence set C(X) are transposes of each other: one is a set of data values for fixed θ₀, the other is a set of parameter values for fixed X. When the underlying test is UMP (uniformly most powerful), the inversion produces the shortest possible CI, connecting test optimality directly to estimation efficiency."
```

## Explainer

From asymptotic normality of the MLE, you know that under regularity conditions √n(θ̂_MLE − θ) → N(0, I(θ)⁻¹) in distribution, where I(θ) is the Fisher information. This immediately suggests a confidence interval: rearrange the normal approximation to get θ̂ ± z_{α/2}/√(n·I(θ)). But to call this a *confidence interval* rigorously requires a precise definition — one with a subtlety that most introductory treatments skip.

A **confidence interval** [L(X), U(X)] is formally a pair of statistics (functions of data, not of the unknown θ) satisfying P_θ(L(X) ≤ θ ≤ U(X)) ≥ 1 − α for *all* θ in the parameter space. Notice the direction of randomness: θ is fixed (though unknown), and the interval is random because L and U depend on the data X. The statement "there is a 95% probability that θ lies in this interval" is literally false once data is observed — θ either is or is not in the realized interval. The correct interpretation is frequentist: if you repeated the experiment and CI construction many times, at least (1−α)·100% of the resulting intervals would contain the true θ.

The **test inversion principle** connects CIs to hypothesis testing. For each candidate value θ₀, consider the level-α test of H₀: θ = θ₀. Let A(θ₀) be the acceptance region of this test. Define the confidence set C(X) = {θ₀ : X ∈ A(θ₀)} — the set of all parameter values that the data would not reject. Then P_θ(θ ∈ C(X)) = P_θ(X ∈ A(θ)) = 1 − α, so C(X) is a valid (1−α) confidence set. This is an exact equality, not just an analogy. When the test is **UMP** (uniformly most powerful), the resulting CI is the shortest possible at that confidence level — test optimality translates directly into CI optimality.

Asymptotic CIs fill the practical gap. Exact CIs exist in closed form only for special families (exponential family, location-scale). For most problems, the MLE's asymptotic normality provides a universal construction: estimate I(θ) by I(θ̂), apply the asymptotic normal approximation, and invert. The resulting CI has correct coverage as n → ∞ but may deviate from 1−α in finite samples. More refined approaches — likelihood ratio inversion, bootstrap CIs — improve finite-sample coverage but share the same foundational structure: define coverage probability, connect to a test or pivotal quantity, exploit large-sample approximations.
