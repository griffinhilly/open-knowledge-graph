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

## Questions

```yaml
- question: "Two atomic orbitals are very close in energy but belong to different irreducible representations of the molecule's point group. Can they mix to form molecular orbitals?"
  type: multiple-choice
  options:
    - "Yes — energy proximity is the primary criterion for orbital mixing"
    - "No — only orbitals of matching symmetry (same irreducible representation) can mix, regardless of energy"
    - "Yes — but the mixing will be weak because of the symmetry mismatch"
    - "Only if both orbitals are of σ type"
  answer: 1
  explanation: "Symmetry is a hard constraint, not a preference. The overlap integral between orbitals of different irreducible representations is exactly zero by symmetry — no matter how close in energy they are, there is no interaction. This surprises students who assume that 'similar energy → mixing.' Energy proximity determines the *degree* of mixing when symmetry allows it, but symmetry determines *whether* mixing is allowed at all."

- question: "In water (C₂ᵥ symmetry), the oxygen 2px orbital belongs to the b₁ irreducible representation. No hydrogen orbital combination shares that symmetry. What type of orbital does the oxygen 2px become in the water MO diagram?"
  type: multiple-choice
  options:
    - "A strongly bonding orbital — it overlaps broadly with the hydrogen 1s orbitals"
    - "A strongly antibonding orbital — its mismatched symmetry causes destructive interference"
    - "A nonbonding lone pair — it cannot interact with any hydrogen combination"
    - "A σ* orbital — it cancels the contribution of the bonding σ orbital"
  answer: 2
  explanation: "When an atomic orbital has no partner of matching symmetry among the other basis orbitals, it cannot mix into any bonding or antibonding MO. It remains as a pure nonbonding orbital — its energy is unchanged from the isolated atom, and it constitutes a lone pair. This is how MO theory predicts the existence and location of lone pairs without any empirical guessing."

- question: "In a linear molecule, the labels σ, π, and δ are themselves symmetry classifications — σ orbitals are symmetric with respect to rotation about the bond axis, while π orbitals have one nodal plane containing the bond axis."
  type: true-false
  answer: true
  explanation: "Exactly right. σ, π, and δ are not just conventional labels — they encode the orbital's behavior under the symmetry operations of the linear molecule's point group (C∞ᵥ or D∞ₕ). A σ orbital is totally symmetric with respect to rotation; a π orbital changes sign under 180° rotation and is doubly degenerate. For nonlinear molecules, these simple labels are replaced by irreducible representation labels of the appropriate point group, but the logic is identical."

- question: "Two orbitals can always be made to interact by adjusting the molecular geometry, even if they currently belong to different irreducible representations."
  type: true-false
  answer: false
  explanation: "Changing geometry changes the point group and can change which irreducible representation each orbital belongs to — so geometry changes can sometimes enable previously forbidden interactions. However, for a fixed geometry with a fixed point group, the symmetry constraint is absolute: orbitals of different irreducible representations have zero overlap and cannot mix. The statement inverts cause and effect: it is the geometry that determines the symmetry labels, not the other way around."

- question: "Explain why the symmetry matching rule — that only orbitals of the same irreducible representation can mix — allows chemists to predict molecular orbital diagrams without doing any quantum mechanical calculations."
  type: short-answer
  answer: "Because the overlap integral between orbitals of different irreducible representations is exactly zero, which can be proved from symmetry alone without computing any integrals. Group theory therefore tells you which interactions are forbidden (zero overlap by symmetry) and which are allowed (potentially nonzero overlap). This reduces MO construction to asking 'what symmetry does each atomic orbital transform as?' and grouping orbitals accordingly. The energy ordering within allowed interactions requires calculation, but the pattern of which orbitals interact at all is determined by symmetry alone."
  explanation: "This is the central power of group theory applied to chemistry. Instead of solving the Schrödinger equation for every molecule from scratch, you identify the point group, assign irreducible representations to each atomic orbital, and immediately know the allowed interactions. Orbitals of the same irreducible representation form bonding/antibonding pairs; orbitals with no symmetry-matching partners become nonbonding. The entire MO diagram topology follows from symmetry before any energy calculation begins."
```

## Explainer

From group theory you know how to assign a molecule to its point group and work with symmetry operations, and from molecular orbital theory you know that atomic orbitals combine to form bonding and antibonding molecular orbitals. This topic connects the two: symmetry labels tell you which atomic orbitals are *allowed* to combine and which are forbidden from mixing, turning MO construction from guesswork into a systematic procedure.

The core principle is the **symmetry matching rule**: only atomic orbitals (or symmetry-adapted linear combinations of atomic orbitals) that belong to the same **irreducible representation** of the molecular point group can have nonzero overlap and therefore combine into molecular orbitals. Consider water (C₂ᵥ point group). The oxygen 2pz orbital transforms as the b₂ irreducible representation, and so does a specific combination of the two hydrogen 1s orbitals (their difference). Because they share the same symmetry label, they can mix to form a bonding MO and an antibonding MO. The oxygen 2px orbital transforms as b₁ — no hydrogen combination has that symmetry, so it remains a nonbonding lone pair. Symmetry alone, without any calculation, tells you which interactions are possible and which are zero by symmetry.

The familiar labels **σ**, **π**, and **δ** are themselves symmetry classifications for linear molecules. A σ orbital is symmetric with respect to rotation about the bond axis (it belongs to the totally symmetric representation of the C∞ᵥ or D∞ₕ point group). A π orbital has a single nodal plane containing the bond axis and changes sign under 180° rotation — it belongs to a doubly degenerate representation. A δ orbital has two nodal planes and appears in transition metal complexes. For nonlinear molecules, you replace these simple labels with the irreducible representation labels of the appropriate point group (a₁, b₂, e, t₂, etc.), but the underlying logic is identical: the symmetry label tells you the orbital's behavior under every symmetry operation of the molecule.

This classification has direct physical consequences. **Selection rules** for spectroscopic transitions follow from symmetry: a transition is allowed only if the direct product of the initial state symmetry, the transition operator symmetry, and the final state symmetry contains the totally symmetric representation. Without symmetry classification of the orbitals, you cannot apply selection rules, and without selection rules, you cannot predict which transitions appear in a spectrum. Symmetry classification also determines orbital energy ordering — orbitals of the same symmetry can interact (and push each other apart in energy), while orbitals of different symmetry cross without interacting. This is the basis for constructing correlation diagrams and Walsh diagrams that predict how molecular geometry affects electronic structure.
