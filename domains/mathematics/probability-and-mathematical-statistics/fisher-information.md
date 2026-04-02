---
id: fisher-information
title: Fisher Information
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: expectation-measure-theoretic
  type: hard
- id: distribution-functions-densities-rigorous
  type: hard
builds-toward:
- cramer-rao-lower-bound
- asymptotic-normality-mle
tags:
- fisher-information
- information-theory
- statistics
stage: expert
status: validated
---

# Fisher Information

## Core Idea
The Fisher information is I(θ) = E[(∂log f(X|θ)/∂θ)²] = -E[∂²log f(X|θ)/∂θ²]. It quantifies how much information the data carries about θ: larger I means θ is more precisely estimable. For n i.i.d. observations, Iₙ(θ) = nI(θ). Fisher information appears in the Cramer-Rao bound and characterizes the asymptotic variance of MLEs.

## Questions

```yaml
- question: "Consider estimating the mean μ of a Gaussian distribution with known variance σ². If σ² is doubled while μ remains the same, what happens to the Fisher information I(μ)?"
  type: multiple-choice
  options:
    - "It doubles, because more variable observations provide more information about spread"
    - "It is halved, because each observation carries weaker signal about μ when the noise level is higher"
    - "It remains the same, because σ² affects the estimator's variance but not the information content"
    - "It increases, because a wider distribution explores more of the parameter space"
  answer: 1
  explanation: "For a Gaussian with known σ², Fisher information about μ is I(μ) = 1/σ². Doubling σ² halves I(μ). Intuitively: more variable observations are harder to learn from. Precisely: the log-likelihood ℓ(μ; x) = −(x−μ)²/(2σ²) has score function ∂ℓ/∂μ = (x−μ)/σ², whose variance is 1/σ². Higher noise flattens the log-likelihood landscape, reducing curvature, making it harder to pinpoint where the peak is — that is lower Fisher information. The Cramér-Rao bound directly implies that any unbiased estimator of μ from a single observation has variance at least σ²."

- question: "Which of the following best captures the geometric meaning of high Fisher information for parameter θ?"
  type: multiple-choice
  options:
    - "The MLE is approximately unbiased, so the estimator is centered near the true θ on average"
    - "The log-likelihood has a sharp, narrow peak near the true θ, so different θ values produce noticeably different distributions"
    - "The likelihood is maximized at exactly the true θ, ensuring consistent estimation"
    - "The sample size needed to estimate θ is small, regardless of which estimation method is used"
  answer: 1
  explanation: "Fisher information measures curvature of the log-likelihood. A sharply peaked log-likelihood means the data strongly discriminates between parameter values near the truth — small changes in θ produce large changes in the probability of the observed data. That is high information. Option A confuses information with bias (a separate property of an estimator). Option C is true for any regular distribution but does not capture what 'high' information means — it says nothing about how fast likelihood drops off on either side of the maximum. Option D is approximately true but imprecise: Fisher information bounds how precisely θ can be estimated, but the sample size needed depends on the specific precision goal."

- question: "For n independent and identically distributed observations from the same distribution, the total Fisher information is n times the Fisher information from a single observation."
  type: true-false
  answer: true
  explanation: "Fisher information is additive for independent observations, just as independent bits of evidence accumulate. Formally: the log-likelihood for n i.i.d. observations is the sum of the individual log-likelihoods, and the variance of a sum of independent random variables is the sum of the variances. So Iₙ(θ) = nI(θ). This additivity is practically important: to halve the standard error of an estimator (which scales as 1/√I), you need four times the observations — the information must quadruple. The Cramér-Rao lower bound Var(θ̂) ≥ 1/nI(θ) formalizes this."

- question: "The Fisher information I(θ) can be computed as the expected value of the score function ∂log f(X|θ)/∂θ, since the score measures how steeply the likelihood changes with θ."
  type: true-false
  answer: false
  explanation: "The expected score is zero at the true θ (a regularity condition: E[∂log f(X|θ)/∂θ] = 0), not the Fisher information. Fisher information is the variance of the score — equivalently, the expected squared score: I(θ) = E[(∂log f(X|θ)/∂θ)²] = Var[score]. It is the second moment, not the first. The expected score is zero because the likelihood integrates to 1 and differentiating under the integral gives zero. The information comes from the spread of the score around zero — how much it fluctuates as data varies — which is measured by its variance."

- question: "Why does the Fisher information determine a fundamental lower bound on how precisely any unbiased estimator can estimate θ, regardless of which estimation method is used?"
  type: short-answer
  answer: "The Cramér-Rao lower bound states that for any unbiased estimator θ̂, Var(θ̂) ≥ 1/I(θ). The bound comes from a Cauchy-Schwarz inequality applied to the covariance between the estimator and the score. Because the score is the only object connecting the data distribution to the parameter, and Fisher information measures how much the distribution changes with θ, it sets an irreducible limit on how much information any function of the data can contain about θ. No clever choice of estimator can extract more than I(θ) units of information per observation — the bound is a property of the data-generating process, not of any particular estimator."
  explanation: "The MLE achieves this bound asymptotically: for large n, the MLE has variance approximately 1/nI(θ), making it asymptotically efficient. This is why the Fisher information is the natural 'currency' for comparing estimators — an estimator with variance 2/nI(θ) is only 50% efficient, discarding half the available information in the data. In experimental design, Fisher information guides how to allocate measurements: place observations where the score has the most variance (where the likelihood changes most steeply) to maximize information per sample."
```

## Explainer

From your work with expectations and densities, you know that the log-likelihood ℓ(θ; x) = log f(x|θ) measures how well the parameter value θ explains the observed data x. The derivative ∂ℓ/∂θ — called the **score function** — tells you which direction to move θ to increase the likelihood. At the true parameter value, the expected score is zero: E[∂log f(X|θ)/∂θ] = 0 (this is a regularity condition you can verify by differentiating under the integral sign). The Fisher information is the **variance of the score**: I(θ) = Var[∂log f(X|θ)/∂θ] = E[(∂log f(X|θ)/∂θ)²].

The intuition is curvature. Think of the log-likelihood as a landscape: the score is the slope, and the Fisher information measures how steeply the likelihood peaks around the true parameter. If I(θ) is large, the log-likelihood drops off sharply when you move θ away from the truth — different parameter values lead to noticeably different distributions, so the data "discriminates" well between them. If I(θ) is small, the log-likelihood is flat near the true value — many θ values produce similar distributions, so the data carries weak signal about which θ is correct. Large Fisher information means the parameter is easy to estimate precisely; small Fisher information means it is hard.

The **equivalence** I(θ) = −E[∂²log f(X|θ)/∂θ²] connects information to the curvature (second derivative) of the log-likelihood. The expected negative second derivative measures how sharply the log-likelihood bends downward at its peak — a high peak corresponds to high information. This form is often easier to compute in practice, because second derivatives of log-likelihoods are frequently simpler than squares of first derivatives. For exponential family distributions (Gaussian, Poisson, Bernoulli, etc.), there are clean closed-form expressions for I(θ).

The key property **Iₙ(θ) = nI(θ)** for i.i.d. observations reflects the additivity of information: each independent observation contributes the same amount of information I(θ) about θ, and independent contributions add. This linearity is what makes Fisher information so useful for sample size calculations — if you need information to scale by a factor of 4 (halving the standard error), you need 4 times as many observations. The payoff of all this machinery comes in the **Cramér-Rao lower bound** and in the asymptotic theory of the MLE: the maximum likelihood estimator achieves variance 1/I(θ) asymptotically, making it the most efficient estimator in the class of unbiased estimators, and Fisher information is the fundamental currency in which that efficiency is measured.
