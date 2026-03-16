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

## Explainer

From your study of work-energy methods for particles, you know the core idea: the net work done on a particle equals its change in kinetic energy, W_net = ΔKE = ½mv₂² − ½mv₁². This is powerful because it bypasses forces and accelerations — you only need to account for work at two instants. Rigid bodies keep this same elegance but add a new complication: they can rotate as well as translate, and rotation carries kinetic energy too.

A rigid body in general planar motion has two independent types of kinetic energy. The **translational kinetic energy** ½mv_G² accounts for the motion of the center of mass G moving through space at velocity v_G. The **rotational kinetic energy** ½I_G·ω² accounts for the body spinning about G at angular velocity ω, with I_G being the **mass moment of inertia** about G (which you already know from your prerequisite — it measures how mass is distributed relative to the axis of rotation). The total kinetic energy is simply their sum: T = ½mv_G² + ½I_G·ω². For a body rotating about a fixed point O, these two terms collapse into a single expression T = ½I_O·ω² using the parallel-axis theorem.

The work side of the equation has a subtle but important feature: **not all forces do work**. Work requires a force acting through a displacement. At a smooth pin joint, the reaction forces do exist — but their point of application doesn't move (the pin is fixed), so they do zero work. For a body rolling without slip on a surface, the contact point is instantaneously at rest (that's what "no slip" means), so the friction force at the contact does zero work even though the friction force itself may be nonzero and physically important. This is the key to solving multi-body problems: pin-connected and rolling systems have many constraint forces, but they all drop out of the work-energy equation automatically.

For a system of connected rigid bodies, write T as the sum of kinetic energies of all bodies and W as the sum of all external work terms. Internal forces at pins between bodies form Newton's-third-law pairs — equal, opposite, and acting through the same point — so their net work is zero and they disappear from the equation entirely. The result is a single scalar equation relating the initial state, the final state, and all the external work done in between. This is particularly efficient compared to Newton-Euler equations, which would require separate free-body diagrams and equations for every body in the system.

