---
id: vibrational-modes-and-symmetry
title: Group Theory and Vibrational Mode Classification
domain: chemistry
course: physical-chemistry
prerequisites:
- id: vibrational-spectroscopy-theory
  type: hard
- id: vsepr-theory
  type: soft
builds-toward:
- electronic-spectroscopy-theory
tags:
- group-theory
- symmetry
- point-groups
- character-tables
- reducible-representations
stage: advanced
status: validated
---

# Group Theory and Vibrational Mode Classification

## Core Idea
Molecular point group symmetry classifies normal modes into irreducible representations using character tables. The reducible representation Γ_total is decomposed using the reduction formula to identify how many modes belong to each symmetry species. IR-active modes must transform as x, y, or z (components of the dipole vector); Raman-active modes must transform as quadratic functions (x², xy, etc.) of the polarizability tensor. This systematic approach predicts the number of IR and Raman peaks without computing wavefunctions, and is essential for interpreting spectra of complex molecules.

## How It's Best Learned
Master the C₂ᵥ and D₂ₕ character tables first. Classify the three modes of water (C₂ᵥ) and the four modes of CO₂ (D∞ₕ), predicting IR/Raman activity and verifying against known spectra.

## Common Misconceptions
- Thinking group theory is only for crystals; it applies to any molecule with symmetry.
- Forgetting to subtract translations (3) and rotations (3 or 2) from Γ_total before identifying vibrational modes.

## Explainer

From vibrational spectroscopy theory, you know that a molecule with N atoms has 3N − 6 vibrational normal modes (or 3N − 5 if linear). Each mode involves all atoms moving at the same frequency, and each mode is either IR-active, Raman-active, both, or neither. The question is: how do you determine which modes are which without solving the full quantum mechanical problem? The answer is **group theory** — a systematic method that uses the molecule's symmetry to classify every normal mode and predict its spectroscopic activity purely from the geometry of the molecule.

The procedure begins by identifying the molecule's **point group** — the set of all symmetry operations (rotations, reflections, inversions, improper rotations) that leave the molecule looking identical. Water belongs to C₂ᵥ (a C₂ rotation axis and two mirror planes); CO₂ belongs to D∞ₕ (an infinite rotation axis, infinite mirror planes, and an inversion center). Once you know the point group, you look up its **character table**, which lists the irreducible representations — the fundamental symmetry patterns that any motion of the molecule must conform to. Each irreducible representation is a row in the table, labeled by a symbol (A₁, B₂, E, etc.) and characterized by how it transforms under each symmetry operation (+1, −1, 0, etc.).

The practical recipe has three steps. First, you construct the **reducible representation** Γ_total by considering how each atom's three Cartesian displacement coordinates (x, y, z) transform under every symmetry operation. For each operation, you count only the atoms that remain unmoved — moved atoms contribute zero. Each unmoved atom contributes a character based on the transformation matrix for that operation (+3 for identity, −1 for a C₂ rotation, +1 for a σ_v reflection, and so on). Second, you subtract the representations for translation (Γ_trans) and rotation (Γ_rot), which are listed directly in the character table. What remains is the vibrational representation Γ_vib. Third, you decompose Γ_vib into irreducible representations using the **reduction formula**: n_i = (1/h)Σ N_R · χ(R) · χ_i(R), where h is the group order, N_R is the number of operations in each class, χ(R) is your reducible character, and χ_i(R) is the character from the table.

The payoff is immediate spectroscopic prediction. The character table's rightmost columns show which irreducible representations transform as x, y, or z (the dipole moment components) and which transform as x², xy, xz, etc. (the polarizability tensor components). A vibrational mode is **IR-active** if its irreducible representation matches a translational function (x, y, or z), because IR absorption requires a change in dipole moment. A mode is **Raman-active** if it matches a quadratic function, because Raman scattering requires a change in polarizability. For centrosymmetric molecules (those with an inversion center, like CO₂), the **mutual exclusion rule** holds: no mode can be both IR and Raman active. This means IR and Raman spectra give complementary information, and group theory tells you exactly how to read that complementarity from the character table.
