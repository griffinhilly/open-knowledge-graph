---
id: parallel-axis-theorem-statics
title: Parallel Axis Theorem for Area Moments
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: area-moment-of-inertia-engineering
  type: hard
tags:
- statics
- parallel axis theorem
- moment of inertia
- composite sections
stage: formal-systems
status: draft
---

# Parallel Axis Theorem for Area Moments

## Core Idea
The parallel axis theorem states that the area moment of inertia about any axis equals the centroidal moment of inertia about a parallel centroidal axis plus the product of area and the square of the distance between the axes: I = Ī + A·d². This theorem enables calculation of moments of inertia for composite cross-sections (I-beams, T-sections, channels) built from standard shapes by combining each part's centroidal moment with its transfer term A·d².

## How It's Best Learned
For composite sections, build a table listing each part's Ī, area A, distance d from the part's centroid to the overall reference axis, and Ad². Sum I = ΣĪᵢ + ΣAᵢdᵢ² to find the total moment of inertia.

## Common Misconceptions
- Measuring d from the reference axis to the reference axis of the part rather than to the part's centroid.
- Double-applying the theorem (Ī is already the centroidal moment; only one Ad² transfer is needed per part).
- Forgetting that Ī must be about a centroidal axis parallel to the reference axis.
