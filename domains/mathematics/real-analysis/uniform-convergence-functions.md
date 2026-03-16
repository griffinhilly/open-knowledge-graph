---
id: uniform-convergence-functions
title: Uniform Convergence
domain: mathematics
course: real-analysis
prerequisites:
- id: pointwise-convergence-functions
  type: hard
builds-toward:
- uniform-convergence-preserves-continuity
- weierstrass-m-test
- interchange-limit-integral
- interchange-limit-derivative
tags:
- uniform-convergence
- function-sequences
- strengthened
stage: advanced
status: draft
---

# Uniform Convergence

## Core Idea
A sequence of functions (fₙ) converges uniformly to f on a set S if for every ε > 0, there exists N (independent of x) such that for all x ∈ S, n > N implies |fₙ(x) - f(x)| < ε. Uniform convergence is stronger than pointwise and guarantees that limits can be exchanged with derivatives and integrals. It is fundamental to analysis on function spaces.

## Explainer

You already understand **pointwise convergence**: fₙ converges pointwise to f if, for each fixed x, the number sequence fₙ(x) converges to f(x). Every x gets its own race to the finish line — every x eventually arrives, but different points may need wildly different amounts of time. This "each x on its own schedule" aspect is what makes pointwise convergence too weak for preserving analytical structure.

**Uniform convergence** tightens this: the entire domain must finish by the same lap N. Formally, for every ε > 0, there is a single N depending only on ε (not on x) such that once n > N, every point in the domain is within ε of f simultaneously. Picture it geometrically: the tube of width ±ε around the limit function f eventually swallows the entire graph of fₙ at once — not pointwise region by region.

The classic counterexample that separates the two notions is fₙ(x) = xⁿ on [0, 1]. Pointwise, this converges to f(x) = 0 for x ∈ [0, 1) and f(1) = 1 — a discontinuous limit function. Each fₙ is continuous, but the pointwise limit is not. This discontinuity cannot arise under uniform convergence: the uniform limit of continuous functions is always continuous. This theorem is the key example of why uniform convergence is the "right" notion for preserving analytical properties.

The practical test is the **supremum criterion**: fₙ → f uniformly if and only if sup_{x∈S} |fₙ(x) − f(x)| → 0 as n → ∞. This converts a universal quantifier over x into a single limit on a supremum — a much more tractable object. For series, the **Weierstrass M-test** provides a sufficient condition: if |gₙ(x)| ≤ Mₙ for all x and ΣMₙ converges (as a series of constants), then Σgₙ converges uniformly and absolutely. This is the standard tool for establishing uniform convergence of power series and Fourier series. Everything downstream — preserving continuity, exchanging limits with integrals, exchanging limits with derivatives — depends on whether this one uniform convergence condition holds.
