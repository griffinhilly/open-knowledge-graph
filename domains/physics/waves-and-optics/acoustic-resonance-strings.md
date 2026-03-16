---
id: acoustic-resonance-strings
title: Acoustic Resonance in Strings and Tension
domain: physics
course: waves-and-optics
prerequisites:
- id: standing-waves-formation-mechanism
  type: hard
builds-toward:
- fundamental-frequency-and-overtones
tags:
- resonance
- strings
- tension
- fundamental-frequency
stage: formal-systems
status: draft
---

# Acoustic Resonance in Strings and Tension

## Core Idea
A string fixed at both ends resonates at discrete frequencies where standing waves fit: f_n = n v/(2L) = n/(2L) √(T/μ), where n = 1, 2, 3, ... (harmonics), v is wave speed, T is tension, L is length, and μ is linear mass density. The fundamental (n=1) has the longest wavelength; higher harmonics have progressively shorter wavelengths and higher frequencies.

## Explainer

You already know from standing waves that when two identical waves travel in opposite directions along a medium, they can superimpose to form a stable pattern of **nodes** (points of zero displacement) and **antinodes** (points of maximum displacement). A string fixed at both ends has a boundary condition that forces both ends to be nodes — the string cannot move where it is attached. This constraint is what produces the discrete, quantized set of resonant frequencies.

Imagine driving the string with a vibrating source. Most driving frequencies produce a chaotic, rapidly-decaying response: the reflections from the two ends return out of phase and cancel the motion. But at certain special frequencies, the reflected wave arrives back in phase with the original — the two reinforce each other and the amplitude builds. These are the **resonant frequencies**, and they are exactly the frequencies for which a whole number of half-wavelengths fits between the endpoints. For the **fundamental** (first harmonic, n = 1), one half-wavelength spans the full length L, so λ₁ = 2L. For the **second harmonic** (first overtone, n = 2), two half-wavelengths fit, so λ₂ = L. In general, λ_n = 2L/n.

The connection to tension and mass density comes through the wave speed on the string: v = √(T/μ). This relationship has an intuitive basis — a tighter string (higher T) snaps back to equilibrium more forcefully, so disturbances travel faster. A heavier string (higher μ) has more inertia, so disturbances travel slower. Substituting v = fλ into f_n = v/λ_n gives f_n = n/(2L) · √(T/μ). So to raise all the resonant frequencies of a guitar string, you can either shorten it (decrease L), tighten it (increase T), or use a thinner string (decrease μ). Guitarists exploit all three: fretting shortens the vibrating length, tuning pegs adjust tension, and different strings have different mass densities.

The **harmonic series** f₁, 2f₁, 3f₁, ... has a deep consequence for musical timbre. When you pluck a guitar string, you excite many harmonics simultaneously. The relative amplitudes of each harmonic — not just the fundamental — determine the characteristic sound of the instrument. A violin and a flute playing the same note have the same fundamental frequency, but sound different because they excite different mixtures of harmonics. In this way, the physics of resonance on a string is the physical foundation for understanding timbre and musical acoustics.
