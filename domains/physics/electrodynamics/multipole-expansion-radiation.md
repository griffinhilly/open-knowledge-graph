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
stage: expert
status: draft
---

# Multipole Expansion and Far-Field Radiation

## Core Idea
For radiation at distances large compared to source size, multipole expansion systematically approximates far fields. The dipole moment p(t) dominates for non-relativistic sources; higher moments are suppressed by factors of (a/c)². This reveals which source properties radiate effectively.

## Questions

```yaml
- question: "A small antenna oscillates at frequency ω. Its charge distribution is perfectly symmetric, so the electric dipole moment p = Σqᵢrᵢ is identically zero at all times. What is the dominant radiation from this antenna?"
  type: multiple-choice
  options:
    - "The antenna still radiates electric dipole radiation, because the individual charges still accelerate"
    - "No radiation occurs, since the dipole moment is zero and dipole radiation is the only significant contribution for small antennas"
    - "Magnetic dipole or electric quadrupole radiation dominates, suppressed by a factor of (ka)² relative to what dipole would have been"
    - "The radiation pattern is identical to dipole radiation, but weaker by a factor of ka"
  answer: 2
  explanation: "When the dipole moment vanishes by symmetry, the dipole term in the multipole expansion is zero, and the next terms — magnetic dipole and electric quadrupole — dominate. These are suppressed by a factor (ka)² = (a/λ)² relative to electric dipole radiation. Dipole radiation requires a time-varying dipole moment; if that moment is zero, the leading-order radiation comes from the next multipole. This is exactly the situation for gravitational radiation: conservation laws forbid monopole and dipole gravitational radiation, forcing the dominant emission to be quadrupole."

- question: "A small dipole antenna radiates at frequency f. If the frequency is doubled while the dipole moment amplitude is held constant, what happens to the radiated power?"
  type: multiple-choice
  options:
    - "The power doubles, since power is proportional to frequency"
    - "The power quadruples, since power is proportional to frequency squared"
    - "The power increases by a factor of 16, since dipole radiated power scales as ω⁴"
    - "The power is unchanged, since the dipole moment amplitude is the same"
  answer: 2
  explanation: "The electric dipole radiated power is P = p̈²/(6πε₀c³). For a dipole moment oscillating as p(t) = p₀cos(ωt), we have p̈ = −ω²p₀cos(ωt), so p̈² ∝ ω⁴. Doubling the frequency (ω → 2ω) increases the power by 2⁴ = 16. This strong frequency dependence is why higher-frequency radiation is so intense, and why efficient generation at low frequencies requires large antenna structures or high dipole moments to compensate."

- question: "For a source much smaller than a wavelength (ka << 1), the multipole expansion converges rapidly because higher multipole contributions are suppressed by successive powers of (ka)²."
  type: true-false
  answer: true
  explanation: "This is the physical foundation of the multipole approach. When the source size a is small compared to the wavelength λ = 2π/k, the parameter ka = 2πa/λ << 1. Each successive multipole term carries an extra factor of (ka)², making the series converge rapidly. The electric dipole term then provides an excellent approximation by itself, without needing to track the detailed internal structure of the source."

- question: "A system of two equal and opposite charges oscillating symmetrically about the origin has no net electric dipole moment, so it cannot radiate electromagnetic energy."
  type: true-false
  answer: false
  explanation: "A vanishing dipole moment eliminates *dipole* radiation, but not all radiation. Such a system would still radiate through electric quadrupole (and possibly magnetic dipole) contributions, though suppressed by a factor (ka)² relative to dipole. Only a system with zero for *all* multipole moments would be completely non-radiating — which does not occur for oscillating charge distributions. The statement reflects the misconception that dipole radiation exhausts all radiation mechanisms."

- question: "Why do gravitational waves from merging black holes radiate only through the quadrupole moment, and what does this tell you about the fundamental constraints on gravitational radiation?"
  type: short-answer
  answer: "Monopole gravitational radiation is forbidden by energy conservation — a changing mass monopole would imply changing total mass, which is forbidden. Dipole gravitational radiation is forbidden by momentum conservation — a changing gravitational dipole moment (Σmᵢrᵢ = M·R_cm) would require a net external force on the system. With monopole and dipole both eliminated by conservation laws, the leading gravitational radiation is quadrupole, suppressed by (v/c)² relative to electromagnetic dipole radiation of comparable sources. This is why gravitational waves are extraordinarily weak and required kilometer-scale interferometers to detect."
  explanation: "The conservation law argument is fundamental: each suppressed multipole order corresponds to a conserved quantity (mass, momentum) that forbids lower-order radiation. This hierarchy — monopole and dipole forbidden, quadrupole the first allowed term — explains the extreme weakness of gravitational waves even from spectacular astrophysical events."
```

## Explainer

From your study of radiation from accelerated charges, you know that a single accelerating charge radiates power P = q²a²/(6πε₀c³) (the Larmor formula). Real systems — antennas, atoms, molecules — involve many charges moving in a bounded region. **Multipole expansion** is the systematic technique for computing the radiation from such a source without tracking every charge individually, by instead characterizing the source through a hierarchy of moments.

The key observation is that if the source region has size a and the observation point is at distance r >> a, then the retardation delays from different parts of the source differ by at most Δt ~ a/c. If the source oscillates at frequency ω, this delay represents a phase shift of roughly ωa/c = ka (where k = ω/c is the wavenumber). When ka << 1 (the source is much smaller than a wavelength), this phase shift is small, and the entire source can be described by just a few integrated quantities — the multipole moments — rather than its detailed internal structure.

The expansion proceeds by expanding the retarded potential in powers of (a/r): the leading term gives the **electric dipole** contribution, the next gives magnetic dipole and electric quadrupole, and so on. The electric dipole contribution depends on p̈ = d²p/dt² (the acceleration of the dipole moment p = Σqᵢrᵢ). The radiated power from electric dipole radiation is P_dipole = p̈²/(6πε₀c³). Each successive term in the expansion is suppressed by an additional factor of (ka)² = (a/λ)². For a typical radio antenna or a vibrating molecule where a << λ, the dipole term overwhelmingly dominates: quadrupole radiation is suppressed by a factor (a/λ)² relative to dipole radiation.

This hierarchy has profound physical consequences. A system with no time-varying dipole moment — because total charge is zero and it oscillates symmetrically — radiates primarily through the next term (quadrupole or magnetic dipole). Gravitational wave sources (like merging black holes) are even more restricted: there is no monopole radiation (energy conservation) and no dipole radiation (momentum conservation), so the dominant radiation is **quadrupole**, suppressed by (v/c)² relative to a comparable electromagnetic dipole. Understanding which multipoles are active in a given source tells you the angular pattern, the frequency dependence of the power (P_dipole ∝ ω⁴), and the total radiated intensity — making multipole expansion the universal language of radiation physics.
