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
stage: advanced
status: draft
---

# Bogoliubov Transformation

## Core Idea
The Bogoliubov transformation is a canonical transformation mixing creation and annihilation operators that diagonalizes quadratic Hamiltonians with off-diagonal terms. It reveals the quasiparticle spectrum and is essential for understanding superfluids and superconductors, where particle and hole excitations are mixed by the condensate.

## Explainer

You know from creation and annihilation operators that a free bosonic system can be described by a Hamiltonian of the form H = Σ_k ε_k a†_k a_k — a diagonal sum of occupation number terms. Each mode k has energy ε_k and evolves independently. But real systems have interactions. In a weakly interacting Bose gas near its condensation temperature, interactions scatter pairs of particles: two particles with momenta +k and −k can be scattered from or into the k = 0 condensate, generating terms like a†_k a†_{-k} and a_k a_{-k} in the Hamiltonian. These off-diagonal terms couple creation and annihilation operators and prevent simple diagonalization.

The **Bogoliubov transformation** handles this by defining new operators α_k = u_k a_k + v_k a†_{-k}, where u_k and v_k are real coefficients satisfying u_k² − v_k² = 1 (which preserves the bosonic commutation relations, analogous to the canonical condition in classical mechanics). By choosing u_k and v_k appropriately, the transformed Hamiltonian H becomes Σ_k E_k α†_k α_k — diagonal in the new operators. The α†_k and α_k are **quasiparticle** creation and annihilation operators. The quasiparticles are not the original atoms but quantum superpositions of a particle at +k and a "hole" at −k (or vice versa), mixed together by the condensate.

The new dispersion relation E_k tells you the energy of these quasiparticles. For the interacting Bose gas, Bogoliubov found E_k = √(ε_k(ε_k + 2gn)), where g measures interaction strength and n is the condensate density. At high k (short wavelengths), E_k ≈ ε_k — the quasiparticles look like free particles. But at low k, E_k ≈ ck where c = √(gn/m) is a velocity: the quasiparticles are **phonons**, sound-like collective modes with linear dispersion. This linear dispersion at low energies is the microscopic explanation for **superfluidity** — Landau's criterion says a system is superfluid if its quasiparticle spectrum grows linearly at low momentum, because subsonic flow cannot create quasiparticles and therefore cannot dissipate energy.

The same mathematical structure appears in superconductors (BCS theory), where electrons near the Fermi surface are paired by phonon-mediated interactions and the Bogoliubov transformation mixes electron and hole states to produce **Bogoliubons** — the fermionic analogue. In that context u_k² − v_k² = 1 is replaced by u_k² + v_k² = 1 (the fermionic version preserving anticommutation relations). The Bogoliubov transformation is thus the canonical tool for any system where the ground state is a coherent mixture of particles and holes — a mathematical scalpel that cuts through quadratic complexity to reveal the true elementary excitations.
