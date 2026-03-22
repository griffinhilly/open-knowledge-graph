---
id: electric-flux-and-gauss-law
title: Electric Flux and Gauss's Law
domain: physics
course: electrodynamics
prerequisites:
- id: electric-field-and-coulombs-law
  type: hard
- id: multivariable-calculus
  type: hard
builds-toward:
- maxwells-equations-integral-form
tags:
- gauss-law
- flux
- symmetry
stage: advanced
status: draft
---

# Electric Flux and Gauss's Law

## Core Idea
Gauss's law states that the electric flux through a closed surface equals the enclosed charge divided by ε₀. It emerges from Coulomb's law via symmetry arguments and provides an elegant method for calculating electric fields in high-symmetry situations.

## Questions

```yaml
- question: "A student applies Gauss's law to an infinite plane of uniform charge density σ, using a cylindrical 'pillbox' Gaussian surface that straddles the plane, with flat caps of area A on each side. She writes E × A = σA/ε₀ and solves to get E = σ/ε₀. Her answer is off by a factor of 2. What did she miss?"
  type: multiple-choice
  options:
    - "She used the wrong formula for the enclosed charge"
    - "She should have used a spherical Gaussian surface for a plane of charge"
    - "The electric field passes through both caps of the pillbox — one on each side of the plane — so the total flux is 2E × A, not E × A, giving E = σ/(2ε₀)"
    - "Gauss's law cannot be applied to infinite planes because they lack the required symmetry"
  answer: 2
  explanation: "The infinite plane produces a field pointing away from the surface on both sides. The pillbox has two flat caps — one above the plane and one below — and field lines exit through both. The correct flux equation is 2EA = σA/ε₀, giving E = σ/(2ε₀). Forgetting the factor of 2 is the most common error in this geometry. The curved side of the pillbox contributes no flux because the field is parallel to it (perpendicular to the area normal). This example illustrates why carefully identifying which surfaces contribute flux — and how much — is the key skill in applying Gauss's law."

- question: "Why does the net electric flux through a closed surface remain the same whether you use a sphere, a cube, or an irregular blob as your Gaussian surface, as long as the enclosed charge is the same?"
  type: multiple-choice
  options:
    - "Because electric fields are uniform throughout space, so any surface intercepts the same field"
    - "Because charges outside the surface don't affect the field at all"
    - "Because every field line that enters a closed surface from an outside charge must also exit it, contributing zero net flux; only enclosed sources determine the total outward flux"
    - "Because Gauss's law only holds for surfaces that match the symmetry of the charge distribution"
  answer: 2
  explanation: "This is the profound geometrical insight behind Gauss's law. A charge outside the closed surface does produce a field inside and at the surface — option B is false. But every field line from that external charge that enters the surface must, by continuity, also exit the surface. The entry and exit contributions cancel, giving zero net flux from any external charge. Only sources enclosed within the surface have field lines that originate inside and exit outward without a matching return — so net flux = Q_enc/ε₀ regardless of surface shape. This independence from surface shape is what makes Gauss's law so powerful and general."

- question: "A charge located outside a closed Gaussian surface contributes zero net electric flux through that surface, because any field line it sends into the surface must also exit the surface."
  type: true-false
  answer: true
  explanation: "This is the key to understanding why Gauss's law depends only on enclosed charge. An external charge does create a field everywhere, including at and inside the Gaussian surface — it's not that the field vanishes outside. Rather, every field line from the external charge that pierces the surface on one side must pierce it again on the other side going outward. The two contributions are equal and opposite, summing to zero net flux. Internal charges, by contrast, send field lines outward through the surface with no matching inward contribution."

- question: "The specific shape of your Gaussian surface affects the total electric flux through it, because surfaces with different shapes intercept field lines at different angles and over different areas."
  type: true-false
  answer: false
  explanation: "Total net flux through any closed surface enclosing the same charge is always Q_enc/ε₀, regardless of shape, size, or orientation. The shape affects the difficulty of computing the surface integral — a sphere concentric with a point charge makes E constant and parallel to dA everywhere, collapsing the integral to E × 4πr² — but it doesn't change the result. A lopsided irregular blob enclosing the same charge gives the same total flux as a perfect sphere. This shape-independence is not a computational convenience; it is the physical content of Gauss's law."

- question: "Why does the r² in the denominator of Coulomb's law cancel exactly with the r² surface area of a sphere, and why is this more than a mathematical coincidence?"
  type: short-answer
  answer: "The electric field from a point charge falls as 1/r² — at radius r, the field is q/(4πε₀r²). The surface area of a sphere of radius r grows as r² — specifically, 4πr². When you compute the flux, these two factors cancel: the weakening field exactly compensates for the larger sphere, giving the same total flux q/ε₀ at any radius. This cancellation reflects the geometry of three-dimensional space. In 3D, field lines spread outward in all directions simultaneously; the number of lines per unit area decreases as 1/r² because the total area grows as r². The 1/r² field law is precisely what's needed for the flux through any enclosing surface to be constant — it is the unique signature of a 3D inverse-square law. In two dimensions, the analogous law would be 1/r, and in four dimensions, 1/r³."
  explanation: "This connection between the inverse-square law and 3D geometry is what gives Gauss's law its deep significance. It's not just a useful computational trick — it reveals that the form of Coulomb's law is tied to the dimensionality of space. This is why Gauss's law is one of Maxwell's four equations: it encodes something fundamental about how electric fields relate to their sources in the geometry of our universe."
```

## Explainer

You already know Coulomb's law: the electric field from a point charge q falls off as E = kq/r² = q/(4πε₀r²). Now ask a different question: instead of knowing the field at one point, can you characterize how much "field" passes through a closed surface surrounding the charge? Define **electric flux** Φ = ∮E⃗·dA⃗ as the surface integral of the field dotted with the outward-pointing area element. For a sphere of radius r surrounding a charge q, every part of the surface has E pointing radially outward with magnitude q/(4πε₀r²), and dA = r²sinθ dθ dφ. The integral gives Φ = [q/(4πε₀r²)] × 4πr² = q/ε₀. The r² in the denominator from the field and the r² in the numerator from the sphere's area cancel exactly. This cancellation is not a coincidence — it is a geometric consequence of living in three-dimensional space.

The profound insight of **Gauss's law** is that this result is independent of the shape of the surface and the distribution of the source charge. You can deform the sphere into any closed surface and the result stays Φ = Q_enc/ε₀. Why? Because field lines that enter the surface must also exit it (they can't end in empty space), and only the enclosed sources determine the net outward flux. Charge outside the closed surface contributes field lines that enter and exit in equal number, contributing zero net flux. This makes Gauss's law far more general than Coulomb's law in form, even though the two are mathematically equivalent (Gauss's law in integral form is Coulomb's law plus the superposition principle).

The practical power of Gauss's law is that in high-symmetry situations, you can **choose a Gaussian surface** where E is constant in magnitude and parallel to dA everywhere. Then ∮E⃗·dA⃗ = E × A_surface, and solving E × A = Q_enc/ε₀ gives E immediately. For a spherical charge distribution, use a concentric spherical Gaussian surface. For an infinite line charge (linear charge density λ), use a coaxial cylindrical surface of length L: E × 2πrL = λL/ε₀, so E = λ/(2πε₀r). For an infinite plane with surface charge density σ, use a pillbox straddling the surface: 2E × A = σA/ε₀, so E = σ/(2ε₀). These three geometries — sphere, cylinder, plane — are the canonical applications, and recognizing which one applies to a given problem is the main skill.

Gauss's law in differential form, ∇·E⃗ = ρ/ε₀, is one of Maxwell's four equations. The divergence ∇·E at a point measures the local "spreading out" of field lines, which equals the local charge density. A positive charge is a source (positive divergence); a negative charge is a sink (negative divergence). In regions with no charge, ∇·E = 0 — field lines neither begin nor end, they just pass through. This differential form is more general than the integral form because it applies locally, and it is this form that appears in Maxwell's unified theory of electromagnetism.
