---
id: gravity-potential-theory-earths-field
title: Gravity Potential Theory and Earth's Gravitational Field
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: earth-interior-structure
  type: soft
- id: laplaces-equation
  type: soft
- id: applications-integrals-area-mass
  type: soft
- id: electric-potential
  type: soft
builds-toward:
- gravity-anomalies-and-interpretation
- geoid-determination-and-geodesy
- potential-field-methods-gravity-magnetics
tags:
- gravity
- potential-theory
- field-theory
- inverse-problems
stage: advanced
status: validated
---

# Gravity Potential Theory and Earth's Gravitational Field

## Core Idea
The gravitational potential U satisfies Laplace's equation ∇²U = 0 in mass-free regions and Poisson's equation ∇²U = −4πGρ in regions with density ρ. With this sign convention (U = GM/r for a point mass), the gravity field is g = ∇U, and gravitational anomalies arise from lateral density variations in the crust and mantle. Forward modeling of gravity anomalies allows estimation of crustal thickness, density structure, and subsurface mass distribution; inverse methods recover density models from observed gravity data.

## How It's Best Learned
Verify by hand that 1/r satisfies Laplace's equation away from the origin, using the radial part of the Laplacian in spherical coordinates. Then apply Gauss's theorem: integrating a surface gravity anomaly over the whole plane gives 2πG times the excess mass, whatever its shape or depth. Check this on a buried sphere's anomaly to see that total excess mass is fixed even though geometry is not.

## Common Misconceptions
- Because gravity inversion is non-unique, gravity data fix nothing about the source. (The anomaly fixes the total excess mass, and the anomaly's width sets a maximum possible depth for the source.)
- Gravitational potential and gravitational acceleration are the same quantity. (Potential is a scalar and gravity is its gradient, a vector; a surface of constant potential is not a surface of constant gravity.)
- A spherical body's external gravity depends on how mass is arranged inside it. (Outside any spherically symmetric body, the field is exactly that of a point mass at its centre, so only the total mass matters.)

## Questions

```yaml
- question: "Which equation governs the gravitational potential U in a region that contains matter with density ρ?"
  type: multiple-choice
  options: ["∇²U = 0 (Laplace's equation)", "∇²U = −4πGρ (Poisson's equation)", "g = −∇²U", "∇U = −4πGρ"]
  answer: 1
  explanation: "Poisson's equation ∇²U = −4πGρ applies wherever mass is present (ρ ≠ 0). Laplace's equation ∇²U = 0 is the special case when ρ = 0 — i.e., in mass-free regions such as the air above the ground. The gravity field vector is recovered from the potential as its gradient, g = ∇U in this sign convention, not the Laplacian."

- question: "A gravity anomaly observed at Earth's surface can arise mainly from density variations in the upper crust, not from deeper mantle structure."
  type: true-false
  answer: false
  explanation: "Gravity anomalies integrate the effect of all density contrasts along the entire vertical column beneath the measurement point. Deep density variations — such as thickened oceanic crust, subducting slabs, or mantle plumes — can produce measurable gravity anomalies at the surface. The challenge of gravity interpretation is precisely that signals from different depths superimpose, making it an underdetermined inverse problem."

- question: "Explain the conceptual difference between the forward problem and the inverse problem in gravity interpretation."
  type: short-answer
  answer: "The forward problem predicts the surface gravity field produced by a given (assumed) density distribution in the subsurface. The inverse problem works backwards: given observed surface gravity data, it seeks to recover the subsurface density distribution that could explain those observations. The inverse problem is non-unique — many different density models can fit the same gravity data — so additional constraints (e.g., seismic or borehole data) are needed."
  explanation: "Forward modeling is deterministic and always has a unique solution: a specified density model produces one and only one gravity field. The inverse is ill-posed because gravity measurements lose information about depth — a shallow low-density body and a deeper high-density body can produce the same surface anomaly. This non-uniqueness is a fundamental challenge in all potential-field geophysics."
```

## Explainer

Gravity potential theory extends the point-mass formula from classical mechanics to the full, continuous density distribution of the Earth. Instead of summing the gravitational pull of individual mass points, we define a scalar field U at every point in space such that the gravitational acceleration vector **g** = ∇U (the geodesy convention, in which U = GM/r is positive). This means you can recover the direction and magnitude of gravity everywhere by taking the spatial gradient of a single scalar quantity — a powerful simplification that draws directly on the potential theory framework you learned in mathematics.

In mass-free regions (above the surface, in air), U satisfies Laplace's equation ∇²U = 0. Where matter is present with density ρ, the equation becomes Poisson's equation ∇²U = −4πGρ. These two equations are not different physics — Poisson's equation reduces to Laplace's when ρ = 0. The analogy with electric potential is close: just as electrostatic potential satisfies Laplace's equation in charge-free space and Poisson's equation where charge exists, gravitational potential obeys the same mathematical structure (with mass density replacing charge density and 4πG replacing 1/ε₀).

The practical power of this framework lies in gravity anomalies — departures from the expected gravity of a smooth, idealized reference Earth (the normal gravity field). If the crust beneath your gravimeter is unusually dense (like a buried iron ore deposit), the observed gravity will exceed the reference value: a positive anomaly. If the crust is unusually thin or contains a low-density salt dome, gravity will fall below reference: a negative anomaly. The shape and magnitude of the anomaly encode information about the depth, geometry, and density contrast of the causative body.

Forward modeling works from cause to effect: given an assumed density structure, compute the predicted gravity field by integrating Poisson's equation. This is unique and mathematically tractable. The inverse problem — recovering density structure from observed anomalies — is fundamentally non-unique: infinitely many density distributions can produce the same surface gravity field, because gravity measurements at the surface cannot distinguish a shallow weak density contrast from a deep strong one. Resolving this ambiguity requires additional constraints from seismic data, borehole samples, or geological reasoning. This non-uniqueness is not a limitation of our methods but a mathematical property of potential fields, and managing it is central to applied geophysics.
