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

## Explainer

You already know from fluid properties and continuum mechanics that a fluid deforms continuously under shear stress — unlike a solid, which deforms to a fixed amount and stops. But what determines the rate of deformation? Viscosity is the answer: it quantifies how much resistance a fluid offers to being sheared. The physical picture is one of fluid **layers** sliding past one another. Faster layers drag slower layers forward through molecular momentum exchange; slower layers drag faster layers backward. This internal friction, averaged over enormous numbers of molecular collisions, is what Newton's law of viscosity captures in a single equation.

**Newton's law of viscosity** states τ = μ(du/dy): the shear stress τ (force per unit area) between adjacent fluid layers equals the **dynamic viscosity** μ times the **velocity gradient** du/dy. A **Newtonian fluid** is defined precisely by this linear relationship — doubling the shear rate du/dy doubles the shear stress τ. Water and air are Newtonian across virtually all engineering conditions. The viscosity μ has units of Pa·s and depends strongly on temperature: water's viscosity drops by a factor of three between 20°C and 70°C (molecular mobility increases with thermal energy), while air's viscosity increases modestly with temperature (more frequent molecular collisions transfer more momentum). **Kinematic viscosity** ν = μ/ρ combines viscosity and density into a single parameter that governs how momentum diffuses through a fluid; it appears naturally in the Reynolds number Re = VL/ν.

The **no-slip condition** — that fluid immediately at a solid boundary moves at exactly the boundary's velocity — follows from molecular physics: fluid molecules collide with the wall, exchange momentum, and match its velocity. This is not an assumption imposed for convenience; it is an empirical observation holding for virtually all engineering flows. Its consequence is immediately practical: even a flow with high free-stream velocity has zero velocity at every solid wall, creating a velocity gradient du/dy and therefore a shear stress τ at every surface. Without the no-slip condition, viscosity would be irrelevant at walls — the entire study of boundary layers, pipe friction, and drag depends on it.

**Non-Newtonian fluids** break the linear τ–(du/dy) relationship in characteristic ways. **Shear-thinning** fluids (blood, ketchup, many polymer solutions) have viscosity that decreases with shear rate — they flow more easily when stirred faster, which is why ketchup suddenly pours after vigorous shaking. **Shear-thickening** fluids (dense cornstarch suspensions) stiffen under rapid deformation — the basis of "oobleck" that behaves as a solid under impact. **Bingham plastics** (toothpaste, mayonnaise) act as solids below a yield stress and flow only above it. Recognizing whether a fluid is Newtonian or not matters enormously in design: pipe and pump sizing formulas derived from Newton's viscosity law will give wrong answers for non-Newtonian fluids, sometimes catastrophically so in polymer processing, food engineering, and biological flow applications.
