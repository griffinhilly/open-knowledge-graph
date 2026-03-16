---
id: canonical-ensemble
title: Canonical Ensemble (NVT)
domain: physics
course: statistical-mechanics
prerequisites:
- id: ensemble-theory-fundamentals
  type: hard
- id: temperature-and-thermal-equilibrium
  type: hard
- id: exponential-functions-and-graphs
  type: soft
builds-toward:
- partition-function-definition
- helmholtz-free-energy
tags:
- ensemble
- thermal-reservoir
- temperature-control
stage: advanced
status: draft
---

# Canonical Ensemble (NVT)

## Core Idea
The canonical ensemble describes a system in thermal contact with a heat bath at temperature T, with fixed N and V. Microstates have probabilities proportional to exp(−E/kT), where the Boltzmann factor exp(−E/kT) is the fundamental weight. This is the most commonly used ensemble in practice.

## Questions

```yaml
- question: "A system has two microstates: one with energy E and one with energy 2E. As temperature T increases toward infinity, what happens to the ratio of their probabilities?"
  type: multiple-choice
  options:
    - "The high-energy state becomes even less likely"
    - "The ratio approaches 1 — both states become equally probable"
    - "The high-energy state becomes impossible"
    - "The ratio depends only on the volume, not temperature"
  answer: 1
  explanation: "The probability of a microstate is proportional to exp(−E/kT). The ratio of probabilities is exp(−E/kT) / exp(−2E/kT) = exp(E/kT). As T → ∞, E/kT → 0, so exp(E/kT) → 1 — the two states become equally probable. The Boltzmann factor suppresses high-energy states at low T, but thermal fluctuations wash out energy differences at very high T."

- question: "In the canonical ensemble, the total energy of the system is exactly fixed at all times."
  type: true-false
  answer: false
  explanation: "Only N (particle number), V (volume), and T (temperature) are fixed in the canonical ensemble. Because the system is in thermal contact with a heat bath, energy can fluctuate — individual microstates have different energies. The average energy is well-defined, but instantaneous energy is not fixed. This contrasts with the microcanonical ensemble, where energy is fixed exactly."

- question: "Why is the canonical ensemble more practically useful than the microcanonical ensemble for most calculations?"
  type: short-answer
  answer: "The canonical ensemble holds temperature constant by coupling to a heat bath, which is how real laboratory experiments are typically conducted. The microcanonical ensemble fixes energy exactly, which is mathematically convenient but physically harder to realize. Fixing T is easier in practice than isolating a system to prevent any energy exchange."
  explanation: "Most real experiments are performed in contact with an environment at a known temperature, not in perfect thermal isolation. The canonical ensemble captures this situation directly. The partition function Z = Σ exp(−E_i/kT) also provides a convenient route to all thermodynamic quantities (free energy, entropy, heat capacity) via derivatives."
```

## Explainer

The canonical ensemble is the statistical mechanics framework for systems that can freely exchange energy with their surroundings — the situation in nearly every real experiment. Imagine a small system (say, a gas of N molecules) in a box with thin walls in contact with a huge thermal reservoir. The reservoir is so large that heat flowing in or out doesn't change its temperature. The system's temperature T is therefore fixed, but its energy fluctuates as it constantly exchanges tiny amounts of heat with the reservoir.

The central result is the Boltzmann distribution: the probability that the system occupies a microstate with energy E_i is P_i = exp(−E_i/kT) / Z, where Z = Σ exp(−E_j/kT) is the partition function summing over all microstates. The Boltzmann factor exp(−E/kT) is the engine of this formula. It tells you that lower-energy microstates are always more probable, and the sharpness of this preference depends on temperature. At very low T, the system is almost certainly in its ground state. At very high T, the exponential suppression weakens and the system explores high-energy microstates more freely.

From your prerequisite in ensemble theory, you know that an ensemble is a conceptual collection of many identical copies of a system, each in a possible microstate. In the canonical ensemble, those copies share the same T, N, and V but can have different energies. The probability distribution over those copies is precisely the Boltzmann distribution. This is what distinguishes the canonical from the microcanonical ensemble (which fixes energy) and the grand canonical ensemble (which allows particle exchange too).

The partition function Z is more than a normalization constant — it encodes all thermodynamic information about the system. The average energy is ⟨E⟩ = −∂(ln Z)/∂β where β = 1/kT. The Helmholtz free energy is F = −kT ln Z, and from F you can derive entropy, pressure, and heat capacity. This is why mastering the canonical ensemble opens the door to computing measurable thermodynamic quantities from a microscopic model of the system.

A key intuition: the canonical ensemble is a competition between energy minimization and entropy maximization. Low-energy states are favored by the Boltzmann factor, but there may be vastly more microstates at higher energies. The balance between these two tendencies — encoded in the free energy F = U − TS — determines the equilibrium state. Thermodynamics emerges from this competition.
