---
id: miller-indices
title: 'Miller Indices: Crystallographic Planes and Directions'
domain: engineering
course: materials-science
prerequisites:
- id: crystal-structure-basics
  type: hard
- id: vectors-in-3d
  type: soft
builds-toward:
- plastic-deformation-mechanisms
- x-ray-diffraction-materials
tags:
- miller-indices
- crystallography
- planes
- directions
stage: formal-systems
status: draft
---

# Miller Indices: Crystallographic Planes and Directions

## Core Idea
Miller indices provide a standardized notation for identifying planes and directions within a crystal lattice. A direction [uvw] is specified as the smallest integer vector components along the lattice axes, while a plane (hkl) is defined by the reciprocals of its intercepts with the unit cell axes, cleared to integers. Families of equivalent planes {hkl} and directions <uvw> are related by crystal symmetry. Miller indices are essential for understanding slip systems in plastic deformation and interpreting diffraction patterns.

## How It's Best Learned
Practice on a cubic unit cell by first indexing simple planes (cube faces, body diagonal), then generalizing. Sketch the planes corresponding to given indices and verify by checking axis intercepts.

## Common Misconceptions
- Negative indices are written with an overbar, not a minus sign, but computationally they work identically.
- The direction [111] and the plane (111) are perpendicular only in cubic systems — this does not hold for non-cubic lattices.
