---
id: residues-definition-computation
title: 'Residues: Definition and Computation'
domain: mathematics
course: complex-analysis
prerequisites:
- id: singularities-classification
  type: hard
- id: laurent-series
  type: soft
builds-toward:
- residue-theorem
- argument-principle
tags:
- residues
- laurent-coefficient
- computation
stage: advanced
status: draft
---

# Residues: Definition and Computation

## Core Idea
The residue of f at an isolated singularity z₀ is Res(f, z₀) = a₋₁, the coefficient of 1/(z - z₀) in the Laurent expansion. For a simple pole, Res(f, z₀) = lim_(z→z₀) (z - z₀)f(z). For a pole of order m, use Res(f, z₀) = (1/(m-1)!) d^(m-1)/dz^(m-1) [(z - z₀)^m f(z)] at z₀. Residues measure the strength of circulation around singularities.

## How It's Best Learned
Compute residues for f(z) = 1/(z(z-1)) at both z = 0 and z = 1 using the formulas. Verify by finding the Laurent series and extracting a₋₁.

## Common Misconceptions
Thinking residues are complicated to compute; there are simple formulas for simple and multiple poles. Assuming the residue formula applies to essential singularities; it doesn't — you must find the Laurent series.

## Explainer

From your study of singularities and Laurent series, you know that near an isolated singularity z₀, a function can be expanded as a Laurent series: f(z) = … + a₋₂/(z−z₀)² + a₋₁/(z−z₀) + a₀ + a₁(z−z₀) + … The **residue** of f at z₀ is defined as a₋₁, the coefficient of the 1/(z−z₀) term. At first this looks like just one number among many in the expansion — why does it deserve special attention?

The answer lies in integration. When you integrate a Laurent series term by term around a small circle enclosing z₀, almost every term integrates to zero: ∮ (z−z₀)ⁿ dz = 0 for n ≠ −1, because (z−z₀)ⁿ has an antiderivative. But the n = −1 term is different: ∮ 1/(z−z₀) dz = 2πi (this is the fundamental residue computation you verified when studying Laurent series). So ∮_γ f(z) dz = 2πi · a₋₁ = 2πi · Res(f, z₀). The residue is exactly the piece of the Laurent expansion that survives integration. Everything else cancels.

For computation, you rarely need to find the full Laurent series. If z₀ is a **simple pole** (order 1), the formula Res(f, z₀) = lim_{z→z₀} (z−z₀)f(z) extracts just a₋₁ by canceling the pole. For f(z) = 1/(z(z−1)), at z = 0: lim_{z→0} z · (1/(z(z−1))) = lim_{z→0} 1/(z−1) = −1. At z = 1: lim_{z→1} (z−1) · (1/(z(z−1))) = lim_{z→1} 1/z = 1. For a **pole of order m**, the formula involves differentiating m−1 times after multiplying by (z−z₀)^m to clear the pole, then evaluating at z₀ and dividing by (m−1)!. This is the repeated differentiation you know from power series manipulation.

For **essential singularities** — where infinitely many negative-power terms appear — none of these shortcuts apply. The Laurent series is truly infinite in the negative direction and cannot be cleared by multiplying by a finite power. You must find enough terms of the Laurent expansion to identify a₋₁ directly. The residue is still well-defined (it is still a₋₁), but the computation is harder. The key skill is recognizing which type of singularity you have before choosing your computational strategy.
