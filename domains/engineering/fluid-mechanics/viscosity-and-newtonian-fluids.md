---
id: viscosity-and-newtonian-fluids
title: Viscosity and Newtonian Fluid Behavior
domain: engineering
course: fluid-mechanics
prerequisites:
- id: fluid-properties-and-continuum
  type: hard
builds-toward:
- navier-stokes-equations
- reynolds-number
- laminar-pipe-flow
tags:
- viscosity
- shear stress
- Newtonian fluid
- non-Newtonian
- no-slip condition
stage: abstract-reasoning
status: validated
---

# Viscosity and Newtonian Fluid Behavior

## Core Idea
A Newtonian fluid obeys Newton's law of viscosity: shear stress τ = μ(du/dy), where μ is the dynamic viscosity and du/dy is the velocity gradient (shear rate). The no-slip condition requires that fluid in contact with a solid boundary moves at the boundary's velocity. Non-Newtonian fluids (shear-thinning, shear-thickening, Bingham plastics) have viscosity that depends on shear rate, making them fundamentally different from Newtonian ones like water and air.

## How It's Best Learned
Derive Couette flow (flow between parallel plates with one moving) from Newton's viscosity law to see how a linear velocity profile emerges. Compare viscosities of different fluids in tables and connect units (Pa·s = kg/(m·s)) to physical meaning.

## Common Misconceptions
- Viscosity is a resistance to flow due to internal friction, not a measure of 'thickness' per se; some thick gels are non-Newtonian.
- The no-slip condition is an empirical observation that holds for most engineering flows but breaks down at very low pressures (slip flow regime).
- Kinematic viscosity ν = μ/ρ is not the same as dynamic viscosity μ; both matter in different contexts.
