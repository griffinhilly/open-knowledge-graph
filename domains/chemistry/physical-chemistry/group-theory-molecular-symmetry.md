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

## Explainer

From your work on vibrational modes and symmetry, you know that molecules have characteristic symmetry elements — rotation axes, mirror planes, inversion centers — and that these symmetry properties constrain which vibrational modes are possible. Group theory takes this intuition and makes it rigorous and predictive by treating the collection of all symmetry operations of a molecule as a mathematical **group** — a set with a multiplication rule (performing one operation after another), an identity element, inverses for every element, and associativity. This algebraic structure is what gives group theory its power: instead of reasoning case by case about molecular properties, you can use the group's structure to derive results that apply to every molecule in that **point group**.

The first practical skill is assigning a molecule to its point group by systematically identifying all symmetry operations. Water (C₂ᵥ) has a C₂ rotation axis and two mirror planes. Ammonia (C₃ᵥ) has a C₃ axis and three vertical mirror planes. Benzene (D₆ₕ) has a principal C₆ axis, six C₂ axes perpendicular to it, a horizontal mirror plane, and several vertical planes. Once you know the point group, you look up its **character table** — a compact matrix that encodes how every symmetry species (irreducible representation) transforms under every symmetry operation. Each row of the character table is an irreducible representation labeled by a Mulliken symbol (A₁, B₂, E, T₂, etc.), and each column corresponds to a class of symmetry operations.

The character table's real value lies in the **selection rules** and **orthogonality relationships** it provides. To determine whether a vibrational mode is IR-active, you check whether it belongs to the same irreducible representation as one of the translational coordinates (x, y, or z) — because the transition dipole moment operator transforms like a translation. For Raman activity, you check against the quadratic functions (x², xy, etc.) because the polarizability tensor transforms that way. In the C₂ᵥ point group of water, the character table immediately tells you that all three vibrational modes (2A₁ + B₂) are both IR- and Raman-active. For a molecule in a centrosymmetric point group (one with an inversion center), the **mutual exclusion rule** follows directly: no mode can be both IR- and Raman-active, because the relevant irreducible representations are either symmetric (gerade) or antisymmetric (ungerade) under inversion, and the IR and Raman operators have opposite symmetry.

Beyond spectroscopy, group theory simplifies molecular orbital construction. When building MOs from atomic orbital combinations, only AOs that belong to the same irreducible representation can mix — symmetry-forbidden combinations have zero overlap by orthogonality, and you never need to calculate the integral to prove it. This is the deeper reason group theory saves so much effort: it tells you which integrals vanish before you evaluate a single one. For a molecule like SF₆ with 48 symmetry operations, this eliminates the vast majority of possible orbital interactions and reduces a formidable problem to a manageable one.
