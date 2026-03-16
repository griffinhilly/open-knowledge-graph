---
id: introduction-lebesgue-integral
title: Introduction to the Lebesgue Integral
domain: mathematics
course: real-analysis
prerequisites:
- id: introduction-lebesgue-measure
  type: hard
- id: fundamental-theorem-calculus-rigorous
  type: soft
tags:
- lebesgue-integral
- measure-theory
- integration
stage: advanced
status: draft
---

# Introduction to the Lebesgue Integral

## Core Idea
The Lebesgue integral extends integration to a larger class of functions using measure theory. For a non-negative measurable function f, ∫ f dμ is defined by partitioning the range (not the domain) and summing contributions weighted by measure. The Lebesgue integral has superior convergence theorems (Dominated Convergence, Monotone Convergence) compared to the Riemann integral.

## Explainer

Recall how the Riemann integral works: partition the *domain* into small intervals, pick a sample point in each, multiply height by width, and sum. This works beautifully for continuous functions, but fails for anything too irregular. The classic example is the Dirichlet function — 1 on rationals, 0 on irrationals. The Riemann integral cannot handle it because every interval contains both rationals and irrationals, so the upper and lower sums never agree. From your study of Lebesgue measure, you know that the rationals have measure zero. The Lebesgue perspective says: the Dirichlet function should integrate to 0, because it equals 0 "almost everywhere." The entire machinery of Lebesgue integration is built to make this intuition rigorous.

The key reversal is **partitioning the range instead of the domain**. Rather than asking "what is f(x) on this small interval of x-values?", ask "for which set of x-values does f(x) lie in this small interval [a, b] of output values?" The measure of that preimage set plays the role that interval width plays in Riemann integration. For a **simple function** — one that takes only finitely many values — this is straightforward: ∫ φ dμ = Σ cᵢ · μ(Eᵢ), where Eᵢ is the set where φ = cᵢ. The Lebesgue integral of a general non-negative measurable function is then defined as the supremum over all simple functions bounded below by f. This construction inherits all the pleasant properties of measure: it handles countably many exceptional points without issue, it works on abstract measure spaces, and it interacts cleanly with the σ-algebra structure.

The real payoff is the convergence theorems. The Riemann framework gives you results like "if fₙ → f uniformly, then ∫ fₙ → ∫ f" — uniform convergence is a very strong condition. Lebesgue gives you far more powerful theorems. The **Monotone Convergence Theorem** says: if fₙ is a sequence of non-negative measurable functions increasing pointwise to f, then ∫ fₙ dμ → ∫ f dμ. No uniformity required. The **Dominated Convergence Theorem** is the most frequently used tool in analysis: if fₙ → f pointwise (or almost everywhere) and |fₙ(x)| ≤ g(x) for some integrable function g, then ∫ fₙ dμ → ∫ f dμ. The dominating function g serves as a "ceiling" that prevents the fₙ from escaping to infinity in any direction, justifying the interchange. These theorems are what make modern probability theory, functional analysis, and Fourier analysis work — they let you pass limits through integrals in situations where Riemann integration would be silent or wrong.
