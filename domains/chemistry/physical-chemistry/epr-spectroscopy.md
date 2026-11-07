---
id: epr-spectroscopy
title: Electron Paramagnetic Resonance (EPR) Spectroscopy
domain: chemistry
course: physical-chemistry
prerequisites:
- id: energy-level-transitions
  type: hard
- id: spin-angular-momentum
  type: soft
- id: nmr-quantum-theory
  type: soft
- id: nmr-spectroscopy-spin-coupling
  type: soft
builds-toward: []
tags:
- EPR
- ESR
- g-factor
- hyperfine coupling
- radicals
- magnetic resonance
stage: advanced
status: validated
---

# Electron Paramagnetic Resonance (EPR) Spectroscopy

## Core Idea
EPR spectroscopy, also called electron spin resonance (ESR), detects species with unpaired electrons, such as organic radicals and many transition metal ions. In a magnetic field B, the two spin states of an unpaired electron split by ΔE = gμ_B B, and microwaves of matching energy drive transitions between them. The g-factor reports the electronic environment, and hyperfine splitting from nearby magnetic nuclei reveals where the unpaired electron is spread. Molecules with all electrons paired give no EPR signal.

## How It's Best Learned
Build on NMR: the logic of a spin in a field, a resonance condition and splitting by neighbors carries over, with an electron in place of a nucleus. Calculate the resonance field for a g ≈ 2 radical at 9.5 GHz to get a feel for the numbers. Then predict hyperfine patterns with the 2nI + 1 rule for the methyl radical and a nitroxide, and practise reading first-derivative spectra.

## Common Misconceptions
- Every molecule gives an EPR spectrum. (Only paramagnetic species, those with unpaired electrons, absorb; most stable organic molecules are EPR-silent.)
- An EPR spectrum shows absorption peaks like a UV-Vis spectrum. (Spectrometers usually record the first derivative of absorption, so each line appears as an up-down feature crossing the baseline at the absorption maximum.)
- The g-factor of every radical equals the free-electron value. (Spin-orbit coupling shifts g; organic radicals stay close to 2.0023, while many transition metal ions show g values far from 2 that vary with orientation.)

## Questions

```yaml
- question: "What hyperfine pattern does the methyl radical, •CH₃, show in its EPR spectrum?"
  type: multiple-choice
  options: ["A single line", "A 1:1 doublet", "A 1:2:1 triplet", "A 1:3:3:1 quartet"]
  answer: 3
  explanation: "The unpaired electron couples to three equivalent protons, each with I = 1/2. That gives n + 1 = 4 lines with binomial intensities 1:3:3:1."
- question: "A compound in which every electron is paired gives no EPR spectrum."
  type: true-false
  answer: true
  explanation: "EPR measures transitions between the spin states of an unpaired electron. With all electrons paired, the net electron spin is zero and there is no EPR transition to observe."
- question: "An X-band spectrometer operates at about 9.5 GHz. At roughly what magnetic field does a radical with g ≈ 2.00 come into resonance?"
  type: multiple-choice
  options: ["About 0.0034 T", "About 0.34 T", "About 3.4 T", "About 34 T"]
  answer: 1
  explanation: "From hν = gμ_B B, B = hν/(gμ_B) = (6.63 × 10⁻³⁴ J s × 9.5 × 10⁹ s⁻¹)/(2.00 × 9.27 × 10⁻²⁴ J T⁻¹) ≈ 0.34 T."
- question: "Why does a nitroxide radical, R₂N–O•, show three EPR lines of equal intensity?"
  type: short-answer
  answer: "The unpaired electron is partly on the ¹⁴N nucleus, which has nuclear spin I = 1. A nucleus with spin I splits the line into 2I + 1 = 3 components, one for each orientation m_I = +1, 0, −1, and the three orientations are equally populated."
  explanation: "This is the same counting rule as for protons, generalized to nuclei with I > 1/2. Nitroxides are widely used as spin labels because this simple pattern responds to their surroundings."
```

## Explainer

An electron has spin 1/2 and a magnetic moment. In a magnetic field, its two spin states, m_s = +1/2 and −1/2, have different energies. The gap is

ΔE = hν = gμ_B B

where μ_B is the Bohr magneton and g is the g-factor. For a free electron g is about 2.0023. If you irradiate the sample with photons whose energy matches this gap, unpaired electrons absorb them and flip. This is electron paramagnetic resonance. Yevgeny Zavoisky first observed it in 1944.

The numbers set the experiment. The electron's magnetic moment is about 658 times that of a proton, so the energy gap at a given field is far larger than in NMR. A common X-band spectrometer uses microwaves near 9.5 GHz, and a g ≈ 2 radical then absorbs near 0.34 T. Instead of sweeping frequency, instruments usually hold the frequency fixed and sweep the field. They also record the first derivative of the absorption, so each line looks like a wiggle that crosses the baseline at the true peak.

Only species with unpaired electrons give a signal, so EPR can pick out a radical or a paramagnetic metal center in an otherwise silent sample.

Two features carry chemical information. The first is the g-factor. Spin-orbit coupling mixes some orbital motion into the electron's magnetism and shifts g away from 2.0023. Organic radicals usually stay very close to that value, while transition metal ions such as Cu²⁺ show larger shifts that depend on how the molecule is oriented in the field.

The second is hyperfine splitting. A magnetic nucleus near the unpaired electron adds its own small field, which depends on the nuclear spin orientation. A nucleus of spin I splits each line into 2I + 1 lines. For n equivalent nuclei with I = 1/2, the result is n + 1 lines with binomial intensities, just like spin-spin splitting in proton NMR. The methyl radical, with three equivalent protons, shows a 1:3:3:1 quartet. A nitroxide radical, coupled to one ¹⁴N nucleus with I = 1, shows three equal lines. The size of each splitting, the hyperfine coupling constant, tells you how much of the unpaired electron's density sits near that nucleus.
