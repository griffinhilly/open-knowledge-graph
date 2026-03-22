---
id: wavelength-frequency-speed-relationship
title: Wavelength, Frequency, and Wave Speed
domain: physics
course: waves-and-optics
prerequisites:
- id: wave-properties-and-classification
  type: hard
builds-toward:
- doppler-shift-observer-motion
- sound-waves-longitudinal
tags:
- wavelength
- frequency
- wave-speed
stage: formal-systems
status: draft
---

# Wavelength, Frequency, and Wave Speed

## Core Idea
Wave speed is the product of wavelength (λ) and frequency (f): v = λf. This fundamental relationship connects the spatial extent of a wave cycle to its temporal repetition rate. The speed of a wave is determined by the medium's properties, not by the frequency or wavelength independently.

## Questions

```yaml
- question: "A sound wave traveling through air at 340 m/s has a frequency of 170 Hz. A musician plays a note at 340 Hz in the same room. What is the speed of the higher-frequency wave?"
  type: multiple-choice
  options:
    - "680 m/s — higher frequency means the wave moves faster"
    - "340 m/s — wave speed is determined by the medium, not the frequency"
    - "170 m/s — doubling frequency halves the speed"
    - "Cannot be determined without knowing the wavelength"
  answer: 1
  explanation: "Wave speed through a given medium is fixed by the medium's properties — in this case air at room temperature, where sound travels at approximately 340 m/s regardless of frequency. The 340 Hz wave also travels at 340 m/s. What changes is the wavelength: the 170 Hz note has λ = 340/170 = 2 m, while the 340 Hz note has λ = 340/340 = 1 m. Speed stays constant; wavelength and frequency vary inversely."

- question: "When light passes from air into glass, its speed decreases. Which of the following correctly describes what happens to its wavelength and frequency?"
  type: multiple-choice
  options:
    - "Both wavelength and frequency decrease proportionally"
    - "Wavelength decreases; frequency stays the same"
    - "Frequency increases; wavelength stays the same"
    - "Both wavelength and frequency stay the same; only amplitude changes"
  answer: 1
  explanation: "Frequency is tied to the energy of the photons (E = hf) and is determined by the source — it cannot change as light crosses a boundary. Speed decreases in glass because the medium slows the wave. Since v = λf and f is fixed, λ must decrease proportionally with v. This is why light bends (refracts) at boundaries: the wavelength shortens in the denser medium, which affects how the wavefronts are oriented. Speed and wavelength both decrease; frequency is the invariant."

- question: "In a given medium, doubling the frequency of a wave doubles its speed."
  type: true-false
  answer: false
  explanation: "Wave speed is a property of the medium, not the wave. Doubling frequency leaves speed unchanged and instead halves the wavelength. This follows directly from v = λf: if v is fixed and f doubles, then λ must halve so the product λf remains equal to v. The misconception that higher frequency → higher speed is tempting because in everyday life we associate faster vibration with faster motion, but waves don't work that way."

- question: "For a wave traveling through a fixed medium, if you know the wavelength, you can calculate the wave speed without knowing the frequency."
  type: true-false
  answer: false
  explanation: "Knowing wavelength alone is insufficient — you need both wavelength and frequency to calculate speed (v = λf). Conversely, if you know the medium, you know the speed independently of both λ and f. This is a subtle point: speed is a property of the medium and can be looked up, but the formula v = λf requires two of the three variables to find the third. You cannot infer speed from wavelength without also knowing frequency."

- question: "Why is it said that wave speed is 'set by the medium, not by the wave'? What does this mean physically, and what is its most important implication for how wavelength and frequency relate?"
  type: short-answer
  answer: "Wave speed depends on the mechanical or electromagnetic properties of the medium — density, elasticity, permittivity, etc. — not on how fast the source is vibrating. Because speed is fixed for a given medium, wavelength and frequency must vary inversely: if frequency increases, wavelength decreases proportionally so that their product (the speed) stays constant. This means you cannot change one without the other changing in compensation."
  explanation: "The physical reason is that the medium's restoring force and inertia determine how quickly a disturbance propagates — properties that belong to the medium, not the source. The most important implication is the inverse relationship λ ∝ 1/f (at constant v), which governs everything from why bass notes have longer wavelengths than treble notes in air, to why the same color of light has different wavelengths in different materials, to why the Doppler effect changes frequency but not wave speed through the medium."
```

## Explainer

From your study of wave properties, you know that a wave is a repeating disturbance with a characteristic **wavelength** (λ — the spatial length of one complete cycle, measured in meters) and **frequency** (f — the number of complete cycles passing a fixed point each second, measured in hertz). Wavelength is the spatial picture of the wave; frequency is the temporal picture. The equation v = λf unifies them through wave speed, and the relationship is almost inevitable once you understand what the two quantities mean.

Here is the intuition: if a wave has a frequency of 5 Hz, then 5 complete cycles pass any fixed point every second. If each cycle has a wavelength of 2 meters, then those 5 cycles occupy 5 × 2 = 10 meters of space. Since 10 meters of wave passes the point each second, the wave speed must be 10 m/s. There is nothing to memorize — **speed = distance per cycle × cycles per second = λ × f**. The formula is just the compact version of this reasoning, and you can reconstruct it from first principles whenever you need it.

The most important and counterintuitive implication is that **wave speed is set by the medium, not by the wave**. Sound travels at approximately 340 m/s through air at room temperature regardless of whether the source is a bass drum at 60 Hz or a piccolo at 4000 Hz. Since speed stays constant in a given medium, wavelength and frequency must vary inversely: low-frequency sounds have long wavelengths, high-frequency sounds have short wavelengths. The bass note at 60 Hz has a wavelength of about 5.7 m; the piccolo's note at 4000 Hz has a wavelength of about 8.5 cm. Both propagate through the room at 340 m/s.

This relationship builds directly toward the Doppler effect, where relative motion between source and observer appears to alter frequency (and therefore wavelength), even though the wave speed through the medium is unchanged. It also governs light in different materials: when light enters glass, its speed decreases, so for a fixed-frequency wave the wavelength must shorten proportionally. (Frequency stays fixed because it is tied to the energy of the photons; wavelength adjusts to match the new speed.) Every wave phenomenon from acoustics to optics to radio transmission depends on this single equation connecting three quantities — master it and you have a lever that reaches across all of wave physics.
