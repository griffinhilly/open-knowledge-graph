---
id: force-on-current-carrying-conductor
title: Force on Current-Carrying Conductors in Magnetic Fields
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: lorentz-force-on-moving-charge
  type: hard
- id: current-density-current-distribution
  type: hard
- id: cross-product
  type: hard
- id: magnetic-dipole-moment
  type: soft
builds-toward:
- force-between-parallel-current-wires
tags:
- magnetism
- forces
- current interaction
stage: expert
status: validated
---
# Force on Current-Carrying Conductors in Magnetic Fields

## Core Idea
A current-carrying conductor in a magnetic field experiences force F = I L × B, where L is the length vector. For arbitrary shapes, F = ∫ I (d l × B). This force arises from the Lorentz force on the moving charge carriers. A uniform field exerts net force only on non-planar loops or loops not entirely within the field.

## Questions

```yaml
- question: "A straight wire carrying current I is oriented parallel to a uniform magnetic field B. What is the magnetic force on the wire?"
  type: multiple-choice
  options:
    - "F = ILB, directed perpendicular to both the wire and the field"
    - "F = ILB, directed along the wire"
    - "F = 0, because the cross product of parallel vectors is zero"
    - "F = ILB/2, because parallel orientation gives half the maximum force"
  answer: 2
  explanation: "The force is F = IL × B. The magnitude is ILB sin θ, where θ is the angle between the current direction and B. When the wire is parallel to B, θ = 0° (or 180°), so sin θ = 0 and F = 0. Physically, the conduction electrons drift along the field direction, so v ∥ B, and the cross product v × B = 0 — the Lorentz force on each charge is zero. Maximum force occurs at θ = 90° (wire perpendicular to field)."

- question: "A rectangular current loop lies entirely within a uniform magnetic field. What can you conclude about the net force on the loop?"
  type: multiple-choice
  options:
    - "The net force is nonzero and directed toward the stronger part of the field"
    - "The net force is zero, because opposite sides of the loop carry currents in opposite directions and their forces cancel"
    - "The net force is zero, which follows from ∮ dl = 0 for any closed path"
    - "The net force equals ILB for the longest side of the loop"
  answer: 2
  explanation: "Both B and C are essentially correct statements (opposite currents + the mathematical identity), but C captures the deeper reason more precisely. For any closed loop in a uniform field: F = ∮ I(dl × B) = I(∮ dl) × B = I(0) × B = 0, because ∮ dl = 0 (the loop returns to its starting point). This result is independent of the loop's shape. Importantly, the net force is zero but the loop may still experience a nonzero *torque*, which is the basis of electric motor operation."

- question: "The force on a current-carrying wire is greatest when the wire is oriented perpendicular to the magnetic field."
  type: true-false
  answer: true
  explanation: "The magnitude of the force is F = ILB sin θ, where θ is the angle between the current direction and the field B. sin θ is maximized at θ = 90° (perpendicular orientation), giving F_max = ILB. At θ = 0° (parallel), sin θ = 0 and F = 0. This follows directly from the cross product: |L × B| = LB sin θ, which peaks when L and B are perpendicular."

- question: "A closed current loop in a perfectly uniform magnetic field experiences both a net force and a net torque."
  type: true-false
  answer: false
  explanation: "In a uniform field, the net *force* on a closed loop is always zero (because ∮ dl = 0 for any closed path, so F = I(∮ dl) × B = 0). However, the loop generally experiences a nonzero *torque* (unless the loop's magnetic moment is aligned with the field). Torque and force are independent: zero net force does not imply zero torque. This distinction is critical for understanding electric motors, which rotate due to torque despite experiencing no net translational force in a uniform field."

- question: "Starting from the Lorentz force law on a single charge, derive the force formula F = IL × B for a straight current-carrying wire segment of length L."
  type: short-answer
  answer: "Consider a wire segment of length L, cross-sectional area A, with n charge carriers per unit volume, each with charge q and drift velocity v_d. The total number of charges in the segment is nAL. The Lorentz force on each charge is F_single = qv_d × B. The total force on the segment is (nAL)(qv_d × B) = (nqv_dA)L × B. But nqv_dA is exactly the definition of current I (charge per unit time crossing a cross-section). Substituting: F = IL × B, where L is a vector of magnitude L pointing in the direction of conventional current flow."
  explanation: "The key step is recognizing that current I = nqv_dA consolidates all the microscopic details (carrier density, charge, drift speed, area) into one macroscopic quantity. Once you make this substitution, the formula F = IL × B is nothing more than the Lorentz force on all carriers rewritten in terms of the measurable current. This derivation also shows why the force is zero when the wire is parallel to B: in that case, v_d ∥ B, so v_d × B = 0 for each individual carrier."
```

## Explainer

From the Lorentz force you already know, a single charge q moving with velocity v in a magnetic field B experiences a force F = qv × B. A current-carrying wire is simply a vast number of such moving charges — the conduction electrons drifting along the wire under the influence of an electric potential. The force on the wire is nothing more than the sum of all individual Lorentz forces on those moving charges, and this aggregate can be expressed cleanly in terms of the macroscopic current.

To see how the formula F = IL × B emerges, consider a wire segment of length L carrying current I in a uniform field B. If n is the number of charge carriers per unit volume, each with charge q and drift velocity v_d, then I = nqv_d · A (where A is the cross-sectional area). The total force on the segment is (number of charges) × (Lorentz force per charge) = (nAL) × (qv_d × B). Substituting the expression for I shows that nAL·qv_d = IL, and the direction of L is the direction of conventional current (the drift direction of positive carriers). The result is F = IL × B — macroscopic current I and length L have absorbed all the microscopic details.

The **cross product** L × B is what you practiced in your prerequisites. Its magnitude is LB sin θ, where θ is the angle between the wire and the field: maximum force when wire is perpendicular to B, zero force when wire is parallel to B (charges move along the field, so v ∥ B and v × B = 0). The direction follows the right-hand rule: point fingers along the current direction, curl toward B, and the thumb gives the force on positive-current wire. For a curved or arbitrarily shaped conductor in a non-uniform field, you integrate element-by-element: F = ∫ I (dl × B), treating each infinitesimal length element dl as a tiny straight segment.

A crucial result for closed loops in a **uniform** field: the net force is zero. You can verify this by noting that ∮ dl = 0 (the loop returns to its starting point), so ∮ I (dl × B) = I(∮ dl) × B = 0 when B is constant. However, such a loop still experiences a **torque** (not covered here but built toward in the next topics), which is the operating principle of electric motors. The net-zero force explains why you cannot levitate a current loop in a perfectly uniform magnetic field — you need a field gradient to produce a net translational force.
