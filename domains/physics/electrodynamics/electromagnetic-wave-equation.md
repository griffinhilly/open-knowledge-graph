---
id: electromagnetic-wave-equation
title: Derivation of the Electromagnetic Wave Equation
domain: physics
course: electrodynamics
prerequisites:
- id: maxwell-equations-differential-form
  type: hard
- id: curl-and-divergence
  type: hard
- id: vector-calculus-identities
  type: soft
builds-toward:
- plane-electromagnetic-waves
- electromagnetic-wave-polarization
tags:
- wave-equation
- em-waves
- pdes
stage: advanced
status: draft
---

# Derivation of the Electromagnetic Wave Equation

## Core Idea
Taking the curl of Faraday's and Ampère-Maxwell laws and applying vector identities yields decoupled wave equations for E and B fields: ∇²E = μ₀ε₀∂²E/∂t² and ∇²B = μ₀ε₀∂²B/∂t². The wave speed c = 1/√(μ₀ε₀) emerges naturally and equals the experimentally measured speed of light. This derivation is perhaps the most profound result in classical physics, unifying electromagnetism and optics.

## How It's Best Learned
Work through the derivation carefully, noting each vector identity. Understand why the divergence-free condition (from charge conservation) is crucial for decoupling E and B.

## Common Misconceptions
- Thinking the wave equation applies separately to E and B; they are coupled through Maxwell's equations.
- Forgetting that the wave equation assumes no sources (ρ = 0, J = 0) in the region of interest.
