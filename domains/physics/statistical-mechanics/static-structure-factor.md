---
id: static-structure-factor
title: Static Structure Factor
domain: physics
course: statistical-mechanics
prerequisites:
- id: pair-distribution-function
  type: hard
tags:
- structure
- scattering
- correlations
stage: advanced
status: draft
---

# Static Structure Factor

## Core Idea
The static structure factor S(k) is the Fourier transform of the pair distribution function, describing how a system scatters radiation at different wavelengths. It encodes density correlations at all length scales and is directly measurable in X-ray, neutron, or light scattering experiments.

## Explainer

You already know the **pair distribution function** g(r), which tells you the probability of finding a particle at distance r from a reference particle, relative to the average density. A perfect gas has g(r) = 1 everywhere (no correlations); real liquids show peaks at preferred distances (shells of neighbors) that decay to 1 at large r; crystals show sharp peaks at the lattice spacings. The static structure factor S(k) encodes exactly the same information, but in **reciprocal space** (Fourier space) rather than real space. The relationship is:

S(k) = 1 + ρ ∫ [g(r) − 1] e^{ik·r} d³r

where ρ is the number density and k is a wavevector with magnitude k = 2π/λ, corresponding to a length scale λ. Large k probes short-length-scale correlations (how atoms pack locally); small k probes long-wavelength fluctuations.

The physical significance becomes clear when you consider what a scattering experiment measures. When X-rays or neutrons hit a material, each atom scatters the radiation. The total scattered intensity at a given scattering angle (corresponding to wavevector transfer k) is determined by the **coherent interference** of waves scattered by all pairs of atoms. If atoms are randomly positioned (ideal gas), scattering from different atoms averages out at all angles except k = 0 — giving S(k) = 1 everywhere. If atoms are positively correlated at separation r = 2π/k — meaning there is an enhanced probability of finding pairs at that distance — the scattered waves interfere constructively and S(k) > 1. The peaks of S(k) thus directly reveal the dominant length scales of order in the material. For a crystal, S(k) has sharp delta-function peaks at the reciprocal lattice vectors — the **Bragg peaks** you know from crystallography. For a liquid, S(k) shows a broad primary peak at k ≈ 2π/d (d = typical interparticle spacing) and secondary oscillations that decay away.

The small-k limit is especially informative. As k → 0, S(k → 0) = ρ k_B T κ_T, where κ_T is the isothermal compressibility. A large S(0) means the system is highly compressible — large density fluctuations on long length scales — which happens near a **critical point** where κ_T diverges. This is why critical opalescence (the milky scattering of light near a liquid-gas critical point) is directly a manifestation of S(k) becoming large at small k. The static structure factor thus connects microscopic pair correlations to macroscopic thermodynamic quantities through a single measurable function — making it one of the central diagnostic tools of condensed matter physics and soft matter science.
