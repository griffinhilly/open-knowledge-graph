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

## Explainer

You already know that a moving charge in a magnetic field feels a force F = qv × B (the Lorentz force). A current-carrying wire is nothing more than a stream of moving charges, so it must also feel a force in a magnetic field. The derivation is straightforward: take a small segment of wire with length dL carrying current I. The current is I = nqv_dA, where n is the charge carrier density, v_d is their drift velocity, and A is the cross-sectional area. The force on charges in this segment is dF = (nAL)q(v_d × B) = IL × B, where L points in the direction of conventional current flow. This is not a new force — it is the Lorentz force summed over all the drifting charges in the wire.

The **force law F = IL × B** makes practical sense: a longer wire (more charges) or larger current (faster charges) feels a stronger force, and the force is perpendicular to both the wire and the field. The cross product means zero force when the wire is parallel to the field (L × B = 0) and maximum force when they are perpendicular. For a curved wire in a uniform field, a remarkable shortcut applies: you can replace the entire curved path with the straight vector from one end to the other. The cancellation of transverse contributions leaves only the net endpoint-to-endpoint displacement as the effective length. This is why bent or coiled wires in uniform fields simplify dramatically.

Now consider a closed **current loop** — a rectangle or circle carrying current in a uniform magnetic field. Apply F = IL × B to each segment. In a rectangular loop with sides of length a and b, the forces on opposite sides parallel to B sum to zero, and the forces on the other two sides form a couple — equal and opposite forces displaced from each other. The result is a net torque but zero net force. The torque is τ = IAB sinφ, where φ is the angle between the loop's normal vector and the field. Defining the **magnetic dipole moment** μ = IAn̂ (magnitude = current × area, direction = right-hand rule from the current direction), the torque becomes τ = μ × B. This form is identical to the torque on an electric dipole in an electric field (τ = p × E), completing the conceptual symmetry between electric and magnetic dipoles.

This torque is the operating principle of every electric motor. A current loop in a magnetic field is driven to rotate until μ aligns with B (the stable equilibrium, where τ = 0). A real motor prevents this alignment by commutating the current direction just as the loop reaches alignment, so the torque is always in the same rotational direction. The galvanometer (the meter movement in analog instruments) uses the same torque, balanced against a spring, to convert current into a measurable deflection. Understanding F = IL × B and τ = μ × B is therefore the foundation for understanding most electromechanical devices.
