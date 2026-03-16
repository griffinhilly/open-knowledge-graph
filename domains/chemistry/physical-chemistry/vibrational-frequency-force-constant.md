---
id: vibrational-frequency-force-constant
title: Vibrational Frequency and Force Constant
domain: chemistry
course: physical-chemistry
prerequisites:
- id: harmonic-oscillator-molecular-vibrations
  type: hard
- id: vibrational-spectroscopy-theory
  type: hard
tags:
- vibrational-spectroscopy
- force-constants
- bond-strength
stage: advanced
status: draft
---

# Vibrational Frequency and Force Constant

## Core Idea
The vibrational frequency ν = (1/2π)√(k/μ) where k is the force constant and μ is reduced mass. Stronger bonds have larger force constants and thus higher frequencies; heavier atoms vibrate more slowly. IR spectroscopy directly measures frequencies and forces; Raman scattering accesses frequencies of symmetric vibrations. Force constants correlate with bond strength and polarity.

## Explainer

From your study of the harmonic oscillator model for molecular vibrations, you know that a diatomic molecule vibrates at quantized energy levels with spacing hν. The vibrational frequency ν itself is determined by just two physical properties of the bond: how stiff it is and how heavy the atoms are. The relationship **ν = (1/2π)√(k/μ)** is the same equation that governs a classical mass on a spring, but applied at the molecular scale with profound consequences for spectroscopy.

The **force constant** k measures the stiffness of the bond — technically, it is the second derivative of the potential energy with respect to bond displacement, evaluated at the equilibrium position. A triple bond (like C≡C, k ≈ 15–17 N/m × 10²) is much stiffer than a double bond (C=C, k ≈ 9–10 N/m × 10²), which is stiffer than a single bond (C−C, k ≈ 4–5 N/m × 10²). This directly explains the ordering of stretching frequencies in IR spectra: C≡C absorbs near 2100 cm⁻¹, C=C near 1650 cm⁻¹, and C−C near 1000 cm⁻¹. The force constant is thus a spectroscopic window into bond strength — a larger k means the atoms resist displacement more strongly, which means the bond is harder to stretch and break.

The **reduced mass** μ = m₁m₂/(m₁ + m₂) captures the effect of atomic mass on vibrational frequency. Heavier atoms vibrate more slowly, which is why deuterium substitution (replacing H with D) shifts stretching frequencies dramatically downward — the O−H stretch near 3500 cm⁻¹ drops to about 2600 cm⁻¹ for O−D, even though the bond strength (force constant) is nearly identical. This isotope effect is a powerful diagnostic tool: it confirms which peak in a complex IR spectrum involves hydrogen motion, and it plays a critical role in kinetic isotope effect studies where the rate of bond breaking depends on the vibrational frequency of the bond being broken.

For polyatomic molecules, the same relationship applies to each **normal mode** of vibration. A molecule with N atoms has 3N−6 normal modes (3N−5 if linear), each with its own effective force constant and reduced mass. Some modes involve stretching motions (higher frequency), while others involve bending or torsion (lower frequency, because the restoring force for angular deformation is typically weaker than for bond stretching). The characteristic group frequencies used throughout organic and inorganic spectroscopy — the carbonyl stretch near 1700 cm⁻¹, the N−H stretch near 3400 cm⁻¹, the C−H bend near 1450 cm⁻¹ — all follow directly from the force constant and reduced mass of the local oscillator, modulated by coupling to neighboring vibrations.

Understanding the ν–k–μ relationship also explains why IR and Raman spectroscopy are complementary. Both techniques measure vibrational frequencies, but they differ in which vibrations are observable: IR requires a changing dipole moment during vibration, while Raman requires a changing polarizability. The frequency values themselves, however, are identical because they depend only on the mechanical properties of the bond (k and μ), not on the mechanism of light–matter interaction. When you observe a peak at 2143 cm⁻¹ in both techniques for carbon monoxide, you extract the same force constant regardless of which instrument produced the spectrum.
