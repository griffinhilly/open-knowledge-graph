---
id: microcanonical-ensemble
title: Microcanonical Ensemble (NVE)
domain: physics
course: statistical-mechanics
prerequisites:
- id: ensemble-theory-fundamentals
  type: hard
- id: entropy-intro
  type: hard
builds-toward:
- canonical-ensemble
- partition-function-definition
tags:
- ensemble
- isolated-system
- constant-energy
stage: advanced
status: draft
---

# Microcanonical Ensemble (NVE)

## Core Idea
The microcanonical ensemble describes an isolated system with fixed energy E, volume V, and particle number N. All microstates with energy exactly E are equally probable. Entropy is proportional to the logarithm of the multiplicity Ω(E,V,N), and all thermodynamic quantities follow from the fundamental relation S(E,V,N).

## Explainer

From your study of ensemble theory fundamentals and entropy, you know that a macrostate is characterized by a small number of macroscopic variables while an enormous number of microscopic configurations (microstates) are consistent with it. The microcanonical ensemble is the simplest and most fundamental ensemble: it describes a system that is completely isolated — no heat exchange, no particle exchange, fixed energy E, volume V, and particle number N. The NVE label captures these three constraints.

The foundational postulate is the **equal a priori probability principle**: for an isolated system in equilibrium, every accessible microstate with energy E is equally probable. This is not derived from more basic principles — it is a postulate, justified by its remarkable success in predicting experimental outcomes. If you have a gas of N particles in a box with total energy E, every arrangement of positions and momenta consistent with that energy is equally likely. There's no reason to prefer any particular microstate over another when the system is isolated and in equilibrium. This democratic assumption, combined with the sheer number of particles (∼10²³), is enough to derive all of thermodynamics.

The key quantity is **Ω(E,V,N)**, the number of microstates accessible to the system — sometimes called the multiplicity or density of states. For a simple example, consider N two-state systems (spins), each either up (+) or down (−), with energy E = −m·B proportional to the number of up spins minus down spins. Given the total energy, you know the total magnetization, which fixes the number of up and down spins. The multiplicity is just the combinatorial count Ω = N! / (N_up! N_down!). For large N, this peaks sharply near 50/50, explaining why disordered states are overwhelmingly more probable than ordered ones — not because disorder is preferred, but because there are far more ways to be disordered.

**Boltzmann's formula** S = k_B ln Ω is the bridge between the microscopic count and the macroscopic entropy you know from thermodynamics. Taking the logarithm converts multiplicative combinatorics into additive entropy, and the factor k_B (Boltzmann's constant) converts to standard thermodynamic units. From this single equation, all thermodynamic quantities emerge by differentiation. Temperature is defined by 1/T = (∂S/∂E)_{V,N}: temperature is the rate at which entropy increases as you add energy. When two systems are brought into thermal contact, energy flows from higher T to lower T until (∂S/∂E) is equal for both — maximizing total entropy, which is the second law.

The microcanonical ensemble is conceptually foundational but computationally impractical for most systems. The constraint that energy is exactly E (rather than approximately E) makes Ω difficult to calculate except for simple models. In practice, allowing energy to fluctuate while fixing average energy — the **canonical ensemble** — is mathematically much easier and gives identical results in the thermodynamic limit. The microcanonical ensemble establishes the conceptual ground (equal a priori probabilities, entropy as log of multiplicity), and the canonical ensemble builds on it by introducing a heat bath, leading to the Boltzmann factor and partition function that you'll use for almost all real calculations.


