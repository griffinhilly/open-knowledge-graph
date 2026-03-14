---
id: greens-theorem
title: 'Green''s Theorem'
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: line-integrals-vector-fields
  type: hard
- id: double-integrals-cartesian
  type: hard
- id: conservative-fields
  type: soft
- id: fundamental-theorem-line-integrals
  type: soft
builds-toward:
- stokes-theorem
- divergence-theorem
- curl-and-divergence
tags:
- Greens-theorem
- circulation
- flux
- boundary
- orientation
stage: formal-systems
status: validated
---
# Green's Theorem

## Core Idea
Green's theorem relates a line integral around a positively oriented closed curve C (boundary of region D) to a double integral over D: ∮_C P dx + Q dy = ∬_D (∂Q/∂x − ∂P/∂y) dA. The integrand ∂Q/∂x − ∂P/∂y is the 2D curl (or scalar curl) of F = ⟨P, Q⟩, measuring the local rotational tendency of the field. Green's theorem is the 2D special case of both Stokes' theorem and the divergence theorem, connecting boundary behavior to interior properties.

## How It's Best Learned
Present Green's theorem as a 'boundary-to-interior' exchange: instead of integrating around the boundary, integrate a related quantity over the enclosed area, or vice versa. Applications to computing area (using ∮ x dy or −∮ y dx) demonstrate immediate utility. Emphasize the counterclockwise (positive) orientation convention.

## Common Misconceptions
- The curve C must be positively oriented (counterclockwise); reversing orientation negates the integral.
- Green's theorem requires a simple closed curve bounding a region — it does not apply to open curves.
- For a region with holes, the boundary consists of multiple curves (outer boundary counterclockwise, inner boundaries clockwise).
- Green's theorem does not apply to conservative fields in the sense that both sides equal zero in that case.
