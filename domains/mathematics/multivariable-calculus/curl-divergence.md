---
id: curl-divergence
title: Curl and Divergence
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: curl-and-divergence
  type: hard
- id: partial-derivatives-basics
  type: hard
builds-toward:
- greens-theorem
- stokes-theorem
- divergence-theorem
tags:
- curl
- divergence
stage: formal-systems
status: draft
---

# Curl and Divergence

## Core Idea
For F = (P, Q, R), curl is ∇×F = (R_y - Q_z, P_z - R_x, Q_x - P_y) (rotation), and divergence is ∇·F = P_x + Q_y + R_z (outflow). Conservative fields have curl = 0.
