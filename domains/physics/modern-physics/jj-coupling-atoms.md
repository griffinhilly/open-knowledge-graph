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

## Questions

```yaml
- question: "A physicist tries to label the energy levels of bismuth (Z=83) using LS-coupling term symbols like ³P₂. Why will this approach fail for bismuth but work well for carbon (Z=6)?"
  type: multiple-choice
  options:
    - "Bismuth has too many electrons for the term symbol notation to accommodate — it runs out of letter labels"
    - "In heavy atoms like bismuth, spin-orbit coupling scales as Z⁴ and dominates over electron-electron Coulomb repulsion, so each electron's ℓᵢ and sᵢ couple together first. Total L and S are no longer good quantum numbers, making LS term symbols undefined"
    - "Bismuth emits X-rays at energies too high for visible spectroscopy, so term symbols are inapplicable"
    - "LS coupling term symbols would technically apply, but the fine structure splittings are too small to measure in heavy atoms"
  answer: 1
  explanation: "LS coupling term symbols encode total orbital angular momentum L and total spin S, which are good quantum numbers only when electron-electron Coulomb repulsion couples the ℓᵢ together strongly before spin-orbit coupling matters. In carbon (Z=6), this condition holds. In bismuth (Z=83), spin-orbit coupling scales as Z⁴ and becomes so strong that each electron's own ℓᵢ and sᵢ couple to form individual jᵢ before the electrons interact much with each other. The resulting jj-coupled states have well-defined individual jᵢ and total J, but L and S are not well-defined — the LS term symbols are meaningless."

- question: "What physical fact explains why LS coupling governs light atoms while jj coupling governs heavy atoms?"
  type: multiple-choice
  options:
    - "Heavy atoms have more electrons that pair up, canceling individual angular momenta and forcing collective coupling"
    - "Spin-orbit coupling energy scales as Z⁴, so for sufficiently heavy atoms it becomes larger than the electron-electron Coulomb repulsion energy. Each electron then couples its own ℓᵢ to its own sᵢ to form jᵢ before interacting significantly with other electrons"
    - "Heavy atoms are larger, reducing nuclear attraction and weakening the coupling of orbital angular momenta to the nucleus"
    - "The Pauli exclusion principle enforces jj coupling for atoms with more than 30 electrons"
  answer: 1
  explanation: "The competition is between two interactions: electron-electron electrostatic repulsion (couples all ℓᵢ together → forms L, couples all sᵢ → forms S) and the spin-orbit interaction for each electron individually (couples ℓᵢ to sᵢ → forms jᵢ). Spin-orbit coupling is proportional to Z⁴ because it involves the electron experiencing the nuclear electric field, which scales with Z. For light atoms Z⁴ is small and electron-electron repulsion wins (LS coupling). For heavy atoms Z⁴ is enormous and spin-orbit wins (jj coupling). The Z~30–70 range shows intermediate coupling where neither dominates cleanly."

- question: "In jj coupling, L and S are still good quantum numbers — they are simply not used in spectroscopic labeling for convenience."
  type: true-false
  answer: false
  explanation: "This is a critical misconception. In jj coupling, L and S are genuinely not conserved quantities and cannot meaningfully label the quantum states. When spin-orbit coupling dominates, there is no single well-defined total orbital angular momentum or total spin — the good quantum numbers are the individual electron jᵢ values and the total J = Σjᵢ. LS term symbols like ³P₂ require knowing L and S; in heavy atoms these are simply undefined, not just inconvenient. This is why predicting the energy levels and spectra of heavy atoms requires jj coupling formalism, not LS coupling applied with caveats."

- question: "The coupling scheme (LS vs. jj) directly affects an atom's observable emission spectrum because different coupling schemes lead to different selection rules and different allowed transitions."
  type: true-false
  answer: true
  explanation: "Selection rules for radiative transitions depend on which quantum numbers are good. In LS coupling, the rules ΔL=±1, ΔS=0, ΔJ=0,±1 apply because L and S are well-defined. In jj coupling, selection rules are stated in terms of each electron's individual jᵢ: Δjᵢ=0,±1 for the active electron, while other electrons' jᵢ are unchanged. These different rules mean different transitions are allowed or forbidden, producing spectra with different line patterns and intensities. Naively applying LS selection rules to a heavy atom like lead would predict spectral lines that don't appear and miss lines that do."

- question: "Why does the coupling scheme for a multi-electron atom matter for predicting its spectrum, and what determines which scheme applies?"
  type: short-answer
  answer: "The coupling scheme determines which quantum numbers are conserved, which in turn determines the selection rules governing which transitions are allowed. In LS coupling (light atoms), L and S are good quantum numbers and the selection rules involve ΔL=±1, ΔS=0; in jj coupling (heavy atoms), individual jᵢ are good quantum numbers with their own selection rules, while L and S are not defined. Applying the wrong scheme predicts the wrong spectrum. What determines which scheme applies is the relative magnitude of electron-electron Coulomb repulsion versus spin-orbit coupling: LS coupling holds when repulsion dominates (Z ≲ 30), jj when spin-orbit dominates (Z ≳ 70). Spin-orbit coupling scales as Z⁴, which is why heavier atoms cross over to the jj regime."
  explanation: "The practical consequence is that spectroscopists working with heavy elements cannot use the familiar LS term-symbol machinery and must work in the jj framework or with full intermediate-coupling calculations. The coupling scheme is not just a labeling convention — it reflects the actual physical hierarchy of interactions and determines the observable properties of the atom."
```

## Explainer

From atomic selection rules you know that multi-electron atoms have quantum states labeled by total angular momentum quantum numbers — but *how* those totals are built from individual electron angular momenta is not fixed. It depends on which interaction is stronger: the **Coulomb repulsion** between electrons (which couples their orbital motions together) or the **spin-orbit interaction** for each electron individually (which couples each electron's spin to its own orbital motion). These two interactions compete, and their relative strength determines how we should add up the angular momenta.

In **LS coupling** (Russell-Saunders coupling), typical of light atoms (Z ≲ 30), electron-electron Coulomb repulsion dominates. The strong mutual electrostatic interaction makes all the orbital angular momenta ℓᵢ "speak" to each other rapidly, coupling them into a total orbital angular momentum L = Σℓᵢ. Independently, all the spins sᵢ couple into a total spin S = Σsᵢ. Only then does the comparatively weak spin-orbit interaction couple L and S together to form the total angular momentum J. The good quantum numbers are L, S, J, and M_J. Spectroscopic term symbols like ²S+¹L_J (e.g., ³P₂) encode exactly these numbers: the superscript is 2S+1, the letter encodes L, and the subscript is J.

In **jj coupling**, typical of heavy atoms (Z ≳ 70), spin-orbit coupling scales as Z⁴ and becomes dominant. Each electron's own ℓᵢ and sᵢ are strongly coupled *to each other*, forming an individual total jᵢ = ℓᵢ + sᵢ. The electrons then interact only weakly with each other (Coulomb repulsion is comparatively small), and the individual jᵢ couple to form total J = Σjᵢ. In this scheme, L and S are no longer good quantum numbers — the states cannot be cleanly labeled by total orbital and total spin angular momentum. Only J and M_J remain well-defined.

The crossover region between Z ≈ 30 and Z ≈ 70 shows neither scheme cleanly. Real atoms in this range exhibit **intermediate coupling**, where both interactions contribute comparably and neither L nor the individual jᵢ are good quantum numbers. Computational treatments must diagonalize the full Hamiltonian including both effects. The practical consequence for spectroscopy is that LS-coupled atoms (like helium, carbon, sodium) show characteristic patterns of fine-structure multiplets with predictable level spacings, while jj-coupled atoms (like lead, bismuth) show dramatically different level ordering that would be mispredicted if you naively applied LS term symbols. The coupling scheme also governs which transitions are allowed: selection rules for radiative transitions depend on which quantum numbers are good, so the observable spectra directly reflect the coupling regime.
