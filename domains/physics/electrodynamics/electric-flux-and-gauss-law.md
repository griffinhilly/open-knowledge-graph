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
stage: abstract-reasoning
status: draft
---

# Electric Flux and Gauss's Law

## Core Idea
Gauss's law states that the electric flux through a closed surface equals the enclosed charge divided by ε₀. It emerges from Coulomb's law via symmetry arguments and provides an elegant method for calculating electric fields in high-symmetry situations.

## Explainer

You already know Coulomb's law: the electric field from a point charge q falls off as E = kq/r² = q/(4πε₀r²). Now ask a different question: instead of knowing the field at one point, can you characterize how much "field" passes through a closed surface surrounding the charge? Define **electric flux** Φ = ∮E⃗·dA⃗ as the surface integral of the field dotted with the outward-pointing area element. For a sphere of radius r surrounding a charge q, every part of the surface has E pointing radially outward with magnitude q/(4πε₀r²), and dA = r²sinθ dθ dφ. The integral gives Φ = [q/(4πε₀r²)] × 4πr² = q/ε₀. The r² in the denominator from the field and the r² in the numerator from the sphere's area cancel exactly. This cancellation is not a coincidence — it is a geometric consequence of living in three-dimensional space.

The profound insight of **Gauss's law** is that this result is independent of the shape of the surface and the distribution of the source charge. You can deform the sphere into any closed surface and the result stays Φ = Q_enc/ε₀. Why? Because field lines that enter the surface must also exit it (they can't end in empty space), and only the enclosed sources determine the net outward flux. Charge outside the closed surface contributes field lines that enter and exit in equal number, contributing zero net flux. This makes Gauss's law far more general than Coulomb's law in form, even though the two are mathematically equivalent (Gauss's law in integral form is Coulomb's law plus the superposition principle).

The practical power of Gauss's law is that in high-symmetry situations, you can **choose a Gaussian surface** where E is constant in magnitude and parallel to dA everywhere. Then ∮E⃗·dA⃗ = E × A_surface, and solving E × A = Q_enc/ε₀ gives E immediately. For a spherical charge distribution, use a concentric spherical Gaussian surface. For an infinite line charge (linear charge density λ), use a coaxial cylindrical surface of length L: E × 2πrL = λL/ε₀, so E = λ/(2πε₀r). For an infinite plane with surface charge density σ, use a pillbox straddling the surface: 2E × A = σA/ε₀, so E = σ/(2ε₀). These three geometries — sphere, cylinder, plane — are the canonical applications, and recognizing which one applies to a given problem is the main skill.

Gauss's law in differential form, ∇·E⃗ = ρ/ε₀, is one of Maxwell's four equations. The divergence ∇·E at a point measures the local "spreading out" of field lines, which equals the local charge density. A positive charge is a source (positive divergence); a negative charge is a sink (negative divergence). In regions with no charge, ∇·E = 0 — field lines neither begin nor end, they just pass through. This differential form is more general than the integral form because it applies locally, and it is this form that appears in Maxwell's unified theory of electromagnetism.
