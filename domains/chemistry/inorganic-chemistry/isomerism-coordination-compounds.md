---
id: isomerism-coordination-compounds
title: Isomerism in Coordination Compounds
domain: chemistry
course: inorganic-chemistry
prerequisites:
- id: coordination-compounds-nomenclature
  type: hard
- id: crystal-field-theory
  type: soft
- id: vsepr-theory
  type: soft
builds-toward:
- reaction-mechanisms-coordination-compounds
tags:
- geometric isomerism
- optical isomerism
- linkage isomerism
- coordination isomers
stage: formal-systems
status: validated
---

# Isomerism in Coordination Compounds

## Core Idea
Coordination compounds exhibit a rich variety of isomerism — multiple distinct compounds sharing the same molecular formula but differing in the arrangement of atoms. Structural isomers differ in which atoms are bonded to which (linkage, ionization, coordination isomerism), while stereoisomers share the same connectivity but differ in spatial arrangement (geometric cis/trans and optical isomerism). Recognizing and predicting isomerism is essential for understanding reactivity and biological activity.

## Questions

```yaml
- question: "The compound [Co(NH₃)₄Cl₂]⁺ can exist as two geometric isomers. What are they, and how do their properties differ?"
  type: multiple-choice
  options:
    - "cis (both Cl⁻ adjacent, violet) and trans (both Cl⁻ opposite, green) isomers with identical chemical reactivity"
    - "cis (both Cl⁻ adjacent, violet) and trans (both Cl⁻ opposite, green) isomers with different colors, dipole moments, and reactivity"
    - "fac and mer isomers, differing only in their NMR spectra"
    - "d and l optical isomers that rotate plane-polarized light in opposite directions"
  answer: 1
  explanation: "In an octahedral complex with four NH₃ and two Cl⁻, the two chlorides can be adjacent (cis, 90° Cl-Co-Cl angle) or opposite (trans, 180° angle). These geometric isomers are physically distinct compounds: the cis isomer is violet and has a net dipole moment, while the trans isomer is green and has no dipole (the Cl-Co-Cl dipoles cancel). They also differ in reactivity — cis isomers undergo different substitution pathways. Option C describes fac/mer isomerism, which applies to MA₃B₃ octahedral complexes (three of each ligand), not MA₄B₂. Option D describes optical isomers, which are not possible for this compound."

- question: "An octahedral complex [Co(en)₃]³⁺ (where en = ethylenediamine) has no geometric isomers because all donor atoms are nitrogen. However, it can exist as two optical isomers (enantiomers)."
  type: true-false
  answer: true
  explanation: "All six donor atoms in [Co(en)₃]³⁺ are equivalent nitrogen atoms, so there is no possibility of geometric isomerism — every arrangement of three identical bidentate ligands around an octahedron gives the same connectivity pattern. However, the three en ligands create a propeller-like arrangement that is non-superimposable on its mirror image, making the complex chiral. The two enantiomers (designated Δ and Λ) rotate plane-polarized light in equal and opposite directions. This is significant in bioinorganic chemistry because biological systems often interact selectively with one enantiomer."

- question: "Linkage isomers like [Co(NH₃)₅(NO₂)]²⁺ and [Co(NH₃)₅(ONO)]²⁺ differ in which atom of the ambidentate ligand bonds to the metal."
  type: true-false
  answer: true
  explanation: "Nitrite (NO₂⁻) is an ambidentate ligand — it can coordinate through nitrogen (nitro, -NO₂) or through oxygen (nitrito, -ONO). The two linkage isomers have the same molecular formula and overall charge but different metal-ligand bonds: Co-N in the nitro form and Co-O in the nitrito form. These isomers have different colors (yellow nitro vs red nitrito), different stabilities, and can interconvert — the nitrito isomer typically converts to the more stable nitro isomer over time or upon heating."

- question: "Explain why square planar complexes of the type [MA₂B₂] exhibit geometric (cis/trans) isomerism, but tetrahedral complexes of the same type do not."
  type: short-answer
  answer: "In a square planar complex, the four coordination positions are not all equivalent with respect to each other: two positions are adjacent (90° apart, cis) and two are across from each other (180° apart, trans). Placing two B ligands in adjacent vs opposite positions creates geometrically distinct, non-interconvertible arrangements. In a tetrahedron, all four positions are equivalent — every pair of positions is separated by the same angle (109.5°). There is no 'opposite' position in a tetrahedron, so placing two B ligands in any two positions gives an arrangement that can be rotated to match any other placement. Therefore, only one isomer exists."
  explanation: "This geometric argument also explains why octahedral MA₂B₄ complexes show cis/trans isomerism (90° vs 180° positions exist) while trigonal bipyramidal complexes show axial/equatorial isomerism (distinct position types). Isomerism requires that the coordination geometry creates distinguishable positions."
```

## Explainer

Isomerism in coordination chemistry is far richer than in simple inorganic salts because the three-dimensional arrangement of ligands around a central metal creates multiple ways to assemble the same collection of atoms. The broadest division is between structural isomers (different connectivity) and stereoisomers (same connectivity, different spatial arrangement). Understanding which types of isomerism are possible for a given formula and geometry is a fundamental skill in inorganic chemistry.

Structural isomerism takes several forms. Linkage isomers arise from ambidentate ligands — ligands with more than one potential donor atom. The classic example is nitrite (NO₂⁻), which can bind through nitrogen (nitro) or oxygen (nitrito). Ionization isomers swap a ligand from inside the coordination sphere with a counter ion outside: [Co(NH₃)₅Br]SO₄ and [Co(NH₃)₅(SO₄)]Br dissolve to give different ions in solution. Coordination isomers, possible in compounds with both cationic and anionic complex ions, redistribute the ligands between the two metal centers.

Stereoisomerism in coordination compounds divides into geometric and optical types. Geometric isomerism is most familiar in octahedral and square planar complexes. An octahedral complex MA₄B₂ can have the two B ligands adjacent (cis) or opposite (trans), producing compounds with different colors, dipole moments, and reactivities. For MA₃B₃ octahedral complexes, the analogous distinction is facial (fac, three B ligands on one triangular face) versus meridional (mer, three B ligands in a plane through the metal). Tetrahedral complexes of the type MA₂B₂ do not exhibit geometric isomerism because all positions in a tetrahedron are equivalent — there is no distinction between adjacent and opposite.

Optical isomerism arises when a complex is non-superimposable on its mirror image — that is, when it is chiral. The most important examples are tris-bidentate octahedral complexes like [Co(en)₃]³⁺, where the three chelate rings create a helical arrangement. The two enantiomers, designated Δ (right-handed helix) and Λ (left-handed helix), are identical in all properties except their interaction with polarized light and with other chiral entities. This chirality has profound biological significance: many metalloenzymes have chiral active sites that select one enantiomer of a metal complex over the other, and cisplatin's anticancer activity depends critically on its geometric isomer — the trans form is inactive.
