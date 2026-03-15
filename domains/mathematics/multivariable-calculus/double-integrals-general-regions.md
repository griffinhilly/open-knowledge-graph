---
id: double-integrals-general-regions
title: Double Integrals over General Regions
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: double-integrals-cartesian-coordinates
  type: hard
builds-toward:
- applications-integrals-area-mass
tags:
- double-integrals
- integration-bounds
- general-regions
stage: formal-systems
status: draft
---

# Double Integrals over General Regions

## Core Idea
For a region D described as {(x, y) : a ≤ x ≤ b, g₁(x) ≤ y ≤ g₂(x)}, the double integral ∬_D f(x, y) dA = ∫_a^b ∫_{g₁(x)}^{g₂(x)} f(x, y) dy dx. Describing regions correctly (both as Type I and Type II) allows choosing the easier integration order.
