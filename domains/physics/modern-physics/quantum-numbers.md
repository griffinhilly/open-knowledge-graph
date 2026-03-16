---
id: quantum-numbers
title: Quantum Numbers
domain: physics
course: modern-physics
prerequisites:
- id: bohr-model
  type: hard
- id: schrodinger-equation-intro
  type: soft
- id: particle-in-a-box
  type: soft
builds-toward:
- atomic-orbitals
- spin-quantum-number
tags:
- quantum
- hydrogen
- principal
- angular-momentum
- magnetic
- quantum-numbers
stage: advanced
status: validated
---
# Quantum Numbers

## Core Idea
The full quantum mechanical treatment of the hydrogen atom yields four quantum numbers. The principal quantum number n = 1, 2, 3, … determines the energy level. The orbital angular momentum quantum number ℓ = 0, 1, …, n−1 determines the shape of the orbital. The magnetic quantum number m_ℓ = −ℓ, …, +ℓ determines the orientation of the orbital in a magnetic field. The spin quantum number m_s = ±½ describes the intrinsic angular momentum of the electron. Together they uniquely label each quantum state of a hydrogen electron.

## How It's Best Learned
Build up from Bohr (n only) to include ℓ (angular momentum quantization from solving the 3D Schrödinger equation) and m_ℓ (projection). Introduce spin separately as an experimental fact (Stern–Gerlach) before showing it requires a relativistic treatment (Dirac equation) for its full explanation.

## Common Misconceptions
- n alone determines everything about the state — n gives the energy (for hydrogen), but ℓ and m_ℓ specify the orbital shape and orientation; all four numbers are needed to specify the state.
- ℓ can equal n — ℓ ranges from 0 to n−1; ℓ = n is not allowed.

## Questions

```yaml
- question: "For an electron in the n = 3 shell of hydrogen, how many distinct values of ℓ are allowed?"
  type: multiple-choice
  options: ["1 (only ℓ = 0)", "2 (ℓ = 0 and 1)", "3 (ℓ = 0, 1, and 2)", "4 (ℓ = 0, 1, 2, and 3)"]
  answer: 2
  explanation: "ℓ ranges from 0 to n−1 inclusive. For n = 3, the allowed values are ℓ = 0, 1, 2 — three values. The common error is allowing ℓ = n = 3, but the constraint is ℓ ≤ n−1. Each value of ℓ corresponds to a subshell: s (ℓ=0), p (ℓ=1), d (ℓ=2)."

- question: "In hydrogen, knowing the principal quantum number n is sufficient to completely specify the electron's quantum state."
  type: true-false
  answer: false
  explanation: "n determines the energy level of hydrogen, but specifying the quantum state requires all four quantum numbers: n, ℓ, m_ℓ, and m_s. For n = 2 alone, there are 8 distinct states: the ℓ=0 subshell has 1 orbital × 2 spin states = 2; the ℓ=1 subshell has 3 orientations (m_ℓ = −1, 0, +1) × 2 spin states = 6. Total: 8 states all sharing the same energy in hydrogen."

- question: "Why did the Bohr model need to be replaced by the full quantum mechanical treatment, even though it gives the correct energy levels for hydrogen?"
  type: short-answer
  answer: "The Bohr model gives correct energies but cannot explain orbital shapes, the degeneracy structure of subshells, fine structure of spectral lines, or multi-electron atoms. The full treatment with ℓ, m_ℓ, and m_s accounts for these and provides a consistent framework for all atoms."
  explanation: "Bohr quantized angular momentum by fiat (L = nℏ) without a physical justification, predicted only circular orbits, and failed for any atom beyond hydrogen. The wave-mechanical treatment solves the Schrödinger equation in 3D, from which ℓ and m_ℓ emerge naturally and explain orbital shapes and the Zeeman effect. Spin (m_s) is needed for the Pauli exclusion principle and the periodic table."
```

## Explainer

The Bohr model gave you the principal quantum number n to label energy levels, and that was enough to explain hydrogen's emission spectrum. But when the full Schrödinger equation is solved in three dimensions, three more quantum numbers emerge naturally from the mathematics — not as assumptions, but as requirements for wave solutions to exist. Together, the four quantum numbers form a complete label for any quantum state of a hydrogen electron.

The orbital angular momentum quantum number ℓ comes from the angular part of the wave equation. It determines the shape of the orbital: ℓ = 0 gives a spherically symmetric s-orbital; ℓ = 1 gives the dumbbell-shaped p-orbitals; ℓ = 2 gives the more complex d-orbitals. The constraint ℓ = 0, 1, …, n−1 is not arbitrary — it is the mathematical condition for the wave solution to remain finite as you move away from the nucleus. You cannot have a d-orbital (ℓ = 2) in the n = 2 shell because no valid wavefunction exists for that combination.

The magnetic quantum number m_ℓ distinguishes among orbitals of the same shape but different orientations in space. For ℓ = 1, the values m_ℓ = −1, 0, +1 correspond to the three p-orbitals (conventionally labeled px, py, pz). In free space these three orientations all have the same energy — they are degenerate. Apply an external magnetic field and the degeneracy breaks: the energy levels split, producing additional lines in the spectrum. This splitting (the Zeeman effect) is where m_ℓ gets its name and how it was experimentally confirmed.

Spin (m_s = ±½) does not emerge from the non-relativistic Schrödinger equation at all — it must be added as an experimental fact, first demonstrated by the Stern-Gerlach experiment, and fully explained only by Dirac's relativistic quantum theory. The electron's spin is an intrinsic angular momentum with no classical analog. The half-integer values ±½ are especially notable: classical angular momenta must be integers, but spin obeys different rules. The practical consequence is that each orbital (specified by n, ℓ, m_ℓ) can be occupied by at most two electrons with opposite spins — the Pauli exclusion principle.

The total number of distinct states at principal level n is 2n², which you can verify by counting: for each ℓ from 0 to n−1, there are 2ℓ+1 values of m_ℓ, and each state is doubled by spin. Summing 2(2ℓ+1) over ℓ = 0 to n−1 gives 2n². This counting directly explains the shell structure of the periodic table: 2 electrons in the first shell (n=1), 8 in the second (n=2), 18 in the third (n=3). The four quantum numbers are not just a labeling scheme — they are the mathematical foundation of all of chemistry.
