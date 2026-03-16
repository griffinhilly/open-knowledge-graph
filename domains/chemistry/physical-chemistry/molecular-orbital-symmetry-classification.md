---
id: molecular-orbital-symmetry-classification
title: Molecular Orbital Symmetry Classification
domain: chemistry
course: physical-chemistry
prerequisites:
- id: group-theory-molecular-symmetry
  type: hard
- id: molecular-orbital-theory-advanced
  type: hard
builds-toward:
- walsh-diagrams-structure-bonding-correlation
- selection-rules-spectroscopy
tags:
- symmetry
- molecular-orbitals
- group-theory
stage: advanced
status: draft
---

# Molecular Orbital Symmetry Classification

## Core Idea
Molecular orbitals are classified by symmetry labels (σ, π, δ) and point group irreducible representations. Symmetry determines orbital interactions—only orbitals of matching symmetry can mix and hybridize. This classification predicts which orbitals occupy which energies and which transitions are spectroscopically allowed, making it a powerful predictive tool.

## How It's Best Learned
Classify orbitals for small molecules (N₂, CO₂, H₂O) using point group operations. Construct MO diagrams using symmetry constraints and compare with ab initio calculations.

## Explainer

From group theory you know how to assign a molecule to its point group and work with symmetry operations, and from molecular orbital theory you know that atomic orbitals combine to form bonding and antibonding molecular orbitals. This topic connects the two: symmetry labels tell you which atomic orbitals are *allowed* to combine and which are forbidden from mixing, turning MO construction from guesswork into a systematic procedure.

The core principle is the **symmetry matching rule**: only atomic orbitals (or symmetry-adapted linear combinations of atomic orbitals) that belong to the same **irreducible representation** of the molecular point group can have nonzero overlap and therefore combine into molecular orbitals. Consider water (C₂ᵥ point group). The oxygen 2pz orbital transforms as the b₂ irreducible representation, and so does a specific combination of the two hydrogen 1s orbitals (their difference). Because they share the same symmetry label, they can mix to form a bonding MO and an antibonding MO. The oxygen 2px orbital transforms as b₁ — no hydrogen combination has that symmetry, so it remains a nonbonding lone pair. Symmetry alone, without any calculation, tells you which interactions are possible and which are zero by symmetry.

The familiar labels **σ**, **π**, and **δ** are themselves symmetry classifications for linear molecules. A σ orbital is symmetric with respect to rotation about the bond axis (it belongs to the totally symmetric representation of the C∞ᵥ or D∞ₕ point group). A π orbital has a single nodal plane containing the bond axis and changes sign under 180° rotation — it belongs to a doubly degenerate representation. A δ orbital has two nodal planes and appears in transition metal complexes. For nonlinear molecules, you replace these simple labels with the irreducible representation labels of the appropriate point group (a₁, b₂, e, t₂, etc.), but the underlying logic is identical: the symmetry label tells you the orbital's behavior under every symmetry operation of the molecule.

This classification has direct physical consequences. **Selection rules** for spectroscopic transitions follow from symmetry: a transition is allowed only if the direct product of the initial state symmetry, the transition operator symmetry, and the final state symmetry contains the totally symmetric representation. Without symmetry classification of the orbitals, you cannot apply selection rules, and without selection rules, you cannot predict which transitions appear in a spectrum. Symmetry classification also determines orbital energy ordering — orbitals of the same symmetry can interact (and push each other apart in energy), while orbitals of different symmetry cross without interacting. This is the basis for constructing correlation diagrams and Walsh diagrams that predict how molecular geometry affects electronic structure.
