---
id: curl-divergence
title: Curl and Divergence
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: curl-and-divergence
  type: hard
- id: partial-derivatives
  type: hard
builds-toward:
- greens-theorem
- stokes-theorem
- divergence-theorem
tags:
- curl
- divergence
stage: formal-systems
status: validated
---

# Curl and Divergence

## Core Idea
For F = (P, Q, R), curl is ∇×F = (R_y - Q_z, P_z - R_x, Q_x - P_y) (rotation), and divergence is ∇·F = P_x + Q_y + R_z (outflow). Conservative fields have curl = 0.

## Questions

```yaml
- question: "A fluid velocity field F has ∇·F > 0 at a point P. What does this tell you about the flow at P?"
  type: multiple-choice
  options:
    - "The fluid is spinning at P — divergence measures rotation"
    - "There is a source at P — fluid is flowing outward, expanding away from this point"
    - "The fluid flow is conservative at P"
    - "The field has no curl at P"
  answer: 1
  explanation: "Divergence ∇·F measures the net rate of outward flow (expansion) at a point. ∇·F > 0 means fluid is being created there — a source. ∇·F < 0 would be a sink. Rotation is measured by curl, not divergence — this is the most common confusion between the two operators."

- question: "A vector field F has ∇×F = 0 everywhere. Which of the following must be true?"
  type: multiple-choice
  options:
    - "F is the zero vector field"
    - "F has no sources or sinks (∇·F = 0 everywhere)"
    - "F can be written as the gradient of some scalar potential φ"
    - "F is a constant vector field"
  answer: 2
  explanation: "∇×F = 0 means F is irrotational, which (on simply connected domains) is equivalent to F being a conservative field — expressible as F = ∇φ for some scalar potential. This says nothing about divergence: a conservative field can have sources and sinks. The zero field satisfies both conditions, but many non-zero, non-constant fields have zero curl."

- question: "The divergence of the curl of any smooth vector field is always zero: ∇·(∇×F) = 0."
  type: true-false
  answer: true
  explanation: "This identity follows from the antisymmetry of the cross product and the symmetry of mixed partial derivatives. Intuitively: if curl measures local rotation, divergence of a curl would measure 'net outflow of rotation,' which is geometrically zero — rotation has no net source or sink. This identity is essential background for Stokes' theorem and the Divergence Theorem."

- question: "If a vector field F has ∇·F = 0 everywhere (incompressible), then F is conservative."
  type: true-false
  answer: false
  explanation: "Incompressible (zero divergence) and conservative (zero curl) are entirely different conditions. ∇·F = 0 means no sources or sinks — as much flows in as flows out. ∇×F = 0 means no local rotation, which implies the field is a gradient field. Neither condition implies the other. For example, a steady vortex flow can be incompressible but highly rotational (nonzero curl)."

- question: "Explain why curl is a vector while divergence is a scalar, and what each one measures about a vector field at a point."
  type: short-answer
  answer: "Divergence sums the self-derivatives of each component (∂P/∂x + ∂Q/∂y + ∂R/∂z), producing a single number that measures net outward flow — one scalar per point. Curl computes cross-derivatives between different components, producing a vector whose direction indicates the axis of rotation and whose magnitude measures the angular speed of local spinning."
  explanation: "The scalar vs. vector distinction reflects the geometry. Outflow has no preferred direction — it's symmetric — so divergence is scalar. Rotation has an axis and sense (clockwise vs. counterclockwise), so curl must be a vector to encode that directional information. This also explains why the del notation works: ∇·F is a dot product (scalar), ∇×F is a cross product (vector)."
```

## Explainer

From your work with partial derivatives, you know that ∂f/∂x measures how a scalar function changes in the x-direction while other variables are held fixed. Curl and divergence extend this idea to **vector fields** — functions F that assign a vector to each point in space. Where a scalar function has one rate of change per direction, a vector field has many partial derivatives interacting with each other, and curl and divergence are specific combinations that extract physically meaningful information.

**Divergence** measures whether a vector field is spreading out or compressing at each point. For F = (P, Q, R), the divergence is ∇·F = ∂P/∂x + ∂Q/∂y + ∂R/∂z — the sum of the "self-derivatives" of each component. Think of F as the velocity field of a fluid. At each point, divergence measures the net rate at which fluid is expanding away from that point. If ∇·F > 0 at a point, fluid is being created there (a **source**). If ∇·F < 0, fluid is draining away (a **sink**). If ∇·F = 0 everywhere, the fluid is incompressible — as much flows in as flows out. Divergence is a scalar: one number at each point.

**Curl** measures the local rotation in a vector field. For F = (P, Q, R), the curl is ∇×F = (∂R/∂y − ∂Q/∂z, ∂P/∂z − ∂R/∂x, ∂Q/∂x − ∂P/∂y) — the "cross-derivatives" between different components. In the fluid analogy: if you placed a tiny paddle wheel at a point in the fluid, would it spin? Curl measures this local rotation. Its direction gives the axis of rotation (by the right-hand rule), and its magnitude gives the angular speed. A field with ∇×F = **0** everywhere is called **irrotational** or **conservative** — it has no local spin. Conservative fields are exactly the gradient fields (F = ∇φ for some scalar potential φ), and line integrals around closed loops in such fields are always zero.

Both operations are organized through the **del operator** ∇ = (∂/∂x, ∂/∂y, ∂/∂z) treated as a formal vector. Divergence is the dot product ∇·F (scalar output), and curl is the cross product ∇×F (vector output). This notation is more than a mnemonic — the antisymmetry of the cross product correctly captures why curl reverses when you flip orientation, and why the identity ∇·(∇×F) = 0 holds identically (the divergence of any curl is zero). These two operations are the key ingredients in the major theorems ahead — Green's theorem in the plane, Stokes' theorem on surfaces, and the Divergence Theorem in space — which relate curl and divergence to the boundary behavior of vector fields.
