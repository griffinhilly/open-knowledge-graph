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

## Questions

```yaml
- question: "A student sets up the volume integral for the solid cylinder r ≤ 2, 0 ≤ z ≤ 3 in cylindrical coordinates and writes ∫∫∫ dr dθ dz over the appropriate limits. What error did they make?"
  type: multiple-choice
  options:
    - "They should use spherical coordinates for cylindrical solids, not cylindrical coordinates"
    - "The z-limits should be centered at zero, from −3/2 to 3/2"
    - "They omitted the factor of r — the volume element is r dr dθ dz, not dr dθ dz"
    - "The order of integration must always be dz dr dθ in cylindrical coordinates"
  answer: 2
  explanation: "The factor of r is mandatory in the cylindrical volume element. A thin wedge at radius r with angular opening dθ has arc length r dθ in the tangential direction — not just dθ. Without r, you treat all wedges as having the same arc width regardless of radius, which overcounts near the origin and undercounts far from it. The error produces a volume that is systematically wrong. This is the same Jacobian factor that appears in polar area elements: dA = r dr dθ."

- question: "Which of the following integrals would be MOST efficiently simplified by switching to cylindrical coordinates?"
  type: multiple-choice
  options:
    - "∫∫∫ (x² + y² + z²) dV over a sphere — use spherical coordinates instead"
    - "∫∫∫ e^(x² + y²) dV over the region x² + y² ≤ 4, 0 ≤ z ≤ 1"
    - "∫∫∫ xyz dV over the rectangular box [0,1] × [0,1] × [0,1]"
    - "∫∫∫ z² dV over the unit sphere — use spherical coordinates instead"
  answer: 1
  explanation: "The integrand e^(x² + y²) contains x² + y², which collapses to r² in cylindrical coordinates: the integral becomes ∫∫∫ e^(r²) r dr dθ dz, which is separable. The circular region of integration x² + y² ≤ 4 becomes r ≤ 2, a natural cylindrical boundary. When the integrand or boundary involves x² + y², that is the telltale sign to use cylindrical. When it involves x² + y² + z², use spherical instead."

- question: "Cylindrical coordinates introduce fundamentally new mathematics compared to polar coordinates — they require learning separate conversion formulas and a different integration framework."
  type: true-false
  answer: false
  explanation: "Cylindrical coordinates extend polar coordinates to three dimensions by simply appending an unchanged z-coordinate. The conversion formulas x = r cosθ, y = r sinθ, z = z are exactly the polar formulas with z added. The volume element r dr dθ dz comes directly from the polar area element r dr dθ with dz appended. Students who understand polar coordinates can grasp cylindrical coordinates immediately — there are no genuinely new ideas, only a straightforward extension."

- question: "In the cylindrical volume element r dr dθ dz, the factor r appears because arc length in the angular direction equals r times the angular increment dθ."
  type: true-false
  answer: true
  explanation: "This is the geometric origin of the Jacobian factor. A thin wedge at radius r spanning an angular increment dθ has arc length r dθ at that radius — the further from the axis, the wider the wedge becomes in absolute terms. The volume of the wedge element is (radial extent dr) × (arc extent r dθ) × (vertical extent dz) = r dr dθ dz. The same reasoning gives the polar area element r dr dθ. The r factor is not optional; it reflects real geometry."

- question: "Why does the volume element in cylindrical coordinates include a factor of r, and what goes wrong in a volume calculation if you omit it?"
  type: short-answer
  answer: "The r factor arises because the angular coordinate θ does not directly measure length — arc length in the θ direction at radius r is r dθ, not dθ. So a tiny volume wedge has dimensions dr (radial) × r dθ (arc) × dz (vertical) = r dr dθ dz. Without the r factor, all wedges at different radii are treated as having the same physical width, which is false: wedges near the origin are narrow, and those far away are wide. Omitting r overcounts volume near the axis and undercounts it far from the axis, producing an incorrect result."
  explanation: "This is the single most important fact about integration in cylindrical coordinates. The Jacobian factor r is what connects the coordinate increment dθ to actual physical arc length — it is not an algebraic technicality but a geometric necessity. The same principle explains why polar area integrals use r dr dθ."
```

## Explainer

If you are comfortable with polar coordinates, cylindrical coordinates require almost no new ideas. Recall that polar coordinates describe a point in the plane by its distance r from the origin and its angle θ from the positive x-axis: x = r cosθ, y = r sinθ. **Cylindrical coordinates** (r, θ, z) do exactly the same thing in the horizontal plane, then simply append a vertical z-coordinate to reach the third dimension. The conversion formulas are x = r cosθ, y = r sinθ, z = z — the z-coordinate is unchanged. The inverse conversion gives r² = x² + y² and tanθ = y/x, just as in polar.

The geometric picture is immediate: fix a value of r and vary θ and z, and you trace out a cylinder of radius r centered on the z-axis. Fix θ and vary r and z, and you get a half-plane containing the z-axis. Fix z and vary r and θ, and you get a horizontal disk. Shapes that have rotational symmetry around the z-axis — cylinders, cones, paraboloids, tori — are described by simple equations in cylindrical coordinates. The cylinder x² + y² = 4 becomes simply r = 2. The paraboloid z = x² + y² becomes z = r².

The critical quantity for integration is the **volume element**. In Cartesian coordinates, a tiny box has volume dx dy dz. In cylindrical coordinates, the corresponding tiny region is not a box but a curved wedge: it spans dr in the radial direction, r dθ in the arc direction (the arc length of a sector of radius r and angle dθ is r dθ), and dz vertically. So the volume element is **dV = r dr dθ dz**. The factor of r is the same Jacobian factor you computed for polar area elements; it appears because arc length grows with radius. Forgetting this factor is the most common error when setting up triple integrals in cylindrical coordinates.

The practical rule for when to use cylindrical coordinates: if the region of integration, or the integrand, simplifies when expressed in r, θ, and z, switch coordinate systems. The telltale sign is the expression x² + y² appearing in the integrand or the boundary — it collapses to r². If the integrand involves x² + y² + z² instead, spherical coordinates are better suited. The strength of cylindrical coordinates is capturing circular symmetry in the horizontal plane while leaving the vertical direction completely free.
