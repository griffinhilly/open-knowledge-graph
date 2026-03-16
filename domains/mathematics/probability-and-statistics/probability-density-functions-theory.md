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

## Explainer

You already know that a random variable assigns a number to each outcome, and you know from working with discrete random variables that a **probability mass function (PMF)** gives P(X = x) directly. The jump to continuous distributions requires giving up something: for a continuous random variable, the probability of landing on any single exact value is zero. This sounds strange at first — if X is "uniformly distributed on [0,1]," what is P(X = 0.5)? The answer is exactly zero, not because it's impossible, but because a single point has no width, and probability accumulates over intervals, not points.

This is where the **probability density function (PDF)** comes in. Think of f(x) as a density in the same sense as physical density: it tells you how probability is concentrated per unit length along the real line. Just as you find mass by integrating density over a region (mass = ∫ρ dV), you find probability by integrating the PDF over an interval: P(a ≤ X ≤ b) = ∫ₐᵇ f(x) dx. The definite integral you studied is exactly the right tool here — it sums up infinitely many infinitesimally thin slices of probability. The total area under the entire PDF must equal 1, because the probability of X landing somewhere is certain.

A valid PDF must satisfy two conditions: f(x) ≥ 0 everywhere (you can't have negative probability density), and ∫₋∞^∞ f(x) dx = 1. Notice that f(x) itself is not bounded above by 1 — it is a density, not a probability, so values greater than 1 are perfectly legal as long as the total area is 1. For example, a uniform distribution on [0, 0.5] has f(x) = 2, because the density must be 2 to make the total area (0.5 × 2 = 1) correct.

The deepest difference from the discrete case is that **the PDF value at a point carries no probability meaning on its own**. If f(0.5) = 2, that does not mean P(X = 0.5) = 2 — it means probability is densely packed near 0.5. What matters is always the integral over a region. This is analogous to how knowing the density of water at a single molecule tells you nothing about the mass of a sample — you must integrate. Once you internalize this, continuous distributions become intuitive: the PDF shapes how probability is distributed across the real line, and integration is the operation that extracts probability from that shape.

The PDF is the complete description of a continuous distribution. Everything you will want to compute — expected values, variances, probabilities of events — comes down to integrating f(x) against appropriate functions. The normal distribution, exponential distribution, and every other continuous distribution you will encounter is fully characterized by its PDF. The skill to develop now is reading a PDF as a picture: peaks show where values are likely, troughs show where they are rare, and the total area always stays at 1.
