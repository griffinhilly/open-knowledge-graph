---
id: periodic-table-filling-orbitals
title: Periodic Table and Orbital Filling Rules
domain: physics
course: modern-physics
prerequisites:
- id: quantum-numbers-spherical-harmonics
  type: hard
- id: pauli-exclusion-principle
  type: hard
builds-toward:
- photon-absorption-emission
tags:
- atomic-physics
- chemistry
stage: advanced
status: draft
---

# Periodic Table and Orbital Filling Rules

## Core Idea
The periodic table emerges from quantum mechanics: the Pauli exclusion principle limits occupation of orbitals (2 electrons per orbital: opposite spins). The aufbau principle fills orbitals in order of increasing energy, leading to subshells (2s² in n=2 gives helium's period structure, 3d¹⁰ fills in transition metals). Element properties repeat periodically as valence electron configurations repeat, explaining chemical periodicity from first principles.

## How It's Best Learned
Memorize the aufbau sequence and use it to write electron configurations for elements. Draw orbital diagrams and relate shell structure to periodic trends (ionization energy, electronegativity).

## Common Misconceptions
- Orbitals are not orbits; they represent probability distributions, not paths.
- The 4s orbital fills before 3d, but 3d is sometimes lower in energy once filled (context matters).
- The periodic table's structure is purely a consequence of quantum mechanics and the Pauli principle, not empirical sorting.

## Explainer

You know from quantum numbers that each electron state in an atom is labeled by four numbers: the principal quantum number n (shell), the angular momentum quantum number ℓ (subshell), the magnetic quantum number mℓ (orbital orientation), and the spin quantum number mₛ (±1/2). The Pauli exclusion principle, which you've already studied, states that no two electrons in the same atom can share all four quantum numbers. The direct consequence: each orbital (a specific n, ℓ, mℓ combination) holds at most two electrons — one spin-up and one spin-down. This single rule is what gives the periodic table its structure.

The **aufbau principle** ("building up" in German) says electrons fill orbitals starting from the lowest available energy. For a hydrogen-like atom, energy depends only on n, so 1s fills first, then 2s, then 2p. But in multi-electron atoms, electron-electron repulsion shifts the energies: the 2s orbital is slightly lower than 2p because s-electrons penetrate closer to the nucleus on average, experiencing greater attraction. By the time you reach the transition metals, the 4s orbital is lower in energy than 3d during filling — which is why potassium (K) puts its 19th electron into 4s rather than 3d, making it alkali-metal-like rather than transition-metal-like.

Counting the states shows why each period has the length it does. The n=1 shell has only 1s: 2 electrons → period 1 has 2 elements (H, He). The n=2 shell has 2s and 2p: 2 + 6 = 8 electrons → period 2 has 8 elements. The n=3 shell adds 3s and 3p: another 8. Then 3d appears in the fourth period (filling after 4s), adding 10 transition metals. The 4f lanthanides add 14 elements to the 6th period. The table's widths — 2, 8, 8, 18, 18 — are directly the counts of available electron states, following from (2ℓ+1) orientations per subshell times 2 spins.

**Chemical periodicity** — the fact that elements in the same column share similar properties — emerges because chemical behavior is determined primarily by the **valence electrons** (the outermost, most loosely bound electrons). Sodium (Na, period 3) and potassium (K, period 4) both have a single valence s-electron and behave similarly as alkali metals. Fluorine and chlorine both have seven valence electrons (one short of a full shell) and are reactive halogens. The periodic table is not an arbitrary sorting scheme — it is a visualization of how quantum mechanics fills energy levels, with each column corresponding to the same valence electron configuration recurring at higher n.
