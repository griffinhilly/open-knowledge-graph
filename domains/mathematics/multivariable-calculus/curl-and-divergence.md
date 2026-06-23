---
id: curl-and-divergence
title: Curl and Divergence of Vector Fields
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: conservative-fields-potential
  type: hard
- id: cross-product
  type: hard
- id: dot-cross-products-geometry
  type: soft
builds-toward:
- greens-theorem
- surface-integrals-flux
tags:
- curl
- divergence
- vector-calculus
stage: formal-systems
status: validated
---

# Curl and Divergence of Vector Fields

## Core Idea
The curl ∇ × F measures rotation and circulation of F; for F = ⟨P, Q, R⟩, curl F = ⟨(∂R/∂y − ∂Q/∂z), (∂P/∂z − ∂R/∂x), (∂Q/∂x − ∂P/∂y)⟩. The divergence ∇ · F = ∂P/∂x + ∂Q/∂y + ∂R/∂z measures net outflow. Both are fundamental to Green's, Stokes', and divergence theorems.

## Questions

```yaml
- question: "For a 2D vector field F = ⟨P, Q⟩, which expression gives the z-component of the curl (the scalar 2D curl)?"
  type: multiple-choice
  options:
    - "∂P/∂x + ∂Q/∂y"
    - "∂Q/∂x − ∂P/∂y"
    - "∂P/∂y − ∂Q/∂x"
    - "∂P/∂x − ∂Q/∂y"
  answer: 1
  explanation: "The 2D curl is ∂Q/∂x − ∂P/∂y — the cross-partial pattern with a minus sign. This is a common confusion point: the divergence uses the same partial derivatives but with a plus sign (∂P/∂x + ∂Q/∂y). Curl involves the 'cross' combination of partials, while divergence involves the 'straight' combination."

- question: "A vector field with zero divergence everywhere has no sources or sinks — fluid neither accumulates nor drains at any point."
  type: true-false
  answer: true
  explanation: "Divergence measures net outflow per unit volume at a point. Zero divergence means the field is divergence-free (or incompressible): as much flows into any region as flows out. This is exactly the condition of having no sources (positive divergence) or sinks (negative divergence). Incompressible fluid flow satisfies ∇ · F = 0 everywhere."

- question: "What does it mean physically if the curl of a vector field F is zero at every point in its domain?"
  type: short-answer
  answer: "The field is irrotational — there is no local rotation or swirling tendency at any point. On a simply connected domain, this is equivalent to F being a conservative field (having a scalar potential function)."
  explanation: "Curl measures the rotation/circulation tendency of a field. Imagine placing a tiny paddle wheel at a point: if curl F = 0, the wheel won't spin. Zero curl (irrotational) plus a simply connected domain guarantees F = ∇f for some scalar f — a conservative field where line integrals are path-independent."
```

## Explainer

Curl and divergence are the two fundamental ways to differentiate a vector field, and each captures a physically distinct property. **Divergence** asks: is fluid (or field) flowing out from a point, or converging into it? **Curl** asks: is the fluid spinning, and in which direction? Together they give a complete local picture of how a vector field behaves near any point.

Divergence is the simpler of the two. For F = ⟨P, Q, R⟩, the divergence is just ∇ · F = ∂P/∂x + ∂Q/∂y + ∂R/∂z — a scalar sum of how much each component is "spreading out" along its own axis. Positive divergence at a point means the field expands outward (a source); negative means it contracts inward (a sink). A field with zero divergence everywhere is called **solenoidal** or incompressible — magnetic fields and incompressible fluid velocity fields satisfy this.

Curl is more complex because it measures rotation, which is inherently a higher-dimensional concept. In 3D, curl F = ∇ × F is a vector (computed like a cross product with ∇ as one factor) that points along the axis of rotation by the right-hand rule. Its magnitude is the strength of the rotation. In 2D, the curl reduces to a single scalar — ∂Q/∂x − ∂P/∂y — which tells you whether field lines swirl counterclockwise (positive) or clockwise (negative). A field with zero curl everywhere is called **irrotational**, and on a simply connected domain, irrotational is equivalent to being conservative (having a potential function).

The key to not confusing curl and divergence is to remember their symbolic forms: divergence uses ∇ · F (dot product, mixes each component with its own axis), while curl uses ∇ × F (cross product, mixes components with *other* axes). This cross-mixing is exactly what detects rotation. The divergence theorem connects divergence to flux through a closed surface; Stokes' theorem connects curl to circulation around a closed curve — these theorems are where the physical meaning of curl and divergence is most powerfully expressed.
