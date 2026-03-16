---
id: electron-diffraction-matter-wavelength
title: Electron Diffraction and Matter Wave Properties
domain: physics
course: modern-physics
prerequisites:
- id: de-broglie-wavelength
  type: hard
- id: wave-particle-duality
  type: hard
builds-toward:
- davisson-germer-crystal-diffraction
tags:
- wave-particle-duality
- quantum-mechanics
- experimental
stage: advanced
status: draft
---

# Electron Diffraction and Matter Wave Properties

## Core Idea
Electrons, like photons, exhibit wave behavior with wavelength λ = h/p. When electrons pass through a small slit or reflect from a crystal, they produce diffraction patterns identical in form to those of waves with the same wavelength. This demonstrates the wave nature of matter predicted by de Broglie.

## How It's Best Learned
Calculate the de Broglie wavelength for electrons accelerated through various voltages. Compare predicted diffraction patterns with experimental observations using crystals or double slits. Use single-slit diffraction to measure the electron wavelength.

## Common Misconceptions
Electrons are not sometimes particles and sometimes waves—they have both properties (complementarity). The wavelength depends on momentum, so slower electrons have longer wavelengths and diffract more.

## Explainer

De Broglie's hypothesis assigned a wavelength λ = h/p to any particle with momentum p. But a hypothesis is not confirmed until experiment tests it. The key question was: do electrons actually diffract the way waves do? If the de Broglie wavelength is real and physically meaningful, then electrons passing through an appropriate aperture or reflecting from an appropriate periodic structure should produce interference fringes — the unmistakable fingerprint of wave behavior.

The experiment that confirmed this was performed by **Clinton Davisson and Lester Germer** in 1927 (and independently by George Thomson). They directed a beam of electrons at a nickel crystal and observed that the reflected electrons arrived preferentially at specific angles — exactly the angles predicted by the Bragg diffraction condition nλ = 2d sin θ, using the de Broglie wavelength λ = h/p for the electron momentum. The crystal lattice spacing d (~0.2 nm for nickel) is comparable to the de Broglie wavelength of electrons accelerated through tens of volts (λ ~ 0.1–0.3 nm), making crystals ideal diffraction gratings for electron waves. The agreement between predicted and observed diffraction angles was quantitative and decisive.

The setup for understanding these experiments connects directly to what you know about waves: when a wave encounters a periodic structure with spacing d, constructive interference occurs at angles where the path length difference between waves from successive planes is an integer multiple of the wavelength. For electrons accelerated through voltage V, the kinetic energy is eV = p²/2m, so p = √(2meV) and λ = h/√(2meV). This lets you predict exactly where diffraction peaks should appear — and experiments confirm these predictions. Crucially, you can adjust λ by changing the accelerating voltage: lower voltage → lower momentum → longer wavelength → more spread-out diffraction pattern.

The deeper lesson is about **complementarity**: electrons do not choose to be particles in some experiments and waves in others. They always have both properties. Whether wave-like or particle-like behavior is manifest depends on the experimental arrangement. In the Davisson-Germer experiment, the periodic crystal structure creates conditions where interference is observable, and wave behavior dominates the measurement. If you instead measure which crystal plane each electron bounced from (a "which-path" measurement), the diffraction pattern disappears. Electron diffraction was the experimental proof that the de Broglie relation is not an analogy or a metaphor — matter genuinely has a wave nature, and quantum mechanics must account for it.
