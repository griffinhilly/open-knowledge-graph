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
status: draft
---

# Character Tables and Spectroscopic Selection Rules

## Core Idea
Character tables encode how molecular orbitals, vibrational modes, and electronic states transform under point group operations, using irreducible representations (irreps). By matching symmetry properties of initial states, operators, and final states, character tables determine which transitions are symmetry-allowed and predict relative intensities. This is the computational heart of understanding IR, Raman, and UV-Vis spectroscopy.

## Explainer

From molecular symmetry and group theory, you know that every molecule belongs to a point group defined by its symmetry elements (rotation axes, mirror planes, inversion centers). A **character table** is the complete mathematical summary of that point group — a grid that tells you exactly how every possible molecular property transforms under each symmetry operation. Reading a character table is the practical skill that converts abstract group theory into concrete spectroscopic predictions.

Each row of a character table is an **irreducible representation** (irrep) — a symmetry label like A₁, B₂, or E. Each column is a symmetry operation (E, C₂, σᵥ, etc.). The numbers in the grid are **characters**: they tell you whether a particular property is unchanged (+1), reversed (−1), or partially mixed (other values) by each operation. On the right side of the table, you find functions (x, y, z, x², xy, etc.) listed next to their corresponding irreps. These tell you which irrep each physical quantity belongs to — for example, the z-component of the dipole moment might transform as A₁, while the xz-component of polarizability transforms as B₁.

The power of character tables lies in the **symmetry selection rule**: a transition between two states is allowed only if the direct product of the initial state's irrep, the operator's irrep, and the final state's irrep contains the totally symmetric representation (A₁ or equivalent). For infrared spectroscopy, the operator is the dipole moment (which transforms like x, y, or z), so a vibrational mode is IR-active only if it belongs to the same irrep as one of these translational functions. For Raman spectroscopy, the operator is the polarizability tensor (which transforms like x², xy, etc.), so a mode is Raman-active if it shares an irrep with one of these quadratic functions. This is why, in molecules with an inversion center, no mode is both IR- and Raman-active — the mutual exclusion rule falls directly out of the character table.

In practice, you classify each normal mode of vibration by its symmetry species using the reduction formula, then look up whether that species appears alongside dipole or polarizability components in the character table. This procedure tells you exactly how many peaks to expect in an IR spectrum versus a Raman spectrum, and it can distinguish between isomers — for instance, cis and trans configurations of a metal complex have different point groups and therefore different numbers of IR-active stretching modes. The character table transforms spectroscopy from pattern recognition into a deductive exercise.
