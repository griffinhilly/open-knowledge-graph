---
id: magnetic-force-current-wires
title: Magnetic Force on Current-Carrying Wires
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: magnetic-force-moving-charges
  type: hard
builds-toward:
- magnetic-field-definition
- magnetic-torque-dipole
tags:
- force
- current
- wire
stage: formal-systems
status: draft
---

# Magnetic Force on Current-Carrying Wires

## Core Idea
Force on a wire segment carrying current I in field B is dF = I(dL × B). For straight wire of length L: F = IL × B. Parallel currents attract; antiparallel currents repel. Force per unit length between parallel wires defines ampere.

## Explainer

You already know that a moving charge in a magnetic field experiences a force F⃗ = qv⃗ × B⃗. A current-carrying wire is simply a collection of moving charges — the conduction electrons drifting along the conductor. To find the force on a small wire segment, count the charge dq passing through length dL in time dt: since I = dq/dt, the force on that segment is dF⃗ = dq(v⃗ × B⃗) = I(dL⃗ × B⃗). Integrating along the wire gives the total magnetic force. This is not a new law — it is the Lorentz force applied to bulk current.

For a **straight wire** of length L carrying current I in a uniform field B⃗, the force simplifies to F⃗ = IL⃗ × B⃗, where L⃗ points in the direction of current flow. The magnitude is F = ILB sinθ, where θ is the angle between the wire and the field. Maximum force occurs when the wire is perpendicular to B⃗; no force acts when current flows parallel to the field. The direction follows the right-hand rule: point fingers along the current, curl toward B⃗, and the thumb points in the force direction.

The interaction between **two parallel wires** follows from combining this with Ampere's law. Wire 1 creates a magnetic field that circles around it; at the location of wire 2, this field is directed perpendicularly to wire 2. Applying dF = I dL × B to wire 2 reveals that if the currents run in the same direction, the force pulls the wires together; opposite currents push them apart. You can verify this using the right-hand rule for both the B field of wire 1 and the force on wire 2.

The force per unit length between two parallel wires separated by distance d carrying currents I₁ and I₂ is F/L = μ₀I₁I₂/(2πd). This formula has a distinguished history: it was used to define the **ampere** — historically, one ampere was defined as the current that, in each of two parallel wires one meter apart, produces a force of 2 × 10⁻⁷ N per meter. (Modern SI redefined the ampere in terms of the elementary charge, but the physics is unchanged.) This makes the magnetic force between current-carrying wires not just a lab curiosity but a foundational metrological standard.
