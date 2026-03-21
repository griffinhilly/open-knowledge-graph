---
id: planck-einstein-relation
title: 'Planck-Einstein Relation: Energy and Frequency'
domain: physics
course: modern-physics
prerequisites:
- id: photon-particle-properties
  type: hard
builds-toward:
- wave-particle-duality-observations
- photoelectric-effect
tags:
- quantum-intro
- quantization
stage: advanced
status: draft
---

# Planck-Einstein Relation: Energy and Frequency

## Core Idea
The energy of a photon is directly proportional to its frequency: E = hf, where h ≈ 6.626 × 10⁻³⁴ J·s is Planck's constant. This relationship revealed that electromagnetic radiation is quantized—energy comes in discrete packets called quanta. The proportionality constant h represents the scale of quantum mechanics and is one of nature's fundamental constants.

## How It's Best Learned
Work through specific examples: calculate photon energies for visible light, X-rays, and radio waves. Compare energy scales to atomic ionization energies to see why visible photons can eject electrons but radio photons cannot.

## Common Misconceptions
- Planck's constant h is not related to Planck length; they have different dimensions.
- E = hf applies to all photons regardless of direction or polarization—frequency is the only relevant property for energy.
- Higher frequency does not mean more photons; it means each photon carries more energy.

## Questions

```yaml
- question: "You shine two light beams on a metal with a work function of 2.5 eV. Beam A is dim violet light (λ ≈ 400 nm, ~3.1 eV per photon). Beam B is intense red light (λ ≈ 700 nm, ~1.8 eV per photon). Which beam ejects electrons?"
  type: multiple-choice
  options:
    - "Beam B, because its greater intensity delivers more total energy to the metal surface"
    - "Beam A only, because each violet photon's energy exceeds the work function threshold, regardless of the beam's intensity"
    - "Both beams together, because their combined energy exceeds the threshold"
    - "Neither beam — continuous wave energy delivery is required to eject electrons"
  answer: 1
  explanation: "Whether a photon can eject an electron depends entirely on whether its individual energy hf exceeds the work function — a threshold that must be crossed by a single photon in a single interaction. Red photons each carry 1.8 eV, below the 2.5 eV threshold; no number of red photons overcomes this because the energy is not cumulative. Dim violet photons each carry 3.1 eV, exceeding the threshold, so even a small number eject electrons immediately. Intensity controls how many electrons are ejected per second, not whether ejection occurs at all."

- question: "Doubling the intensity of a green laser beam while keeping its wavelength fixed:"
  type: multiple-choice
  options:
    - "Doubles the energy of each photon"
    - "Doubles the frequency of the light"
    - "Doubles the number of photons per second while leaving each photon's individual energy unchanged"
    - "Doubles both the number of photons and their individual energies"
  answer: 2
  explanation: "Intensity (power per unit area) scales with the number of photons per second, not with individual photon energy. Each photon's energy is fixed by its frequency through E = hf; changing intensity means changing the photon flux, not the frequency. This is the quantization insight: the energy per quantum is set by the frequency alone, and more intense light means more quanta, not more energetic quanta."

- question: "A beam of bright red light has photons with more energy per photon than a beam of dim blue light."
  type: true-false
  answer: false
  explanation: "Photon energy depends on frequency (E = hf), not on the intensity of the beam. Blue photons have higher frequency than red photons and therefore more energy per photon — regardless of how many there are. Brightness (intensity) measures photons per second per unit area; it has no bearing on the energy carried by each individual photon. This is the core misconception E = hf is designed to correct: energy per photon is a property of the frequency, not the beam."

- question: "The fact that radio waves cannot ionize atoms while X-rays can is a direct consequence of the Planck-Einstein relation E = hf and the large difference in frequency between the two types of radiation."
  type: true-false
  answer: true
  explanation: "Radio waves have frequencies around 10⁸ Hz, giving photon energies of roughly 10⁻⁶ eV — far below atomic binding energies (~10 eV). X-rays have frequencies around 10¹⁸ Hz, giving photon energies of ~10 keV — well above atomic binding energies. The E = hf relation directly maps the electromagnetic spectrum onto a scale of photon energies that determines whether radiation interacts with atomic electrons (ionizing) or passes through matter without exciting them (non-ionizing)."

- question: "Why can a single ultraviolet photon eject an electron from a metal surface when a million radio photons cannot, and what does this reveal about the nature of electromagnetic energy?"
  type: short-answer
  answer: "Because the photoelectric interaction is a one-photon, one-electron event: a single photon must carry enough energy to overcome the metal's work function in one interaction. Radio photons each carry energy far below this threshold (E = hf is tiny for radio frequencies), and energy from multiple photons doesn't accumulate to eject a single electron. A UV photon's frequency is high enough that hf exceeds the threshold, so ejection occurs immediately. This reveals that electromagnetic energy is quantized: it is exchanged in discrete packets whose size depends only on frequency, not on intensity."
  explanation: "This insight — that electromagnetic energy comes in indivisible quanta of size hf — is what Einstein's 1905 paper established and what the photoelectric effect proves experimentally. The classical picture would allow low-intensity light to slowly deliver enough energy to eject electrons; the quantum picture says no, because delivery is always in one-photon chunks. The quantum of energy sets a hard threshold: either the chunk is big enough or it isn't."
```

## Explainer

From your prerequisite study of photon particle properties, you know that light has a dual nature — it behaves both as a wave (characterized by frequency f and wavelength λ) and as a stream of particles (photons). The **Planck-Einstein relation** E = hf is the precise quantitative bridge between these two descriptions: it tells you the energy carried by a single photon of frequency f. The constant h ≈ 6.626 × 10⁻³⁴ J·s is tiny by everyday standards, which is why individual photons are imperceptible at human scales but decisive at atomic ones.

The historical significance of this relation is hard to overstate. Before 1900, classical physics assumed that the electromagnetic field was a continuous entity — you could add any amount of energy to a light wave by increasing its amplitude slightly. Planck introduced quantization in 1900 as a mathematical trick to fix the **ultraviolet catastrophe**: classical theory predicted that a hot object would radiate infinite power at short wavelengths, which obviously never happens. By postulating that the energy of each electromagnetic oscillation mode came only in discrete packets E = hf, Planck derived the correct blackbody spectrum. Einstein extended this in 1905 by asserting that light genuinely *consists* of these quanta (photons), not just that it is absorbed and emitted in chunks — a claim supported by the photoelectric effect.

The relation E = hf implies that **all photons of the same frequency carry the same energy**, regardless of intensity or direction. A beam of dim blue light and a beam of bright blue light have photons with the same individual energy; the bright beam just has more of them. Intensity (power per area) scales with the number of photons per second, not their individual energy. This counting picture explains the photoelectric effect precisely: whether a photon can eject an electron from a metal depends entirely on whether its frequency (and hence its individual energy hf) exceeds the **work function** of the metal. A million radio photons cannot eject a single electron because each photon's energy is far below the threshold; one violet photon can eject an electron immediately because its energy exceeds the threshold. Intensity is irrelevant; frequency is everything.

Since wavelength and frequency are related by c = fλ, the Planck-Einstein relation also takes the form E = hc/λ. Higher frequency means shorter wavelength means larger energy per photon. Visible light photons (wavelength 400–700 nm) carry 1.8–3.1 eV per photon — the same order of magnitude as atomic binding energies and chemical bond energies, which is exactly why visible light can drive photochemistry and vision but cannot ionize atoms. X-ray photons (λ ~ 0.1 nm) carry ~10 keV — enough to knock electrons out of inner atomic shells. Radio photons (λ ~ 1 m) carry ~10⁻⁶ eV — far too little to excite atomic transitions, which is why radio waves pass through matter without ionizing it. The energy scale set by E = hf thus defines the boundary between ionizing and non-ionizing radiation and organizes the entire electromagnetic spectrum in terms of its interaction with matter.
