---
id: wave-energy-and-intensity
title: Wave Energy and Intensity
domain: physics
course: waves-and-optics
prerequisites:
- id: wave-properties-intro
  type: hard
- id: kinetic-energy
  type: soft
builds-toward:
- sound-intensity-and-decibels
- youngs-double-slit
tags:
- wave energy
- intensity
- amplitude
- inverse square law
- power
stage: formal-systems
status: validated
---

# Wave Energy and Intensity

## Core Idea
The energy carried by a wave is proportional to the square of its amplitude: E ∝ A². Intensity (power per unit area, I = P/A) is likewise proportional to A². For a point source radiating in three dimensions, intensity decreases as the inverse square of distance: I ∝ 1/r². This inverse-square law is a purely geometric result — the same power spreads over a larger spherical surface as r increases. Amplitude therefore decreases as 1/r.

## How It's Best Learned
Measure the loudness (approximately ∝ intensity) of a sound source at distances 1m, 2m, and 4m from the source. Verify that intensity roughly quarters each time distance doubles.

## Common Misconceptions
- Intensity ∝ A² is counterintuitive; doubling amplitude quadruples intensity, not doubles it.
- The inverse-square law assumes isotropic propagation in 3D; for waves confined to 2D (surface waves) or 1D (strings), energy falls off differently.

## Explainer

From kinetic energy, you know that energy scales with the square of velocity: KE = ½mv². Waves carry energy by making particles oscillate, and the maximum speed of those oscillating particles is proportional to amplitude A — a larger displacement means faster oscillatory motion. Combining these two ideas gives the foundational result: **wave energy is proportional to the square of amplitude**, E ∝ A². This quadratic relationship is the reason a wave twice as tall carries four times the energy, not twice. The same logic applies to intensity — the power delivered per unit area of wavefront — so I ∝ A² as well. Doubling the amplitude of a sound wave quadruples its perceived loudness in physical terms, which is why acoustics uses a logarithmic decibel scale to make the range of human hearing manageable.

**Intensity** is defined as power per unit area: I = P/A (where A here is area, not amplitude). Imagine a point source radiating power uniformly in all directions. At distance r, that fixed total power P is spread over the surface area of a sphere: 4πr². Since I = P/(4πr²), intensity falls off as 1/r². This is the **inverse-square law**, and it is a purely geometric result — the energy doesn't disappear, it just spreads over an ever-larger surface as the wavefront expands. Double the distance from a campfire and the warmth you feel drops to one-quarter; move three times as far and it drops to one-ninth.

The amplitude consequence follows directly. Since I ∝ A² and I ∝ 1/r², combining them gives A ∝ 1/r. Amplitude decreases linearly with distance for a spherical wave in three dimensions. This is why you can shout across a room but not across a football field — the same vocal power spreads over a sphere that is thousands of times larger in area. Whispers carry even less power to begin with, making the 1/r² fall-off doubly unforgiving.

It is important to note the geometric assumption embedded in the inverse-square law. It holds for waves that radiate isotropically into three dimensions. Surface waves on water, confined to two dimensions, spread over a circular perimeter 2πr rather than a spherical surface 4πr², so intensity falls as 1/r instead of 1/r². Waves on a string are one-dimensional — they carry the same intensity everywhere along the string, ignoring damping. Whenever you apply the inverse-square law, verify that the wave is genuinely radiating in three-dimensional open space; beams, waveguides, and acoustic horns deliberately break the 3D assumption to prevent the energy loss that would otherwise occur.


