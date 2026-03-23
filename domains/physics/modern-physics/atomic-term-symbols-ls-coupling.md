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
status: validated
---

# Atomic Term Symbols and LS Coupling Scheme

## Core Idea
Term symbols ²ˢ⁺¹Lⱼ encode the electronic configuration of an atom: 2S+1 is the multiplicity (spin degeneracy), L is the total orbital angular momentum (S, P, D, F, ...), and J is the total angular momentum. In LS coupling, individual electron spins and orbital momenta couple to form L and S, which then couple via spin-orbit interaction to form J. Term symbols predict level structure and allowed transitions.

## How It's Best Learned
Derive term symbols for simple atoms (He, Li, C) using Russell-Saunders rules. Predict J-levels and their relative energies. Use term symbols to apply selection rules (ΔL = 0,±1, ΔS = 0, ΔJ = 0,±1) for allowed transitions.

## Common Misconceptions
Term symbols apply to the whole atom, not individual electrons (electron labels are not meaningful in the quantum case). The ordering of J-levels (normal vs inverted multiplicity) requires knowledge of whether shells are less than or more than half full.

## Questions

```yaml
- question: "Carbon's ground state is represented as ³P₀. What does the superscript '3' signify?"
  type: multiple-choice
  options:
    - "The principal quantum number n = 3 of the outermost electrons"
    - "The spin multiplicity 2S+1 = 3, meaning total spin S = 1 (two electrons with parallel spins)"
    - "The number of electrons in the 2p subshell"
    - "The total angular momentum quantum number J = 3"
  answer: 1
  explanation: "The superscript in ²ˢ⁺¹Lⱼ is the spin multiplicity 2S+1. For ³P₀, 2S+1 = 3 means S = 1 — two electrons with aligned (parallel) spins. The letter P gives L = 1 (total orbital angular momentum), and the subscript 0 gives J = 0. Note that J = 0 is the lowest J level for ³P because carbon's 2p² subshell is less than half full (normal multiplicity, lowest J is lowest energy)."

- question: "Which of the following spectral transitions is forbidden by the electric dipole selection rules for LS-coupled atoms?"
  type: multiple-choice
  options:
    - "³P₁ → ³D₂ (ΔL = 1, ΔS = 0, ΔJ = 1)"
    - "¹S₀ → ¹P₁ (ΔL = 1, ΔS = 0, ΔJ = 1)"
    - "³P₁ → ¹S₀ (ΔS = −1)"
    - "²P₁/₂ → ²S₁/₂ (ΔL = 1, ΔS = 0, ΔJ = 1)"
  answer: 2
  explanation: "The selection rule ΔS = 0 requires that the total spin quantum number cannot change in an allowed electric dipole transition. In ³P₁ → ¹S₀, the transition goes from S = 1 to S = 0, so ΔS = −1, violating this rule. This is why singlet-triplet transitions are forbidden (or very weak) in LS coupling. The other options all have ΔS = 0 and satisfy ΔL = ±1, ΔJ = 0 or ±1, making them allowed."

- question: "Term symbols like ³P₀ describe the quantum state of individual electrons within an atom."
  type: true-false
  answer: false
  explanation: "Term symbols describe the state of the atom as a whole, not individual electrons. The letters and numbers (L, S, J) refer to the *total* orbital angular momentum, *total* spin, and *total* angular momentum resulting from the combined contributions of all electrons in the atom. This is a key conceptual point of LS coupling: individual electron labels lose meaning — what matters is the collective quantum state."

- question: "For an atom whose outermost subshell is more than half full, the J-level with the highest value of J lies lowest in energy (inverted multiplet rule)."
  type: true-false
  answer: true
  explanation: "Correct — this is the inverted multiplet rule. For shells less than half full, the lowest J lies lowest (normal multiplet, as in carbon's ³P₀ ground state). For shells more than half full, the highest J lies lowest in energy. This arises from the sign of the spin-orbit coupling constant, which flips between less-than-half-full and more-than-half-full subshells. For example, oxygen (2p⁴, more than half full) has the ³P₂ level as its ground state."

- question: "Why do only the electrons in incompletely filled subshells matter when determining the term symbol of an atom?"
  type: short-answer
  answer: "Completely filled subshells (like 1s², 2s², 2p⁶) have all magnetic quantum numbers m_l and spin projections m_s symmetrically occupied. Their contributions to total orbital angular momentum L and total spin S cancel exactly: the vector sum of all l⃗ᵢ and s⃗ᵢ is zero. Only electrons in partially filled subshells have unbalanced angular momenta that contribute to L and S — so the term symbol is determined entirely by the incomplete subshell configuration."
  explanation: "This is why the term symbol for carbon (1s²2s²2p²) depends only on the two 2p electrons: the filled 1s² and 2s² subshells contribute L = 0 and S = 0. The same logic applies across the periodic table: noble gas core electrons are spectroscopically inert, and the term symbol reflects only the valence electrons in partially filled subshells."
```

## Explainer

You already know that each electron in an atom is assigned four quantum numbers: the principal quantum number n, the orbital angular momentum quantum number l (0, 1, 2, 3 → s, p, d, f), the magnetic quantum number m_l (ranging from −l to +l), and the spin quantum number m_s (±1/2). The Pauli exclusion principle tells you no two electrons in the same atom can share all four. **LS coupling** (also called Russell-Saunders coupling) goes one step further: it combines all the electrons' individual angular momenta into collective quantum numbers that characterize the atom as a whole.

In LS coupling, the individual orbital momenta l⃗ᵢ couple together to give a total orbital angular momentum L⃗ = Σ l⃗ᵢ, with quantum number L = 0, 1, 2, 3, ... (labeled S, P, D, F, ... following the same letter convention as single-electron states). Simultaneously, the individual spins s⃗ᵢ couple to give total spin S⃗ = Σ s⃗ᵢ, with quantum number S = 0, 1/2, 1, 3/2, ... The **multiplicity** 2S+1 counts the number of distinct m_S values and gives the number of levels the spin degeneracy splits into. Finally, L⃗ and S⃗ couple via spin-orbit interaction to give the total angular momentum J⃗, with J ranging from |L − S| to L + S in integer steps. The **term symbol** ²ˢ⁺¹Lⱼ compactly encodes all three: multiplicity, total orbital angular momentum, and total angular momentum.

To build intuition, consider carbon (1s² 2s² 2p²). The closed 1s² and 2s² subshells contribute L = 0 and S = 0, so only the two 2p electrons matter. Each has l = 1, so L can be 0, 1, or 2. Each has s = 1/2, so S can be 0 or 1. But not all combinations are allowed — the Pauli exclusion principle restricts which (m_l, m_s) pairs can both be occupied. Applying the rules carefully yields the terms ³P (the ground term), ¹D, and ¹S in order of energy. The ³P term (S = 1, L = 1) further splits into ³P₀, ³P₁, and ³P₂ as J takes values 0, 1, 2. For shells less than half-full, the lowest J level lies lowest in energy (normal multiplicity); for shells more than half-full, the highest J is lowest.

Term symbols are indispensable for spectroscopy because **selection rules** for dipole-allowed transitions are stated in terms of them: ΔL = 0 or ±1, ΔS = 0, ΔJ = 0 or ±1 (but J = 0 → J = 0 is forbidden). A transition from ³P₁ to ¹S₀ is forbidden by ΔS = 0; a transition from ³P₂ to ³D₃ is allowed. These rules explain why certain spectral lines appear in atomic spectra and others are absent — they are the quantum-mechanical statement that the atom and emitted photon must together conserve angular momentum. Mastering term symbols transforms spectral line tables from empirical catalogs into a deducible consequence of quantum mechanics.
