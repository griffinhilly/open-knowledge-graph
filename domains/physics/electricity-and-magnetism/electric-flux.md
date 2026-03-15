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
