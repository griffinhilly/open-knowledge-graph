---
id: dielectric-susceptibility-permittivity
title: Dielectric Susceptibility and Permittivity
domain: physics
course: electrodynamics
prerequisites:
- id: electric-field
  type: hard
- id: dielectrics
  type: hard
builds-toward:
- frequency-dependent-permittivity
- electromagnetic-waves-in-dielectrics
tags:
- dielectrics
- polarization
- constitutive-relations
stage: advanced
status: draft
---

# Dielectric Susceptibility and Permittivity

## Core Idea
The electric displacement field D relates to the field E and polarization P through D = ε₀E + P. The dielectric susceptibility χ = P/(ε₀E) and relative permittivity εᵣ = 1 + χ characterize the linear response of materials to electric fields.

## How It's Best Learned
Relate susceptibility to microscopic polarizability through the Lorentz field concept. Calculate for simple models (atomic dipoles, charged particles in potential wells).

## Explainer

You already know from studying dielectrics and electric fields that placing a material between capacitor plates reduces the field inside. The reason is that the material becomes **polarized** — its positive and negative charges shift slightly in opposite directions in response to the applied field, creating tiny electric dipoles throughout. **Dielectric susceptibility** χ and **permittivity** ε are the mathematical tools that quantify this response precisely.

The key insight is that inside a dielectric, the electric field has two types of sources: the free charges you deliberately placed (on capacitor plates, say) and the bound charges created by polarization. The **polarization** P⃗ describes the electric dipole moment density — how strongly and in which direction the material has polarized per unit volume. The relationship P⃗ = ε₀χE⃗ defines the susceptibility χ: it measures how strongly the material polarizes per unit of applied field. A large χ means the material responds strongly; a χ near zero means the material is nearly inert. In vacuum, there is no material to polarize, so χ = 0.

The **electric displacement field** D⃗ = ε₀E⃗ + P⃗ is constructed specifically to isolate the contribution of free charges. Gauss's law takes the clean form ∇·D⃗ = ρ_free, avoiding the complication of tracking bound charges separately. In a linear, isotropic medium, substituting P⃗ = ε₀χE⃗ gives D⃗ = ε₀(1 + χ)E⃗ = ε₀εᵣE⃗, where the **relative permittivity** εᵣ = 1 + χ. For vacuum, εᵣ = 1; for typical dielectrics, εᵣ ranges from about 2 (most plastics) to 80 (water), meaning water's molecular polarization response is enormous compared to its free-space value.

This framework matters because it cleanly separates what free charges do from what the material does in response. Boundary value problems at dielectric interfaces use the continuity of the tangential component of E⃗ and the normal component of D⃗ (in the absence of free surface charge) — conditions that follow directly from Maxwell's equations written in terms of D⃗ and E⃗. The susceptibility framework also generalizes naturally: when χ becomes frequency-dependent, you get dispersion and optical phenomena like refraction; when χ depends on field strength, you get nonlinear optics. The linear response described here is the foundation for all of those richer behaviors.
