---
id: curl-and-divergence
title: Curl and Divergence of Vector Fields
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: conservative-fields-potential
  type: hard
- id: cross-product-3d
  type: hard
builds-toward:
- greens-theorem
- surface-integrals-flux
tags:
- curl
- divergence
- vector-calculus
stage: formal-systems
status: draft
---

# Curl and Divergence of Vector Fields

## Core Idea
The curl ∇ × F measures rotation and circulation of F; for F = ⟨P, Q, R⟩, curl F = ⟨(∂R/∂y − ∂Q/∂z), (∂P/∂z − ∂R/∂x), (∂Q/∂x − ∂P/∂y)⟩. The divergence ∇ · F = ∂P/∂x + ∂Q/∂y + ∂R/∂z measures net outflow. Both are fundamental to Green's, Stokes', and divergence theorems.
