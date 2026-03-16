---
id: collision-analysis-restitution
title: Collision Analysis and Coefficient of Restitution
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: impulse-momentum-particles
  type: hard
- id: impact-and-restitution
  type: hard
- id: conservation-of-linear-momentum
  type: hard
tags:
- collision
- restitution
- elastic
- inelastic
- impact
stage: formal-systems
status: draft
---

# Collision Analysis and Coefficient of Restitution

## Core Idea
The coefficient of restitution e relates velocities before and after collision for particles along the collision line: e = -(v₂' - v₁')/(v₂ - v₁). Values range from e = 0 (perfectly inelastic) to e = 1 (perfectly elastic). Both momentum and the restitution equation are used to solve collision problems. Energy is lost in collisions when e < 1.

## Explainer

Conservation of linear momentum — your core prerequisite — tells you that the total momentum of an isolated two-particle system is unchanged by a collision: m₁v₁ + m₂v₂ = m₁v₁' + m₂v₂'. This gives you one equation with two unknowns (the post-collision velocities v₁' and v₂'). The momentum equation alone is underdetermined; you need a second relationship that characterizes the collision itself. That's where the **coefficient of restitution** e enters.

The coefficient of restitution is defined along the line of impact as e = -(v₂' - v₁')/(v₂ - v₁), or equivalently, the relative separation velocity equals e times the relative approach velocity. When e = 1, the particles bounce apart as fast as they came together — a **perfectly elastic collision** — and kinetic energy is fully conserved. When e = 0, the particles stick together and move as one mass — a **perfectly inelastic collision** — and the maximum kinetic energy is lost. Real collisions fall between these extremes; a rubber ball on concrete might have e ≈ 0.8, a lump of clay e ≈ 0.

The standard solution procedure for a **direct central impact** (1D, particles moving along the same line) is to write the momentum equation and the restitution equation as a 2×2 linear system in v₁' and v₂', then solve simultaneously. The kinetic energy lost in the collision is ΔKE = ½m₁v₁² + ½m₂v₂² - ½m₁v₁'² - ½m₂v₂'², and this can be verified to vanish only when e = 1. For an **oblique impact** (particles approaching at an angle), resolve velocities into components along the line of impact and perpendicular to it. The impulse acts only along the line of impact, so components perpendicular to it are unchanged; apply momentum conservation and the restitution equation only to the impact-line components.

The impulse-momentum framework you already know connects naturally here: the entire velocity change is caused by the impulsive contact force, which acts for a very short time. The ratio e fundamentally reflects how much of the approach kinetic energy is stored as elastic deformation and recovered, versus dissipated as heat, sound, or permanent deformation. Engineering applications range from designing protective packaging (low e absorbs energy) to billiard ball dynamics (e near 1 preserves speed) to vehicle crash analysis (where e governs how energy is transferred to occupants).
