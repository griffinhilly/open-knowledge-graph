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

## Questions

```yaml
- question: "Potassium has 19 electrons. After filling through 3p, where does the 19th electron go, and why?"
  type: multiple-choice
  options:
    - "Into 3d, because 3d has a lower principal quantum number (n=3) than 4s (n=4)"
    - "Into 4s, because the (n+ℓ) rule gives 4s a value of 4 while 3d has a value of 5, so 4s has lower energy"
    - "Into 4p, because electrons always complete one subshell type before starting the next"
    - "Into 3d, because d orbitals fill before s orbitals in the same period of the periodic table"
  answer: 1
  explanation: "The 19th electron goes into 4s, not 3d. For 4s: n+ℓ = 4+0 = 4. For 3d: n+ℓ = 3+2 = 5. Lower (n+ℓ) fills first, so 4s fills before 3d. The common misconception is to fill by n alone, which would incorrectly place 3d (n=3) before 4s (n=4). In multi-electron atoms, effective nuclear charge and shielding split subshell energies in a way that makes this crossing necessary."

- question: "Why do sodium (Na) and potassium (K), which are in the same column of the periodic table, show similar chemical behavior?"
  type: multiple-choice
  options:
    - "They have the same total number of electrons in their atoms"
    - "They have the same number of neutrons in their nuclei"
    - "They have the same valence electron configuration — both have a single electron in an outermost s subshell ([noble gas] ns¹)"
    - "They have similar atomic masses, so they behave similarly in chemical reactions"
  answer: 2
  explanation: "Chemical behavior is determined by valence electrons — the outermost electrons that participate in bonding. Na is [Ne]3s¹ and K is [Ar]4s¹; both have one electron in an outermost s orbital. This identical valence configuration produces similar reactivity (both readily lose one electron to form +1 ions). Column placement in the periodic table directly encodes valence electron configuration, which is why periodic trends are possible."

- question: "In multi-electron atoms, the 4s subshell fills before 3d because electrons in 4s experience greater effective nuclear charge and lower energy than those in 3d."
  type: true-false
  answer: true
  explanation: "In hydrogen, all subshells with the same n are degenerate. In multi-electron atoms, inner electrons shield outer electrons from the nucleus, and different subshells penetrate the electron cloud differently. The 4s orbital penetrates closer to the nucleus on average than 3d, giving it lower energy despite the higher principal quantum number. The (n+ℓ) rule is a practical summary of this effect."

- question: "In multi-electron atoms, as in hydrogen, all subshells with the same principal quantum number n have the same energy (are degenerate)."
  type: true-false
  answer: false
  explanation: "Degeneracy of same-n subshells holds only for hydrogen (a one-electron atom with no electron-electron repulsion). In multi-electron atoms, electron-electron repulsion and differential shielding break the degeneracy: 2s and 2p have different energies, as do 3s, 3p, and 3d. This is precisely why 4s fills before 3d — the orbital energies depend on both n and ℓ in multi-electron atoms."

- question: "Explain why 4s fills before 3d in multi-electron atoms, even though 3 is a smaller principal quantum number than 4."
  type: short-answer
  answer: "In multi-electron atoms, orbital energy depends on both n and ℓ, not n alone. Inner electrons shield outer electrons from the nucleus. The 4s orbital penetrates closer to the nucleus than 3d (despite higher n), giving it lower energy in multi-electron atoms. The (n+ℓ) rule captures this: 4s has n+ℓ = 4, while 3d has n+ℓ = 5, so 4s has lower energy and fills first."
  explanation: "This is one of the most important departures from the naive 'fill by n' picture. In hydrogen, subshells with the same n are degenerate. But electron-electron repulsion in multi-electron atoms creates an energy splitting that depends on the orbital's shape (ℓ) as well as its size (n). The crossing of 4s below 3d is the reason the transition metals (d-block) appear where they do in the periodic table, and it directly explains why period 4 starts with K and Ca (filling 4s) before Sc–Zn (filling 3d)."
```

## Explainer

From your study of the Pauli exclusion principle, you know that no two electrons in an atom can occupy the same quantum state — and for electrons this means no two can share the same set of all four quantum numbers (n, ℓ, mₗ, mₛ). The **Aufbau principle** (German: "building up") uses this constraint to explain how multi-electron atoms are constructed: you add electrons one at a time, each going into the lowest available energy state not yet forbidden by Pauli exclusion.

Each electron's state is labeled by four quantum numbers. The **principal quantum number** n = 1, 2, 3, ... controls the shell and sets the coarse energy scale (higher n = higher energy, larger orbital). The **angular momentum quantum number** ℓ = 0, 1, ..., n−1 labels subshells by their orbital shape (s, p, d, f for ℓ = 0,1,2,3). The **magnetic quantum number** mₗ = −ℓ, ..., +ℓ gives the orbital orientation — there are 2ℓ+1 orbitals in each subshell. The **spin quantum number** mₛ = ±½ allows two electrons per orbital. Counting up: an s subshell holds 2 electrons, a p subshell 6, a d subshell 10, an f subshell 14.

The energy ordering is almost, but not exactly, by n alone. For hydrogen, all subshells with the same n are degenerate. For multi-electron atoms, electron-electron repulsion and **effective nuclear charge** (the net positive charge experienced by an outer electron, shielded by inner electrons) split the subshell energies. The rule of thumb is the (n + ℓ) rule: lower (n + ℓ) fills first; when equal, lower n fills first. This gives the sequence 1s, 2s, 2p, 3s, 3p, **4s, 3d**, 4p, **5s, 4d**, ... The crossing of 4s before 3d is the most important consequence: electrons prefer 4s over 3d because 4s has n + ℓ = 4 + 0 = 4 while 3d has 3 + 2 = 5.

The **valence electrons** — those in the outermost shell — determine virtually all of an atom's chemical behavior, from what bonds it forms to how it reacts. Elements in the same column of the periodic table have the same valence electron configuration (same ℓ and number of electrons in the outermost subshell), which is why they show similar chemistry. Sodium and potassium are both [noble gas] ns¹; chlorine and bromine are both [noble gas] ns²np⁵. The periodicity of the table is a direct consequence of the Aufbau filling order: each new row begins when electrons start filling a new principal quantum number, and the block structure (s-block, p-block, d-block, f-block) reflects which subshell is being filled across that row.
