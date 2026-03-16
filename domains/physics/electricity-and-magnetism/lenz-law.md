---
id: lenz-law
title: Lenz's Law and Direction of Induction
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: self-inductance
  type: soft
- id: faraday-induced-emf
  type: hard
builds-toward:
- ac-impedance
tags:
- lenz-law
- direction
- opposition
stage: formal-systems
status: draft
---

# Lenz's Law and Direction of Induction

## Core Idea
Lenz's law states that an induced EMF, current, or magnetic field opposes the change in magnetic flux that caused it. This is expressed by the minus sign in Faraday's law: ε = −dΦ_B/dt. If flux increases, the induced field opposes the increase. If flux decreases, the induced field opposes the decrease. Lenz's law is a consequence of energy conservation.

## Explainer

From Faraday's law, you know that a changing magnetic flux through a loop induces an EMF equal to −dΦ_B/dt. Faraday's law tells you the magnitude of this EMF and includes a minus sign — but what does that minus sign mean physically? **Lenz's law** is the physical interpretation: the induced EMF drives a current in the direction that **opposes** the change in flux that caused it.

Think of it this way: nature resists change. If you push a bar magnet toward a conducting loop, the increasing flux through the loop induces a current. By Lenz's law, that current must create a magnetic field that opposes the increase — so the induced current flows in the direction that creates a field pointing opposite to the approaching magnet's field, effectively repelling the magnet. If you pull the magnet away, flux decreases, and the induced current reverses direction to try to maintain the flux by creating a field aligned with the departing magnet, effectively attracting it back. In either case, the induced response works against whatever change you are imposing.

This opposition is required by **energy conservation**. If the induced current aided the flux increase instead of opposing it, it would create a stronger field, inducing a still larger current, creating an even stronger field — a runaway process generating energy from nothing. The minus sign in Faraday's law is thermodynamics encoded in an equation. Any time you see an induced effect, it will always act to make your life harder: the induced current in a generator opposes the rotation of the coil (you feel resistance when turning the crank), and the **back-EMF** in a motor opposes the applied voltage that drives it.

A vivid application is **self-inductance**, where a changing current in a coil induces a back-EMF in that same coil. When current increases, the growing magnetic flux through the coil's own turns induces a voltage opposing the increase — this is why inductors resist sudden changes in current and store energy in their magnetic fields. The same principle governs eddy-current braking (the drag felt by a metal plate swinging through a magnet), transformer operation, and the reactive impedance of coils in AC circuits. In every case, you can determine the direction of the induced response by asking: what change is occurring in flux, and what direction of induced current would oppose that change?
