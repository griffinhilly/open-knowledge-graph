---
id: applications-triple-integrals
title: 'Applications of Triple Integrals: Volume and Mass'
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: change-of-variables-jacobian
  type: hard
builds-toward:
- vector-fields
tags:
- applications
- volume
- mass
- center-of-mass
stage: formal-systems
status: draft
---

# Applications of Triple Integrals: Volume and Mass

## Core Idea
Triple integrals compute volume of solids, mass with density functions, and center of mass. The choice of coordinates (Cartesian, cylindrical, spherical) depends on the region's symmetry, dramatically affecting computational difficulty.

## Explainer

You know from the Jacobian and change-of-variables that when you switch coordinate systems, the volume element transforms: dV = |J| du dv dw, where |J| is the absolute value of the Jacobian determinant. This is not just a technical detail — it is the engine that makes triple integrals tractable. The three coordinate systems (Cartesian, cylindrical, spherical) each come with their own volume element, and matching the coordinate system to the problem's symmetry can turn an impossible integral into a routine one.

The simplest application is **volume**. For a solid region E, the volume is simply ∭_E dV — integrating 1 over the region. In Cartesian coordinates, dV = dx dy dz, and you set up iterated limits. For the ball of radius R centered at the origin, this gives six nested limits with ugly square-root boundaries — technically correct but painful. In **spherical coordinates** (ρ, φ, θ), where dV = ρ² sin(φ) dρ dφ dθ, the same ball becomes 0 ≤ ρ ≤ R, 0 ≤ φ ≤ π, 0 ≤ θ ≤ 2π — a rectangular box of limits, yielding (4/3)πR³ almost immediately. The symmetry of the region and the coordinate system are aligned.

**Mass** generalizes volume: if a solid has density function δ(x, y, z), then mass = ∭_E δ dV. The density might vary with position — heavier near the center of a planet, for example, or varying with height in a layered material. Once you have mass, the **center of mass** follows: x̄ = (1/m) ∭_E x δ dV, and similarly for ȳ and z̄. **Moments of inertia** (for rotation) have the same structure: I_z = ∭_E (x² + y²) δ dV, where x² + y² is the squared distance from the z-axis. This integrand is why **cylindrical coordinates** (r, θ, z) with r² = x² + y² and dV = r dr dθ dz are natural for cylindrical or axially symmetric objects.

The practical skill is recognizing symmetry quickly. A cone or hemisphere suggests spherical or cylindrical coordinates. A box or prism suggests Cartesian. An ellipsoid suggests a scaled version of spherical coordinates with a Jacobian adjustment. In every case, the Jacobian from your change-of-variables prerequisite tells you the factor to include. The conceptual content — mass, volume, center of mass — is the same regardless of coordinates; only the computational path changes. Choosing well is what separates a five-minute calculation from a fifty-minute one.
