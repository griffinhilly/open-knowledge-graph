---
id: blackbody-radiation
title: Blackbody Radiation and Planck's Law
domain: physics
course: modern-physics
prerequisites:
- id: electromagnetic-spectrum
  type: hard
- id: heat-transfer-radiation
  type: hard
- id: wave-properties-intro
  type: soft
builds-toward:
- photoelectric-effect
- photon-model
tags:
- quantum
- blackbody
- planck
- ultraviolet-catastrophe
stage: advanced
status: validated
---

# Blackbody Radiation and Planck's Law

## Core Idea
A blackbody absorbs all incident radiation and emits a characteristic spectrum that depends only on its temperature. Classical physics (the Rayleigh–Jeans law) predicts the emitted power grows without bound at short wavelengths — the 'ultraviolet catastrophe.' Planck resolved this in 1900 by postulating that electromagnetic energy is emitted in discrete quanta of energy E = hf, where h is Planck's constant. This quantization suppresses the short-wavelength modes and yields Planck's distribution, which matches experiment precisely.

## How It's Best Learned
Plot the Rayleigh–Jeans and Planck spectra on the same axes to see the catastrophe and its resolution. Derive the Stefan–Boltzmann law and Wien displacement law as consequences. The key conceptual leap is that energy quantization is not a property of matter alone but of the radiation field itself.

## Common Misconceptions
- Quantization was introduced to fix a math trick, not because it is real — Planck himself hoped it was a calculational device, but it turned out to be fundamental.
- Blackbody radiation requires a black object — it is an idealized emitter; many physical objects approximate it closely (stars, the CMB).

## Questions

```yaml
- question: "Classical physics (the Rayleigh–Jeans law) predicted that the power radiated by a blackbody at short wavelengths would..."
  type: multiple-choice
  options: ["Approach zero as wavelength decreases", "Grow without bound as wavelength decreases", "Remain constant regardless of wavelength", "Depend on the material the object is made of"]
  answer: 1
  explanation: "The Rayleigh–Jeans law predicts intensity proportional to 1/λ⁴, which diverges as wavelength approaches zero — the 'ultraviolet catastrophe.' Planck's quantization suppresses this divergence by making high-frequency modes energetically costly to excite."

- question: "A 'blackbody' must be visually black in color in order to emit blackbody radiation."
  type: true-false
  answer: false
  explanation: "A blackbody is defined as a perfect absorber and emitter of radiation at all wavelengths — not by its visible color. Stars (which appear white, yellow, or red) and the cosmic microwave background are excellent blackbody approximators. The word 'black' refers to the object absorbing all incident light, not to its appearance."

- question: "What was Planck's key postulate that resolved the ultraviolet catastrophe, and what does it imply about the nature of electromagnetic energy?"
  type: short-answer
  answer: "Planck postulated that electromagnetic energy is emitted in discrete quanta of size E = hf, where h is Planck's constant and f is frequency. This implies energy is not continuously divisible — it comes in indivisible packets proportional to frequency, suppressing the high-frequency modes that caused the classical divergence."
  explanation: "By requiring each oscillation mode to emit or absorb energy in chunks of hf, high-frequency modes become statistically unlikely to be excited (since each quantum is large). This naturally produces the observed dropoff in the Planck spectrum at short wavelengths, matching experiment perfectly where classical theory catastrophically failed."
```

## Explainer

You already know that hot objects glow, and that the electromagnetic spectrum spans radio waves, visible light, X-rays, and beyond. Blackbody radiation is the study of exactly what spectrum a hot object emits — and the answer turned out to overturn classical physics entirely.

A blackbody is an idealized object that absorbs all incoming radiation and emits radiation purely based on its temperature. Real objects (stars, the filament in a light bulb, the cosmic microwave background) approximate this well. Classical physics, using the Rayleigh–Jeans law, predicted how much energy should be radiated at each wavelength by modeling the electromagnetic field inside a cavity as a collection of standing waves. Each wave mode was assumed to carry, on average, the same thermal energy — a perfectly sensible assumption from classical statistical mechanics. But the number of modes increases without bound as wavelength shrinks, so the predicted total power radiated at short wavelengths grows without limit. This is the ultraviolet catastrophe: an infinite amount of energy should pour out of any warm object in the ultraviolet and beyond. Obviously that does not happen.

Planck's 1900 resolution was radical: he postulated that each electromagnetic mode can only exchange energy in discrete packets, or quanta, of size E = hf, where f is frequency and h is a new constant (Planck's constant). This is not a property of the object — it is a property of the radiation field itself. The consequence is elegant: high-frequency modes require large quanta to be excited at all. At a given temperature, thermal energy simply is not large enough to excite the highest-frequency modes very often, so they contribute little to the spectrum. This naturally produces the observed bell-shaped Planck curve: rising at intermediate wavelengths and falling off sharply at short wavelengths.

The Planck distribution has two important limits you can derive from it. Integrating over all wavelengths gives the Stefan–Boltzmann law: total power emitted scales as T⁴. The peak wavelength shifts with temperature according to Wien's displacement law: λ_peak ∝ 1/T, which is why hotter stars appear bluer. Both laws were known empirically; Planck's distribution gives them a common foundation.

Planck himself hoped energy quantization was a mathematical trick with no deep physical meaning. It was not. Within a decade, Einstein used the same idea to explain the photoelectric effect, Bohr applied it to atomic spectra, and quantum mechanics was born. Blackbody radiation is the historical entry point into quantum physics — the first place where the classical continuum assumption definitively failed.
