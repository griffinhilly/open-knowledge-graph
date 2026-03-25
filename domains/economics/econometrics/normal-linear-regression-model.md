---
id: normal-linear-regression-model
title: Normal Linear Regression Model
domain: economics
course: econometrics
prerequisites:
- id: simple-linear-regression-estimation
  type: hard
- id: normal-distribution
  type: soft
- id: linear-algebra
  type: hard
- id: probability-theory
  type: hard
- id: normal-distribution-theory
  type: hard
- id: parallel-trends-assumption-validity
  type: soft
builds-toward:
- t-statistic-individual-coefficient
- f-statistic-overall-significance
tags:
- regression
- normality
- inference
- assumptions
stage: advanced
status: validated
---
# Normal Linear Regression Model

## Core Idea
The normal regression model assumes u ~ N(0,σ²) in addition to OLS assumptions. This distributional assumption enables hypothesis testing and confidence intervals via t and F statistics, allowing exact inference in finite samples rather than relying on asymptotics.

## Questions

```yaml
- question: "A researcher has 12 observations and uses OLS to estimate a regression coefficient. She reports a p-value of 0.04 from a t-test. Under which condition is this p-value exact rather than an asymptotic approximation?"
  type: multiple-choice
  options:
    - "When the sample is a simple random sample from the population of interest"
    - "When the error terms follow a normal distribution, as assumed by the normal linear regression model"
    - "When the OLS estimator is consistent and the Gauss-Markov assumptions hold"
    - "When n > 30, because the Central Limit Theorem guarantees approximate normality at that threshold"
  answer: 1
  explanation: "The Gauss-Markov assumptions (zero-mean, homoskedastic, uncorrelated errors) make OLS BLUE but say nothing about the shape of β̂'s sampling distribution. Without knowing that distribution, you cannot compute p-values exactly. The normality assumption (u ~ N(0,σ²)) is what produces the exact result: since β̂ is a linear combination of normal errors, β̂ is exactly normal, and the t-statistic follows an exact t-distribution with (n-k) degrees of freedom. With only 12 observations, the CLT has not kicked in, and asymptotic results are unreliable. Only the normality assumption provides valid inference here."

- question: "An econometrician fits a regression on 800 observations where the error terms are visibly right-skewed — clearly not normal. She uses standard OLS t-statistics for inference. What is the most accurate characterization?"
  type: multiple-choice
  options:
    - "Invalid — t-statistics require exact normality of errors, so all her inference is meaningless"
    - "Valid exactly — OLS estimators are unbiased regardless of error distribution, and unbiasedness implies valid inference"
    - "Approximately valid — with 800 observations, the CLT ensures the sampling distribution of β̂ is approximately normal, making t-tests approximately correct"
    - "Valid exactly — skewness only affects standard error estimation, not the t-statistic distribution"
  answer: 2
  explanation: "With a large sample, the Central Limit Theorem ensures that the OLS estimator β̂ is approximately normal regardless of the error distribution, under mild regularity conditions. This asymptotic normality makes t and F tests approximately valid even when errors are not normally distributed. The approximation is excellent at n = 800. The key contrast with a small sample (12 observations): asymptotic justification is reliable with large n, but in small samples, if normality fails, p-values may be meaningfully wrong. Unbiasedness (option B) is a property of the estimator's expected value, which says nothing about the shape of its sampling distribution."

- question: "The OLS estimator β̂ follows an exact normal distribution in finite samples if and only if the error terms are normally distributed (given a fixed X matrix)."
  type: true-false
  answer: true
  explanation: "β̂ = β + (X'X)⁻¹X'u — it is a linear function of the error vector u. A fundamental property of normal distributions is that any linear combination of normal random variables is also normal. So if u ~ N(0, σ²I), then β̂ ~ N(β, σ²(X'X)⁻¹) exactly. Conversely, if u is not normally distributed, β̂ is not normally distributed in finite samples (though it converges to normal asymptotically via CLT). This is why the normality assumption is the precise ingredient that converts Gauss-Markov efficiency into exact distributional results."

- question: "Because large samples make the normality assumption unnecessary, the normal linear regression model is purely a teaching tool with no practical relevance in applied econometrics."
  type: true-false
  answer: false
  explanation: "In large samples, asymptotic theory (CLT) makes normality less critical — t and F tests are approximately valid regardless. But in many applied settings — macroeconomics with quarterly data over 30 years (n ≈ 120), natural experiments with limited treatment groups, clinical trials — samples are genuinely small. In these cases, normality is load-bearing: without it, there is no exact justification for t-test critical values, and inference can be wrong in practice, not just in theory. Additionally, the normal model provides the clean finite-sample framework on which asymptotic theory is built — understanding it precisely is essential for knowing when you can safely relax it."

- question: "Why does adding the normality assumption for error terms enable exact finite-sample inference, when the Gauss-Markov assumptions alone cannot provide this?"
  type: short-answer
  answer: "The Gauss-Markov assumptions specify the mean and variance of the errors (zero mean, constant variance, no serial correlation) and guarantee that OLS is the best linear unbiased estimator. But they say nothing about the shape of the error distribution. Without knowing the shape, you cannot determine the sampling distribution of β̂, and without the sampling distribution you cannot compute probabilities — i.e., p-values and confidence intervals. The normality assumption adds u ~ N(0,σ²). Since β̂ is a linear combination of u, and linear combinations of normal variables are normal, β̂ ~ N(β, σ²(X'X)⁻¹) exactly. This exact distribution produces exact t and F statistics valid in any sample size."
  explanation: "The distinction between Gauss-Markov and the normal linear model is between efficiency claims and distributional claims. Gauss-Markov: 'OLS is best among linear unbiased estimators.' Normal model: 'β̂ has this exact distribution.' The first claim is about competing estimators; the second is about the probability calculus needed for inference. They are logically independent — you can have efficiency without normality (and thus no exact inference), or normality without Gauss-Markov (and thus exact inference with a possibly inefficient estimator). The normal linear model combines both."
```

## Explainer

From simple linear regression, you know how to estimate coefficients by minimizing the sum of squared residuals. OLS gives you β̂ with desirable properties under the Gauss-Markov assumptions: it's unbiased and efficient among linear estimators. But those properties say nothing about the *distribution* of β̂ — without knowing the shape of that distribution, you cannot make probability statements about how far your estimate might be from the truth. That's where the **normal linear regression model** comes in: by adding one additional assumption about the error term's distribution, you unlock the entire apparatus of hypothesis testing and confidence intervals without needing large samples.

The new assumption is that the error terms follow a **normal distribution**: u ~ N(0, σ²). This is a strong claim — you're asserting not just that errors have mean zero and constant variance (the Gauss-Markov assumptions), but that they're drawn from a bell-shaped distribution. Once you make this assumption, a remarkable thing happens: because OLS is a linear function of the errors, and because linear combinations of normal random variables are also normal, the OLS estimator β̂ is itself normally distributed. Specifically, β̂ ~ N(β, σ²(X'X)⁻¹). You now have the exact sampling distribution of your estimator — not an approximation, but the precise distribution.

This sampling distribution is what makes inference possible. The **t-statistic** for testing whether a coefficient βⱼ equals some hypothesized value β₀ is (β̂ⱼ - β₀) / se(β̂ⱼ), where the standard error is estimated from the data. Under the null hypothesis and the normality assumption, this statistic follows an exact t-distribution with (n-k) degrees of freedom — where n is sample size and k is the number of parameters including the intercept. Similarly, the **F-statistic** for testing joint hypotheses (does this entire set of coefficients equal zero?) follows an exact F-distribution under the null. These are finite-sample results: they hold exactly even in small samples, not just approximately as sample size grows.

Without the normality assumption, you can still do inference — but only asymptotically, by appealing to the Central Limit Theorem. As n → ∞, the distribution of β̂ converges to normal regardless of the distribution of the errors (under mild regularity conditions), so t and F tests remain valid approximately in large samples. The practical implication: in small samples, the normality assumption is load-bearing. If you have 15 observations and your errors are highly skewed, your t-test p-values may be meaningfully wrong. In large samples — say, 500+ observations — the asymptotic justification is usually sufficient, and the normal regression model becomes a special case of the more general asymptotic theory rather than a necessary restriction. This is why econometrics courses introduce the normal model first for clean finite-sample theory, then relax it for the large-sample results that dominate applied work.
