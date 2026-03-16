---
id: chair-cyclohexane-conformations
title: Chair Conformation and Axial-Equatorial Positioning
domain: chemistry
course: organic-chemistry
prerequisites:
- id: ring-strain-and-stability
  type: hard
- id: conformational-analysis-alkanes
  type: hard
builds-toward:
- stereochemistry-intro
tags:
- cyclohexane
- axial
- equatorial
- pseudoaxial
- 1,3-diaxial
stage: formal-systems
status: draft
---

# Chair Conformation and Axial-Equatorial Positioning

## Core Idea
Cyclohexane adopts a chair shape to minimize strain. In this conformation, six C-H bonds point either up/down axial (parallel to the ring axis) or up/down equatorial (projecting outward). Axial positions experience steric repulsion from 1,3-diaxial interactions with other axial hydrogens. Bulky substituents prefer equatorial positions; the equilibrium between two chair conformations can flip depending on substituent size and temperature.

## How It's Best Learned
Draw chair structures with axial and equatorial bonds clearly marked. Flip the chair and track how bonds change positions. Use van der Waals radii to estimate 1,3-diaxial interaction energies for different groups.

## Common Misconceptions
Axial and equatorial are FIXED labels—they flip positions during ring flip, but axial bonds stay parallel to the ring axis. All substituents prefer equatorial equally—some bulky groups (t-Bu, Ph) prefer equatorial more strongly than smaller ones (Me, Cl). Cyclic enantiomers cannot exist from chair flipping alone (enantiomers remain enantiomers).

## Explainer

From conformational analysis of alkanes, you know that rotation around C–C bonds creates different spatial arrangements (conformations) with different energies, and that staggered conformations are more stable than eclipsed ones. From ring strain, you know that cyclopropane and cyclobutane are strained because their bond angles deviate from the ideal tetrahedral 109.5°. Cyclohexane escapes this problem entirely by puckering into the **chair conformation**, where all C–C–C bond angles are very close to 109.5° and all adjacent C–H bonds are perfectly staggered. The chair is not flat — it looks like a lounge chair viewed from the side, with four carbons forming a plane and one carbon tipped up, another tipped down.

In the chair, each carbon bears two types of bonds to its substituents: **axial** bonds point straight up or straight down, alternating around the ring and running parallel to the vertical axis of the chair. **Equatorial** bonds project outward at a slight angle from the ring's "equator," roughly following the plane of the ring. Every carbon has one axial and one equatorial bond, and they alternate: if one carbon has its axial bond pointing up, the adjacent carbon has its axial bond pointing down. Drawing this correctly is essential — practice until the alternating up-down pattern of axial bonds becomes automatic.

The energetic difference between axial and equatorial positions comes from **1,3-diaxial interactions**. When a substituent sits in an axial position, it points directly toward the axial hydrogens on carbons two positions away (the 1,3 relationship). These atoms are close enough for steric repulsion — analogous to the gauche interaction you saw in Newman projections of butane. The larger the substituent, the more severe the clash. A methyl group in the axial position experiences about 7.6 kJ/mol of strain from 1,3-diaxial interactions; a tert-butyl group experiences so much strain (>20 kJ/mol) that it locks the ring into whichever chair places it equatorial.

Cyclohexane undergoes a **ring flip** — a concerted motion where the "up" carbon swings down and the "down" carbon swings up, converting one chair into another. Crucially, every bond that was axial becomes equatorial, and vice versa. For unsubstituted cyclohexane, the two chairs are identical. But for methylcyclohexane, one chair has the methyl axial (with 1,3-diaxial strain) and the other has it equatorial (strain-free). The equilibrium favors the equatorial conformer by about 95:5 at room temperature. For disubstituted cyclohexanes, you evaluate both chairs by adding up the 1,3-diaxial strain for each substituent in each conformer, and the lower-energy chair dominates. This is a quantitative tool: you can predict conformational preferences using tabulated A-values (the energy cost of placing each group axial).
