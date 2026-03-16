---
id: two-point-correlation-functions
title: Two-Point Correlation Functions
domain: physics
course: statistical-mechanics
prerequisites:
- id: statistical-ensembles-intro
  type: hard
- id: partition-function-fundamentals
  type: hard
builds-toward:
- pair-distribution-function
- time-correlation-functions
- response-functions-definition
tags:
- correlations
- structure
- equilibrium
stage: advanced
status: draft
---

# Two-Point Correlation Functions

## Core Idea
Two-point correlation functions G(r,r') = ⟨A(r)B(r')⟩ quantify spatial or temporal correlations between observables at different locations or times. They characterize the structure of thermal fluctuations, measure how perturbations propagate through a system, and provide direct connection to experimental scattering measurements.

## Explainer

You know from statistical ensembles that thermal averages ⟨A⟩ give the mean value of an observable. A two-point correlation function asks a more refined question: given that observable A has some value at position r, how does that constrain what observable B looks like at position r'? The **connected correlation function** G(r,r') = ⟨A(r)B(r')⟩ − ⟨A(r)⟩⟨B(r')⟩ measures the covariance — it is zero when the two locations fluctuate independently and large when they are correlated.

In a translationally invariant system, G(r,r') depends only on the separation |r − r'|, and we write G(r) where r = |r − r'|. The **correlation length** ξ characterizes how quickly G(r) decays with distance. Far from any phase transition, fluctuations are short-ranged: G(r) ~ exp(−r/ξ) falls off exponentially, meaning distant parts of the system are statistically independent. Near a critical point, ξ diverges — correlations extend across the entire system and G(r) decays only as a power law. The divergence of ξ at criticality is what makes phase transitions universal and difficult to treat perturbatively.

From the partition function you already know, correlations are computable as derivatives. For a system in a field h(r) that couples to A(r), the connected correlator is exactly δ²ln(Z)/δh(r)δh(r'). This makes the partition function doubly useful: the first derivative gives the order parameter; the second derivative gives its fluctuations. The structure of fluctuations is encoded in Z, and two-point functions are the systematic way to extract it.

The experimental importance of two-point functions is direct: **scattering experiments** (X-ray, neutron, light scattering) measure the structure factor S(q) = ∫G(r)exp(iq·r)dr, the Fourier transform of the density-density correlation function. The positions and widths of scattering peaks directly encode spatial ordering (crystal structure) and the correlation length. A sharp Bragg peak signals long-range order; a broad, diffuse peak signals short-range correlations with length ξ ~ 1/Δq. The connection between statistical mechanics and experiment runs directly through the two-point function — it is the primary bridge between theory and measurement in condensed matter and liquids.
