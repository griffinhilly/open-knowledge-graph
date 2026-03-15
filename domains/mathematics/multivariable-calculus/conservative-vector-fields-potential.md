---
id: conservative-vector-fields-potential
title: Conservative Vector Fields and Potential Functions
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: line-integrals-definition-properties
  type: hard
builds-toward:
- greens-theorem-applications
tags:
- conservative-fields
- potential
- path-independence
stage: formal-systems
status: draft
---

# Conservative Vector Fields and Potential Functions

## Core Idea
A vector field F is conservative if F = ∇f for some scalar potential f. For conservative fields, ∫_C F · dr depends only on endpoints (path-independent). If F is conservative and curl-free (∂Q/∂x = ∂P/∂y for F = ⟨P, Q⟩), then ∫ F · dr around any closed path is zero.
