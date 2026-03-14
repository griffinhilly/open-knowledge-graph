---
id: fourier-series-definition
title: 'Fourier Series: Definition and Coefficients'
domain: mathematics
course: differential-equations
prerequisites:
- id: definite-integral-definition
  type: hard
- id: integration-by-parts
  type: hard
- id: trigonometric-identities-pythagorean
  type: hard
builds-toward:
- convergence-fourier-series
tags:
- fourier-series
- orthogonal-functions
- periodic
stage: advanced
status: draft
---

# Fourier Series: Definition and Coefficients

## Core Idea
A function f on [-L, L] can be written as f(x) = a₀/2 + Σ(aₙcos(nπx/L) + bₙsin(nπx/L)) with coefficients given by integrals of f against the basis functions. Fourier series decompose a function into sines and cosines, revealing frequency content. The coefficients measure the contribution of each harmonic to the overall function.
