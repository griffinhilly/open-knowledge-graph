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
status: validated
---

# Change of Variables and the Jacobian Determinant

## Core Idea
For transformation (u, v) = T(x, y), the Jacobian J = ∂(x, y)/∂(u, v) = det([∂x/∂u, ∂x/∂v; ∂y/∂u, ∂y/∂v]) scales area. Thus ∬_D f(x, y) dA = ∬_S f(x(u, v), y(u, v)) |J| du dv. Cylindrical and spherical coordinates are special cases.

## Questions

```yaml
- question: "When converting ∬_D f(x,y) dA to polar coordinates, a factor of 'r' appears so that dA = r dr dθ. Where does this factor come from?"
  type: multiple-choice
  options:
    - "It is a correction factor for non-Cartesian coordinates that must be memorized for each system"
    - "It is the Jacobian determinant of the polar transformation, measuring how polar area elements stretch relative to Cartesian ones"
    - "It ensures the integrand f is evaluated at the correct radial distance"
    - "It converts arc length to area by accounting for the circular geometry of polar coordinates"
  answer: 1
  explanation: "The factor r is the absolute value of the Jacobian determinant computed from x = r cos θ, y = r sin θ. The Jacobian matrix has partial derivatives of (x, y) with respect to (r, θ), and its determinant equals r. This is not a special rule for polar coordinates — it is the general change-of-variables formula applied to this specific transformation. The same principle yields ρ² sin φ for spherical coordinates."

- question: "A student applies the substitution x = u², y = v to a double integral and writes ∬ f(u², v) du dv. What critical step was omitted?"
  type: multiple-choice
  options:
    - "The student forgot to express f entirely in terms of u and v"
    - "The student must multiply the integrand by the absolute value of the Jacobian determinant |∂(x,y)/∂(u,v)|"
    - "The student needs to verify that the transformation maps the region one-to-one before proceeding"
    - "The limits of integration must always be changed before substituting the new variables"
  answer: 1
  explanation: "The change-of-variables formula is ∬_D f(x,y) dA = ∬_S f(x(u,v), y(u,v)) |J| du dv. Without the Jacobian factor, the area elements du dv in (u,v)-space are not the same size as the corresponding dA in (x,y)-space. Here, ∂x/∂u = 2u, ∂x/∂v = 0, ∂y/∂u = 0, ∂y/∂v = 1, so J = 2u and |J| = 2u. The correct integral is ∬ f(u², v) · 2u du dv. Omitting 2u gives the wrong answer even though f is correctly transformed."

- question: "The Jacobian determinant of a coordinate transformation is typically positive, since it represents an area scaling factor."
  type: true-false
  answer: false
  explanation: "The Jacobian determinant can be negative, which indicates that the transformation reverses orientation (like a reflection). This is why the change-of-variables formula uses |J|, the absolute value — we want the magnitude of area scaling regardless of orientation. A negative Jacobian is not an error; it just means the transformation flips the orientation of the coordinate system."

- question: "The integration factors r (cylindrical) and ρ² sin φ (spherical) used in triple integrals can both be derived from the general change-of-variables formula by computing the Jacobian determinant of the respective coordinate transformations."
  type: true-false
  answer: true
  explanation: "This is exactly the point of the general theory. For cylindrical coordinates (x = r cos θ, y = r sin θ, z = z), computing the 3×3 Jacobian determinant gives r. For spherical coordinates (x = ρ sin φ cos θ, y = ρ sin φ sin θ, z = ρ cos φ), the determinant gives ρ² sin φ. These familiar factors are not separate rules to memorize — they are consequences of the same general theorem applied to two common transformations."

- question: "Why must you multiply by |J| (the absolute value of the Jacobian determinant) when changing variables in a double integral, rather than simply substituting the new variable expressions into f?"
  type: short-answer
  answer: "Because the area element dA in the original coordinates does not equal du dv in the new coordinates. The Jacobian measures how much a small rectangle of area du dv in (u,v)-space stretches or compresses when mapped to (x,y)-space. Locally, the transformation looks linear, and a small rectangle gets mapped to a parallelogram whose area is |J| du dv. Without this factor, you correctly transform the integrand values but integrate over incorrectly sized area elements, producing the wrong total."
  explanation: "The core idea is that area is not preserved by coordinate transformations in general. A change of variables changes both what you are integrating (the function values, expressed in new coordinates) and how you measure area (the size of each infinitesimal patch). The Jacobian accounts for the second change. Omitting it is analogous to measuring a room in feet but reporting the area as if you had used meters."
```

## Explainer

From your work with cylindrical and spherical coordinates, you have already used the change-of-variables idea in specific cases: in polar coordinates, dA becomes r dr dθ, and in spherical coordinates, dV becomes ρ² sin φ dρ dφ dθ. The extra factors r and ρ² sin φ are not magic — they measure how much area or volume is stretched or compressed by the coordinate transformation. The **Jacobian determinant** is the general tool that computes this stretching factor for any smooth change of coordinates.

Think about what a coordinate transformation does locally. Near any point, a smooth map T(u, v) = (x(u, v), y(u, v)) looks approximately linear. A small rectangle of area du dv in (u, v)-space gets mapped to a small parallelogram in (x, y)-space. The area of that parallelogram is |J| du dv, where J is the determinant of the 2×2 matrix of partial derivatives: J = (∂x/∂u)(∂y/∂v) - (∂x/∂v)(∂y/∂u). This matrix — the **Jacobian matrix** of the transformation — encodes the local linear approximation, and its determinant encodes the signed area scaling factor. Taking the absolute value |J| gives the unsigned area ratio, which is what you need to correctly account for how area changes under the map.

The change-of-variables formula is then: ∬_D f(x, y) dA = ∬_S f(x(u,v), y(u,v)) |J(u,v)| du dv, where D is the region in (x, y)-space, S is the corresponding region in (u, v)-space, and f is expressed in the new coordinates. You choose the transformation to simplify either the region S or the integrand — ideally both. For polar coordinates, x = r cos θ, y = r sin θ, and computing the Jacobian gives J = r, recovering the familiar factor. The formula is not a separate rule for polar coordinates; polar coordinates are simply one instance of the general theorem.

In three dimensions, the Jacobian becomes a 3×3 determinant and |J| du dv dw replaces dA. For cylindrical coordinates (x = r cos θ, y = r sin θ, z = z), J = r. For spherical (x = ρ sin φ cos θ, y = ρ sin φ sin θ, z = ρ cos φ), J = ρ² sin φ. Both results you used in your work with triple integrals are now derivable from first principles rather than accepted as formulas. The deeper principle: whenever a region or integrand is naturally described in some non-Cartesian coordinate system, compute the Jacobian of the transformation and substitute — the geometry will simplify, even if the algebra of computing J takes some effort.
