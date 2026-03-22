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

## Questions

```yaml
- question: "Two parallel wires are separated by 5 cm. Wire A carries current flowing north; wire B carries current flowing south. What is the magnetic interaction between them?"
  type: multiple-choice
  options:
    - "They attract each other — current flow in any direction creates mutual attraction between wires"
    - "They repel each other — antiparallel currents produce a repulsive force"
    - "No force acts between them because the magnetic fields from each wire cancel at the other's location"
    - "They attract if currents are equal in magnitude, repel if the magnitudes differ"
  answer: 1
  explanation: "Antiparallel currents (flowing in opposite directions) produce repulsion. Wire A creates a magnetic field that circles around it; at wire B's location this field points in a direction such that F = IL × B pushes wire B away from wire A. You can verify with the right-hand rule: curl your fingers around wire A in the direction of its field, then apply the force rule to wire B. Parallel currents attract; antiparallel currents repel. Options A and D ignore the directional dependence of the cross product."

- question: "A straight wire carrying current I is oriented parallel to a uniform magnetic field B. What is the magnetic force on the wire?"
  type: multiple-choice
  options:
    - "F = ILB, directed perpendicular to both the wire and the field"
    - "F = ILB, directed along the wire in the direction of current flow"
    - "F = 0, because the wire is parallel to the field"
    - "F = ILB/2, reduced by half because the geometry is non-perpendicular"
  answer: 2
  explanation: "The force on a wire is F = ILB sinθ where θ is the angle between the wire direction and field B. When the wire is parallel to B, θ = 0° and sin(0°) = 0, so F = 0. Physically, the drifting electrons in the wire are moving parallel to B, so v × B = 0 (a vector crossed with a parallel vector is zero). The Lorentz force only acts when velocity has a component perpendicular to the field. Options A and D incorrectly assume a nonzero force, and option B gives the wrong direction even if force were nonzero."

- question: "The force between two parallel current-carrying wires arises because wire 1's magnetic field exerts a Lorentz force on the moving charges (current) in wire 2."
  type: true-false
  answer: true
  explanation: "This is the conceptual bridge between dF = I(dL × B) and the Lorentz force F = qv × B. Wire 1 creates a magnetic field at wire 2's location (by Ampere's law, curling around wire 1). The conduction electrons drifting through wire 2 are moving charges in that field, so each experiences a Lorentz force. Summing over all the charges in a wire segment gives dF = I(dL × B). The force between wires is not a new phenomenon — it is the Lorentz force applied to bulk current."

- question: "Doubling the separation between two parallel current-carrying wires doubles the force per unit length between them."
  type: true-false
  answer: false
  explanation: "The force per unit length is F/L = μ₀I₁I₂/(2πd). Doubling d (from d to 2d) gives F/L = μ₀I₁I₂/(2π·2d) = half the original force. The relationship is inverse, not direct: greater separation means weaker force. This follows from the fact that the magnetic field of an infinite straight wire falls off as 1/r. Doubling the distance halves the field strength at wire 2's location, which halves the force on wire 2."

- question: "Explain why a wire carrying current perpendicular to a magnetic field experiences maximum force, while a wire parallel to the field experiences no force."
  type: short-answer
  answer: "The force on a wire segment is F = ILB sinθ, where θ is the angle between the current direction and B. When perpendicular (θ = 90°), sinθ = 1 and force is maximum F = ILB. When parallel (θ = 0°), sinθ = 0 and force is zero. The physical reason is the cross product in dF = I(dL × B): a vector crossed with a parallel vector is zero because there is no perpendicular component to generate a force. The drifting electrons in the wire only experience a Lorentz force when their velocity has a component perpendicular to B."
  explanation: "This directly follows from the vector nature of the Lorentz force. The cross product v × B measures the component of v perpendicular to B — that is the only component that contributes to the magnetic force. When v is parallel to B, there is no perpendicular component and the force vanishes entirely. When v is perpendicular to B, the full magnitude is available. For a wire, v is fixed in the direction of current flow, so the geometry of how the wire is oriented relative to B completely determines the force magnitude."
```

## Explainer

You already know that a moving charge in a magnetic field experiences a force F⃗ = qv⃗ × B⃗. A current-carrying wire is simply a collection of moving charges — the conduction electrons drifting along the conductor. To find the force on a small wire segment, count the charge dq passing through length dL in time dt: since I = dq/dt, the force on that segment is dF⃗ = dq(v⃗ × B⃗) = I(dL⃗ × B⃗). Integrating along the wire gives the total magnetic force. This is not a new law — it is the Lorentz force applied to bulk current.

For a **straight wire** of length L carrying current I in a uniform field B⃗, the force simplifies to F⃗ = IL⃗ × B⃗, where L⃗ points in the direction of current flow. The magnitude is F = ILB sinθ, where θ is the angle between the wire and the field. Maximum force occurs when the wire is perpendicular to B⃗; no force acts when current flows parallel to the field. The direction follows the right-hand rule: point fingers along the current, curl toward B⃗, and the thumb points in the force direction.

The interaction between **two parallel wires** follows from combining this with Ampere's law. Wire 1 creates a magnetic field that circles around it; at the location of wire 2, this field is directed perpendicularly to wire 2. Applying dF = I dL × B to wire 2 reveals that if the currents run in the same direction, the force pulls the wires together; opposite currents push them apart. You can verify this using the right-hand rule for both the B field of wire 1 and the force on wire 2.

The force per unit length between two parallel wires separated by distance d carrying currents I₁ and I₂ is F/L = μ₀I₁I₂/(2πd). This formula has a distinguished history: it was used to define the **ampere** — historically, one ampere was defined as the current that, in each of two parallel wires one meter apart, produces a force of 2 × 10⁻⁷ N per meter. (Modern SI redefined the ampere in terms of the elementary charge, but the physics is unchanged.) This makes the magnetic force between current-carrying wires not just a lab curiosity but a foundational metrological standard.
