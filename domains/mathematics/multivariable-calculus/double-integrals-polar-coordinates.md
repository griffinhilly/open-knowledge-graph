---
id: double-integrals-polar-coordinates
title: Double Integrals in Polar Coordinates
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: double-integrals-cartesian-coordinates
  type: hard
- id: double-integrals-polar
  type: hard
builds-toward:
- triple-integrals-cylindrical
tags:
- polar-coordinates
- double-integrals
- change-of-variables
stage: formal-systems
status: draft
---

# Double Integrals in Polar Coordinates

## Core Idea
In polar coordinates (r, θ), the element dA = r dr dθ (not dr dθ). For a region in polar form, ∬_D f(x, y) dA = ∫_α^β ∫_{r₁(θ)}^{r₂(θ)} f(r cos θ, r sin θ) r dr dθ. Polar coordinates simplify integrals over disks and annuli.

## Explainer

From your study of double integrals in Cartesian coordinates, you know how to integrate f(x, y) over a rectangular or general region by iterating single-variable integrals. The key challenge was describing the region of integration — for a disk of radius R centered at the origin, the bounds x² + y² ≤ R² produce messy square-root expressions in Cartesian form. **Polar coordinates** replace (x, y) with (r, θ), where r is the distance from the origin and θ is the angle from the positive x-axis. In polar form, the disk becomes simply 0 ≤ r ≤ R, 0 ≤ θ ≤ 2π — a clean rectangle in (r, θ) space.

The critical detail — and the most common source of error — is the area element. In Cartesian coordinates, a small rectangle has area dA = dx dy. In polar coordinates, a small "polar rectangle" between r and r + dr, and between θ and θ + dθ, is shaped like a curved wedge. Its area is approximately r dr dθ, not dr dθ. The extra factor of **r** is the **Jacobian** of the polar coordinate transformation; it accounts for the fact that polar "cells" near the origin are tiny while those far from the origin are large. Forgetting this factor r is the single most frequent mistake.

The full conversion rule is: substitute x = r cos θ and y = r sin θ into the integrand, replace dA with r dr dθ, and set the limits in terms of r and θ. For a disk D of radius R: ∬_D f(x, y) dA = ∫₀^{2π} ∫₀^R f(r cos θ, r sin θ) · r dr dθ. For an annulus a² ≤ x² + y² ≤ b², the r limits become a to b. When the region's boundary is described by a curve like r = 1 + cos θ (a cardioid), the inner r-integral runs from 0 to 1 + cos θ.

Polar coordinates shine whenever the integrand contains x² + y² (which becomes r²) or the region is a disk, sector, or annulus. The canonical example is the Gaussian integral: ∬_{ℝ²} e^{−(x²+y²)} dA. In Cartesian coordinates this is intractable directly, but in polar it becomes ∫₀^{2π} ∫₀^∞ e^{−r²} r dr dθ, which separates into ∫₀^{2π} dθ · ∫₀^∞ r e^{−r²} dr = 2π · ½ = π. This result establishes that ∫_{−∞}^∞ e^{−x²} dx = √π, one of the most important integrals in probability and physics — made accessible only by polar coordinates.
