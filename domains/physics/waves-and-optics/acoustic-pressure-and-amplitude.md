---
id: acoustic-pressure-and-amplitude
title: Acoustic Pressure and Amplitude in Sound Waves
domain: physics
course: waves-and-optics
prerequisites:
- id: sound-waves-intro
  type: hard
- id: pressure
  type: soft
builds-toward:
- sound-intensity-and-decibels
tags:
- sound
- pressure
- amplitude
stage: formal-systems
status: draft
---

# Acoustic Pressure and Amplitude in Sound Waves

## Core Idea
Sound waves create oscillating pressure variations in the medium: P = Pamplitude × sin(kx - ωt). Acoustic pressure amplitude is related to particle velocity amplitude by P = ρvvₚ. Higher pressure amplitudes correspond to louder sounds and higher acoustic intensity.

## Explainer

You already know from sound-waves-intro that sound is a longitudinal wave — particles in the medium being pushed together (compressions) and pulled apart (rarefactions) as the wave passes. The next step is to describe these disturbances quantitatively. The key quantity is **acoustic pressure**: the difference between the local pressure at a point in the medium and the undisturbed ambient pressure. As the wave passes, each point oscillates between positive acoustic pressure (compression) and negative acoustic pressure (rarefaction). This oscillation follows the same sinusoidal form as any wave: P(x,t) = P_amplitude × sin(kx − ωt).

The **pressure amplitude** P_amplitude is the peak value of that departure from ambient. A whisper produces a pressure amplitude of roughly 0.02 Pa — a tiny fraction of atmospheric pressure (101,325 Pa), yet easily detected by the ear. A jet engine at close range produces roughly 200 Pa. These numbers make clear that we are dealing with extremely small pressure variations relative to background, which is why the ear evolved such extraordinary sensitivity to detect them.

There is a deep physical link between acoustic pressure and particle motion. When a compression arrives, the particles are not only squeezed together — they are also moving, rushing toward the region of high pressure. The pressure amplitude and the **particle velocity amplitude** v_p are proportional through the medium's properties: P_amplitude = ρ × v_sound × v_p, where ρ is the medium's density and v_sound is the wave speed. The product ρv_sound is called the **acoustic impedance** of the medium. A high acoustic impedance means a large pressure swing is required to drive a given particle velocity — just as high electrical resistance requires high voltage to drive a given current.

The practical payoff is the relationship between pressure amplitude and **acoustic intensity** (power per unit area): I ∝ P_amplitude². This is the same squared-amplitude proportionality you saw for mechanical waves — doubling the pressure amplitude quadruples the intensity. This quadratic relationship is precisely why the decibel scale (which you'll encounter next in sound-intensity-and-decibels) uses a logarithmic unit: the enormous range of intensities the ear can handle compresses into a manageable 0–140 dB scale.
