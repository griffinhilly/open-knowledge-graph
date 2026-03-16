---
id: condition-number
title: Condition Number of a Problem
domain: mathematics
course: numerical-analysis
prerequisites:
- id: numerical-stability
  type: hard
- id: mean-value-theorem
  type: soft
builds-toward:
- condition-number-of-matrix
tags:
- condition-number
- conditioning
- sensitivity
stage: abstract-reasoning
status: draft
---

# Condition Number of a Problem

## Core Idea
The condition number measures how much the solution changes relative to changes in input data. A large condition number indicates an ill-conditioned problem where small input perturbations cause large output changes. The relative condition number κ(x) = |x f'(x) / f(x)| quantifies this sensitivity for a general function f.

## Explainer

From your study of numerical stability, you learned to distinguish between problems that are inherently sensitive and algorithms that introduce unnecessary error. The condition number makes the inherent sensitivity of a problem precise and quantitative. It answers: "If my input has a tiny relative error ε, how large a relative error should I expect in the output — before I've even chosen an algorithm?"

The formula κ(x) = |x f′(x) / f(x)| has a clear structure. The numerator |x f′(x)| captures how fast the output changes (via the derivative, connecting to the Mean Value Theorem you know), scaled by the size of the input x. The denominator |f(x)| normalizes by the output size. The result is dimensionless: a condition number of 100 means a relative input error of 0.01% can produce a relative output error of up to 1%. You can think of κ as an amplification factor for relative errors.

Concrete examples sharpen the intuition. Consider f(x) = √x near x = 1. Here κ(1) = |1 · (1/2) / 1| = 0.5 — well-conditioned; relative errors shrink by half. Now consider f(x) = ln(x) near x ≈ 1. Here f′(x) = 1/x, so κ(x) = |x · (1/x) / ln(x)| = 1/|ln(x)|. As x → 1, ln(x) → 0, so κ → ∞. Taking the logarithm of a number close to 1 is **ill-conditioned**: tiny relative errors in x produce enormous relative errors in ln(x). This is a property of the mathematical problem, not the algorithm.

A critical conceptual move: conditioning is a **problem property**, stability is an **algorithm property**. An ill-conditioned problem will give inaccurate answers no matter how careful you are — the underlying mathematics is sensitive, and floating-point inputs always carry small errors. A well-conditioned problem, however, can still be ruined by an unstable algorithm. The condition number sets the ceiling on achievable accuracy; stable algorithms approach that ceiling. When numerical results look wrong, diagnosing which of these two issues you have — is the problem ill-conditioned, or is the algorithm unstable? — determines whether better arithmetic or a better algorithm is the solution.
