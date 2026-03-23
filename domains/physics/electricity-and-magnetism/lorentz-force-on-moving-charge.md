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
status: validated
---

# Lorentz Force on Moving Charges

## Core Idea
The force on a moving charged particle in a magnetic field is F = q(v × B), perpendicular to both velocity and field. This force does no work, changing only direction, not speed. The magnitude is F = qvB sin θ. This is the fundamental mechanism by which magnetic fields deflect moving charges.

## Questions

```yaml
- question: "A proton moves in the +x direction through a region where the magnetic field points in the +x direction. What magnetic force does the proton experience?"
  type: multiple-choice
  options:
    - "A force in the +y direction, perpendicular to the proton's motion"
    - "A force in the −x direction, opposing the proton's motion"
    - "No magnetic force, because the velocity and field are parallel"
    - "A force whose direction depends on the proton's speed"
  answer: 2
  explanation: "The magnetic force is F = q(v × B). When v and B are parallel (both in the +x direction), their cross product is zero: v × B = 0. The magnetic force is identically zero for any charge moving parallel to the field, regardless of speed or charge magnitude. Only the component of velocity perpendicular to B contributes to the force. This is why particles moving parallel to a magnetic field are undeflected — a key geometric property of the Lorentz force."

- question: "A proton moves perpendicular to a uniform magnetic field, undergoing circular motion with orbital radius r. If the magnetic field strength is doubled while the proton's speed remains constant, what happens to the orbital radius?"
  type: multiple-choice
  options:
    - "The radius doubles, because stronger fields create larger orbits"
    - "The radius halves, because r = mv/(qB) and B appears in the denominator"
    - "The radius stays the same, because the speed is unchanged"
    - "The radius increases by √2, because force scales with the square root of field strength"
  answer: 1
  explanation: "From the circular motion condition mv²/r = qvB, solving for r gives r = mv/(qB). The radius is inversely proportional to B — doubling the field strength halves the radius. A stronger field exerts a larger centripetal force, curving the path more tightly. This relationship is the operating principle of mass spectrometers: ions of different mass but same charge and speed follow different radii, allowing separation by mass-to-charge ratio."

- question: "The magnetic force on a moving charge can change the charge's direction of motion without changing its kinetic energy."
  type: true-false
  answer: true
  explanation: "The magnetic force F = q(v × B) is always perpendicular to the velocity v by the definition of the cross product. Since work = F · d, and force is always perpendicular to displacement, the work done by the magnetic force is always zero. Zero work means no change in kinetic energy, and therefore no change in speed. The magnetic force is a pure steering force — it redirects without accelerating or decelerating. This is why a charged particle in a uniform perpendicular field moves in a circle at constant speed."

- question: "Doubling the strength of a magnetic field causes a charged particle moving in a circular orbit to speed up, because the particle experiences a stronger force."
  type: true-false
  answer: false
  explanation: "The magnetic force never changes a particle's speed — it can only change direction. Even though a stronger field exerts a larger force and curves the path more tightly (smaller radius), the force remains perpendicular to velocity at every instant and does zero work. The particle moves faster around a tighter circle in the same amount of time — specifically, the orbital period T = 2πm/(qB) decreases with stronger field, but the speed v = qBr/m stays determined by initial conditions, not field strength."

- question: "Why does the magnetic force F = q(v × B) do no work on a moving charge, and what consequence does this have for how the charge moves?"
  type: short-answer
  answer: "The cross product v × B is always perpendicular to v. Since the force is perpendicular to the velocity (and thus to the displacement at every instant), the dot product F · v = 0, meaning the rate of work done is identically zero. Zero work means no change in kinetic energy and therefore no change in speed. The consequence is that the magnetic force can only steer — it changes the direction of motion but not the magnitude. A charged particle moving perpendicular to a uniform field follows uniform circular motion: constant speed, changing direction."
  explanation: "This is the most important conceptual point about magnetic forces: unlike electric forces, which can accelerate and decelerate charges, magnetic forces are purely geometric — they act as a compass that redirects the particle without adding or removing energy. This is why magnetic confinement in particle accelerators and plasma reactors can steer high-energy beams without changing their energy, and why the aurora borealis forms as solar wind particles are funneled along magnetic field lines toward the poles without being slowed down."
```

## Explainer

From your study of the cross product, you know that v × B produces a vector perpendicular to both v and B, with magnitude |v||B|sinθ where θ is the angle between them. The **Lorentz magnetic force** F = q(v × B) is exactly this cross product scaled by the charge q. The direction follows the right-hand rule: point fingers along v, curl toward B, and the thumb points in the direction of the force on a positive charge. For a negative charge, the force is reversed.

The most striking feature of the magnetic force is that it does no work. Work requires a force component along the direction of motion, but F = q(v × B) is always perpendicular to v by definition of the cross product. If no work is done, the kinetic energy (and therefore speed) cannot change. The magnetic force can only redirect a particle — it acts as a pure steering force. This has a remarkable consequence: a charged particle moving perpendicular to a uniform magnetic field undergoes **uniform circular motion**. The magnetic force provides the centripetal acceleration, giving mv²/r = qvB, so the orbital radius is r = mv/(qB). Faster particles and heavier particles orbit in larger circles; stronger fields produce tighter orbits.

The magnitude formula F = qvB sinθ tells you that the force is maximum when v ⊥ B (sinθ = 1) and zero when v ∥ B (sinθ = 0). A particle moving exactly parallel to the field experiences no magnetic force at all — only when it has a component of velocity perpendicular to B does the force appear. This selectivity makes the Lorentz force geometrically sensitive in ways that an electric force is not.

These principles underlie technologies from mass spectrometers (where radius r = mv/qB separates ions by mass-to-charge ratio) to particle accelerators (where magnetic fields bend high-energy beams around circular tracks) to the aurora borealis (where Earth's magnetic field funnels charged solar wind particles toward the poles). The combination of the electric and magnetic contributions, **F = q(E + v × B)**, is the complete Lorentz force law, unifying how charged particles respond to all electromagnetic fields.
