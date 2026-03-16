---
id: rational-functions-asymptotes-review
title: Rational Functions and Asymptotes Review
domain: mathematics
course: precalculus
prerequisites:
  - id: domain-and-range
    type: hard
  - id: polynomial-division-review
    type: hard
builds-toward:
  - limits-at-infinity
  - infinite-limits
tags: [rational-functions, asymptotes, graphing]
stage: formal-systems
status: validated
---

# Rational Functions and Asymptotes Review

## Core Idea
A rational function is a ratio of two polynomials, p(x)/q(x). Its behavior is governed by where the denominator is zero (vertical asymptotes or holes), the end behavior as x approaches infinity (horizontal or oblique asymptotes), and the zeros of the numerator (x-intercepts). Understanding rational functions bridges algebra and the limit concept central to calculus.

## How It's Best Learned
Systematically analyze: find domain, factor numerator and denominator, identify holes vs. vertical asymptotes, determine horizontal asymptote by comparing degrees, use polynomial division for oblique asymptotes. Graph by plotting key features and testing intervals.

## Common Misconceptions
- Confusing holes (common factors that cancel) with vertical asymptotes (factors that remain).
- Believing the graph cannot cross a horizontal asymptote (it can, in the middle of the graph).
- Forgetting that the degree comparison for horizontal asymptotes only applies as x approaches infinity.

## Explainer

A **rational function** is a fraction where both numerator and denominator are polynomials: f(x) = p(x)/q(x). Its behavior is entirely governed by where the denominator is zero (danger zones), how the numerator and denominator compare in degree (end behavior), and where the numerator is zero (x-intercepts). From your work with domain and range, you know that any x making q(x) = 0 is excluded from the domain. What happens *near* those points, and what happens *far* from them in either direction, is what asymptotes describe.

**Vertical asymptotes** occur where the denominator is zero and the factor doesn't cancel. Factor both numerator and denominator completely. If a factor (x − a) appears in the denominator but not the numerator, then x = a is a vertical asymptote — the function grows without bound as x approaches a. If the same factor appears in both numerator and denominator, it cancels, and x = a is a **hole** (a removable discontinuity) rather than an asymptote. This distinction matters: a hole is just a missing point; a vertical asymptote is a wall the function never crosses.

**Horizontal asymptotes** describe what happens to f(x) as x → ±∞. From your polynomial division review, you can see why: for very large x, the highest-degree terms dominate all others. If deg(p) < deg(q), the denominator grows faster, so f(x) → 0 (horizontal asymptote at y = 0). If deg(p) = deg(q), the ratio of leading coefficients dominates, giving a nonzero horizontal asymptote y = a_n/b_n. If deg(p) > deg(q) by exactly 1, polynomial long division gives a linear quotient — that quotient is an **oblique asymptote** and there is no horizontal one. If deg(p) exceeds deg(q) by more than 1, the function grows without bound and there is no horizontal asymptote at all.

A common surprise is that a graph *can* cross its horizontal asymptote — asymptotes describe limiting behavior, not absolute barriers. The graph might weave across the horizontal asymptote in the middle of the domain before settling down near it at the extremes. Vertical asymptotes, by contrast, are true barriers: the function is undefined there and never crosses. Building intuition for rational functions means developing a mental checklist — factor, identify holes and vertical asymptotes, compare degrees for end behavior, find intercepts, sketch the curve in each region — and this systematic approach is exactly what limits and calculus will formalize when you study infinite limits and limits at infinity.
