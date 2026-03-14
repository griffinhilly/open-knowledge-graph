---
id: bessel-functions
title: Bessel Functions and Their Properties
domain: mathematics
course: differential-equations
prerequisites:
- id: frobenius-method
  type: hard
builds-toward:
- separation-of-variables-for-pdes
tags:
- special-functions
- bessel
- orthogonal
stage: advanced
status: draft
---

# Bessel Functions and Their Properties

## Core Idea
Bessel functions J_n(x) are solutions to Bessel's equation x²y'' + xy' + (x² - n²)y = 0, arising in cylindrical coordinate PDEs. They oscillate with decreasing amplitude, possess orthogonality properties, and appear in heat, wave, and vibration problems with cylindrical symmetry.

## How It's Best Learned
Study graphs of J₀(x) and J₁(x) to see oscillatory decay. Learn integral representations and orthogonality: ∫₀¹ x·J_m(λ_m·x)·J_m(λ_n·x) dx = 0 for m ≠ n. Use Bessel function tables for numerical work.

## Common Misconceptions
- Thinking J_n(x) ~ cos(x) for large x; the asymptotic form is J_n(x) ~ √(2/(πx))·cos(x - nπ/2 - π/4). - Forgetting the factor x in the orthogonality inner product for Bessel functions. - Confusing J_n with Neumann functions Y_n or Hankel functions; each solves the same ODE but with different boundary behavior.
