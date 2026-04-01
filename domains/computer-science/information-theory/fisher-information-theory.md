---
id: fisher-information-theory
title: Fisher Information
domain: computer-science
course: information-theory
prerequisites:
- id: differential-entropy
  type: hard
- id: probability-density-functions
  type: hard
- id: kl-divergence
  type: soft
builds-toward:
- information-geometry-basics
tags:
- Fisher information
- Cramer-Rao bound
- estimation theory
- score function
- statistical efficiency
stage: expert
status: validated
---

# Fisher Information

## Core Idea
The Fisher information I(theta) = E[(d/d_theta log f(X;theta))^2] = -E[d^2/d_theta^2 log f(X;theta)] measures how much a sample from the distribution f(X;theta) tells you about the parameter theta. It quantifies the curvature of the log-likelihood around the true parameter value — sharp peaks (high Fisher information) mean the data is highly informative. The Cramer-Rao bound states that any unbiased estimator of theta has variance at least 1/I(theta), establishing Fisher information as the fundamental limit of parameter estimation. Fisher information connects to KL divergence (it is the second derivative of D_KL) and forms the metric tensor in information geometry.

## Questions

```yaml
- question: "A coin has unknown bias theta. You flip it n times. The Fisher information per flip is I(theta) = 1/(theta(1-theta)). At theta = 0.5 (fair coin), I = 4, while at theta = 0.01 (very biased), I = 1/(0.01*0.99) ≈ 101. Why is Fisher information higher for the biased coin?"
  type: multiple-choice
  options:
    - "Biased coins provide more entropy per flip"
    - "Each flip from a biased coin is more informative about theta because the outcome is more deterministic — a single flip from a near-certain coin strongly confirms or refutes the hypothesized bias, while a fair coin flip is ambiguous about theta"
    - "Fisher information is inversely related to entropy, so lower entropy means higher information"
    - "The formula is incorrect for extreme theta values"
  answer: 1
  explanation: "At theta = 0.01, most flips land heads (say). An occasional tail is very surprising and sharply constrains theta. The log-likelihood changes steeply with theta near extreme values. At theta = 0.5, both outcomes are equally common regardless of small changes in theta, so each flip is less informative about the precise value of theta. Fisher information measures sensitivity to theta, not entropy. The Cramer-Rao bound confirms: Var(theta-hat) >= theta(1-theta)/n, which is minimized at extreme theta (easiest to estimate precisely)."

- question: "The Cramer-Rao bound states that no unbiased estimator can have variance lower than 1/(nI(theta)) for n independent observations."
  type: true-false
  answer: true
  explanation: "For n i.i.d. observations, the total Fisher information is n*I(theta), and the Cramer-Rao lower bound (CRLB) on the variance of any unbiased estimator is 1/(n*I(theta)). Maximum likelihood estimators (MLEs) are asymptotically efficient: their variance approaches the CRLB as n grows. The CRLB is the information-theoretic limit of estimation precision — Fisher information determines the hardest-possible accuracy floor for any unbiased method."

- question: "Explain the relationship between Fisher information and KL divergence, and why this connection matters for information geometry."
  type: short-answer
  answer: "Fisher information is the second derivative of KL divergence: I(theta) = d^2/d_theta'^2 D_KL(f(x;theta) || f(x;theta')) evaluated at theta' = theta. KL divergence measures how different two distributions are; Fisher information measures how quickly they become different as theta changes. This makes Fisher information a local measure of distinguishability between nearby distributions. In information geometry, Fisher information serves as the Riemannian metric tensor on the manifold of probability distributions — it defines the 'distance' between infinitesimally close distributions. Geodesics on this manifold (shortest paths in the Fisher metric) correspond to natural interpolations between distributions, and the curvature of the manifold reveals the statistical structure of the model family."
  explanation: "The Fisher information matrix (for vector parameters) generalizes this to multiple parameters: I_{ij}(theta) = E[(d/d_theta_i log f)(d/d_theta_j log f)]. This positive-definite matrix defines a Riemannian metric, making the space of distributions a curved manifold. This is the foundation of information geometry."
```

## Explainer

Shannon entropy and mutual information measure how much uncertainty exists or how much two variables share. Fisher information asks a different question: given that data comes from a parametric family f(x; theta), how much does a sample tell you about the parameter theta? While Shannon's measures are distribution-to-distribution, Fisher information is a property of a parametric model at a specific parameter value.

The **score function** s(x; theta) = d/d_theta log f(x; theta) measures how the log-likelihood changes as theta varies. Under regularity conditions, E[s] = 0 (the score has zero mean). The Fisher information is the variance of the score: I(theta) = Var[s(X; theta)] = E[s^2]. High Fisher information means the log-likelihood is steep — small changes in theta cause large changes in the likelihood, making different theta values easy to distinguish from data. An equivalent expression is I(theta) = -E[d^2/d_theta^2 log f(X; theta)], relating Fisher information to the curvature (concavity) of the expected log-likelihood.

The **Cramer-Rao bound** gives Fisher information its operational meaning: for any unbiased estimator theta-hat of theta, Var(theta-hat) >= 1/I(theta). With n i.i.d. observations, the bound becomes 1/(nI(theta)). This says that estimation precision is fundamentally limited by how informative the data is about the parameter. An estimator achieving this bound is called "efficient." Maximum likelihood estimators are asymptotically efficient — they approach the bound as the sample size grows.

The connection to information theory runs deep. Fisher information is the local version of KL divergence: I(theta) = d^2/d_epsilon^2 D_KL(f(x;theta) || f(x;theta+epsilon))|_{epsilon=0}. KL divergence measures global distributional difference; Fisher information measures infinitesimal difference. This relationship makes Fisher information the natural metric on the space of probability distributions — the starting point of information geometry. It also connects to the maximum entropy principle: the Fisher-efficient estimator is the one that maximizes entropy subject to the observed sufficient statistics, linking estimation theory back to Shannon's framework.
