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
stage: advanced
status: draft
---

# Dispersion Relations and Group Velocity

## Core Idea
The dispersion relation ω(k) describes frequency-wave vector dependence. Phase velocity v_p = ω/k is the speed of crests; group velocity v_g = dω/dk is the energy and packet speed. In vacuum, v_p = v_g = c. In dispersive media, v_p ≠ v_g; dispersion causes packet broadening.

## Explainer

You already know that electromagnetic waves in vacuum satisfy ω = ck — a perfectly linear relationship between angular frequency and wave number. This linearity has an important consequence: every Fourier component travels at exactly the same speed c, so a wave packet (a superposition of many frequencies) keeps its shape as it propagates. A light pulse in vacuum arrives as a sharp pulse. But in a medium, you've seen that the refractive index n = c/v_p varies with frequency — this is why a prism splits white light into colors. That variation is exactly what **dispersion** means, and the **dispersion relation** ω(k) is the function that encodes it.

The **phase velocity** v_p = ω/k is the speed at which a single-frequency crest moves. If you watched a monochromatic wave and tracked one peak, v_p is its speed. But physical signals are never truly monochromatic — they are wave packets built from a spread of frequencies. The speed of the packet's *envelope* — the speed at which the peak of the pulse moves, and the speed at which energy and information travel — is the **group velocity** v_g = dω/dk. This is the derivative of the dispersion relation, not the ratio ω/k. In vacuum, ω = ck gives v_p = v_g = c. In a dispersive medium, the two speeds differ.

A concrete analogy: imagine a group of runners on a track, each moving at a slightly different speed. The individual runners are like Fourier components; the cluster is like the wave packet. The "group" moves at the average velocity of the cluster, not the speed of any one runner. In a dispersive medium, the faster components run ahead and the slower ones fall behind — the cluster spreads out. This is **group velocity dispersion**, and it is the fundamental reason why short light pulses broaden as they travel through glass fibers. Optical fiber engineers must compensate for this broadening to maintain signal quality over long distances.

The dispersion relation ω(k) is the master equation of wave physics in any medium. For electromagnetic waves in a plasma, ω² = ω_p² + c²k² (where ω_p is the plasma frequency) — a nonlinear relationship that means v_p and v_g are both functions of frequency, and v_p · v_g = c². Waves below the plasma frequency don't propagate at all (k becomes imaginary). For waveguides, similarly, there is a cutoff frequency below which no propagation occurs. Reading the dispersion relation tells you immediately whether a wave propagates, at what speeds, and how packets distort — making it one of the most information-dense tools in wave physics.
