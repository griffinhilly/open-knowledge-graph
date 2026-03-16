---
id: simple-functions-approximation
title: Simple Functions and Approximation
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: measurable-functions-definition
  type: hard
builds-toward:
- lebesgue-integral-simple-functions
tags:
- measure-theory
- simple-functions
stage: abstract-reasoning
status: draft
---

# Simple Functions and Approximation

## Core Idea
A simple function is a finite linear combination of indicator functions: φ = Σᵢ aᵢ 𝟙ₐᵢ. Every non-negative measurable function is the pointwise limit of an increasing sequence of simple functions. Simple functions form the foundation for constructing the Lebesgue integral.

## How It's Best Learned
Construct increasing sequences of simple approximations by discretizing height levels of a given measurable function.

## Common Misconceptions
Simple functions must be finite sums. While countable sums of measurable functions remain measurable, they are no longer 'simple.' Approximation is pointwise, not uniform.

## Explainer

Before the Lebesgue integral can be defined for arbitrary measurable functions, we need a class of functions simple enough to integrate by inspection yet rich enough to approximate anything. **Simple functions** fill this role exactly.

A simple function is a finite linear combination of **indicator functions**: φ = a₁𝟙_{A₁} + a₂𝟙_{A₂} + ... + aₙ𝟙_{Aₙ}, where each Aᵢ is a measurable set and each aᵢ is a real number. The indicator 𝟙_A equals 1 on A and 0 outside it, so φ is a function taking only finitely many values, each on a measurable set. Think of a histogram with flat horizontal bars: that picture is a simple function. Its integral is immediate — ∫φ dμ = Σ aᵢμ(Aᵢ) — a weighted sum of the measures of its level sets.

The central theorem is that every non-negative measurable function can be approximated from below by an increasing sequence of simple functions. The construction is geometric: divide the "height axis" into strips of width 1/n. For each integer k from 1 to n², define the set where k/n ≤ f(x) < (k+1)/n, and assign height k/n there. Stack these indicator functions to build a staircase φₙ that increases pointwise toward f. As n → ∞, the stairs become infinitely fine and φₙ(x) → f(x) at every point. The sequence {φₙ} is monotone increasing and converges to f pointwise everywhere.

This approximation theorem is the engine of the Lebesgue integral. For a general non-negative measurable function, the integral is defined as ∫f dμ = lim_{n→∞} ∫φₙ dμ — you integrate the simple approximations and take the limit. The theorem guarantees this bridge exists for every non-negative measurable function, not just well-behaved ones. The requirement that the sum defining a simple function is *finite* is essential: infinite sums would reintroduce the convergence problems the theory is designed to handle, and the clean formula ∫φ dμ = Σ aᵢμ(Aᵢ) depends on having only finitely many terms to sum.
