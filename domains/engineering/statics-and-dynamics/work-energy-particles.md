---
id: work-energy-particles
title: Work-Energy Principle for Particles
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: dynamics-newtons-second-law
  type: hard
- id: work-energy-theorem
  type: hard
- id: kinetic-energy
  type: hard
- id: potential-energy
  type: soft
- id: conservation-of-energy
  type: soft
- id: dot-product
  type: soft
builds-toward:
- impulse-momentum-particles
tags:
- dynamics
- work
- energy
- kinetic energy
- potential energy
- conservation
stage: formal-systems
status: draft
---

# Work-Energy Principle for Particles

## Core Idea
The work-energy principle states that net work done on a particle equals its change in kinetic energy: U₁₋₂ = T₂ − T₁, where T = ½mv². Work by a force along a path is U = ∫F·dr. Conservative forces (gravity, springs) have associated potential energy: V_g = mgh, V_e = ½kx². For conservative systems, total mechanical energy is conserved: T₁ + V₁ = T₂ + V₂. When non-conservative forces (friction, applied forces) act, the work they do modifies the energy balance: T₁ + V₁ + U₁₋₂(nc) = T₂ + V₂.

## How It's Best Learned
Classify every force as conservative or non-conservative. For conservative systems, apply energy conservation directly between two states without integrating equations of motion. For problems with friction or variable applied forces, compute work integrals explicitly.

## Common Misconceptions
- Normal forces and forces perpendicular to displacement do zero work — forgetting this inflates the work calculation.
- Applying conservation of energy when friction is present without including the energy dissipation term.
- Using the spring energy formula ½kx² with x measured incorrectly (x must be the spring deformation from natural length).
