---
id: energy-analysis-oscillations
title: Energy Analysis in Oscillating Systems
domain: physics
course: classical-mechanics
prerequisites:
- id: simple-harmonic-motion
  type: hard
- id: conservation-of-energy
  type: hard
builds-toward:
- coupled-oscillator-equations
- driven-harmonic-oscillator
tags:
- oscillations
- energy
- harmonics
stage: formal-systems
status: draft
---

# Energy Analysis in Oscillating Systems

## Core Idea
In simple harmonic motion, kinetic and potential energy continuously exchange, with total energy E = ½mω²A² constant. The energy oscillates between kinetic and potential at twice the frequency of displacement.

## How It's Best Learned
Plot kinetic, potential, and total energy vs. time and position. Verify that maximum kinetic energy equals maximum potential energy. Relate amplitude to total energy.

## Explainer

You already know **simple harmonic motion**: a restoring force proportional to displacement (F = −kx) produces sinusoidal oscillations described by x(t) = A cos(ωt + φ), with angular frequency ω = √(k/m) and period T = 2π/ω. You also know **conservation of energy**: in the absence of non-conservative forces, the total mechanical energy of a system is constant. Energy analysis in oscillating systems is what you get when you apply conservation of energy to the specific case of SHM — and the result reveals the oscillation from a completely different angle.

Start with the two forms of energy in a spring-mass system. **Kinetic energy** is KE = ½mv², which is largest when the mass moves fastest. **Potential energy** (elastic potential energy stored in the spring) is PE = ½kx², which is largest when the spring is most compressed or stretched. Now use conservation of energy: KE + PE = E (constant). Substituting x(t) = A cos(ωt) gives PE = ½k A² cos²(ωt) and, since v = −Aω sin(ωt), KE = ½mA²ω² sin²(ωt). Because ω² = k/m, both terms simplify to ½kA² times a squared trig function, and sin²(ωt) + cos²(ωt) = 1 ensures the total is always **E = ½kA²**. Total energy depends only on the amplitude — double the amplitude, quadruple the energy.

The exchange between kinetic and potential energy is continuous and perfectly timed. At the **turning points** (x = ±A), the mass is momentarily at rest: all energy is potential (PE = ½kA², KE = 0). At the **equilibrium position** (x = 0), the spring is relaxed: all energy is kinetic (KE = ½kA² = ½mv²_max, PE = 0). This means the maximum speed v_max = Aω — larger amplitude or higher frequency gives greater maximum speed. Between these extremes, energy sloshes back and forth between kinetic and potential, always summing to E = ½kA².

Notice that while displacement oscillates at frequency ω (one full cycle per period T), the energy functions oscillate at **twice the frequency** — sin²(ωt) and cos²(ωt) each complete two full cycles per period T, because squaring doubles the frequency. This means energy is at maximum twice per oscillation cycle: kinetic energy peaks when the mass passes through equilibrium going in either direction, and potential energy peaks at both turning points. This factor-of-two relationship between displacement frequency and energy frequency is a precise mathematical result worth internalizing.

Finally, connect this to **amplitude as the energy parameter**. When friction or damping is present, energy is gradually removed from the system, and amplitude decreases. The amplitude decay directly tracks the energy loss: since E ∝ A², a 50% reduction in energy corresponds to a 29% reduction in amplitude (since 0.71² ≈ 0.5). This relationship between amplitude and energy is essential for analyzing damped oscillators, resonance, and driven systems in the topics that build on this one.


