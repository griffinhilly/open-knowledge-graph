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

## Questions

```yaml
- question: "An atomic transition is 'E1-forbidden' — selection rules prohibit electric dipole radiation. What actually happens to an atom in such an excited state?"
  type: multiple-choice
  options:
    - "The atom remains permanently in the excited state, since all radiation is forbidden"
    - "The atom rapidly decays via E2 or M1 transitions, which are only slightly slower than E1"
    - "The atom eventually decays via M1 or E2 radiation, but the lifetime is roughly 10⁶ times longer than a typical E1 transition"
    - "The atom decays by emitting two photons simultaneously, which is always faster than M1 or E2"
  answer: 2
  explanation: "E1-'forbidden' means the E1 amplitude is zero by selection rules, not that radiation is impossible. M1 and E2 transitions proceed — but because their power scales as (a/λ)⁴ compared to E1's (a/λ)², they are suppressed by roughly (a/λ)² ≈ (10⁻³)² = 10⁻⁶ relative to E1. This means lifetimes are roughly 10⁶ times longer. In laboratory conditions with dense matter, collisions redistribute energy before the atom radiates. In nebulae — extremely low density environments — atoms can survive long enough for these slow forbidden transitions to occur, producing the distinctive forbidden emission lines observed in astronomical spectra."

- question: "In nuclear gamma-ray physics, why is classifying a transition as E1, M1, E2, M2, etc. practically important?"
  type: multiple-choice
  options:
    - "The classification determines the color of the emitted gamma ray, which affects detector sensitivity"
    - "Each multipole order corresponds to a different energy range, so the classification identifies the gamma-ray energy"
    - "The multipole order directly determines the transition rate (lifetime), and comparing measured lifetimes to predictions reveals nuclear structure"
    - "The classification determines the recoil momentum of the nucleus, which is needed for Mössbauer spectroscopy"
  answer: 2
  explanation: "Multipole radiation rates scale as (a/λ)^{2L} where L is the multipole order, so higher multipoles are increasingly suppressed. An E1 transition in a nucleus decays orders of magnitude faster than an M1, which decays faster than an E2, and so on. Measuring the half-life of a nuclear excited state and comparing it to the predicted rate for each multipole type both identifies which multipole is operating and provides sensitive tests of nuclear structure models. Long-lived nuclear isomers (nuclear states with unusual stability) often arise because only a high-multipole transition is available — the angular momentum or parity change required is large."

- question: "In atomic physics, 'forbidden' transitions (M1 or E2) can and do occur — they are simply much slower than E1 transitions and require low-density environments to be observed."
  type: true-false
  answer: true
  explanation: "The term 'forbidden' is a misnomer that confuses many students. M1 and E2 transitions are not literally impossible — they are suppressed by powers of (a/λ) relative to E1. For atoms, this suppression is about 10⁻⁶ per order, making the radiative lifetime roughly 10⁶ times longer. In dense environments (laboratory gases, solids), collisions transfer the energy before the photon is emitted. In nebulae, the density is so low (sometimes just a few atoms per cubic centimeter) that the atom has time to radiate. The forbidden emission lines of ionized oxygen and nitrogen are among the brightest features in nebular spectra."

- question: "Magnetic dipole radiation and electric dipole radiation have different angular radiation patterns — M1 produces four-lobed emission while E1 produces the familiar two-lobed donut pattern."
  type: true-false
  answer: false
  explanation: "Magnetic dipole radiation has the same angular pattern as electric dipole radiation — the sin²θ donut shape with two lobes. What differs is the polarization structure: in M1 radiation, the roles of E⃗ and B⃗ in the radiation field are swapped relative to E1. The four-lobed pattern belongs to electric quadrupole (E2) radiation, which arises from an oscillating second-moment distribution. Distinguishing these patterns is important in both atomic spectroscopy and antenna design."

- question: "Why are 'forbidden' transition lines from M1 and E2 radiation observed in nebulae but not in laboratory plasma discharges, even when both environments contain the same excited atoms?"
  type: short-answer
  answer: "The lifetime of an M1 or E2 excited state is roughly 10⁶ times longer than an E1 state — on the order of seconds to hours rather than nanoseconds. In a laboratory plasma, collisions between atoms occur far more frequently than the M1/E2 radiative rate: the excited atom collides with another atom and transfers its energy before it can radiate a photon. In a nebula, the particle density is extremely low (sometimes ~10² particles/cm³ vs ~10¹⁹/cm³ in laboratory gas), so collisions are rare enough that the atom survives long enough to eventually emit the forbidden photon. The transition is not more likely in nebulae — it is simply uninterrupted by collisions."
  explanation: "This explains why forbidden line observations in astronomy were initially puzzling: astronomers observed spectral lines from 'nebulium' that didn't match any known laboratory element. The lines turned out to be forbidden transitions of ordinary oxygen and nitrogen ions that simply could not be seen in any laboratory environment dense enough to prevent them. The observation required recognizing that astrophysical plasmas occupy a density regime qualitatively different from anything achievable on Earth."
```

## Explainer

From your study of electric dipole radiation, you know that an oscillating charge distribution with a time-varying dipole moment p⃗(t) radiates electromagnetic waves with power P ∝ ω⁴|p⃗|². The radiation pattern is the familiar sin²θ donut shape, and the field falls off as 1/r. But what happens when the electric dipole moment is zero — either exactly (by symmetry) or by selection rule? The multipole expansion tells you: the next terms are the **magnetic dipole** (M1) and **electric quadrupole** (E2), but they radiate far more weakly.

The critical parameter governing how strongly each multipole radiates is the ratio a/λ, where a is the characteristic size of the source and λ is the emitted wavelength. For electric dipole radiation, radiated power scales as (a/λ)². For M1 and E2 radiation, it scales as (a/λ)⁴. For atoms, a ~ 10⁻¹⁰ m and visible light has λ ~ 10⁻⁷ m, giving a/λ ~ 10⁻³. So magnetic dipole and quadrupole transitions are suppressed by roughly a factor of (10⁻³)² = 10⁻⁶ relative to electric dipole transitions. This is why E1 transitions dominate atomic spectra: they are overwhelmingly faster. **Forbidden transitions** — M1 or E2 transitions in atoms where E1 is disallowed by selection rules — are so slow that they are only observable in very low-density environments (nebulae, for example) where collisions don't redistribute energy before the atom eventually radiates.

**Magnetic dipole radiation** arises from oscillating magnetic dipole moments, as produced by current loops or spinning charges. Its radiation pattern is identical to the electric dipole's, but the roles of E⃗ and B⃗ in the radiation field are swapped. **Electric quadrupole radiation** arises from oscillating second-moment distributions — charge configurations with no net dipole moment but with an asymmetric spread, like two dipoles of opposite orientation placed end to end. Its radiation pattern has four lobes rather than two. In nuclear physics, where nuclear radii (~10⁻¹⁵ m) and gamma-ray wavelengths (~10⁻¹² m) give a/λ ~ 10⁻³ as well, classifying gamma transitions as E1, M1, E2, M2, and so on directly determines their decay rates and reveals nuclear structure.

The selection rules that forbid E1 while permitting M1 or E2 come from conservation of angular momentum and parity. An E1 photon carries angular momentum ΔJ = 1 and changes parity; an M1 photon also carries ΔJ = 1 but does not change parity; an E2 photon carries ΔJ = 2 and does not change parity. When initial and final states have quantum numbers incompatible with E1 but compatible with M1 or E2, the lower multipole is forbidden and the higher one proceeds — slowly but inevitably. The competition between these channels, and the lifetimes they imply, is central to both atomic spectroscopy and nuclear gamma-ray physics.
