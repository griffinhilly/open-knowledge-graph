---
id: molecular-symmetry-and-group-theory
title: Molecular Symmetry and Point Groups
domain: chemistry
course: physical-chemistry
prerequisites:
- id: molecular-geometry-basics
  type: hard
builds-toward:
- character-tables-spectroscopic-applications
- selection-rules-electronic-spectroscopy
tags:
- symmetry
- group-theory
- point-groups
- spectroscopy
stage: advanced
status: draft
---

# Molecular Symmetry and Point Groups

## Core Idea
Group theory describes the symmetry properties of molecules through point groups, which classify symmetry operations (rotations, reflections, inversions) that leave molecular geometry unchanged. Each point group has associated character tables that encode how molecular orbitals and vibrations transform under symmetry operations. This mathematical framework is essential for predicting allowed spectroscopic transitions and molecular properties.

## Explainer

From molecular geometry, you know how to describe a molecule's shape — whether it is linear, bent, tetrahedral, octahedral, and so on. Symmetry and group theory formalize that intuition by asking a precise question: what operations can you perform on the molecule that leave it looking exactly the same? These **symmetry operations** include rotations around an axis (C_n), reflections through a plane (σ), inversion through a center (i), and improper rotations (S_n, a rotation followed by a reflection). The complete set of symmetry operations for a molecule forms a mathematical group — a closed collection of operations where combining any two gives another operation in the set. The particular group a molecule belongs to is its **point group**, and identifying it is the first step in any symmetry analysis.

Assigning a point group follows a systematic flowchart. Is the molecule linear? If so, is it symmetric about its center (like CO₂, which is D∞h) or not (like HCN, which is C∞v)? For nonlinear molecules: find the highest-order rotation axis (the **principal axis**), check for perpendicular C₂ axes, check for mirror planes, and the combination of elements present determines the point group. Water (H₂O) has a C₂ axis and two mirror planes, placing it in C₂v. Ammonia (NH₃) has a C₃ axis and three vertical mirror planes: C₃v. Benzene has a C₆ axis, six C₂ axes, a horizontal mirror plane, and more — it belongs to D₆h. The labels may seem like arbitrary notation at first, but each one encodes the complete symmetry content of the molecule.

The real payoff comes from **character tables** — compact mathematical summaries of how things transform under each symmetry operation. Every point group has a character table listing its **irreducible representations** (symmetry species), each describing one of the fundamental ways an object can behave under the group's operations. A molecular orbital, for example, might be symmetric (+1) under a C₂ rotation and antisymmetric (−1) under a mirror reflection — the pattern of +1s and −1s identifies which irreducible representation it belongs to. This classification is not merely bookkeeping; it has predictive power. Two orbitals can only interact (mix, bond, overlap) if they belong to the same irreducible representation. A vibrational mode is infrared-active only if it transforms like x, y, or z (a translational vector), and Raman-active only if it transforms like a quadratic function (x², xy, etc.). These are **selection rules**, and they can be read directly from the character table without computing a single integral.

For a concrete example, consider the question: how many IR-active vibrational modes does water have? Water belongs to C₂v, which has four irreducible representations: A₁, A₂, B₁, B₂. Using the reduction formula on the 3N = 9 degrees of freedom for water's three atoms, you find that the 3 vibrational modes transform as 2A₁ + B₂. The character table shows that A₁ transforms like z and B₂ transforms like y — both are translation-like, so all three modes are IR-active. This kind of analysis, which would require laborious integral computation without group theory, becomes a simple table lookup. That efficiency is why symmetry analysis is ubiquitous in spectroscopy, bonding theory, and solid-state chemistry.
