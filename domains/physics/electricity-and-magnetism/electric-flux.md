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

## Explainer

You already know that an **electric field** fills the space around charges, pointing away from positive charges and toward negative ones. You also know the dot product, which extracts "how much of one vector lies along another." Electric flux combines these ideas to answer a geometric question: how much of the electric field passes *through* a surface, rather than skimming along it?

Think of the field as invisible wind. A flat net held perpendicular to the wind intercepts maximum wind — full flux. Tilt the net 45° and the wind partly passes through, partly along the mesh — less flux. Rotate the net until it is parallel to the wind and you catch nothing — zero flux. The formula Φ_E = E · A = EA cos θ encodes exactly this geometry, where θ is the angle between the field vector and the **outward normal** to the surface. When θ = 0° the field punches straight through; when θ = 90° the field runs parallel to the surface and contributes nothing. Note that flux is a scalar: the two vectors E and dA combine through a dot product to give a single number.

For curved surfaces or non-uniform fields, you divide the surface into infinitesimal patches, each treated as locally flat and experiencing a locally uniform field, and integrate: Φ_E = ∫ E · dA. This is exactly the flux integral from vector calculus — electric flux is the flux of the vector field E. The integral sums contributions from every patch of the surface, weighted by how perpendicular the field is to each patch.

On a **closed surface**, the sign of flux has physical meaning. Field lines exiting the enclosed volume contribute positive flux; lines entering contribute negative. If a net positive charge sits inside, all field lines radiate outward — net flux is positive. If a net negative charge sits inside, field lines converge inward — net flux is negative. If *no* net charge is enclosed, every field line that enters must exit somewhere else, and the contributions cancel exactly — net flux is zero no matter how complicated the field is inside. This last observation is the content of Gauss's law: net flux through any closed surface equals the enclosed charge divided by ε₀. Electric flux is the mathematical language in which Gauss's law is written, making your mastery of it the direct path to one of the most powerful tools in electrostatics.
