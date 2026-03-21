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

## Questions

```yaml
- question: "A student computes ∫₀²π ∫₀ᴿ ∫₀ᴴ f(r,θ,z) dz dr dθ to find the mass of a cylinder. What critical error have they made?"
  type: multiple-choice
  options:
    - "The order of integration is wrong — z must be the outermost integral"
    - "The bounds on θ should go from 0 to π, not 0 to 2π"
    - "The volume element is missing the factor r — the correct element is r dz dr dθ, giving an extra factor that grows with radius"
    - "f must be expressed in Cartesian coordinates before integration"
  answer: 2
  explanation: "The volume element in cylindrical coordinates is dV = r dr dθ dz (in any order of integration). The student wrote dz dr dθ, omitting the essential factor of r. This factor arises from the Jacobian of the coordinate transformation: a change of angle dθ sweeps an arc of length r dθ, not dθ, so the infinitesimal 'width' of the volume element in the θ-direction is r dθ. Omitting r systematically undercounts volume, with the error proportional to how far from the z-axis the integration occurs. The order of integration (option A) can be rearranged without affecting correctness, and option B gives the wrong angular range for a full cylinder."

- question: "Which of the following regions is BEST suited for cylindrical coordinates rather than Cartesian?"
  type: multiple-choice
  options:
    - "A rectangular box 0 ≤ x ≤ 2, 0 ≤ y ≤ 3, 0 ≤ z ≤ 5"
    - "The region inside the sphere x² + y² + z² = 4 and above the plane z = 1"
    - "The solid bounded below by z = 0, above by z = 4 − r², and inside the cylinder x² + y² = 1"
    - "The tetrahedron with vertices at (0,0,0), (1,0,0), (0,1,0), (0,0,1)"
  answer: 2
  explanation: "Cylindrical coordinates excel when the region has rotational symmetry around the z-axis, which converts curved Cartesian boundaries into simple inequalities on r and z. The region bounded by z = 4 − r² (a paraboloid in cylindrical form) and the cylinder x² + y² = 1 (which becomes simply r = 1) is naturally described as 0 ≤ r ≤ 1, 0 ≤ θ ≤ 2π, 0 ≤ z ≤ 4 − r². In Cartesian, the paraboloid z = 4 − x² − y² would require dealing with a circular cross-section producing square roots. Options A and D are natural for Cartesian. Option B has spherical symmetry, making spherical coordinates the better choice."

- question: "The extra factor of r in the cylindrical volume element dV = r dr dθ dz arises because a small change in angle dθ sweeps an arc of physical length r dθ, not dθ."
  type: true-false
  answer: true
  explanation: "This is the geometric heart of the result. In polar/cylindrical coordinates, equal angular increments dθ correspond to arcs of different physical lengths depending on radius: the arc length is r dθ. A small 'box' in cylindrical coordinates has dimensions dr in the radial direction, r dθ in the angular direction, and dz vertically, giving volume dr × r dθ × dz = r dr dθ dz. The Jacobian of the transformation formalizes this: |∂(x,y,z)/∂(r,θ,z)| = r. Farther from the z-axis, the same angular increment sweeps more physical space, which is why r appears as a multiplicative factor."

- question: "The volume element in cylindrical coordinates is dr dθ dz, because θ is dimensionless (measured in radians) and contributes no length factor."
  type: true-false
  answer: false
  explanation: "This is the most common error when switching to cylindrical coordinates. Radians are indeed dimensionless, but that is beside the point: a radian is a ratio of arc length to radius, so an arc of angle dθ has physical length r dθ. Dimensionlessness of the angle does not mean the arc it sweeps has zero extent. The correct volume element is dV = r dr dθ dz, with r as the Jacobian factor. Forgetting r produces integrals that systematically undercount volume, with the error largest for regions at large r."

- question: "Why does the volume element in cylindrical coordinates include a factor of r, and what goes wrong computationally if you forget it?"
  type: short-answer
  answer: "The factor r is the Jacobian of the transformation from Cartesian (x,y,z) to cylindrical (r,θ,z). It accounts for the fact that equal increments of angle θ sweep different amounts of physical space depending on the radius: the arc length is r dθ. An infinitesimal cylindrical 'box' has radial width dr, circumferential width r dθ, and height dz, giving volume r dr dθ dz. If you omit r and use dr dθ dz, you are treating angular increments as having unit width everywhere — undercounting volume in proportion to how far from the axis the region lies. For a symmetric region like a cylinder, the error factor is exactly ∫₀ᴿ r dr / ∫₀ᴿ dr = R/2, so you undercount by half the radius on average."
  explanation: "The Jacobian is the formal machinery behind this: changing variables in a multiple integral requires multiplying by |det(J)| where J is the matrix of partial derivatives of the new coordinates with respect to the old. For cylindrical coordinates, |det(J)| = r. The practical diagnostic: if your answer for the volume of a cylinder of radius R and height H is πR²H but your integral gives RH (missing the R factor), you forgot the r in dV."
```

## Explainer

You already know cylindrical coordinates (r, θ, z) as a way to describe points in 3D space: r is the distance from the z-axis, θ is the angle around the z-axis, and z is the height — essentially polar coordinates in the xy-plane with z added unchanged. You also know how to set up and evaluate triple integrals in Cartesian coordinates, with dV = dx dy dz. The question now is: how does the volume element change when you switch to cylindrical coordinates?

The crucial fact is that dV = r dr dθ dz, not dr dθ dz. The extra factor of r is not optional — it comes from the **Jacobian** of the coordinate transformation. In polar/cylindrical coordinates, a small "box" defined by increments dr, dθ, dz is not a rectangular box. A change in θ by dθ sweeps an arc whose actual length is r dθ, not dθ. The arc length grows with radius because a larger circle has more circumference per radian. So the infinitesimal volume element — the "width" times the "depth" times the "height" — is (dr)(r dθ)(dz) = r dr dθ dz. If you forget the r, you systematically undercount volume, with the error growing for regions far from the z-axis.

To set up a triple integral in cylindrical coordinates, you describe the region of integration using inequalities on r, θ, and z. For a cylinder of radius R and height H centered on the z-axis, the bounds are 0 ≤ r ≤ R, 0 ≤ θ ≤ 2π, 0 ≤ z ≤ H. The integral ∫∫∫ f(x, y, z) dV becomes ∫₀ᴴ ∫₀²π ∫₀ᴿ f(r cos θ, r sin θ, z) · r dr dθ dz. The integrand is rewritten using x = r cos θ and y = r sin θ. Critically, r ≥ 0 always, so the r in front of the Jacobian does not introduce sign issues.

The power of cylindrical coordinates is that they make circular and cylindrical boundaries natural — a circle becomes r = constant instead of x² + y² = R², which produces impossible square roots in Cartesian setups. Regions bounded by cones (z = r, since r = √(x² + y²)), paraboloids (z = r²), or spheres of revolution also simplify dramatically. The decision rule is straightforward: whenever the region or integrand has rotational symmetry around the z-axis (or can be rotated so it does), cylindrical coordinates will simplify the computation. If the symmetry is spherical — around a point — spherical coordinates are the next tool in your kit.
