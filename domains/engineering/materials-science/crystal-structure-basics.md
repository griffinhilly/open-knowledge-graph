---
id: crystal-structure-basics
title: Crystal Structure and Unit Cells
domain: engineering
course: materials-science
prerequisites:
- id: atomic-structure-basics
  type: hard
- id: covalent-bonding
  type: soft
- id: ionic-bonding
  type: soft
- id: metallic-bonding
  type: soft
- id: atomic-structure-and-atoms
  type: hard
- id: crystal-structures-and-properties
  type: hard
- id: atomic-bonding-in-materials
  type: soft
builds-toward:
- miller-indices
- crystal-defects
- ceramic-structure-and-properties
tags:
- crystal
- unit-cell
- lattice
- structure
stage: formal-systems
status: validated
---

# Crystal Structure and Unit Cells

## Core Idea
Crystalline solids are characterized by long-range periodic atomic arrangements described by a unit cell — the smallest repeating unit of the lattice. The 14 Bravais lattices classify all possible 3D periodic arrangements, with metals commonly adopting FCC, BCC, or HCP structures. Knowing a crystal structure allows calculation of atomic packing factor, theoretical density, and coordination number. These structural details directly determine many physical and mechanical properties of the material.

## How It's Best Learned
Build physical or digital models of FCC, BCC, and HCP unit cells and calculate the number of atoms per cell, coordination number, and packing factor for each. Reinforce by working backward from density measurements to confirm crystal structure.

## Common Misconceptions
- Students often confuse the lattice (abstract geometric points) with the basis (actual atoms placed at each point).
- HCP is not a Bravais lattice by itself — it is a hexagonal lattice with a two-atom basis.
- Atoms in adjacent unit cells are shared, so corner atoms count as 1/8 and face atoms as 1/2.

## Questions

```yaml
- question: "An FCC unit cell has 8 corner atoms and 6 face-center atoms. How many atoms does one FCC unit cell contain?"
  type: multiple-choice
  options:
    - "14 — count all corner and face atoms directly"
    - "2 — 8×(1/8) + 6×(1/2) is incorrect; it should be 1"
    - "4 — 8×(1/8) + 6×(1/2) = 1 + 3 = 4"
    - "6 — only face atoms are counted since they are shared between two cells"
  answer: 2
  explanation: "Each corner atom is shared among 8 unit cells, contributing 1/8 per cell. Each face-center atom is shared between 2 unit cells, contributing 1/2 per cell. Total = 8×(1/8) + 6×(1/2) = 1 + 3 = 4 atoms per unit cell. This is the correct count for FCC, and it feeds directly into calculating atomic packing factor and theoretical density."

- question: "HCP (hexagonal close-packed) is one of the 14 Bravais lattices."
  type: true-false
  answer: false
  explanation: "HCP is NOT one of the 14 Bravais lattices. It is a hexagonal Bravais lattice with a two-atom basis — one atom at the corner/face positions and one offset inside the cell. The distinction matters: a Bravais lattice is a set of translation vectors describing periodicity, while a crystal structure is a Bravais lattice plus a basis (the pattern of atoms placed at each lattice point). HCP has hexagonal symmetry but requires two atoms per lattice point to describe the actual arrangement."

- question: "What does the coordination number of an atom in a crystal structure tell you, and how does it differ between BCC and FCC?"
  type: short-answer
  answer: "Coordination number is the number of nearest-neighbor atoms surrounding a given atom. In BCC, each atom has 8 nearest neighbors (the 8 corners surrounding the body-center atom). In FCC, each atom has 12 nearest neighbors. Higher coordination number means more nearest neighbors and generally a higher atomic packing factor."
  explanation: "Coordination number describes the local geometry around each atom — how many atoms it directly touches. FCC (coordination 12) is more densely packed than BCC (coordination 8), which is why FCC has a higher atomic packing factor (0.74 vs 0.68). Coordination number influences physical properties like ductility, diffusion rates, and how easily atoms can slip past each other during deformation."
```

## Explainer

You already know from atomic structure that atoms bond through electron interactions, and from bonding theory that the bond type (metallic, ionic, covalent) determines many of a material's properties. In crystalline solids, those atoms are not randomly arranged — they settle into highly ordered, periodic patterns that repeat in all three dimensions. The unit cell is the fundamental repeating unit: a small box that, when stacked together filling all of space, recreates the entire crystal. Every property derivable from a crystal structure — density, packing efficiency, slip planes for plastic deformation — comes from understanding the unit cell.

The three structures you will encounter most in metals are BCC (body-centered cubic), FCC (face-centered cubic), and HCP (hexagonal close-packed). BCC has one atom at each corner and one at the center of the cube. FCC has one at each corner and one at the center of each face. HCP stacks hexagonal layers with an offset middle layer. A critical skill is counting atoms per unit cell correctly: corner atoms are shared among 8 unit cells (count 1/8 each), edge atoms among 4 (count 1/4), face atoms between 2 (count 1/2), and body-center atoms belong entirely to one cell (count 1). For FCC: 8×(1/8) + 6×(1/2) = 4 atoms per cell.

The atomic packing factor (APF) measures what fraction of the unit cell volume is occupied by atoms, treating atoms as hard spheres touching at the closest approach. FCC achieves APF = 0.74, which is the theoretical maximum for equal sphere packing. BCC achieves 0.68. Both FCC and HCP achieve 0.74 — they are both "close-packed" structures, just with different stacking sequences (ABCABC for FCC, ABABAB for HCP). Materials with higher APF are denser and typically harder to compress.

One of the most important conceptual distinctions is between the lattice and the basis. The lattice is an abstract set of geometric points — it has no chemistry, just spatial repetition. The basis is the atom (or group of atoms) placed at each lattice point. The crystal structure = lattice + basis. For most simple metals, the basis is a single atom and the distinction is trivial. But for HCP, the basis is two atoms, which is why HCP is not itself a Bravais lattice — the hexagonal Bravais lattice plus a two-atom basis generates the HCP arrangement. Getting this distinction right is essential when you encounter more complex structures like ceramics or intermetallics.

These structural details directly drive material properties. FCC metals (aluminum, copper, gold) are generally more ductile than BCC metals (iron at room temperature, tungsten) because their close-packed planes can slide more easily — there are more equivalent slip systems. Coordination number affects bond strength and melting point. Theoretical density calculated from the unit cell (density = nA / VₙNₐ, where n is atoms per cell, A is atomic mass, Vₙ is cell volume, Nₐ is Avogadro's number) is a quick experimental check of crystal structure — if your measured density matches the FCC calculation but not BCC, you have evidence for the structure.
