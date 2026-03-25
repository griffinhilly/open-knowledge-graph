---
id: energy-flow-rate-intensity
title: Energy Transport and Wave Intensity
domain: physics
course: waves-and-optics
prerequisites:
- id: particle-velocity-oscillating-motion
  type: hard
- id: power-and-work-rate
  type: soft
- id: amplitude-intensity-and-energy
  type: soft
builds-toward:
- sound-level-logarithmic-scale
- wave-energy-and-intensity
tags:
- waves
- energy
- power
stage: advanced
status: validated
---
# Energy Transport and Wave Intensity

## Core Idea
Intensity is the average power per unit area carried by a wave (I ∝ A² f²), proportional to the square of amplitude and frequency. Energy flows at the group velocity in dispersive media. The Poynting vector describes energy flow direction and magnitude in electromagnetic waves.

## Questions

```yaml
- question: "A speaker produces sound waves. You double the amplitude of oscillation of the air particles near the speaker. By what factor does the sound intensity change?"
  type: multiple-choice
  options:
    - "It doubles — intensity is proportional to amplitude"
    - "It quadruples — intensity is proportional to amplitude squared"
    - "It increases by a factor of 8 — intensity depends on both amplitude and the cube of frequency"
    - "It remains unchanged — intensity depends only on frequency, not amplitude"
  answer: 1
  explanation: "Intensity scales with the square of amplitude: I ∝ A². Doubling A gives (2A)² = 4A², so intensity quadruples. This follows directly from the energy stored in simple harmonic motion, which goes as kA². Intensity measures the power delivered per unit area, and that power scales with the square of the displacement amplitude. Option D is the common misconception — amplitude and intensity are tightly linked."

- question: "A point source of sound radiates uniformly in all directions. A microphone at 3 m from the source measures an intensity of 0.04 W/m². A second microphone is placed 9 m from the source. What intensity does it measure?"
  type: multiple-choice
  options:
    - "0.013 W/m² — intensity falls as 1/r, so tripling distance cuts it to a third"
    - "0.020 W/m² — intensity falls as 1/√r"
    - "0.0044 W/m² — intensity falls as 1/r², so tripling distance cuts it to one-ninth"
    - "0.04 W/m² — intensity is conserved and independent of distance"
  answer: 2
  explanation: "For a point source, the same total power spreads over a sphere whose area grows as 4πr². Since intensity = power/area, and area ∝ r², intensity ∝ 1/r² — the inverse square law. Tripling distance (from 3 to 9 m) means r² increases by 9, so intensity becomes 0.04/9 ≈ 0.0044 W/m². Option A is the most common distractor: students confuse 1/r (which describes wave amplitude) with 1/r² (which describes intensity)."

- question: "Wave intensity is proportional to both the square of amplitude and the square of frequency."
  type: true-false
  answer: true
  explanation: "The full expression is I ∝ A²f², where A is amplitude and f is frequency. Each oscillation cycle carries energy, and higher frequency means more cycles per second. Combined with the amplitude-squared dependence from the energy in each oscillation, both factors contribute to intensity. This means a wave with twice the frequency and the same amplitude carries four times the intensity."

- question: "The Poynting vector of an electromagnetic wave points in a direction perpendicular to the wave's direction of propagation."
  type: true-false
  answer: false
  explanation: "The Poynting vector S = E × B / μ₀ points in the *same* direction as wave propagation, not perpendicular to it. It represents the direction and magnitude of energy flow. The electric (E) and magnetic (B) fields are each perpendicular to the propagation direction and to each other; their cross product therefore points along the propagation direction. Confusing the orientation of the fields with the direction of energy transport is the common error here."

- question: "Why does wave intensity obey an inverse square law for a point source, even if the medium absorbs no energy at all?"
  type: short-answer
  answer: "Because the total power emitted by the source is constant and spreads over spherical wavefronts whose surface area grows as 4πr². Intensity is power per unit area, so as the same power is divided among an ever-larger area, intensity must decrease as 1/r². No energy is lost — it is simply spread more thinly."
  explanation: "This is a geometry argument, not an energy-loss argument. Energy is conserved: the total power crossing any sphere centered on the source is the same. But the area of that sphere is 4πr², so intensity — power per unit area — must fall as 1/r². This principle applies to light, sound, gravity, and any other quantity that radiates isotropically from a point source."
```

## Explainer

You already know from oscillating motion that the energy stored in a vibrating particle scales with the square of its amplitude — a particle displaced twice as far has four times the potential energy. Waves carry energy by passing that oscillation from particle to particle, so it follows directly that **wave intensity** — the rate at which energy passes through a unit area — also scales with amplitude squared: I ∝ A². Double the amplitude and you quadruple the power delivered to any surface the wave passes through. Frequency matters too: higher frequency means more oscillation cycles per second, each carrying energy, giving the I ∝ f² dependence.

From your work on power and work rate, you know power is energy per unit time. Intensity simply divides that further by the area over which the power is spread. Think of a speaker: it radiates sound power outward in all directions. As you move away, that same total power is spread over an ever-larger spherical surface (area = 4πr²). Since the power is conserved but the area grows as r², intensity falls as 1/r² — the **inverse square law** for point sources. This is why sound seems four times quieter when you double your distance from a loudspeaker.

For electromagnetic waves, the concept needs a vector treatment. The **Poynting vector** S = E × B / μ₀ points in the direction the wave is traveling and has magnitude equal to the instantaneous intensity. The cross product of the electric and magnetic fields gives the direction of energy flow — always perpendicular to both fields — which is exactly the direction of wave propagation. For a plane wave traveling in one direction, the time-averaged Poynting vector magnitude gives the average intensity that you'd measure with a light meter or power sensor.

The key insight connecting all these cases is that energy does not "travel with" the medium. The medium oscillates back and forth while the energy pattern advances steadily forward. The particles you studied in oscillating motion stay roughly in place; what moves is the organized disturbance. Intensity measures how much of that organized energy flux passes through a cross-section per second — whether the wave is sound, light, seismic, or electromagnetic, the same dimensional relationship (power per area) captures how concentrated or diffuse that energy flow is.
