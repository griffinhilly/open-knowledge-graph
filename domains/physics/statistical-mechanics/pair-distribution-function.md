---
id: pair-distribution-function
title: Pair Distribution Function
domain: physics
course: statistical-mechanics
prerequisites:
- id: two-point-correlation-functions
  type: hard
- id: canonical-ensemble
  type: soft
builds-toward:
- radial-distribution-function
- static-structure-factor
- virial-coefficients-interaction
tags:
- structure
- correlations
- liquids
stage: advanced
status: draft
---

# Pair Distribution Function

## Core Idea
The pair distribution function g(r) describes the probability of finding two particles at separation r relative to random distribution: g(r) = 1 for uncorrelated particles and deviates at short range where interactions dominate. It encodes all two-body spatial correlations and can be measured experimentally via X-ray or neutron scattering.

## Explainer

The pair distribution function is the answer to a simple question: if I stand on one particle, how likely am I to find another particle at distance r? Specifically, **g(r)** is defined so that ρg(r) gives the local number density at distance r from a reference particle, where ρ is the bulk average density. If particles were uncorrelated and randomly placed (an ideal gas), g(r) = 1 everywhere — the local density equals the bulk density regardless of where you look. Any deviation from 1 is a signature of real spatial correlations driven by interactions or quantum statistics.

You already know two-point correlation functions from your prerequisite study: they measure how the value of a quantity at one point depends on its value at another. The pair distribution function is precisely the two-body density-density correlation. From the canonical ensemble, it's defined as the normalized probability of simultaneously finding a particle near position **r** and another near the origin, averaged over all particle pairs and thermal fluctuations. In an isotropic fluid, g depends only on the scalar distance r, not the direction — hence the name *radial* distribution function when applied to liquids.

The shape of g(r) encodes the physical character of the material. For a hard-sphere fluid, g(r) = 0 for r < σ (two hard spheres simply cannot overlap), then rises sharply from zero at r = σ as the excluded volume ends. The first peak at r ≈ σ tells you that nearest-neighbor shells are densely packed. Subsequent oscillating peaks at r ≈ 2σ, 3σ, … correspond to second, third, and further neighbor shells. These oscillations decay away over a few particle diameters in a liquid; in a crystal they persist to infinite range. A gas shows no structure beyond r ≈ σ because particles are too dilute to maintain neighbor shells.

The great practical value of g(r) is its connection to experiment and to thermodynamic quantities. The **static structure factor** S(k), measured directly by X-ray and neutron scattering, is related to g(r) by a Fourier transform: S(k) = 1 + ρ∫[g(r) − 1]e^{ik·r}d³r. Scattering experiments thus give you g(r) directly from the diffraction pattern. Conversely, once you have g(r), you can compute the equation of state, the pressure, and the internal energy through the **virial expansion** and related formulas — making g(r) the central structural quantity linking microscopic pair interactions to macroscopic thermodynamic properties.
