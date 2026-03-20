---
id: multipole-expansion-radiation
title: Multipole Expansion and Far-Field Radiation
domain: physics
course: electrodynamics
prerequisites:
- id: radiation-from-accelerated-charges
  type: hard
- id: multivariable-calculus
  type: soft
builds-toward:
- electric-dipole-radiation
tags:
- multipole
- expansion
- far-field
stage: advanced
status: draft
---

# Multipole Expansion and Far-Field Radiation

## Core Idea
For radiation at distances large compared to source size, multipole expansion systematically approximates far fields. The dipole moment p(t) dominates for non-relativistic sources; higher moments are suppressed by factors of (a/c)². This reveals which source properties radiate effectively.

## Explainer

From your study of radiation from accelerated charges, you know that a single accelerating charge radiates power P = q²a²/(6πε₀c³) (the Larmor formula). Real systems — antennas, atoms, molecules — involve many charges moving in a bounded region. **Multipole expansion** is the systematic technique for computing the radiation from such a source without tracking every charge individually, by instead characterizing the source through a hierarchy of moments.

The key observation is that if the source region has size a and the observation point is at distance r >> a, then the retardation delays from different parts of the source differ by at most Δt ~ a/c. If the source oscillates at frequency ω, this delay represents a phase shift of roughly ωa/c = ka (where k = ω/c is the wavenumber). When ka << 1 (the source is much smaller than a wavelength), this phase shift is small, and the entire source can be described by just a few integrated quantities — the multipole moments — rather than its detailed internal structure.

The expansion proceeds by expanding the retarded potential in powers of (a/r): the leading term gives the **electric dipole** contribution, the next gives magnetic dipole and electric quadrupole, and so on. The electric dipole contribution depends on p̈ = d²p/dt² (the acceleration of the dipole moment p = Σqᵢrᵢ). The radiated power from electric dipole radiation is P_dipole = p̈²/(6πε₀c³). Each successive term in the expansion is suppressed by an additional factor of (ka)² = (a/λ)². For a typical radio antenna or a vibrating molecule where a << λ, the dipole term overwhelmingly dominates: quadrupole radiation is suppressed by a factor (a/λ)² relative to dipole radiation.

This hierarchy has profound physical consequences. A system with no time-varying dipole moment — because total charge is zero and it oscillates symmetrically — radiates primarily through the next term (quadrupole or magnetic dipole). Gravitational wave sources (like merging black holes) are even more restricted: there is no monopole radiation (energy conservation) and no dipole radiation (momentum conservation), so the dominant radiation is **quadrupole**, suppressed by (v/c)² relative to a comparable electromagnetic dipole. Understanding which multipoles are active in a given source tells you the angular pattern, the frequency dependence of the power (P_dipole ∝ ω⁴), and the total radiated intensity — making multipole expansion the universal language of radiation physics.
