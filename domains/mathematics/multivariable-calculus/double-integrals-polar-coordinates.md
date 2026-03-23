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
status: validated
---

# Double Integrals in Polar Coordinates

## Core Idea
In polar coordinates (r, θ), the element dA = r dr dθ (not dr dθ). For a region in polar form, ∬_D f(x, y) dA = ∫_α^β ∫_{r₁(θ)}^{r₂(θ)} f(r cos θ, r sin θ) r dr dθ. Polar coordinates simplify integrals over disks and annuli.

## Questions

```yaml
- question: "A student sets up the integral of f over a disk of radius 3 as ∫₀^{2π} ∫₀^3 f(r cosθ, r sinθ) dr dθ. What error have they made?"
  type: multiple-choice
  options:
    - "The limits for θ should be 0 to π, not 0 to 2π"
    - "They should not substitute x = r cosθ and y = r sinθ into the integrand"
    - "They omitted the Jacobian factor r, writing dr dθ instead of r dr dθ"
    - "The r integral should be on the outside and θ on the inside"
  answer: 2
  explanation: "The area element in polar coordinates is r dr dθ, not dr dθ. The extra factor of r is the Jacobian of the polar transformation, accounting for the fact that polar 'cells' grow in size as r increases. Without this factor, the integral treats all radii equally, systematically undercounting regions far from the origin. This is the single most common error in polar integration."

- question: "Why does the integral ∬_{ℝ²} e^{−(x²+y²)} dA become tractable in polar coordinates when it resists direct computation in Cartesian coordinates?"
  type: multiple-choice
  options:
    - "In Cartesian form, e^{−x²} and e^{−y²} cannot be separated into a product of single-variable integrals"
    - "The region ℝ² cannot be expressed with finite bounds in Cartesian coordinates"
    - "In polar form, x²+y² = r², giving e^{−r²}, and the area element r dr dθ allows the integral to factor into a tractable product of separate integrals in r and θ"
    - "Polar coordinates introduce an algebraic simplification specific to exponential functions"
  answer: 2
  explanation: "In Cartesian form, ∫∫ e^{−x²−y²} dx dy = (∫e^{−x²}dx)(∫e^{−y²}dy), which requires evaluating ∫e^{−x²}dx — an integral with no elementary closed form when taken alone. In polar form, x²+y² = r² and dA = r dr dθ, giving ∫₀^{2π}dθ · ∫₀^∞ e^{−r²} r dr. The inner integral ∫r e^{−r²}dr has elementary antiderivative −½e^{−r²}, so the full computation yields π. The key is that the Jacobian factor r makes the r-integral tractable."

- question: "The area element in polar coordinates is dr dθ, analogous to dx dy in Cartesian coordinates."
  type: true-false
  answer: false
  explanation: "The polar area element is r dr dθ, not dr dθ. This is because a 'polar rectangle' between r and r+dr, and between θ and θ+dθ, is a curved wedge whose arc length along its outer edge is r·dθ, giving area ≈ r dr dθ. The factor r is the Jacobian of the transformation from Cartesian to polar coordinates. Near the origin (small r), polar cells are tiny; far away (large r), they are large. Without the r factor, all radial positions are weighted equally, producing a systematically wrong answer."

- question: "Polar coordinates are most useful for double integrals when the region of integration involves x² + y² or has circular symmetry."
  type: true-false
  answer: true
  explanation: "The core benefit of polar coordinates is the conversion x²+y² → r², which simplifies both circular regions (disks, annuli, sectors) and integrands containing x²+y² into clean expressions in r. A disk of radius R becomes simply 0 ≤ r ≤ R, 0 ≤ θ ≤ 2π — a rectangle in (r,θ) space — whereas in Cartesian coordinates it requires messy square-root bounds. The Gaussian integral e^{−(x²+y²)} is the canonical example of an integrand that becomes elementary after the substitution."

- question: "Why does the polar area element include an extra factor of r, and what goes wrong if you forget it?"
  type: short-answer
  answer: "A polar 'cell' between r and r+dr, and between θ and θ+dθ, is a wedge shape. Its width in the angular direction is the arc length r·dθ (not just dθ), so its area is approximately r dr dθ. This factor r is the Jacobian of the coordinate transformation: it corrects for the fact that equal increments of (r, θ) do not correspond to equal areas — cells near the origin are tiny while cells far from the origin are large. Forgetting r means treating all radial positions as equally weighted, which undercounts the contribution from large r and gives an incorrect integral value."
  explanation: "The Jacobian appears whenever you change variables in a multiple integral: the area element transforms as dA = |∂(x,y)/∂(r,θ)| dr dθ, and computing this determinant yields exactly r. This is not a coincidence or a convention to memorize — it is the precise correction factor that makes the area calculation accurate under the coordinate change."
```

## Explainer

From your study of double integrals in Cartesian coordinates, you know how to integrate f(x, y) over a rectangular or general region by iterating single-variable integrals. The key challenge was describing the region of integration — for a disk of radius R centered at the origin, the bounds x² + y² ≤ R² produce messy square-root expressions in Cartesian form. **Polar coordinates** replace (x, y) with (r, θ), where r is the distance from the origin and θ is the angle from the positive x-axis. In polar form, the disk becomes simply 0 ≤ r ≤ R, 0 ≤ θ ≤ 2π — a clean rectangle in (r, θ) space.

The critical detail — and the most common source of error — is the area element. In Cartesian coordinates, a small rectangle has area dA = dx dy. In polar coordinates, a small "polar rectangle" between r and r + dr, and between θ and θ + dθ, is shaped like a curved wedge. Its area is approximately r dr dθ, not dr dθ. The extra factor of **r** is the **Jacobian** of the polar coordinate transformation; it accounts for the fact that polar "cells" near the origin are tiny while those far from the origin are large. Forgetting this factor r is the single most frequent mistake.

The full conversion rule is: substitute x = r cos θ and y = r sin θ into the integrand, replace dA with r dr dθ, and set the limits in terms of r and θ. For a disk D of radius R: ∬_D f(x, y) dA = ∫₀^{2π} ∫₀^R f(r cos θ, r sin θ) · r dr dθ. For an annulus a² ≤ x² + y² ≤ b², the r limits become a to b. When the region's boundary is described by a curve like r = 1 + cos θ (a cardioid), the inner r-integral runs from 0 to 1 + cos θ.

Polar coordinates shine whenever the integrand contains x² + y² (which becomes r²) or the region is a disk, sector, or annulus. The canonical example is the Gaussian integral: ∬_{ℝ²} e^{−(x²+y²)} dA. In Cartesian coordinates this is intractable directly, but in polar it becomes ∫₀^{2π} ∫₀^∞ e^{−r²} r dr dθ, which separates into ∫₀^{2π} dθ · ∫₀^∞ r e^{−r²} dr = 2π · ½ = π. This result establishes that ∫_{−∞}^∞ e^{−x²} dx = √π, one of the most important integrals in probability and physics — made accessible only by polar coordinates.
