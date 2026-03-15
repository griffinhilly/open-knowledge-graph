---
id: uniform-continuity
title: Uniform Continuity
domain: mathematics
course: real-analysis
prerequisites:
- id: epsilon-delta-continuity
  type: hard
builds-toward:
- uniform-continuity-compact-sets
- riemann-integral-darboux-sums
tags:
- uniform-continuity
- epsilon-delta
- strengthened
stage: advanced
status: draft
---

# Uniform Continuity

## Core Idea
A function f is uniformly continuous on a set S if for every ε > 0, there exists δ > 0 (independent of the point) such that for all x, y ∈ S, |x - y| < δ implies |f(x) - f(y)| < ε. This is stronger than pointwise continuity: δ works at all points simultaneously. It is essential for convergence of integrals and derivatives.

## How It's Best Learned
Show f(x) = x is uniformly continuous but f(x) = x² is not on ℝ (though it is on [0,1]). Prove f(x) = 1/x is not uniformly continuous on (0,1) but is on [1,∞).

## Common Misconceptions
- Confusing 'δ depends on ε but not on x' with 'δ is constant'; it can depend on ε.
- Thinking uniform continuity at a point makes sense; it's a property of a function on a set.
- Assuming every continuous function is uniformly continuous; f(x) = x² on ℝ is a counterexample.
