---
id: selection-rules-electronic-spectroscopy
title: Selection Rules for Electronic Transitions
domain: chemistry
course: physical-chemistry
prerequisites:
- id: character-tables-spectroscopic-applications
  type: hard
- id: electronic-spectroscopy-theory
  type: hard
builds-toward:
- excited-state-decay-pathways
tags:
- spectroscopy
- selection-rules
- symmetry
- transitions
stage: advanced
status: draft
---

# Selection Rules for Electronic Transitions

## Core Idea
Selection rules determine which electronic transitions are allowed based on symmetry (Δℓ = ±1 for parity; ΔS = 0 for spin) and operator symmetry. Strong UV-Vis absorptions arise from symmetry-allowed π→π* and n→π* transitions; forbidden transitions may proceed via spin-orbit coupling or vibronic mixing. These rules explain observed absorption intensities and guide assignment of spectroscopic data.

## Explainer

From your work with character tables and electronic spectroscopy theory, you know that molecules absorb light when a photon promotes an electron from one orbital to another. But not every conceivable transition actually occurs — nature imposes **selection rules** that determine which transitions are allowed and which are forbidden. These rules arise from the mathematics of how light interacts with matter: a transition only happens if the transition dipole moment integral is nonzero. If symmetry forces that integral to vanish, the transition is forbidden.

The two most important selection rules for electronic spectroscopy are the **spin selection rule** and the **Laporte (parity) selection rule**. The spin rule says ΔS = 0: the total spin must not change during the transition. Singlet-to-singlet transitions are allowed; singlet-to-triplet transitions are forbidden because the electric dipole operator does not act on spin. The Laporte rule applies to centrosymmetric molecules and states that the transition must involve a change in parity — allowed transitions go from g (gerade) to u (ungerade) or vice versa, meaning Δℓ = ±1 in atomic terms. In practice, d-d transitions in octahedral metal complexes are Laporte-forbidden because both states have the same parity, which is why transition metal complexes often have relatively pale colors compared to organic dyes.

The key insight from group theory is that a transition is allowed only when the direct product of the symmetry representations of the initial state, the transition dipole operator, and the final state contains the totally symmetric representation. Character tables let you evaluate this quickly: look up the irreducible representations of the ground state and excited state, then check whether any component of the dipole operator (which transforms like x, y, or z) connects them. Common allowed transitions in organic molecules include **π → π\*** (strong, giving intense UV absorptions in conjugated systems) and **n → π\*** (weaker, because the spatial overlap between the nonbonding orbital and the π\* orbital is poor).

"Forbidden" does not mean "impossible" — it means "weak." Several mechanisms can relax selection rules. **Spin-orbit coupling** mixes singlet and triplet states, partially lifting the spin selection rule; this is especially important in molecules containing heavy atoms where spin-orbit coupling is strong, enabling phosphorescence. **Vibronic coupling** (the mixing of electronic and vibrational motions) can break the Laporte rule: molecular vibrations temporarily distort the geometry away from centrosymmetry, allowing transitions that would be strictly forbidden in the equilibrium geometry. This is why d-d bands in octahedral complexes are weak but not absent. Understanding which mechanism lifts a particular selection rule lets you predict not just whether a band appears, but how intense it will be — strong absorptions (ε > 1000) indicate fully allowed transitions, while weak ones (ε < 100) typically indicate formally forbidden transitions rescued by vibronic or spin-orbit effects.
