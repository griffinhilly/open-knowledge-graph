---
id: character-tables-spectroscopic-applications
title: Character Tables and Spectroscopic Selection Rules
domain: chemistry
course: physical-chemistry
prerequisites:
- id: molecular-symmetry-and-group-theory
  type: hard
builds-toward:
- selection-rules-electronic-spectroscopy
tags:
- symmetry
- group-theory
- character-tables
- spectroscopy
stage: advanced
status: validated
---

# Character Tables and Spectroscopic Selection Rules

## Core Idea
Character tables encode how molecular orbitals, vibrational modes, and electronic states transform under point group operations, using irreducible representations (irreps). By matching symmetry properties of initial states, operators, and final states, character tables determine which transitions are symmetry-allowed and predict relative intensities. This is the computational heart of understanding IR, Raman, and UV-Vis spectroscopy.

## Questions

```yaml
- question: "A vibrational mode in a C₂ᵥ molecule belongs to the B₁ irrep, which appears alongside the function x in the character table. What can you conclude about this mode?"
  type: multiple-choice
  options:
    - "It is IR-active because B₁ is a non-totally-symmetric irrep"
    - "It is IR-active because x is a translational (dipole) component, and IR activity requires matching a dipole irrep"
    - "It is Raman-active only, because B₁ does not equal A₁"
    - "Its spectroscopic activity cannot be determined from the character table alone"
  answer: 1
  explanation: "IR activity requires that the vibrational mode's irrep match the irrep of at least one component of the electric dipole operator — i.e., x, y, or z as listed in the character table. Because x transforms as B₁, any mode that also belongs to B₁ will have a nonzero transition dipole integral and will be IR-active. The non-totally-symmetric nature of B₁ is irrelevant; what matters is the match between the mode's irrep and a translational function."

- question: "A student argues that a vibrational mode is IR-active whenever its irrep is the totally symmetric representation A₁. This reasoning is:"
  type: multiple-choice
  options:
    - "Correct — all A₁ modes are IR-active in every point group"
    - "Correct — the direct product of any irrep with A₁ always contains A₁"
    - "Incorrect — IR activity requires the mode to share an irrep with x, y, or z (the dipole components), which may not be A₁"
    - "Incorrect — A₁ modes are Raman-active by definition, not IR-active"
  answer: 2
  explanation: "The selection rule is that the direct product of the initial-state irrep, the operator irrep, and the final-state irrep must contain A₁. For IR spectroscopy the operator is the dipole (transforming as x, y, or z). In some point groups, x, y, and z do transform as A₁ — but in others they do not. The correct test is always: does the mode's irrep match the irrep of x, y, or z in this point group's character table? Automatically assuming A₁ modes are IR-active is incorrect in general."

- question: "In a molecule with an inversion center (such as CO₂ or benzene), no single vibrational mode can be both IR-active and Raman-active."
  type: true-false
  answer: true
  explanation: "This is the mutual exclusion rule, and it follows directly from the character table. In centrosymmetric point groups (Dₙₕ, Dₙd, Cᵢ, etc.), the dipole components (x, y, z) all belong to ungerade (u) irreps, while the polarizability components (x², xy, etc.) belong to gerade (g) irreps. A vibrational mode can only belong to one irrep — either gerade or ungerade — so it can match either dipole components or polarizability components, but never both. This mutual exclusion is a powerful tool for distinguishing centrosymmetric from non-centrosymmetric structures."

- question: "The characters in a character table represent the energy eigenvalues of molecular orbitals under each symmetry operation."
  type: true-false
  answer: false
  explanation: "Characters are not energies. A character is the trace of the matrix that represents a symmetry operation acting on a given irreducible representation. For one-dimensional irreps, the character is simply +1 (the property is unchanged by the operation), −1 (the property is reversed), or 0. For multi-dimensional irreps, it is the sum of diagonal matrix elements. Characters encode how a molecular property transforms under symmetry — which is what determines spectroscopic selection rules — not its energy."

- question: "Why do chemists need to know the irreducible representation (irrep) of a vibrational mode, rather than just its frequency, to predict whether it will appear in an IR spectrum?"
  type: short-answer
  answer: "Frequency alone gives no information about whether the transition dipole integral is nonzero. A mode appears in the IR only if the quantum mechanical transition integral ⟨final|dipole|initial⟩ is nonzero, which requires the direct product of the initial state's irrep, the dipole operator's irrep, and the final state's irrep to contain the totally symmetric representation. The character table encodes which irreps correspond to dipole components (x, y, z). Without matching the mode's irrep to those components, you cannot determine activity — two modes at identical frequencies can have completely different activity if they belong to different irreps."
  explanation: "This is the core utility of character tables: they convert symmetry classification into activity predictions. A mode's frequency tells you where a peak would appear; the mode's irrep tells you whether the peak exists at all. Spectroscopic selection rules are fundamentally symmetry rules, not energy rules."
```

## Explainer

From molecular symmetry and group theory, you know that every molecule belongs to a point group defined by its symmetry elements (rotation axes, mirror planes, inversion centers). A **character table** is the complete mathematical summary of that point group — a grid that tells you exactly how every possible molecular property transforms under each symmetry operation. Reading a character table is the practical skill that converts abstract group theory into concrete spectroscopic predictions.

Each row of a character table is an **irreducible representation** (irrep) — a symmetry label like A₁, B₂, or E. Each column is a symmetry operation (E, C₂, σᵥ, etc.). The numbers in the grid are **characters**: they tell you whether a particular property is unchanged (+1), reversed (−1), or partially mixed (other values) by each operation. On the right side of the table, you find functions (x, y, z, x², xy, etc.) listed next to their corresponding irreps. These tell you which irrep each physical quantity belongs to — for example, the z-component of the dipole moment might transform as A₁, while the xz-component of polarizability transforms as B₁.

The power of character tables lies in the **symmetry selection rule**: a transition between two states is allowed only if the direct product of the initial state's irrep, the operator's irrep, and the final state's irrep contains the totally symmetric representation (A₁ or equivalent). For infrared spectroscopy, the operator is the dipole moment (which transforms like x, y, or z), so a vibrational mode is IR-active only if it belongs to the same irrep as one of these translational functions. For Raman spectroscopy, the operator is the polarizability tensor (which transforms like x², xy, etc.), so a mode is Raman-active if it shares an irrep with one of these quadratic functions. This is why, in molecules with an inversion center, no mode is both IR- and Raman-active — the mutual exclusion rule falls directly out of the character table.

In practice, you classify each normal mode of vibration by its symmetry species using the reduction formula, then look up whether that species appears alongside dipole or polarizability components in the character table. This procedure tells you exactly how many peaks to expect in an IR spectrum versus a Raman spectrum, and it can distinguish between isomers — for instance, cis and trans configurations of a metal complex have different point groups and therefore different numbers of IR-active stretching modes. The character table transforms spectroscopy from pattern recognition into a deductive exercise.
