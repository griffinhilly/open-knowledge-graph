---
id: magnetic-field-lines-flux-density
title: Magnetic Field Lines, Flux, and Flux Density
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: magnetic-field-intro
  type: hard
- id: magnetic-flux-and-induction
  type: hard
builds-toward:
- solenoid-magnetic-field-properties
tags:
- magnetism
- field visualization
- flux
stage: formal-systems
status: draft
---

# Magnetic Field Lines, Flux, and Flux Density

## Core Idea
Magnetic field lines form closed loops because there are no magnetic monopoles. The density of field lines is proportional to flux density B. Magnetic flux through a surface is Φ_B = ∫ B·dA. Unlike electric field lines, magnetic field lines never begin or end.

## Explainer

Magnetic field lines offer a visual grammar for understanding how magnetic fields are organized in space. Unlike electric field lines, which begin on positive charges and end on negative charges, **magnetic field lines always close on themselves** — they form complete loops with no beginning and no end. This is not a coincidence or a convention; it reflects a deep physical fact: there are no magnetic monopoles. Every north pole comes attached to a south pole, so there is never a point where field lines can originate or terminate.

The spacing of field lines encodes field strength: **magnetic flux density** B (measured in tesla) is high where lines are crowded together and low where they spread apart. This is the same visual convention as for electric field lines, so your intuition carries over directly. Inside a bar magnet, field lines run from south pole to north pole (completing the loop that arcs from north to south outside). Near a long straight wire carrying current, field lines form concentric circles — perfect closed loops with no beginning or end. Near a solenoid, lines emerge from one end, arc through the surrounding space, and re-enter at the other end.

**Magnetic flux** Φ_B = ∫ B·dA counts how many field lines thread through a surface. If the field is uniform and perpendicular to a flat surface of area A, the integral simplifies to Φ_B = BA. If the field makes an angle θ with the surface normal, it becomes Φ_B = BA cos θ — only the perpendicular component of B threads through. This concept directly underpins Faraday's law from your prerequisite study: changing magnetic flux through a loop induces an EMF. The flux density B makes that relationship precise by quantifying the field locally at every point.

A key consequence of closed field lines is that the total flux through any closed surface is exactly zero: ∮ B·dA = 0. This is **Gauss's law for magnetism** — the magnetic analog of Gauss's law for electric fields, but with zero on the right-hand side because there are no magnetic charges. Every field line entering a closed surface must also exit it. This constraint fundamentally distinguishes the structure of magnetism from electrostatics and has deep consequences throughout electromagnetism: it is one of Maxwell's four equations and rules out any possibility of magnetic monopoles in classical theory.
