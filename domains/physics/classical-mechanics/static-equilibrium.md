---
id: static-equilibrium
title: Static Equilibrium
domain: physics
course: classical-mechanics
prerequisites:
- id: free-body-diagrams
  type: hard
- id: torque
  type: hard
- id: newtons-first-law
  type: hard
- id: systems-elimination
  type: soft
- id: vectors-in-two-dimensions
  type: soft
builds-toward:
- rotational-dynamics
tags:
- equilibrium
- static
- torque
- force-balance
stage: formal-systems
status: validated
---

# Static Equilibrium

## Core Idea
A rigid body is in static equilibrium when both the net force and the net torque on it are zero: ΣF = 0 and Στ = 0. The torque equation provides additional constraints beyond force balance and is essential for determining where forces act (e.g., normal force position under a beam). The choice of pivot for computing torques is arbitrary — any convenient point may be chosen, often one where unknown forces are applied to eliminate them from the equation.

## How It's Best Learned
Solve beam and ladder problems: draw the FBD, write ΣFx = 0, ΣFy = 0, and Στ = 0 about a strategic pivot. Practice choosing the pivot wisely — placing it at the point of application of an unknown force often simplifies algebra.

## Common Misconceptions
- Thinking the torque pivot must be a physical support point: it can be any point.
- Setting up torque equations without specifying the sign convention for clockwise vs. counterclockwise.
