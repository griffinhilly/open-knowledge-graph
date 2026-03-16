---
id: addition-of-angular-momenta
title: Addition of Angular Momenta
domain: physics
course: quantum-mechanics
prerequisites:
- id: orbital-angular-momentum-quantum
  type: hard
- id: spin-angular-momentum
  type: hard
builds-toward:
- clebsch-gordan-coefficients
- hydrogen-atom-quantum
tags:
- angular-momentum
- coupling
- composite-systems
stage: advanced
status: draft
---

# Addition of Angular Momenta

## Core Idea
When two angular momenta J̄₁ and J̄₂ couple, the total angular momentum J̄ = J̄₁ + J̄₂ can take values where |j₁ - j₂| ≤ j ≤ j₁ + j₂. States |j₁m₁⟩|j₂m₂⟩ in the uncoupled basis can be rewritten as superpositions of coupled states |jm⟩. The transformation coefficients are Clebsch-Gordan coefficients governing atomic and nuclear spectra.

## Explainer

You know from orbital angular momentum that a particle with quantum number l can have z-projections m ranging from −l to +l in integer steps, giving 2l+1 states. You also know that spin-1/2 particles have two states: m_s = +1/2 or −1/2. The question this topic addresses is: when a system has *two* sources of angular momentum simultaneously — say, the orbital motion of an electron around a nucleus and its intrinsic spin — what are the allowed values of the *total* angular momentum, and how do you describe the combined quantum state?

The **uncoupled basis** is the natural starting point. You label states by |j₁, m₁⟩|j₂, m₂⟩, specifying each angular momentum's projection independently. The total z-projection m = m₁ + m₂ is always definite in this basis. But the total magnitude J² is generally not — these states are not eigenstates of J². The **coupled basis** |j, m⟩ reorganizes the same Hilbert space so that both J² and J_z are sharp. The allowed values of j run from |j₁ − j₂| up to j₁ + j₂ in integer steps. You can verify the state counts match: Σ(2j+1) over the coupled values equals (2j₁+1)(2j₂+1), the total dimension.

A concrete example: couple spin-1/2 (j₁ = 1/2) with spin-1/2 (j₂ = 1/2). The uncoupled states are |↑↑⟩, |↑↓⟩, |↓↑⟩, |↓↓⟩ — four states. The coupled basis gives j = 1 (three states: m = +1, 0, −1) and j = 0 (one state: m = 0). The j = 1 states form the **triplet** and the j = 0 state is the **singlet**. The singlet is the antisymmetric combination (|↑↓⟩ − |↓↑⟩)/√2, which you may recognize as the spin state of two electrons in a helium ground state or an entangled Bell state. The triplet states are symmetric combinations.

The numbers that convert between these two bases are the **Clebsch-Gordan coefficients** ⟨j₁m₁; j₂m₂ | jm⟩. They are tabulated and encode the full transformation. Physically, coupling matters whenever you need to know how a system responds to a perturbation that depends on total angular momentum (like spin-orbit coupling, which shifts atomic energy levels depending on j = l + s). Spectroscopic selection rules — which transitions are allowed by the emission or absorption of a photon — are written in terms of j, not the individual l and s separately. This is why addition of angular momenta is not just a mathematical exercise but the language in which atomic spectra are organized.
