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
builds-toward:
- force-between-parallel-current-wires
tags:
- magnetism
- forces
- current interaction
stage: formal-systems
status: draft
---

# Force on Current-Carrying Conductors in Magnetic Fields

## Core Idea
A current-carrying conductor in a magnetic field experiences force F = I L × B, where L is the length vector. For arbitrary shapes, F = ∫ I (d l × B). This force arises from the Lorentz force on the moving charge carriers. A uniform field exerts net force only on non-planar loops or loops not entirely within the field.

## Explainer

From the Lorentz force you already know, a single charge q moving with velocity v in a magnetic field B experiences a force F = qv × B. A current-carrying wire is simply a vast number of such moving charges — the conduction electrons drifting along the wire under the influence of an electric potential. The force on the wire is nothing more than the sum of all individual Lorentz forces on those moving charges, and this aggregate can be expressed cleanly in terms of the macroscopic current.

To see how the formula F = IL × B emerges, consider a wire segment of length L carrying current I in a uniform field B. If n is the number of charge carriers per unit volume, each with charge q and drift velocity v_d, then I = nqv_d · A (where A is the cross-sectional area). The total force on the segment is (number of charges) × (Lorentz force per charge) = (nAL) × (qv_d × B). Substituting the expression for I shows that nAL·qv_d = IL, and the direction of L is the direction of conventional current (the drift direction of positive carriers). The result is F = IL × B — macroscopic current I and length L have absorbed all the microscopic details.

The **cross product** L × B is what you practiced in your prerequisites. Its magnitude is LB sin θ, where θ is the angle between the wire and the field: maximum force when wire is perpendicular to B, zero force when wire is parallel to B (charges move along the field, so v ∥ B and v × B = 0). The direction follows the right-hand rule: point fingers along the current direction, curl toward B, and the thumb gives the force on positive-current wire. For a curved or arbitrarily shaped conductor in a non-uniform field, you integrate element-by-element: F = ∫ I (dl × B), treating each infinitesimal length element dl as a tiny straight segment.

A crucial result for closed loops in a **uniform** field: the net force is zero. You can verify this by noting that ∮ dl = 0 (the loop returns to its starting point), so ∮ I (dl × B) = I(∮ dl) × B = 0 when B is constant. However, such a loop still experiences a **torque** (not covered here but built toward in the next topics), which is the operating principle of electric motors. The net-zero force explains why you cannot levitate a current loop in a perfectly uniform magnetic field — you need a field gradient to produce a net translational force.
