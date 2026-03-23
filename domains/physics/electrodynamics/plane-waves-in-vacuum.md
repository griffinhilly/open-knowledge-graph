---
id: plane-waves-in-vacuum
title: Plane Waves in Vacuum
domain: physics
course: electrodynamics
prerequisites:
- id: electromagnetic-wave-equation
  type: hard
builds-toward:
- polarization-of-waves
- poynting-vector-and-energy-flux
tags:
- waves
- propagation
- vacuum
stage: expert
status: draft
---

# Plane Waves in Vacuum

## Core Idea
Plane wave solutions to the wave equation have the form E = E₀e^{i(k·r - ωt)} where ω = ck. The transverse nature of electromagnetic waves (E and B perpendicular to k and to each other) follows from Maxwell's equations. The dispersion relation ω = ck is exact in vacuum, independent of frequency.

## Questions

```yaml
- question: "A student claims: 'The fact that electromagnetic waves are transverse — that E and B are perpendicular to the propagation direction — is an independent physical postulate required to complete Maxwell's theory.' How would you respond?"
  type: multiple-choice
  options:
    - "The student is correct; transversality must be stated separately as an experimental observation"
    - "Transversality follows directly from applying Gauss's law (∇·E = 0) to the plane wave ansatz — it is derived, not assumed"
    - "Transversality is only approximate; at very high frequencies, E develops a small component along k"
    - "Transversality follows from the wave equation alone, without needing any of Maxwell's other equations"
  answer: 1
  explanation: "Transversality is not a separate postulate — it is derived. Substituting E = E₀e^{i(k·r − ωt)} into Gauss's law ∇·E = 0, the divergence acts on the exponent to produce ik·E₀ = 0, which means k·E₀ = 0: the electric field amplitude is perpendicular to k. Option D is wrong because the wave equation alone doesn't enforce transversality — you specifically need the zero-divergence equations (Gauss's laws for E and B)."

- question: "Why does a glass prism separate white light into colors, while a vacuum does not?"
  type: multiple-choice
  options:
    - "Glass absorbs some frequencies more strongly, removing them selectively from the beam"
    - "In glass the dispersion relation is no longer ω = ck — different frequencies travel at different speeds, so they refract at different angles"
    - "The plane wave approximation breaks down in glass, making light travel in curved paths"
    - "Glass introduces a phase delay that is the same for all frequencies, shifting but not separating them"
  answer: 1
  explanation: "In vacuum, ω = ck holds exactly for all frequencies — all EM waves travel at c regardless of frequency. In glass, interactions with the medium produce a frequency-dependent index of refraction n(ω), so different frequencies travel at c/n(ω) and refract at different angles at the glass surface. This dispersion is absent in vacuum, which is why vacuum propagation is non-dispersive and wave packets travel without spreading."

- question: "In vacuum, gamma rays travel faster than radio waves because their much higher frequency gives them greater energy and therefore greater speed."
  type: true-false
  answer: false
  explanation: "The dispersion relation ω = ck holds exactly for all electromagnetic frequencies in vacuum. The phase velocity ω/k = c is the same for every EM wave, regardless of frequency or energy. This is a fundamental consequence of Maxwell's equations in vacuum — there is no medium to interact with and produce frequency-dependent propagation. All electromagnetic radiation travels at exactly c in vacuum."

- question: "The relationship B = k̂ × E/c between the electric and magnetic fields of a plane wave follows from applying Faraday's law to the plane wave ansatz."
  type: true-false
  answer: true
  explanation: "Applying Faraday's law ∇ × E = −∂B/∂t to the plane wave: the curl of E brings down ik × E₀, and the time derivative of B gives iωB₀. Setting ik × E₀ = iωB₀ and using ω = ck yields B₀ = (k × E₀)/ω = k̂ × E₀/c. This confirms that B is perpendicular to both k and E, with magnitude |E|/c — entirely derived from Maxwell's equations, not assumed."

- question: "Explain how applying Gauss's law (∇·E = 0) to a plane wave E = E₀e^{i(k·r − ωt)} proves that the electric field must be transverse."
  type: short-answer
  answer: "Taking the divergence: ∇·E = ∇·(E₀e^{i(k·r − ωt)}). The spatial derivatives act on the exponent and pull down ik, giving ik·E₀ e^{i(k·r − ωt)}. Setting this equal to zero (Gauss's law in vacuum) yields k·E₀ = 0, which is exactly the condition that E₀ is perpendicular to k — the wave is transverse."
  explanation: "The key step is that differentiating a plane wave with respect to position replaces ∇ with ik algebraically. This converts the differential equation (Gauss's law) into an algebraic dot-product condition on the amplitude vector, directly implying transversality."
```

## Explainer

From the electromagnetic wave equation you know that both E and B satisfy ∇²**E** = (1/c²)∂²**E**/∂t², a linear PDE with constant coefficients. The most natural solutions are **plane waves**: fields of the form **E** = **E₀** e^{i(**k**·**r** − ωt)}, where **k** is the wave vector pointing in the direction of propagation and ω is the angular frequency. These solutions are "plane" because at any fixed time, the field is identical everywhere on a plane perpendicular to **k** — the phase **k**·**r** − ωt is constant on such planes, which are the wavefronts. Every other solution — beams, pulses, standing waves — can be built as a superposition of plane waves through Fourier decomposition.

Substituting the plane wave ansatz into the wave equation immediately gives the **dispersion relation**: k² = ω²/c², or equivalently ω = ck. This tells you that all electromagnetic waves in vacuum travel at the same speed c, regardless of frequency. This non-dispersive character distinguishes vacuum from any material medium — in glass or water, different frequencies travel at different speeds (which is why prisms split white light into colors). The dispersion relation ω = ck is linear in k, which implies the group velocity and phase velocity are both equal to c, and a wave packet of any bandwidth travels without spreading.

The truly remarkable consequence comes from applying **Gauss's law** ∇·**E** = 0 to the plane wave. Taking the divergence of **E** = **E₀** e^{i(**k**·**r** − ωt)}, the spatial derivative acts on the exponent to pull down a factor of i**k**, giving i**k**·**E₀** = 0. This means **k**·**E₀** = 0: the electric field is perpendicular to the propagation direction. The wave is **transverse**. Similarly, Gauss's law for magnetism (∇·**B** = 0) forces **k**·**B** = 0 — the magnetic field is also transverse. Faraday's law then fixes the relationship between **E** and **B**: **B** = (**k** × **E**)/ω = k̂ × **E**/c. The three vectors **k**, **E**, and **B** form a right-handed orthogonal triplet, with |**B**| = |**E**|/c. This geometry — not assumed but derived from Maxwell's equations — is the fundamental structure of all electromagnetic radiation.

The plane wave solution is also the foundation for understanding **polarization**: since **E₀** can point in any direction perpendicular to **k**, there is a two-dimensional space of polarization states. Linearly polarized waves have **E₀** pointing along a fixed direction; circularly polarized waves are superpositions of two orthogonal linear polarizations with a 90° phase offset. The energy flux carried by the wave — the Poynting vector **S** = **E** × **H**/μ₀ — points in the **k** direction with magnitude |S| = |E|²/(μ₀c) = c²ε₀|E|², averaging over a cycle to give the intensity. All of this rich structure follows from the single elegant fact that Maxwell's equations in vacuum admit plane wave solutions with ω = ck.

