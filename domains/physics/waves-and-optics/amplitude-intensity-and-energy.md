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

## Explainer

You already know that a wave is a disturbance that travels through a medium, carrying energy without permanently transporting matter. The **amplitude** of a wave measures how large that disturbance gets — the maximum displacement of any particle from its resting position. Think of shaking a rope: a gentle flick produces a small ripple, while a vigorous snap sends a large wave down the rope. That difference in disturbance size is amplitude, and it directly reflects how much energy you put into the wave.

The surprising result is how amplitude and energy relate: energy is proportional to amplitude *squared*, not amplitude itself. This means doubling the amplitude does not double the energy — it quadruples it. The formula I ∝ A² captures this. **Intensity** is defined as power per unit area (watts per square meter), and it measures how much wave energy passes through a given surface each second. A wave with twice the amplitude is four times as intense, not twice. A wave with three times the amplitude is nine times as intense. This quadratic scaling is counterintuitive but comes from the physics of simple harmonic motion — particles in a wave have both kinetic and potential energy, and both scale with A².

One practical consequence: loud sounds and bright light both follow this relationship. If you want to double the perceived power of a sound source, you do not simply double the amplitude — you need to quadruple the power output. This is why the decibel scale (which you'll encounter with sound intensity) uses a logarithmic compression: the actual intensity range humans experience, from a whisper to a jet engine, spans twelve orders of magnitude. The I ∝ A² relationship is the foundation for understanding why that range is so enormous.

Another consequence: waves spread out as they travel, and as they do, the energy spreads over an increasingly large area. For a wave radiating outward in three dimensions (like sound from a speaker or light from a bulb), the area of the expanding wavefront grows as the square of the distance. Since the total power stays constant, intensity must decrease inversely with the square of distance — the **inverse square law**. This is a separate effect from amplitude, but both combine to determine how much energy a wave delivers at any given point. Keeping amplitude and intensity conceptually distinct — while understanding that I ∝ A² connects them — is the foundation for all quantitative wave analysis.
