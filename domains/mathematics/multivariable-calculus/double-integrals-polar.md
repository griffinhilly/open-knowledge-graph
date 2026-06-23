---
id: double-integrals-polar
title: Double Integrals in Polar Coordinates
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: polar-coordinates
  type: hard
- id: double-integrals-cartesian
  type: hard
builds-toward:
- triple-integrals-cylindrical
- change-of-variables-multivariable
tags:
- polar-coordinates
- jacobian
stage: formal-systems
status: validated
---

# Double Integrals in Polar Coordinates

## Core Idea
In polar coordinates (r, θ), the area element becomes dA = r dr dθ. The double integral becomes ∫_α^β ∫_{r₁(θ)}^{r₂(θ)} f(r cos θ, r sin θ) r dr dθ. Polar is natural for circular or radial regions.

## Questions

```yaml
- question: "A student converts ∬_D (x² + y²) dA over a disk of radius 2 to polar and writes the integral as ∫₀^{2π} ∫₀^2 r² dr dθ. What is wrong with this setup?"
  type: multiple-choice
  options:
    - "The integrand is wrong — x² + y² does not equal r² in polar coordinates"
    - "The limits on r should run from -2 to 2 to cover the full disk"
    - "The area element is missing the factor r — the correct integrand is r² · r = r³"
    - "The limits on θ should be 0 to π, not 0 to 2π, for a full disk"
  answer: 2
  explanation: "In polar coordinates x² + y² = r² is correct, and the disk 0 ≤ r ≤ 2, 0 ≤ θ ≤ 2π is correct. The error is in the area element: dA = r dr dθ, not dr dθ. The correct integral is ∫₀^{2π} ∫₀^2 r² · r dr dθ = ∫₀^{2π} ∫₀^2 r³ dr dθ. Omitting the factor r is the single most common mistake in polar integration."

- question: "Why does the polar area element include the factor r, making dA = r dr dθ rather than just dr dθ?"
  type: multiple-choice
  options:
    - "The factor r converts angular measure from radians to arc length units"
    - "A small wedge-shaped patch at radius r and angle dθ has arc length r dθ, so its area dr · r dθ grows with distance from the origin"
    - "The factor r ensures the Jacobian determinant equals 1, preserving area under the transformation"
    - "Without r, the integral would give volume instead of area"
  answer: 1
  explanation: "A polar 'pixel' at radius r spanning dr radially and dθ angularly is not a rectangle — it is a curved wedge. Its radial side has length dr, but its arc side has length r dθ (arc length = radius × angle). So the area is approximately dr · r dθ = r dr dθ. Near the origin r is small, so patches are tiny; far from the origin r is large, so equal parameter steps dr and dθ span much more area. This geometric fact is the Jacobian of the polar transformation."

- question: "Near the origin, small polar patches (equal Δr and Δθ) represent much smaller areas than identical patches far from the origin."
  type: true-false
  answer: true
  explanation: "True. The area of a polar patch is approximately r · Δr · Δθ. Since r → 0 near the origin, the factor r makes the actual area very small there, even for the same parameter increments Δr and Δθ. This is why the r factor is not optional — equal steps in the parameter space (r, θ) correspond to vastly different areas depending on where you are."

- question: "You can convert a double integral from Cartesian to polar by substituting x = r cos θ and y = r sin θ in the integrand and writing dA = dr dθ."
  type: true-false
  answer: false
  explanation: "False. The substitution x = r cos θ, y = r sin θ in the integrand is correct, but the area element is dA = r dr dθ, not dr dθ. The factor r is the Jacobian of the transformation and is never optional. Without it, the integral assigns equal weight to polar patches that actually have very different areas, producing an incorrect answer. For example, the area of a disk of radius R would come out wrong."

- question: "Explain geometrically why the polar area element is r dr dθ and not simply dr dθ. What would go wrong if you omitted the factor r?"
  type: short-answer
  answer: "A small patch in polar coordinates at position (r, θ) has radial width dr and arc length r dθ (not just dθ), making its area approximately dr · r dθ = r dr dθ. The factor r reflects that equal angular steps dθ sweep out more arc length — and hence more area — the farther you are from the origin. Without r, you would be treating all polar patches as having the same area, which is only true at r = 1. The result would overcount distant regions and undercount regions near the origin, giving an incorrect value for any area or integral over the disk."
  explanation: "The Jacobian of the coordinate change (x,y) → (r,θ) equals r, encoding this geometric distortion. The classic example: integrating 1 over a disk of radius R gives πR² correctly with the r factor; without it you get 2πR instead. The r factor is the mathematical way of saying 'account for the actual size of each coordinate patch.'"
```

## Explainer

From your study of **polar coordinates**, you know that any point in the plane can be described by a radius r (distance from the origin) and an angle θ (measured from the positive x-axis), with x = r cos θ and y = r sin θ. Double integrals in polar coordinates arise when you want to integrate over a region that is naturally described in terms of r and θ — a disk, an annulus, a sector — where the Cartesian description would be awkward. The conversion is straightforward for the integrand: replace x and y with r cos θ and r sin θ. The subtlety is in the area element.

The extra factor of **r** in dA = r dr dθ is the Jacobian of the polar coordinate change. Here is the geometric reason: in Cartesian coordinates, a small rectangle at position (x, y) has area dx dy, and every small rectangle looks the same regardless of where you are. In polar coordinates, a small patch at radius r and angle θ is not a rectangle — it is a curved "wedge." Its radial extent is dr and its angular extent is r dθ (arc length at radius r). So the area is approximately dr · r dθ = r dr dθ. Far from the origin (large r), the wedge is wide and the factor r is large; close to the origin, the wedge is narrow and the factor r approaches 0. Without this factor, you would be integrating over equal "parameter patches" that actually represent very different areas.

The practical workflow for a polar double integral is: (1) sketch the region and determine the bounds for r and θ; (2) write the integrand in polar form; (3) include the factor r; (4) set up and evaluate the iterated integral, usually with r in the inner integral. For a disk of radius R, the bounds are 0 ≤ θ ≤ 2π and 0 ≤ r ≤ R. For a sector, restrict θ. For an annulus, restrict r between two positive values. A region that would require splitting into multiple Cartesian pieces often becomes a single clean polar integral.

The classic example is the area of a disk: ∫₀^{2π} ∫₀^R r dr dθ = ∫₀^{2π} R²/2 dθ = πR². Another is the Gaussian integral ∫∫ e^{−(x²+y²)} dA over all of R², which converts to ∫₀^{2π} ∫₀^∞ e^{−r²} r dr dθ = π, unlocking the one-dimensional result ∫₋∞^∞ e^{−x²} dx = √π. The polar area element r dr dθ is also the first instance of the Jacobian substitution you will generalize in change-of-variables for double integrals.
