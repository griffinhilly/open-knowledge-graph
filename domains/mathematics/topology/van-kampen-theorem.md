---
id: van-kampen-theorem
title: van Kampen's Theorem
domain: mathematics
course: topology
prerequisites:
- id: fundamental-group-definition
  type: hard
- id: covering-spaces
  type: soft
builds-toward:
- classification-compact-surfaces
tags:
- van-kampen
- fundamental-group
- amalgamated-product
stage: advanced
status: draft
---

# van Kampen's Theorem

## Core Idea
van Kampen's theorem computes the fundamental group of a space glued from pieces: π₁(X) ≅ π₁(U) *_{π₁(U∩V)} π₁(V) when X = U ∪ V with overlapping U and V. This is the fundamental tool for computing fundamental groups of complex spaces from simpler pieces.
