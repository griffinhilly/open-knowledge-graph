---
id: partial-wave-analysis
title: Partial Wave Analysis in Scattering
domain: physics
course: quantum-mechanics
prerequisites:
- id: scattering-theory-intro
  type: hard
- id: orbital-angular-momentum-quantum
  type: hard
builds-toward:
- cross-sections-scattering
tags:
- partial-waves
- angular-momentum
stage: abstract-reasoning
status: draft
---

# Partial Wave Analysis in Scattering

## Core Idea
Scattering amplitude expands in angular momentum: f(θ) = Σ_l (2l+1) f_l P_l(cos θ) / 2ik. Low energies dominated by s-wave (l=0). Phase shift δ_l encodes each partial wave's phase change.

## Explainer

From scattering theory you already know the basic setup: an incident plane wave e^{ikz} interacts with a target potential and produces an outgoing spherical wave, with everything encoded in the **scattering amplitude** f(θ). Partial wave analysis is a systematic way to decompose this amplitude by angular momentum — essentially, by how far the incoming particle misses the center of the target.

The key insight is that a plane wave can be expanded in spherical waves of definite angular momentum: e^{ikz} = Σ_l i^l (2l+1) j_l(kr) P_l(cos θ). Each term in this sum is a **partial wave** corresponding to orbital angular momentum quantum number l. Far from the target, each radial function j_l(kr) looks like a combination of incoming and outgoing spherical waves. The potential can only change the *relative phase* between incoming and outgoing parts of each partial wave — it cannot mix different l values for a spherically symmetric potential, because you already know from orbital angular momentum theory that l is conserved under central potentials. The effect of the potential on partial wave l is therefore completely captured by a single real number, the **phase shift** δ_l: the outgoing wave is delayed (or advanced) in phase relative to the free case by 2δ_l.

This leads directly to the scattering amplitude: f(θ) = (1/k) Σ_l (2l+1) e^{iδ_l} sin(δ_l) P_l(cos θ), where the Legendre polynomials P_l(cos θ) carry the angular dependence. The total cross section is the integral |f(θ)|² over all angles, giving the **optical theorem**: σ_total = (4π/k) Im[f(0)]. Each partial wave contributes independently, and its maximum possible contribution to the cross section is 4π(2l+1)/k² — achieved when sin²(δ_l) = 1, i.e., δ_l = π/2.

The practical power comes from truncating the sum. A particle with linear momentum ℏk and impact parameter b has angular momentum ℏl ≈ ℏkb, so significant scattering only occurs for partial waves with l ≲ kR, where R is the range of the potential. At low energies (kR ≪ 1), only the **s-wave** (l = 0) contributes — scattering is isotropic (since P₀ = 1) and the entire interaction is encoded in the single number δ₀. This is why nuclear and atomic physicists can often characterize a low-energy scattering potential with just the **scattering length** a = −lim_{k→0} tan(δ₀)/k: one parameter captures all the low-energy physics regardless of the potential's detailed shape. As energy increases, higher partial waves turn on sequentially, and resonances — sharp peaks in a particular δ_l — signal quasi-bound states where the particle lingers near the target.
