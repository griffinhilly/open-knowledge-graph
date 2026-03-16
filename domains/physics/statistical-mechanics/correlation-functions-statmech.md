---
id: correlation-functions-statmech
title: Correlation Functions and Spatial Correlations
domain: physics
course: statistical-mechanics
prerequisites:
- id: canonical-ensemble
  type: hard
- id: critical-phenomena-statmech
  type: soft
builds-toward:
- fluctuation-dissipation-theorem-general
tags:
- correlation-function
- pair-correlation
- correlation-length
stage: advanced
status: draft
---

# Correlation Functions and Spatial Correlations

## Core Idea
Correlation functions G(r) = ⟨σ(0)σ(r)⟩ measure how order at one location influences order at distance r. In ordered phases, G(r) → m² as r → ∞. Near criticality, G(r) ~ exp(-r/ξ), where the correlation length ξ → ∞ at T_c. Spatial correlations are probed experimentally via scattering experiments and encode collective behavior.

## Explainer

In the canonical ensemble you computed average values of single observables — the average energy, the average magnetization. But a deeper question is: if a spin (or density fluctuation) at one location takes a particular value, how likely is a spin far away to align with it? This is precisely what a **correlation function** measures. For an Ising-like system, the two-point correlation function is G(r) = ⟨σ(0)σ(r)⟩, the joint average of the spin at the origin and the spin at position r. If the two spins are statistically independent, G(r) = ⟨σ⟩² = m², the square of the mean magnetization. Departures from this baseline signal genuine correlations — one site "knowing about" the other.

The behavior of G(r) changes dramatically with temperature. Deep in the ordered phase (T ≪ T_c), neighboring spins are strongly aligned, and even distant spins remain correlated: G(r) → m² at large r, reflecting long-range order. In the disordered phase (T > T_c), correlations decay exponentially: G(r) − m² ~ exp(−r/ξ), where **ξ is the correlation length** — the characteristic distance over which fluctuations are correlated. At high temperature, ξ is small (a few lattice spacings); spins behave nearly independently. The correlation length is the physical length scale that controls how "aware" each part of the system is of its neighbors.

The critical point T_c is where everything changes. As T → T_c from above, ξ diverges as ξ ~ |T − T_c|^{−ν}, where ν is a **critical exponent**. At exactly T_c, the exponential decay is replaced by a power law: G(r) ~ r^{−(d−2+η)}, where d is spatial dimension and η is another critical exponent. This power-law decay means correlations extend over all length scales simultaneously — there is no characteristic length, which is why the system looks self-similar (fractal) at criticality. The divergence of ξ is what drives the divergence of other quantities like susceptibility and specific heat: a system with long-range correlations responds dramatically to small perturbations.

Correlation functions are not just theoretical constructs — they are directly measurable. In a scattering experiment (X-ray, neutron, or light), the scattered intensity is proportional to the **structure factor** S(q) = ∫ G(r) e^{iq·r} d^dr, the Fourier transform of the correlation function. A diverging correlation length produces a sharp peak in S(q) at q → 0, observable as **critical opalescence** (the milky appearance of fluids near their liquid-gas critical point). This connection between G(r), its Fourier transform, and measurable scattering data is one of the deepest bridges between theory and experiment in condensed matter physics.


