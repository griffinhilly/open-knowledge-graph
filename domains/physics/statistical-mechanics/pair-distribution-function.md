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

## Questions

```yaml
- question: "A researcher measures g(r) for a fluid and finds g(r) = 1 for all values of r. What does this tell them about the fluid?"
  type: multiple-choice
  options:
    - "The fluid is perfectly ordered, like a crystal"
    - "The particles are spatially uncorrelated — the fluid behaves like an ideal gas"
    - "The fluid has strong repulsive interactions at all distances"
    - "The measurement failed; g(r) = 1 is physically impossible in any real fluid"
  answer: 1
  explanation: "g(r) is defined relative to a random (uncorrelated) distribution: g(r) = ρ_local(r) / ρ_bulk. When g(r) = 1 everywhere, the local density at every distance exactly equals the bulk average, meaning no spatial correlations exist — particles are placed as if randomly. This is the ideal gas limit. A crystal would show sharp peaks at lattice spacings persisting to long range; a liquid shows oscillating peaks that decay over a few particle diameters."

- question: "For a hard-sphere fluid with particle diameter σ, a student claims that g(r) must be small but positive for r < σ due to thermal fluctuations occasionally driving particles to overlap. Is this correct, and what does g(r) actually equal for r < σ?"
  type: multiple-choice
  options:
    - "Correct — thermal energy allows occasional overlaps, so g(r) is small but positive for r < σ"
    - "Incorrect — g(r) = 0 exactly for r < σ because hard spheres cannot overlap under any circumstances"
    - "Correct — quantum tunneling allows rare overlap events, giving a nonzero g(r)"
    - "Incorrect — g(r) = 1 for r < σ, then drops to zero at the particle surface"
  answer: 1
  explanation: "Hard spheres are defined by an infinite repulsive potential for r < σ — two hard spheres simply cannot overlap regardless of thermal energy. Therefore g(r) = 0 exactly for r < σ. The sharp rise from 0 at r = σ corresponds to the excluded-volume boundary, followed by the first peak at r ≈ σ representing the densely packed nearest-neighbor shell. This is not a thermal effect that could be overcome; it is a hard geometric constraint."

- question: "A liquid shows oscillating peaks in g(r) that decay over a few particle diameters, while an ideal gas has g(r) = 1 everywhere. This means the pair distribution function can distinguish between liquid and gas phases."
  type: true-false
  answer: true
  explanation: "True. The oscillating decay in g(r) for a liquid reflects the short-range order of neighbor shells — particles pack around each other in shells at ~σ, ~2σ, ~3σ, etc., but this order fades over a few particle diameters (unlike the infinite-range order in a crystal). The ideal gas shows no such structure. g(r) is precisely the tool that quantifies this difference in spatial correlation, making it a diagnostic of the structural character of a phase."

- question: "The static structure factor S(k) and the pair distribution function g(r) are independent quantities — S(k) measures momentum-space structure while g(r) measures real-space structure — and neither can be derived from the other."
  type: true-false
  answer: false
  explanation: "False. S(k) and g(r) are Fourier transform pairs: S(k) = 1 + ρ∫[g(r) − 1]e^{ik·r}d³r. They encode exactly the same structural information in reciprocal and real space respectively. This is why X-ray and neutron scattering experiments — which directly measure S(k) as a diffraction pattern — give you g(r): you simply Fourier-transform the scattering data. They are not independent; knowing one fully determines the other."

- question: "Why is g(r) = 1 for a completely uncorrelated system, and what does a peak with g(r) > 1 at some distance r* physically signify?"
  type: short-answer
  answer: "g(r) = 1 when the local particle density at distance r equals the bulk average density — the probability of finding a neighbor is exactly what you would expect from a random (Poisson) distribution. A peak with g(r) > 1 at r* means the local density there is enhanced above the bulk average, indicating that particles preferentially sit at that separation. For a liquid, this corresponds to a nearest-neighbor shell: interactions (repulsion at close range, attraction or packing geometry at r*) cause particles to cluster preferentially at that distance."
  explanation: "The ratio g(r) = ρ(r)/ρ_bulk normalizes out the trivial effect of bulk density, so deviations from 1 purely reflect correlations. A peak above 1 means particles are more likely to be found at that separation than chance alone predicts — a signature of structure imposed by interactions. The height and position of the first peak directly quantifies nearest-neighbor packing, while subsequent peaks reveal further shells. This normalization is what makes g(r) comparable across different densities and systems."
```

## Explainer

The pair distribution function is the answer to a simple question: if I stand on one particle, how likely am I to find another particle at distance r? Specifically, **g(r)** is defined so that ρg(r) gives the local number density at distance r from a reference particle, where ρ is the bulk average density. If particles were uncorrelated and randomly placed (an ideal gas), g(r) = 1 everywhere — the local density equals the bulk density regardless of where you look. Any deviation from 1 is a signature of real spatial correlations driven by interactions or quantum statistics.

You already know two-point correlation functions from your prerequisite study: they measure how the value of a quantity at one point depends on its value at another. The pair distribution function is precisely the two-body density-density correlation. From the canonical ensemble, it's defined as the normalized probability of simultaneously finding a particle near position **r** and another near the origin, averaged over all particle pairs and thermal fluctuations. In an isotropic fluid, g depends only on the scalar distance r, not the direction — hence the name *radial* distribution function when applied to liquids.

The shape of g(r) encodes the physical character of the material. For a hard-sphere fluid, g(r) = 0 for r < σ (two hard spheres simply cannot overlap), then rises sharply from zero at r = σ as the excluded volume ends. The first peak at r ≈ σ tells you that nearest-neighbor shells are densely packed. Subsequent oscillating peaks at r ≈ 2σ, 3σ, … correspond to second, third, and further neighbor shells. These oscillations decay away over a few particle diameters in a liquid; in a crystal they persist to infinite range. A gas shows no structure beyond r ≈ σ because particles are too dilute to maintain neighbor shells.

The great practical value of g(r) is its connection to experiment and to thermodynamic quantities. The **static structure factor** S(k), measured directly by X-ray and neutron scattering, is related to g(r) by a Fourier transform: S(k) = 1 + ρ∫[g(r) − 1]e^{ik·r}d³r. Scattering experiments thus give you g(r) directly from the diffraction pattern. Conversely, once you have g(r), you can compute the equation of state, the pressure, and the internal energy through the **virial expansion** and related formulas — making g(r) the central structural quantity linking microscopic pair interactions to macroscopic thermodynamic properties.
