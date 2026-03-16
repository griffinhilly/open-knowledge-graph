---
id: fluid-statics-pressure
title: Fluid Statics and Hydrostatic Pressure
domain: engineering
course: fluid-mechanics
prerequisites:
- id: fluid-properties-and-continuum
  type: hard
- id: equilibrium-particles-3d
  type: soft
builds-toward:
- manometry-and-pressure-measurement
- buoyancy-and-archimedes
- hydrostatic-forces-on-surfaces
tags:
- pressure
- hydrostatics
- Pascal's law
- pressure variation
stage: abstract-reasoning
status: validated
---

# Fluid Statics and Hydrostatic Pressure

## Core Idea
In a static fluid, pressure increases with depth according to dP/dz = −ρg, giving the hydrostatic equation P = P₀ + ρgh for an incompressible fluid. Pascal's law states that a pressure change applied at one point is transmitted undiminished throughout a static fluid. Pressure is isotropic — it acts equally in all directions at a point — and is measured as absolute or gauge pressure relative to atmospheric.

## How It's Best Learned
Derive the pressure-depth relationship from a free-body diagram of a fluid element. Practice computing pressures at various depths in tanks with multiple fluid layers. Use U-tube problems to build physical intuition before formalizing with the hydrostatic equation.

## Common Misconceptions
- Pressure depends only on depth and fluid density, not on the shape or total volume of the container (the hydrostatic paradox).
- Gauge pressure is relative to atmosphere; failing to specify absolute vs. gauge leads to sign errors.
- Pressure is a scalar, not a vector, even though forces due to pressure act normal to surfaces.

## Explainer

From your study of fluid properties, you know that a fluid deforms continuously under shear stress — it cannot sustain a static shear load. That single fact forces a remarkable conclusion: in a fluid at rest, the only internal stress is pressure, and pressure must act equally in all directions at any given point. This **isotropy of pressure** is not an assumption; it follows directly from the inability of fluids to resist shear. If pressure were different in different directions, there would be a net moment on any fluid element, causing continuous rotation — contradicting the premise of static equilibrium.

The pressure-depth relationship P = P₀ + ρgh follows from a simple force balance on a horizontal slice of fluid. Slice out a thin slab at depth h with area A: the weight of the fluid above it is ρ·g·h·A, and this weight must be supported by the excess pressure at the bottom of the slab relative to the top. Dividing by area gives ΔP = ρgh. This derivation has a hidden assumption: the fluid is **incompressible** (constant ρ). For water and most engineering liquids this holds; for gases over large height changes, ρ varies with P and the equation becomes more complex. In differential form, dP/dz = −ρg, where z increases upward — the negative sign confirms that pressure decreases as you rise.

**Pascal's law** is a consequence of isotropy plus static equilibrium: a pressure change at any point is transmitted undiminished to every other point in a connected static fluid. This is the principle behind hydraulic systems. If you press with force F₁ on a piston of area A₁, the pressure increase ΔP = F₁/A₁ propagates through the fluid to a larger piston of area A₂, exerting force F₂ = ΔP·A₂ = F₁·(A₂/A₁). The force is amplified by the area ratio — a hydraulic jack converts a small force over a large stroke into a large force over a small stroke, conserving energy in the process.

A crucial nuance is the distinction between **absolute pressure** and **gauge pressure**. Absolute pressure is measured relative to a perfect vacuum. Gauge pressure is measured relative to the local atmospheric pressure — it can be positive (above atmospheric) or negative (below atmospheric, called vacuum pressure). When you inflate a tire to "35 psi," that is gauge pressure; the absolute pressure inside is 35 + 14.7 ≈ 50 psia. Forgetting this distinction when applying the hydrostatic equation causes errors at boundaries where you interface with the atmosphere. The hydrostatic paradox is also worth internalizing: pressure at the bottom of a tall narrow column of water equals the pressure at the bottom of a wide shallow tank at the same depth — the container shape is irrelevant. What matters is depth and fluid density alone.

