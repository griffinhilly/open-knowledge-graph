---
id: magnetic-force-conductors
title: Magnetic Force on Current-Carrying Conductors
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: magnetic-force-lorentz
  type: hard
builds-toward:
- magnetic-torque-dipole
tags:
- magnetic-force
- current
- conductor
stage: formal-systems
status: validated
---

# Magnetic Force on Current-Carrying Conductors

## Core Idea
A wire of length L carrying current I in a magnetic field B⃗ experiences force F⃗ = I(L⃗ × B⃗), where L⃗ is in the direction of current. For an arbitrary path: F⃗ = I ∫ d⃗ℓ × B⃗. In a uniform field, F = BIL sin(θ), where θ is the angle between wire and field. This is the net result of Lorentz forces on all moving charge carriers.

## Questions

```yaml
- question: "A straight wire carries current flowing in the same direction as an external magnetic field. What force does the wire experience?"
  type: multiple-choice
  options:
    - "A force in the direction of the current"
    - "A force perpendicular to both the current and the field, given by the right-hand rule"
    - "No force, because sin(0°) = 0 when the current direction and field are parallel"
    - "A force that depends on the current magnitude but not on the angle between wire and field"
  answer: 2
  explanation: "The force formula is F = BIL sin(θ), where θ is the angle between the current direction and the magnetic field. When they are parallel, θ = 0° and sin(0°) = 0, so F = 0. This follows directly from the cross product I·L⃗ × B⃗: the cross product of two parallel vectors is zero. Maximum force occurs at θ = 90° (wire perpendicular to field). This is a key practical point for motor and actuator design — the wire must be oriented perpendicular to the field to get maximum torque."

- question: "Why does a magnetic force on the electrons inside a conductor accelerate the entire wire, rather than just deflecting the electrons?"
  type: multiple-choice
  options:
    - "Magnetic fields act directly on all charged particles including positive ions, so both move together"
    - "The drifting electrons are confined within the conductor and transfer their sideways force to the surrounding ion lattice, moving the whole wire"
    - "The force acts on the wire's outer surface, which has a net charge that the field can push"
    - "The current creates a secondary electric field that independently accelerates the positive ions"
  answer: 1
  explanation: "The electrons experience the Lorentz force and are deflected sideways, but they cannot leave the conductor — they are confined within it. As they are pushed sideways, they collide with and exert pressure on the positive ion lattice. The ions, being part of the macroscopic wire, transmit this force to the entire conductor. This is the bridge between microscopic electrodynamics and macroscopic mechanical engineering: the force is ultimately felt by the wire as a whole."

- question: "The formula F = BIL sin(θ) for a current-carrying wire represents a distinct magnetic force law separate from the Lorentz force — it applies specifically to conductors rather than to individual charges."
  type: true-false
  answer: false
  explanation: "F = BIL sin(θ) is not a separate law — it is the Lorentz force summed over all mobile charge carriers in the wire segment. The derivation in the Explainer shows this explicitly: (number of carriers) × (force per carrier) = n·A·dℓ·qv_d × B⃗ = I·dℓ × B⃗. The macroscopic formula emerges from the microscopic Lorentz force through a straightforward summation. Understanding this connection prevents treating electromagnetic laws as a disconnected collection of formulas."

- question: "A wire carrying current in a magnetic field experiences zero net force when oriented parallel to the field and maximum force when oriented perpendicular to the field."
  type: true-false
  answer: true
  explanation: "This follows directly from F = BIL sin(θ). At θ = 0° (parallel), sin(0°) = 0 so F = 0. At θ = 90° (perpendicular), sin(90°) = 1 so F = BIL, the maximum. This angular dependence is central to motor design: the coil must be oriented so that the force-producing wire segments are as close to perpendicular to the field as possible. At parallel orientation, the wire passes through the 'dead zone' where torque momentarily vanishes."

- question: "Derive qualitatively why the force on a current-carrying wire is F = BIL sin(θ) by starting from the Lorentz force on a single charge carrier. What physical reasoning connects the two?"
  type: short-answer
  answer: "Each mobile charge carrier in the wire experiences Lorentz force F = qv_d × B⃗ in the same direction (since all carriers drift the same way). The total force is the sum over all carriers in the segment: (number of carriers) × (force per carrier). For a segment of length dℓ and cross-section A with carrier density n, there are n·A·dℓ carriers. Each contributes qv_d B sin(θ), so total force is n·A·dℓ·qv_d·B sin(θ) = I·dℓ·B sin(θ), since I = nqv_d·A. Integrating over length L gives F = BIL sin(θ)."
  explanation: "The key physical insight is that current is just a macroscopic description of many charges drifting together. The Lorentz force acts on each one, and since they all drift in the same direction with the same velocity, their contributions add constructively. The macroscopic formula is simply the sum — no new physics is required, only the microscopic picture applied at scale."
```

## Explainer

You already know the Lorentz force: a charge q moving with velocity v⃗ in a magnetic field B⃗ experiences F⃗ = qv⃗ × B⃗. A current-carrying wire is simply a conductor where many charges are drifting in one direction. The **magnetic force on a conductor** is not a new law — it is the Lorentz force summed over all the mobile charge carriers inside.

Here is how the summation works. Consider a wire segment of length dℓ with cross-sectional area A. If the carrier density is n (charges per volume), each with charge q and drift velocity v_d, then the current is I = nqv_d·A. The number of carriers in the segment is n·A·dℓ. Each experiences force q·v_d × B⃗, so the total force on the segment is (n·A·dℓ)·q·v_d × B⃗ = I·dℓ × B⃗. This is the differential form F⃗ = I∫dℓ⃗ × B⃗, where dℓ⃗ points along the current direction.

For a straight wire of length L in a uniform field, this gives F = BIL sin(θ), where θ is the angle between the wire and the field. The direction of the force is given by the right-hand rule on I·L⃗ × B⃗: point fingers along the current, curl toward B⃗, and the thumb points in the force direction. Maximum force occurs when the wire is perpendicular to the field (θ = 90°); a wire parallel to the field experiences no force. This is the operating principle of electric motors — loop-shaped conductors in a magnetic field experience torques because opposite sides of the loop carry current in opposite directions and therefore experience forces in opposite directions, producing rotation.

The key subtlety is that the magnetic force is transmitted to the wire as a whole, not just to the electrons. The drifting electrons are pushed sideways by B⃗, but since they are confined within the conductor, they push on the lattice of positive ions, and the entire wire accelerates. This mechanical force on macroscopic objects is the bridge between microscopic electromagnetism and everyday engineering: it underlies speakers, rail guns, magnetohydrodynamic drives, and every electromagnetic actuator ever built.
