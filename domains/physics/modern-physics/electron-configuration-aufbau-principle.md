---
id: electron-configuration-aufbau-principle
title: Electron Configuration and the Aufbau Principle
domain: physics
course: modern-physics
prerequisites:
- id: pauli-exclusion-antisymmetry
  type: hard
builds-toward:
- periodic-table-electronic-structure
tags:
- quantum
- atoms
- configuration
stage: advanced
status: draft
---

# Electron Configuration and the Aufbau Principle

## Core Idea
Electrons fill atomic orbitals in order of increasing energy (aufbau = build-up). Each orbital (n, ℓ, mℓ) holds at most 2 electrons with opposite spins (spin-up and spin-down). The filling order is 1s, 2s, 2p, 3s, 3p, 4s, 3d, ... determined by effective nuclear charge and electron-electron repulsion. Shell and subshell structure derives from quantum number constraints.

## Explainer

From your study of the Pauli exclusion principle, you know that no two electrons in an atom can occupy the same quantum state — and for electrons this means no two can share the same set of all four quantum numbers (n, ℓ, mₗ, mₛ). The **Aufbau principle** (German: "building up") uses this constraint to explain how multi-electron atoms are constructed: you add electrons one at a time, each going into the lowest available energy state not yet forbidden by Pauli exclusion.

Each electron's state is labeled by four quantum numbers. The **principal quantum number** n = 1, 2, 3, ... controls the shell and sets the coarse energy scale (higher n = higher energy, larger orbital). The **angular momentum quantum number** ℓ = 0, 1, ..., n−1 labels subshells by their orbital shape (s, p, d, f for ℓ = 0,1,2,3). The **magnetic quantum number** mₗ = −ℓ, ..., +ℓ gives the orbital orientation — there are 2ℓ+1 orbitals in each subshell. The **spin quantum number** mₛ = ±½ allows two electrons per orbital. Counting up: an s subshell holds 2 electrons, a p subshell 6, a d subshell 10, an f subshell 14.

The energy ordering is almost, but not exactly, by n alone. For hydrogen, all subshells with the same n are degenerate. For multi-electron atoms, electron-electron repulsion and **effective nuclear charge** (the net positive charge experienced by an outer electron, shielded by inner electrons) split the subshell energies. The rule of thumb is the (n + ℓ) rule: lower (n + ℓ) fills first; when equal, lower n fills first. This gives the sequence 1s, 2s, 2p, 3s, 3p, **4s, 3d**, 4p, **5s, 4d**, ... The crossing of 4s before 3d is the most important consequence: electrons prefer 4s over 3d because 4s has n + ℓ = 4 + 0 = 4 while 3d has 3 + 2 = 5.

The **valence electrons** — those in the outermost shell — determine virtually all of an atom's chemical behavior, from what bonds it forms to how it reacts. Elements in the same column of the periodic table have the same valence electron configuration (same ℓ and number of electrons in the outermost subshell), which is why they show similar chemistry. Sodium and potassium are both [noble gas] ns¹; chlorine and bromine are both [noble gas] ns²np⁵. The periodicity of the table is a direct consequence of the Aufbau filling order: each new row begins when electrons start filling a new principal quantum number, and the block structure (s-block, p-block, d-block, f-block) reflects which subshell is being filled across that row.
