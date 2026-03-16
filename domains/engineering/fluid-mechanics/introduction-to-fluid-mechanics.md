---
id: introduction-to-fluid-mechanics
title: Introduction to Fluid Mechanics
domain: engineering
course: fluid-mechanics
prerequisites: []
builds-toward:
- pressure-and-forces-in-fluids
- static-and-dynamic-pressure
tags:
- fundamentals
- overview
stage: formal-systems
status: draft
---

# Introduction to Fluid Mechanics

## Core Idea
Fluid mechanics is the study of fluids (liquids and gases) in motion and at rest, with applications ranging from pipe flow and hydraulic systems to aerodynamics and weather prediction. The field combines conservation principles from physics with empirical relationships developed from experimentation. Understanding fluid behavior is essential for engineering design in mechanical, civil, chemical, and aerospace industries.

## How It's Best Learned
Start with everyday examples of fluids in motion: water flowing from a tap, air movement over a wing, pressure in a hydraulic system. Then build theoretical understanding using the three fundamental conservation laws: mass, momentum, and energy.

## Common Misconceptions
- Fluids must be liquids (gases are also fluids).
- Pressure acts only downward or in one direction (it acts equally in all directions in static fluids).
- All fluids behave the same way (non-Newtonian fluids have viscosity that depends on shear rate).

## Explainer

A **fluid** is any substance that deforms continuously when a shear stress is applied — it flows rather than holding its shape. This is what distinguishes fluids from solids: a solid block resists shear (a tangential force) by deforming a fixed amount and stopping, while a fluid keeps moving as long as the force is applied. Both liquids and gases meet this definition. The practical difference between them is compressibility: liquids are nearly incompressible (their density barely changes under pressure), while gases compress significantly. For many engineering problems — water in pipes, slow airflows — the incompressible assumption applies even to gases, which simplifies the mathematics enormously.

Two properties define how a fluid behaves in most engineering contexts: **density** (mass per unit volume, ρ) and **viscosity** (resistance to internal flow, μ). Honey is highly viscous — it resists shearing strongly — while water and air have low viscosity. Viscosity is what causes friction between layers of fluid moving at different speeds, and it determines whether flow will be smooth and orderly (**laminar**) or chaotic and mixing (**turbulent**). The dimensionless Reynolds number Re = ρVD/μ captures this competition between inertial forces (driving turbulence) and viscous forces (suppressing it). Low Re means laminar flow; high Re means turbulent. This single number appears in nearly every fluid mechanics problem.

The entire field rests on three conservation laws applied to fluids: conservation of **mass** (what flows in must flow out or accumulate), conservation of **momentum** (forces equal the rate of change of momentum in the fluid), and conservation of **energy** (pressure, velocity, and elevation trade off as fluid moves). These are not new physics — they are Newton's laws and thermodynamics, adapted for continuous flowing media. The difficulty in fluid mechanics is not the underlying physics but the mathematics of applying these laws to complex geometries, and the rich variety of flow regimes they produce.

Fluid mechanics appears everywhere in engineering. Water supply systems, irrigation, and sewage rely on pipe flow analysis. Aircraft wings generate lift because of pressure differences created by air moving faster over the curved upper surface. Chemical reactors depend on mixing and flow distribution. Weather systems and ocean currents are governed by the same equations at planetary scale. The tools you develop here — pressure analysis, flow equations, dimensionless numbers, conservation principles — form the foundation for all of these applications. Start with the simplest cases (static fluids, then steady pipe flows) and the generalizations will follow naturally.
