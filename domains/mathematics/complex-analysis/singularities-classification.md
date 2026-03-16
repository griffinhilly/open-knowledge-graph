---
id: singularities-classification
title: Classification of Isolated Singularities
domain: mathematics
course: complex-analysis
prerequisites:
- id: laurent-series
  type: hard
builds-toward:
- residues-definition-computation
- argument-principle
tags:
- singularities
- poles
- essential-singularities
stage: advanced
status: draft
---

# Classification of Isolated Singularities

## Core Idea
An isolated singularity of f at z₀ is classified by its Laurent expansion: a removable singularity has no negative powers (f extends analytically); a pole of order m has principal part with m terms (f ~ a₋ₘ/(z - z₀)^m near z₀); an essential singularity has infinitely many negative powers (f is wildly oscillating near z₀).

## Explainer

From your study of Laurent series, you know that a complex function near an isolated singularity z₀ can be expanded in both positive and negative powers of (z − z₀): f(z) = ... + a₋₂/(z − z₀)² + a₋₁/(z − z₀) + a₀ + a₁(z − z₀) + ... The **negative-power part** (called the **principal part**) is what determines the type of singularity. There are exactly three cases, and they describe increasingly wild behavior.

**Removable singularities** have no principal part — all coefficients aₙ with n < 0 are zero. The Laurent expansion is just a regular power series a₀ + a₁(z − z₀) + ..., so by defining (or redefining) f(z₀) = a₀, the function extends analytically through z₀. The singularity was only apparent — a hole that can be plugged. The canonical example is sin(z)/z at z = 0: expanding sin(z)/z = 1 − z²/6 + z⁴/120 − ..., there are no negative powers, so the singularity is removable by setting f(0) = 1. The function approaches a finite, well-defined limit as z → z₀.

**Poles** have a finite principal part: a₋ₘ/(z − z₀)^m + ... + a₋₁/(z − z₀) with a₋ₘ ≠ 0. Near a pole of order m, the function blows up like |f(z)| ~ |a₋ₘ|/|z − z₀|^m → ∞ as z → z₀. A first-order pole (m = 1) is a **simple pole** — the most common type, and the most important for the Residue Theorem. The coefficient a₋₁ of the simple pole term is the **residue**, which drives complex contour integrals. You can detect a pole of order m by checking that (z − z₀)^m · f(z) has a nonzero, finite limit as z → z₀.

**Essential singularities** have infinitely many negative powers — the principal part is an infinite series. The behavior near an essential singularity is famously chaotic. The **Casorati-Weierstrass theorem** says f comes arbitrarily close to every complex value in any neighborhood of the singularity; the stronger **Picard Great Theorem** says f actually takes every complex value, with at most one exception, infinitely often. The canonical example is e^(1/z) near z = 0: e^(1/z) = 1 + 1/z + 1/(2z²) + ... — infinitely many negative powers. As z → 0 along different paths, e^(1/z) spirals, explodes, and vanishes in completely different ways. Classifying which type of singularity you have is the essential first step in computing residues and applying the Residue Theorem.
