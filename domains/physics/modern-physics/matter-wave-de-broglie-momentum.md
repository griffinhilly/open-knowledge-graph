---
id: matter-wave-de-broglie-momentum
title: Matter Waves and de Broglie Wavelength
domain: physics
course: modern-physics
prerequisites:
- id: photon-concept-quanta
  type: hard
- id: momentum-and-impulse
  type: hard
builds-toward:
- electron-diffraction-matter
tags:
- quantum
- matter-waves
- duality
stage: advanced
status: draft
---

# Matter Waves and de Broglie Wavelength

## Core Idea
All particles, including electrons and atoms, possess an associated wavelength λ = h/p. This de Broglie wavelength decreases as momentum increases. Matter waves are not classical mechanical waves but rather a manifestation of quantum superposition; the wavelength relates to the uncertainty in a particle's position through the uncertainty principle.

## Explainer

You know from the photon concept that light carries both energy E = hf and momentum p = h/λ — quantized packets that behave like particles under some conditions and like waves under others. De Broglie's bold generalization runs this relationship in the opposite direction: if light with wavelength λ has momentum p = h/λ, then by symmetry, any matter with momentum p should have an associated wavelength λ = h/p. The same Planck constant h that quantizes light also governs the wave character of electrons, protons, atoms — all material particles.

The formula λ = h/p = h/mv makes an immediate, testable prediction about where wave behavior will be observable. An electron moving at a few percent of the speed of light has a de Broglie wavelength on the order of 0.1 nm — comparable to the spacing between atoms in a crystal lattice. This is in the X-ray range, and just as X-rays diffract from crystal planes, so should electrons with this wavelength. A baseball, by contrast, has a mass of 0.15 kg and a typical speed of 40 m/s, giving λ ≈ 10^(−34) m — roughly 20 orders of magnitude smaller than an atomic nucleus. Its wave character is utterly undetectable by any physical measurement. The larger the momentum, the shorter the wavelength, and the less observable the wave behavior.

The phrase "matter wave" must be interpreted carefully. The de Broglie wavelength is not a sound wave or a pressure wave — it is the spatial period of the quantum **wavefunction** ψ(x). For a particle with definite momentum p, the wavefunction is a plane wave ψ ∝ e^{ipx/ℏ} oscillating with wavelength h/p spread uniformly throughout space. Since |ψ|² gives the probability density for finding the particle, a plane wave corresponds to completely indefinite position — the particle is equally likely to be anywhere. This is the uncertainty principle in action: definite momentum (Δp = 0) implies infinite positional uncertainty (Δx → ∞), and ΔxΔp ≥ ℏ/2 is satisfied with equality for a pure plane wave.

The experimental confirmation came from the Davisson-Germer experiment, where electrons scattered from a crystal lattice produced diffraction maxima at precisely the angles predicted by Bragg's law using λ = h/p. This was a decisive test: only a wave phenomenon can produce diffraction, yet the electrons were unambiguously particles arriving one at a time at the detector. Today, neutron diffraction uses the same principle to determine protein structures, and atom interferometry uses matter waves to measure gravitational acceleration and fundamental constants with extraordinary precision. The de Broglie relation λ = h/p is the entry point into the full quantum mechanical framework: it is the first clue that the language of physics at small scales is not position and velocity, but wavefunctions and probability amplitudes.
