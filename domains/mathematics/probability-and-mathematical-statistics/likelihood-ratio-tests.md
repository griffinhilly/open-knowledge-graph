---
id: likelihood-ratio-tests
title: Likelihood Ratio Tests
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: neyman-pearson-lemma
  type: hard
- id: convergence-in-distribution
  type: soft
builds-toward:
- uniformly-most-powerful-tests
tags:
- likelihood-ratio-tests
- hypothesis-testing
- statistics
stage: advanced
status: validated
---

# Likelihood Ratio Tests

## Core Idea
The likelihood ratio test rejects H₀ when Λ = L(θ̂₀|X)/L(θ̂|X) < c, where θ̂₀ is the MLE under H₀ and θ̂ is the unrestricted MLE. Under H₀, -2log(Λ) converges in distribution to χ²_r where r is the dimension reduction. LR tests are general and achieve optimal Type II error (power) asymptotically.

## Questions

```yaml
- question: "In a likelihood ratio test, the statistic Λ = L(θ̂₀)/L(θ̂) is computed and found to be 0.97. What does this indicate?"
  type: multiple-choice
  options:
    - "Strong evidence against H₀, because the ratio is close to 1 and the null model explains 97% of the data"
    - "Little evidence against H₀, because the null model achieves nearly the same maximum likelihood as the unconstrained model"
    - "That the test is invalid, because a valid Λ must be below 0.5 to reject H₀"
    - "That θ̂₀ = θ̂, so the null and alternative hypotheses are indistinguishable"
  answer: 1
  explanation: "Λ close to 1 means the best fitting model under H₀ (the numerator) achieves almost as high a likelihood as the best fitting model overall (the denominator). The data is fit nearly equally well whether or not we impose the null constraint — so there is no strong reason to reject H₀. The test rejects when Λ is close to 0: the constrained model fits the data much worse than the unconstrained model, indicating the null constraints are inconsistent with the data. Confusing 'large Λ = reject' with 'small Λ = reject' is a very common error."

- question: "You test H₀: μ = 0 in a Normal(μ, σ²) model with both μ and σ² unknown. The full model has 2 free parameters; under H₀, only σ² is free. By Wilks' theorem, −2 log Λ is asymptotically distributed as:"
  type: multiple-choice
  options:
    - "χ²₂, because the full model has 2 parameters"
    - "χ²₁, because H₀ imposes 1 constraint (fixing μ), reducing the parameter space by 1"
    - "Normal(0, 1), because the test involves a single mean"
    - "t₁, because one mean is being tested from a normal distribution"
  answer: 1
  explanation: "Wilks' theorem states that −2 log Λ converges in distribution to χ²_r, where r is the number of constraints imposed by H₀ — equivalently, the difference in the number of free parameters between the full and null models. Here: full model has 2 free parameters (μ, σ²); null model has 1 free parameter (σ² only, since μ is fixed at 0). So r = 2 − 1 = 1, and −2 log Λ ~ χ²₁ asymptotically. The chi-squared distribution has 1 degree of freedom, not 2. In this case the LRT is equivalent to the squared t-statistic."

- question: "The likelihood ratio statistic Λ always lies between 0 and 1, because the maximum likelihood under the full model is at least as large as the maximum likelihood under the restricted null model."
  type: true-false
  answer: true
  explanation: "Since the null parameter space Θ₀ is a subset of the full parameter space Θ, any parameter value allowed under H₀ is also allowed in the unrestricted optimization. The unrestricted MLE therefore achieves a likelihood at least as high as the constrained MLE. This means sup_{θ∈Θ} L(θ|x) ≥ sup_{θ∈Θ₀} L(θ|x), so Λ = L(θ̂₀)/L(θ̂) ≤ 1. Since likelihoods are non-negative, Λ ≥ 0. The bound Λ ∈ [0,1] is not an assumption but a logical consequence of the nested structure of H₀ within H₁."

- question: "The likelihood ratio test is primarily applicable when the null hypothesis specifies a single fixed value of the parameter (a simple null hypothesis)."
  type: true-false
  answer: false
  explanation: "The LRT was designed specifically to generalize beyond simple null hypotheses. The Neyman-Pearson lemma handles simple nulls (H₀: θ = θ₀ vs. H₁: θ = θ₁) by comparing two fixed likelihoods. The LRT extends this to composite hypotheses — where H₀ specifies a set of parameter values — by replacing fixed likelihoods with the best achievable likelihood under each model (the constrained and unconstrained MLEs). This is precisely the LRT's contribution: a universal framework for testing any constraint on a parametric model, simple or composite."

- question: "Explain why the LRT uses maximum achievable likelihoods (MLEs under each hypothesis) rather than fixed parameter values, and what advantage this provides over the Neyman-Pearson likelihood ratio."
  type: short-answer
  answer: "The Neyman-Pearson likelihood ratio compares L(θ₁|x) / L(θ₀|x) where θ₀ and θ₁ are single specified values — it only works for simple hypotheses. For composite hypotheses (where H₀ and H₁ specify sets of values), there is no single 'the' likelihood under H₀. The LRT solves this by asking: what is the best the null hypothesis can possibly do? It uses the MLE under H₀ in the numerator and the unrestricted MLE in the denominator, so the ratio compares the null hypothesis at its best against the unrestricted model at its best. This makes the test applicable to any nested parametric hypothesis."
  explanation: "The key conceptual move is from 'compare two likelihoods at fixed points' to 'compare the best likelihoods achievable under each model.' This is a natural generalization: if the null model, given every opportunity to fit the data, still fits much worse than the unrestricted model, that is evidence against the null. Wilks' theorem then provides a universal reference distribution (chi-squared) for the test statistic, making the LRT a general-purpose framework rather than a collection of special-case tests for each model type."
```

## Explainer

The **Neyman-Pearson lemma** — your core prerequisite — gave you the most powerful test for a specific kind of problem: a simple null hypothesis (H₀: θ = θ₀) against a simple alternative (H₁: θ = θ₁). The NP test rejects when the likelihood ratio L(θ₁|x)/L(θ₀|x) exceeds a threshold. That ratio compares two fixed parameter values. The likelihood ratio test generalizes this idea to composite hypotheses, where H₀ and H₁ each specify a set of parameter values rather than a single point.

The key insight is to replace the two fixed likelihoods with the best possible likelihoods under each hypothesis. Let Θ₀ be the null parameter space and Θ be the full parameter space. Define the **likelihood ratio statistic** Λ = sup_{θ ∈ Θ₀} L(θ|x) / sup_{θ ∈ Θ} L(θ|x). The numerator is the maximum likelihood achievable while respecting H₀; the denominator is the maximum likelihood overall, achieved at the unrestricted MLE θ̂. Since Θ₀ ⊆ Θ, we always have Λ ∈ [0, 1]. A value of Λ near 1 means the null hypothesis fits the data almost as well as the best unconstrained model — no reason to reject. A value of Λ near 0 means the data is far better explained by some θ outside Θ₀ — strong evidence against H₀. The test rejects when Λ < c for some threshold c.

The practical power of the LRT comes from **Wilks' theorem**: under H₀ and regularity conditions, the statistic −2 log Λ converges in distribution to a chi-squared distribution with r degrees of freedom, where r is the difference in the dimension of the full parameter space and the null parameter space (the number of constraints imposed by H₀). This asymptotic result means you can determine the critical value without knowing the exact distribution of Λ: just compare −2 log Λ to the χ²_r quantile for your chosen significance level. Your prerequisite on **convergence in distribution** is exactly what makes this work — you know that "converges in distribution to χ²_r" means the chi-squared approximation becomes exact as n → ∞, and is often good enough for moderate n.

As a concrete example, suppose X₁, …, Xₙ ~ Normal(μ, σ²) with both μ and σ² unknown, and you want to test H₀: μ = 0 against H₁: μ ≠ 0. The full model has two free parameters (μ, σ²); under H₀, only σ² is free. So r = 2 − 1 = 1, and −2 log Λ ≈ χ²₁. In this normal case, the LRT is equivalent to the t-test (the t-statistic squared follows an F-distribution, and by Wilks the LRT is asymptotically equivalent). For more complex models — exponential families, nested regression models, logistic regression — Wilks' theorem delivers the same chi-squared test, making the LRT a universal framework rather than a collection of special-case tests.
