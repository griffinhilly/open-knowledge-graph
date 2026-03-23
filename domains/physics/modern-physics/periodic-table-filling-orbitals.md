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
status: validated
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

## Questions

```yaml
- question: "Period 4 of the periodic table has 18 elements. Which sequence of subshells is filled across period 4, and why does this produce exactly 18 elements?"
  type: multiple-choice
  options:
    - "4s, 4p, 4d — three subshells with 2, 6, 10 electrons = 18"
    - "4s, 3d, 4p — filling 4s (2 electrons), then 3d (10 electrons), then 4p (6 electrons) = 18 elements"
    - "3d, 4s, 4f — these three subshells together hold 18 electrons"
    - "4s, 4p — two subshells each with 9 electrons give 18 total"
  answer: 1
  explanation: "Period 4 begins with 4s (2 electrons: K and Ca), then fills the 3d subshell (10 electrons: the transition metals Sc through Zn), then fills 4p (6 electrons: Ga through Kr). The count is 2 + 10 + 6 = 18. The 3d fills within period 4 rather than period 3 because in multi-electron atoms the 4s orbital is lower in energy than 3d during filling, so potassium puts its 19th electron into 4s. Once 4s is filled, 3d fills before 4p as the next available subshell by energy."

- question: "Potassium (element 19) places its 19th electron in the 4s orbital rather than 3d. Which best explains why?"
  type: multiple-choice
  options:
    - "The 3d subshell is completely full in period 3, leaving no room for potassium's electron"
    - "In multi-electron atoms, the 4s orbital has lower energy than 3d during filling due to electron penetration effects, so the aufbau principle dictates filling 4s first"
    - "Potassium is an alkali metal by definition, and alkali metals always have electrons in s-orbitals"
    - "The Pauli exclusion principle prevents any electron from occupying 3d until 3s and 3p are completely filled"
  answer: 1
  explanation: "In multi-electron atoms, electron-electron repulsion and nuclear shielding shift orbital energies relative to the hydrogen-like case. The 4s orbital penetrates closer to the nucleus than 3d (higher electron density near the origin), experiencing stronger nuclear attraction and sitting at lower energy during filling. So the aufbau principle places the 19th electron in 4s, giving potassium alkali-metal character. Once 3d is filled, it can drop below 4s in energy, which is why transition metals lose their 4s electrons first in ionization."

- question: "All elements in the same column of the periodic table have identical electron configurations."
  type: true-false
  answer: false
  explanation: "Elements in the same column share the same valence electron configuration — the outermost electrons that determine chemical behavior — but their complete configurations differ. Sodium (Na, period 3) is [Ne] 3s¹ and potassium (K, period 4) is [Ar] 4s¹: both have a single valence s-electron but different core electrons and principal quantum numbers. It is the shared valence configuration, not the total configuration, that gives column-mates similar chemical properties."

- question: "The periodic table's row lengths — 2, 8, 8, 18, 18, 32 — directly reflect the number of available electron states in each period's filling sequence, derived from quantum mechanical counting of orbitals."
  type: true-false
  answer: true
  explanation: "Each subshell holds 2(2ℓ+1) electrons: s holds 2, p holds 6, d holds 10, f holds 14. Period 1: only 1s → 2 elements. Periods 2 and 3: s and p → 8 elements each. Periods 4 and 5: s, d (from the previous shell), p → 18 elements each. Periods 6 and 7: s, f, d, p → 32 elements each. The periodic table's dimensions are not an empirical discovery but a direct read-off of quantum mechanical state counting under the Pauli exclusion principle."

- question: "Explain why sodium (Na, period 3) and potassium (K, period 4) have similar chemical properties despite being in different periods with different total numbers of electrons."
  type: short-answer
  answer: "Chemical behavior is determined primarily by valence electrons — the outermost, most loosely bound electrons that participate in bonding. Sodium has the configuration [Ne] 3s¹ and potassium [Ar] 4s¹: both have a single valence electron in an s-orbital, one beyond a complete noble-gas core. This shared valence structure means both readily lose one electron to form +1 ions and share the same reactivity patterns. The extra inner shells in potassium are shielded core electrons that do not participate in chemistry."
  explanation: "This is the deep reason the periodic table works: periodicity is a periodicity of valence configurations, not total electron count. Elements recur in the same column because every complete shell adds the same valence structure — one more s-electron beyond the core, etc. Quantum mechanics predicts that once you complete a shell and add one more electron to the next s-orbital, the chemical behavior resets to match the element one period above. The relevant physics (valence structure) has genuinely repeated, not just the row count."
```

## Explainer

You know from quantum numbers that each electron state in an atom is labeled by four numbers: the principal quantum number n (shell), the angular momentum quantum number ℓ (subshell), the magnetic quantum number mℓ (orbital orientation), and the spin quantum number mₛ (±1/2). The Pauli exclusion principle, which you've already studied, states that no two electrons in the same atom can share all four quantum numbers. The direct consequence: each orbital (a specific n, ℓ, mℓ combination) holds at most two electrons — one spin-up and one spin-down. This single rule is what gives the periodic table its structure.

The **aufbau principle** ("building up" in German) says electrons fill orbitals starting from the lowest available energy. For a hydrogen-like atom, energy depends only on n, so 1s fills first, then 2s, then 2p. But in multi-electron atoms, electron-electron repulsion shifts the energies: the 2s orbital is slightly lower than 2p because s-electrons penetrate closer to the nucleus on average, experiencing greater attraction. By the time you reach the transition metals, the 4s orbital is lower in energy than 3d during filling — which is why potassium (K) puts its 19th electron into 4s rather than 3d, making it alkali-metal-like rather than transition-metal-like.

Counting the states shows why each period has the length it does. The n=1 shell has only 1s: 2 electrons → period 1 has 2 elements (H, He). The n=2 shell has 2s and 2p: 2 + 6 = 8 electrons → period 2 has 8 elements. The n=3 shell adds 3s and 3p: another 8. Then 3d appears in the fourth period (filling after 4s), adding 10 transition metals. The 4f lanthanides add 14 elements to the 6th period. The table's widths — 2, 8, 8, 18, 18 — are directly the counts of available electron states, following from (2ℓ+1) orientations per subshell times 2 spins.

**Chemical periodicity** — the fact that elements in the same column share similar properties — emerges because chemical behavior is determined primarily by the **valence electrons** (the outermost, most loosely bound electrons). Sodium (Na, period 3) and potassium (K, period 4) both have a single valence s-electron and behave similarly as alkali metals. Fluorine and chlorine both have seven valence electrons (one short of a full shell) and are reactive halogens. The periodic table is not an arbitrary sorting scheme — it is a visualization of how quantum mechanics fills energy levels, with each column corresponding to the same valence electron configuration recurring at higher n.
