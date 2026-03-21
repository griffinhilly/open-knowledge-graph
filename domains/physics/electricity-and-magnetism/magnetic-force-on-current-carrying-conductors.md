---
id: magnetic-force-on-current-carrying-conductors
title: Magnetic Force on Current-Carrying Conductors
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: magnetic-force-on-moving-charges
  type: hard
- id: electric-current-and-resistance
  type: hard
- id: cross-product
  type: hard
builds-toward:
- biot-savart-law
- electromagnetic-induction-applications
tags:
- force-on-wire
- torque-on-loop
- motor
- magnetic-dipole
stage: formal-systems
status: validated
---

# Magnetic Force on Current-Carrying Conductors

## Core Idea
A current-carrying conductor in a magnetic field experiences a force F = IL × B, where L is the length vector of the wire in the direction of conventional current. For a complete current loop in a uniform field, the net force is zero but there is a net torque τ = μ × B, where μ = IAn̂ is the magnetic dipole moment of the loop. This torque is the operating principle of electric motors and galvanometers.

## How It's Best Learned
Derive F = IL × B from the Lorentz force on individual charge carriers. Then analyze a rectangular current loop in a uniform field — computing the force on each side and showing that the net torque drives it toward alignment with B.

## Common Misconceptions
- Two parallel wires carrying current in the same direction attract each other; opposite directions repel.
- The force on a straight wire in a uniform field depends only on the straight-line distance between endpoints, not the wire's actual path.
- A current loop in a uniform field has no net translational force — only torque.

## Questions

```yaml
- question: "A student learns that a complete current loop in a uniform magnetic field has zero net translational force and concludes: 'So nothing interesting happens to the loop.' What is missing from this conclusion?"
  type: multiple-choice
  options:
    - "The net force is not actually zero — the student made a calculation error"
    - "While the net translational force is zero, the loop experiences a net torque τ = μ × B that causes it to rotate toward alignment with the field"
    - "The loop also experiences induced currents that create additional forces"
    - "The force law F = IL × B doesn't apply to closed loops"
  answer: 1
  explanation: "Zero net force means the loop's center of mass doesn't accelerate translationally. But the forces on opposite sides of the loop form a couple: equal, opposite, and displaced, producing a net torque. This torque τ = μ × B drives the loop to rotate until its magnetic dipole moment μ aligns with the field. This rotation is the operating principle of every electric motor — zero net force coexists with a very significant net torque."

- question: "Two long parallel wires are placed side by side. Both carry current flowing in the same direction. What force do they exert on each other?"
  type: multiple-choice
  options:
    - "They attract each other — parallel currents in the same direction experience a net attractive force"
    - "They repel each other — like currents repel, analogous to like charges"
    - "They experience no force — the fields cancel because the currents are identical"
    - "They repel at close range and attract at longer distances"
  answer: 0
  explanation: "Parallel currents in the same direction attract; anti-parallel currents repel. This is the opposite of the naive 'like repels like' intuition from electrostatics. Wire 1 creates a magnetic field that circles around it (right-hand rule). At Wire 2's location, this field points perpendicular to Wire 2's current, and F = IL × B produces a force directed toward Wire 1. Both wires attract each other by Newton's third law."

- question: "A curved wire and a straight wire connecting the same two endpoints, both carrying the same current in a uniform magnetic field, experience different total magnetic forces."
  type: true-false
  answer: false
  explanation: "In a uniform field, the total force on any current-carrying wire depends only on the straight-line vector from one endpoint to the other, not on the actual path. The transverse components of force on small segments cancel when integrated over the full path, leaving only the net endpoint-to-endpoint displacement as the effective length. A coiled, bent, or curved wire has the same total force as a straight wire between the same points."

- question: "The torque τ = μ × B on a current loop in a magnetic field is the operating principle behind electric motors."
  type: true-false
  answer: true
  explanation: "The torque drives a current loop to rotate toward alignment with the field (μ aligning with B), reaching zero torque at equilibrium. A real motor prevents this equilibrium by reversing the current direction (commutation) just as the loop reaches alignment, so the torque is always in the same rotational sense. Without commutation the loop would oscillate around alignment and stop. The same torque principle (with a spring instead of commutation) gives the galvanometer its deflection."

- question: "Derive the connection between the Lorentz force on individual charge carriers and the force law F = IL × B on a current-carrying wire."
  type: short-answer
  answer: "A current I in a wire consists of charge carriers (charge q, drift velocity v_d) moving through a conductor of cross-sectional area A. The number of charges in a segment of length dL is n·A·dL (n = carrier density). The Lorentz force on each charge is qv_d × B. The total force on the segment is (nAqdL)(v_d × B) = I(dL × B), since I = nAqv_d. Integrating over the wire gives F = IL × B."
  explanation: "This derivation shows that F = IL × B is not a new fundamental law — it is the Lorentz force summed over macroscopic numbers of moving charges. Current is the macroscopic manifestation of ordered charge motion, and the magnetic force on the wire is the collective force on all those carriers. This is why the force depends linearly on both I (more or faster carriers) and L (more carriers in a longer wire)."
```

## Explainer

You already know that a moving charge in a magnetic field feels a force F = qv × B (the Lorentz force). A current-carrying wire is nothing more than a stream of moving charges, so it must also feel a force in a magnetic field. The derivation is straightforward: take a small segment of wire with length dL carrying current I. The current is I = nqv_dA, where n is the charge carrier density, v_d is their drift velocity, and A is the cross-sectional area. The force on charges in this segment is dF = (nAL)q(v_d × B) = IL × B, where L points in the direction of conventional current flow. This is not a new force — it is the Lorentz force summed over all the drifting charges in the wire.

The **force law F = IL × B** makes practical sense: a longer wire (more charges) or larger current (faster charges) feels a stronger force, and the force is perpendicular to both the wire and the field. The cross product means zero force when the wire is parallel to the field (L × B = 0) and maximum force when they are perpendicular. For a curved wire in a uniform field, a remarkable shortcut applies: you can replace the entire curved path with the straight vector from one end to the other. The cancellation of transverse contributions leaves only the net endpoint-to-endpoint displacement as the effective length. This is why bent or coiled wires in uniform fields simplify dramatically.

Now consider a closed **current loop** — a rectangle or circle carrying current in a uniform magnetic field. Apply F = IL × B to each segment. In a rectangular loop with sides of length a and b, the forces on opposite sides parallel to B sum to zero, and the forces on the other two sides form a couple — equal and opposite forces displaced from each other. The result is a net torque but zero net force. The torque is τ = IAB sinφ, where φ is the angle between the loop's normal vector and the field. Defining the **magnetic dipole moment** μ = IAn̂ (magnitude = current × area, direction = right-hand rule from the current direction), the torque becomes τ = μ × B. This form is identical to the torque on an electric dipole in an electric field (τ = p × E), completing the conceptual symmetry between electric and magnetic dipoles.

This torque is the operating principle of every electric motor. A current loop in a magnetic field is driven to rotate until μ aligns with B (the stable equilibrium, where τ = 0). A real motor prevents this alignment by commutating the current direction just as the loop reaches alignment, so the torque is always in the same rotational direction. The galvanometer (the meter movement in analog instruments) uses the same torque, balanced against a spring, to convert current into a measurable deflection. Understanding F = IL × B and τ = μ × B is therefore the foundation for understanding most electromechanical devices.
