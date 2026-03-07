---
id: rational-functions-and-asymptotes
title: Rational Functions and Asymptotes
domain: mathematics
course: algebra-2
prerequisites:
  - id: polynomial-long-division
    type: hard
  - id: polynomial-functions-degree-and-leading-coefficient
    type: hard
builds-toward:
  - graphing-rational-functions
  - solving-rational-equations
tags: [rational-functions, asymptotes, vertical, horizontal, oblique]
stage: abstract-reasoning
status: draft
---

# Rational Functions and Asymptotes

## Core Idea
A rational function is a ratio of two polynomials: f(x) = p(x)/q(x). Vertical asymptotes occur at values where q(x) = 0 and p(x) != 0. Horizontal asymptotes depend on the degree comparison: if deg(p) < deg(q), the HA is y = 0; if deg(p) = deg(q), the HA is y = (leading coefficient of p)/(leading coefficient of q); if deg(p) > deg(q), there is no horizontal asymptote (but there may be an oblique asymptote found via polynomial long division). Holes occur where both p and q share a common factor.

## How It's Best Learned
Analyze the function algebraically before graphing: find domain restrictions, factor numerator and denominator, identify holes vs. vertical asymptotes, determine horizontal/oblique asymptotes by degree comparison. Build understanding incrementally with simpler rational functions (1/x, 1/x^2) before more complex ones.

## Common Misconceptions
- Confusing holes and vertical asymptotes (holes occur when a factor cancels; VAs occur when it does not).
- Thinking the graph cannot cross a horizontal asymptote (it can, in the middle of its domain; HAs describe end behavior only).
- Not factoring before identifying asymptotes, leading to missed holes.
