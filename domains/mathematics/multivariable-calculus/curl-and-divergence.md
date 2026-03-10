---
id: curl-and-divergence
title: Curl and Divergence
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: partial-derivatives
  type: hard
- id: vector-fields
  type: hard
- id: cross-product
  type: soft
- id: greens-theorem
  type: soft
builds-toward:
- stokes-theorem
- divergence-theorem
tags:
- curl
- divergence
- del-operator
- rotation
- flux
stage: formal-systems
status: draft
---

# Curl and Divergence

## Core Idea
For F = ⟨P, Q, R⟩, the curl is curl F = ∇ × F = ⟨R_y − Q_z, P_z − R_x, Q_x − P_y⟩, measuring the local rotation of the field. The divergence is div F = ∇ · F = P_x + Q_y + R_z, measuring the local expansion (source strength) or contraction (sink strength) of the field. A conservative field has curl F = 0 everywhere. A field with div F = 0 is called incompressible (solenoid). Both operators use the nabla (del) operator ∇ = ⟨∂/∂x, ∂/∂y, ∂/∂z⟩.

## How It's Best Learned
Physical intuition first: curl measures rotation (put a paddle wheel in the fluid — does it spin?), divergence measures expansion (is fluid being created or destroyed at this point?). Then derive the formulas from the del operator notation. The identities div(curl F) = 0 and curl(∇f) = 0 are fundamental and worth verifying by computation.

## Common Misconceptions
- Curl is a vector quantity in ℝ³; divergence is a scalar. The 2D 'curl' (∂Q/∂x − ∂P/∂y) from Green's theorem is the z-component of the 3D curl.
- curl F = 0 implies F is conservative only on simply connected domains.
- The del operator ∇ must be applied carefully: ∇ × F uses the cross product formula with ∂/∂x etc., not component-wise multiplication.
