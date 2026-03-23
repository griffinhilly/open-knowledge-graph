---
id: magnetic-field-and-lorentz-force
title: Magnetic Field and the Lorentz Force
domain: physics
course: electrodynamics
prerequisites:
- id: classical-mechanics
  type: hard
- id: multivariable-calculus
  type: hard
builds-toward:
- vector-potential-and-curl
- faraday-law-of-induction
tags:
- magnetism
- field-theory
- forces
stage: expert
status: draft
---

# Magnetic Field and the Lorentz Force

## Core Idea
The Lorentz force F = q(E + v × B) describes the force on a charge moving in electromagnetic fields. The magnetic force is always perpendicular to velocity, doing no work but changing direction. This defines the magnetic field B operationally.

## Questions

```yaml
- question: "A proton moves eastward (+x) through a region where a uniform magnetic field points northward (+y). Using the Lorentz force law, the magnetic force on the proton points in which direction?"
  type: multiple-choice
  options:
    - "Northward — the force aligns with the field"
    - "Eastward — the force aligns with the velocity"
    - "Upward (+z) — perpendicular to both velocity and field by the right-hand rule"
    - "Zero — the proton must move parallel to the field for a force to act"
  answer: 2
  explanation: "The magnetic force is F = q(v × B). With v in the +x direction and B in the +y direction, v × B = x̂ × ŷ = ẑ (upward, +z). Since q is positive for a proton, the force is in the +z direction — upward. The force is always perpendicular to both the velocity and the field; it never aligns with either. The common wrong answer (zero) applies only when v is parallel to B, making the cross product zero — which is not the case here."

- question: "Magnetic fields are used to steer charged particle beams in accelerators. Which statement correctly describes what the magnetic field does to the particles?"
  type: multiple-choice
  options:
    - "It does no work; the particles' speed stays constant but their direction changes"
    - "It does positive work, continuously increasing the particles' kinetic energy"
    - "It does negative work, slowing the particles as they curve"
    - "It does work proportional to the field strength B"
  answer: 0
  explanation: "The magnetic force is always perpendicular to the velocity, so the dot product F · v = 0 at every instant. Work requires a force component along the displacement, and the magnetic force has none. This means a magnetic field can only change the direction of motion, never the speed. In a uniform field, this produces circular (or helical) motion with constant speed — the field continuously redirects without adding or removing kinetic energy. Accelerating particles (increasing their speed) requires electric fields, not magnetic fields."

- question: "A charged particle moving parallel to a magnetic field experiences zero magnetic force."
  type: true-false
  answer: true
  explanation: "The magnetic force is F = q(v × B). The cross product v × B has magnitude |v||B|sinθ, where θ is the angle between the velocity and field vectors. When v is parallel to B, θ = 0°, so sin(0°) = 0, and the force is zero. Only the component of velocity perpendicular to B contributes to the magnetic force. This is why charged particles in a uniform field travel in helices when they have a velocity component along the field: the parallel component is unaffected (no force), while the perpendicular component is deflected into a circle."

- question: "A magnetic field can accelerate a charged particle, increasing its kinetic energy over time."
  type: true-false
  answer: false
  explanation: "This is the key misconception about magnetic forces. The magnetic force F = q(v × B) is always perpendicular to the velocity. Work is defined as W = F · ds, and since the force is perpendicular to the displacement (ds = v dt), the dot product is zero. No work is done, so kinetic energy cannot change. Speed stays constant. The magnetic field is a 'steering' force only — it can curve a particle's path but cannot speed it up or slow it down. Electric fields, not magnetic fields, do work on charges and change their kinetic energy."

- question: "Why do charged particles move in circular paths in a uniform magnetic field? Explain in terms of what the magnetic force does and does not do to the particle's velocity."
  type: short-answer
  answer: "The magnetic force is always perpendicular to the velocity, so it changes the direction of motion but never the speed (it does no work). This is exactly the condition that produces circular motion: a constant-magnitude force perpendicular to the velocity acts as centripetal acceleration, continuously redirecting the particle without changing how fast it moves. Setting the magnetic force equal to the centripetal force gives qvB = mv²/r, from which the cyclotron radius r = mv/(qB) follows directly."
  explanation: "Circular motion requires a centripetal force — always directed toward the center, always perpendicular to the velocity. The magnetic force satisfies this automatically: it is always perpendicular to v (by the cross product geometry) and has constant magnitude when v and B are perpendicular and B is uniform (since |F| = qvB, and v is constant because no work is done). The radius of the circle encodes particle mass and charge — which is why cyclotrons and mass spectrometers can separate particles by their charge-to-mass ratio."
```

## Explainer

In classical mechanics, forces are the fundamental objects that govern motion through Newton's second law F = ma. The electromagnetic force on a point charge is the **Lorentz force**: F⃗ = q(E⃗ + v⃗ × B⃗). The electric part qE⃗ acts along the field direction regardless of the particle's velocity — a familiar force from the Coulomb picture. The magnetic part q(v⃗ × B⃗) is newer and more subtle: it depends on the particle's velocity and points perpendicular to both the velocity and the field. The cross product from multivariable calculus you've studied is exactly the right language here — v⃗ × B⃗ gives a vector perpendicular to both inputs, with magnitude |v||B|sinθ where θ is the angle between them.

The single most important consequence of the cross product geometry is that the magnetic force does no work. Work is F⃗ · ds⃗, and since the magnetic force is always perpendicular to v⃗ = ds⃗/dt, the dot product is always zero. A magnetic field can never speed up or slow down a charged particle — it can only steer it. This is why charged particles in a uniform magnetic field travel in circles (or helices if they have a velocity component along B⃗): the field continuously redirects the velocity without changing its magnitude. The radius of the resulting **cyclotron orbit** r = mv/(qB) is a direct consequence of setting the magnetic force equal to the centripetal acceleration from Newton's second law.

The Lorentz force law is the operational definition of the magnetic field B⃗. Rather than defining B⃗ through its sources (currents, magnets), you define it as the field that, when present, exerts a force q(v⃗ × B⃗) on a charge moving with velocity v⃗. This operational definition ties together field and force, and it is the starting point for deriving all of magnetostatics: Biot-Savart and Ampere's law follow by asking what field configuration, combined with the Lorentz force law, produces the observed forces between current-carrying wires.

Understanding the Lorentz force deeply also connects to your future study of the vector potential and Faraday's law. When you allow B⃗ to vary in time, the force on a moving charge includes an additional contribution from the induced electric field — and the full Lorentz force is needed to correctly account for both. In the relativistic formulation, qF^μν u_ν (where F^μν is the field tensor and u_ν the four-velocity) reproduces the Lorentz force law automatically in any inertial frame, revealing that the electric and magnetic forces are truly two aspects of one relativistic force.
