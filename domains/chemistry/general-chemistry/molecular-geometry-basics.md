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
status: draft
---

# Molecular Geometry and Electron Pair Geometry

## Core Idea
Molecular geometry describes the 3D arrangement of atoms in a molecule, while electron pair geometry includes both bonding and lone pairs. Repulsive forces between electron pairs (bonding and lone) determine the geometry. Lone pairs occupy more space than bonding pairs, affecting actual molecular shapes.

## Explainer

From drawing Lewis structures, you can determine how many bonding pairs and lone pairs surround a central atom. Molecular geometry takes that 2D blueprint and answers the 3D question: what shape does the molecule actually adopt in space? The governing principle is simple — electron pairs repel each other (they're all negatively charged), so they arrange themselves as far apart as possible. This is the core idea behind VSEPR (Valence Shell Electron Pair Repulsion) theory.

Start by counting the total number of **electron groups** around the central atom — each bond (single, double, or triple counts as one group) and each lone pair is one group. The number of groups determines the **electron pair geometry**: 2 groups → linear (180°), 3 → trigonal planar (120°), 4 → tetrahedral (109.5°), 5 → trigonal bipyramidal, 6 → octahedral. These are the idealized arrangements that maximize the distance between electron groups. For example, methane (CH₄) has 4 bonding groups and no lone pairs on carbon, so both its electron pair geometry and its molecular geometry are tetrahedral.

The crucial distinction is between **electron pair geometry** (which includes all electron groups) and **molecular geometry** (which describes only where the atoms are). When lone pairs are present, the molecular geometry differs from the electron pair geometry because lone pairs are invisible in the molecular shape — you can't "see" where they are, only the atoms. Water (H₂O) has 4 electron groups on oxygen (2 bonding, 2 lone pairs), so its electron pair geometry is tetrahedral, but its molecular geometry is **bent** because you only see the two hydrogen atoms. Ammonia (NH₃) also has a tetrahedral electron pair geometry (3 bonding, 1 lone pair) but a **trigonal pyramidal** molecular geometry.

Lone pairs don't just change the name of the shape — they compress bond angles. A lone pair's electron cloud spreads out more than a bonding pair's (it's held by only one nucleus, not pinned between two), so it repels neighboring groups more strongly. This is why water's H–O–H angle is about 104.5° rather than the ideal tetrahedral 109.5°, and why ammonia's H–N–H angle is about 107°. The hierarchy of repulsion is: lone pair–lone pair > lone pair–bonding pair > bonding pair–bonding pair. Understanding this hierarchy lets you predict not just the qualitative shape but also whether bond angles will be compressed or expanded relative to the ideal values — information that directly affects molecular polarity, which is the next concept you'll build toward.
