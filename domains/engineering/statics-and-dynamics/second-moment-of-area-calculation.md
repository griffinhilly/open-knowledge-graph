---
id: second-moment-of-area-calculation
title: Calculation of Second Moment of Area
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: area-moment-of-inertia-engineering
  type: hard
- id: parallel-axis-theorem-statics
  type: hard
builds-toward:
- moment-of-inertia-about-centroid
tags:
- moment-of-inertia
- second-moment
- integration
stage: formal-systems
status: draft
---

# Calculation of Second Moment of Area

## Core Idea
The second moment of area I is calculated by integration: I = ∫∫ r² dA, where r is the perpendicular distance from an axis. For composite sections, use the parallel-axis theorem: I = I_c + A d², where I_c is the moment about the centroid and d is the distance between axes. These properties are fundamental to beam bending analysis.
