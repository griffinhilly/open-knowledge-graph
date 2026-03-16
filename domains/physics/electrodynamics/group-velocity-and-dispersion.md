---
id: group-velocity-and-dispersion
title: Group Velocity and Dispersion Relations
domain: physics
course: electrodynamics
prerequisites:
- id: dispersion-relations-em-waves
  type: hard
- id: electromagnetic-waves
  type: hard
builds-toward:
- evanescent-waves-total-reflection
tags:
- group-velocity
- phase-velocity
- dispersion
- wave-packets
stage: advanced
status: draft
---

# Group Velocity and Dispersion Relations

## Core Idea
The group velocity vg = dω/dk describes wave packet motion while phase velocity vp = ω/k describes individual wavefront motion. Dispersion (vg ≠ vp) causes wave packets to spread. When dω/dk is imaginary, waves are evanescent rather than propagating.

## Explainer

From your study of electromagnetic waves and dispersion relations, you know that a medium's dispersion relation ω(k) connects a wave's frequency to its wavenumber. For light in vacuum, ω = ck — a perfectly linear relationship — so all frequencies travel at the same speed c. But in any real medium, the relationship is more complicated, and different frequency components travel at different speeds. This **dispersion** is what a prism exploits: red and violet light travel at slightly different speeds in glass, bending by different angles and separating into a rainbow.

The two velocity concepts arise naturally when you think about a **wave packet** — a spatially localized group of waves, like a radar pulse or a light pulse in a fiber. Such a packet is built by superposing many sinusoidal waves with slightly different frequencies and wavenumbers. Two superposed waves of nearly equal frequency ω₁, ω₂ and wavenumber k₁, k₂ produce a beat pattern: a fast carrier oscillation modulated by a slow envelope. The carrier travels at the **phase velocity** vₚ = ω/k, which describes how quickly the individual wave crests move. The envelope — the actual "bump" of the pulse, the part carrying the energy and information — travels at the **group velocity** vg = dω/dk, the slope of the dispersion curve. In a non-dispersive medium like vacuum, vg = vₚ = c; in a dispersive medium, they differ.

Dispersion causes two distinct effects. First, if vg ≠ vₚ, the carrier oscillations slide through the envelope as the packet travels — the "wiggles" move at a different speed than the "bump." This is observable in water waves, where ripples travel faster than the wave group. Second, and more practically important, **pulse spreading** occurs: different frequency components of the packet travel at slightly different speeds, so they drift apart over time and the pulse broadens. This limits data rates in fiber-optic cables, since overlapping pulses become indistinguishable — the fundamental reason why fiber dispersion must be carefully managed in long-haul communications.

**Evanescent waves** arise when the dispersion relation yields an imaginary wavenumber k at a given frequency — meaning the wave cannot propagate and instead decays exponentially. This happens below the cutoff frequency of a waveguide: the mode mathematically "exists" but its amplitude dies away within a skin depth rather than oscillating. The group velocity formula dω/dk becomes imaginary, signaling no energy transport. This is physically consistent: no propagating mode means no energy flow. Understanding evanescent waves is essential for analyzing total internal reflection, waveguide cutoff, and quantum mechanical tunneling, where the same exponentially-decaying solution appears in classically forbidden regions.
