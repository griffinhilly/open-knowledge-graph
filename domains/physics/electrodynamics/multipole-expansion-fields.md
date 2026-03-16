---
id: multipole-expansion-fields
title: Multipole Expansion of Electromagnetic Fields
domain: physics
course: electrodynamics
prerequisites:
- id: scalar-vector-potentials
  type: hard
- id: laplace-poisson-equations-electrostatics
  type: soft
- id: taylor-series
  type: soft
- id: spherical-coordinates
  type: soft
builds-toward:
- radiation-accelerating-charges
tags:
- multipole-expansion
- systematic-expansion
stage: advanced
status: draft
---

# Multipole Expansion of Electromagnetic Fields

## Core Idea
Multipole expansion systematically expresses electromagnetic fields far from localized sources as a series of monopole, dipole, quadrupole, and higher moments. Each term falls off as a higher power of 1/r, allowing truncation at low order for distant observation points. This expansion reveals which multipoles dominate in different frequency regimes and provides physical insight into radiation mechanisms.

## Explainer

From your study of scalar and vector potentials you know that once you have the charge and current distribution, the fields follow from the potentials via differential operations. The difficulty is that real sources are always extended — a molecule, an antenna, a nucleus — not a single point. The **multipole expansion** is a systematic way to describe what such a source looks like from far away, by expanding the potential in powers of (r'/r), where r' is the size of the source and r is your distance from it. When r ≫ r', each successive term in the expansion is smaller by a factor of r'/r.

The first term is the **monopole**: it depends only on the total charge Q and falls off as Q/r. An electrically neutral system — any atom or molecule — has zero monopole, so this term vanishes. The next term is the **dipole**: it depends on the charge distribution's first moment **p** = Σ qᵢ **r**ᵢ (or ∫ρ **r** dV for a continuous distribution) and falls off as 1/r². A water molecule has a permanent electric dipole moment; two charges ±q separated by distance d form a dipole with p = qd. Because most neutral objects have non-zero dipole moments, the dipole term often dominates at large distances. The next term is the **quadrupole**, falling off as 1/r³, followed by octupole at 1/r⁴, and so on. Each higher multipole requires finer spatial structure in the source to be nonzero, and each falls off faster with distance.

The Taylor series prerequisite makes the mathematical structure transparent. You expand 1/|**r** − **r**'| in Legendre polynomials (using spherical coordinates), and each Legendre polynomial P_ℓ(cos θ) corresponds to one multipole order: ℓ=0 is monopole, ℓ=1 is dipole, ℓ=2 is quadrupole. The physical content is that the source contributes to distant fields through an infinite hierarchy of shape descriptors — moments — and the hierarchy is ordered by how quickly each contribution decays with distance. Truncating at low order is valid whenever r ≫ r', which is precisely the far-field regime.

For radiation (time-varying sources), the same hierarchy applies but with important differences: all radiation fields fall off as 1/r (they must, to carry finite power through a sphere of any radius), but the radiated power from each multipole scales differently with frequency. **Electric dipole radiation** power scales as ω⁴; electric quadrupole scales as ω⁶; magnetic dipole as ω⁴ but suppressed by (v/c)². This is why the dipole approximation dominates in antenna theory and molecular spectroscopy: for slowly varying sources at large distances, the monopole and dipole terms tell you nearly everything, and the expansion provides the systematic framework to know exactly what you are neglecting when you stop there.
