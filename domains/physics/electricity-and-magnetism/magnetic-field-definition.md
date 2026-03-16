---
id: magnetic-field-definition
title: Definition and Properties of Magnetic Field
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: magnetic-force-moving-charges
  type: hard
builds-toward:
- biot-savart-law-applications
- ampere-law-applications
tags:
- magnetic-field
- definition
- units
stage: formal-systems
status: draft
---

# Definition and Properties of Magnetic Field

## Core Idea
Magnetic field B is defined via the Lorentz force F = q(v × B); units are tesla (T) or weber/m² (Wb/m²). Magnetic field lines are continuous (no magnetic monopoles): ∇⋅B = 0. Field circulates around currents.

## Explainer

You have already learned that a moving charge experiences a magnetic force. That force depends on the charge's velocity — but velocity relative to what, and through what? The magnetic field **B** is the answer: it is the field permeating space that mediates the interaction between moving charges. Just as the electric field E tells you the force per unit charge on a stationary test charge, the magnetic field B tells you the force per unit charge per unit velocity on a moving one, with the crucial twist that the force direction depends on the cross product v × B.

The defining equation F = q(v × B) has several important geometric consequences that follow directly from the cross product. The force is always **perpendicular** to both the velocity and the field — which means the magnetic force does no work on the charge (it cannot speed it up or slow it down, only change its direction). A charge moving parallel to B feels no force at all; the force is maximum when v is perpendicular to B. For a positive charge moving in the +x direction through a field pointing in the +z direction, the force is in the +y direction; reverse the charge sign or reverse the velocity, and the force reverses. The right-hand rule encodes all of this geometry. Units of B are **teslas (T)**: one tesla is the field strength that exerts 1 N of force on a 1 C charge moving at 1 m/s perpendicular to the field.

The deep structural property of the magnetic field is stated by ∇·B = 0: there are no **magnetic monopoles**. Electric field lines begin on positive charges and end on negative charges — but magnetic field lines have no beginnings or endings. They form closed loops. Break a bar magnet in half and you get two smaller magnets, each with their own north and south poles, not an isolated north pole. This is a fundamental symmetry distinction between electricity and magnetism: the electric field has sources (charges), but the magnetic field does not. All magnetic fields are produced by electric currents (moving charges) or changing electric fields. The field "circulates" around its current source rather than radiating away from it — a hint of the Biot-Savart and Ampère's law physics you will develop next.

The **tesla** is a large unit for everyday purposes: the Earth's magnetic field is about 50 microtesla, MRI machines operate around 1–3 T, and the strongest continuous laboratory magnets reach about 45 T. When you study how currents create magnetic fields via Biot-Savart and Ampère's law, you will be computing the B field produced by specific current configurations. The framework you are building now — that B is defined by its force on moving charges and its lines form closed loops — is the foundation for all of that analysis.
