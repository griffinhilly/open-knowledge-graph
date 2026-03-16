---
id: contour-integration
title: Contour Integration
domain: mathematics
course: complex-analysis
prerequisites:
- id: complex-line-integrals
  type: hard
builds-toward:
- cauchys-theorem
- residue-theorem
tags:
- contour-integrals
- closed-paths
- circulation
stage: advanced
status: draft
---

# Contour Integration

## Core Idea
A contour integral is the integral of f(z) around a closed path γ, written ∮_γ f(z) dz. For holomorphic f on a simply connected domain, any closed contour integral is zero — a consequence of Cauchy's theorem. For f with isolated singularities, the contour integral picks up 2πi times the sum of residues inside, the foundation of the residue theorem.

## Explainer

Complex line integrals, which you just studied, allow you to integrate f(z) along any path in the complex plane connecting two endpoints. A **contour integral** is a special case: the path is **closed**, meaning it starts and ends at the same point. The notation ∮_γ f(z) dz emphasizes this closure. What makes the closed-path case special is that the topology of what lies *inside* the path determines the value of the integral — something with no direct analogue in single-variable real calculus.

The foundational fact is that if f is **holomorphic** (complex-differentiable) everywhere inside and on the closed curve γ, then ∮_γ f(z) dz = 0. This is Cauchy's theorem, which you will prove next. Holomorphic functions have no "sources" or "circulation" — if the function is smooth throughout the enclosed region, the integral detects nothing. But the moment f has an isolated **singularity** (a point where it is undefined or not differentiable) inside the contour, the integral need not vanish. The contour path never passes through the singularity, yet the integral "feels" it through the surrounding behavior of f.

The mechanism is the **residue**: a number associated with each isolated singularity that captures the leading singular behavior of f near that point. For a simple pole at z = z₀ (a singularity where f(z) ≈ c/(z − z₀) near z₀), the residue is lim(z→z₀) (z − z₀)f(z). To see this concretely: consider f(z) = 1/z and a unit circle γ centered at the origin. Parameterize as z = e^(iθ), dz = ie^(iθ) dθ, and compute ∮ (1/z) dz = ∫₀^(2π) (e^(−iθ)) · ie^(iθ) dθ = ∫₀^(2π) i dθ = 2πi. This equals 2πi times the residue of 1/z at z = 0, which is 1. The closed path has gone around the singularity once and picked up its full contribution.

The **residue theorem** generalizes this: ∮_γ f(z) dz = 2πi · Σ(residues of f at singularities inside γ), where each residue is weighted by the number of times γ winds around that singularity. This turns contour integration into a largely algebraic problem — locate the singularities inside the contour, compute each residue, sum them, multiply by 2πi. The theorem's real power emerges when you use cleverly chosen contours to evaluate definite real integrals like ∫₋∞^∞ 1/(1+x²) dx that are difficult or impossible to compute by elementary antiderivatives.
