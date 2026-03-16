---
id: higher-multipole-radiation
title: Magnetic Dipole and Higher Multipole Radiation
domain: physics
course: electrodynamics
prerequisites:
- id: electric-dipole-radiation
  type: hard
- id: multipole-expansion-fields
  type: hard
builds-toward:
- multipole-expansion-fields
tags:
- multipole
- higher-order
- weak-radiation
stage: advanced
status: draft
---

# Magnetic Dipole and Higher Multipole Radiation

## Core Idea
When electric dipole radiation vanishes (e.g., for parity reasons), magnetic dipole and electric quadrupole radiation become important. These higher-order multipoles radiate much more weakly, falling off as higher powers of frequency and size relative to wavelength. Understanding multipole radiation is essential for atomic physics, nuclear physics, and analyzing radiation from complex current distributions.

## Explainer

From your study of electric dipole radiation, you know that an oscillating charge distribution with a time-varying dipole moment p⃗(t) radiates electromagnetic waves with power P ∝ ω⁴|p⃗|². The radiation pattern is the familiar sin²θ donut shape, and the field falls off as 1/r. But what happens when the electric dipole moment is zero — either exactly (by symmetry) or by selection rule? The multipole expansion tells you: the next terms are the **magnetic dipole** (M1) and **electric quadrupole** (E2), but they radiate far more weakly.

The critical parameter governing how strongly each multipole radiates is the ratio a/λ, where a is the characteristic size of the source and λ is the emitted wavelength. For electric dipole radiation, radiated power scales as (a/λ)². For M1 and E2 radiation, it scales as (a/λ)⁴. For atoms, a ~ 10⁻¹⁰ m and visible light has λ ~ 10⁻⁷ m, giving a/λ ~ 10⁻³. So magnetic dipole and quadrupole transitions are suppressed by roughly a factor of (10⁻³)² = 10⁻⁶ relative to electric dipole transitions. This is why E1 transitions dominate atomic spectra: they are overwhelmingly faster. **Forbidden transitions** — M1 or E2 transitions in atoms where E1 is disallowed by selection rules — are so slow that they are only observable in very low-density environments (nebulae, for example) where collisions don't redistribute energy before the atom eventually radiates.

**Magnetic dipole radiation** arises from oscillating magnetic dipole moments, as produced by current loops or spinning charges. Its radiation pattern is identical to the electric dipole's, but the roles of E⃗ and B⃗ in the radiation field are swapped. **Electric quadrupole radiation** arises from oscillating second-moment distributions — charge configurations with no net dipole moment but with an asymmetric spread, like two dipoles of opposite orientation placed end to end. Its radiation pattern has four lobes rather than two. In nuclear physics, where nuclear radii (~10⁻¹⁵ m) and gamma-ray wavelengths (~10⁻¹² m) give a/λ ~ 10⁻³ as well, classifying gamma transitions as E1, M1, E2, M2, and so on directly determines their decay rates and reveals nuclear structure.

The selection rules that forbid E1 while permitting M1 or E2 come from conservation of angular momentum and parity. An E1 photon carries angular momentum ΔJ = 1 and changes parity; an M1 photon also carries ΔJ = 1 but does not change parity; an E2 photon carries ΔJ = 2 and does not change parity. When initial and final states have quantum numbers incompatible with E1 but compatible with M1 or E2, the lower multipole is forbidden and the higher one proceeds — slowly but inevitably. The competition between these channels, and the lifetimes they imply, is central to both atomic spectroscopy and nuclear gamma-ray physics.
