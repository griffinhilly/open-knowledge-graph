---
id: crystal-structure-bravais-lattices
title: Crystal Structure and Bravais Lattices
domain: physics
course: condensed-matter-physics
prerequisites:
- id: crystal-structure-basics
  type: hard
- id: eigenvalues-and-eigenvectors
  type: soft
tags:
- crystal-structure
- bravais-lattice
- unit-cell
- symmetry
stage: expert
status: validated
---

# Crystal Structure and Bravais Lattices

## Core Idea
A crystal is a solid whose atoms are arranged in a periodically repeating pattern. This periodicity is captured by a Bravais lattice — the set of all points R = n_1 a_1 + n_2 a_2 + n_3 a_3, where a_i are primitive lattice vectors and n_i are integers. In three dimensions there are exactly 14 distinct Bravais lattices grouped into 7 crystal systems (cubic, tetragonal, orthorhombic, hexagonal, trigonal, monoclinic, triclinic), each distinguished by the symmetry operations that leave the lattice invariant. The physical crystal is described by placing a basis (one or more atoms) at each lattice point.

## Questions

```yaml
- question: "A Bravais lattice requires that every lattice point have an identical environment when viewed from that point. Which of the following is NOT a Bravais lattice?"
  type: multiple-choice
  options:
    - "Simple cubic"
    - "Body-centered cubic (BCC)"
    - "Honeycomb lattice"
    - "Face-centered cubic (FCC)"
  answer: 2
  explanation: "The honeycomb lattice (like graphene) is not a Bravais lattice because it contains two inequivalent sites per unit cell. It is instead described as a hexagonal Bravais lattice with a two-atom basis. Every Bravais lattice must look identical from every point, which fails for the honeycomb because alternating vertices have different neighbor configurations."

- question: "What distinguishes a primitive unit cell from a conventional unit cell in crystallography?"
  type: multiple-choice
  options:
    - "A primitive cell always has cubic symmetry; a conventional cell does not"
    - "A primitive cell contains exactly one lattice point and is the smallest repeating unit, while a conventional cell may contain multiple lattice points but is chosen to display the full symmetry of the lattice"
    - "A primitive cell and conventional cell always have the same volume"
    - "A conventional cell is always smaller than a primitive cell"
  answer: 1
  explanation: "The primitive unit cell contains exactly one lattice point (volume = |a_1 · (a_2 × a_3)|) and tiles space without gaps. However, primitive cells can have awkward shapes that obscure the lattice symmetry. The conventional cell is chosen to make symmetry obvious — for example, the conventional BCC cell is a cube containing 2 lattice points, while the primitive BCC cell is a rhombohedron. The conventional cell is always an integer multiple of the primitive cell volume."

- question: "The 14 Bravais lattices in 3D arise because some crystal systems allow centering (body-centered, face-centered, base-centered) while others do not, since centering would produce a lattice equivalent to a different type."
  type: true-false
  answer: true
  explanation: "Starting from the 7 crystal systems (defined by axial lengths and angles), one can attempt to add centering points. But many centerings are redundant — for instance, a base-centered cubic lattice is equivalent to a tetragonal lattice after redefining axes. After eliminating all such redundancies, exactly 14 distinct lattices remain. This classification was established by Auguste Bravais in 1850."

- question: "Explain why the diamond structure requires a basis of two atoms on an FCC lattice, rather than being a Bravais lattice itself."
  type: short-answer
  answer: "In the diamond structure, each atom is tetrahedrally bonded to four neighbors, but the two atoms in each pair have different orientations of their bonding environment. Specifically, the structure consists of two interpenetrating FCC sublattices offset by (a/4, a/4, a/4). An atom on one sublattice sees its neighbors arranged differently than an atom on the other sublattice would if you simply translated the lattice. Since a Bravais lattice demands that every point has an identical environment, diamond fails this test and must be described as FCC + a two-atom basis."
  explanation: "This is a common source of confusion. Diamond, silicon, and germanium all have this structure. The key insight is that 'identical environment' in the Bravais lattice definition means identical under pure translation — no rotation or reflection allowed. The two sublattice sites in diamond are related by a non-primitive translation, not by any lattice vector."
```

## Explainer

Condensed matter physics begins with a question that sounds deceptively simple: how are the atoms in a solid arranged? For crystalline solids — which include most metals, semiconductors, and many ceramics — the answer is a periodic arrangement that repeats identically throughout space. The mathematical abstraction of this periodicity is the **Bravais lattice**: an infinite set of discrete points generated by R = n_1 a_1 + n_2 a_2 + n_3 a_3, where the three primitive vectors a_i define the lattice and n_i range over all integers. The defining property is that the lattice looks exactly the same from every lattice point — every point has an identical environment.

In three dimensions, the constraints of symmetry allow exactly **14 distinct Bravais lattices**, organized into 7 crystal systems. The crystal systems are defined by the relationships among the lattice parameters (edge lengths a, b, c and angles alpha, beta, gamma): cubic has a = b = c with all right angles, hexagonal has a = b with gamma = 120 degrees, and so on down to triclinic with no constraints at all. Within each system, you can place additional lattice points at the body center, face centers, or base centers — but many of these centerings turn out to be equivalent to a lattice in a different (lower-symmetry) system after redefining the primitive vectors. Eliminating all redundancies leaves exactly 14.

A real crystal is more than just a lattice — it is a lattice plus a **basis**, the set of atoms placed at each lattice point. Monatomic metals like copper have a one-atom basis on an FCC lattice. Sodium chloride has a two-atom basis (Na and Cl) on an FCC lattice. Diamond and silicon have a two-atom basis on FCC where both atoms are the same element but sit at inequivalent positions. The distinction between lattice and basis is critical: the lattice captures translational symmetry, while the basis captures what sits at each point. Two completely different materials can share the same Bravais lattice but differ in their basis.

The full symmetry of a crystal includes not just translations but also rotations, reflections, and inversions that map the crystal onto itself. These additional symmetries define the **point group** (symmetry operations that leave at least one point fixed) and the **space group** (the full set of symmetry operations including translations, screw axes, and glide planes). There are 32 crystallographic point groups and 230 space groups. While you rarely need all 230 in a physics course, the key insight is that symmetry constrains everything — the allowed vibrational modes, electronic band structure, optical properties, and response to external fields are all dictated by the space group. Understanding the lattice is the first step toward understanding the solid.
