---
id: moment-of-inertia-about-centroid
title: Moment of Inertia about Centroidal Axes
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: second-moment-of-area-calculation
  type: hard
- id: centroid-areas-composite
  type: hard
builds-toward:
- principal-axes-and-rotation
- shear-force-bending-moment-diagrams
tags:
- centroidal-axes
- parallel-axis-theorem
- composite
stage: formal-systems
status: draft
---

# Moment of Inertia about Centroidal Axes

## Core Idea
The moment of inertia about centroidal axes is minimal and is used as a reference point. Using the parallel-axis theorem, the moment of inertia about any parallel axis is I = I_c + A d². For composite sections, calculate the centroid first, then sum the individual moments of inertia (corrected for distance) to find the total.
