---
id: gram-schmidt-process
title: Gram-Schmidt Orthogonalization Process
domain: mathematics
course: linear-algebra
prerequisites:
- id: orthogonal-projections
  type: hard
builds-toward:
- least-squares-approximation
tags:
- gram-schmidt
- orthogonalization
- qr-decomposition
stage: formal-systems
status: draft
---

# Gram-Schmidt Orthogonalization Process

## Core Idea
Gram–Schmidt converts a linearly independent set v₁, ..., vₖ into an orthonormal set e₁, ..., eₖ by recursively subtracting projections. At step i: orthogonalize via u_i = v_i − Σⱼ₌₁^{i-1} ⟨v_i, e_j⟩ e_j, then normalize e_i = u_i/‖u_i‖. This process produces the QR decomposition when applied to matrix columns.
