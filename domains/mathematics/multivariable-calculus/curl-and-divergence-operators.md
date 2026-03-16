---
id: curl-and-divergence-operators
title: Curl and Divergence of Vector Fields
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: vector-fields
  type: hard
builds-toward:
- stokes-theorem-applications
- divergence-theorem-applications
tags:
- curl
- divergence
- differential-operators
stage: formal-systems
status: draft
---

# Curl and Divergence of Vector Fields

## Core Idea
For F = ⟨P, Q, R⟩, the curl is ∇ × F = ⟨∂R/∂y − ∂Q/∂z, ∂P/∂z − ∂R/∂x, ∂Q/∂x − ∂P/∂y⟩, measuring rotation. The divergence ∇ · F = ∂P/∂x + ∂Q/∂y + ∂R/∂z measures net outflow. For conservative F, curl(F) = 0.

## Explainer

From your study of vector fields, you know that a vector field assigns a vector to each point in space — think of wind velocity, the force of gravity, or fluid flow. **Divergence** and **curl** are two differential operators that measure fundamentally different aspects of how a vector field varies in space. Both are built from partial derivatives of the components, but they extract different geometric information: divergence measures spreading or concentrating, while curl measures spinning.

**Divergence** answers the question: is this point a source or a sink? Formally, div(F) = ∇ · F = ∂P/∂x + ∂Q/∂y + ∂R/∂z. Positive divergence at a point means nearby flow vectors are pointing outward from that region — the point acts like a source, as if fluid were being emitted there. Negative divergence means vectors converge inward — the point is a sink. Zero divergence everywhere means the fluid is **incompressible**: as much flows in as flows out everywhere, volume is conserved. Imagine enclosing a region in a tiny balloon; the divergence measures the rate at which the balloon inflates or deflates.

**Curl** answers: is there rotation? For F = ⟨P, Q, R⟩, the curl ∇ × F is a vector field whose direction gives the axis of local rotation and whose magnitude gives the rate of rotation. In the 2D special case — which uses only the z-component ∂Q/∂x − ∂P/∂y — the curl tells you whether a tiny paddle wheel placed in the flow would spin counterclockwise (positive) or clockwise (negative). A field with curl = 0 everywhere is called **irrotational**, which you already know is equivalent to being conservative on simply connected domains. This connects curl directly to path independence: the line integral of F is path-independent if and only if curl(F) = 0.

Two key identities tie these operators together: curl(∇f) = 0 for any scalar function f, and div(curl F) = 0 for any vector field F. In words: gradient fields are always irrotational, and curl fields always have zero divergence. These identities encode deep topological structure — they express which fields can be "derived from" a potential function or a vector potential. They also set the stage for Stokes' theorem (which relates curl over a surface to circulation around its boundary) and the divergence theorem (which relates divergence over a volume to flux through its bounding surface), both of which make these abstract operators computationally decisive.
