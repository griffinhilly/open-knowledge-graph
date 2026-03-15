---
id: residue-theorem
title: The Residue Theorem
domain: mathematics
course: complex-analysis
prerequisites:
- id: residues-definition-computation
  type: hard
- id: contour-integration
  type: soft
builds-toward:
- evaluating-integrals-residues
- argument-principle
tags:
- residue-theorem
- contour-integrals
- applications
stage: advanced
status: draft
---

# The Residue Theorem

## Core Idea
If f is holomorphic inside and on a closed contour γ except for finitely many isolated singularities z₁, ..., zₙ inside γ, then ∮_γ f(z) dz = 2πi Σ Res(f, zₖ). This theorem reduces a contour integral to a sum of residues, making it a powerful tool for evaluating real integrals and summing series.

## How It's Best Learned
Apply this to compute ∮_γ dz/(z²+1) around a circle of radius 2. Identify the poles, compute their residues, and verify the result matches a direct contour integral.

## Common Misconceptions
Forgetting the factor 2πi; it comes from the integral formula for a simple pole. Assuming the theorem works for multiply-connected domains without accounting for all enclosed singularities.
