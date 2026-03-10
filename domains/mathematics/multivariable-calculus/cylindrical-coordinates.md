---
id: cylindrical-coordinates
title: Cylindrical Coordinates
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: polar-coordinates
  type: hard
- id: vectors-in-3d
  type: soft
builds-toward:
- spherical-coordinates
- triple-integrals-cylindrical-spherical
tags:
- cylindrical-coordinates
- 3d
- polar
- coordinate-system
stage: formal-systems
status: draft
---

# Cylindrical Coordinates

## Core Idea
Cylindrical coordinates (r, θ, z) extend polar coordinates to ℝ³ by appending a vertical z-axis. The conversion is x = r cosθ, y = r sinθ, z = z, with r² = x² + y². Cylindrical coordinates are natural for solids with circular or cylindrical symmetry (cylinders, cones, paraboloids). The volume element in cylindrical coordinates is dV = r dr dθ dz, inheriting the factor of r from polar coordinates.

## How It's Best Learned
Students who understand polar coordinates can immediately grasp cylindrical: it is just polar in the xy-plane with an unchanged z-coordinate. Practice by describing simple surfaces (z = r, r = 2, z = r²) in cylindrical coordinates and sketching the corresponding 3D shapes. The volume element r dr dθ dz is the same derivation as for polar area.

## Common Misconceptions
- The volume element is r dr dθ dz, not dr dθ dz — the factor r is essential.
- r ≥ 0 by convention; negative r values require care if they arise.
- Cylindrical coordinates are most useful when the projection onto the xy-plane has circular symmetry; if the solid has spherical symmetry, use spherical coordinates instead.
