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

## Explainer

From your prerequisite study of photon particle properties, you know that light has a dual nature — it behaves both as a wave (characterized by frequency f and wavelength λ) and as a stream of particles (photons). The **Planck-Einstein relation** E = hf is the precise quantitative bridge between these two descriptions: it tells you the energy carried by a single photon of frequency f. The constant h ≈ 6.626 × 10⁻³⁴ J·s is tiny by everyday standards, which is why individual photons are imperceptible at human scales but decisive at atomic ones.

The historical significance of this relation is hard to overstate. Before 1900, classical physics assumed that the electromagnetic field was a continuous entity — you could add any amount of energy to a light wave by increasing its amplitude slightly. Planck introduced quantization in 1900 as a mathematical trick to fix the **ultraviolet catastrophe**: classical theory predicted that a hot object would radiate infinite power at short wavelengths, which obviously never happens. By postulating that the energy of each electromagnetic oscillation mode came only in discrete packets E = hf, Planck derived the correct blackbody spectrum. Einstein extended this in 1905 by asserting that light genuinely *consists* of these quanta (photons), not just that it is absorbed and emitted in chunks — a claim supported by the photoelectric effect.

The relation E = hf implies that **all photons of the same frequency carry the same energy**, regardless of intensity or direction. A beam of dim blue light and a beam of bright blue light have photons with the same individual energy; the bright beam just has more of them. Intensity (power per area) scales with the number of photons per second, not their individual energy. This counting picture explains the photoelectric effect precisely: whether a photon can eject an electron from a metal depends entirely on whether its frequency (and hence its individual energy hf) exceeds the **work function** of the metal. A million radio photons cannot eject a single electron because each photon's energy is far below the threshold; one violet photon can eject an electron immediately because its energy exceeds the threshold. Intensity is irrelevant; frequency is everything.

Since wavelength and frequency are related by c = fλ, the Planck-Einstein relation also takes the form E = hc/λ. Higher frequency means shorter wavelength means larger energy per photon. Visible light photons (wavelength 400–700 nm) carry 1.8–3.1 eV per photon — the same order of magnitude as atomic binding energies and chemical bond energies, which is exactly why visible light can drive photochemistry and vision but cannot ionize atoms. X-ray photons (λ ~ 0.1 nm) carry ~10 keV — enough to knock electrons out of inner atomic shells. Radio photons (λ ~ 1 m) carry ~10⁻⁶ eV — far too little to excite atomic transitions, which is why radio waves pass through matter without ionizing it. The energy scale set by E = hf thus defines the boundary between ionizing and non-ionizing radiation and organizes the entire electromagnetic spectrum in terms of its interaction with matter.
