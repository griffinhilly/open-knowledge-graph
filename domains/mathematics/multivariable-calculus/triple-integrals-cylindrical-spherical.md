---
id: triple-integrals-cylindrical-spherical
title: Triple Integrals in Cylindrical and Spherical Coordinates
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: triple-integrals-cartesian
  type: hard
- id: cylindrical-coordinates
  type: soft
builds-toward:
- change-of-variables-jacobian
tags:
- cylindrical-coordinates
- spherical-coordinates
- triple-integrals
stage: formal-systems
status: validated
---

# Triple Integrals in Cylindrical and Spherical Coordinates

## Core Idea
Cylindrical coordinates (r, θ, z) have dV = r dr dθ dz. Spherical coordinates (ρ, φ, θ) have dV = ρ² sin φ dρ dφ dθ. Choose coordinates based on the region's symmetry: cylindrical for objects with axis symmetry, spherical for radial symmetry from a point.

## Questions

```yaml
- question: "You want to compute the volume of a solid ball of radius 3 centered at the origin. Which setup is correct in spherical coordinates?"
  type: multiple-choice
  options:
    - "∫₀²π ∫₀π ∫₀³ dρ dφ dθ"
    - "∫₀²π ∫₀π ∫₀³ ρ² sin φ dρ dφ dθ"
    - "∫₀²π ∫₀π ∫₀³ ρ sin φ dρ dφ dθ"
    - "∫₀²π ∫₀π ∫₀³ ρ² dρ dφ dθ"
  answer: 1
  explanation: "The spherical volume element is dV = ρ² sin φ dρ dφ dθ — both factors are required. The ρ² factor accounts for the shell's growing surface area with radius, and sin φ accounts for the shrinking arc length near the poles (where sin φ → 0). Option A omits both Jacobian factors entirely. Option C uses ρ instead of ρ². Option D forgets the sin φ. Forgetting either factor is the most common error in spherical integrals."

- question: "A region is bounded by the cylinder r = 2 (in cylindrical coordinates) and the planes z = 0 and z = 5. A student sets up the triple integral as ∫₀²π ∫₀² ∫₀⁵ dr dz dθ, claiming the extra factor is unnecessary because the region is already described in cylindrical coordinates. What is wrong?"
  type: multiple-choice
  options:
    - "Nothing — once you switch to cylindrical coordinates, no Jacobian factor is needed"
    - "The limits are wrong; r should go from 0 to 4"
    - "The volume element must be r dr dz dθ, not just dr dz dθ — the factor r is always required"
    - "The order of integration must be dz dr dθ for cylindrical coordinates"
  answer: 2
  explanation: "The factor r in dV = r dr dθ dz is not optional — it is the Jacobian of the cylindrical coordinate transformation. A thin wedge at radius r has arc length r dθ along the θ direction, not dθ, so small volume elements at larger r are physically larger. Without the r factor, the integral underestimates the volume for regions away from the axis. The order of integration can be freely rearranged (option D is wrong), and the limits are correct as given."

- question: "The factor r appearing in the cylindrical volume element dV = r dr dθ dz is the same factor that appears in the polar area element dA = r dr dθ."
  type: true-false
  answer: true
  explanation: "This is exactly right. Cylindrical coordinates are polar coordinates in the xy-plane with a z-axis attached. The factor r arises in both cases for the same geometric reason: a small arc at radius r in the θ direction has length r dθ, not just dθ. The z integration adds a simple dz factor with no Jacobian contribution because z is a Cartesian coordinate."

- question: "Spherical coordinates are the best choice for computing any triple integral over a three-dimensional region."
  type: true-false
  answer: false
  explanation: "Coordinate system choice should match the region's geometry. Spherical coordinates excel for regions with symmetry about a central point (balls, cones, regions bounded by spheres). For regions with an axis of symmetry (cylinders, paraboloids, annuli), cylindrical coordinates are preferable. For rectangular boxes or regions with flat boundaries, Cartesian coordinates remain the simplest choice. Forcing spherical coordinates on a cuboid region, for example, would produce enormously complicated limits."

- question: "Why does the spherical volume element dV = ρ² sin φ dρ dφ dθ include the factor ρ² sin φ? What goes wrong if you forget it?"
  type: short-answer
  answer: "The factor ρ² sin φ is the Jacobian of the transformation from Cartesian to spherical coordinates. It accounts for the fact that small 'spherical boxes' are not equal in size at all locations. At large ρ, the same angular increment spans a larger arc, so the box is larger (hence ρ²). Near the poles (φ ≈ 0 or π), the azimuthal arc r dθ = ρ sin φ dθ shrinks toward zero, so boxes near the poles are smaller (hence sin φ). Without this factor, the integral counts all (ρ, φ, θ) cells as equal in size, giving a systematically wrong answer — typically undercounting volume away from the origin and overcounting near the poles."
  explanation: "The Jacobian is not a correction or adjustment — it is a fundamental requirement when changing variables of integration. Forgetting it is the single most common error in spherical triple integrals, often producing answers that differ by a factor of several times the correct value."
```

## Explainer

From your work with triple integrals in Cartesian coordinates, you know the setup: divide a 3D region into small rectangular boxes of volume dV = dx dy dz, integrate a function over all of them, and sum. The challenge is that many natural 3D regions — cylinders, cones, spheres — have boundaries that are ugly in Cartesian coordinates but simple in other coordinate systems. Switching to **cylindrical** or **spherical** coordinates trades a complicated region description for a complicated volume element, usually a net win.

**Cylindrical coordinates** (r, θ, z) are just polar coordinates in the xy-plane with a vertical z-axis attached. The point (r, θ, z) lies at horizontal distance r from the z-axis, at angle θ around that axis, and height z. Regions like cylinders (r ≤ a), cones (z = r), and half-spaces have simple descriptions. The volume element is dV = r dr dθ dz — note the factor of r, which is the same factor that appeared in the polar area element dA = r dr dθ. It arises because a thin cylindrical shell at radius r has circumference 2πr; a small "wedge-box" at radius r has arc length r dθ along the θ direction, not just dθ.

**Spherical coordinates** (ρ, φ, θ) describe a point by its distance ρ from the origin, polar angle φ measured down from the positive z-axis (the "colatitude"), and azimuthal angle θ around the z-axis. Spheres (ρ = a) and cones (φ = constant) have elegant descriptions. The volume element is dV = ρ² sin φ dρ dφ dθ. The factor ρ² sin φ is the Jacobian of the coordinate change — it accounts for the fact that small "spherical boxes" are larger near the equator (where sin φ is largest) and shrink toward the poles (where sin φ → 0). Forgetting this factor is the single most common error in spherical integrals.

The practical rule: **if the region has an axis of symmetry**, use cylindrical; **if it is symmetric about a central point**, use spherical. A solid ball ρ ≤ a is trivial in spherical coordinates: ∫₀²π ∫₀π ∫₀ᵃ ρ² sin φ dρ dφ dθ. Evaluating each integral separately gives (2π)(2)(a³/3) = 4πa³/3 — the familiar volume of a sphere. In Cartesian coordinates, the same calculation requires intricate nested radical limits. The coordinate system does not change the geometry; it changes how conveniently you can describe it.
