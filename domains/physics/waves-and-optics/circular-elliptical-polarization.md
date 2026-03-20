---
id: circular-elliptical-polarization
title: 'Polarization States: Linear, Circular, and Elliptical'
domain: physics
course: waves-and-optics
prerequisites:
- id: electromagnetic-wave-polarization
  type: soft
- id: phase-of-oscillation-initial
  type: hard
tags:
- polarization
- waves
stage: advanced
status: draft
---

# Polarization States: Linear, Circular, and Elliptical

## Core Idea
Polarization describes the orientation of the electric field oscillation. Linear polarization confines the field to a single direction. Circular polarization occurs when two perpendicular components have equal amplitude and 90° phase difference; the field vector rotates as the wave travels. Elliptical polarization is the general case with unequal amplitudes or non-90° phase differences. Malus's law governs transmission through polarizers.

## Explainer

Think of a transverse wave as a rope being shaken — the rope can oscillate up-down, left-right, or anywhere in between. Light is an electromagnetic wave with an oscillating electric field, and **polarization** describes the direction that field oscillates as the wave travels. When you already understand phase of oscillation, you have the key tool for distinguishing all three polarization states: what makes them different is the phase relationship and amplitude balance between two perpendicular field components.

**Linear polarization** is the simplest case: the electric field oscillates along a single fixed direction — say, always vertical. Mathematically, this is one non-zero field component and zero in the perpendicular direction. A polarizing filter produces this by blocking all field orientations except one, transmitting only the component aligned with the filter's **transmission axis**. When unpolarized light (with electric field pointing in all transverse directions randomly) hits a polarizer, roughly half the intensity passes through — the half that happened to be aligned.

**Circular polarization** arises when you combine two perpendicular components of *equal amplitude* and exactly 90° phase difference. Imagine a vertical component E_y = A sin(kx - ωt) and a horizontal component E_z = A sin(kx - ωt + 90°) = A cos(kx - ωt). At any instant, the combined tip of the electric field vector traces a circle as the wave travels forward — the field doesn't flicker back and forth, it spins. The sign of the phase shift determines whether it's left-handed or right-handed circular polarization, a distinction that matters in optics and chemistry alike.

**Elliptical polarization** is the general case. When the two perpendicular components have *unequal* amplitudes, or a phase difference that isn't exactly 90°, the field vector traces an ellipse rather than a perfect circle or a line. Linear and circular polarization are limiting cases: a degenerate ellipse (flat line) and a perfectly round ellipse respectively. Most light emerging from crystals or optical waveplates is elliptically polarized.

**Malus's law** governs what happens when linearly polarized light passes through a second polarizer tilted at angle θ to the polarization direction: I = I₀cos²θ. At θ = 0° all intensity passes; at θ = 90° (crossed polarizers) none does. This squared cosine comes directly from the projection of the electric field vector onto the polarizer axis — intensity is proportional to amplitude squared, and the projected amplitude is the full amplitude times cos θ.
