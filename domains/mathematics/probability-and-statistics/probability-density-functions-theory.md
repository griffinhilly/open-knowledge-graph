---
id: probability-density-functions-theory
title: Probability Density Functions and Continuous Distributions
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: random-variables-definition-types
  type: hard
- id: definite-integral-definition
  type: hard
builds-toward:
- expected-value
- normal-distribution
tags:
- pdf
- continuous
stage: formal-systems
status: draft
---

# Probability Density Functions and Continuous Distributions

## Core Idea
The PDF f(x) of a continuous random variable satisfies P(a≤X≤b)=∫ₐᵇ f(x)dx. Valid PDFs satisfy f(x)≥0 and ∫f(x)dx=1. Unlike the PMF, f(x) is not a probability itself, and P(X=x)=0 for any single value. The PDF completely characterizes continuous distributions.

## Questions

```yaml
- question: "A continuous random variable X has PDF f(x) = 4 for x ∈ [0, 0.25] and f(x) = 0 elsewhere. What is P(X = 0.1)?"
  type: multiple-choice
  options:
    - "0.4, since f(0.1) = 4 and we multiply by the distance 0.1 from the left endpoint"
    - "4, since f(0.1) = 4 is the PDF value at x = 0.1"
    - "0, since the probability of any single exact value is zero for a continuous distribution"
    - "0.25, since 0.1 falls within the support interval [0, 0.25]"
  answer: 2
  explanation: "For any continuous random variable, P(X = c) = 0 for every specific value c, regardless of how large the PDF is there. Probability accumulates only over intervals with nonzero width. f(0.1) = 4 tells you the density at that point — how concentrated probability is near 0.1 — but a single point has no width, so its contribution to probability is zero. To find a nonzero probability you must integrate: P(0 ≤ X ≤ 0.25) = ∫₀^0.25 4 dx = 1."

- question: "A student claims: 'A PDF with f(x) = 3 on the interval [0, 1/3] and f(x) = 0 elsewhere is invalid, because a probability function cannot exceed 1.' Is the student right?"
  type: multiple-choice
  options:
    - "Yes — a valid PDF must always satisfy 0 ≤ f(x) ≤ 1 for all x"
    - "No — f(x) is a density, not a probability; what must equal 1 is the total area ∫f(x)dx, not the function values"
    - "Yes — probabilities are between 0 and 1, so the density representing them must be as well"
    - "No — but this PDF is still technically invalid because the support [0, 1/3] is too short"
  answer: 1
  explanation: "The student is wrong. The constraints on a valid PDF are: (1) f(x) ≥ 0 everywhere, and (2) ∫₋∞^∞ f(x)dx = 1. The function value f(x) is a density, not a probability, and is not bounded above by 1. Here, f(x) = 3 on [0, 1/3] gives total area = 3 × (1/3) = 1, so the PDF is perfectly valid. The analogy to physical density is exact: just as mass per unit volume can far exceed 1, probability per unit length can too, as long as the total integrates to 1."

- question: "A valid probability density function must satisfy f(x) ≤ 1 for all values of x in its support."
  type: true-false
  answer: false
  explanation: "This is a very common misconception. The constraint is that the total area under the PDF equals 1: ∫f(x)dx = 1. The function values themselves can be arbitrarily large. A uniform distribution on [0, 0.1] has f(x) = 10 throughout its support — perfectly valid, because 10 × 0.1 = 1. Confusing 'density' with 'probability' leads to this error. Density is probability per unit length; it is not bounded by 1."

- question: "For a continuous random variable X, P(a ≤ X ≤ b) equals P(a < X < b) for any a < b."
  type: true-false
  answer: true
  explanation: "Including or excluding the endpoints makes no difference for continuous random variables because P(X = a) = 0 and P(X = b) = 0. Since individual points contribute zero probability, the events {a ≤ X ≤ b} and {a < X < b} differ only by two probability-zero points, so they have identical probabilities. This is a key difference from discrete distributions, where endpoint inclusion can matter significantly."

- question: "Explain why the value of a PDF at a single point f(c) is not a probability, and describe what operation you must perform on the PDF to extract actual probability."
  type: short-answer
  answer: "f(c) is a density — it measures how concentrated probability is per unit length near c, not the probability of landing exactly at c. A single point has zero width, so it captures zero probability regardless of how large f(c) is. To get actual probability, you must integrate f(x) over an interval: P(a ≤ X ≤ b) = ∫ₐᵇ f(x)dx. The integral sums infinitely many infinitesimally thin probability slices. Just as physical mass is found by integrating density over a region (not by reading off density at a point), probability is found by integrating the PDF over an interval."
  explanation: "The analogy to physical density is the deepest way to understand PDFs. Mass density tells you concentration per unit volume; integrating gives total mass. Probability density tells you probability concentration per unit length; integrating gives total probability. The density value at a point is meaningful as a comparative measure (peaks show where X is likely to fall), but only the integral gives actual probability."
```

## Explainer

You already know that a random variable assigns a number to each outcome, and you know from working with discrete random variables that a **probability mass function (PMF)** gives P(X = x) directly. The jump to continuous distributions requires giving up something: for a continuous random variable, the probability of landing on any single exact value is zero. This sounds strange at first — if X is "uniformly distributed on [0,1]," what is P(X = 0.5)? The answer is exactly zero, not because it's impossible, but because a single point has no width, and probability accumulates over intervals, not points.

This is where the **probability density function (PDF)** comes in. Think of f(x) as a density in the same sense as physical density: it tells you how probability is concentrated per unit length along the real line. Just as you find mass by integrating density over a region (mass = ∫ρ dV), you find probability by integrating the PDF over an interval: P(a ≤ X ≤ b) = ∫ₐᵇ f(x) dx. The definite integral you studied is exactly the right tool here — it sums up infinitely many infinitesimally thin slices of probability. The total area under the entire PDF must equal 1, because the probability of X landing somewhere is certain.

A valid PDF must satisfy two conditions: f(x) ≥ 0 everywhere (you can't have negative probability density), and ∫₋∞^∞ f(x) dx = 1. Notice that f(x) itself is not bounded above by 1 — it is a density, not a probability, so values greater than 1 are perfectly legal as long as the total area is 1. For example, a uniform distribution on [0, 0.5] has f(x) = 2, because the density must be 2 to make the total area (0.5 × 2 = 1) correct.

The deepest difference from the discrete case is that **the PDF value at a point carries no probability meaning on its own**. If f(0.5) = 2, that does not mean P(X = 0.5) = 2 — it means probability is densely packed near 0.5. What matters is always the integral over a region. This is analogous to how knowing the density of water at a single molecule tells you nothing about the mass of a sample — you must integrate. Once you internalize this, continuous distributions become intuitive: the PDF shapes how probability is distributed across the real line, and integration is the operation that extracts probability from that shape.

The PDF is the complete description of a continuous distribution. Everything you will want to compute — expected values, variances, probabilities of events — comes down to integrating f(x) against appropriate functions. The normal distribution, exponential distribution, and every other continuous distribution you will encounter is fully characterized by its PDF. The skill to develop now is reading a PDF as a picture: peaks show where values are likely, troughs show where they are rare, and the total area always stays at 1.
