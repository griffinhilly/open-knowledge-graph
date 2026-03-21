---
id: magnetic-force-moving-charges
title: Lorentz Force on Moving Electric Charges
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: transient-response-rc-circuits
  type: hard
builds-toward:
- magnetic-force-current-wires
- magnetic-field-definition
tags:
- lorentz-force
- moving-charge
- magnetic
stage: formal-systems
status: draft
---

# Lorentz Force on Moving Electric Charges

## Core Idea
A charge q moving with velocity v in magnetic field B experiences force F = q(v × B). Force is perpendicular to both v and B; magnitude is F = qvB sin(θ). Stationary charges experience no magnetic force; motion is essential.

## Questions

```yaml
- question: "A proton enters a uniform magnetic field moving at constant speed. Which of the following CANNOT be caused by the magnetic force alone?"
  type: multiple-choice
  options:
    - "The proton's direction of travel changes"
    - "The proton moves in a circular arc"
    - "The proton's speed increases"
    - "The proton follows a helical path along a field line"
  answer: 2
  explanation: "The magnetic force is always perpendicular to the velocity, so the dot product F·v = 0 — the force does no work. Since kinetic energy = ½mv², and no work is done, speed cannot change. The magnetic force can only redirect the particle: it causes circular motion (when v ⊥ B), helical motion (when v has components both perpendicular and parallel to B), or direction changes generally. It is purely a steering force."

- question: "An electron moves to the right through a region where the magnetic field points into the page. The right-hand rule applied to v × B gives an upward direction. In which direction does the magnetic force on the electron point?"
  type: multiple-choice
  options:
    - "Upward — the right-hand rule determines the force direction regardless of charge sign"
    - "Downward — the force on a negative charge reverses compared to a positive charge"
    - "Into the page — the force is parallel to the field"
    - "To the right — the force is parallel to the velocity"
  answer: 1
  explanation: "The Lorentz force is F = q(v × B). The right-hand rule gives the direction of v × B, which is upward here. For a positive charge, F is upward. For a negative charge (the electron), q is negative, so F = q(v × B) reverses direction — the force is downward. The key: always find v × B first with the right-hand rule, then flip the direction if the charge is negative."

- question: "A stationary electric charge placed inside a strong magnetic field experiences no magnetic force."
  type: true-false
  answer: true
  explanation: "The magnetic force law is F = q(v × B). If v = 0 (the charge is stationary), then v × B = 0, so F = 0. Motion is essential — the magnetic force acts only on moving charges. This distinguishes it fundamentally from the electric force, which acts on charges regardless of whether they move."

- question: "A magnetic force can accelerate a charged particle — that is, increase its kinetic energy — if the field is strong enough."
  type: true-false
  answer: false
  explanation: "No matter how strong the magnetic field, the magnetic force is always perpendicular to the velocity. Since power = F · v and the dot product of perpendicular vectors is zero, the magnetic force does zero work at every instant. Kinetic energy (½mv²) cannot change. Magnetic forces change direction but never speed. This is why particle accelerators use electric fields (which can do work) to speed particles up, while magnetic fields are used to steer them."

- question: "Why does a charged particle moving perpendicular to a uniform magnetic field follow a circular path at constant speed? Explain using the force law."
  type: short-answer
  answer: "The magnetic force F = qvB is always perpendicular to the velocity, so it provides centripetal acceleration without doing work. This means the speed stays constant while the direction continually changes — which is exactly the definition of uniform circular motion. Setting the magnetic force equal to the centripetal force: qvB = mv²/r gives the cyclotron radius r = mv/(qB). The particle curves continuously because the force always points toward the center of the circle."
  explanation: "The key physical insight is that a force perpendicular to velocity acts as a centripetal force: it bends the trajectory without changing the magnitude of velocity. The resulting orbit has a radius that depends on the particle's momentum mv and the field strength qB — a stronger field means tighter bending. This is the operating principle of cyclotrons and particle beam steering magnets."
```

## Explainer

Recall that electric forces act on charges whether they move or not — a stationary charge in an electric field experiences **F** = q**E**. The magnetic force is fundamentally different: it requires motion. A charge sitting still in even the strongest magnetic field feels nothing. The instant it moves, a new force appears, and this force has a peculiar direction: it is always *perpendicular to the velocity*. The **Lorentz force** law **F** = q(**v** × **B**) captures this: the cross product v × B produces a vector at right angles to both **v** and **B**.

The perpendicularity has a decisive consequence — the magnetic force can never do work. Because **F** is always perpendicular to **v**, the dot product **F** · **v** = 0. Power (rate of doing work) is zero. Magnetic forces *redirect* charged particles but cannot speed them up or slow them down. The particle's kinetic energy is conserved; only its direction of travel changes. This is why a charged particle moving perpendicular to a uniform **B** field follows a perfect circle at constant speed: the force provides centripetal acceleration without changing the speed. Setting qvB = mv²/r gives the **cyclotron radius** r = mv/(qB) — a large magnetic field bends the trajectory more tightly, a large momentum makes it harder to bend.

The right-hand rule determines the direction: point your fingers in the direction of **v**, curl them toward **B**, and your thumb points in the direction of **v** × **B**. For a positive charge, the force is in this direction; for a negative charge (like an electron), the force reverses. In a uniform field with both perpendicular and parallel components of **v**, the perpendicular component creates circular motion while the parallel component is unaffected (since v_∥ × **B** = 0 when they are parallel). The result is **helical motion** — the particle spirals along the field line. This is why charged particles from the solar wind spiral along Earth's magnetic field lines and funnel into the polar regions, creating the aurora.

The same force explains how conventional current-carrying wires interact with magnetic fields. A wire is just an ensemble of moving charges (electrons), and each one feels q**v** × **B**. Summing over all carriers gives a net force on the wire proportional to the current and the length of the conductor. This is the principle behind electric motors: a current-carrying loop in a magnetic field experiences opposing forces on opposite sides, creating a torque that rotates the loop. Every electric motor you have ever encountered runs on this one force law.
