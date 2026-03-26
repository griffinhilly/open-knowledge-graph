---
id: bogoliubov-transformation
title: Bogoliubov Transformation
domain: physics
course: statistical-mechanics
prerequisites:
- id: collective-excitations-phonons
  type: hard
- id: creation-annihilation-operators
  type: hard
builds-toward:
- superfluidity-bosons
tags:
- diagonalization
- quasiparticles
- interactions
stage: expert
status: validated
---

# Bogoliubov Transformation

## Core Idea
The Bogoliubov transformation is a canonical transformation mixing creation and annihilation operators that diagonalizes quadratic Hamiltonians with off-diagonal terms. It reveals the quasiparticle spectrum and is essential for understanding superfluids and superconductors, where particle and hole excitations are mixed by the condensate.

## Questions

```yaml
- question: "Why does the interacting Bose gas have phonon-like quasiparticles (linear dispersion E_k ≈ ck) at low momentum, instead of the quadratic dispersion of free particles?"
  type: multiple-choice
  options:
    - "Interactions cause the effective mass of particles to increase, which linearizes the dispersion at low k"
    - "The Bogoliubov transformation mixes a†_{-k} into the definition of quasiparticles; at low k the hole-mixing term dominates and transforms the quadratic free-particle dispersion into linear phonon-like behavior"
    - "The condensate provides a background potential that acts as a restoring force, exactly like a harmonic oscillator, producing linear dispersion"
    - "Low-momentum particles cannot be distinguished from their surrounding condensate and therefore propagate as sound waves by the uncertainty principle"
  answer: 1
  explanation: "The Bogoliubov dispersion E_k = √(ε_k(ε_k + 2gn)) interpolates between two regimes. At high k, ε_k ≫ 2gn, so E_k ≈ ε_k = ℏ²k²/2m — free-particle quadratic dispersion. At low k, ε_k ≪ 2gn, so E_k ≈ √(2gnε_k) ∝ k — linear dispersion. The linear behavior emerges because the off-diagonal coupling (∝ 2gn) mixes particle and hole modes in a way that fundamentally restructures the low-energy spectrum. This is not an effective-mass renormalization (option A) or a quantum uncertainty effect (option D) — it is a qualitative change in the nature of the excitations due to the mixing."

- question: "What physical operation does the Bogoliubov transformation perform, and what is the evidence that the new operators α_k describe genuinely new physical excitations?"
  type: multiple-choice
  options:
    - "It rescales the energy levels of original atoms to account for interactions, keeping the same eigenstates but adjusting their energies"
    - "It defines new operators α_k = u_k a_k + v_k a†_{-k} that diagonalize the Hamiltonian; the eigenstates of H are states with definite quasiparticle number, not definite atom number"
    - "It projects out the condensate contribution to the Hamiltonian, leaving a residual Hamiltonian for non-condensate particles"
    - "It performs a Legendre transform to switch from a particle description to a field description of the system"
  answer: 1
  explanation: "The Bogoliubov transformation rotates the operator basis from bare particles (a_k, a†_k) to quasiparticles (α_k, α†_k). The transformed Hamiltonian H = Σ_k E_k α†_k α_k is diagonal in quasiparticle number — meaning states of definite quasiparticle number are energy eigenstates. But states of definite quasiparticle number are *not* states of definite atom number, because α†_k = u_k a†_k + v_k a_{-k} creates a superposition of a particle at +k and a hole at −k. The physical evidence is the modified dispersion E_k — measuring this experimentally (e.g., via neutron scattering in superfluid helium) confirms these are distinct excitations, not simply dressed bare particles."

- question: "The quasiparticles produced by the Bogoliubov transformation are quantum superpositions of a particle with momentum +k and a particle missing from (a hole at) momentum −k, rather than simply modified versions of the original atoms."
  type: true-false
  answer: true
  explanation: "The quasiparticle creation operator is α†_k = u_k a†_k + v_k a_{-k}. Acting with a†_k creates a particle at +k; acting with a_{-k} annihilates a particle at −k, which is equivalent to creating a 'hole' at −k. The quasiparticle is a coherent quantum superposition of these two processes, mixed by the condensate-mediated interaction. This mixing has a physical interpretation: the condensate is a macroscopic quantum object that can absorb or emit pairs (k, −k) through the interaction terms a†_k a†_{-k} and a_k a_{-k}, so single-particle excitations inevitably acquire a hole component. The quasiparticle is the appropriate description of what actually propagates through the superfluid."

- question: "The Bogoliubov transformation is required whenever a quantum many-body system has interactions, because most interacting Hamiltonians need to be diagonalized via this method."
  type: true-false
  answer: false
  explanation: "The Bogoliubov transformation is specifically designed for quadratic Hamiltonians — those with terms at most bilinear in creation and annihilation operators, including off-diagonal pairing terms like a†_k a†_{-k} and a_k a_{-k}. These arise when interactions are treated at the mean-field level (replacing the condensate operators by c-numbers). General interactions produce higher-order terms (a†a†aa, etc.) that the Bogoliubov transformation cannot diagonalize. For those systems, other methods — perturbation theory, renormalization group, diagrammatic techniques — are needed. The Bogoliubov transformation is powerful precisely because pairing terms arise naturally in superfluids and superconductors, not because it is a universal tool."

- question: "Why is the linear dispersion E_k ≈ ck at low k, produced by the Bogoliubov transformation, the key to explaining superfluidity? What would happen if the dispersion were quadratic (like free particles) instead?"
  type: short-answer
  answer: "Landau's criterion for superfluidity states that a system is superfluid if its quasiparticle dispersion grows at least linearly at low momentum. The reason: a uniform flow of the superfluid at velocity v can only be slowed by creating quasiparticles. The minimum energy cost to create a quasiparticle in the lab frame is E_k − ℏkv. For linear dispersion E_k = ck, this is (c − v)ℏk, which is positive as long as v < c. So subsonic flow cannot create quasiparticles and cannot dissipate energy — giving frictionless (superfluid) flow. If dispersion were quadratic (E_k = ℏ²k²/2m), the minimum ratio E_k/(ℏk) → 0 as k → 0, meaning even infinitesimally slow flow could create quasiparticles. The Landau criterion would be violated and there would be no superfluidity."
  explanation: "The key insight is that the linear dispersion creates an 'energy gap' against quasiparticle creation at low velocities. The slope of the dispersion at k = 0 — the speed of sound c = √(gn/m) — is the critical velocity below which superfluid flow is dissipation-free. This microscopic explanation of superfluidity is one of the great results of quantum many-body theory: the Bogoliubov transformation translates the quartic interaction term (via mean-field approximation) into a modified dispersion relation, and that dispersion relation directly controls the macroscopic transport property of superfluidity."
```

## Explainer

You know from creation and annihilation operators that a free bosonic system can be described by a Hamiltonian of the form H = Σ_k ε_k a†_k a_k — a diagonal sum of occupation number terms. Each mode k has energy ε_k and evolves independently. But real systems have interactions. In a weakly interacting Bose gas near its condensation temperature, interactions scatter pairs of particles: two particles with momenta +k and −k can be scattered from or into the k = 0 condensate, generating terms like a†_k a†_{-k} and a_k a_{-k} in the Hamiltonian. These off-diagonal terms couple creation and annihilation operators and prevent simple diagonalization.

The **Bogoliubov transformation** handles this by defining new operators α_k = u_k a_k + v_k a†_{-k}, where u_k and v_k are real coefficients satisfying u_k² − v_k² = 1 (which preserves the bosonic commutation relations, analogous to the canonical condition in classical mechanics). By choosing u_k and v_k appropriately, the transformed Hamiltonian H becomes Σ_k E_k α†_k α_k — diagonal in the new operators. The α†_k and α_k are **quasiparticle** creation and annihilation operators. The quasiparticles are not the original atoms but quantum superpositions of a particle at +k and a "hole" at −k (or vice versa), mixed together by the condensate.

The new dispersion relation E_k tells you the energy of these quasiparticles. For the interacting Bose gas, Bogoliubov found E_k = √(ε_k(ε_k + 2gn)), where g measures interaction strength and n is the condensate density. At high k (short wavelengths), E_k ≈ ε_k — the quasiparticles look like free particles. But at low k, E_k ≈ ck where c = √(gn/m) is a velocity: the quasiparticles are **phonons**, sound-like collective modes with linear dispersion. This linear dispersion at low energies is the microscopic explanation for **superfluidity** — Landau's criterion says a system is superfluid if its quasiparticle spectrum grows linearly at low momentum, because subsonic flow cannot create quasiparticles and therefore cannot dissipate energy.

The same mathematical structure appears in superconductors (BCS theory), where electrons near the Fermi surface are paired by phonon-mediated interactions and the Bogoliubov transformation mixes electron and hole states to produce **Bogoliubons** — the fermionic analogue. In that context u_k² − v_k² = 1 is replaced by u_k² + v_k² = 1 (the fermionic version preserving anticommutation relations). The Bogoliubov transformation is thus the canonical tool for any system where the ground state is a coherent mixture of particles and holes — a mathematical scalpel that cuts through quadratic complexity to reveal the true elementary excitations.
