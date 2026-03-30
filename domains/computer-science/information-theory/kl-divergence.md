---
id: kl-divergence
title: KL Divergence
domain: computer-science
course: information-theory
prerequisites:
- id: shannon-entropy
  type: hard
- id: mutual-information
  type: hard
- id: probability-distributions
  type: hard
builds-toward:
- rate-distortion-theory
- information-theoretic-security
- information-geometry-basics
tags:
- KL divergence
- Kullback-Leibler
- relative entropy
- divergence
stage: advanced
status: validated
---

# KL Divergence

## Core Idea
The Kullback-Leibler divergence D_KL(P || Q) = sum p(x) log(p(x)/q(x)) measures how much one probability distribution P differs from a reference distribution Q, in units of information. It quantifies the extra bits needed to encode samples from P using a code optimized for Q. KL divergence is always non-negative (Gibbs' inequality), equals zero only when P = Q, and is not symmetric: D_KL(P||Q) != D_KL(Q||P). It is the central tool for comparing distributions in information theory, statistics (likelihood ratio tests), and machine learning (variational inference, training generative models).

## Questions

```yaml
- question: "A language model Q assigns probability 0.01 to a word that actually occurs with probability 0.25 in the true distribution P. How does this specific word contribute to D_KL(P || Q)?"
  type: multiple-choice
  options:
    - "0.25 * log2(0.25 / 0.01) ≈ 1.16 bits — a large contribution because Q severely underestimates this word's probability"
    - "0.01 * log2(0.01 / 0.25) — a negative contribution because Q assigns too little probability"
    - "log2(0.25 / 0.01) ≈ 4.64 bits — unweighted by the true probability"
    - "0.25 * log2(0.01 / 0.25) — a negative value that reduces the divergence"
  answer: 0
  explanation: "Each term in D_KL(P||Q) is p(x) * log(p(x)/q(x)). For this word: 0.25 * log2(0.25/0.01) = 0.25 * log2(25) = 0.25 * 4.64 ≈ 1.16 bits. The contribution is large and positive because Q dramatically underestimates a common word. KL divergence heavily penalizes cases where Q assigns low probability to events that P considers likely — this is why mode-dropping in generative models (Q missing modes of P) is so costly in the KL sense."

- question: "KL divergence is a proper distance metric between probability distributions."
  type: true-false
  answer: false
  explanation: "KL divergence is NOT a metric. It fails two requirements: (1) it is not symmetric — D_KL(P||Q) != D_KL(Q||P) in general, and (2) it does not satisfy the triangle inequality. It is sometimes called a 'divergence' or 'relative entropy' specifically to avoid the word 'distance.' However, it has deep connections to actual metrics: the symmetrized KL (D_KL(P||Q) + D_KL(Q||P)) and the square root of the Jensen-Shannon divergence (which IS a metric) are commonly used alternatives."

- question: "In variational inference, we minimize D_KL(q || p) where q is an approximate posterior and p is the true posterior. Why does this tend to produce approximations q that are more concentrated (mode-seeking) than the true posterior?"
  type: multiple-choice
  options:
    - "Minimizing D_KL(q||p) penalizes q for placing mass where p has low density, so q avoids the tails and concentrates on a single mode"
    - "D_KL(q||p) is always smaller than D_KL(p||q), forcing q to be narrower"
    - "Variational inference uses gradient descent, which naturally converges to point estimates"
    - "The KL divergence is symmetric, so the direction does not matter"
  answer: 0
  explanation: "D_KL(q||p) = sum q(x) log(q(x)/p(x)). Where q(x) > 0 but p(x) ≈ 0, the log ratio explodes, creating a huge penalty. So q learns to avoid placing mass anywhere p does not — it 'fits inside' p. For a multimodal p, q will typically collapse to a single mode rather than spread across all modes. The reverse KL, D_KL(p||q), has the opposite behavior: it penalizes q for assigning low probability where p is high, producing moment-matching (mean-seeking) approximations that cover all modes but may be too diffuse."

- question: "Explain the relationship between KL divergence and mutual information. How is I(X;Y) expressed as a KL divergence, and what does this representation reveal?"
  type: short-answer
  answer: "Mutual information is the KL divergence between the joint distribution and the product of marginals: I(X;Y) = D_KL(p(x,y) || p(x)p(y)). This reveals that mutual information measures how far X and Y are from being independent — it is the information cost of wrongly assuming independence when the variables are actually dependent. If X and Y are independent, the joint equals the product of marginals, the KL divergence is zero, and I(X;Y) = 0. This representation also makes it clear why mutual information is always non-negative: it inherits this from Gibbs' inequality (D_KL >= 0)."
  explanation: "This connection unifies two fundamental concepts: KL divergence as a measure of distributional difference, and mutual information as a measure of statistical dependence. Many other information-theoretic quantities (conditional mutual information, information gain in decision trees, ELBO in variational inference) can similarly be expressed as KL divergences."
```

## Explainer

You have seen that mutual information measures how much two random variables share. KL divergence is the more general tool: it measures how one probability distribution differs from another, and mutual information turns out to be a special case. D_KL(P || Q) = sum over x of p(x) log(p(x)/q(x)) answers: if nature generates data from P, but I designed my encoding assuming Q, how many extra bits per symbol do I waste?

The asymmetry of KL divergence is not a defect — it reflects a real distinction. D_KL(P || Q) measures the cost of using Q when the truth is P. D_KL(Q || P) measures the cost of using P when the truth is Q. These are different situations. In variational inference, minimizing D_KL(q || p) (the "forward" or "exclusive" KL) makes q avoid regions where p is small, producing compact, mode-seeking approximations. Minimizing D_KL(p || q) (the "reverse" or "inclusive" KL) makes q cover all regions where p is large, producing diffuse, mean-seeking approximations. The choice of direction fundamentally shapes the behavior of the approximation.

**Gibbs' inequality** states that D_KL(P || Q) >= 0 for all distributions P and Q, with equality if and only if P = Q. This is perhaps the most important inequality in information theory. It implies that the entropy H(P) = -sum p(x) log p(x) is the minimum average code length for distribution P — any other distribution Q used for coding adds at least D_KL(P || Q) extra bits. Gibbs' inequality also immediately proves that mutual information is non-negative, since I(X;Y) = D_KL(p(x,y) || p(x)p(y)) >= 0.

KL divergence appears throughout modern machine learning. Cross-entropy loss, the standard training objective for classification, equals H(P) + D_KL(P || Q), where P is the true label distribution and Q is the model's predicted distribution. Minimizing cross-entropy is equivalent to minimizing KL divergence (since H(P) is constant). The evidence lower bound (ELBO) in variational autoencoders involves a KL term. GANs minimize divergences between real and generated distributions. Understanding KL divergence — its asymmetry, its non-negativity, its operational meaning as wasted bits — is essential for reasoning about any system that compares probability distributions.
