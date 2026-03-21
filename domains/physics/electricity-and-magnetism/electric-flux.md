---
id: electric-flux
title: Electric Flux
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: electric-field
  type: hard
- id: dot-product
  type: hard
- id: flux-integrals
  type: soft
- id: divergence-theorem
  type: hard
builds-toward:
- gauss-law
tags:
- flux
- surface-integral
- electrostatics
stage: formal-systems
status: validated
---

# Electric Flux

## Core Idea
Electric flux Φ_E measures the total electric field passing through a surface, defined as Φ_E = ∫ E · dA, where dA is an area element vector pointing outward normal to the surface. For a uniform field through a flat surface, Φ_E = EA cos θ, where θ is the angle between the field and the surface normal. Flux is positive when field lines exit a closed surface and negative when they enter. This concept is central to Gauss's law.

## How It's Best Learned
Visualize flux as the number of field lines piercing a surface. Practice with flat surfaces tilted at various angles, then move to closed surfaces like cubes and spheres around point charges.

## Common Misconceptions
- Flux depends on the angle between the field and the normal, not the surface itself.
- A closed surface with no net charge inside has zero net flux, even if the field is nonzero inside.
- Flux is a scalar quantity, even though both E and dA are vectors.

## Questions

```yaml
- question: "A flat surface is held in a uniform electric field. The surface is then rotated until it is exactly parallel to the field lines. What is the electric flux through the surface?"
  type: multiple-choice
  options:
    - "Maximum — the field passes fully along the surface area"
    - "Half the maximum — the surface is at 45° to the normal"
    - "Zero — no field lines pass through the surface when it is parallel to the field"
    - "It depends on the magnitude of E and the area of the surface"
  answer: 2
  explanation: "Flux measures how much field passes *through* a surface, not along it. The formula Φ = EA cos θ uses θ as the angle between E and the outward normal to the surface. When the surface is parallel to the field, the normal is perpendicular to E, so θ = 90° and cos 90° = 0 — flux is zero. Think of the wind-and-net analogy: a net held parallel to the wind catches nothing. The most common error is confusing 'angle with the surface' and 'angle with the normal' — these are complementary angles."

- question: "A closed spherical surface surrounds a region containing a complicated, non-uniform electric field. No net charge is enclosed within the sphere. What is the net electric flux through the sphere?"
  type: multiple-choice
  options:
    - "Positive — because E² is always positive, field contributions never cancel"
    - "Nonzero — the complicated field means contributions do not perfectly cancel"
    - "Zero — every field line that enters the closed surface must also exit somewhere"
    - "Negative — field lines entering the sphere dominate because the field points inward"
  answer: 2
  explanation: "By Gauss's law, net flux through any closed surface equals the enclosed charge divided by ε₀. With zero net enclosed charge, the net flux is exactly zero — regardless of how complex the field is inside. This is not an approximation: every field line that enters the closed surface must exit it somewhere, because there is no source (positive charge) or sink (negative charge) inside to terminate them. The field can be arbitrarily complicated; the net cancellation is exact. This is one of the most powerful consequences of Gauss's law."

- question: "Electric flux is a scalar quantity, even though it is calculated using the dot product of two vectors (E and dA)."
  type: true-false
  answer: true
  explanation: "True. The dot product of two vectors produces a scalar — a single number with no direction. E · dA = |E| |dA| cos θ, where θ is the angle between them. The result is a signed number (positive when E has a component in the direction of the outward normal, negative when it has a component opposing the normal). Even though both E and dA are vectors, their combination through the dot product — and the integration over the surface — yields a scalar: the total flux. Many students mistakenly expect flux to have a direction since it involves vectors, but the dot product removes this."

- question: "Increasing the area of a surface always increases the electric flux through it, because more surface area intercepts more field lines."
  type: true-false
  answer: false
  explanation: "False. Flux depends on both area and orientation. If you increase the area of a surface that is already parallel to the field (normal perpendicular to E), the flux remains zero regardless of how large the surface becomes — no field lines pass through it. More precisely, Φ = ∫ E · dA, and each area element contributes E cos θ dA. If θ = 90° everywhere, additional area adds nothing. It is only when the surface (or part of it) is oriented with a component perpendicular to the field that area increases flux."

- question: "A closed cube is placed in a uniform electric field directed parallel to one pair of faces (so two faces are perpendicular to the field, two are parallel, and two are at right angles to both). Which faces contribute to net flux, and what is the total net flux through the cube?"
  type: short-answer
  answer: "Only the two faces perpendicular to the field contribute nonzero flux. The field enters through one face (negative flux, since field is antiparallel to the outward normal) and exits through the opposite face (positive flux, since field is parallel to the outward normal). The four faces parallel or oblique to the field have zero flux. The entering and exiting fluxes are equal in magnitude, so the total net flux is zero — consistent with no enclosed charge."
  explanation: "This example illustrates both aspects of flux: the angle-dependence (faces parallel to the field contribute nothing) and the cancellation on closed surfaces with no enclosed charge (entering flux equals exiting flux). Gauss's law guarantees the net is zero. If instead a positive charge were enclosed, the exiting flux would exceed the entering flux, and the net would be positive."
```

## Explainer

You already know that an **electric field** fills the space around charges, pointing away from positive charges and toward negative ones. You also know the dot product, which extracts "how much of one vector lies along another." Electric flux combines these ideas to answer a geometric question: how much of the electric field passes *through* a surface, rather than skimming along it?

Think of the field as invisible wind. A flat net held perpendicular to the wind intercepts maximum wind — full flux. Tilt the net 45° and the wind partly passes through, partly along the mesh — less flux. Rotate the net until it is parallel to the wind and you catch nothing — zero flux. The formula Φ_E = E · A = EA cos θ encodes exactly this geometry, where θ is the angle between the field vector and the **outward normal** to the surface. When θ = 0° the field punches straight through; when θ = 90° the field runs parallel to the surface and contributes nothing. Note that flux is a scalar: the two vectors E and dA combine through a dot product to give a single number.

For curved surfaces or non-uniform fields, you divide the surface into infinitesimal patches, each treated as locally flat and experiencing a locally uniform field, and integrate: Φ_E = ∫ E · dA. This is exactly the flux integral from vector calculus — electric flux is the flux of the vector field E. The integral sums contributions from every patch of the surface, weighted by how perpendicular the field is to each patch.

On a **closed surface**, the sign of flux has physical meaning. Field lines exiting the enclosed volume contribute positive flux; lines entering contribute negative. If a net positive charge sits inside, all field lines radiate outward — net flux is positive. If a net negative charge sits inside, field lines converge inward — net flux is negative. If *no* net charge is enclosed, every field line that enters must exit somewhere else, and the contributions cancel exactly — net flux is zero no matter how complicated the field is inside. This last observation is the content of Gauss's law: net flux through any closed surface equals the enclosed charge divided by ε₀. Electric flux is the mathematical language in which Gauss's law is written, making your mastery of it the direct path to one of the most powerful tools in electrostatics.
