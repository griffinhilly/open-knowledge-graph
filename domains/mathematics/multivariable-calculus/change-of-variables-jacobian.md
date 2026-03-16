---
id: change-of-variables-jacobian
title: Change of Variables and the Jacobian Determinant
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: triple-integrals-cylindrical-spherical
  type: hard
builds-toward:
- surface-parametrization
tags:
- jacobian
- change-of-variables
- transformation
stage: formal-systems
status: draft
---

# Change of Variables and the Jacobian Determinant

## Core Idea
For transformation (u, v) = T(x, y), the Jacobian J = ∂(x, y)/∂(u, v) = det([∂x/∂u, ∂x/∂v; ∂y/∂u, ∂y/∂v]) scales area. Thus ∬_D f(x, y) dA = ∬_S f(x(u, v), y(u, v)) |J| du dv. Cylindrical and spherical coordinates are special cases.

## Explainer

From your work with cylindrical and spherical coordinates, you have already used the change-of-variables idea in specific cases: in polar coordinates, dA becomes r dr dθ, and in spherical coordinates, dV becomes ρ² sin φ dρ dφ dθ. The extra factors r and ρ² sin φ are not magic — they measure how much area or volume is stretched or compressed by the coordinate transformation. The **Jacobian determinant** is the general tool that computes this stretching factor for any smooth change of coordinates.

Think about what a coordinate transformation does locally. Near any point, a smooth map T(u, v) = (x(u, v), y(u, v)) looks approximately linear. A small rectangle of area du dv in (u, v)-space gets mapped to a small parallelogram in (x, y)-space. The area of that parallelogram is |J| du dv, where J is the determinant of the 2×2 matrix of partial derivatives: J = (∂x/∂u)(∂y/∂v) - (∂x/∂v)(∂y/∂u). This matrix — the **Jacobian matrix** of the transformation — encodes the local linear approximation, and its determinant encodes the signed area scaling factor. Taking the absolute value |J| gives the unsigned area ratio, which is what you need to correctly account for how area changes under the map.

The change-of-variables formula is then: ∬_D f(x, y) dA = ∬_S f(x(u,v), y(u,v)) |J(u,v)| du dv, where D is the region in (x, y)-space, S is the corresponding region in (u, v)-space, and f is expressed in the new coordinates. You choose the transformation to simplify either the region S or the integrand — ideally both. For polar coordinates, x = r cos θ, y = r sin θ, and computing the Jacobian gives J = r, recovering the familiar factor. The formula is not a separate rule for polar coordinates; polar coordinates are simply one instance of the general theorem.

In three dimensions, the Jacobian becomes a 3×3 determinant and |J| du dv dw replaces dA. For cylindrical coordinates (x = r cos θ, y = r sin θ, z = z), J = r. For spherical (x = ρ sin φ cos θ, y = ρ sin φ sin θ, z = ρ cos φ), J = ρ² sin φ. Both results you used in your work with triple integrals are now derivable from first principles rather than accepted as formulas. The deeper principle: whenever a region or integrand is naturally described in some non-Cartesian coordinate system, compute the Jacobian of the transformation and substitute — the geometry will simplify, even if the algebra of computing J takes some effort.
