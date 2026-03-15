---
id: ampere-law-field
title: Ampere's Law and Magnetic Field Symmetry
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: biot-savart-field
  type: soft
- id: curl-and-divergence
  type: hard
- id: line-integrals-vector-fields
  type: hard
builds-toward:
- magnetic-field-solenoid
tags:
- ampere-law
- symmetry
- circulation
stage: formal-systems
status: draft
---

# Ampere's Law and Magnetic Field Symmetry

## Core Idea
Ampere's law states ∮ B⃗·d⃗ℓ = μ₀I_enc. For high-symmetry current distributions, choosing an Amperian loop aligned with that symmetry makes the circulation integral trivial. For a solenoid: B = μ₀nI inside, 0 outside. For a toroid: B = μ₀NI/(2πr) inside, 0 outside. Ampere's law is a direct consequence of the Biot-Savart law.
