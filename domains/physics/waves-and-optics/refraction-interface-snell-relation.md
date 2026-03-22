---
id: refraction-interface-snell-relation
title: Refraction at Boundaries and Snell's Law
domain: physics
course: waves-and-optics
prerequisites:
- id: wavelength-frequency-speed-relation
  type: hard
builds-toward:
- grazing-angle-critical-condition
- wavelength-color-refractive-index
tags:
- refraction
- optics
stage: advanced
status: draft
---

# Refraction at Boundaries and Snell's Law

## Core Idea
When a wave enters a new medium with different speed, its direction bends according to Snell's law: n₁ sin(θ₁) = n₂ sin(θ₂). The refractive index n = c/v is the ratio of light speed in vacuum to speed in the medium. Refraction arises because the wavelength changes while frequency remains constant, causing a direction change to maintain phase continuity at the interface.

## How It's Best Learned
Derive Snell's law using the Huygens-Fresnel principle: wavelets from the interface must add constructively to the refracted ray.

## Common Misconceptions
Light does not 'change speed' in the usual sense—rather, light speed in a medium is the definition of the medium's refractive index.

## Questions

```yaml
- question: "Light travels from glass (n = 1.5) into water (n = 1.33). Which correctly describes the refracted ray?"
  type: multiple-choice
  options:
    - "It bends toward the normal because it enters a denser medium"
    - "It bends away from the normal because it enters a less optically dense medium"
    - "It travels in the same direction because both media are transparent"
    - "It bends toward the normal because the wavelength increases upon entering water"
  answer: 1
  explanation: "When light moves from a higher-n to a lower-n medium (glass → water), it speeds up. By Snell's law n₁ sin θ₁ = n₂ sin θ₂, if n₁ > n₂ then sin θ₂ > sin θ₁, so θ₂ > θ₁ — the ray bends away from the normal. Option A confuses the direction of bending; 'denser medium' means higher n, which bends toward the normal — but here glass is the denser medium, not water."

- question: "When light passes from air into glass, which property of the wave remains unchanged at the interface?"
  type: multiple-choice
  options:
    - "Speed"
    - "Wavelength"
    - "Frequency"
    - "Direction of propagation"
  answer: 2
  explanation: "Frequency is set by the source and cannot change at the interface — wave cycles cannot be created or destroyed there (phase continuity). Speed decreases (v = c/n), wavelength shortens proportionally (λ = v/f), and direction changes. Frequency alone is invariant. This invariance is the physical reason refraction happens: the wavelength must shorten, which forces the wavefront to pivot."

- question: "A ray entering a medium with a higher refractive index always bends toward the normal."
  type: true-false
  answer: true
  explanation: "Snell's law: n₁ sin θ₁ = n₂ sin θ₂. If n₂ > n₁, then sin θ₂ must be smaller than sin θ₁ to keep the products equal, so θ₂ < θ₁ — the refracted ray is closer to the normal. This is unambiguous and direction-independent; entering a higher-n medium always bends toward the normal."

- question: "When light slows down upon entering a denser medium, its frequency decreases proportionally so that energy is conserved."
  type: true-false
  answer: false
  explanation: "Frequency does not change when light crosses an interface — it is determined by the source, not the medium. Energy per photon (E = hf) is also unchanged. What decreases proportionally with speed is the wavelength: since v = fλ, if v drops and f is fixed, then λ must drop by the same factor. Confusing wavelength change with frequency change is a common error."

- question: "Why does light change direction when it crosses from one medium into another? Explain in terms of what changes and what stays constant at the interface."
  type: short-answer
  answer: "Frequency must remain constant at the interface (wave cycles cannot be created or destroyed there). Since v = fλ, when the wave slows in the new medium, the wavelength must shorten. The portion of the wavefront that enters first slows and shortens, while the rest still travels at the original speed — this mismatch pivots the wavefront, changing the ray's direction. Snell's law quantifies that pivot."
  explanation: "The deeper insight is that bending is a consequence of wavelength change forced by frequency invariance. A useful analogy: soldiers marching at an angle toward mud — those who hit the mud first slow down, causing the rank to swing. The frequency-stays-constant constraint is what makes this analysis rigorous rather than just a visual analogy."
```

## Explainer

You already know that waves have a speed, frequency, and wavelength linked by v = fλ. When a wave crosses from one medium into another — say, from air into glass — something has to give. The frequency cannot change: it is set by the source, and the wave cannot pile up or thin out at the interface (that would require creating or destroying cycles of oscillation). So when the wave slows down in the denser medium, it is the **wavelength** that shortens to compensate. Shorter wavelength, same frequency, lower speed — v = fλ still holds.

This wavelength change is what causes **refraction**, the bending of the wave's direction. Picture a column of soldiers marching in a line at an angle toward muddy ground. The soldiers who hit the mud first slow down, while those still on firm ground continue at full speed. The rank swings around — the direction of travel rotates. Waves behave identically: the part of the wavefront that enters the slower medium first falls behind, pivoting the wavefront toward the normal. **Snell's law** formalizes this: n₁ sin θ₁ = n₂ sin θ₂, where n = c/v is the **refractive index** (a dimensionless measure of how much slower light travels in that medium relative to vacuum).

The law tells you the direction of bending unambiguously. When light enters a denser medium (n₂ > n₁), the right side of the equation must produce a smaller sin θ₂ — so θ₂ < θ₁, meaning the ray bends toward the normal. When light exits the dense medium back into air, it bends away from the normal. This asymmetry is why a straw in a glass of water appears bent: light from the underwater portion of the straw bends away from the normal as it exits the water into air, causing the apparent position of the straw to shift upward.

The refractive index also depends slightly on wavelength — a phenomenon called **dispersion**. Glass has a slightly higher n for violet light than for red light, so violet bends more steeply. A prism exploits this to spread white light into a rainbow; raindrops do the same thing to produce natural rainbows. You will encounter this dispersion again when studying wavelength and color. For now, Snell's law in its basic form treats n as a constant, which is an excellent approximation for monochromatic (single-wavelength) light and the foundation for all of geometrical optics that follows.
