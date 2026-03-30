---
id: shannon-entropy
title: Shannon Entropy
domain: computer-science
course: information-theory
prerequisites:
- id: probability-distributions
  type: hard
- id: expected-value
  type: hard
- id: logarithms
  type: hard
- id: random-variables
  type: soft
builds-toward:
- joint-and-conditional-entropy
- mutual-information
- source-coding-theorem
- maximum-entropy-principle
- entropy-rate-stochastic-processes
tags:
- entropy
- uncertainty
- information
- bits
- Shannon
stage: advanced
status: validated
---

# Shannon Entropy

## Core Idea
Shannon entropy H(X) = -sum p(x) log p(x) quantifies the average uncertainty or "surprise" in a random variable X. It measures the minimum average number of bits needed to encode outcomes drawn from a distribution. A fair coin has entropy 1 bit; a biased coin has less. Entropy is maximized when all outcomes are equally likely and equals zero only when the outcome is certain. It is the foundational quantity of information theory, from which nearly all other measures are derived.

## Questions

```yaml
- question: "A random variable X takes four values, each with probability 1/4. What is H(X), and why does this value have a natural interpretation in terms of binary encoding?"
  type: multiple-choice
  options:
    - "H(X) = 4 bits, because there are 4 possible outcomes"
    - "H(X) = 2 bits, because log2(4) = 2, meaning two binary questions perfectly identify the outcome"
    - "H(X) = 1 bit, because each outcome has the same probability"
    - "H(X) = 0 bits, because there is no uncertainty when all outcomes are equally likely"
  answer: 1
  explanation: "H(X) = -4*(1/4)*log2(1/4) = -4*(1/4)*(-2) = 2 bits. This means you need exactly 2 binary questions (bits) to identify which of 4 equally likely outcomes occurred. Entropy measures average surprise: each outcome contributes -log2(1/4) = 2 bits of surprise, and averaging over all outcomes gives 2. Entropy equals log2(n) for a uniform distribution over n outcomes — this is the maximum entropy for n outcomes."

- question: "A source emits symbol A with probability 0.99 and symbol B with probability 0.01. Which statement about H(X) is correct?"
  type: multiple-choice
  options:
    - "H(X) is close to 1 bit because there are two symbols"
    - "H(X) is close to 0 bits because the outcome is nearly certain — most of the time there is very little surprise"
    - "H(X) equals exactly 0 bits because one probability dominates"
    - "H(X) is negative because one probability is very small"
  answer: 1
  explanation: "H(X) = -0.99*log2(0.99) - 0.01*log2(0.01) ≈ 0.081 bits. When one outcome dominates, there is very little uncertainty on average — you almost always see A, which carries negligible surprise. The rare B carries high surprise (-log2(0.01) ≈ 6.64 bits), but it occurs so infrequently that its contribution to the average is small. Entropy reaches its maximum of 1 bit for two symbols only when both are equally likely (p = 0.5)."

- question: "Shannon entropy can be negative for discrete random variables."
  type: true-false
  answer: false
  explanation: "Shannon entropy for discrete random variables is always non-negative: H(X) >= 0. Each term -p(x)*log(p(x)) is non-negative because 0 <= p(x) <= 1, so log(p(x)) <= 0, making -p(x)*log(p(x)) >= 0. The sum of non-negative terms is non-negative. H(X) = 0 only when the distribution is degenerate (one outcome has probability 1). Note: differential entropy (the continuous analog) CAN be negative, but discrete Shannon entropy cannot."

- question: "Explain why entropy is maximized by the uniform distribution over a finite alphabet, and what this reveals about the relationship between entropy and knowledge."
  type: short-answer
  answer: "The uniform distribution maximizes entropy because it represents maximum ignorance — every outcome is equally plausible, so there is no way to predict the next symbol better than random guessing. Mathematically, this can be proved using Jensen's inequality or Lagrange multipliers: subject to the constraint that probabilities sum to 1, H(X) = -sum p(x) log p(x) is maximized when all p(x) = 1/n, giving H(X) = log(n). Any deviation from uniformity — any structure or predictability — reduces entropy. This reveals that entropy measures what you DON'T know: the more predictable a source is, the lower its entropy, because there is less genuine uncertainty to resolve."
  explanation: "This maximum-entropy property connects to the maximum entropy principle in statistical mechanics and Bayesian inference: when you have no information beyond constraints, the distribution that maximizes entropy is the least presumptuous choice."
```

## Explainer

You know from probability that a random variable X has a distribution assigning probabilities to outcomes. Shannon's insight was to ask: how much "information" does observing an outcome of X provide? If an event has probability p, the surprise (or self-information) of seeing it is -log2(p) bits. A coin landing heads with probability 1/2 gives -log2(1/2) = 1 bit of surprise. An event with probability 1 gives zero surprise — you already knew it would happen. An event with probability 1/1024 gives 10 bits — it was deeply unexpected.

**Shannon entropy** is the expected surprise: H(X) = -sum over all x of p(x) * log2(p(x)). It averages the surprise across all possible outcomes, weighted by how often each occurs. For a fair coin, H = 1 bit. For a fair die, H = log2(6) ≈ 2.58 bits. For a degenerate distribution (one outcome certain), H = 0. The key formula uses the convention that 0 * log(0) = 0, which is justified by the limit as p approaches 0.

The operational meaning of entropy is precise: it is the minimum average number of bits per symbol needed to losslessly encode a long sequence of independent draws from the distribution. If a source has entropy 2 bits per symbol, no encoding scheme can compress the output to fewer than 2 bits per symbol on average (and there exist schemes, like Huffman or arithmetic coding, that get arbitrarily close). This is Shannon's source coding theorem, which gives entropy its concrete, engineering significance.

Entropy has several important properties. It is non-negative for discrete distributions. It is maximized by the uniform distribution (maximum ignorance). It is concave — mixtures of distributions have at least as much entropy as the average of their individual entropies. And it is additive for independent random variables: H(X, Y) = H(X) + H(Y) when X and Y are independent. These properties make entropy the natural measure of uncertainty, and all other information-theoretic quantities — joint entropy, conditional entropy, mutual information, KL divergence — are defined in terms of it.
