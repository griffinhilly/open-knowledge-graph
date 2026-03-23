---
id: molecular-geometry-basics
title: Molecular Geometry and Electron Pair Geometry
domain: chemistry
course: general-chemistry
prerequisites:
- id: vsepr-theory
  type: soft
- id: lewis-structures
  type: hard
builds-toward:
- molecular-polarity
- reaction-mechanisms-overview
tags:
- geometry
- vsepr
- shape
- bonds
stage: formal-systems
status: validated
---

# Molecular Geometry and Electron Pair Geometry

## Core Idea
Molecular geometry describes the 3D arrangement of atoms in a molecule, while electron pair geometry includes both bonding and lone pairs. Repulsive forces between electron pairs (bonding and lone) determine the geometry. Lone pairs occupy more space than bonding pairs, affecting actual molecular shapes.

## Questions

```yaml
- question: "A molecule has 3 bonding pairs and 1 lone pair on its central atom. What are its electron pair geometry and molecular geometry?"
  type: multiple-choice
  options:
    - "Electron pair geometry: trigonal planar; Molecular geometry: trigonal planar"
    - "Electron pair geometry: tetrahedral; Molecular geometry: trigonal pyramidal"
    - "Electron pair geometry: tetrahedral; Molecular geometry: tetrahedral"
    - "Electron pair geometry: trigonal pyramidal; Molecular geometry: tetrahedral"
  answer: 1
  explanation: "4 electron groups (3 bonding + 1 lone pair) produce a tetrahedral electron pair geometry. But molecular geometry describes only where the atoms are — the lone pair is invisible in the shape name. With 3 bonded atoms arranged around a central atom with one lone pair pushing down, you get a tripod-like structure — trigonal pyramidal. Ammonia (NH₃) is the classic example. Option 2 (tetrahedral molecular geometry) is wrong because molecular geometry cannot include the lone pair in its shape description."

- question: "Water has a bond angle of approximately 104.5° rather than the ideal tetrahedral 109.5°. What best explains this compression?"
  type: multiple-choice
  options:
    - "Water has only 2 bonding pairs, so the bond angle is naturally smaller than in molecules with 4 bonds"
    - "Oxygen is electronegative, pulling bonding electrons toward itself and compressing the angle between the bonds"
    - "The two lone pairs repel the bonding pairs more strongly than bonding pairs repel each other, pushing the H–O–H angle inward"
    - "Water's geometry is trigonal planar, which has a smaller ideal angle than tetrahedral"
  answer: 2
  explanation: "The repulsion hierarchy is: lone pair–lone pair > lone pair–bonding pair > bonding pair–bonding pair. Lone pairs spread out more than bonding pairs because they are held by only one nucleus rather than pinned between two atoms. In water, two lone pairs squeeze the two O–H bonding pairs closer together, compressing the angle from the ideal 109.5° to ~104.5°. Option 0 misidentifies the cause — the tetrahedral electron pair geometry is set by all 4 groups; the compression comes from the lone pair's stronger repulsion."

- question: "Water and methane both have 4 electron groups around their central atom, but they have different molecular geometries."
  type: true-false
  answer: true
  explanation: "Methane (CH₄) has 4 bonding pairs and 0 lone pairs — both its electron pair geometry and its molecular geometry are tetrahedral. Water (H₂O) also has 4 electron groups (2 bonding + 2 lone pairs), giving it a tetrahedral electron pair geometry, but its molecular geometry is bent because only the 2 bonded hydrogen atoms define the shape. Lone pairs are not atoms and do not contribute to the molecular geometry name — their presence changes the shape without appearing in it."

- question: "In VSEPR theory, a double bond counts as two electron groups because it contains two pairs of electrons."
  type: true-false
  answer: false
  explanation: "In VSEPR theory, each bond — single, double, or triple — counts as exactly ONE electron group, regardless of how many electron pairs it contains. All the electrons in a double bond are concentrated in the same region between the two atoms, so they repel neighboring groups as a single unit. CO₂, with two double bonds on carbon, has only 2 electron groups and a linear geometry — not 4 groups giving a tetrahedral shape."

- question: "Why do lone pairs on a central atom cause actual bond angles to be smaller than the ideal electron pair geometry predicts?"
  type: short-answer
  answer: "Lone pairs are held by only one nucleus rather than shared between two atoms, so their electron cloud spreads out more in space. This makes lone pairs stronger repellers of neighboring electron groups than bonding pairs are. When lone pairs push on adjacent bonding pairs, they squeeze those bonds closer together, compressing the angle below the ideal value. The more lone pairs present, the greater the compression — water (two lone pairs) has a smaller angle than ammonia (one lone pair), both relative to the ideal tetrahedral 109.5°."
  explanation: "The repulsion hierarchy — LP-LP > LP-BP > BP-BP — is the quantitative expression of this effect. Understanding it lets you not just name molecular geometries but also predict whether bond angles will be above or below ideal values, which directly affects molecular polarity: the next concept that builds on this one."
```

## Explainer

From drawing Lewis structures, you can determine how many bonding pairs and lone pairs surround a central atom. Molecular geometry takes that 2D blueprint and answers the 3D question: what shape does the molecule actually adopt in space? The governing principle is simple — electron pairs repel each other (they're all negatively charged), so they arrange themselves as far apart as possible. This is the core idea behind VSEPR (Valence Shell Electron Pair Repulsion) theory.

Start by counting the total number of **electron groups** around the central atom — each bond (single, double, or triple counts as one group) and each lone pair is one group. The number of groups determines the **electron pair geometry**: 2 groups → linear (180°), 3 → trigonal planar (120°), 4 → tetrahedral (109.5°), 5 → trigonal bipyramidal, 6 → octahedral. These are the idealized arrangements that maximize the distance between electron groups. For example, methane (CH₄) has 4 bonding groups and no lone pairs on carbon, so both its electron pair geometry and its molecular geometry are tetrahedral.

The crucial distinction is between **electron pair geometry** (which includes all electron groups) and **molecular geometry** (which describes only where the atoms are). When lone pairs are present, the molecular geometry differs from the electron pair geometry because lone pairs are invisible in the molecular shape — you can't "see" where they are, only the atoms. Water (H₂O) has 4 electron groups on oxygen (2 bonding, 2 lone pairs), so its electron pair geometry is tetrahedral, but its molecular geometry is **bent** because you only see the two hydrogen atoms. Ammonia (NH₃) also has a tetrahedral electron pair geometry (3 bonding, 1 lone pair) but a **trigonal pyramidal** molecular geometry.

Lone pairs don't just change the name of the shape — they compress bond angles. A lone pair's electron cloud spreads out more than a bonding pair's (it's held by only one nucleus, not pinned between two), so it repels neighboring groups more strongly. This is why water's H–O–H angle is about 104.5° rather than the ideal tetrahedral 109.5°, and why ammonia's H–N–H angle is about 107°. The hierarchy of repulsion is: lone pair–lone pair > lone pair–bonding pair > bonding pair–bonding pair. Understanding this hierarchy lets you predict not just the qualitative shape but also whether bond angles will be compressed or expanded relative to the ideal values — information that directly affects molecular polarity, which is the next concept you'll build toward.
