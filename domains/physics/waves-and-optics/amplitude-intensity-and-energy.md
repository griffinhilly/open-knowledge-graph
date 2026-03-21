---
id: amplitude-intensity-and-energy
title: Amplitude, Intensity, and Wave Energy
domain: physics
course: waves-and-optics
prerequisites:
- id: wave-properties-and-classification
  type: hard
builds-toward:
- sound-intensity-and-decibels
tags:
- amplitude
- intensity
- energy
stage: formal-systems
status: draft
---

# Amplitude, Intensity, and Wave Energy

## Core Idea
Amplitude is the maximum displacement of a particle from equilibrium and determines the energy carried by a wave. Intensity is the average power per unit area perpendicular to wave propagation: I ∝ A². The energy in a wave increases quadratically with amplitude, so doubling amplitude quadruples intensity.

## How It's Best Learned
Measure sound intensity with a decibel meter at various distances from a speaker. Observe how shaking a rope harder (greater amplitude) sends more energy down the rope. Plot intensity vs distance.

## Common Misconceptions
- Amplitude and wavelength are related; they're independent properties.
- All waves lose energy equally; energy loss depends on the medium and distance.
- Intensity is proportional to amplitude; it's proportional to amplitude squared.

## Questions

```yaml
- question: "A speaker produces sound at a certain amplitude. If the amplitude is doubled, what happens to the intensity?"
  type: multiple-choice
  options:
    - "Intensity doubles — amplitude and intensity are proportional"
    - "Intensity increases by a factor of three — the relationship is slightly superlinear"
    - "Intensity quadruples — intensity scales with the square of amplitude"
    - "Intensity increases by a factor of eight — amplitude affects both energy and frequency"
  answer: 2
  explanation: "Intensity is proportional to amplitude squared (I ∝ A²). Doubling A gives (2A)² = 4A², so intensity quadruples. This quadratic relationship is counterintuitive but follows from the physics of simple harmonic motion: particles in a wave store both kinetic and potential energy, and both scale with A². Option A — the most tempting wrong answer — treats the relationship as linear, confusing a doubling of amplitude with a doubling of intensity."

- question: "A light bulb radiates energy uniformly in all directions. You move from 5 meters away to 10 meters away. How does the intensity of light at your new position compare to your original position?"
  type: multiple-choice
  options:
    - "Intensity halves — it is inversely proportional to distance"
    - "Intensity drops to one-quarter — it follows an inverse square law"
    - "Intensity stays the same — only the amplitude decreases, not the intensity"
    - "Intensity drops to one-eighth — both amplitude and area effects compound"
  answer: 1
  explanation: "For a point source radiating in three dimensions, the wavefront area grows as 4πr², so the same total power is spread over 4 times the area when distance doubles. Intensity (power per unit area) therefore drops to one-quarter — the inverse square law: I ∝ 1/r². This is a separate effect from the I ∝ A² relationship: the inverse square law describes how intensity changes with distance from a source; I ∝ A² describes how intensity depends on the amplitude of the wave itself."

- question: "If a wave's amplitude is tripled, its intensity increases by a factor of nine."
  type: true-false
  answer: true
  explanation: "Since I ∝ A², tripling the amplitude means intensity scales as (3A)² = 9A² — a ninefold increase. This is a direct application of the quadratic relationship. The factor is A², so multiplying A by any value n multiplies intensity by n²."

- question: "Doubling the amplitude of a wave doubles the energy it carries per unit area."
  type: true-false
  answer: false
  explanation: "Doubling amplitude quadruples intensity (energy per unit area per unit time), not doubles it, because I ∝ A². This is the most common misconception about wave energy — students often assume a linear relationship because many physical quantities scale proportionally. The quadratic relationship means small changes in amplitude produce large changes in energy, which is why a shout carries dramatically more energy than a whisper."

- question: "Why does wave energy scale with the square of amplitude rather than proportionally with amplitude? What is the physical reason for this quadratic relationship?"
  type: short-answer
  answer: "Particles in a wave undergo simple harmonic motion, storing both kinetic energy (½mv²) and potential energy (½kx²). Both forms of energy depend on the square of their respective quantities — velocity (which scales with amplitude) and displacement (which is amplitude). When you double the amplitude, maximum velocity doubles and maximum displacement doubles, so both kinetic and potential energy quadruple. The total energy, being the sum of two terms that each scale with A², therefore scales as A²."
  explanation: "The key is that energy in simple harmonic motion has two contributions — kinetic and potential — and both scale quadratically. This is why the I ∝ A² law applies across all wave types: mechanical waves, electromagnetic waves, and sound. Understanding this prevents the common error of treating amplitude as directly proportional to energy."
```

## Explainer

You already know that a wave is a disturbance that travels through a medium, carrying energy without permanently transporting matter. The **amplitude** of a wave measures how large that disturbance gets — the maximum displacement of any particle from its resting position. Think of shaking a rope: a gentle flick produces a small ripple, while a vigorous snap sends a large wave down the rope. That difference in disturbance size is amplitude, and it directly reflects how much energy you put into the wave.

The surprising result is how amplitude and energy relate: energy is proportional to amplitude *squared*, not amplitude itself. This means doubling the amplitude does not double the energy — it quadruples it. The formula I ∝ A² captures this. **Intensity** is defined as power per unit area (watts per square meter), and it measures how much wave energy passes through a given surface each second. A wave with twice the amplitude is four times as intense, not twice. A wave with three times the amplitude is nine times as intense. This quadratic scaling is counterintuitive but comes from the physics of simple harmonic motion — particles in a wave have both kinetic and potential energy, and both scale with A².

One practical consequence: loud sounds and bright light both follow this relationship. If you want to double the perceived power of a sound source, you do not simply double the amplitude — you need to quadruple the power output. This is why the decibel scale (which you'll encounter with sound intensity) uses a logarithmic compression: the actual intensity range humans experience, from a whisper to a jet engine, spans twelve orders of magnitude. The I ∝ A² relationship is the foundation for understanding why that range is so enormous.

Another consequence: waves spread out as they travel, and as they do, the energy spreads over an increasingly large area. For a wave radiating outward in three dimensions (like sound from a speaker or light from a bulb), the area of the expanding wavefront grows as the square of the distance. Since the total power stays constant, intensity must decrease inversely with the square of distance — the **inverse square law**. This is a separate effect from amplitude, but both combine to determine how much energy a wave delivers at any given point. Keeping amplitude and intensity conceptually distinct — while understanding that I ∝ A² connects them — is the foundation for all quantitative wave analysis.
