---
id: group-theory-molecular-symmetry
title: 'Group Theory and Molecular Symmetry: Point Groups and Applications'
domain: chemistry
course: physical-chemistry
prerequisites:
- id: vibrational-modes-and-symmetry
  type: hard
- id: quantum-chemistry-foundations
  type: soft
builds-toward: []
tags:
- group-theory
- point-groups
- character-tables
- symmetry-operations
- irreducible-representations
- molecular-symmetry
stage: advanced
status: draft
---

# Group Theory and Molecular Symmetry: Point Groups and Applications

## Core Idea
Group theory provides a rigorous mathematical framework for exploiting molecular symmetry in chemistry. Every molecule belongs to a point group defined by its symmetry operations (identity, rotation C_n, reflection sigma, inversion i, improper rotation S_n), and the properties of these groups are encoded in character tables. Irreducible representations label how molecular properties (orbitals, vibrations, electronic states) transform under symmetry operations. The power of group theory lies in its predictive shortcuts: selection rules for spectroscopic transitions reduce to checking whether the direct product of initial state, operator, and final state representations contains the totally symmetric representation; the number and symmetry species of IR- and Raman-active vibrational modes follow directly from the reducible representation of atomic displacements; and symmetry-adapted linear combinations simplify MO construction by restricting which atomic orbitals can mix. These applications save enormous computational effort by identifying which integrals are zero by symmetry before calculating anything.

## How It's Best Learned
Assign the point group of a series of molecules (H2O, NH3, BF3, SF6) by identifying all symmetry elements, then use the character table to determine which vibrational modes are IR-active and which are Raman-active. Verify predictions against experimental spectra.

## Common Misconceptions
- Thinking group theory only applies to highly symmetric molecules; even low-symmetry molecules (C1 point group) benefit from the formalism, though fewer simplifications arise.
- Confusing symmetry elements (the geometric object: axis, plane) with symmetry operations (the action: rotation by 2*pi/n, reflection); the point group is defined by its operations, not its elements.
