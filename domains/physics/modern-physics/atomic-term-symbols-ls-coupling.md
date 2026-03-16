---
id: atomic-term-symbols-ls-coupling
title: Atomic Term Symbols and LS Coupling Scheme
domain: physics
course: modern-physics
prerequisites:
- id: principal-angular-magnetic-quantum-numbers
  type: hard
- id: pauli-exclusion-principle
  type: hard
tags:
- term-symbols
- ls-coupling
- atomic-structure
stage: advanced
status: draft
---

# Atomic Term Symbols and LS Coupling Scheme

## Core Idea
Term symbols ²ˢ⁺¹Lⱼ encode the electronic configuration of an atom: 2S+1 is the multiplicity (spin degeneracy), L is the total orbital angular momentum (S, P, D, F, ...), and J is the total angular momentum. In LS coupling, individual electron spins and orbital momenta couple to form L and S, which then couple via spin-orbit interaction to form J. Term symbols predict level structure and allowed transitions.

## How It's Best Learned
Derive term symbols for simple atoms (He, Li, C) using Russell-Saunders rules. Predict J-levels and their relative energies. Use term symbols to apply selection rules (ΔL = 0,±1, ΔS = 0, ΔJ = 0,±1) for allowed transitions.

## Common Misconceptions
Term symbols apply to the whole atom, not individual electrons (electron labels are not meaningful in the quantum case). The ordering of J-levels (normal vs inverted multiplicity) requires knowledge of whether shells are less than or more than half full.

## Explainer

You already know that each electron in an atom is assigned four quantum numbers: the principal quantum number n, the orbital angular momentum quantum number l (0, 1, 2, 3 → s, p, d, f), the magnetic quantum number m_l (ranging from −l to +l), and the spin quantum number m_s (±1/2). The Pauli exclusion principle tells you no two electrons in the same atom can share all four. **LS coupling** (also called Russell-Saunders coupling) goes one step further: it combines all the electrons' individual angular momenta into collective quantum numbers that characterize the atom as a whole.

In LS coupling, the individual orbital momenta l⃗ᵢ couple together to give a total orbital angular momentum L⃗ = Σ l⃗ᵢ, with quantum number L = 0, 1, 2, 3, ... (labeled S, P, D, F, ... following the same letter convention as single-electron states). Simultaneously, the individual spins s⃗ᵢ couple to give total spin S⃗ = Σ s⃗ᵢ, with quantum number S = 0, 1/2, 1, 3/2, ... The **multiplicity** 2S+1 counts the number of distinct m_S values and gives the number of levels the spin degeneracy splits into. Finally, L⃗ and S⃗ couple via spin-orbit interaction to give the total angular momentum J⃗, with J ranging from |L − S| to L + S in integer steps. The **term symbol** ²ˢ⁺¹Lⱼ compactly encodes all three: multiplicity, total orbital angular momentum, and total angular momentum.

To build intuition, consider carbon (1s² 2s² 2p²). The closed 1s² and 2s² subshells contribute L = 0 and S = 0, so only the two 2p electrons matter. Each has l = 1, so L can be 0, 1, or 2. Each has s = 1/2, so S can be 0 or 1. But not all combinations are allowed — the Pauli exclusion principle restricts which (m_l, m_s) pairs can both be occupied. Applying the rules carefully yields the terms ³P (the ground term), ¹D, and ¹S in order of energy. The ³P term (S = 1, L = 1) further splits into ³P₀, ³P₁, and ³P₂ as J takes values 0, 1, 2. For shells less than half-full, the lowest J level lies lowest in energy (normal multiplicity); for shells more than half-full, the highest J is lowest.

Term symbols are indispensable for spectroscopy because **selection rules** for dipole-allowed transitions are stated in terms of them: ΔL = 0 or ±1, ΔS = 0, ΔJ = 0 or ±1 (but J = 0 → J = 0 is forbidden). A transition from ³P₁ to ¹S₀ is forbidden by ΔS = 0; a transition from ³P₂ to ³D₃ is allowed. These rules explain why certain spectral lines appear in atomic spectra and others are absent — they are the quantum-mechanical statement that the atom and emitted photon must together conserve angular momentum. Mastering term symbols transforms spectral line tables from empirical catalogs into a deducible consequence of quantum mechanics.
