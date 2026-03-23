---
id: ion-formation-from-electron-transfer
title: Ion Formation from Electron Transfer
domain: chemistry
course: general-chemistry
prerequisites:
- id: ionic-bonding
  type: hard
- id: electron-configuration
  type: hard
builds-toward:
- ionic-bonding
- acid-base-definitions
tags:
- ions
- cations
- anions
- octet rule
stage: formal-systems
status: validated
---

# Ion Formation from Electron Transfer

## Core Idea
Ions form when atoms gain or lose electrons to achieve stable electron configurations, typically following the octet rule. The number of electrons lost or gained determines the charge of the resulting ion.

## Questions

```yaml
- question: "Sulfur (S) is in Group 16. When it forms an ion, what charge would you predict, and why?"
  type: multiple-choice
  options:
    - "S²⁺, because sulfur can lose 2 electrons from its outer shell"
    - "S²⁻, because sulfur needs 2 more electrons to complete its outer shell and reach the argon configuration"
    - "S⁶⁺, because sulfur has 6 valence electrons that can all be removed"
    - "S¹⁻, because sulfur needs only 1 electron to fill the next available orbital"
  answer: 1
  explanation: "Sulfur has 6 valence electrons and needs 2 more to reach 8 and achieve the electron configuration of argon (the next noble gas). The driving force is stability — gaining 2 electrons fills the outer shell. While sulfur could theoretically lose electrons (forming S²⁺ or higher), doing so would require breaking the noble gas core, which requires far more energy than is gained. Main-group nonmetals on the right side of the table characteristically gain electrons rather than lose them. Option D is wrong — sulfur has 6 valence electrons and needs 2, not 1, to complete the shell."

- question: "Why does sodium form Na⁺ and not Na²⁺, even though a higher positive charge might seem to mean more electron loss?"
  type: multiple-choice
  options:
    - "Sodium only has one valence electron, so it physically cannot lose a second electron"
    - "Losing the first electron gives sodium the stable neon configuration; losing the second would require breaking into a filled, stable inner shell at enormously greater energy cost"
    - "Na²⁺ would be too small to form stable ionic bonds with anions"
    - "Sodium's ionization energy drops to zero after the first electron is removed"
  answer: 1
  explanation: "Sodium's electron configuration is [Ne]3s¹. Removing the single 3s electron gives Na⁺ the neon configuration — a stable, filled outer shell. Removing a second electron would require pulling from the 2p subshell, which is part of the filled noble-gas core. The second ionization energy is enormously higher than the first because of this stability. Ion formation stops when the next noble gas configuration is reached; further removal dismantles a stable shell rather than shedding a lone outer electron. Option A is incorrect — sodium has more electrons, but removing them is energetically prohibitive."

- question: "The charge of a main-group ion directly tells you how many electrons were gained or lost, and this number is determined by how far the neutral atom is from a noble gas configuration."
  type: true-false
  answer: true
  explanation: "This is the core principle of ion formation for main-group elements. The number of electrons transferred is dictated by the shortest path to a filled outer shell — losing a few electrons (metals, left side) or gaining a few (nonmetals, right side). This directly predicts ion charges: Group 1 → 1+, Group 2 → 2+, Group 16 → 2−, Group 17 → 1−. The charge is not arbitrary; it is the count of electrons transferred, and those electrons are transferred because doing so delivers the atom to a more stable configuration."

- question: "Atoms form ions because they are attracted to the opposite charges of nearby ions in an ionic compound."
  type: true-false
  answer: false
  explanation: "Ion formation is driven by the energetic stability of reaching a noble-gas electron configuration — an intrinsic property of the atom's electron structure, not a response to nearby ions. Sodium has the same tendency to lose one electron whether or not a chloride ion is nearby. The attraction between oppositely charged ions (ionic bonding) stabilizes the compound after ions form, but it is not the cause of electron transfer. Confusing the stability of the resulting bond with the driving force for electron loss or gain is a common error."

- question: "Why does aluminum form Al³⁺ rather than Al²⁺, and what general principle does this illustrate about main-group ion charges?"
  type: short-answer
  answer: "Aluminum has 3 valence electrons (configuration [Ne]3s²3p¹). Removing all three gives it the stable neon configuration. Stopping at Al²⁺ would leave it with one 3s electron still in the outer shell — less stable than a fully stripped outer shell reaching neon. The general principle: main-group ions form by losing or gaining exactly as many electrons as needed to reach the electron configuration of the nearest noble gas. The charge equals the number of electrons transferred, which is determined by the most energetically favorable path to a stable (filled-shell) configuration."
  explanation: "The ionization energy profile tells the story: the first three ionization energies of aluminum increase gradually (removing 3p¹, then 3s²), but the fourth jumps enormously because it starts removing from the neon core. This energy cliff explains why Al³⁺ is strongly preferred over Al⁴⁺ — further removal would dismantle a stable noble-gas configuration."
```

## Explainer

From electron configuration, you know that atoms arrange their electrons in shells and subshells, and that noble gases have completely filled outer shells. **Ion formation** is driven by the energetic advantage of achieving or approaching these stable configurations. Atoms do not gain or lose electrons randomly — the number they transfer is determined by how close they already are to a full outer shell.

**Cations** (positive ions) form when atoms lose electrons. Metals on the left side of the periodic table have just one, two, or three valence electrons. Removing those electrons is energetically favorable because the atom reaches the stable configuration of the preceding noble gas. Sodium (Na), with the configuration 1s²2s²2p⁶3s¹, loses its single 3s electron to become Na⁺, which has the same electron configuration as neon. The energy required to remove this electron (ionization energy) is modest because the atom gains so much stability in return. Magnesium loses two electrons to form Mg²⁺, and aluminum loses three to form Al³⁺ — each reaching the neon configuration.

**Anions** (negative ions) form when atoms gain electrons. Nonmetals on the right side of the periodic table are just one, two, or three electrons short of a full outer shell. Chlorine (Cl), with configuration [Ne]3s²3p⁵, needs only one electron to complete its 3p subshell and reach the argon configuration, so it forms Cl⁻. Oxygen gains two electrons to form O²⁻, and nitrogen gains three to form N³⁻. The energy released when an atom gains an electron (electron affinity) reflects how strongly the atom pulls that electron into its nearly complete shell.

The pattern connects directly to periodic table position. Group 1 metals form 1+ ions, Group 2 form 2+ ions, Group 16 nonmetals form 2− ions, and Group 17 form 1− ions. Transition metals are more complex — they can form multiple oxidation states because their d electrons are close in energy to their outermost s electrons. The key principle is always the same: electron transfer occurs because the resulting ion has a more stable electron configuration than the neutral atom, and the charge of the ion tells you exactly how many electrons were transferred.
