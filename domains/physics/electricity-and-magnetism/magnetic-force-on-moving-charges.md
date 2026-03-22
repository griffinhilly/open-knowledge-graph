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

## Questions

```yaml
- question: "A proton moves in a circle inside a uniform magnetic field at speed v. You double the magnetic field strength. What happens to the proton's speed and the radius of its circular orbit?"
  type: multiple-choice
  options:
    - "Speed doubles; radius stays the same"
    - "Speed stays the same; radius doubles"
    - "Speed stays the same; radius halves"
    - "Speed doubles; radius halves"
  answer: 2
  explanation: "The magnetic force does no work, so it cannot change the proton's kinetic energy or speed — speed stays the same regardless of field strength. The cyclotron radius is r = mv/(|q|B); doubling B while keeping m, v, and q constant halves r. This question targets the misconception that a stronger magnetic force means a faster particle. The force changes direction only, not magnitude of velocity."

- question: "A student argues that a magnetic field can accelerate a charged particle because 'the Lorentz force acts on the particle and pushes it forward.' What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing — the Lorentz force does accelerate the particle by changing its velocity vector"
    - "The Lorentz force is always perpendicular to velocity, so it changes direction but does zero work and cannot increase speed"
    - "The student is right only for positive charges; negative charges are decelerated by magnetic fields"
    - "Magnetic forces only act on stationary charges; moving charges experience electric forces instead"
  answer: 1
  explanation: "The key insight is that 'acceleration' in everyday language (getting faster) differs from the physics definition (any change in velocity vector). The magnetic force F = qv × B is always perpendicular to v, so W = F · v dt = 0 at every instant — the force does no work and the particle's speed never changes. The Lorentz force does cause acceleration in the physics sense (changing direction), but it cannot increase kinetic energy. This is what makes magnetic confinement possible: you can steer charged particles without energizing them."

- question: "The cyclotron frequency at which a charged particle completes orbits in a uniform magnetic field is independent of the particle's speed."
  type: true-false
  answer: true
  explanation: "The cyclotron frequency f = |q|B/(2πm) depends only on the charge, field strength, and mass — not on speed. Although a faster particle has a larger orbit radius (r = mv/|q|B), it also travels a proportionally longer circumference, and these two effects cancel exactly. This remarkable property is what makes the cyclotron particle accelerator work: the oscillating electric field can stay in fixed synchrony with the orbiting particle across many acceleration cycles, because the orbital period T = 1/f doesn't change as the particle speeds up (until relativistic effects intervene)."

- question: "A magnetic field does work on a moving charged particle whenever the particle changes direction, because work is force times distance."
  type: true-false
  answer: false
  explanation: "This is the central misconception. Work is W = F · d, which is the dot product — only the component of force parallel to displacement contributes. Since the magnetic force F = qv × B is always perpendicular to v (the direction of motion), every instantaneous dot product F · v = 0. No work is ever done, regardless of how sharply the particle's direction changes. The particle's speed (and kinetic energy) remain constant throughout circular motion in a magnetic field."

- question: "Why can the magnetic force never do work on a charged particle, even though that force is clearly causing the particle to move in a curved path?"
  type: short-answer
  answer: "Work requires a force component parallel to the displacement (W = F · d). The magnetic force F = qv × B is always perpendicular to the velocity v by the definition of the cross product. Since the force is perpendicular to the direction of motion at every instant, the dot product F · v = 0 always, and no work is ever done. The force continuously redirects the velocity vector — changing direction — without ever adding energy to the particle. Speed and kinetic energy remain constant."
  explanation: "Students often conflate 'exerting a force on a moving object' with 'doing work on it.' Work requires the force to have a component in the direction of motion. The geometric property of the cross product — that v × B ⊥ v always — makes the magnetic force categorically incapable of doing work. This is not an approximation or special case; it holds exactly at every instant of the motion."
```

## Explainer

From your study of magnetic fields, you know that a magnetic field B exists in space and can be measured by its effect on moving charges. The **Lorentz force law** F = qv × B is the fundamental statement of how. The cross product tells you both magnitude and direction: the force is perpendicular to both the velocity and the field simultaneously. Recall from your prerequisites that the cross product v × B has magnitude |v||B| sin θ and points along a direction given by the right-hand rule — point fingers along v, curl toward B, and the thumb gives F for a positive charge.

The perpendicularity of F to v has an immediate and profound consequence: the magnetic force can never do work on a charged particle. Work is W = F · d = F · v dt, and since F ⊥ v always, this dot product is identically zero. The kinetic energy — and therefore the speed — of a charged particle in a magnetic field never changes. What the magnetic force *can* do is continuously redirect the velocity vector. A particle entering a uniform magnetic field perpendicular to the field lines experiences a force that is always perpendicular to its motion, exactly the condition for uniform **circular motion**. The magnetic force plays the role of the centripetal force: qvB = mv²/r, which gives the **cyclotron radius** r = mv/(|q|B). A heavier particle or a faster particle traces a larger circle; a stronger field or larger charge gives a tighter circle.

The **cyclotron frequency** f = |q|B/(2πm) is independent of the particle's speed — a remarkable fact that is the operating principle of the cyclotron particle accelerator. No matter how fast the particle moves, it completes one orbit in the same time T = 1/f. This allows the accelerator's oscillating electric field to stay in synchrony with the particle through many orbits, giving it an energy kick each time it crosses the gap, until relativistic effects become important and the cyclotron frequency starts to shift.

For negative charges, the sign of q reverses the direction of F = qv × B: where a proton would be deflected upward, an electron is deflected downward. This is why in cloud chamber photographs of cosmic ray tracks in a magnetic field, positive and negative particles curve in opposite directions — a reliable signature of charge sign. In practice, the right-hand rule applied to v × B gives F for positive charges; simply flip the direction for negative ones.
