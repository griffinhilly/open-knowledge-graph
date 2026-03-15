---
id: electric-field-from-distributions
title: Electric Field from Charge Distributions
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: coulomb-force-superposition
  type: hard
- id: triple-integrals
  type: soft
builds-toward:
- gauss-law-symmetry
tags:
- field
- distributions
- integration
stage: formal-systems
status: draft
---

# Electric Field from Charge Distributions

## Core Idea
For extended charge distributions with linear, surface, or volume charge densities (λ, σ, ρ), the electric field is found by integrating Coulomb contributions: E⃗(r⃗) = (1/4πε₀) ∫ (ρ(r⃗′)/|r⃗−r⃗′|²) r̂ dV′. Symmetric configurations (spheres, cylinders, planes) yield closed-form results or simplify via Gauss's law.
