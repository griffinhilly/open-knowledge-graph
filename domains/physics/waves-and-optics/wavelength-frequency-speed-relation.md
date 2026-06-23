---
id: wavelength-frequency-speed-relation
title: Wavelength, Frequency, and Wave Speed
domain: physics
course: waves-and-optics
prerequisites:
- id: harmonic-wave-time-dependence
  type: hard
- id: transverse-wave-characteristics
  type: soft
- id: wave-properties-and-classification
  type: soft
builds-toward:
- acoustic-wave-speed-properties
- diffraction-resolution-angular-separation
tags:
- waves
- kinematics
stage: advanced
status: validated
---

# Wavelength, Frequency, and Wave Speed

## Core Idea
The fundamental relation v = fλ connects wave speed (v), frequency (f), and wavelength (λ). Frequency is determined by the source, wavelength by the medium's properties (via wave speed), and the product always gives the propagation speed. This simple relation allows prediction of how waves behave when they change media.

## Questions

```yaml
- question: "A 440 Hz sound wave travels from air (343 m/s) into water (1480 m/s). What happens to its wavelength?"
  type: multiple-choice
  options:
    - "It increases by a factor of about 4.3, because a higher wave speed at the same frequency requires a longer wavelength"
    - "It stays the same, because wavelength — like frequency — is set by the source"
    - "It decreases, because the denser medium compresses the wave spatially"
    - "It increases, but so does frequency, so the wave speed ratio is preserved"
  answer: 0
  explanation: "Frequency is fixed by the source at 440 Hz and cannot change at the boundary. Wave speed is determined by the new medium: 1480 m/s in water. Since v = fλ, wavelength = v/f = 1480/440 ≈ 3.4 m, compared to 343/440 ≈ 0.78 m in air — about 4.3 times longer. Option B describes the most common misconception: students often think wavelength is 'set by the source' like frequency, but it is the quantity that adjusts when the medium changes. Option C is wrong because a faster medium lengthens, not compresses, the wavelength."

- question: "Which quantity is determined by the source of a wave rather than by the medium through which it travels?"
  type: multiple-choice
  options:
    - "Wavelength — the spatial period is fixed when the wave is emitted"
    - "Wave speed — the source controls how fast the disturbance propagates"
    - "Frequency — the source oscillates at a fixed rate that the medium cannot alter"
    - "All three are fixed by the medium once the wave enters it"
  answer: 2
  explanation: "The source oscillates at frequency f, completing f cycles per second. A medium boundary cannot change this rate — it would require the medium to somehow speed up or slow down the source's vibration, which is physically incoherent. Wave speed is entirely determined by medium properties (density and elasticity for mechanical waves). Since v = fλ and v changes at the boundary while f stays constant, wavelength must adjust: λ = v/f. This is why light slows in glass (lower v) and its wavelength shortens, while frequency (and thus color) stays the same."

- question: "When light passes from air into glass, its frequency stays the same but its wavelength shortens."
  type: true-false
  answer: true
  explanation: "This is the direct consequence of v = fλ. Frequency is fixed by the source. Glass slows light (lower v than air). Since λ = v/f and f is constant, a smaller v forces a smaller λ. This wavelength change at the boundary is also the origin of refraction: the wavefronts bend because the wavelength changes on one side before the other."

- question: "If you double the frequency of a wave while keeping the wave speed constant, the wavelength also doubles."
  type: true-false
  answer: false
  explanation: "From v = fλ, if v is constant and f doubles, then λ = v/f must halve. Frequency and wavelength are inversely proportional at constant wave speed. A common error is treating them as independent quantities; v = fλ is a constraint that ties all three together."

- question: "Why does wavelength (and not frequency) change when a wave crosses from one medium into another?"
  type: short-answer
  answer: "Frequency is set by the source — the rate at which it oscillates — and a passive medium boundary has no mechanism to alter that rate. Wave speed, however, is a property of the medium (its density, stiffness, or electromagnetic constants), so it changes at the boundary. Since v = fλ and f is fixed, wavelength must adjust to satisfy the relation: λ = v/f. In a faster medium, wavelength is longer; in a slower medium, it is shorter."
  explanation: "The physical image is helpful: in one period T = 1/f, the source produces exactly one wavelength's worth of disturbance. If the wave is slower on the other side, those same crests are packed more closely together — shorter λ. The number of crests passing any point per second (f) hasn't changed, because the source is still generating them at the same rate."
```

## Explainer

From harmonic wave time-dependence, you know that a wave oscillates in time at frequency f: the displacement at any fixed point in space completes f full cycles per second, with period T = 1/f. The wave also has a spatial pattern — the displacement varies with position, forming crests and troughs. The distance between two adjacent identical points (two crests, two troughs, or two zero-crossings moving in the same direction) is the **wavelength** λ. The equation v = fλ connects the wave's spatial structure (λ) to its temporal structure (f) through the speed at which the pattern travels (v).

The physical derivation is worth carrying out mentally once. In one period T, the source completes one full oscillation and sends exactly one wavelength of disturbance down the medium. That wavefront advances a distance of one wavelength in a time T. Speed is distance divided by time, so v = λ/T = λ·f. The equation is unavoidable once you accept those two facts. There's no free parameter to choose.

The equation's most important consequence involves what happens when a wave crosses from one medium into another. The **frequency is set by the source** and does not change at the boundary — it would be physically incoherent for the medium to somehow alter the rate at which the source oscillates. What changes is the wave speed, which depends on the new medium's properties (density, elasticity for mechanical waves; permittivity, permeability for electromagnetic waves). Since v = fλ and f is fixed, a slower medium forces a shorter wavelength; a faster medium forces a longer wavelength. When light enters glass (slower medium), its frequency stays fixed, its speed drops, and its wavelength shortens. The direction change you call **refraction** is a consequence of this wavelength change at the boundary.

In practice, v = fλ solves a third of unknown given the other two. For sound in air at 20 °C, v ≈ 343 m/s; a 440 Hz musical A has wavelength 343/440 ≈ 0.78 m. For visible light in vacuum, v = 3 × 10⁸ m/s; green light at 550 nm has frequency f = 3 × 10⁸ / 550 × 10⁻⁹ ≈ 5.5 × 10¹⁴ Hz. When a problem tells you a wave passes from air into water where sound travels at 1,480 m/s, the frequency stays at 440 Hz and the wavelength becomes 1480/440 ≈ 3.4 m — more than four times longer. The same number of cycles per second now spans much more distance per cycle.
