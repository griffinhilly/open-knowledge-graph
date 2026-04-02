---
id: confidence-intervals-rigorous
title: Confidence Intervals (Rigorous Theory)
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: asymptotic-normality-of-mle
  type: hard
builds-toward:
- bayesian-inference-foundations
tags:
- confidence-intervals
- coverage
- inversion
stage: expert
status: validated
---

# Confidence Intervals (Rigorous Theory)

## Core Idea
A confidence interval [L(X), U(X)] has level 1-α if P(θ ∈ [L,U]) = 1-α for all θ (exact) or approximately (asymptotic). Intervals are constructed by inverting hypothesis tests or using pivotal quantities. Asymptotic CIs rely on the CLT and estimator asymptotics. Confidence is frequentist; different from Bayesian credible intervals.

## Questions

```yaml
- question: "A researcher computes a 95% confidence interval for a population mean and obtains [2.3, 4.7]. She states: 'There is a 95% probability that the true mean lies between 2.3 and 4.7.' What is wrong with this interpretation?"
  type: multiple-choice
  options:
    - "Nothing — this is precisely what a 95% confidence interval means"
    - "She should say 90%, not 95%, because the interval is symmetric"
    - "Once the data are observed, the interval is fixed and the parameter is fixed — either it is in the interval or it is not; the 95% describes the procedure's long-run coverage, not this realized interval"
    - "The statement would be correct only if the sample size were large enough for the CLT to apply"
  answer: 2
  explanation: "This is the single most common misinterpretation of confidence intervals. After the data are observed, L = 2.3 and U = 4.7 are fixed numbers, and θ is a fixed (unknown) number. There is no randomness left to assign a probability to. The 95% confidence level describes the *procedure*: if repeated many times, 95% of the resulting intervals would contain the true θ. No probability statement applies to any single computed interval."

- question: "The test inversion approach to constructing a confidence interval produces a set of parameter values θ₀ that would not be rejected by a level-α test. How does this relate to the pivotal quantity approach?"
  type: multiple-choice
  options:
    - "They are unrelated — one is frequentist and one is Bayesian"
    - "Test inversion applies only to one-sided tests; pivotal quantities produce two-sided intervals"
    - "They are mathematically equivalent and produce the same intervals"
    - "Test inversion gives exact intervals while pivotal quantities only give approximate ones"
  answer: 2
  explanation: "The two constructions are formally equivalent. A pivotal quantity Q(X, θ) defines an interval by inverting P(a ≤ Q ≤ b) = 1-α into a range of θ values. The test inversion approach defines the confidence set as exactly those θ₀ for which a level-α test at the observed data would not reject — this is the same algebraic inversion. The equivalence reveals the deep connection between hypothesis testing and interval estimation."

- question: "A 95% frequentist confidence interval and a 95% Bayesian credible interval answer fundamentally the same question about the parameter."
  type: true-false
  answer: false
  explanation: "They answer different questions. The credible interval gives P(θ ∈ interval | data) = 0.95, treating θ as a random variable with a prior distribution — it makes a posterior probability statement about the parameter given the observed data. The confidence interval makes no probability statement about θ at all; it says that the *procedure* covers the true (fixed) θ in 95% of repetitions. The intervals may look numerically similar, especially with diffuse priors and large samples, but the philosophical interpretations are entirely distinct."

- question: "The confidence level 1-α of a confidence interval refers to how often the interval construction procedure captures the true parameter in repeated sampling, not to the probability that a specific realized interval contains the parameter."
  type: true-false
  answer: true
  explanation: "This is the correct frequentist interpretation. The randomness in a confidence interval comes from the data X: before observing data, [L(X), U(X)] is a random interval that covers θ with probability 1-α. After observing data, the interval is fixed. The 1-α coverage is a property of the procedure (the estimator, the pivotal quantity, the sample size), not of any individual result."

- question: "Explain why it is incorrect to say 'there is a 95% probability that the parameter θ lies in this computed confidence interval,' once the data have been observed."
  type: short-answer
  answer: "After observing data, the confidence interval [L, U] is a pair of fixed numbers and θ is a fixed unknown constant. There is no random experiment being described — the probability is either 0 or 1 (θ either is or is not in the interval). The 95% refers to the long-run frequency: if the same procedure were repeated across many independent datasets, 95% of the resulting intervals would contain θ. To assign a probability to a specific realized interval requires treating θ as a random variable, which is the Bayesian approach (credible intervals), not the frequentist one."
  explanation: "Frequentist probability is defined over repeated sampling, not over unknown constants. The interval is what varies across repetitions; the parameter is fixed. This distinction also explains why two different 95% CIs from the same data (constructed by different methods) can have the same nominal coverage but very different actual properties — the coverage guarantee is about the procedure, not the particular numbers obtained."
```

## Explainer

From the asymptotic normality of the MLE, you know that under regularity conditions √n(θ̂ - θ) →_d N(0, I(θ)^{-1}), where I(θ) is the Fisher information. This gives the building block for interval estimation: an approximate normal pivot. A **confidence interval** [L(X), U(X)] is not a fixed interval with a probability attached to it — it is a random interval, a function of the data X, defined so that the probability of covering the true θ meets a specified level.

The formal definition makes the frequentist interpretation precise. We say [L(X), U(X)] has **coverage probability** 1-α if P_θ(θ ∈ [L(X), U(X)]) = 1-α for all θ in the parameter space. The subscript θ means: we are computing probability over the distribution of X when θ is the true parameter. In repeated sampling — draw a new dataset, compute a new interval, repeat — exactly 100(1-α)% of those intervals contain the true θ. No single computed interval carries a probability: once data is observed, L and U are fixed numbers and θ is a fixed (unknown) number. Either θ is in [L, U] or it is not. The 1-α confidence level describes the procedure's long-run performance, not any individual interval's uncertainty.

There are two standard constructions. The **pivotal quantity** approach finds a function Q(X, θ) whose distribution does not depend on θ, then inverts its probability statement into an interval. For example, if Q = (X̄ - μ)/(s/√n) ~ t_{n-1}, then P(-t_{α/2} ≤ Q ≤ t_{α/2}) = 1-α rearranges to P(X̄ - t_{α/2}·s/√n ≤ μ ≤ X̄ + t_{α/2}·s/√n) = 1-α. The **test inversion** approach is equivalent in theory: the 1-α confidence set for θ is exactly the set of parameter values θ₀ that would not be rejected by a level-α test at the observed data. These two constructions produce the same intervals and illuminate their connection to hypothesis testing.

The Bayesian **credible interval** looks superficially similar but is philosophically distinct. It treats θ as a random variable with a prior distribution, and gives P(θ ∈ interval | data) = 1-α using the posterior distribution. A 95% credible interval means exactly what naive intuition expects — 95% posterior probability — while a 95% confidence interval means long-run coverage. In practice the intervals often have similar numerical endpoints, especially in large samples or with diffuse priors. But they answer different questions: the frequentist confidence interval makes a claim about the procedure; the Bayesian credible interval makes a claim about the current posterior state of belief.
