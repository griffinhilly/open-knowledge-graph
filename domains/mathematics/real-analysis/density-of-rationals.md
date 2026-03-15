---
id: density-of-rationals
title: Density of the Rationals
domain: mathematics
course: real-analysis
prerequisites:
- id: archimedean-property
  type: hard
- id: supremum-and-infimum
  type: hard
builds-toward:
- epsilon-n-convergence
tags:
- rationals
- density
- approximation
stage: advanced
status: draft
---

# Density of the Rationals

## Core Idea
Between any two distinct real numbers, there exists at least one rational number, and hence infinitely many. This is the density of ℚ in ℝ: the closure of ℚ is ℝ. Density means rationals are arbitrarily close to any real number, making them essential for approximation in analysis.

## How It's Best Learned
Prove this using the Archimedean Property: given reals a < b, show that n(b - a) > 1 for some n, then find the smallest integer m with m/n > a. Construct rational approximations to √2 and π to see the density in action.

## Common Misconceptions
- Thinking density means rationals are 'everywhere' contradicts the uncountability of irrationals.
- Confusing density with continuity; density is discrete (countably many rationals) in a continuous space.
- Assuming density implies every real is rational, which is false.
