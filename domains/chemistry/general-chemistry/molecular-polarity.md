---
id: molecular-polarity
title: Molecular Polarity and Dipole Moments
domain: chemistry
course: general-chemistry
prerequisites:
- id: vsepr-theory
  type: hard
- id: periodic-trends
  type: soft
- id: resonance-and-formal-charge
  type: soft
builds-toward:
- intermolecular-forces
tags:
- dipole-moment
- polar-molecule
- nonpolar-molecule
- symmetry
- bond-dipole
stage: formal-systems
status: validated
---

# Molecular Polarity and Dipole Moments

## Core Idea
A molecule is polar if it contains polar bonds whose bond dipole moments do not cancel due to molecular geometry. Bond polarity arises from electronegativity differences between bonded atoms, and the molecular dipole moment is the vector sum of all bond dipoles. Symmetric molecules — like CO₂ (linear) or CCl₄ (tetrahedral) — have polar bonds that cancel exactly, making the molecule nonpolar overall. Molecular polarity governs solubility ('like dissolves like'), boiling point, and reactivity.

## How It's Best Learned
Combine VSEPR geometry with electronegativity trends to classify molecules as polar or nonpolar. Draw bond dipole arrows and check whether they cancel by symmetry. Water's bent geometry (due to lone pairs) prevents its bond dipoles from canceling — contrast with CO₂.

## Common Misconceptions
- Having polar bonds does not make a molecule polar — symmetry can cancel all bond dipoles even in highly polar bonds (e.g., BF₃, CCl₄).
- Water's polarity comes not just from O–H bond polarity but from the asymmetric geometry imposed by its two lone pairs.

## Questions

```yaml
- question: "Which of the following molecules contains polar bonds but has a net dipole moment of zero?"
  type: multiple-choice
  options: ["H₂O", "NH₃", "CO₂", "HCl"]
  answer: 2
  explanation: "CO₂ is linear, so its two identical C=O bond dipoles point in exactly opposite directions and cancel, giving a zero net dipole moment. H₂O (bent), NH₃ (trigonal pyramidal), and HCl (diatomic, asymmetric) all have net dipole moments because their bond dipoles do not cancel by symmetry."

- question: "Any molecule that contains polar bonds is a polar molecule."
  type: true-false
  answer: false
  explanation: "Molecular polarity depends on both bond polarity AND molecular geometry. If polar bonds are arranged symmetrically, their vector dipoles cancel and the net dipole moment is zero. CCl₄ (tetrahedral) and BF₃ (trigonal planar) are classic examples: all bonds are polar, but the symmetric arrangement produces a nonpolar molecule."

- question: "Both CO₂ and H₂O contain polar covalent bonds. Why is CO₂ nonpolar while H₂O is polar?"
  type: short-answer
  answer: "CO₂ is linear — its two C=O bond dipoles point in opposite directions and cancel exactly. H₂O is bent (due to two lone pairs on oxygen), so its two O–H bond dipoles point in directions that do not cancel, producing a net dipole moment pointing toward oxygen."
  explanation: "Geometry is the deciding factor. The VSEPR model predicts CO₂ as linear (no lone pairs on carbon) and H₂O as bent (two lone pairs on oxygen repel the bonding pairs). In CO₂, the 180° bond angle guarantees perfect cancellation. In H₂O, the ~104.5° bond angle means the two O–H dipoles add to a net downward vector (toward O), making the molecule polar."
```

## Explainer

Molecular polarity is the result of two factors working together: individual bond polarity and molecular geometry. You already know from electronegativity trends that when two different atoms share electrons, the more electronegative atom pulls electron density toward itself, creating a bond dipole — a small separation of positive and negative charge along that bond. But whether the molecule as a whole is polar depends on whether those individual bond dipoles add up to a nonzero net vector, or cancel each other out.

Think of bond dipoles as arrows pointing from the less electronegative atom toward the more electronegative one. The molecular dipole moment is the vector sum of all these arrows. If the geometry is symmetric, the arrows point in directions that exactly oppose each other and cancel. This is the case for CO₂: it has two very polar C=O bonds, but the molecule is linear, so the two bond dipole arrows point in exactly opposite directions (left and right). They cancel completely — net dipole moment = 0. Despite having highly polar bonds, CO₂ is a nonpolar molecule.

Water is the contrasting case. Oxygen is highly electronegative, making the O–H bonds quite polar. But here, geometry makes all the difference. VSEPR predicts that oxygen's two lone pairs push the bonding pairs into a bent shape (~104.5°). The two O–H bond dipoles both point partially toward the oxygen but are angled, so they do not cancel — they add to a net dipole pointing toward the oxygen atom. Water is a polar molecule with a significant dipole moment (1.85 D), which explains its high boiling point, surface tension, and its role as an excellent solvent for ionic and polar compounds.

The practical payoff of understanding molecular polarity is the "like dissolves like" rule. Polar solvents like water dissolve polar solutes and ionic compounds because they can interact favorably via dipole-dipole forces and ion-dipole interactions. Nonpolar solvents like hexane dissolve nonpolar solutes because both interact via London dispersion forces and do not disrupt each other's favorable interactions. When you combine a polar solute with a nonpolar solvent, neither side benefits energetically, and dissolution is unfavorable. This logic flows directly from molecular dipole moments.
