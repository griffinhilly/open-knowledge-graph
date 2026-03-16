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
status: validated
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

## Explainer

If you are comfortable with polar coordinates, cylindrical coordinates require almost no new ideas. Recall that polar coordinates describe a point in the plane by its distance r from the origin and its angle θ from the positive x-axis: x = r cosθ, y = r sinθ. **Cylindrical coordinates** (r, θ, z) do exactly the same thing in the horizontal plane, then simply append a vertical z-coordinate to reach the third dimension. The conversion formulas are x = r cosθ, y = r sinθ, z = z — the z-coordinate is unchanged. The inverse conversion gives r² = x² + y² and tanθ = y/x, just as in polar.

The geometric picture is immediate: fix a value of r and vary θ and z, and you trace out a cylinder of radius r centered on the z-axis. Fix θ and vary r and z, and you get a half-plane containing the z-axis. Fix z and vary r and θ, and you get a horizontal disk. Shapes that have rotational symmetry around the z-axis — cylinders, cones, paraboloids, tori — are described by simple equations in cylindrical coordinates. The cylinder x² + y² = 4 becomes simply r = 2. The paraboloid z = x² + y² becomes z = r².

The critical quantity for integration is the **volume element**. In Cartesian coordinates, a tiny box has volume dx dy dz. In cylindrical coordinates, the corresponding tiny region is not a box but a curved wedge: it spans dr in the radial direction, r dθ in the arc direction (the arc length of a sector of radius r and angle dθ is r dθ), and dz vertically. So the volume element is **dV = r dr dθ dz**. The factor of r is the same Jacobian factor you computed for polar area elements; it appears because arc length grows with radius. Forgetting this factor is the most common error when setting up triple integrals in cylindrical coordinates.

The practical rule for when to use cylindrical coordinates: if the region of integration, or the integrand, simplifies when expressed in r, θ, and z, switch coordinate systems. The telltale sign is the expression x² + y² appearing in the integrand or the boundary — it collapses to r². If the integrand involves x² + y² + z² instead, spherical coordinates are better suited. The strength of cylindrical coordinates is capturing circular symmetry in the horizontal plane while leaving the vertical direction completely free.
