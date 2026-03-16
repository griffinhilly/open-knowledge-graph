---
id: newman-projection-and-conformations
title: Newman Projections and Conformational Analysis
domain: chemistry
course: organic-chemistry
prerequisites:
- id: molecular-geometry-basics
  type: hard
- id: alkane-structure-and-properties
  type: hard
- id: organic-chemistry-intro
  type: soft
builds-toward:
- fischer-projection-and-wedge-dash
- e2-mechanism-hoffmann-rule
tags:
- newman-projection
- conformation
- staggered
- eclipsed
- 3d-visualization
stage: formal-systems
status: draft
---

# Newman Projections and Conformational Analysis

## Core Idea
Newman projections depict molecules as viewed along a C-C bond, with the front carbon at the center and the back carbon as a circle. Staggered conformations (bonds offset by 60°) are lower in energy than eclipsed conformations (bonds aligned). Newman projections are essential for visualizing stereochemical outcomes in reactions like E2, where orbital alignment matters.

## Explainer

From molecular geometry, you know that carbon with four bonds adopts a tetrahedral arrangement with bond angles of about 109.5°. From alkane structure, you know that rotation around C–C single bonds is relatively free. A **Newman projection** is a drawing convention that lets you visualize this rotation by looking straight down the axis of a C–C bond. The **front carbon** appears as a dot (or the center point where its three other bonds meet), and the **back carbon** appears as a circle. Each carbon shows its three remaining bonds as lines radiating outward — the front carbon's bonds radiate from the center dot, and the back carbon's bonds radiate from the edge of the circle.

The value of Newman projections is that they make the **dihedral angle** — the angle between substituents on the front and back carbons — immediately visible. In a **staggered conformation**, the front and back bonds are offset by 60°, placing each substituent in the gaps between the substituents on the other carbon. In an **eclipsed conformation**, the front and back bonds align directly (0° dihedral), placing substituents directly behind one another. Staggered conformations are lower in energy because eclipsed bonds experience **torsional strain** from the repulsion between electron clouds in adjacent bonds that are forced into close proximity.

For ethane, all staggered conformations are equivalent and all eclipsed conformations are equivalent — the energy difference is about 12 kJ/mol. But for butane (looking along the C2–C3 bond), the staggered conformations are no longer equal. The **anti conformation** (methyl groups 180° apart) is the lowest in energy because the large groups are maximally separated. The **gauche conformation** (methyl groups 60° apart) is about 3.8 kJ/mol higher due to **steric strain** from the proximity of the two methyl groups. Among the eclipsed conformations, the one with the two methyl groups directly aligned (0° dihedral) is the highest energy of all. This energy landscape — anti < gauche < eclipsed — establishes the principle that molecules preferentially adopt conformations that minimize steric and torsional interactions.

Newman projections become indispensable when you need to predict reaction stereochemistry. In E2 elimination reactions, the leaving group and the hydrogen being removed must be **anti-periplanar** — a 180° dihedral angle — for the orbital overlap required to form the new double bond. Drawing the Newman projection, rotating to find the conformation where H and the leaving group are anti to each other, and then reading off which substituents end up cis or trans in the resulting alkene is a skill you will use repeatedly. The ability to mentally rotate between Newman projections and other representations (wedge-dash, sawhorse) is fundamental to three-dimensional reasoning in organic chemistry.
