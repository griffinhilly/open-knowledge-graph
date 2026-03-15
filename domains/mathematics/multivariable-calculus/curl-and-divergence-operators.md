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
