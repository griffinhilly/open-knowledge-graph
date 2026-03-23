---
id: particle-velocity-oscillating-motion
title: Particle Velocity in Wave Motion
domain: physics
course: waves-and-optics
prerequisites:
- id: harmonic-wave-time-dependence
  type: hard
builds-toward:
- energy-flow-rate-intensity
tags:
- waves
- velocity
- calculus
stage: advanced
status: validated
---

# Particle Velocity in Wave Motion

## Core Idea
As a wave passes through a medium, individual particles oscillate perpendicular to (transverse waves) or along (longitudinal waves) the direction of wave propagation. Particle velocity (v_particle = ∂u/∂t) is distinct from and usually much less than wave speed (v_wave). The phase difference between particle displacement and velocity is 90°.

## Common Misconceptions
Particles in a wave do not propagate along with the wave—they remain near their equilibrium position while the wave pattern travels past them.

## Questions

```yaml
- question: "A transverse wave travels through a medium at 500 m/s. A particle in the medium is at its equilibrium position (zero displacement) as the wave passes. What can you conclude about the particle's speed at this moment?"
  type: multiple-choice
  options:
    - "The particle is also moving at approximately 500 m/s, matching the wave speed"
    - "The particle's speed is at its maximum value of Aω, since it is at the equilibrium position"
    - "The particle's speed is zero, since the wave has just reached it"
    - "The particle's speed equals the wave speed divided by the amplitude"
  answer: 1
  explanation: "Particle velocity is v = -Aω cos(kx - ωt). At zero displacement, sin(kx - ωt) = 0, which means cos(kx - ωt) = ±1, so particle speed is at its maximum |Aω|. Wave speed (ω/k) is an entirely separate quantity describing how fast the pattern moves through the medium — determined by medium properties, not by the particle's oscillation phase. The two speeds have different causes and different formulas."

- question: "A wave passes through a medium and a particle is observed to be at its maximum displacement from equilibrium (a crest). What is the particle's velocity at this instant?"
  type: multiple-choice
  options:
    - "Maximum, since the wave is pushing it hardest at the crest"
    - "Equal to the wave speed — the particle rides the crest"
    - "Zero, since the particle is momentarily at its turning point"
    - "Aω, the maximum particle speed"
  answer: 2
  explanation: "At maximum displacement (crest or trough), the particle is at its turning point — like a ball thrown upward at its peak, momentarily at rest before reversing. From v = -Aω cos(kx - ωt): when displacement is maximum, sin(kx - ωt) = ±1, which forces cos(kx - ωt) = 0, giving zero velocity. The 90° phase difference between displacement and velocity is the key relationship: maximum displacement coincides with zero speed, and zero displacement coincides with maximum speed."

- question: "A particle in a medium that carries a wave must be moving whenever the wave is moving."
  type: true-false
  answer: false
  explanation: "At maximum displacement (a crest or trough), a particle is momentarily at rest even as the wave pattern continues traveling. The particle's velocity is governed by its phase in the oscillation cycle, not by whether the wave is propagating. This is the fundamental distinction: wave propagation does not require particles to be in constant motion — at any given instant, particles at the crests and troughs are stationary while those at equilibrium positions are moving fastest."

- question: "A wave can have rapidly oscillating particles even if the wave itself propagates slowly through the medium."
  type: true-false
  answer: true
  explanation: "Maximum particle velocity = Aω, which depends on amplitude and frequency — not on wave speed. Wave speed v_wave = ω/k depends on the medium's physical properties (tension, density, etc.). These are independent quantities. A slow-propagating wave with large amplitude or high frequency will have fast-moving particles. Conversely, seismic waves can travel thousands of meters per second while particles oscillate with tiny velocities. The cork bobs up and down; the pattern travels to shore."

- question: "Explain why particle velocity and wave speed are fundamentally different quantities, and what determines each."
  type: short-answer
  answer: "Particle velocity (v_particle = ∂u/∂t) describes how fast an individual piece of the medium oscillates about its equilibrium position; its maximum is Aω (amplitude × angular frequency). Wave speed (v_wave = ω/k) describes how fast the wave pattern — the crests and troughs — moves through the medium; it is determined by the medium's physical properties (e.g., tension and linear density for a string). A cork on water illustrates the difference: the cork bobs up and down (particle velocity) while the wave pattern travels toward shore (wave speed). The cork does not travel to shore; only the pattern does."
  explanation: "The distinction matters for energy calculations: wave intensity is proportional to (particle velocity)² × (density × wave speed), so both quantities appear together. Getting them confused leads to errors in predicting how much energy a wave carries. It also resolves the apparent paradox of how energy can flow through a medium without any net transport of matter — the pattern moves, but the matter stays near its equilibrium position."
```

## Explainer

Your prerequisite — harmonic wave time dependence — gave you the displacement function u(x, t) = A sin(kx − ωt). This equation tells you where a particle at position x is displaced at time t. But it answers a static question: where is the particle? The more dynamically interesting question is: how fast is it moving? That's what **particle velocity** captures, and it is obtained simply by differentiating the displacement with respect to time: v_particle = ∂u/∂t = −Aω cos(kx − ωt).

Notice that the particle velocity is another sinusoidal function of the same frequency, but it is shifted 90° in phase relative to the displacement. When the particle is at its maximum displacement (the crest of a wave), its velocity is zero — it is momentarily at rest, about to reverse direction. When the particle passes through its equilibrium position (zero displacement), its velocity is at maximum magnitude ±Aω. This 90° relationship is identical to the behavior of a mass on a spring, which you may have encountered in oscillation problems: maximum displacement coincides with zero speed, and maximum speed coincides with zero displacement.

The most important conceptual distinction here is between **particle velocity** and **wave speed**. Wave speed v_wave = ω/k describes how fast the pattern (the crest, the trough, the zero-crossing) moves through space. It depends on the medium's properties. Particle velocity describes how fast an individual piece of the medium is bobbing up and down (or back and forth). These two speeds are entirely different quantities with entirely different causes. A cork floating on the surface of water bobs up and down as waves pass — the cork's velocity is the particle velocity; the speed of the wave pattern moving toward the shore is the wave speed. The cork does not travel to shore; the pattern does.

The maximum particle velocity is Aω — the product of amplitude and angular frequency. This means a wave with large amplitude or high frequency will have fast-moving particles even if the wave itself propagates slowly. Conversely, a wave can travel at thousands of meters per second while its particles oscillate only microns per second. This is the case for low-amplitude seismic waves. Understanding this distinction is essential for the next topic of energy flow and intensity, where both v_particle and v_wave appear together: intensity (power per unit area) turns out to be proportional to (v_particle)² × (density × v_wave), making the two concepts inseparable in calculating how much energy a wave carries.

