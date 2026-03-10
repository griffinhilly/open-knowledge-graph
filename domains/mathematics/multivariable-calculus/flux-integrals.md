---
id: flux-integrals
title: Flux Integrals
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: surface-integrals-scalar
  type: hard
- id: vector-fields
  type: hard
- id: dot-product
  type: hard
builds-toward:
- stokes-theorem
- divergence-theorem
tags:
- flux
- surface-integral
- vector-field
- normal
- orientation
stage: formal-systems
status: draft
---

# Flux Integrals

## Core Idea
The flux integral ∬_S F · dS = ∬_S F · n dS measures the net flow of a vector field F through an oriented surface S, where n is the unit outward normal. It equals ∬_D F(r(u,v)) · (r_u × r_v) dA, where the cross product gives the oriented normal (outward or inward depending on parametrization order). Flux is fundamental in physics: it measures how much fluid passes through a surface per unit time, or the total electric field emanating from a charge distribution.

## How It's Best Learned
The physical motivation of fluid flux (liters per second through a membrane) is the clearest entry point. The distinction between scalar surface integrals (f dS) and flux integrals (F · dS) parallels the distinction between scalar and vector line integrals. Emphasize orientation: the sign of ∬ F · dS depends on whether the normal is chosen to be inward or outward.

## Common Misconceptions
- Flux integrals are orientation-dependent; reversing the normal direction negates the flux.
- F · (r_u × r_v) is a scalar (the dot product of two vectors in ℝ³), not a vector — students sometimes confuse the dimensions.
- The outward normal for a closed surface points away from the enclosed volume; this convention is standard in the divergence theorem.
