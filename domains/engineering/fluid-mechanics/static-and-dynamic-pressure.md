---
id: static-and-dynamic-pressure
title: Static and Dynamic Pressure
domain: engineering
course: fluid-mechanics
prerequisites:
- id: pressure-and-forces-in-fluids
  type: hard
- id: bernoullis-equation
  type: soft
builds-toward:
- pitot-tube-velocity-measurement
- absolute-gauge-atmospheric-pressure
tags:
- pressure
- flow
- measurement
stage: advanced
status: draft
---

# Static and Dynamic Pressure

## Core Idea
Static pressure is the pressure of a fluid at rest or the component of pressure independent of motion, while dynamic pressure represents the kinetic energy per unit volume of moving fluid. The sum of static and dynamic pressure (plus elevation effects) is constant along a streamline for incompressible inviscid flow, forming the basis of Bernoulli's equation.

## How It's Best Learned
Compare a manometer reading taken when a Pitot tube faces the flow (stagnation pressure) versus when a static pressure tap is used perpendicular to flow. The difference directly demonstrates dynamic pressure and Bernoulli's principle in action.

## Common Misconceptions
- Dynamic pressure is a different type of pressure added to static pressure (it is actually the kinetic energy density per unit volume, derived from Bernoulli's energy balance).
- Static pressure is zero in a moving fluid (static pressure is always present; it is measured by pressure taps perpendicular to flow).

## Explainer

From your study of pressure in fluids, you know that a fluid exerts force on any surface it contacts, and that pressure is that force per unit area. In a stationary fluid, pressure is the same in all directions at a given depth — it's isotropic. When the fluid moves, this clean picture breaks down in one important way: the pressure you measure depends on whether your measurement surface faces the flow or is aligned with it. That distinction is the heart of this topic.

**Static pressure** is the pressure the fluid exerts on a surface that moves with the fluid — or equivalently, on a surface oriented parallel to the flow direction. It represents the thermal and intermolecular activity of the fluid molecules, independent of their bulk motion. You measure static pressure with a tap drilled perpendicular to the pipe wall, so the flowing fluid slides past it without being slowed down. In the absence of any flow, static pressure is the only pressure; it matches the ambient or gauge pressure you already understand.

**Dynamic pressure** is the additional pressure that arises from bringing a moving fluid to rest. When flow is decelerated to zero velocity — for example, at the front face of a blunt object or inside a forward-facing tube — kinetic energy converts to pressure energy. The amount of pressure gained equals ½ρV², where ρ is the fluid density and V is the flow speed. This quantity has units of pressure (Pa) but physically represents the kinetic energy per unit volume of the moving fluid. It is not "added" to the static pressure in the sense of an extra force; rather, Bernoulli's equation tells us that when velocity decreases, pressure increases by exactly this amount.

The sum of static pressure and dynamic pressure is **stagnation pressure** (also called total pressure): P_stag = P_static + ½ρV². Bernoulli's equation is simply a statement that stagnation pressure is conserved along a streamline in ideal flow. A Pitot tube measures stagnation pressure at its tip (flow comes to rest there) while a separate static port measures static pressure; the velocity follows from V = √(2(P_stag − P_static)/ρ). This is the operational definition that makes the distinction between static and dynamic pressure practically useful — every velocity measurement in a flowing fluid exploits this exact relationship.
