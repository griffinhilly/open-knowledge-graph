---
id: molecular-spectroscopy-selection-rules
title: Selection Rules in Molecular Spectroscopy
domain: chemistry
course: physical-chemistry
prerequisites:
- id: electronic-spectroscopy-theory
  type: hard
- id: group-theory-molecular-symmetry
  type: hard
- id: selection-rules-spectroscopy
  type: soft
builds-toward:
- electronic-transitions-excited-states
- nmr-spectroscopy-spin-coupling
tags:
- spectroscopy
- selection-rules
- transitions
- symmetry
stage: advanced
status: draft
---

# Selection Rules in Molecular Spectroscopy

## Core Idea
Selection rules determine which transitions between energy levels are allowed by quantum mechanics, predicting whether spectral lines will appear or be absent. Spin, orbital angular momentum, and molecular symmetry all impose selection rules. Violating selection rules results in forbidden transitions with very low intensity or complete absence from the spectrum. Selection rules allow spectroscopists to assign observed spectra to specific molecular transitions.

## How It's Best Learned
Combine symmetry arguments with explicit transition dipole moment calculations. Use character tables from group theory to predict allowed transitions. Compare predictions with experimental spectra from databases.

## Common Misconceptions
- Forbidden transitions never occur (they do, but with much lower intensity from higher-order effects).
- Selection rules are the same in all types of spectroscopy (they vary significantly between UV-Vis, IR, Raman, etc.).

## Explainer

From electronic spectroscopy and group theory, you know that molecules absorb light to transition between energy levels and that molecular symmetry governs many physical properties. **Selection rules** connect these ideas by answering a precise question: for a given pair of energy levels, will the molecule actually absorb (or emit) a photon to make the transition? The answer comes from evaluating the **transition dipole moment integral** ⟨ψ_final|μ̂|ψ_initial⟩, where μ̂ is the dipole moment operator. If this integral is zero by symmetry, the transition is "forbidden" and will not appear in the spectrum (or will appear only very weakly). If it is nonzero, the transition is "allowed."

This is where group theory earns its keep. Rather than computing the integral explicitly, you can determine whether it is zero by inspecting **symmetry representations**. The rule is: the direct product of the representations of ψ_initial, the dipole operator μ̂, and ψ_final must contain the totally symmetric representation of the molecule's point group. If it does not, the integral vanishes by symmetry and the transition is forbidden. In practice, you look up the irreducible representations in the character table, take their direct product, and check whether A₁ (or whatever the totally symmetric species is called in that point group) appears. This symmetry-based approach lets you predict the entire absorption spectrum's structure without solving any integrals.

Different types of spectroscopy interact with molecules through different mechanisms, producing different selection rules. In **infrared (IR) spectroscopy**, the photon couples to changes in dipole moment, so a vibration is IR-active only if it changes the molecular dipole moment — symmetric stretches of homonuclear diatomics (like N₂ or O₂) are IR-inactive. In **Raman spectroscopy**, the photon couples to changes in polarizability, so the complementary rule applies: symmetric stretches that do not change the dipole are often Raman-active. For centrosymmetric molecules, the **rule of mutual exclusion** states that no vibration can be both IR- and Raman-active. In **electronic (UV-Vis) spectroscopy**, the key selection rules involve spin (ΔS = 0, transitions must conserve spin multiplicity) and orbital symmetry (Laporte rule: in centrosymmetric molecules, transitions between states of the same parity, g→g or u→u, are forbidden).

A crucial nuance is that "forbidden" does not mean "impossible." Forbidden transitions still occur, just with much lower intensity — sometimes 100 to 1,000,000 times weaker than allowed transitions. Mechanisms that relax selection rules include **vibronic coupling** (molecular vibrations temporarily break the symmetry that makes a transition forbidden), **spin-orbit coupling** (heavy atoms mix spin states, weakening the ΔS = 0 rule), and **magnetic dipole or electric quadrupole transitions** (higher-order interaction mechanisms with weaker but nonzero transition moments). Recognizing these weak, "forbidden" bands in experimental spectra — and understanding why they appear at all — is essential for correctly assigning molecular electronic structure.
