---
id: electron-configuration-principles
title: Electron Configuration and Orbital Theory
domain: chemistry
course: general-chemistry
prerequisites:
- id: atomic-structure-and-atoms
  type: hard
builds-toward:
- periodic-trends-and-properties
- valence-electrons-and-bonding
tags:
- electron configuration
- orbitals
- aufbau principle
- pauli exclusion
stage: advanced
status: draft
---

# Electron Configuration and Orbital Theory

## Core Idea
Electrons occupy orbitals organized by increasing energy levels (shells) and sublevels (s, p, d, f). The aufbau principle, Pauli exclusion principle, and Hund's rule determine how electrons fill these orbitals. Electron configuration determines an element's chemical properties, especially its tendency to form bonds.

## Questions

```yaml
- question: "Nitrogen has 7 electrons (configuration 1s² 2s² 2p³). How are the three 2p electrons arranged according to Hund's rule?"
  type: multiple-choice
  options:
    - "All three in the same 2p orbital with alternating spins, to minimize repulsion by keeping them close"
    - "Two in one 2p orbital (paired) and one alone in a second 2p orbital, leaving the third empty"
    - "One electron in each of the three 2p orbitals, all with the same spin direction"
    - "Two in the 2p subshell and one promoted to the 3s orbital to reduce electron-electron repulsion"
  answer: 2
  explanation: "Hund's rule: within a subshell, electrons occupy orbitals singly before pairing up, and the unpaired electrons have the same spin. With three 2p orbitals and three electrons, each orbital gets exactly one electron, all with the same spin. This maximizes unpaired spins and minimizes electron-electron repulsion within the subshell. Option A reverses the rule — pairing electrons in one orbital actually increases repulsion by forcing two electrons into the same space. This arrangement (three unpaired electrons) makes nitrogen unusually stable and less reactive than its neighbors."

- question: "Which electron configuration is correct for iron (atomic number 26)?"
  type: multiple-choice
  options:
    - "1s² 2s² 2p⁶ 3s² 3p⁶ 3d⁸ — filling the 3d subshell completely because shell 3 has a lower number than 4"
    - "1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d⁶ — because 4s is lower in energy than 3d for most atoms and fills first"
    - "1s² 2s² 2p⁶ 3s² 3p⁶ 4s⁴ 3d⁴ — distributing electrons evenly between 4s and 3d"
    - "1s² 2s² 2p⁶ 3s² 3p⁶ 4p² 3d⁶ — 4p fills before 3d because the 4 shell comes after the 3 shell"
  answer: 1
  explanation: "The aufbau principle fills orbitals in order of increasing energy, not strictly by shell number. For most atoms, the 4s orbital is lower in energy than the 3d orbitals, so 4s fills first. Iron (Z=26) fills: 1s² 2s² 2p⁶ 3s² 3p⁶ (18 electrons), then 4s² (2 more = 20), then 3d⁶ (6 more = 26). Option A is the classic misconception — assuming shell number determines filling order. The crossover between 4s and 3d is a key exception to the naive expectation that lower shell numbers always mean lower energy."

- question: "Two electrons sharing the same orbital must have opposite spins because the Pauli exclusion principle states that no two electrons in an atom can have the same set of four quantum numbers."
  type: true-false
  answer: true
  explanation: "Two electrons in the same orbital share the same principal quantum number (n), angular momentum quantum number (l), and magnetic quantum number (mₗ) — three of their four quantum numbers are identical. For the Pauli exclusion principle to be satisfied, their fourth quantum number — spin (mₛ) — must differ. Since spin can only be +1/2 or -1/2, two electrons in the same orbital must have opposite spins. This is why each orbital holds a maximum of two electrons — a third electron would have to duplicate all four quantum numbers of one of the existing electrons."

- question: "The aufbau principle predicts that the 3d subshell always fills before the 4s subshell because the '3' in 3d indicates a lower principal energy level than the '4' in 4s."
  type: true-false
  answer: false
  explanation: "Shell number alone does not determine filling order — what matters is the actual energy of each orbital in a many-electron atom. For most atoms, the 4s orbital is lower in energy than the 3d orbitals due to electron shielding and penetration effects, so 4s fills before 3d. The standard diagonal mnemonic and the observed electron configurations of transition metals confirm this. The misconception that lower shell number = lower energy fails at the 3d/4s crossover and at several other points in the periodic table."

- question: "Why do elements in the same column of the periodic table tend to have similar chemical properties? Connect your answer directly to electron configuration."
  type: short-answer
  answer: "Elements in the same column share the same number and type of valence electrons — the outermost electrons that participate in bonding. For example, lithium (1s²2s¹), sodium (1s²2s²2p⁶3s¹), and potassium all have exactly one electron in an outer s orbital. Chemical behavior is determined primarily by how easily an atom gains, loses, or shares its valence electrons. Because same-group elements have the same valence electron count and the same orbital type (s, p, d, or f), they undergo analogous reactions and form analogous compounds — losing one electron to form +1 ions, for instance. The periodic repetition of properties in the table directly reflects the periodic repetition of valence electron configurations as atomic number increases."
```

## Explainer

From your study of atomic structure, you know that atoms consist of a nucleus surrounded by electrons. But electrons don't orbit the nucleus like planets around a star — they occupy **orbitals**, which are three-dimensional regions of space where an electron is most likely to be found. Each orbital has a characteristic shape: s orbitals are spherical, p orbitals are dumbbell-shaped, d orbitals have more complex four-lobed shapes, and f orbitals are more intricate still. These shapes matter because they determine how atoms approach each other and form bonds.

Orbitals are organized into **energy levels (shells)** numbered 1, 2, 3, and so on, and each shell contains **sublevels** (s, p, d, f) with increasing energy. Shell 1 has only the 1s sublevel; shell 2 has 2s and 2p; shell 3 has 3s, 3p, and 3d; and so on. The number of orbitals in each sublevel is fixed: s has 1, p has 3, d has 5, f has 7 — and each orbital holds at most 2 electrons. This maximum capacity of two electrons per orbital is the **Pauli exclusion principle**, which states that no two electrons in an atom can have the same set of four quantum numbers. In practice, the two electrons sharing an orbital must have opposite spins.

Three rules govern the order in which electrons fill orbitals. The **aufbau principle** (German for "building up") says electrons occupy the lowest-energy orbital available first. Energy ordering mostly follows shell number, but there are crossovers — 4s fills before 3d because it is lower in energy for most atoms. The standard filling order (1s, 2s, 2p, 3s, 3p, 4s, 3d, 4p, ...) can be remembered using a diagonal diagram. **Hund's rule** says that within a sublevel, electrons spread out among available orbitals before pairing up, each with the same spin. Think of it like strangers boarding a bus — they sit in empty rows before doubling up. This minimizes electron-electron repulsion and produces a lower-energy, more stable arrangement.

Writing an electron configuration means listing the occupied sublevels with the number of electrons in each. Carbon, with 6 electrons, is 1s² 2s² 2p². Iron, with 26 electrons, is 1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d⁶. The electrons in the outermost shell — the **valence electrons** — are the ones that participate in chemical bonding and determine an element's reactivity. This is why electron configuration is not just bookkeeping: it explains why elements in the same column of the periodic table behave similarly (they have the same number of valence electrons) and why chemical properties repeat periodically as atomic number increases.
