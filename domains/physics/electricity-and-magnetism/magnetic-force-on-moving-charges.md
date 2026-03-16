---
id: magnetic-force-on-moving-charges
title: Magnetic Force on Moving Charges
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: magnetic-field-intro
  type: hard
- id: cross-product
  type: hard
- id: circular-motion-dynamics
  type: soft
builds-toward:
- magnetic-force-on-current-carrying-conductors
- charged-particle-motion-in-fields
tags:
- Lorentz-force
- cyclotron
- magnetic-force
- cross-product
stage: formal-systems
status: validated
---

# Magnetic Force on Moving Charges

## Core Idea
The magnetic force on a charge q moving with velocity v in field B is F = qv × B. The magnitude is F = qvB sin θ, where θ is the angle between v and B; it is maximum when v ⊥ B and zero when v ∥ B. Since F ⊥ v always, the magnetic force does no work and a charge in a uniform magnetic field moves in a circle with radius r = mv/(|q|B) — the cyclotron radius — completing circles at the cyclotron frequency f = |q|B/(2πm).

## How It's Best Learned
Apply the right-hand rule (or left-hand rule for negative charges) systematically: point fingers in v direction, curl toward B, thumb gives F for positive charge. Practice determining the circular orbit radius for protons, electrons, and other particles in given fields.

## Common Misconceptions
- The magnetic force cannot do work — it changes direction but never speed.
- For negative charges, the force is opposite to v × B.
- Circular motion in a magnetic field is not the same as orbital mechanics — no central force potential is involved.

## Explainer

From your study of magnetic fields, you know that a magnetic field B exists in space and can be measured by its effect on moving charges. The **Lorentz force law** F = qv × B is the fundamental statement of how. The cross product tells you both magnitude and direction: the force is perpendicular to both the velocity and the field simultaneously. Recall from your prerequisites that the cross product v × B has magnitude |v||B| sin θ and points along a direction given by the right-hand rule — point fingers along v, curl toward B, and the thumb gives F for a positive charge.

The perpendicularity of F to v has an immediate and profound consequence: the magnetic force can never do work on a charged particle. Work is W = F · d = F · v dt, and since F ⊥ v always, this dot product is identically zero. The kinetic energy — and therefore the speed — of a charged particle in a magnetic field never changes. What the magnetic force *can* do is continuously redirect the velocity vector. A particle entering a uniform magnetic field perpendicular to the field lines experiences a force that is always perpendicular to its motion, exactly the condition for uniform **circular motion**. The magnetic force plays the role of the centripetal force: qvB = mv²/r, which gives the **cyclotron radius** r = mv/(|q|B). A heavier particle or a faster particle traces a larger circle; a stronger field or larger charge gives a tighter circle.

The **cyclotron frequency** f = |q|B/(2πm) is independent of the particle's speed — a remarkable fact that is the operating principle of the cyclotron particle accelerator. No matter how fast the particle moves, it completes one orbit in the same time T = 1/f. This allows the accelerator's oscillating electric field to stay in synchrony with the particle through many orbits, giving it an energy kick each time it crosses the gap, until relativistic effects become important and the cyclotron frequency starts to shift.

For negative charges, the sign of q reverses the direction of F = qv × B: where a proton would be deflected upward, an electron is deflected downward. This is why in cloud chamber photographs of cosmic ray tracks in a magnetic field, positive and negative particles curve in opposite directions — a reliable signature of charge sign. In practice, the right-hand rule applied to v × B gives F for positive charges; simply flip the direction for negative ones.
