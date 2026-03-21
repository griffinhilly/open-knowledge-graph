---
id: de-broglie-wavelength
title: de Broglie Wavelength
domain: physics
course: modern-physics
prerequisites:
- id: wave-particle-duality
  type: hard
- id: momentum-and-impulse
  type: hard
- id: photon-model
  type: hard
builds-toward:
- heisenberg-uncertainty-principle
- schrodinger-equation-intro
tags:
- quantum
- matter-waves
- de-broglie
- wavelength
stage: advanced
status: validated
---

# de Broglie Wavelength

## Core Idea
de Broglie (1924) proposed that all matter has an associated wavelength λ = h/p = h/(mv) for a non-relativistic particle with momentum p. This matter wave is not a physical wave in a medium but a probability wave. For a macroscopic object the wavelength is immeasurably small, which is why classical mechanics works; for electrons the wavelength is comparable to atomic spacings, producing observable diffraction. The de Broglie relation gives a physical basis for Bohr's angular momentum quantization: standing matter waves fit on integer orbits.

## How It's Best Learned
Calculate de Broglie wavelengths for electrons, protons, and a baseball to get a sense of scale. Rederive Bohr quantization by requiring an integer number of matter wave wavelengths to fit the orbit circumference.

## Common Misconceptions
- The de Broglie wavelength applies only to electrons — it applies to all matter; it is just negligible for large masses.
- A slower particle has a shorter wavelength — a slower particle has less momentum, so λ = h/p is larger, not smaller.

## Questions

```yaml
- question: "An electron is moving at 1×10⁶ m/s. A proton is also moving at 1×10⁶ m/s. Which particle has the longer de Broglie wavelength?"
  type: multiple-choice
  options:
    - "The proton — it is more massive and therefore has more wave-like character"
    - "The electron — it has less mass and therefore less momentum, giving a longer wavelength"
    - "They are equal — same speed means same wavelength"
    - "The proton — faster particles in quantum mechanics have longer wavelengths"
  answer: 1
  explanation: "λ = h/p = h/(mv). At the same speed, the more massive proton has far greater momentum (m_proton ≈ 1836 × m_electron), so its wavelength is about 1836 times shorter. The electron's tiny mass means tiny momentum, which gives a large wavelength. This is why electron diffraction is experimentally observable but proton diffraction requires much more effort."

- question: "A baseball and an electron are traveling at the same speed. Which has a shorter de Broglie wavelength and why does this explain why we don't see the baseball diffract?"
  type: multiple-choice
  options:
    - "The electron — because macroscopic objects don't have de Broglie wavelengths"
    - "The baseball — because it is more massive, giving it far greater momentum and therefore a far shorter wavelength"
    - "The baseball — because classical objects travel faster, reducing their wavelength"
    - "They are the same — de Broglie wavelength depends only on speed, not mass"
  answer: 1
  explanation: "λ = h/(mv). The baseball's mass (~0.15 kg) is ~10²⁸ times greater than an electron's, so its momentum is ~10²⁸ times larger and its wavelength is ~10²⁸ times shorter — on the order of 10⁻³⁴ m, far smaller than any atomic nucleus. No physical obstacle or slit can produce diffraction at that scale. The de Broglie relation applies to ALL matter; quantum effects simply vanish at macroscopic scales because h is so small."

- question: "A slower particle always has a shorter de Broglie wavelength than a faster particle of the same mass."
  type: true-false
  answer: false
  explanation: "This is the most common misconception about the de Broglie relation. λ = h/p = h/(mv): wavelength is *inversely* proportional to momentum. A slower particle has less momentum, so it has a *longer* wavelength, not shorter. The intuition fails because in everyday wave experience (e.g., sound), speed is tied to wavelength differently. For matter waves, slower means more wavelike (longer λ), which is why ultra-cold atoms — slowed to near absolute zero — exhibit dramatic quantum wave effects like Bose-Einstein condensation."

- question: "The de Broglie matter wave is a physical oscillation of a medium, similar to a water wave or sound wave."
  type: true-false
  answer: false
  explanation: "The matter wave is a probability wave — there is no medium oscillating. The squared magnitude of the wave function at any location gives the probability of finding the particle there. This is a fundamentally non-classical concept: there is nothing physically waving, yet the wave predicts interference patterns (observed in double-slit and Davisson-Germer experiments). Confusing the matter wave with a physical oscillation leads to paradoxes; the correct interpretation is purely probabilistic."

- question: "Explain how de Broglie's hypothesis gives a physical reason for Bohr's quantization rule, rather than treating it as an arbitrary postulate."
  type: short-answer
  answer: "Bohr postulated that angular momentum is quantized in units of ħ without explaining why. de Broglie's hypothesis says an electron with momentum p has wavelength λ = h/p. For a stable circular orbit of radius r, the electron's matter wave must form a standing wave — an integer number of wavelengths must fit the circumference: 2πr = nλ = nh/p. This gives mvr = nħ, exactly Bohr's condition. Quantization is no longer arbitrary — it is a resonance condition. Only orbits where the matter wave closes on itself constructively are stable."
  explanation: "This derivation reveals a deep principle: quantization throughout quantum mechanics arises from wave boundary conditions. Just as a guitar string can only sustain standing waves at specific frequencies (harmonics), an electron orbit can only sustain a standing matter wave for specific radii. The 'arbitrary' Bohr postulate turns out to be the statement that non-resonant orbits self-destructively interfere and disappear — exactly analogous to destructive interference in any wave system."
```

## Explainer

From your prerequisite on wave-particle duality, you know that light behaves both as a wave (diffraction, interference) and as a particle (the photon, with energy E = hf). From the photon model, you know that a photon carries momentum p = E/c = hf/c = h/λ. de Broglie's 1924 insight was audaciously simple: if light (which we thought was a wave) turned out to have particle properties, why shouldn't matter (which we thought was particles) have wave properties? He proposed that any particle with momentum p has an associated wavelength **λ = h/p**, where h is Planck's constant.

The formula connects your two prerequisites directly. From momentum-and-impulse, you know p = mv for a non-relativistic particle. So λ = h/(mv): a heavier or faster particle has a shorter wavelength. Planck's constant h ≈ 6.63 × 10⁻³⁴ J·s is extraordinarily small. For a baseball (0.15 kg) at 40 m/s: λ = 6.63 × 10⁻³⁴ / (0.15 × 40) ≈ 10⁻³⁴ m — far smaller than an atomic nucleus. No experiment can detect wave behavior at that scale, which is why classical mechanics works perfectly for everyday objects. For an electron accelerated through 100 V: its kinetic energy is 100 eV, its momentum p = √(2mE) ≈ 5.4 × 10⁻²⁴ kg·m/s, and λ ≈ 1.2 × 10⁻¹⁰ m = 1.2 Å — exactly the spacing between atoms in a crystal. This is why electron diffraction is a real, observable phenomenon used to determine crystal structures.

The **matter wave** described by λ = h/p is not a physical oscillation of a medium — it is a **probability wave**. The squared magnitude of the wave function at a location gives the probability of finding the particle there. This reinterpretation has no classical analog, but the mathematical consequences are immediate and testable. When electron beams scatter off a crystal lattice, they produce diffraction patterns (Davisson-Germer experiment, 1927) that match the prediction from λ = h/p exactly, confirming de Broglie's hypothesis.

The most elegant connection is the derivation of Bohr's quantization rule. Bohr had postulated, without justification, that angular momentum must be quantized in units of ħ = h/(2π). de Broglie's hypothesis explains this: for a stable electron orbit of radius r, you require an **integer number of wavelengths to fit the circumference** — a standing wave condition. This gives 2πr = nλ = nh/p = nh/(mv), so mvr = nħ, which is exactly Bohr's quantization condition. The formerly arbitrary postulate becomes a resonance condition: only orbits that support standing matter waves are stable. This insight — that quantization arises from wave interference — is the conceptual foundation on which Schrödinger would later build his full wave equation.
