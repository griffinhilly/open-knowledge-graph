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

## Explainer

Recall that electric forces act on charges whether they move or not — a stationary charge in an electric field experiences **F** = q**E**. The magnetic force is fundamentally different: it requires motion. A charge sitting still in even the strongest magnetic field feels nothing. The instant it moves, a new force appears, and this force has a peculiar direction: it is always *perpendicular to the velocity*. The **Lorentz force** law **F** = q(**v** × **B**) captures this: the cross product v × B produces a vector at right angles to both **v** and **B**.

The perpendicularity has a decisive consequence — the magnetic force can never do work. Because **F** is always perpendicular to **v**, the dot product **F** · **v** = 0. Power (rate of doing work) is zero. Magnetic forces *redirect* charged particles but cannot speed them up or slow them down. The particle's kinetic energy is conserved; only its direction of travel changes. This is why a charged particle moving perpendicular to a uniform **B** field follows a perfect circle at constant speed: the force provides centripetal acceleration without changing the speed. Setting qvB = mv²/r gives the **cyclotron radius** r = mv/(qB) — a large magnetic field bends the trajectory more tightly, a large momentum makes it harder to bend.

The right-hand rule determines the direction: point your fingers in the direction of **v**, curl them toward **B**, and your thumb points in the direction of **v** × **B**. For a positive charge, the force is in this direction; for a negative charge (like an electron), the force reverses. In a uniform field with both perpendicular and parallel components of **v**, the perpendicular component creates circular motion while the parallel component is unaffected (since v_∥ × **B** = 0 when they are parallel). The result is **helical motion** — the particle spirals along the field line. This is why charged particles from the solar wind spiral along Earth's magnetic field lines and funnel into the polar regions, creating the aurora.

The same force explains how conventional current-carrying wires interact with magnetic fields. A wire is just an ensemble of moving charges (electrons), and each one feels q**v** × **B**. Summing over all carriers gives a net force on the wire proportional to the current and the length of the conductor. This is the principle behind electric motors: a current-carrying loop in a magnetic field experiences opposing forces on opposite sides, creating a torque that rotates the loop. Every electric motor you have ever encountered runs on this one force law.
