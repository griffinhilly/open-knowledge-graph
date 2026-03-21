---
id: hybridization-introduction
title: Orbital Hybridization and Bonding Models
domain: chemistry
course: general-chemistry
prerequisites:
- id: sigma-pi-bonds-and-orbitals
  type: hard
- id: electron-configuration
  type: hard
builds-toward:
- molecular-geometry-basics
- organic-chemistry-intro
tags:
- hybridization
- orbitals
- bonding
- sp-orbitals
stage: advanced
status: draft
---

# Orbital Hybridization and Bonding Models

## Core Idea
Hybridization describes how atomic orbitals mix to form new hybrid orbitals suited for bonding. Common hybridization schemes are sp (linear), sp² (trigonal planar), and sp³ (tetrahedral), each yielding different molecular geometries and bond angles. Hybridization explains why bonding geometry often differs from pure orbital geometry.

## How It's Best Learned
Determine the number of electron groups around a central atom, predict hybridization, and sketch the geometry. Verify predictions using molecular models.

## Questions

```yaml
- question: "Ammonia (NH₃) has three N–H bonds. A student predicts it is sp² hybridized and has a flat, trigonal planar shape. What is the error in this reasoning?"
  type: multiple-choice
  options:
    - "Nitrogen cannot form sp² hybrid orbitals — only carbon can"
    - "The lone pair on nitrogen counts as an electron group and occupies a fourth sp³ orbital, giving a pyramidal shape"
    - "NH₃ is actually linear because nitrogen has only one lone pair"
    - "sp² hybridization would give bond angles of 90°, not 120°"
  answer: 1
  explanation: "This is the classic hybridization misconception: counting only bonds to predict hybridization and ignoring lone pairs. The rule is to count all electron groups — bonds AND lone pairs. Nitrogen in NH₃ has three bonds plus one lone pair, giving four electron groups. Four electron groups → sp³ hybridization → tetrahedral electron geometry. The three N–H bonds form the three corners of a trigonal pyramid; the lone pair occupies the fourth sp³ orbital and pushes the bonds downward, producing the observed pyramidal molecular shape."

- question: "Which statement best describes the relationship between hybridization and observed molecular geometry?"
  type: multiple-choice
  options:
    - "Hybridization is a physical process atoms undergo before bonding, rearranging their electrons into new orbitals"
    - "Hybridization is a mathematical model that correctly predicts bond angles and equivalent bond lengths, connecting electron configuration to molecular geometry"
    - "Hybridization applies only to carbon; other atoms use their unmodified atomic orbitals for bonding"
    - "Hybridization and VSEPR are competing theories; only one can be correct for a given molecule"
  answer: 1
  explanation: "Hybridization is a mathematical description, not a physical event. Atoms do not literally remix their orbitals before bonding occurs. The model's value is predictive: given electron configuration and electron group count, it correctly predicts bond angles, bond equivalence, and three-dimensional geometry. For example, it explains why methane's four C–H bonds are identical (all sp³) and why they point toward tetrahedral corners — something the unhybridized orbital picture cannot explain. Hybridization and VSEPR are complementary, not competing."

- question: "A carbon atom in acetylene (C₂H₂) uses sp hybridization, leaving two unhybridized p orbitals per carbon available for pi bonding."
  type: true-false
  answer: true
  explanation: "In sp hybridization, one s orbital mixes with one p orbital to produce two sp hybrid orbitals pointing in opposite directions (180°). This leaves two p orbitals per carbon untouched — one for each pi bond. In acetylene, the C≡C triple bond consists of one sigma bond (sp–sp overlap) and two pi bonds (from the two pairs of parallel p orbitals). This is why acetylene is linear: the two sp orbitals point in exactly opposite directions."

- question: "Hybridization is a physical process in which an atom's electrons reorganize into new orbitals before forming bonds with another atom."
  type: true-false
  answer: false
  explanation: "Hybridization is a mathematical model, not a real physical process. Atoms do not literally go through a remixing step before bonding. Rather, hybridization is a convenient theoretical framework that uses linear combinations of atomic orbital wavefunctions to produce hybrid orbitals that better match observed molecular geometries. Its value is entirely predictive — it works because it correctly describes the electron distribution in the bonded molecule, not because the atom physically rearranged itself."

- question: "Why does ammonia (NH₃) have a pyramidal shape rather than a flat trigonal arrangement, even though it has only three N–H bonds?"
  type: short-answer
  answer: "Ammonia has sp³ hybridization because nitrogen has four electron groups: three N–H bonds plus one lone pair. The lone pair occupies the fourth sp³ hybrid orbital, making the electron geometry tetrahedral. Since molecular shape describes only bond positions (not lone pairs), the three N–H bonds form a trigonal pyramid rather than a flat triangle. The lone pair still occupies space and exerts repulsion, compressing the H–N–H bond angles slightly below the ideal tetrahedral 109.5°."
  explanation: "The key insight is that lone pairs count as electron groups when predicting hybridization and geometry. A student who counts only bonds (three) might incorrectly predict sp² hybridization and a flat shape. Including the lone pair gives four groups → sp³ → tetrahedral electron geometry → pyramidal molecular geometry. This is why hybridization prediction always begins with counting ALL electron groups around the central atom."
```

## Explainer

From your study of electron configuration, you know that carbon's ground state has two electrons in the 2s orbital and two in separate 2p orbitals — which would suggest carbon should form only two bonds. But carbon routinely forms four equivalent bonds, as in methane (CH₄). Something about the simple atomic orbital picture does not match reality. **Hybridization** is the model that resolves this discrepancy: it proposes that atomic orbitals on the same atom can mathematically combine — or "mix" — to produce a new set of equivalent **hybrid orbitals** that are better suited for forming bonds.

The number of orbitals you mix equals the number of hybrid orbitals you get out. In **sp³ hybridization**, one s orbital and three p orbitals combine to produce four identical sp³ hybrid orbitals, each pointing toward the corner of a tetrahedron with 109.5° angles between them. This is exactly what we observe in methane: four equivalent C–H bonds arranged tetrahedrally. In **sp² hybridization**, one s orbital mixes with two p orbitals to produce three sp² hybrid orbitals in a trigonal planar arrangement (120° angles), leaving one unhybridized p orbital available for pi bonding — which you already know from your study of sigma and pi bonds. This is the bonding picture in ethylene (C₂H₄), where the double bond consists of one sigma bond (from sp² overlap) and one pi bond (from the leftover p orbitals). In **sp hybridization**, one s and one p orbital mix to give two sp hybrids pointing in opposite directions (180°), leaving two unhybridized p orbitals for pi bonds — as in acetylene (C₂H₂) with its triple bond.

The practical rule for predicting hybridization is straightforward: count the number of **electron groups** (bonds plus lone pairs) around the central atom. Two electron groups mean sp, three mean sp², and four mean sp³. A lone pair counts as an electron group just like a bond does — it occupies a hybrid orbital and affects the geometry. This is why ammonia (NH₃) is sp³ hybridized even though it has only three bonds: the lone pair occupies the fourth sp³ orbital, pushing the three N–H bonds into a pyramidal shape rather than a flat trigonal arrangement.

It is important to understand that hybridization is a model, not a physical process that atoms undergo. Atoms do not literally remix their orbitals before bonding. Rather, hybridization is a mathematical description that correctly predicts observed bond angles, bond equivalence, and molecular geometry. Its predictive power is what makes it valuable: given only the molecular formula, you can determine how many electron groups surround each atom, assign hybridization, and predict the three-dimensional shape of the molecule — connecting electron configuration directly to molecular geometry.
