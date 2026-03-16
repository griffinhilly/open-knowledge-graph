---
id: electric-flux-and-divergence
title: Electric Flux and Divergence Theorem
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: electric-field-continuous-distributions
  type: hard
- id: surface-integrals-flux
  type: hard
- id: divergence-theorem
  type: hard
builds-toward:
- gauss-law-integral-form
tags:
- flux
- divergence
- integration
stage: formal-systems
status: draft
---

# Electric Flux and Divergence Theorem

## Core Idea
Electric flux through a surface is Φ = ∫E⋅dA. The divergence theorem relates flux through a closed surface to charge enclosed: ∮E⋅dA = Q_enclosed/ε₀, fundamental for Gauss's law.

## Explainer

You already know how to compute electric fields from continuous charge distributions by integrating Coulomb's law. **Electric flux** provides a complementary, often far more powerful perspective: instead of asking what field a source creates, ask how much field passes through a surface. Flux is the surface integral Φ = ∫E⋅dA — at each patch of the surface you take the component of E perpendicular to the surface (E⋅n̂) and sum it up over the entire area. Geometrically, flux counts how many field lines thread through the surface: if field lines are dense and perpendicular to the surface, flux is large; if they are sparse or graze the surface at shallow angles, flux is small.

The key physical insight is that for a closed surface surrounding a charge distribution, the total outward flux depends only on the enclosed charge — not on the shape of the surface or how the charges are arranged inside. This is Gauss's law in integral form: ∮E⋅dA = Q_enclosed/ε₀. To see why, picture a point charge q at the center of a sphere. The field radiates outward uniformly, so E = q/(4πε₀r²) everywhere on the sphere, and the total flux is E × 4πr² = q/ε₀. Now deform the sphere into any lumpy closed shape that still encloses q — field lines that enter the surface on one side must exit on another, and the total count does not change. The flux is a topological property of how many source lines originate inside.

This is where your prerequisite knowledge of the **divergence theorem** becomes essential. The divergence theorem (∮F⋅dA = ∫∇⋅F dV) converts a closed surface integral into a volume integral of the divergence. Applied to the electric field, it says that ∮E⋅dA equals ∫(∇⋅E)dV over the enclosed volume. Combining with Gauss's law gives ∇⋅E = ρ/ε₀ — the differential form of Gauss's law, which is one of Maxwell's four equations. The divergence of E at a point equals the charge density at that point divided by ε₀. Where there is positive charge, field lines diverge outward; where there is negative charge, they converge inward; in empty space, ∇⋅E = 0.

The practical power of flux calculations comes from exploiting symmetry. For a uniformly charged infinite plane, a cylinder, or a sphere, you can choose a Gaussian surface where E is constant in magnitude and always perpendicular (or parallel) to the surface. The integral ∮E⋅dA then reduces to E × A, and you can solve for E in one line — vastly simpler than the direct Coulomb integration you learned earlier. This trade-off — replacing an integral over the source with a cleverly chosen surface integral — is the method you will use repeatedly in computing fields for symmetric charge distributions.
