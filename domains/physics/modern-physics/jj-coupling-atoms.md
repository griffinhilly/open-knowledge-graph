---
id: jj-coupling-atoms
title: LS and jj Coupling Schemes in Multi-Electron Atoms
domain: physics
course: modern-physics
prerequisites:
- id: atomic-selection-rules
  type: hard
builds-toward:
- pauli-exclusion-antisymmetry
tags:
- quantum
- atoms
- coupling
stage: advanced
status: draft
---

# LS and jj Coupling Schemes in Multi-Electron Atoms

## Core Idea
In light atoms, LS coupling (Russell-Saunders) couples individual orbital and spin angular momenta to form total L and S, then couple to J. Heavy atoms show jj coupling where spin-orbit interaction dominates, coupling each electron's ℓ and s to jᵢ before summing over electrons. The crossover between schemes reflects changing relative strengths of Coulomb repulsion and spin-orbit coupling.

## Explainer

From atomic selection rules you know that multi-electron atoms have quantum states labeled by total angular momentum quantum numbers — but *how* those totals are built from individual electron angular momenta is not fixed. It depends on which interaction is stronger: the **Coulomb repulsion** between electrons (which couples their orbital motions together) or the **spin-orbit interaction** for each electron individually (which couples each electron's spin to its own orbital motion). These two interactions compete, and their relative strength determines how we should add up the angular momenta.

In **LS coupling** (Russell-Saunders coupling), typical of light atoms (Z ≲ 30), electron-electron Coulomb repulsion dominates. The strong mutual electrostatic interaction makes all the orbital angular momenta ℓᵢ "speak" to each other rapidly, coupling them into a total orbital angular momentum L = Σℓᵢ. Independently, all the spins sᵢ couple into a total spin S = Σsᵢ. Only then does the comparatively weak spin-orbit interaction couple L and S together to form the total angular momentum J. The good quantum numbers are L, S, J, and M_J. Spectroscopic term symbols like ²S+¹L_J (e.g., ³P₂) encode exactly these numbers: the superscript is 2S+1, the letter encodes L, and the subscript is J.

In **jj coupling**, typical of heavy atoms (Z ≳ 70), spin-orbit coupling scales as Z⁴ and becomes dominant. Each electron's own ℓᵢ and sᵢ are strongly coupled *to each other*, forming an individual total jᵢ = ℓᵢ + sᵢ. The electrons then interact only weakly with each other (Coulomb repulsion is comparatively small), and the individual jᵢ couple to form total J = Σjᵢ. In this scheme, L and S are no longer good quantum numbers — the states cannot be cleanly labeled by total orbital and total spin angular momentum. Only J and M_J remain well-defined.

The crossover region between Z ≈ 30 and Z ≈ 70 shows neither scheme cleanly. Real atoms in this range exhibit **intermediate coupling**, where both interactions contribute comparably and neither L nor the individual jᵢ are good quantum numbers. Computational treatments must diagonalize the full Hamiltonian including both effects. The practical consequence for spectroscopy is that LS-coupled atoms (like helium, carbon, sodium) show characteristic patterns of fine-structure multiplets with predictable level spacings, while jj-coupled atoms (like lead, bismuth) show dramatically different level ordering that would be mispredicted if you naively applied LS term symbols. The coupling scheme also governs which transitions are allowed: selection rules for radiative transitions depend on which quantum numbers are good, so the observable spectra directly reflect the coupling regime.
