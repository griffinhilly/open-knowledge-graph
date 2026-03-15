---
id: cauchys-integral-formula
title: Cauchy's Integral Formula
domain: mathematics
course: complex-analysis
prerequisites:
- id: cauchys-theorem
  type: hard
builds-toward:
- cauchys-integral-formula-derivatives
- taylor-series-complex
tags:
- cauchys-integral-formula
- reconstruction
- values-from-boundary
stage: advanced
status: draft
---

# Cauchy's Integral Formula

## Core Idea
If f is holomorphic in a simply connected domain D and γ is a simple closed contour in D enclosing a point z₀, then f(z₀) = (1/2πi) ∮_γ f(z)/(z - z₀) dz. This formula says the value of an analytic function at an interior point is completely determined by its values on any surrounding contour — a rigidity that has no real analogue.

## How It's Best Learned
Apply this formula to f(z) = z² and a circle around z = 0 to verify it gives f(0) = 0. This may seem trivial, but the power comes when f is complicated and you can choose any contour.

## Common Misconceptions
Thinking this is just an integral formula; it reveals that analytic functions are completely rigid. Assuming the contour can be any curve; it must enclose z₀ and lie in the domain of analyticity.
