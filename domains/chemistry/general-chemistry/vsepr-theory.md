---
id: vsepr-theory
title: VSEPR Theory and Molecular Geometry
domain: chemistry
course: general-chemistry
prerequisites:
- id: lewis-structures
  type: hard
builds-toward:
- molecular-polarity
tags:
- vsepr
- electron-geometry
- molecular-geometry
- bond-angles
- lone-pairs
- hybridization
stage: formal-systems
status: validated
---

# VSEPR Theory and Molecular Geometry

## Core Idea
VSEPR (Valence Shell Electron Pair Repulsion) theory predicts molecular geometry by assuming that electron groups (bonding pairs and lone pairs) around a central atom arrange to minimize repulsion. The number of electron groups determines electron geometry: 2 → linear, 3 → trigonal planar, 4 → tetrahedral, 5 → trigonal bipyramidal, 6 → octahedral. Lone pairs repel more strongly than bonding pairs, compressing bond angles and distinguishing molecular geometry (atom positions only) from electron geometry (all groups).

## How It's Best Learned
Work through a large variety of molecules systematically: count all electron groups, determine electron geometry, identify lone pairs, then name molecular geometry. Build physical models to develop 3D intuition. Compare H₂O (bent, 104.5°) vs. CH₄ (tetrahedral, 109.5°) to see the effect of lone pairs on angles.

## Common Misconceptions
- VSEPR electron geometry and molecular geometry are different: water has tetrahedral electron geometry but bent molecular geometry.
- Double and triple bonds count as one electron group in VSEPR, not two or three — a carbon with two double bonds is linear (like CO₂), not bent.

## Questions

```yaml
- question: "Water (H₂O) has four electron groups around oxygen (two bonding pairs and two lone pairs). What is the correct sequence of electron geometry → molecular geometry?"
  type: multiple-choice
  options:
    - "Bent electron geometry → tetrahedral molecular geometry"
    - "Tetrahedral electron geometry → bent molecular geometry"
    - "Tetrahedral electron geometry → tetrahedral molecular geometry"
    - "Trigonal planar electron geometry → bent molecular geometry"
  answer: 1
  explanation: "Four electron groups produce tetrahedral electron geometry (the arrangement minimizing repulsion among four groups). But molecular geometry describes only where the atoms are — two O–H bonds are visible while two lone pairs are not. Since we see only two atoms attached to oxygen, the molecular geometry is bent. This is the essential VSEPR distinction: electron geometry counts everything; molecular geometry counts only atom positions. Confusing the two is the most common VSEPR error."

- question: "Carbon dioxide (CO₂) has the Lewis structure O=C=O with two double bonds. What is the molecular geometry?"
  type: multiple-choice
  options:
    - "Bent — the two double bonds create more electron density and repel each other more strongly"
    - "Trigonal planar — there are two bonding regions plus carbon's lone pair"
    - "Linear — each double bond counts as one electron group, giving two total groups at 180°"
    - "Tetrahedral — each double bond contains four electrons, totaling eight electrons around carbon"
  answer: 2
  explanation: "The critical VSEPR rule: a double bond counts as ONE electron group, regardless of how many electron pairs it contains. CO₂ has two electron groups (two C=O double bonds, no lone pairs on carbon), giving linear geometry (180°). Choosing 'bent' is the classic error from incorrectly thinking double bonds count as two groups or that more electron density always means bending. Compare with SO₂, where a lone pair on sulfur is present, making it bent."

- question: "In VSEPR theory, a triple bond counts as three electron groups because it contains three pairs of electrons."
  type: true-false
  answer: false
  explanation: "A triple bond counts as ONE electron group. An electron group is a region of electron density, regardless of how many pairs occupy it. The σ and π electrons in a triple bond all occupy the same general region between two atoms, so they count as a single group. For example, acetylene (HC≡CH) has two electron groups around each carbon (the triple bond plus one single bond), giving linear geometry. Counting triple bonds as three groups would incorrectly predict bent geometry for linear molecules."

- question: "Ammonia (NH₃) and boron trifluoride (BF₃) both have three bonds to the central atom, so they must have the same molecular geometry."
  type: true-false
  answer: false
  explanation: "BF₃ has three bonding pairs and no lone pairs on boron (boron has 3 valence electrons, all used in bonds), giving trigonal planar geometry (120°). NH₃ has three bonding pairs plus one lone pair on nitrogen (5 valence electrons, 3 in bonds, 1 remaining as lone pair), giving trigonal pyramidal geometry (~107°). Lone pairs are invisible in molecular geometry naming but they are real electron groups that push bonding pairs together. Ignoring lone pairs when counting groups is the fundamental VSEPR error."

- question: "Why do water (H₂O) and methane (CH₄) both have tetrahedral electron geometry but different bond angles (104.5° vs 109.5°)? Explain using VSEPR principles."
  type: short-answer
  answer: "Both have four electron groups, giving tetrahedral electron geometry. In methane, all four groups are identical bonding pairs, which repel equally and settle at the ideal 109.5°. In water, two of the four groups are lone pairs, which spread out more than bonding pairs (no second nucleus confines them) and exert greater repulsion on neighboring groups. The two lone pairs push the two O–H bonds closer together, compressing the H–O–H angle from the ideal 109.5° to 104.5°."
  explanation: "The compression is predictable and progressive: each lone pair substituted for a bonding pair compresses bond angles slightly. NH₃ (one lone pair) has angles of ~107°, intermediate between CH₄ (109.5°) and H₂O (104.5°). This regular trend follows directly from the lone-pair repulsion principle."
```

## Explainer

Once you have drawn a Lewis structure for a molecule, VSEPR theory lets you predict its three-dimensional shape using one simple principle: **electron groups repel each other and arrange themselves as far apart as possible around a central atom.** An electron group is any region of electron density — a single bond, a double bond, a triple bond, or a lone pair all count as one group each. This is the critical counting rule: a C=O double bond is one electron group, not two, because the electrons in both bonds occupy roughly the same region of space.

Start by counting the total number of electron groups around the central atom. Two groups push to opposite sides of the atom, giving a **linear** arrangement (180° apart). Three groups spread into a **trigonal planar** shape (120° angles). Four groups adopt a **tetrahedral** arrangement (109.5° angles). Five and six groups give **trigonal bipyramidal** and **octahedral** geometries, respectively. This count gives you the **electron geometry** — the arrangement of all electron groups, whether they contain atoms or not.

The distinction between **electron geometry** and **molecular geometry** is where most students stumble. Molecular geometry describes only where the atoms are — lone pairs are invisible to experimental shape-determination methods. Water (H₂O) has four electron groups around oxygen (two bonding pairs and two lone pairs), so its electron geometry is tetrahedral. But since we only "see" the two O–H bonds, its molecular geometry is **bent**. Ammonia (NH₃) also has tetrahedral electron geometry (three bonds plus one lone pair), but its molecular geometry is **trigonal pyramidal**. The name changes because removing a vertex from a tetrahedron gives a pyramid, not a flat triangle.

Lone pairs also compress bond angles below the ideal values. A lone pair spreads out more than a bonding pair (there is no second nucleus to confine it), so it exerts greater repulsion on neighboring groups. In methane (CH₄), with four identical bonding pairs, angles are a perfect 109.5°. In ammonia, the lone pair pushes the three N–H bonds slightly closer together to about 107°. In water, two lone pairs compress the H–O–H angle further to about 104.5°. This predictable compression lets you refine angle estimates beyond the ideal geometry and explains trends across related molecules.

To apply VSEPR systematically to any molecule: (1) draw the Lewis structure, (2) count electron groups around the central atom, (3) determine the electron geometry from the count, (4) identify how many groups are lone pairs, and (5) name the molecular geometry based on the positions of atoms only. This procedure works for molecules with expanded octets (like PCl₅ or SF₆) just as well as for simple cases. The shapes you predict here become essential for determining molecular polarity — a topic that depends entirely on knowing the geometry first.
