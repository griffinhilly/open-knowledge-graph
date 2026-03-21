---
id: refraction-and-snells-law
title: Refraction and Snell's Law
domain: physics
course: waves-and-optics
prerequisites:
- id: wavelength-frequency-speed-relationship
  type: hard
- id: wave-properties-and-classification
  type: soft
builds-toward:
- snells-law
- critical-angle-total-internal-reflection-optical
tags:
- refraction
- snells-law
- refractive-index
stage: formal-systems
status: draft
---

# Refraction and Snell's Law

## Core Idea
Refraction occurs when a wave crosses an interface between two media with different wave speeds, causing the wave to bend. Snell's law relates incident and refracted angles: n₁ sin θ₁ = n₂ sin θ₂, where n is the refractive index of each medium. Refraction happens because the wave slows down (or speeds up), changing its direction while maintaining frequency.

## Questions

```yaml
- question: "Light travels from glass (n = 1.5) into water (n = 1.33). What happens to the light ray at the boundary?"
  type: multiple-choice
  options:
    - "It bends toward the normal, since it enters a denser medium"
    - "It bends away from the normal, since it enters a medium with a lower refractive index and speeds up"
    - "It continues straight — bending only occurs when going from lower to higher refractive index"
    - "It reflects entirely — light cannot pass from glass to water"
  answer: 1
  explanation: "When light crosses from a higher-index medium (glass, n=1.5) to a lower-index medium (water, n=1.33), it speeds up. Snell's law confirms: n₁ sin θ₁ = n₂ sin θ₂; with n₁ > n₂, sin θ₂ > sin θ₁, so the refracted angle is larger — the ray bends away from the normal. The common misconception (option A) is that 'denser always means toward the normal.' The direction depends entirely on which side has the higher index: higher to lower means away from normal, lower to higher means toward normal."

- question: "A student reasons: 'When light slows down entering glass from air, its frequency must decrease since v = fλ.' What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing — frequency does decrease proportionally when the wave slows down"
    - "Frequency is set by the source and cannot change at a boundary — wavelength decreases instead, since v = fλ and f is fixed"
    - "The formula v = fλ doesn't apply at boundaries, only inside a homogeneous medium"
    - "Speed doesn't actually change at the boundary — only the direction of propagation changes"
  answer: 1
  explanation: "Frequency is determined by the source — wave crests are emitted at a fixed rate and arrive at the boundary at that same rate. They cannot pile up or disappear, so frequency is invariant across any boundary. Since v = fλ and f is constant, a decrease in speed (denser medium) must be accompanied by a decrease in wavelength. This wavelength compression — not frequency change — is the mechanical cause of refraction. The explainer makes this explicit: 'a slower medium means a shorter wavelength.'"

- question: "A light ray entering a flat glass slab at an angle bends toward the normal at entry, then bends away from the normal at exit — so the emergent ray is parallel to the incident ray, only laterally displaced."
  type: true-false
  answer: true
  explanation: "At the first surface (air→glass), the ray slows and bends toward the normal. At the second parallel surface (glass→air), it speeds up and bends away from the normal by exactly the same angle. Since both surfaces are parallel, the two refractions cancel, and the exit ray is parallel to the entry ray — just shifted sideways. The explainer states: 'A flat slab of glass produces two parallel refractions that cancel out, leaving the beam displaced but not deflected.'"

- question: "A straw appears bent in a glass of water because light travels at different speeds through the glass container versus the water."
  type: true-false
  answer: false
  explanation: "The apparent bend is caused by refraction at the water-air interface, not the glass. Light from the submerged portion of the straw travels through water, strikes the water-air boundary, and refracts (changes direction) before reaching the eye. The glass container is not the relevant boundary for this effect — a straw in an open bowl of water with no glass would appear equally bent. The interface between two media with different refractive indices is what causes bending, and here that interface is water-to-air."

- question: "When a wave crosses a boundary from one medium into another, why does its wavelength change but not its frequency?"
  type: short-answer
  answer: "Frequency is determined by the source — the number of wave crests generated per second is fixed before the wave reaches the boundary. At the interface, crests arrive at exactly the rate they were emitted and depart at the same rate; they cannot accumulate or disappear. So frequency is conserved across any boundary. Since the wave speed changes (due to the new medium's physical properties) and v = fλ with f fixed, wavelength must change to compensate: λ = v/f. A slower medium means shorter wavelength."
  explanation: "Frequency invariance at boundaries is a universal property of wave behavior, not specific to light. If frequency changed, wave crests would either pile up (building infinite amplitude) or thin out at the interface — physically impossible in steady state. The angular bending of Snell's law is the geometric consequence of wavefront portions with different wavelengths arriving at the boundary simultaneously."
```

## Explainer

From your study of wave properties, you know that waves have three interdependent quantities: frequency f, wavelength λ, and speed v, related by v = fλ. When a wave crosses the boundary between two media, its frequency cannot change — the wave crests arrive at the boundary at the same rate they depart, so f is fixed by the source. But the wave speed changes because the new medium has different physical properties. Since v = fλ and f is constant, a slower medium means a shorter wavelength. This wavelength compression is the mechanical cause of refraction.

The direction change can be understood with a simple marching band analogy. Imagine a line of marchers walking diagonally from pavement onto mud, where they can only walk at half the speed. The marchers who hit the mud first slow down while the others are still on pavement. The whole line pivots toward the slower side. Waves do exactly this: the portion of the wavefront that enters the denser medium first slows and the wavefront rotates, bending the ray toward the normal (the perpendicular to the surface). **Snell's law**, n₁ sin θ₁ = n₂ sin θ₂, is the quantitative statement of this rotation, where angles are measured from the normal and n = c/v is the **refractive index** (how many times slower light travels in the medium compared to a vacuum).

The direction of bending follows from the index values. When light goes from a lower-index medium to a higher-index one (air into glass, n₁ < n₂), it slows down and bends toward the normal — the refracted angle is smaller than the incident angle. Going the other way (glass into air), light speeds up and bends away from the normal. A flat slab of glass produces two parallel refractions that cancel out, leaving the beam displaced but not deflected. A prism refracts the beam twice at non-parallel surfaces, producing a net deflection — and because different wavelengths have slightly different refractive indices in glass (**dispersion**), they exit at different angles, spreading white light into its spectrum.

Everyday examples abound. A straw appears bent in a glass of water because the light rays from the submerged part refract at the water-air interface, changing direction before reaching your eye. The apparent depth of a swimming pool is less than the actual depth for the same reason — refracted rays make the bottom appear closer. Eyeglass lenses and camera optics deliberately engineer specific curvatures to exploit refraction at precise angles, making Snell's law the governing equation behind essentially all of optics that involves glass or water. The next topics in this course — total internal reflection and lenses — are both direct extensions of this single equation.


