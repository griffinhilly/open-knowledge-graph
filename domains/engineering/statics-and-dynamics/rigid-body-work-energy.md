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
- id: work-energy-systems-analysis
  type: soft
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
status: validated
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

## Questions

```yaml
- question: "A uniform disk rolls without slipping down an inclined plane. When applying the work-energy theorem to find its speed at the bottom, what is the work done by the friction force at the contact point?"
  type: multiple-choice
  options:
    - "W_friction = μ_k × N × d, opposing motion and reducing the final speed"
    - "W_friction > 0 because friction provides the torque that generates rotational kinetic energy"
    - "W_friction = 0 because the contact point has zero instantaneous velocity in rolling without slip"
    - "W_friction equals the rotational kinetic energy gained, since friction is its source"
  answer: 2
  explanation: "Work equals force times the displacement of the point of application. For rolling without slip, the contact point is instantaneously at rest (zero velocity), so its displacement is zero and friction does zero work. This is why energy conservation applies directly to rolling problems: only gravity (and springs, if present) appear as work terms. The common misconception (options B and D) is that because friction causes rotation, it must do work — but work requires displacement, and the contact point has none."

- question: "A system of two rigid bodies is connected by a smooth pin joint. When you write the work-energy equation for the entire system, what happens to the forces at the pin?"
  type: multiple-choice
  options:
    - "They must be included as separate external work terms for each body"
    - "They cancel completely — Newton's third law pairs act at the same point, so their net work is zero"
    - "They partially cancel, leaving a residual term proportional to the pin's angular displacement"
    - "They must be computed as constraint forces using the Lagrange multiplier method"
  answer: 1
  explanation: "By Newton's third law, the pin exerts equal and opposite forces on the two connected bodies. Crucially, both forces act at the same point (the pin), so both act through the same displacement. Net work = F·ds + (−F)·ds = 0. This is why the work-energy method is so efficient for multi-body systems: all internal constraint forces at pins vanish from the equation automatically, leaving only external forces (gravity, applied loads, springs)."

- question: "For a rigid body undergoing general planar motion (both translating and rotating), the total kinetic energy includes both a translational term (½mv_G²) and a rotational term (½I_Gω²) — omitting either term gives the wrong answer."
  type: true-false
  answer: true
  explanation: "In general planar motion, the center of mass G moves through space (translational KE = ½mv_G²) while the body simultaneously spins about G (rotational KE = ½I_Gω²). These are independent contributions — a bowling ball rolling down a lane has both, and both must be included. The common error of using KE = ½mv² alone (as for a particle) underestimates the total kinetic energy and gives incorrect velocities."

- question: "When a disk rolls without slipping on a surface, the friction force does positive work on the disk because it is the torque source responsible for the disk's rotational kinetic energy."
  type: true-false
  answer: false
  explanation: "Even though friction provides the torque that maintains rolling, it does zero work because its point of application (the contact point) is instantaneously at rest in rolling without slip. The rotational kinetic energy does not come from friction doing work — it comes from the conversion of gravitational potential energy (for a body rolling down a slope). This distinction is critical: a torque can cause rotation without doing work, provided the point of application has no velocity."

- question: "Explain why forces at fixed pin joints and rolling contacts do no work, and why this makes the work-energy method especially powerful for multi-body systems."
  type: short-answer
  answer: "Work requires a force acting through a nonzero displacement. A fixed pin joint has a stationary attachment point — the pin itself does not move — so any reaction force there has zero displacement and does zero work. For rolling without slip, the contact point is instantaneously at rest (zero velocity, zero displacement), so the friction force there also does zero work. In multi-body systems connected by pins and rolling contacts, there are many internal constraint forces, but all of them drop out of the work-energy equation automatically. The result is a single scalar equation relating kinetic energies at two states to the work done only by external forces — far simpler than Newton-Euler methods, which require free-body diagrams and vector equations for every body."
  explanation: "This is why the work-energy method is especially preferred for systems with multiple connected rigid bodies: the constraint forces that complicate Newton-Euler analysis simply vanish. You sum the kinetic energies of all bodies (translational + rotational for each), sum the external work terms (gravity, springs, applied forces), and equate them. Internal constraint forces never appear."
```

## Explainer

From your study of work-energy methods for particles, you know the core idea: the net work done on a particle equals its change in kinetic energy, W_net = ΔKE = ½mv₂² − ½mv₁². This is powerful because it bypasses forces and accelerations — you only need to account for work at two instants. Rigid bodies keep this same elegance but add a new complication: they can rotate as well as translate, and rotation carries kinetic energy too.

A rigid body in general planar motion has two independent types of kinetic energy. The **translational kinetic energy** ½mv_G² accounts for the motion of the center of mass G moving through space at velocity v_G. The **rotational kinetic energy** ½I_G·ω² accounts for the body spinning about G at angular velocity ω, with I_G being the **mass moment of inertia** about G (which you already know from your prerequisite — it measures how mass is distributed relative to the axis of rotation). The total kinetic energy is simply their sum: T = ½mv_G² + ½I_G·ω². For a body rotating about a fixed point O, these two terms collapse into a single expression T = ½I_O·ω² using the parallel-axis theorem.

The work side of the equation has a subtle but important feature: **not all forces do work**. Work requires a force acting through a displacement. At a smooth pin joint, the reaction forces do exist — but their point of application doesn't move (the pin is fixed), so they do zero work. For a body rolling without slip on a surface, the contact point is instantaneously at rest (that's what "no slip" means), so the friction force at the contact does zero work even though the friction force itself may be nonzero and physically important. This is the key to solving multi-body problems: pin-connected and rolling systems have many constraint forces, but they all drop out of the work-energy equation automatically.

For a system of connected rigid bodies, write T as the sum of kinetic energies of all bodies and W as the sum of all external work terms. Internal forces at pins between bodies form Newton's-third-law pairs — equal, opposite, and acting through the same point — so their net work is zero and they disappear from the equation entirely. The result is a single scalar equation relating the initial state, the final state, and all the external work done in between. This is particularly efficient compared to Newton-Euler equations, which would require separate free-body diagrams and equations for every body in the system.

