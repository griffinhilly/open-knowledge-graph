---
id: scattering-theory-intro
title: Introduction to Scattering Theory
domain: physics
course: quantum-mechanics
prerequisites:
- id: hydrogen-atom-solution
  type: hard
builds-toward:
- born-approximation
- partial-wave-analysis
tags:
- scattering
- cross-sections
stage: advanced
status: draft
---

# Introduction to Scattering Theory

## Core Idea
Scattering theory describes how quantum particles interact with localized potentials. An incoming plane wave scatters into outgoing spherical waves. Scattering amplitude f(θ, φ) encodes angular distribution; dσ/dΩ = |f|².

## Explainer

From your study of the hydrogen atom, you solved the Schrödinger equation for bound states — states with negative energy, where the electron stays near the proton. Scattering theory addresses the complementary situation: positive-energy states where a particle arrives from far away, interacts with a potential, and flies off in some direction. These **unbound states** cannot be normalized in the usual sense (they extend to infinity), but they are physically real and experimentally essential — every particle accelerator experiment is a scattering measurement.

The standard setup is an incident **plane wave** ψ_inc = e^{ikz}, representing a particle moving in the z-direction with definite momentum ℏk. After encountering the localized potential V(r), the total wavefunction asymptotically takes the form ψ ≈ e^{ikz} + f(θ,φ) e^{ikr}/r. The first term is the unscattered wave continuing forward; the second is the scattered **spherical wave**, whose amplitude decreases as 1/r. The 1/r falloff is mandatory: probability must be distributed over an expanding spherical surface of area 4πr², so the probability density |ψ|² ∝ 1/r², requiring |ψ_amplitude| ∝ 1/r. The **scattering amplitude** f(θ,φ) encodes all the physics of the interaction in the far field.

The connection to experiment is through the **differential cross section** dσ/dΩ = |f(θ,φ)|². Think of it geometrically: a detector subtending solid angle dΩ at angle (θ,φ) catches a fraction of the scattered beam. The differential cross section is the effective target area that would scatter that fraction if the beam were perfectly uniform. It has units of area (barns, fm², etc.) and is directly measurable by counting particles at each angle. The **total cross section** σ = ∫|f|² dΩ is the total effective area, relating the incident beam flux to the total scattering rate.

The remarkable fact is that f(θ,φ) — a single complex function of two angles — completely determines all scattering observables. Different potentials V(r) produce different scattering amplitudes, and measuring the angular distribution of scattered particles is the primary experimental tool for learning about the potential. This is how Rutherford deduced the nuclear charge distribution, how electron scattering revealed the proton's internal quark structure, and how modern accelerator experiments probe the fundamental interactions at small scales.
