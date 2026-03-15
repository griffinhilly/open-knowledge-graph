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
