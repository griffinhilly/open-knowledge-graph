---
id: greens-theorem
title: Green's Theorem
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: greens-theorem
  type: hard
- id: line-integrals-vector-fields
  type: hard
- id: double-integrals-cartesian
  type: hard
builds-toward:
- stokes-theorem
- divergence-theorem
tags:
- greens-theorem
- circulation
stage: formal-systems
status: draft
---

# Green's Theorem

## Core Idea
Green's theorem: ∮_C (P dx + Q dy) = ∬_D (Q_x - P_y) dA. This relates line integrals around a closed curve to a double integral of curl over the region, converting circulation to an area integral.
