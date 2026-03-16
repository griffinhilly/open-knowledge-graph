---
id: walsh-diagrams-structure-bonding-correlation
title: 'Walsh Diagrams: Structure and Bonding Correlation'
domain: chemistry
course: physical-chemistry
prerequisites:
- id: molecular-orbital-symmetry-classification
  type: hard
- id: molecular-geometry-basics
  type: hard
builds-toward:
- aromaticity-huckel-rule-pi-system
tags:
- orbital-correlation
- molecular-geometry
- structure-prediction
stage: advanced
status: draft
---

# Walsh Diagrams: Structure and Bonding Correlation

## Core Idea
Walsh diagrams plot how molecular orbital energies change with a key geometric parameter (e.g., bond angle). They reveal why certain geometries are preferred by showing which configurations minimize electronic energy. Crossings and avoided crossings in Walsh diagrams explain barriers to rotation, bending angles in triatomic molecules, and conformational preferences.

## How It's Best Learned
Construct Walsh diagrams for H₂O (linear to bent) and H₃ (linear to triangular); predict preferred geometries by electron occupation and compare to experimental structures. Understand how orbital mixing changes with geometry.

## Explainer

From your study of molecular orbital theory, you know how to construct MO diagrams for molecules at a fixed geometry — combining atomic orbitals of appropriate symmetry to form bonding and antibonding molecular orbitals. A **Walsh diagram** takes the next step: it tracks how those molecular orbital energies change continuously as you vary a geometric parameter, such as a bond angle. The result is a plot with the geometric parameter on the x-axis and orbital energy on the y-axis, with lines showing each MO's energy trajectory. This seemingly simple graph turns out to be a powerful tool for predicting molecular shapes.

Consider the classic example: the Walsh diagram for AH₂ molecules (like BeH₂, BH₂, CH₂, NH₂, H₂O) as the H–A–H angle varies from 180° (linear) to 90° (severely bent). In the linear geometry, the molecular orbitals have the symmetry labels of the D∞h point group. As the molecule bends, symmetry is lowered to C₂v, and something important happens: some orbitals that were degenerate in the linear geometry split apart, and orbitals that couldn't mix in the linear geometry begin to interact. Specifically, the 1πu pair (degenerate in linear) splits into two orbitals of different energy — one drops in energy as the molecule bends (it gains s-orbital character through mixing), while the other rises. The orbital that drops is the key: it is strongly stabilized by bending.

The rule for predicting geometry is straightforward: **fill the electrons into the Walsh diagram and find the angle that minimizes total electronic energy**. For BeH₂ (4 electrons), the lowest orbitals are filled and their energies are relatively flat or slightly favored by the linear arrangement — so BeH₂ is linear. For H₂O (8 electrons), the additional electrons occupy the orbital that is strongly stabilized by bending, so the total energy is minimized at a bent geometry (the observed angle is about 104.5°). BH₂ with 6 electrons falls in between and is bent. This explains a trend that VSEPR theory describes but doesn't truly derive: Walsh diagrams show you the electronic energy reason behind the geometry, not just an electron-pair repulsion heuristic.

**Avoided crossings** are another critical feature of Walsh diagrams. When two orbitals of the same symmetry approach each other in energy as the geometry changes, they cannot actually cross — instead, they repel each other, creating a gap. These avoided crossings often create energy barriers to geometric changes and explain why certain conformational transitions require significant activation energy. Walsh diagrams also extend beyond triatomics: you can construct them for any geometric distortion — ring-opening reactions, Jahn-Teller distortions, or rotation about bonds — making them a unifying framework for understanding how electronic structure dictates molecular shape.
