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
status: validated
---

# Electric Flux and Divergence Theorem

## Core Idea
Electric flux through a surface is Φ = ∫E⋅dA. The divergence theorem relates flux through a closed surface to charge enclosed: ∮E⋅dA = Q_enclosed/ε₀, fundamental for Gauss's law.

## Questions

```yaml
- question: "A point charge +q sits inside a small sphere, and you calculate the total outward electric flux through the sphere's surface. You then replace the sphere with a much larger cube that also encloses +q. How does the flux through the cube compare to the flux through the sphere?"
  type: multiple-choice
  options:
    - "The flux through the cube is larger — the cube's surface area is greater, so more field lines pass through it."
    - "The flux through the cube is smaller — the field is weaker at the greater distance from the charge, reducing flux."
    - "The flux through the cube equals the flux through the sphere — only the enclosed charge determines total outward flux."
    - "The flux through the cube is zero — field lines strike the flat faces at varying angles and cancel out."
  answer: 2
  explanation: "Gauss's law states that total outward flux through any closed surface equals Q_enclosed/ε₀ — it depends only on the enclosed charge, not on the shape or size of the surface. Options A and B reflect a common confusion: while field strength does decrease with distance (less flux per unit area), the cube's larger surface area exactly compensates, leaving total flux unchanged. This is the topological insight: flux counts field lines originating inside, and that count does not change when you change the surface shape."

- question: "In a region of space where ∇·E = 0 everywhere, what must be true?"
  type: multiple-choice
  options:
    - "The electric field E is zero throughout the region."
    - "There are no free charges in the region — the charge density ρ = 0."
    - "The electric field has constant magnitude and direction throughout the region."
    - "The region is enclosed by a conducting shell that shields it from external fields."
  answer: 1
  explanation: "The differential form of Gauss's law is ∇·E = ρ/ε₀. If ∇·E = 0, then ρ = 0 — there is no charge density at those points. The field can still be nonzero (field lines from external charges can thread through the region), it just has no sources or sinks inside. Option A confuses zero divergence with zero field; option C confuses it with a uniform field. Divergence measures whether field lines spread from or converge to a point, not the field's magnitude."

- question: "The total electric flux through any closed surface depends only on the net charge enclosed within it, not on the shape or size of the surface."
  type: true-false
  answer: true
  explanation: "True — this is Gauss's law: ∮E·dA = Q_enclosed/ε₀. The shape and size of the Gaussian surface are irrelevant. Intuitively, flux counts field lines threading through the surface, and every field line originating from a charge inside must pass through any closed surface surrounding that charge, regardless of how that surface is shaped or how large it is."

- question: "Increasing the radius of a spherical Gaussian surface surrounding a fixed point charge will increase the total electric flux through the surface."
  type: true-false
  answer: false
  explanation: "False. The total flux equals Q_enclosed/ε₀ and does not depend on radius. While field strength decreases as 1/r², surface area increases as 4πr², and the two effects cancel exactly: E × 4πr² = (q/4πε₀r²) × 4πr² = q/ε₀, independent of r. This constancy is precisely why Gauss's law is powerful — the Gaussian surface can be chosen for geometric convenience without affecting the result."

- question: "Explain why the total outward flux through a closed surface depends only on the enclosed charge and not on the shape or size of the surface."
  type: short-answer
  answer: "Field lines from a charge radiate outward continuously and do not terminate in empty space. Any closed surface surrounding the charge will be threaded by all of those field lines — each one must pass through the surface to reach infinity. Reshaping or enlarging the surface does not create or destroy field lines; it only changes which patch of surface each line crosses. The total count of field lines threading the surface is therefore determined entirely by how many originate inside — that is, by the enclosed charge. The divergence theorem makes this precise: ∮E·dA = ∫∇·E dV = ∫(ρ/ε₀) dV = Q_enclosed/ε₀."
  explanation: "Flux is a topological count, not a local measurement. Field lines from charges outside the surface enter on one side and exit on the other, contributing zero net flux. Only sources (positive charges) and sinks (negative charges) inside the surface generate net outward or inward flux — this is why only the enclosed charge matters."
```

## Explainer

You already know how to compute electric fields from continuous charge distributions by integrating Coulomb's law. **Electric flux** provides a complementary, often far more powerful perspective: instead of asking what field a source creates, ask how much field passes through a surface. Flux is the surface integral Φ = ∫E⋅dA — at each patch of the surface you take the component of E perpendicular to the surface (E⋅n̂) and sum it up over the entire area. Geometrically, flux counts how many field lines thread through the surface: if field lines are dense and perpendicular to the surface, flux is large; if they are sparse or graze the surface at shallow angles, flux is small.

The key physical insight is that for a closed surface surrounding a charge distribution, the total outward flux depends only on the enclosed charge — not on the shape of the surface or how the charges are arranged inside. This is Gauss's law in integral form: ∮E⋅dA = Q_enclosed/ε₀. To see why, picture a point charge q at the center of a sphere. The field radiates outward uniformly, so E = q/(4πε₀r²) everywhere on the sphere, and the total flux is E × 4πr² = q/ε₀. Now deform the sphere into any lumpy closed shape that still encloses q — field lines that enter the surface on one side must exit on another, and the total count does not change. The flux is a topological property of how many source lines originate inside.

This is where your prerequisite knowledge of the **divergence theorem** becomes essential. The divergence theorem (∮F⋅dA = ∫∇⋅F dV) converts a closed surface integral into a volume integral of the divergence. Applied to the electric field, it says that ∮E⋅dA equals ∫(∇⋅E)dV over the enclosed volume. Combining with Gauss's law gives ∇⋅E = ρ/ε₀ — the differential form of Gauss's law, which is one of Maxwell's four equations. The divergence of E at a point equals the charge density at that point divided by ε₀. Where there is positive charge, field lines diverge outward; where there is negative charge, they converge inward; in empty space, ∇⋅E = 0.

The practical power of flux calculations comes from exploiting symmetry. For a uniformly charged infinite plane, a cylinder, or a sphere, you can choose a Gaussian surface where E is constant in magnitude and always perpendicular (or parallel) to the surface. The integral ∮E⋅dA then reduces to E × A, and you can solve for E in one line — vastly simpler than the direct Coulomb integration you learned earlier. This trade-off — replacing an integral over the source with a cleverly chosen surface integral — is the method you will use repeatedly in computing fields for symmetric charge distributions.
