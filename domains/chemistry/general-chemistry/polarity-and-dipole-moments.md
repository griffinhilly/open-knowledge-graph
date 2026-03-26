---
id: polarity-and-dipole-moments
title: Molecular Polarity and Dipole Moments
domain: chemistry
course: general-chemistry
prerequisites:
- id: molecular-geometry-prediction
  type: hard
- id: polar-covalent-bonds-and-dipoles
  type: soft
builds-toward:
- intermolecular-forces
- solution-properties
tags:
- polarity
- dipole moment
- electronegativity
- bond dipole
stage: formal-systems
status: validated
---
# Molecular Polarity and Dipole Moments

## Core Idea
Molecular polarity results from both bond polarity (electronegativity difference) and molecular geometry. Polar molecules have unequal charge distribution and a net dipole moment; nonpolar molecules have either no bond dipoles or symmetric cancellation. Polarity determines solubility, boiling point, and intermolecular forces.

## Questions

```yaml
- question: "CO₂ has two highly polar C=O double bonds, yet it does not dissolve well in water and has no net dipole moment. A student argues that since polar bonds are present, the molecule must be polar. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "The C=O bonds are actually nonpolar because carbon and oxygen have similar electronegativities"
    - "CO₂ is polar, but it dissolves poorly in water for unrelated reasons"
    - "Molecular polarity depends on both bond polarity and geometry; CO₂'s linear shape causes the two equal and opposite C=O dipoles to cancel exactly, yielding zero net dipole moment"
    - "CO₂ becomes polar in water because the solvent induces an asymmetric electron distribution"
  answer: 2
  explanation: "The student is confusing bond polarity with molecular polarity — the central misconception this topic addresses. Both C=O bonds are polar (oxygen is more electronegative than carbon), but in linear CO₂, the two bond dipole vectors point in exactly opposite directions and cancel. Vector cancellation requires both equal magnitude *and* opposite direction — which the linear geometry ensures. Water (H₂O) also has polar O-H bonds, but its bent geometry means the dipoles don't cancel: they point in roughly the same direction and sum to a large net dipole. The difference between CO₂ and H₂O comes entirely from geometry, not bond polarity."

- question: "Which of the following molecules has polar bonds but is overall nonpolar due to its geometry?"
  type: multiple-choice
  options:
    - "Water (H₂O) — bent geometry, two polar O-H bonds"
    - "Ammonia (NH₃) — trigonal pyramidal, three polar N-H bonds"
    - "Carbon tetrachloride (CCl₄) — tetrahedral with four identical C-Cl bonds that cancel by symmetry"
    - "Hydrogen fluoride (HF) — one polar H-F bond, no cancellation possible"
  answer: 2
  explanation: "CCl₄ is the classic example: each C-Cl bond is polar (chlorine is more electronegative), but the four identical bonds point symmetrically outward in a perfect tetrahedron. Vector addition of four equal dipoles arranged tetrahedrally gives exactly zero. H₂O and NH₃ are polar despite simple structures because their geometries are asymmetric — lone pairs on the central atom distort the shape, preventing cancellation. HF is polar because a diatomic molecule with one polar bond cannot cancel. The rule: symmetric molecules with identical substituents are nonpolar; asymmetry (from lone pairs or mixed substituents) typically produces a net dipole."

- question: "A molecule with a lone pair on the central atom is likely to be polar even if all the peripheral atoms are the same element."
  type: true-false
  answer: true
  explanation: "Lone pairs on the central atom create asymmetry in the molecular geometry. In water (O with 2 lone pairs) and ammonia (N with 1 lone pair), the lone pair pushes the bonding pairs asymmetrically, creating a bent or pyramidal shape. The bond dipoles then point in directions that do not cancel. Compare with BF₃ (no lone pair, trigonal planar) — all three B-F dipoles cancel to zero. Or CH₄ (no lone pair, perfect tetrahedron) — also zero. The lone pair is geometrically equivalent to a substituent that contributes no bond dipole but distorts the shape, breaking the symmetry needed for cancellation."

- question: "Any molecule containing bonds between atoms of different electronegativity must have a nonzero dipole moment."
  type: true-false
  answer: false
  explanation: "This confuses bond polarity with molecular polarity. Many molecules have polar bonds that cancel due to symmetric geometry: CO₂ (linear), CCl₄ (tetrahedral), BF₃ (trigonal planar), and SF₆ (octahedral) all have polar bonds but zero dipole moments because their symmetry causes perfect vector cancellation. The existence of polar bonds is a necessary but not sufficient condition for molecular polarity — the geometry must also prevent cancellation. This is why you cannot assess molecular polarity from the formula alone; you must know the three-dimensional structure."

- question: "Explain why CO₂ is nonpolar while H₂O is polar, even though both molecules have two polar bonds to electronegative atoms."
  type: short-answer
  answer: "In CO₂, the molecule is linear — the two C=O bond dipoles point in exactly opposite directions (180° apart) and cancel by vector addition to give a net dipole moment of zero. The symmetry of linear geometry ensures perfect cancellation. In H₂O, the molecule has a bent geometry (approximately 104.5° bond angle) due to the two lone pairs on oxygen. The two O-H bond dipoles both point roughly from the hydrogens toward oxygen, and because they are not antiparallel, their vector sum produces a substantial net dipole moment pointing along the bisector of the H-O-H angle. Same number of polar bonds, completely different geometry — completely different polarity."
  explanation: "The key insight is that polarity is a property of the whole molecule, determined by how bond dipole vectors add up in three dimensions. Geometry is the deciding factor. This is also why predicting polarity requires knowing the molecular shape (from VSEPR) before asking about bond dipoles."
```

## Explainer

From molecular geometry prediction, you know how to determine the three-dimensional shape of a molecule using VSEPR theory. Polarity asks the next question: given that shape, does the molecule have an uneven distribution of electrical charge? The answer depends on two things working together — **bond polarity** (are individual bonds polar?) and **molecular geometry** (do those bond dipoles cancel or add up?).

A **bond dipole** arises whenever two atoms with different electronegativities share electrons. In HCl, chlorine is more electronegative than hydrogen, so the shared electrons spend more time near chlorine. This creates a partial negative charge (δ−) on chlorine and a partial positive charge (δ+) on hydrogen. The bond dipole is a vector pointing from the positive end toward the negative end, and its magnitude depends on the electronegativity difference and the bond length. Larger electronegativity differences produce stronger bond dipoles.

The critical insight is that **molecular polarity is not the same as bond polarity**. A molecule can have polar bonds yet be nonpolar overall if the geometry causes the bond dipoles to cancel. Carbon dioxide (CO₂) has two highly polar C=O bonds, but its linear geometry means the two bond dipoles point in exactly opposite directions and cancel to zero — CO₂ is nonpolar. Water (H₂O) also has two polar O−H bonds, but its bent geometry means the dipoles point in roughly the same direction and add together to produce a net **dipole moment** — water is polar. The shape determines whether the tug-of-war between bond dipoles results in a winner or a draw.

To assess molecular polarity, treat each bond dipole as a vector arrow and add them using vector addition. Symmetric molecules — linear with identical bonds, trigonal planar, tetrahedral with four identical substituents — always cancel. Asymmetric geometries — bent, trigonal pyramidal, or any shape with lone pairs on the central atom or different substituents — generally produce a net dipole. The **dipole moment** (measured in debyes, D) quantifies the magnitude of this charge separation. Polarity has far-reaching consequences: polar molecules dissolve in polar solvents ("like dissolves like"), experience stronger intermolecular forces (raising boiling points), and interact with electric fields. Understanding polarity bridges the gap between individual bond properties and the bulk behavior of substances.
