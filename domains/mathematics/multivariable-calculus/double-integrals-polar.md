---
id: double-integrals-polar
title: Double Integrals in Polar Coordinates
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: polar-coordinates
  type: hard
builds-toward:
- triple-integrals-cylindrical
- change-of-variables-multivariable
tags:
- polar-coordinates
- jacobian
stage: formal-systems
status: draft
---

# Double Integrals in Polar Coordinates

## Core Idea
In polar coordinates (r, θ), the area element becomes dA = r dr dθ. The double integral becomes ∫_α^β ∫_{r₁(θ)}^{r₂(θ)} f(r cos θ, r sin θ) r dr dθ. Polar is natural for circular or radial regions.

## Explainer

From your study of **polar coordinates**, you know that any point in the plane can be described by a radius r (distance from the origin) and an angle θ (measured from the positive x-axis), with x = r cos θ and y = r sin θ. Double integrals in polar coordinates arise when you want to integrate over a region that is naturally described in terms of r and θ — a disk, an annulus, a sector — where the Cartesian description would be awkward. The conversion is straightforward for the integrand: replace x and y with r cos θ and r sin θ. The subtlety is in the area element.

The extra factor of **r** in dA = r dr dθ is the Jacobian of the polar coordinate change. Here is the geometric reason: in Cartesian coordinates, a small rectangle at position (x, y) has area dx dy, and every small rectangle looks the same regardless of where you are. In polar coordinates, a small patch at radius r and angle θ is not a rectangle — it is a curved "wedge." Its radial extent is dr and its angular extent is r dθ (arc length at radius r). So the area is approximately dr · r dθ = r dr dθ. Far from the origin (large r), the wedge is wide and the factor r is large; close to the origin, the wedge is narrow and the factor r approaches 0. Without this factor, you would be integrating over equal "parameter patches" that actually represent very different areas.

The practical workflow for a polar double integral is: (1) sketch the region and determine the bounds for r and θ; (2) write the integrand in polar form; (3) include the factor r; (4) set up and evaluate the iterated integral, usually with r in the inner integral. For a disk of radius R, the bounds are 0 ≤ θ ≤ 2π and 0 ≤ r ≤ R. For a sector, restrict θ. For an annulus, restrict r between two positive values. A region that would require splitting into multiple Cartesian pieces often becomes a single clean polar integral.

The classic example is the area of a disk: ∫₀^{2π} ∫₀^R r dr dθ = ∫₀^{2π} R²/2 dθ = πR². Another is the Gaussian integral ∫∫ e^{−(x²+y²)} dA over all of R², which converts to ∫₀^{2π} ∫₀^∞ e^{−r²} r dr dθ = π, unlocking the one-dimensional result ∫₋∞^∞ e^{−x²} dx = √π. The polar area element r dr dθ is also the first instance of the Jacobian substitution you will generalize in change-of-variables for double integrals.
