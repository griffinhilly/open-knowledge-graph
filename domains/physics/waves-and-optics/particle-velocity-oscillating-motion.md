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
status: draft
---

# Particle Velocity in Wave Motion

## Core Idea
As a wave passes through a medium, individual particles oscillate perpendicular to (transverse waves) or along (longitudinal waves) the direction of wave propagation. Particle velocity (v_particle = ∂u/∂t) is distinct from and usually much less than wave speed (v_wave). The phase difference between particle displacement and velocity is 90°.

## Common Misconceptions
Particles in a wave do not propagate along with the wave—they remain near their equilibrium position while the wave pattern travels past them.

## Explainer

Your prerequisite — harmonic wave time dependence — gave you the displacement function u(x, t) = A sin(kx − ωt). This equation tells you where a particle at position x is displaced at time t. But it answers a static question: where is the particle? The more dynamically interesting question is: how fast is it moving? That's what **particle velocity** captures, and it is obtained simply by differentiating the displacement with respect to time: v_particle = ∂u/∂t = −Aω cos(kx − ωt).

Notice that the particle velocity is another sinusoidal function of the same frequency, but it is shifted 90° in phase relative to the displacement. When the particle is at its maximum displacement (the crest of a wave), its velocity is zero — it is momentarily at rest, about to reverse direction. When the particle passes through its equilibrium position (zero displacement), its velocity is at maximum magnitude ±Aω. This 90° relationship is identical to the behavior of a mass on a spring, which you may have encountered in oscillation problems: maximum displacement coincides with zero speed, and maximum speed coincides with zero displacement.

The most important conceptual distinction here is between **particle velocity** and **wave speed**. Wave speed v_wave = ω/k describes how fast the pattern (the crest, the trough, the zero-crossing) moves through space. It depends on the medium's properties. Particle velocity describes how fast an individual piece of the medium is bobbing up and down (or back and forth). These two speeds are entirely different quantities with entirely different causes. A cork floating on the surface of water bobs up and down as waves pass — the cork's velocity is the particle velocity; the speed of the wave pattern moving toward the shore is the wave speed. The cork does not travel to shore; the pattern does.

The maximum particle velocity is Aω — the product of amplitude and angular frequency. This means a wave with large amplitude or high frequency will have fast-moving particles even if the wave itself propagates slowly. Conversely, a wave can travel at thousands of meters per second while its particles oscillate only microns per second. This is the case for low-amplitude seismic waves. Understanding this distinction is essential for the next topic of energy flow and intensity, where both v_particle and v_wave appear together: intensity (power per unit area) turns out to be proportional to (v_particle)² × (density × v_wave), making the two concepts inseparable in calculating how much energy a wave carries.

