---
id: dispersion-relations
title: Dispersion Relations and Group Velocity
domain: physics
course: electrodynamics
prerequisites:
- id: electromagnetic-waves-in-media
  type: hard
- id: plane-waves-in-vacuum
  type: soft
builds-toward:
- waveguides-transmission-lines
tags:
- dispersion
- group-velocity
- phase-velocity
stage: expert
status: validated
---

# Dispersion Relations and Group Velocity

## Core Idea
The dispersion relation ω(k) describes frequency-wave vector dependence. Phase velocity v_p = ω/k is the speed of crests; group velocity v_g = dω/dk is the energy and packet speed. In vacuum, v_p = v_g = c. In dispersive media, v_p ≠ v_g; dispersion causes packet broadening.

## Questions

```yaml
- question: "In a plasma, the dispersion relation is ω² = ω_p² + c²k². A physicist wants to send a signal using a wave packet centered at frequency ω₀ > ω_p. Which quantity gives the speed at which the signal (the packet envelope) travels?"
  type: multiple-choice
  options:
    - "Phase velocity v_p = ω₀/k, because signals travel with the wave crests"
    - "Group velocity v_g = dω/dk evaluated at k₀, because the packet envelope moves at this speed"
    - "The speed of light c, because signals always travel at c in electromagnetic media"
    - "Zero, because the plasma frequency prevents propagation"
  answer: 1
  explanation: "The group velocity v_g = dω/dk is the speed of the envelope — the speed at which energy and information travel. For the plasma dispersion relation, v_g = c²k/ω, which is less than c. The phase velocity v_p = ω/k = ω/(√(ω² − ω_p²)/c) is actually greater than c in a plasma, which is precisely why it cannot carry information. Option C is wrong: c is only the limit; signals in a dispersive medium travel at v_g ≠ c. Option D is wrong because ω > ω_p means k is real and propagation occurs."

- question: "Two physicists disagree. Physicist A says 'phase velocity in this medium exceeds c, so signals here travel faster than light, violating relativity.' Physicist B says 'no violation occurs.' What is Physicist B's correct response?"
  type: multiple-choice
  options:
    - "Physicist B is wrong; any superluminal speed does violate relativity"
    - "Phase velocity is the speed of crests of a monochromatic wave, which carries no information; signals travel at the group velocity, which remains ≤ c"
    - "Phase velocity and group velocity are always equal, so if one exceeds c, both do"
    - "Relativity only applies to massive particles, not electromagnetic waves"
  answer: 1
  explanation: "Phase velocity v_p = ω/k can exceed c in a dispersive medium (e.g., in a plasma or waveguide) without violating relativity. A pure monochromatic wave — a single frequency extending infinitely in space and time — cannot encode a signal or carry information, since it contains no variation. Information requires a modulation, which is a wave packet; the packet travels at the group velocity v_g = dω/dk, which in causal media is ≤ c. This is the key distinction: phase velocity is a kinematic feature of crest motion, not information transport."

- question: "A short laser pulse traveling through a vacuum will broaden over distance because different frequency components of the pulse travel at slightly different speeds."
  type: true-false
  answer: false
  explanation: "In vacuum, ω = ck — a perfectly linear dispersion relation with constant slope. Every Fourier component of the pulse travels at exactly c regardless of frequency. Since v_g = dω/dk = c = v_p for all k, there is no differential spreading. Pulse broadening (group velocity dispersion) occurs only in dispersive media where d²ω/dk² ≠ 0. This is exactly why optical fibers — which are dispersive — must be engineered to manage pulse broadening, while free-space propagation requires no such compensation."

- question: "The group velocity v_g = dω/dk is the physically meaningful speed for energy transport in a dispersive medium, while the phase velocity v_p = ω/k describes the motion of wavefronts of constant phase."
  type: true-false
  answer: true
  explanation: "This is the central distinction of dispersion theory. Phase velocity tracks a crest — a surface of constant phase — and can exceed c without violating causality because crests carry no information. Group velocity tracks the envelope of a wave packet, which is where the amplitude (and thus the energy and signal) is concentrated. In a non-dispersive medium (ω ∝ k), these are equal. In a dispersive medium, they differ, and only v_g bounds the speed of information."

- question: "Explain why a short light pulse broadens as it travels through glass, but not through vacuum, using the concept of group velocity dispersion."
  type: short-answer
  answer: "A short pulse contains a spread of frequencies (by the Fourier uncertainty principle, the shorter the pulse, the wider its frequency bandwidth). In vacuum, all frequency components travel at the same speed c (the dispersion relation is linear: ω = ck), so the pulse maintains its shape. In glass, the refractive index varies with frequency — the dispersion relation is nonlinear — meaning different Fourier components have different group velocities. Higher-frequency components may travel faster or slower than lower-frequency ones. Over distance, this differential speed causes the components to arrive at different times, spreading the pulse temporally."
  explanation: "The key concept is d²ω/dk² ≠ 0 (non-zero group velocity dispersion). In vacuum, d²ω/dk² = 0 exactly, so all components propagate identically. In glass, this second derivative is nonzero, quantifying how much v_g changes across the pulse's bandwidth. This broadening limits the bit rate in fiber optic communication — compressed pulses from adjacent data bits overlap — and is why dispersion-compensating fibers and chirped pulse amplification are essential technologies."
```

## Explainer

You already know that electromagnetic waves in vacuum satisfy ω = ck — a perfectly linear relationship between angular frequency and wave number. This linearity has an important consequence: every Fourier component travels at exactly the same speed c, so a wave packet (a superposition of many frequencies) keeps its shape as it propagates. A light pulse in vacuum arrives as a sharp pulse. But in a medium, you've seen that the refractive index n = c/v_p varies with frequency — this is why a prism splits white light into colors. That variation is exactly what **dispersion** means, and the **dispersion relation** ω(k) is the function that encodes it.

The **phase velocity** v_p = ω/k is the speed at which a single-frequency crest moves. If you watched a monochromatic wave and tracked one peak, v_p is its speed. But physical signals are never truly monochromatic — they are wave packets built from a spread of frequencies. The speed of the packet's *envelope* — the speed at which the peak of the pulse moves, and the speed at which energy and information travel — is the **group velocity** v_g = dω/dk. This is the derivative of the dispersion relation, not the ratio ω/k. In vacuum, ω = ck gives v_p = v_g = c. In a dispersive medium, the two speeds differ.

A concrete analogy: imagine a group of runners on a track, each moving at a slightly different speed. The individual runners are like Fourier components; the cluster is like the wave packet. The "group" moves at the average velocity of the cluster, not the speed of any one runner. In a dispersive medium, the faster components run ahead and the slower ones fall behind — the cluster spreads out. This is **group velocity dispersion**, and it is the fundamental reason why short light pulses broaden as they travel through glass fibers. Optical fiber engineers must compensate for this broadening to maintain signal quality over long distances.

The dispersion relation ω(k) is the master equation of wave physics in any medium. For electromagnetic waves in a plasma, ω² = ω_p² + c²k² (where ω_p is the plasma frequency) — a nonlinear relationship that means v_p and v_g are both functions of frequency, and v_p · v_g = c². Waves below the plasma frequency don't propagate at all (k becomes imaginary). For waveguides, similarly, there is a cutoff frequency below which no propagation occurs. Reading the dispersion relation tells you immediately whether a wave propagates, at what speeds, and how packets distort — making it one of the most information-dense tools in wave physics.
