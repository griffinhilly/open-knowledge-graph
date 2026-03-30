---
id: differential-entropy
title: Differential Entropy
domain: computer-science
course: information-theory
prerequisites:
- id: shannon-entropy
  type: hard
- id: probability-distributions
  type: hard
- id: random-variables
  type: hard
builds-toward:
- gaussian-channel
- maximum-entropy-principle
- fisher-information
- information-geometry-basics
tags:
- differential entropy
- continuous entropy
- negative entropy
- Gaussian
stage: expert
status: validated
---

# Differential Entropy

## Core Idea
Differential entropy h(X) = -integral f(x) log f(x) dx extends Shannon entropy to continuous random variables by replacing sums with integrals and probabilities with densities. Unlike discrete entropy, differential entropy can be negative (a narrow Gaussian has h(X) < 0). It is NOT the limit of discrete entropy as the quantization becomes finer — that limit diverges. Despite this, differences of differential entropies are well-defined and match the corresponding discrete quantities: mutual information I(X;Y) = h(X) - h(X|Y) is always non-negative and finite. Differential entropy is essential for analyzing continuous channels, Gaussian sources, and rate-distortion theory.

## Questions

```yaml
- question: "A continuous random variable X ~ Uniform(0, 1/4) has differential entropy h(X) = log2(1/4) = -2 bits. How should this negative value be interpreted?"
  type: multiple-choice
  options:
    - "The source generates negative information, which is physically impossible — the formula is wrong"
    - "Differential entropy is negative because the density exceeds 1 — the source is highly concentrated, and the negative value reflects that it takes fewer bits to describe X than a reference Uniform(0,1) variable"
    - "Negative entropy means the random variable is deterministic"
    - "The logarithm should use natural log to avoid negative values"
  answer: 1
  explanation: "Differential entropy measures information content RELATIVE to a continuous uniform reference, not in absolute terms. When the density f(x) > 1 (as for Uniform(0, 1/4), where f(x) = 4), log f(x) > 0, making -f(x) log f(x) negative. The interpretation: X is 'more concentrated' than a unit-width uniform distribution, so its differential entropy is negative. Crucially, the mutual information I(X;Y) = h(X) - h(X|Y) is still non-negative and operationally meaningful. Differential entropy by itself is not the number of bits needed to represent X (that is infinite for continuous variables); only entropy differences have operational meaning."

- question: "Among all continuous distributions with a fixed variance sigma^2, the Gaussian distribution maximizes differential entropy."
  type: true-false
  answer: true
  explanation: "This is a fundamental result. Among all distributions on the real line with variance sigma^2, the Gaussian N(0, sigma^2) has the maximum differential entropy: h(X) = (1/2) log2(2*pi*e*sigma^2). This can be proved using the non-negativity of KL divergence: for any distribution f with variance sigma^2, D_KL(f || phi) >= 0 where phi is the Gaussian, which implies h(f) <= h(phi). This result is why the Gaussian channel has a particularly clean capacity formula — the worst-case noise (from an information-theoretic perspective) is Gaussian."

- question: "Explain why differential entropy is not simply the limit of discrete entropy as quantization becomes infinitely fine, and what this implies about the relationship between discrete and continuous information theory."
  type: short-answer
  answer: "If you quantize a continuous variable X into bins of width delta, the discrete entropy of the quantized version is approximately h(X) + log(1/delta). As delta -> 0, log(1/delta) -> infinity, so the discrete entropy diverges. The finite quantity h(X) is what remains after subtracting this divergent term. This means differential entropy is an entropy DIFFERENCE, not an absolute entropy — it depends on the coordinate system (units of measurement). Changing variables from X to Y = aX shifts h by log|a|, unlike discrete entropy which is invariant under relabeling. The practical implication: only DIFFERENCES of differential entropies (like mutual information) are physically meaningful. Absolute differential entropy is a useful computational tool but lacks the direct operational interpretation of discrete entropy."
  explanation: "This subtlety trips up many students: they expect h(X) to represent 'the number of bits to describe X,' but describing a continuous variable to infinite precision requires infinite bits. What h(X) captures is the information content relative to a continuous uniform density — a quantity that is useful for computing mutual information and capacity but is not meaningful in isolation."
```

## Explainer

Shannon entropy works perfectly for discrete random variables, but continuous variables require care. You might try directly substituting integrals for sums in the entropy formula, and indeed that gives **differential entropy**: h(X) = -integral f(x) log f(x) dx, where f(x) is the probability density function. This quantity is useful but has important differences from its discrete counterpart.

The most striking difference is that differential entropy can be negative. A Uniform(0, 1/2) random variable has h(X) = log2(1/2) = -1 bit. A very narrow Gaussian has large, positive density values, making -f(x) log f(x) negative over most of its support. This seems paradoxical until you realize what happened: densities can exceed 1 (unlike probabilities), so log f(x) can be positive, flipping the sign. The negativity reflects extreme concentration, not any pathology.

The deeper issue is that differential entropy is NOT the true continuous analog of discrete entropy. If you quantize X into bins of width delta, the discrete entropy is approximately h(X) + log(1/delta). As delta shrinks, the discrete entropy grows without bound — it takes infinitely many bits to specify a continuous value exactly. Differential entropy is what remains after subtracting this infinite offset. Consequently, h(X) depends on the coordinate system: scaling X by a constant a changes h(X) by log|a|, unlike discrete entropy which is invariant under permutations of the alphabet.

Despite these subtleties, differential entropy is extremely useful because **differences** of differential entropies are well-behaved. Mutual information I(X;Y) = h(X) - h(X|Y) is always non-negative, coordinate-invariant, and has the same operational interpretation as in the discrete case. The capacity of the Gaussian channel, C = (1/2) log(1 + P/N), is derived using differential entropy. Rate-distortion functions for continuous sources use differential entropy. The maximum-entropy property of the Gaussian (h_Gauss >= h_other for fixed variance) is proved using differential entropy. The rule of thumb: use differential entropy freely in calculations, but only trust differences of differential entropies for operational conclusions.
