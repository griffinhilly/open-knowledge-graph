---
id: scalar-vector-potentials
title: Scalar and Vector Potentials
domain: physics
course: electrodynamics
prerequisites:
- id: maxwell-equations-differential-form
  type: hard
- id: curl-and-divergence
  type: hard
builds-toward:
- retarded-potentials
- gauge-transformations
tags:
- potentials
- alternative-formulation
stage: advanced
status: draft
---

# Scalar and Vector Potentials

## Core Idea
Instead of working directly with E and B fields, one can use the scalar potential φ and vector potential A such that E = -∇φ - ∂A/∂t and B = ∇ × A. These potentials automatically satisfy the two Maxwell equations with no sources (∇·B = 0 and ∇ × E = -∂B/∂t). Potentials are mathematically more convenient and form the foundation for quantum mechanics and quantum field theory.
