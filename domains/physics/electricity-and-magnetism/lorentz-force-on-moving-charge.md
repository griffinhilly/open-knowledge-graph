---
id: lorentz-force-on-moving-charge
title: Lorentz Force on Moving Charges
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: magnetic-field-intro
  type: hard
- id: magnetic-field-and-lorentz-force
  type: hard
- id: cross-product
  type: hard
builds-toward:
- force-on-current-carrying-conductor
- cyclotron-motion-and-frequency
tags:
- magnetism
- forces
- charged particles
stage: formal-systems
status: draft
---

# Lorentz Force on Moving Charges

## Core Idea
The force on a moving charged particle in a magnetic field is F = q(v × B), perpendicular to both velocity and field. This force does no work, changing only direction, not speed. The magnitude is F = qvB sin θ. This is the fundamental mechanism by which magnetic fields deflect moving charges.

## Explainer

From your study of the cross product, you know that v × B produces a vector perpendicular to both v and B, with magnitude |v||B|sinθ where θ is the angle between them. The **Lorentz magnetic force** F = q(v × B) is exactly this cross product scaled by the charge q. The direction follows the right-hand rule: point fingers along v, curl toward B, and the thumb points in the direction of the force on a positive charge. For a negative charge, the force is reversed.

The most striking feature of the magnetic force is that it does no work. Work requires a force component along the direction of motion, but F = q(v × B) is always perpendicular to v by definition of the cross product. If no work is done, the kinetic energy (and therefore speed) cannot change. The magnetic force can only redirect a particle — it acts as a pure steering force. This has a remarkable consequence: a charged particle moving perpendicular to a uniform magnetic field undergoes **uniform circular motion**. The magnetic force provides the centripetal acceleration, giving mv²/r = qvB, so the orbital radius is r = mv/(qB). Faster particles and heavier particles orbit in larger circles; stronger fields produce tighter orbits.

The magnitude formula F = qvB sinθ tells you that the force is maximum when v ⊥ B (sinθ = 1) and zero when v ∥ B (sinθ = 0). A particle moving exactly parallel to the field experiences no magnetic force at all — only when it has a component of velocity perpendicular to B does the force appear. This selectivity makes the Lorentz force geometrically sensitive in ways that an electric force is not.

These principles underlie technologies from mass spectrometers (where radius r = mv/qB separates ions by mass-to-charge ratio) to particle accelerators (where magnetic fields bend high-energy beams around circular tracks) to the aurora borealis (where Earth's magnetic field funnels charged solar wind particles toward the poles). The combination of the electric and magnetic contributions, **F = q(E + v × B)**, is the complete Lorentz force law, unifying how charged particles respond to all electromagnetic fields.
