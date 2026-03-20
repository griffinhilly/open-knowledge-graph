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
- id: conservative-fields
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

## Questions

```yaml
- question: "The electric potential V at a point in space equals zero. Which of the following must be true at that point?"
  type: multiple-choice
  options:
    - "The electric field is also zero"
    - "No net charge exists anywhere in the surroundings"
    - "No net work is needed to bring a test charge to that point from infinity"
    - "Positive charges placed there will experience no force"
  answer: 2
  explanation: "V = 0 means U = qV = 0 for any test charge, so no net work is done moving it from infinity (where V is also defined as zero) to that point. The electric field at a point is E = −∇V; a field requires a *gradient* (slope) of potential, not a nonzero value. A region can have V = 0 with a strong field if the potential is changing rapidly there — this is the most important misconception about potential."

- question: "The electric potential is higher at a point closer to a positive point charge than at a point farther away from the same charge."
  type: true-false
  answer: true
  explanation: "For a positive charge Q, V = kQ/r. Since k > 0 and Q > 0, V decreases as r increases — so points closer to the charge have higher potential. This is consistent with the fact that positive test charges naturally accelerate from high to low potential (away from the positive source), just as objects fall from high to low gravitational potential."

- question: "Why is electric potential (a scalar) typically easier to use than electric field (a vector) when computing the effect of multiple point charges?"
  type: short-answer
  answer: "Potential obeys scalar superposition: the total potential at a point is the algebraic sum V = kQ₁/r₁ + kQ₂/r₂ + ... with no direction to track. Electric field requires vector addition — you must resolve each contribution into components and add them separately. Once total V is known, the field can be recovered from E = −∇V if needed."
  explanation: "This computational advantage is the main reason electric potential is introduced rather than working purely with fields. The strategy of 'find V first, then find E' solves many problems with far less algebra than direct vector field superposition."
```

## Explainer

When you studied electric potential energy, you found that moving a charge in an electric field involves work — and that the energy stored depends on how much charge is present. Electric potential strips out the charge dependence by asking: how much energy *per unit charge* is needed? The result, V = U/q, is measured in volts (1 V = 1 J/C) and describes a property of the field configuration itself, independent of any particular test charge you might place there.

The most important conceptual shift is recognizing that potential is a *scalar field* — a single number at every point in space, not an arrow pointing in some direction. This makes superposition dramatically simpler. For a distribution of point charges, the total potential at any point is just the algebraic sum of the individual contributions: V = kQ₁/r₁ + kQ₂/r₂ + .... Compare this to the electric field, where you would have to decompose each contribution into x- and y-components and add them as vectors. The scalar nature of V is not merely a convenience — it reflects a deep feature of conservative fields, which you may have seen in work on conservative fields (a soft prerequisite).

The relationship between field and potential is E = −∇V (in one dimension, E = −dV/dx). The negative sign and the derivative together mean: the electric field points in the direction of *decreasing* potential, and its magnitude reflects how steeply potential changes. A region of zero potential does not imply zero field — a constant nonzero potential would have zero field; a zero potential in the middle of a steep gradient can have a very strong field. This is the central misconception to guard against.

Equipotential surfaces are surfaces of constant V. Since the field points in the direction of steepest descent of V, field lines must always cross equipotentials at right angles — just as a river runs perpendicular to the contour lines on a topographic map. Sketching both together for simple charge distributions (a single point charge, a dipole, a parallel-plate capacitor) builds powerful intuition about how field geometry relates to energy landscape.

Finally, keep potential and potential energy distinct. V is a property of a location in the field; U = qV depends on the charge placed there. When physicists say a conductor is "at 5 volts," they mean every point on its surface has V = 5 V — the actual energy stored depends on the charge. Voltage, potential, and potential energy are related but not interchangeable, and precision with language here will prevent persistent confusion as you proceed to capacitors and circuits.
