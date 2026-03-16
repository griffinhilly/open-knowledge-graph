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
stage: advanced
status: draft
---

# Fisher Information

## Core Idea
The Fisher information is I(θ) = E[(∂log f(X|θ)/∂θ)²] = -E[∂²log f(X|θ)/∂θ²]. It quantifies how much information the data carries about θ: larger I means θ is more precisely estimable. For n i.i.d. observations, Iₙ(θ) = nI(θ). Fisher information appears in the Cramer-Rao bound and characterizes the asymptotic variance of MLEs.

## Explainer

From your work with expectations and densities, you know that the log-likelihood ℓ(θ; x) = log f(x|θ) measures how well the parameter value θ explains the observed data x. The derivative ∂ℓ/∂θ — called the **score function** — tells you which direction to move θ to increase the likelihood. At the true parameter value, the expected score is zero: E[∂log f(X|θ)/∂θ] = 0 (this is a regularity condition you can verify by differentiating under the integral sign). The Fisher information is the **variance of the score**: I(θ) = Var[∂log f(X|θ)/∂θ] = E[(∂log f(X|θ)/∂θ)²].

The intuition is curvature. Think of the log-likelihood as a landscape: the score is the slope, and the Fisher information measures how steeply the likelihood peaks around the true parameter. If I(θ) is large, the log-likelihood drops off sharply when you move θ away from the truth — different parameter values lead to noticeably different distributions, so the data "discriminates" well between them. If I(θ) is small, the log-likelihood is flat near the true value — many θ values produce similar distributions, so the data carries weak signal about which θ is correct. Large Fisher information means the parameter is easy to estimate precisely; small Fisher information means it is hard.

The **equivalence** I(θ) = −E[∂²log f(X|θ)/∂θ²] connects information to the curvature (second derivative) of the log-likelihood. The expected negative second derivative measures how sharply the log-likelihood bends downward at its peak — a high peak corresponds to high information. This form is often easier to compute in practice, because second derivatives of log-likelihoods are frequently simpler than squares of first derivatives. For exponential family distributions (Gaussian, Poisson, Bernoulli, etc.), there are clean closed-form expressions for I(θ).

The key property **Iₙ(θ) = nI(θ)** for i.i.d. observations reflects the additivity of information: each independent observation contributes the same amount of information I(θ) about θ, and independent contributions add. This linearity is what makes Fisher information so useful for sample size calculations — if you need information to scale by a factor of 4 (halving the standard error), you need 4 times as many observations. The payoff of all this machinery comes in the **Cramér-Rao lower bound** and in the asymptotic theory of the MLE: the maximum likelihood estimator achieves variance 1/I(θ) asymptotically, making it the most efficient estimator in the class of unbiased estimators, and Fisher information is the fundamental currency in which that efficiency is measured.
