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

## Questions

```yaml
- question: "An electron in a hydrogen atom has orbital quantum number l = 1 and spin s = 1/2. What are the allowed values of total angular momentum quantum number j?"
  type: multiple-choice
  options:
    - "j = 0, 1/2, 1, 3/2, and 2 — all values from 0 to l + s"
    - "j = 1/2 and j = 3/2 — the values from |l − s| to l + s in integer steps"
    - "j = 3/2 only — angular momenta always add to their maximum"
    - "j = 1/2, 1, and 3/2 — all half-integer and integer values between |l − s| and l + s"
  answer: 1
  explanation: "The rule is |j₁ − j₂| ≤ j ≤ j₁ + j₂ in integer steps. With l = 1 and s = 1/2: |1 − 1/2| = 1/2 and 1 + 1/2 = 3/2. The allowed values are j = 1/2 and j = 3/2 — exactly two values, separated by 1. The total number of states is (2×1/2+1) + (2×3/2+1) = 2 + 4 = 6, which equals (2l+1)(2s+1) = 3 × 2 = 6. The intermediate values (j = 1, j = 0) are not allowed here because they don't fit the integer-step rule starting from |l − s| = 1/2."

- question: "For two spin-1/2 particles, the uncoupled state |↑↓⟩ (particle 1 up, particle 2 down) is not an eigenstate of J². A measurement of J² on this state would:"
  type: multiple-choice
  options:
    - "Always give j = 1, since the spins are anti-aligned and the triplet includes an m = 0 state"
    - "Always give j = 0, since the spins cancel"
    - "Give j = 1 or j = 0 with certain probabilities, because |↑↓⟩ is a superposition of triplet and singlet states"
    - "Be undefined, because |↑↓⟩ is not a valid quantum state for coupled angular momenta"
  answer: 2
  explanation: "|↑↓⟩ can be written as a superposition of the triplet m=0 state (|↑↓⟩ + |↓↑⟩)/√2 and the singlet state (|↑↓⟩ − |↓↑⟩)/√2: specifically, |↑↓⟩ = [(triplet m=0) + (singlet)]/√2. Measuring J² collapses this superposition, yielding j = 1 with probability 1/2 and j = 0 with probability 1/2. This illustrates why the uncoupled basis is inconvenient when J² matters — neither |↑↓⟩ nor |↓↑⟩ is a total-angular-momentum eigenstate."

- question: "When two angular momenta j₁ and j₂ are coupled, the total number of states in the coupled basis equals (2j₁+1)(2j₂+1), the same dimension as the uncoupled basis."
  type: true-false
  answer: true
  explanation: "True. The coupled and uncoupled bases are two different orthonormal bases for the same Hilbert space — they span the same space. The dimension must be preserved. You can verify: summing (2j+1) over j from |j₁−j₂| to j₁+j₂ in integer steps always gives (2j₁+1)(2j₂+1). For the two spin-1/2 case: (2×1+1) + (2×0+1) = 3 + 1 = 4 = 2×2. The Clebsch-Gordan transformation is unitary precisely because it maps between two orthonormal bases of the same space."

- question: "In the coupled basis |j, m⟩, the total z-projection m is no longer a good quantum number — it becomes indefinite because coupling mixes states with different m₁ and m₂ values."
  type: true-false
  answer: false
  explanation: "False. The total z-projection m = m₁ + m₂ remains a good quantum number in both bases. In the uncoupled basis, m₁ and m₂ are individually definite, so their sum is definite. In the coupled basis, m is still definite as the eigenvalue of J_z = J₁z + J₂z. What becomes indefinite in the uncoupled basis is J² (the total magnitude). What the coupling accomplishes is making J² definite while keeping m definite — switching from (j₁, m₁, j₂, m₂) as quantum numbers to (j₁, j₂, j, m)."

- question: "Why is the coupled basis |j, m⟩ more physically useful than the uncoupled basis |j₁m₁⟩|j₂m₂⟩ for a hydrogen atom electron subject to spin-orbit coupling?"
  type: short-answer
  answer: "Spin-orbit coupling adds a term to the Hamiltonian proportional to L·S, which equals (J² − L² − S²)/2. This operator is diagonal in the coupled basis |j, m⟩ — states of definite j are energy eigenstates of the spin-orbit perturbation — but mixes states in the uncoupled basis. The energy shift depends on j: the j = l+1/2 and j = l−1/2 levels are split by an amount proportional to the spin-orbit coupling constant. Calculating this splitting requires using the coupled basis where J² is a good quantum number. Spectroscopic selection rules (which transitions are allowed) are also written in terms of j rather than l and s separately."
  explanation: "More generally, any perturbation that depends on total angular momentum (spin-orbit coupling, hyperfine interaction, response to external fields in certain regimes) is most naturally analyzed in the coupled basis. The uncoupled basis is simpler to construct, but the coupled basis reveals the physical symmetry of the problem."
```

## Explainer

You know from orbital angular momentum that a particle with quantum number l can have z-projections m ranging from −l to +l in integer steps, giving 2l+1 states. You also know that spin-1/2 particles have two states: m_s = +1/2 or −1/2. The question this topic addresses is: when a system has *two* sources of angular momentum simultaneously — say, the orbital motion of an electron around a nucleus and its intrinsic spin — what are the allowed values of the *total* angular momentum, and how do you describe the combined quantum state?

The **uncoupled basis** is the natural starting point. You label states by |j₁, m₁⟩|j₂, m₂⟩, specifying each angular momentum's projection independently. The total z-projection m = m₁ + m₂ is always definite in this basis. But the total magnitude J² is generally not — these states are not eigenstates of J². The **coupled basis** |j, m⟩ reorganizes the same Hilbert space so that both J² and J_z are sharp. The allowed values of j run from |j₁ − j₂| up to j₁ + j₂ in integer steps. You can verify the state counts match: Σ(2j+1) over the coupled values equals (2j₁+1)(2j₂+1), the total dimension.

A concrete example: couple spin-1/2 (j₁ = 1/2) with spin-1/2 (j₂ = 1/2). The uncoupled states are |↑↑⟩, |↑↓⟩, |↓↑⟩, |↓↓⟩ — four states. The coupled basis gives j = 1 (three states: m = +1, 0, −1) and j = 0 (one state: m = 0). The j = 1 states form the **triplet** and the j = 0 state is the **singlet**. The singlet is the antisymmetric combination (|↑↓⟩ − |↓↑⟩)/√2, which you may recognize as the spin state of two electrons in a helium ground state or an entangled Bell state. The triplet states are symmetric combinations.

The numbers that convert between these two bases are the **Clebsch-Gordan coefficients** ⟨j₁m₁; j₂m₂ | jm⟩. They are tabulated and encode the full transformation. Physically, coupling matters whenever you need to know how a system responds to a perturbation that depends on total angular momentum (like spin-orbit coupling, which shifts atomic energy levels depending on j = l + s). Spectroscopic selection rules — which transitions are allowed by the emission or absorption of a photon — are written in terms of j, not the individual l and s separately. This is why addition of angular momenta is not just a mathematical exercise but the language in which atomic spectra are organized.
