---
id: rigid-body-work-energy
title: Work-Energy Methods for Rigid Bodies
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: work-energy-particles
  type: hard
- id: mass-moment-of-inertia
  type: hard
builds-toward:
- virtual-work-method
tags:
- dynamics
- work
- energy
- kinetic energy
- rigid bodies
- rotation
stage: formal-systems
status: draft
---

# Work-Energy Methods for Rigid Bodies

## Core Idea
The work-energy theorem for a rigid body states that the net work done by all external forces and couples equals the change in the body's total kinetic energy. For planar motion, the kinetic energy has two parts: translational KE = 1/2 * m * v_G^2 and rotational KE = 1/2 * I_G * omega^2, giving T = 1/2 * m * v_G^2 + 1/2 * I_G * omega^2. For pure rotation about a fixed point O, this simplifies to T = 1/2 * I_O * omega^2. Work is done by forces moving through displacements (U_F = integral F . ds) and by couples rotating through angles (U_M = integral M d(theta)). Forces at fixed points (pins, rolling contact with no slip) do no work. Conservative systems (gravity, springs) permit energy conservation: T_1 + V_1 = T_2 + V_2. This method is especially powerful for multi-body systems connected by pins and rolling contacts, where internal constraint forces do no net work.

## How It's Best Learned
Identify every force and determine whether it does work (force moves through a displacement) or not (force at a stationary contact point). For rolling without slip, note that the friction force at the contact does no work. Write the kinetic energy at two states and equate the work-energy balance. For systems with multiple connected bodies, sum the kinetic energies of all bodies and account for all external work terms in a single equation.

## Common Misconceptions
- Forgetting the rotational kinetic energy term 1/2 * I_G * omega^2 — a rolling or rotating body has kinetic energy from both translation and rotation.
- Assuming friction always does work — for rolling without slip, the contact point has zero velocity, so friction does no work despite being nonzero.
- Double-counting internal constraint forces at pins connecting two rigid bodies — Newton's third law ensures these internal forces cancel when the system work-energy equation is written.
