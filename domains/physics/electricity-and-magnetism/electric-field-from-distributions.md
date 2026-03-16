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

## Explainer

You already know from Coulomb's law that the field from a single point charge falls off as 1/r² in a radial direction. You also know the superposition principle: fields from multiple charges add as vectors. This topic is simply the logical extension of superposition to infinitely many infinitesimal charges spread across a line, surface, or volume. Instead of summing discrete contributions, you integrate continuous ones.

The central idea is to replace the discrete sum ΣkqᵢR̂ᵢ/rᵢ² with an integral. If charge is spread along a line with **linear charge density** λ (charge per unit length), each infinitesimal element dℓ carries charge dq = λ dℓ and contributes a field dE = (1/4πε₀)(λ dℓ/r²)r̂. You integrate this over the whole line. Similarly, **surface charge density** σ gives dq = σ dA, and **volume charge density** ρ gives dq = ρ dV. The vector nature of the integral is what makes the calculation challenging: both the magnitude 1/r² and the direction r̂ change with each source element's position, so you must often work in components.

The most important skill is recognizing when symmetry makes the integral tractable or unnecessary. For an infinite line of charge, all field components parallel to the line cancel by symmetry — only the radial component survives, and the integral reduces to a simple one-dimensional computation. For an infinite plane of surface charge, only the normal component survives. These symmetric cases are worth memorizing as building blocks: infinite line gives E = λ/(2πε₀r), infinite plane gives E = σ/(2ε₀). When you later encounter Gauss's law, you will see that these same results emerge more elegantly from symmetry arguments alone — but the direct integration here builds the intuition for *why* symmetry matters.

For less symmetric distributions, the integration becomes a genuine triple integral over volume. Your prerequisite knowledge of triple integrals applies directly: you choose a coordinate system suited to the geometry (spherical for spheres, cylindrical for cylinders), express r and r̂ in those coordinates, and carry out the integral component by component. The result is always a vector field — every point in space gets assigned a direction and magnitude telling you the force per unit charge that a test charge would feel there.
