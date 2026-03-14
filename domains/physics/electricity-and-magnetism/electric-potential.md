---
id: electric-potential
title: Electric Potential
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: electric-potential-energy
  type: hard
- id: electric-field
  type: soft
- id: gradient-vector
  type: soft
- id: line-integrals-vector-fields
  type: soft
builds-toward:
- capacitance
- conductors-in-electrostatics
tags:
- voltage
- potential
- equipotential
- electrostatics
stage: formal-systems
status: validated
---

# Electric Potential

## Core Idea
The electric potential V at a point is the electric potential energy per unit charge: V = U/q, measured in volts (V = J/C). For a point charge Q, V = kQ/r. Potential is a scalar field, making it far easier to compute for multiple sources than the vector field E — just add scalar contributions. The relationship between field and potential is E = −∇V (in 1D, E = −dV/dx), and equipotential surfaces are always perpendicular to field lines.

## How It's Best Learned
Master the scalar superposition of V for point charge distributions before computing E from −∇V. Sketch equipotential surfaces alongside field lines for simple configurations to build intuition about their perpendicularity.

## Common Misconceptions
- Potential is not the same as potential energy; V is potential energy per unit charge.
- A region of zero potential does not imply zero electric field.
- Charges move from high to low potential (if positive) or low to high (if negative).
