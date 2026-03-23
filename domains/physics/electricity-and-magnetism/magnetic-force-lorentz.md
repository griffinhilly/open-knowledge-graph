---
id: magnetic-force-lorentz
title: Magnetic Force on Moving Charges (Lorentz Force)
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: conservation-of-electric-charge
  type: soft
- id: cross-product
  type: hard
builds-toward:
- magnetic-force-conductors
tags:
- lorentz-force
- magnetic
- motion
stage: formal-systems
status: validated
---

# Magnetic Force on Moving Charges (Lorentz Force)

## Core Idea
A charge q moving with velocity v⃗ in a magnetic field B⃗ experiences force F⃗ = q(v⃗ × B⃗). This force is perpendicular to both v⃗ and B⃗, so it does no work and cannot change particle speed—only direction. Particles move in circles perpendicular to B⃗ with radius r = mv/(qB), demonstrating the non-conservative nature of magnetic forces.

## Questions

```yaml
- question: "A proton moves through a uniform magnetic field. What happens to its kinetic energy?"
  type: multiple-choice
  options:
    - "It increases because the magnetic force does positive work in the direction of motion"
    - "It remains constant — the magnetic force is always perpendicular to the velocity and does no work"
    - "It decreases because the field redirects the proton and steals kinetic energy"
    - "It oscillates, alternately increasing and decreasing as the proton curves"
  answer: 1
  explanation: "Work equals force dotted with displacement: W = F⃗ · dr⃗. The magnetic force F⃗ = q(v⃗ × B⃗) is always perpendicular to v⃗ (a property of the cross product), and since the particle's displacement is always along v⃗, the dot product is always zero. No work is done, so kinetic energy — and therefore speed — cannot change. The magnetic force is a perpetual steering mechanism: it deflects the particle's direction without ever accelerating or decelerating it."

- question: "A particle accelerator must both increase a charged particle's energy and bend its path in a circle. How must it use electric and magnetic fields?"
  type: multiple-choice
  options:
    - "Use magnetic fields for energy gain; use electric fields for bending the circular path"
    - "Use only magnetic fields — they can do both since they exert force on moving charges"
    - "Use electric fields for energy gain; use magnetic fields for bending the path"
    - "Use only electric fields — magnetic fields cannot exert force on charged particles"
  answer: 2
  explanation: "Electric fields do work on charges (force parallel to motion is possible), so they can increase kinetic energy. Magnetic fields do no work, so they cannot increase kinetic energy — they can only change the direction of motion. This is why modern accelerators like synchrotrons use radiofrequency electric cavities to accelerate particles and strong dipole magnets to bend the beam in a closed circular path. Magnetic fields are perfect for steering precisely because they don't alter the particle's energy."

- question: "A stationary charged particle placed in a strong magnetic field will be accelerated by the magnetic force."
  type: true-false
  answer: false
  explanation: "The Lorentz magnetic force is F⃗ = q(v⃗ × B⃗). If the particle is stationary, v⃗ = 0, so F⃗ = 0 regardless of how strong B⃗ is. The magnetic force requires motion to exist at all — it is velocity-dependent. This is why magnetic fields alone cannot start a particle from rest; an electric field is needed to provide the initial impulse. Once the particle is moving, the magnetic force can redirect it but still cannot change its speed."

- question: "A charged particle moving exactly parallel to a magnetic field (velocity vector parallel to B⃗) experiences no magnetic force."
  type: true-false
  answer: true
  explanation: "The cross product v⃗ × B⃗ equals |v||B|sin θ, where θ is the angle between v⃗ and B⃗. When v⃗ ∥ B⃗, θ = 0° and sin 0° = 0, so the force is zero. The particle continues in a straight line at constant velocity — completely unaffected by the field. This is why charged particles spiral along magnetic field lines: the component of velocity parallel to B⃗ is unaffected, while the perpendicular component undergoes circular motion, combining to produce the helix."

- question: "Why does the magnetic force on a moving charge produce circular (or helical) motion rather than linear acceleration? Explain using the direction of the force relative to velocity."
  type: short-answer
  answer: "The magnetic force F⃗ = q(v⃗ × B⃗) is always perpendicular to the velocity (by the definition of the cross product). A force perpendicular to velocity changes the direction of motion but not its magnitude — this is precisely the condition for circular motion, where the centripetal force points radially inward while velocity remains tangential. Setting qvB = mv²/r gives the cyclotron radius r = mv/(qB). If there is also a velocity component along B⃗, that component is unaffected (force is zero for it), so the particle traces a helix."
  explanation: "This perpendicularity is the key geometric fact underlying all magnetic force effects. It also explains why magnetic forces do no work: power = F⃗ · v⃗ = 0 when F⃗ ⊥ v⃗. The cyclotron radius formula r = mv/(qB) has immediate practical applications: larger mass m means harder to deflect (larger radius), stronger field B means tighter curve (smaller radius). Mass spectrometers exploit this — different isotopes with different m/q ratios follow arcs of different radii, separating them spatially."
```

## Explainer

From your study of the cross product, you know that v⃗ × B⃗ produces a vector perpendicular to both inputs, with a magnitude of |v||B|sin θ where θ is the angle between them. The **Lorentz magnetic force** F⃗ = q(v⃗ × B⃗) puts this geometry directly into physics: a charged particle moving through a magnetic field gets pushed sideways — always sideways. The direction is given by the right-hand rule: point your fingers along v⃗, curl them toward B⃗, and your thumb points in the direction of the force on a positive charge. A negative charge feels the opposite direction.

The most profound consequence of the perpendicularity is that **the magnetic force does no work**. Work is force dotted with displacement, W = F⃗·dr⃗. But the displacement of a particle is always along its velocity, and the force is always perpendicular to the velocity, so the dot product is always zero. Magnetic forces are a perpetual steering mechanism — they can redirect particles without ever speeding them up or slowing them down. This is why magnetic fields alone cannot accelerate particles from rest; particle accelerators use electric fields to gain energy and magnetic fields to bend the beam.

What happens when a charge enters a uniform magnetic field perpendicular to B⃗? The force is always perpendicular to the velocity, which continuously changes the velocity's direction without changing its magnitude. This is precisely the condition for **circular motion**: the Lorentz force provides the centripetal acceleration. Setting qvB = mv²/r and solving gives the **cyclotron radius** r = mv/(qB). Faster particles curve more gently (larger r); stronger fields bend them more tightly (smaller r); heavier particles are harder to deflect (larger m means larger r). If the particle has a velocity component along B⃗, that component is unaffected, so the particle traces a helix — a combination of circular motion perpendicular to B⃗ and straight-line motion along it.

This combination of steering ability and force-direction rule is exploited throughout physics and engineering. Mass spectrometers separate ions by their cyclotron radius — different m/q ratios give different circular arcs, allowing identification of isotopes. Cyclotrons and synchrotrons use it to guide particle beams. The aurora borealis results from charged particles spiraling along Earth's magnetic field lines and funneling toward the poles. As you go on to study forces on current-carrying conductors, you will apply the same F = qv × B logic to many drifting charges simultaneously, recovering the macroscopic force on wires.
