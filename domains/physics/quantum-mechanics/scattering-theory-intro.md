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
status: validated
---

# Introduction to Scattering Theory

## Core Idea
Scattering theory describes how quantum particles interact with localized potentials. An incoming plane wave scatters into outgoing spherical waves. Scattering amplitude f(θ, φ) encodes angular distribution; dσ/dΩ = |f|².

## Questions

```yaml
- question: "A particle scatters off a potential and the measured angular distribution shows strong forward scattering. What does this tell you about the scattering amplitude f(θ,φ)?"
  type: multiple-choice
  options:
    - "f(θ,φ) is large for small θ, because dσ/dΩ = |f|² and the differential cross section is large near θ = 0"
    - "f(θ,φ) is small for small θ, because forward scattering means particles are not deflected"
    - "The total cross section σ must be small, since most particles pass straight through"
    - "The scattering amplitude cannot be determined from the angular distribution alone"
  answer: 0
  explanation: "The differential cross section dσ/dΩ = |f(θ,φ)|² directly connects what is measured (the angular distribution of scattered particles) to the scattering amplitude. Strong forward scattering means dσ/dΩ is large at small θ, which means |f|² is large there, so |f| itself is large. The total cross section σ = ∫|f|²dΩ could still be large or small depending on the full angular dependence — forward-peaked scattering often comes with a large total cross section."

- question: "In the asymptotic wavefunction ψ ≈ e^{ikz} + f(θ,φ)e^{ikr}/r, a student argues the scattered amplitude should fall as 1/r² to match how intensity decreases with distance from a point source. Evaluate this reasoning."
  type: multiple-choice
  options:
    - "Correct — both the amplitude and intensity should decrease as 1/r²"
    - "Incorrect — the amplitude must fall as 1/r so that the probability density |ψ|² ∝ 1/r², conserving total probability flux through an expanding spherical shell"
    - "Incorrect — the amplitude falls as 1/r² and the intensity falls as 1/r⁴, which is steeper than a classical point source"
    - "Correct in reasoning but wrong conclusion — the 1/r dependence comes from angular momentum conservation, not probability conservation"
  answer: 1
  explanation: "Probability flux must be conserved: the total number of particles crossing a sphere of radius r per unit time must be independent of r. The area of a sphere grows as r², so the probability density |ψ|² must fall as 1/r², which requires the amplitude to fall as 1/r. If the amplitude fell as 1/r², the probability density would fall as 1/r⁴, and the total flux through a large sphere would shrink to zero — a violation of probability conservation."

- question: "The scattering amplitude f(θ,φ) has dimensions of length."
  type: true-false
  answer: true
  explanation: "The differential cross section dσ/dΩ = |f(θ,φ)|² must have units of area per steradian. Since steradians are dimensionless, dσ/dΩ has units of area (e.g., m², barn). Therefore |f|² has units of area and f itself has units of length. This dimensional analysis also explains why the Born approximation, which integrates the potential over a volume, produces a result with the right dimensions for f."

- question: "Measuring the complete angular distribution |f(θ,φ)|² at a fixed energy fully determines the scattering amplitude f(θ,φ), including its phase."
  type: true-false
  answer: false
  explanation: "The angular distribution measurement gives dσ/dΩ = |f(θ,φ)|², which reveals only the magnitude |f| at each angle — the phase of f is not directly measurable in a single-beam scattering experiment. Recovering the phase requires interference measurements (e.g., Coulomb-nuclear interference) or use of partial wave analysis to exploit unitarity constraints. This 'phase problem' in scattering is analogous to the phase problem in X-ray crystallography."

- question: "Why is the scattering amplitude f(θ,φ) described as encoding 'all the physics of the interaction in the far field'? What information does it capture, and what does it not capture?"
  type: short-answer
  answer: "f(θ,φ) encodes everything needed to predict experimental observables: the angular distribution of scattered particles (via dσ/dΩ = |f|²) and the total scattering rate (via σ = ∫|f|²dΩ). Different potentials V(r) produce different f, so measuring f characterizes the interaction. However, f does not capture the wavefunction inside or near the potential region — it is strictly an asymptotic (large-r) quantity. Also, f is a complex function, but experiments typically measure only |f|², so the phase information is inaccessible without special interference setups."
  explanation: "The scattering amplitude is the bridge between the quantum mechanical description (wavefunction solving Schrödinger's equation) and experimental measurements (particle counts at each angle). Its power is that two very different potentials that produce the same f(θ,φ) are experimentally indistinguishable — scattering experiments constrain but do not uniquely determine the underlying interaction, a fact with deep implications for nuclear and particle physics."
```

## Explainer

From your study of the hydrogen atom, you solved the Schrödinger equation for bound states — states with negative energy, where the electron stays near the proton. Scattering theory addresses the complementary situation: positive-energy states where a particle arrives from far away, interacts with a potential, and flies off in some direction. These **unbound states** cannot be normalized in the usual sense (they extend to infinity), but they are physically real and experimentally essential — every particle accelerator experiment is a scattering measurement.

The standard setup is an incident **plane wave** ψ_inc = e^{ikz}, representing a particle moving in the z-direction with definite momentum ℏk. After encountering the localized potential V(r), the total wavefunction asymptotically takes the form ψ ≈ e^{ikz} + f(θ,φ) e^{ikr}/r. The first term is the unscattered wave continuing forward; the second is the scattered **spherical wave**, whose amplitude decreases as 1/r. The 1/r falloff is mandatory: probability must be distributed over an expanding spherical surface of area 4πr², so the probability density |ψ|² ∝ 1/r², requiring |ψ_amplitude| ∝ 1/r. The **scattering amplitude** f(θ,φ) encodes all the physics of the interaction in the far field.

The connection to experiment is through the **differential cross section** dσ/dΩ = |f(θ,φ)|². Think of it geometrically: a detector subtending solid angle dΩ at angle (θ,φ) catches a fraction of the scattered beam. The differential cross section is the effective target area that would scatter that fraction if the beam were perfectly uniform. It has units of area (barns, fm², etc.) and is directly measurable by counting particles at each angle. The **total cross section** σ = ∫|f|² dΩ is the total effective area, relating the incident beam flux to the total scattering rate.

The remarkable fact is that f(θ,φ) — a single complex function of two angles — completely determines all scattering observables. Different potentials V(r) produce different scattering amplitudes, and measuring the angular distribution of scattered particles is the primary experimental tool for learning about the potential. This is how Rutherford deduced the nuclear charge distribution, how electron scattering revealed the proton's internal quark structure, and how modern accelerator experiments probe the fundamental interactions at small scales.
