---
id: laurent-series
title: Laurent Series
domain: mathematics
course: complex-analysis
prerequisites:
- id: power-series-complex-plane
  type: hard
builds-toward:
- singularities-classification
- residues-definition-computation
tags:
- laurent-series
- principal-part
- singularities
stage: advanced
status: draft
---

# Laurent Series

## Core Idea
A Laurent series is Σ_(n=-∞)^∞ aₙ(z - z₀)^n. It converges on an annulus r < |z - z₀| < R. Any holomorphic function on an annulus has a unique Laurent expansion. The coefficient a₋₁ (the residue) plays a special role. The principal part Σ_(n=-∞)^(-1) aₙ(z - z₀)^n captures the behavior near the singularity at z₀.

## How It's Best Learned
Expand f(z) = 1/(z(z-1)) as a Laurent series around z = 0 in the annulus 0 < |z| < 1. Notice the negative powers appear and identify the residue (a₋₁).

## Common Misconceptions
Thinking Laurent series are like Taylor series but with negative powers; they describe behavior near singularities. Confusing the principal part with the regular part; they represent different aspects of the singularity.
