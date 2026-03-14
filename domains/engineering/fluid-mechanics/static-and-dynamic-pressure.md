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
stage: formal-systems
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
