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
stage: abstract-reasoning
status: draft
---

# Magnetic Field and the Lorentz Force

## Core Idea
The Lorentz force F = q(E + v × B) describes the force on a charge moving in electromagnetic fields. The magnetic force is always perpendicular to velocity, doing no work but changing direction. This defines the magnetic field B operationally.

## Explainer

In classical mechanics, forces are the fundamental objects that govern motion through Newton's second law F = ma. The electromagnetic force on a point charge is the **Lorentz force**: F⃗ = q(E⃗ + v⃗ × B⃗). The electric part qE⃗ acts along the field direction regardless of the particle's velocity — a familiar force from the Coulomb picture. The magnetic part q(v⃗ × B⃗) is newer and more subtle: it depends on the particle's velocity and points perpendicular to both the velocity and the field. The cross product from multivariable calculus you've studied is exactly the right language here — v⃗ × B⃗ gives a vector perpendicular to both inputs, with magnitude |v||B|sinθ where θ is the angle between them.

The single most important consequence of the cross product geometry is that the magnetic force does no work. Work is F⃗ · ds⃗, and since the magnetic force is always perpendicular to v⃗ = ds⃗/dt, the dot product is always zero. A magnetic field can never speed up or slow down a charged particle — it can only steer it. This is why charged particles in a uniform magnetic field travel in circles (or helices if they have a velocity component along B⃗): the field continuously redirects the velocity without changing its magnitude. The radius of the resulting **cyclotron orbit** r = mv/(qB) is a direct consequence of setting the magnetic force equal to the centripetal acceleration from Newton's second law.

The Lorentz force law is the operational definition of the magnetic field B⃗. Rather than defining B⃗ through its sources (currents, magnets), you define it as the field that, when present, exerts a force q(v⃗ × B⃗) on a charge moving with velocity v⃗. This operational definition ties together field and force, and it is the starting point for deriving all of magnetostatics: Biot-Savart and Ampere's law follow by asking what field configuration, combined with the Lorentz force law, produces the observed forces between current-carrying wires.

Understanding the Lorentz force deeply also connects to your future study of the vector potential and Faraday's law. When you allow B⃗ to vary in time, the force on a moving charge includes an additional contribution from the induced electric field — and the full Lorentz force is needed to correctly account for both. In the relativistic formulation, qF^μν u_ν (where F^μν is the field tensor and u_ν the four-velocity) reproduces the Lorentz force law automatically in any inertial frame, revealing that the electric and magnetic forces are truly two aspects of one relativistic force.
