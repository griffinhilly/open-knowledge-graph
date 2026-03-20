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
stage: advanced
status: draft
---

# Plane Waves in Vacuum

## Core Idea
Plane wave solutions to the wave equation have the form E = E₀e^{i(k·r - ωt)} where ω = ck. The transverse nature of electromagnetic waves (E and B perpendicular to k and to each other) follows from Maxwell's equations. The dispersion relation ω = ck is exact in vacuum, independent of frequency.

## Explainer

From the electromagnetic wave equation you know that both E and B satisfy ∇²**E** = (1/c²)∂²**E**/∂t², a linear PDE with constant coefficients. The most natural solutions are **plane waves**: fields of the form **E** = **E₀** e^{i(**k**·**r** − ωt)}, where **k** is the wave vector pointing in the direction of propagation and ω is the angular frequency. These solutions are "plane" because at any fixed time, the field is identical everywhere on a plane perpendicular to **k** — the phase **k**·**r** − ωt is constant on such planes, which are the wavefronts. Every other solution — beams, pulses, standing waves — can be built as a superposition of plane waves through Fourier decomposition.

Substituting the plane wave ansatz into the wave equation immediately gives the **dispersion relation**: k² = ω²/c², or equivalently ω = ck. This tells you that all electromagnetic waves in vacuum travel at the same speed c, regardless of frequency. This non-dispersive character distinguishes vacuum from any material medium — in glass or water, different frequencies travel at different speeds (which is why prisms split white light into colors). The dispersion relation ω = ck is linear in k, which implies the group velocity and phase velocity are both equal to c, and a wave packet of any bandwidth travels without spreading.

The truly remarkable consequence comes from applying **Gauss's law** ∇·**E** = 0 to the plane wave. Taking the divergence of **E** = **E₀** e^{i(**k**·**r** − ωt)}, the spatial derivative acts on the exponent to pull down a factor of i**k**, giving i**k**·**E₀** = 0. This means **k**·**E₀** = 0: the electric field is perpendicular to the propagation direction. The wave is **transverse**. Similarly, Gauss's law for magnetism (∇·**B** = 0) forces **k**·**B** = 0 — the magnetic field is also transverse. Faraday's law then fixes the relationship between **E** and **B**: **B** = (**k** × **E**)/ω = k̂ × **E**/c. The three vectors **k**, **E**, and **B** form a right-handed orthogonal triplet, with |**B**| = |**E**|/c. This geometry — not assumed but derived from Maxwell's equations — is the fundamental structure of all electromagnetic radiation.

The plane wave solution is also the foundation for understanding **polarization**: since **E₀** can point in any direction perpendicular to **k**, there is a two-dimensional space of polarization states. Linearly polarized waves have **E₀** pointing along a fixed direction; circularly polarized waves are superpositions of two orthogonal linear polarizations with a 90° phase offset. The energy flux carried by the wave — the Poynting vector **S** = **E** × **H**/μ₀ — points in the **k** direction with magnitude |S| = |E|²/(μ₀c) = c²ε₀|E|², averaging over a cycle to give the intensity. All of this rich structure follows from the single elegant fact that Maxwell's equations in vacuum admit plane wave solutions with ω = ck.

