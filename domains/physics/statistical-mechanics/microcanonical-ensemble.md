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
stage: expert
status: validated
---

# Microcanonical Ensemble (NVE)

## Core Idea
The microcanonical ensemble describes an isolated system with fixed energy E, volume V, and particle number N. All microstates with energy exactly E are equally probable. Entropy is proportional to the logarithm of the multiplicity Ω(E,V,N), and all thermodynamic quantities follow from the fundamental relation S(E,V,N).

## Questions

```yaml
- question: "A system of 100 distinguishable coins starts with all 100 showing heads. After being shaken randomly, it overwhelmingly reaches a disordered state. The best statistical mechanics explanation for this is:"
  type: multiple-choice
  options:
    - "Physical forces preferentially push the system toward disorder"
    - "The coins are driven toward equilibrium by entropy maximization acting as a physical force"
    - "There are astronomically more microstates corresponding to mixed outcomes than to all-heads, so random access to microstates overwhelmingly produces disordered-looking macrostates"
    - "Energy is minimized in disordered states, making them thermodynamically favorable"
  answer: 2
  explanation: "Disorder wins by pure combinatorics, not by any preference or force. For 100 coins, there is exactly 1 microstate with all heads, but C(100,50) ≈ 10²⁹ microstates near the 50/50 split. The equal a priori probability postulate says all microstates are equally likely. So 'disordered' macrostates are overwhelmingly more probable simply because they correspond to vastly more microstates. Entropy doesn't 'push' the system anywhere — the system is just equally likely to be in any microstate, and almost all microstates look disordered."

- question: "In the microcanonical ensemble, temperature is defined by 1/T = (∂S/∂E)_{V,N}. What does this definition mean physically?"
  type: multiple-choice
  options:
    - "Temperature is the average kinetic energy of particles in the system divided by Boltzmann's constant"
    - "Temperature is the inverse of the rate at which the system's entropy increases as energy is added — a high-T system gains little additional entropy per unit of added energy"
    - "Temperature measures the number of accessible microstates at a given energy"
    - "Temperature in the microcanonical ensemble is defined independently of entropy and only relates to particle velocities"
  answer: 1
  explanation: "The definition 1/T = (∂S/∂E) says temperature is derived from entropy, not the other way around. When you add a unit of energy to a cold system (low T, high ∂S/∂E), entropy increases a lot — the system has many new accessible states. When you add the same energy to a hot system (high T, low ∂S/∂E), entropy barely changes — the system was already exploring a vast number of states. This definition also explains heat flow: when two systems with different T are brought into contact, energy flows from high-T to low-T because doing so increases total entropy."

- question: "The equal a priori probability postulate — that all accessible microstates are equally probable for an isolated equilibrium system — is derived from Newton's laws of mechanics."
  type: true-false
  answer: false
  explanation: "The equal a priori probability postulate is a foundational assumption, not a derived result. It is justified by its extraordinary predictive success — the entire edifice of equilibrium statistical mechanics is built on it — but it cannot be rigorously derived from classical or quantum mechanics alone. Attempts to derive it from ergodic theory (that systems explore all accessible states over time) provide partial justification but not a complete proof. The postulate's status as a postulate rather than a theorem is important to recognize."

- question: "The microcanonical ensemble is conceptually foundational but computationally impractical for most systems, because the constraint that energy is exactly E makes the multiplicity Ω very difficult to calculate."
  type: true-false
  answer: true
  explanation: "Calculating Ω(E) requires counting the exact number of microstates with energy precisely equal to E — a combinatorially hard problem for most realistic systems. The canonical ensemble avoids this by allowing energy to fluctuate around a fixed average (controlled by temperature), which introduces the Boltzmann factor e^(−βE) and makes the mathematics far more tractable. In the thermodynamic limit, the two ensembles give identical predictions for average quantities, so physicists almost always work with the canonical ensemble in practice while understanding the microcanonical ensemble as the conceptual foundation."

- question: "Why does S = k_B ln Ω, rather than S = k_B · Ω, correctly capture thermodynamic behavior? What property of physical systems does the logarithm capture?"
  type: short-answer
  answer: "Entropy must be additive: the entropy of two independent systems combined equals the sum of their individual entropies. When two independent systems are combined, their total number of microstates is the product of their individual multiplicities (Ω_total = Ω₁ × Ω₂), because each state of one system can be combined with each state of the other. The logarithm converts this multiplicative combination into an additive one: ln(Ω₁ × Ω₂) = ln Ω₁ + ln Ω₂. This ensures entropy is extensive — proportional to system size — as thermodynamics requires."
  explanation: "The logarithm also converts astronomical numbers into manageable ones. For a mole of gas, Ω might be on the order of 10^(10^23), but ln Ω is a tractable number proportional to N. The Boltzmann constant k_B then gives the correct dimensional units (J/K) to match macroscopic thermodynamics. Both the additivity requirement and the need for extensive quantities point uniquely to the logarithm as the correct function relating multiplicity to entropy."
```

## Explainer

From your study of ensemble theory fundamentals and entropy, you know that a macrostate is characterized by a small number of macroscopic variables while an enormous number of microscopic configurations (microstates) are consistent with it. The microcanonical ensemble is the simplest and most fundamental ensemble: it describes a system that is completely isolated — no heat exchange, no particle exchange, fixed energy E, volume V, and particle number N. The NVE label captures these three constraints.

The foundational postulate is the **equal a priori probability principle**: for an isolated system in equilibrium, every accessible microstate with energy E is equally probable. This is not derived from more basic principles — it is a postulate, justified by its remarkable success in predicting experimental outcomes. If you have a gas of N particles in a box with total energy E, every arrangement of positions and momenta consistent with that energy is equally likely. There's no reason to prefer any particular microstate over another when the system is isolated and in equilibrium. This democratic assumption, combined with the sheer number of particles (∼10²³), is enough to derive all of thermodynamics.

The key quantity is **Ω(E,V,N)**, the number of microstates accessible to the system — sometimes called the multiplicity or density of states. For a simple example, consider N two-state systems (spins), each either up (+) or down (−), with energy E = −m·B proportional to the number of up spins minus down spins. Given the total energy, you know the total magnetization, which fixes the number of up and down spins. The multiplicity is just the combinatorial count Ω = N! / (N_up! N_down!). For large N, this peaks sharply near 50/50, explaining why disordered states are overwhelmingly more probable than ordered ones — not because disorder is preferred, but because there are far more ways to be disordered.

**Boltzmann's formula** S = k_B ln Ω is the bridge between the microscopic count and the macroscopic entropy you know from thermodynamics. Taking the logarithm converts multiplicative combinatorics into additive entropy, and the factor k_B (Boltzmann's constant) converts to standard thermodynamic units. From this single equation, all thermodynamic quantities emerge by differentiation. Temperature is defined by 1/T = (∂S/∂E)_{V,N}: temperature is the rate at which entropy increases as you add energy. When two systems are brought into thermal contact, energy flows from higher T to lower T until (∂S/∂E) is equal for both — maximizing total entropy, which is the second law.

The microcanonical ensemble is conceptually foundational but computationally impractical for most systems. The constraint that energy is exactly E (rather than approximately E) makes Ω difficult to calculate except for simple models. In practice, allowing energy to fluctuate while fixing average energy — the **canonical ensemble** — is mathematically much easier and gives identical results in the thermodynamic limit. The microcanonical ensemble establishes the conceptual ground (equal a priori probabilities, entropy as log of multiplicity), and the canonical ensemble builds on it by introducing a heat bath, leading to the Boltzmann factor and partition function that you'll use for almost all real calculations.


