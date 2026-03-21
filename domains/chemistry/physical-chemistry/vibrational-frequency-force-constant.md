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

## Questions

```yaml
- question: "An O−H bond absorbs near 3500 cm⁻¹ in the IR spectrum. When hydrogen is replaced by deuterium to form O−D, where would you expect the new absorption?"
  type: multiple-choice
  options:
    - "Near 3500 cm⁻¹ — the force constant increases to compensate for heavier deuterium"
    - "Near 7000 cm⁻¹ — deuterium is twice as heavy, so the frequency doubles"
    - "Near 2600 cm⁻¹ — the heavier reduced mass lowers the frequency while the force constant stays nearly the same"
    - "Near 1750 cm⁻¹ — deuterium substitution halves the vibrational frequency"
  answer: 2
  explanation: "Replacing H (mass 1) with D (mass 2) roughly doubles the reduced mass μ. Since ν ∝ 1/√μ, the frequency drops by a factor of √2 ≈ 1.41. Starting at 3500 cm⁻¹, the O−D stretch appears near 3500/1.41 ≈ 2480–2600 cm⁻¹ — consistent with observed values. Crucially, the force constant k is essentially unchanged because it reflects bond stiffness (electronic structure), not atomic mass. Isotope substitution is a clean probe of reduced mass effects precisely because it changes μ without changing k."

- question: "A C≡N triple bond absorbs at a higher wavenumber than a C=N double bond, which absorbs higher than a C−N single bond. What is the primary reason for this trend?"
  type: multiple-choice
  options:
    - "Carbon-nitrogen bonds with more electrons have smaller reduced masses, increasing frequency"
    - "Triple bonds have larger force constants due to greater bond stiffness, and higher k means higher vibrational frequency"
    - "The reduced mass decreases with bond order because electrons contribute to molecular mass"
    - "Triple bonds are shorter, and shorter path length means higher frequency"
  answer: 1
  explanation: "The force constant k measures bond stiffness — how strongly the bond resists stretching. A triple bond involves three shared electron pairs, making it much stiffer than a double bond (two pairs) or single bond (one pair). Since ν ∝ √k, higher k gives higher frequency. The reduced mass is essentially the same for C≡N, C=N, and C−N (the atomic masses don't change with bond order), so the frequency trend is driven entirely by the increasing force constant. This is why C≡C absorbs near 2100 cm⁻¹, C=C near 1650 cm⁻¹, and C−C near 1000 cm⁻¹."

- question: "Deuterium substitution (replacing H with D) changes the force constant of the bond, which is why the vibrational frequency shifts to lower wavenumber."
  type: true-false
  answer: false
  explanation: "The force constant k reflects the bond's electronic structure — how stiff the bond is — which is determined by the number and type of electrons shared between the atoms. Replacing H with D does not change the electronic structure of the bond, so k remains essentially unchanged. What changes is the reduced mass μ: deuterium is twice as heavy as hydrogen, increasing μ and thereby lowering the vibrational frequency according to ν = (1/2π)√(k/μ). This is precisely what makes isotope substitution a clean diagnostic: it selectively probes the reduced mass without perturbing the force constant."

- question: "A bond with a larger force constant will absorb at a higher wavenumber in the IR spectrum, all else being equal."
  type: true-false
  answer: true
  explanation: "The vibrational frequency ν = (1/2π)√(k/μ). For fixed reduced mass μ, a larger force constant k means a stiffer bond that vibrates faster, appearing at higher wavenumber (cm⁻¹ = ν/c). This is why multiple bonds absorb at higher wavenumbers than single bonds between the same atoms: C≡O (triple bond character, large k) absorbs near 2143 cm⁻¹ in CO gas, while C=O (double bond, smaller k) absorbs near 1700–1750 cm⁻¹, and C−O (single bond, smallest k) absorbs near 1000–1200 cm⁻¹."

- question: "A chemist observes an IR absorption at 2100 cm⁻¹ and suspects it is either a C≡C or a C≡N stretch. Explain how the concept of reduced mass could help distinguish between them, and what isotopic experiment would test the assignment."
  type: short-answer
  answer: "The reduced mass for a C≡C vibration (both atoms are carbon, mass 12) differs from that for C≡N (nitrogen mass 14 vs carbon mass 12). For C≡C, μ = (12×12)/(12+12) = 6 amu. For C≡N, μ = (12×14)/(12+14) ≈ 6.46 amu. Since ν ∝ 1/√μ, the C≡N stretch should appear at slightly lower wavenumber than C≡C with the same force constant. To test the assignment, you could perform isotopic labeling: replace ¹²C with ¹³C (mass 13) in the triple bond. For C≡C, substituting one carbon shifts μ to (12×13)/(12+13) = 6.24 amu, predicting a specific frequency shift. For ¹³C≡N, μ = (13×14)/(13+14) ≈ 6.74 amu. The magnitude and direction of the observed shift would confirm which assignment is correct."
  explanation: "This illustrates the power of isotope labeling in spectroscopic assignment. Because isotopic substitution changes μ but not k, the predicted frequency shift is precisely calculable from the mass ratio. If the observed shift matches the prediction for ¹³C≡C, the original assignment is confirmed; if it matches ¹³C≡N, the other is. This approach is widely used in inorganic and biochemistry to assign IR bands in complex molecules."
```

## Explainer

From your study of the harmonic oscillator model for molecular vibrations, you know that a diatomic molecule vibrates at quantized energy levels with spacing hν. The vibrational frequency ν itself is determined by just two physical properties of the bond: how stiff it is and how heavy the atoms are. The relationship **ν = (1/2π)√(k/μ)** is the same equation that governs a classical mass on a spring, but applied at the molecular scale with profound consequences for spectroscopy.

The **force constant** k measures the stiffness of the bond — technically, it is the second derivative of the potential energy with respect to bond displacement, evaluated at the equilibrium position. A triple bond (like C≡C, k ≈ 15–17 N/m × 10²) is much stiffer than a double bond (C=C, k ≈ 9–10 N/m × 10²), which is stiffer than a single bond (C−C, k ≈ 4–5 N/m × 10²). This directly explains the ordering of stretching frequencies in IR spectra: C≡C absorbs near 2100 cm⁻¹, C=C near 1650 cm⁻¹, and C−C near 1000 cm⁻¹. The force constant is thus a spectroscopic window into bond strength — a larger k means the atoms resist displacement more strongly, which means the bond is harder to stretch and break.

The **reduced mass** μ = m₁m₂/(m₁ + m₂) captures the effect of atomic mass on vibrational frequency. Heavier atoms vibrate more slowly, which is why deuterium substitution (replacing H with D) shifts stretching frequencies dramatically downward — the O−H stretch near 3500 cm⁻¹ drops to about 2600 cm⁻¹ for O−D, even though the bond strength (force constant) is nearly identical. This isotope effect is a powerful diagnostic tool: it confirms which peak in a complex IR spectrum involves hydrogen motion, and it plays a critical role in kinetic isotope effect studies where the rate of bond breaking depends on the vibrational frequency of the bond being broken.

For polyatomic molecules, the same relationship applies to each **normal mode** of vibration. A molecule with N atoms has 3N−6 normal modes (3N−5 if linear), each with its own effective force constant and reduced mass. Some modes involve stretching motions (higher frequency), while others involve bending or torsion (lower frequency, because the restoring force for angular deformation is typically weaker than for bond stretching). The characteristic group frequencies used throughout organic and inorganic spectroscopy — the carbonyl stretch near 1700 cm⁻¹, the N−H stretch near 3400 cm⁻¹, the C−H bend near 1450 cm⁻¹ — all follow directly from the force constant and reduced mass of the local oscillator, modulated by coupling to neighboring vibrations.

Understanding the ν–k–μ relationship also explains why IR and Raman spectroscopy are complementary. Both techniques measure vibrational frequencies, but they differ in which vibrations are observable: IR requires a changing dipole moment during vibration, while Raman requires a changing polarizability. The frequency values themselves, however, are identical because they depend only on the mechanical properties of the bond (k and μ), not on the mechanism of light–matter interaction. When you observe a peak at 2143 cm⁻¹ in both techniques for carbon monoxide, you extract the same force constant regardless of which instrument produced the spectrum.
