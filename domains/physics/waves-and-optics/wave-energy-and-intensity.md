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
- id: energy-flow-rate-intensity
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

## Questions

```yaml
- question: "A speaker produces sound waves with amplitude A. The amplitude is doubled to 2A. What happens to the intensity of the sound?"
  type: multiple-choice
  options:
    - "It doubles — intensity is proportional to amplitude"
    - "It quadruples — intensity is proportional to the square of amplitude"
    - "It increases by √2 — the relationship is through the square root"
    - "It stays the same — intensity depends on frequency, not amplitude"
  answer: 1
  explanation: "Intensity is proportional to the square of amplitude: I ∝ A². Doubling the amplitude gives (2A)² = 4A², so intensity quadruples. This quadratic relationship is the central counterintuitive fact of wave energy — many students expect a linear relationship. It's the reason acoustics uses a logarithmic decibel scale: the physical intensity range of human hearing spans many orders of magnitude."

- question: "A point source of sound is 2 m from a listener. The listener moves to 6 m from the source. By what factor does the intensity change?"
  type: multiple-choice
  options:
    - "It decreases by a factor of 3 — intensity is inversely proportional to distance"
    - "It decreases by a factor of 9 — intensity follows the inverse-square law"
    - "It decreases by a factor of 6 — the total distance traveled by the wave"
    - "It decreases by a factor of 4 — distance doubled (approximately)"
  answer: 1
  explanation: "I ∝ 1/r². The distance tripled (from 2 m to 6 m), so intensity changes by 1/3² = 1/9. The inverse-square law is a geometric result: the same power spreads over a sphere of area 4πr², which grows as r². Tripling the distance means the sphere's area increases by 9×, so each unit area receives 1/9 the power."

- question: "For a wave traveling along a one-dimensional string, intensity decreases as 1/r² with distance from the source."
  type: true-false
  answer: false
  explanation: "False. The inverse-square law applies to waves radiating isotropically in three dimensions. A wave on a one-dimensional string does not spread over an expanding surface area — energy stays concentrated along the string, so intensity (ignoring damping) remains constant with distance. The 1/r² law is a geometric consequence of 3D spherical spreading, and it only applies when waves genuinely propagate in open three-dimensional space."

- question: "Doubling the distance from a point source reduces the wave amplitude to half its original value."
  type: true-false
  answer: true
  explanation: "True. Since I ∝ A² and I ∝ 1/r², combining gives A ∝ 1/r. Amplitude decreases linearly (not quadratically) with distance for a spherical wave in 3D. If you double the distance, A → A/2. This is why sound becomes dramatically quieter as you move away — both amplitude and intensity fall, but intensity falls faster (as 1/r²) while amplitude falls as 1/r."

- question: "Why is the inverse-square law for intensity described as a 'purely geometric result'?"
  type: short-answer
  answer: "Because it follows from geometry alone, not from any property of the wave or medium. A point source radiates fixed total power P uniformly over a sphere of area 4πr². Intensity I = P/(4πr²) must fall as 1/r² because the same energy is spread over an ever-larger surface as r grows. No energy disappears — it just thins out across a larger area."
  explanation: "The key insight is that the 1/r² law is about the geometry of spheres, not about anything special about waves. Any quantity (light, gravity, electrostatic force) that radiates isotropically from a point source into 3D space will follow an inverse-square law for the same reason. Waves in 2D (surface waves) follow 1/r; waves in 1D (strings) don't diminish at all — the dimensionality of the spreading determines the law."
```

## Explainer

From kinetic energy, you know that energy scales with the square of velocity: KE = ½mv². Waves carry energy by making particles oscillate, and the maximum speed of those oscillating particles is proportional to amplitude A — a larger displacement means faster oscillatory motion. Combining these two ideas gives the foundational result: **wave energy is proportional to the square of amplitude**, E ∝ A². This quadratic relationship is the reason a wave twice as tall carries four times the energy, not twice. The same logic applies to intensity — the power delivered per unit area of wavefront — so I ∝ A² as well. Doubling the amplitude of a sound wave quadruples its perceived loudness in physical terms, which is why acoustics uses a logarithmic decibel scale to make the range of human hearing manageable.

**Intensity** is defined as power per unit area: I = P/A (where A here is area, not amplitude). Imagine a point source radiating power uniformly in all directions. At distance r, that fixed total power P is spread over the surface area of a sphere: 4πr². Since I = P/(4πr²), intensity falls off as 1/r². This is the **inverse-square law**, and it is a purely geometric result — the energy doesn't disappear, it just spreads over an ever-larger surface as the wavefront expands. Double the distance from a campfire and the warmth you feel drops to one-quarter; move three times as far and it drops to one-ninth.

The amplitude consequence follows directly. Since I ∝ A² and I ∝ 1/r², combining them gives A ∝ 1/r. Amplitude decreases linearly with distance for a spherical wave in three dimensions. This is why you can shout across a room but not across a football field — the same vocal power spreads over a sphere that is thousands of times larger in area. Whispers carry even less power to begin with, making the 1/r² fall-off doubly unforgiving.

It is important to note the geometric assumption embedded in the inverse-square law. It holds for waves that radiate isotropically into three dimensions. Surface waves on water, confined to two dimensions, spread over a circular perimeter 2πr rather than a spherical surface 4πr², so intensity falls as 1/r instead of 1/r². Waves on a string are one-dimensional — they carry the same intensity everywhere along the string, ignoring damping. Whenever you apply the inverse-square law, verify that the wave is genuinely radiating in three-dimensional open space; beams, waveguides, and acoustic horns deliberately break the 3D assumption to prevent the energy loss that would otherwise occur.


