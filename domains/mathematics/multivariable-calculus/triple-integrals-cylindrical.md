---
id: triple-integrals-cylindrical
title: Triple Integrals in Cylindrical Coordinates
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: cylindrical-coordinates
  type: hard
- id: triple-integrals
  type: hard
builds-toward:
- applications-multivariable
tags:
- cylindrical
- triple-integral
stage: formal-systems
status: draft
---

# Triple Integrals in Cylindrical Coordinates

## Core Idea
In cylindrical coordinates (r, θ, z), the volume element is dV = r dr dθ dz. Cylindrical is ideal for regions with circular symmetry around the z-axis.

## Explainer

You already know cylindrical coordinates (r, θ, z) as a way to describe points in 3D space: r is the distance from the z-axis, θ is the angle around the z-axis, and z is the height — essentially polar coordinates in the xy-plane with z added unchanged. You also know how to set up and evaluate triple integrals in Cartesian coordinates, with dV = dx dy dz. The question now is: how does the volume element change when you switch to cylindrical coordinates?

The crucial fact is that dV = r dr dθ dz, not dr dθ dz. The extra factor of r is not optional — it comes from the **Jacobian** of the coordinate transformation. In polar/cylindrical coordinates, a small "box" defined by increments dr, dθ, dz is not a rectangular box. A change in θ by dθ sweeps an arc whose actual length is r dθ, not dθ. The arc length grows with radius because a larger circle has more circumference per radian. So the infinitesimal volume element — the "width" times the "depth" times the "height" — is (dr)(r dθ)(dz) = r dr dθ dz. If you forget the r, you systematically undercount volume, with the error growing for regions far from the z-axis.

To set up a triple integral in cylindrical coordinates, you describe the region of integration using inequalities on r, θ, and z. For a cylinder of radius R and height H centered on the z-axis, the bounds are 0 ≤ r ≤ R, 0 ≤ θ ≤ 2π, 0 ≤ z ≤ H. The integral ∫∫∫ f(x, y, z) dV becomes ∫₀ᴴ ∫₀²π ∫₀ᴿ f(r cos θ, r sin θ, z) · r dr dθ dz. The integrand is rewritten using x = r cos θ and y = r sin θ. Critically, r ≥ 0 always, so the r in front of the Jacobian does not introduce sign issues.

The power of cylindrical coordinates is that they make circular and cylindrical boundaries natural — a circle becomes r = constant instead of x² + y² = R², which produces impossible square roots in Cartesian setups. Regions bounded by cones (z = r, since r = √(x² + y²)), paraboloids (z = r²), or spheres of revolution also simplify dramatically. The decision rule is straightforward: whenever the region or integrand has rotational symmetry around the z-axis (or can be rotated so it does), cylindrical coordinates will simplify the computation. If the symmetry is spherical — around a point — spherical coordinates are the next tool in your kit.
