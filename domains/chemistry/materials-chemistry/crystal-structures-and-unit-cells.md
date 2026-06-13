---
id: crystal-structures-and-unit-cells
title: Crystal Structures and Unit Cells
domain: chemistry
course: materials-chemistry
prerequisites:
- id: ionic-bonding
  type: hard
- id: metallic-bonding
  type: hard
- id: covalent-bonding
  type: soft
- id: periodic-trends
  type: soft
- id: solid-state-chemistry-fundamentals
  type: hard
builds-toward:
- crystal-symmetry-and-space-groups
- defect-chemistry
- x-ray-powder-diffraction
tags:
- crystal structures
- unit cells
- Bravais lattices
- packing
- coordination number
stage: advanced
status: validated
---

# Crystal Structures and Unit Cells

## Core Idea
Crystalline solids consist of atoms, ions, or molecules arranged in a periodically repeating three-dimensional pattern. The smallest repeating unit that captures the full symmetry and composition of the crystal is the unit cell. There are 14 Bravais lattices in three dimensions, grouped into 7 crystal systems (cubic, tetragonal, orthorhombic, hexagonal, trigonal, monoclinic, triclinic). Common structure types — FCC, BCC, HCP for metals; rock salt, fluorite, zinc blende for ionic compounds — arise from different ways of packing spheres and filling interstitial sites. The choice of unit cell determines how you calculate density, coordination numbers, and stoichiometry from crystallographic data.

## Questions

```yaml
- question: "A face-centered cubic (FCC) unit cell contains how many atoms?"
  type: multiple-choice
  options:
    - "1"
    - "2"
    - "4"
    - "8"
  answer: 2
  explanation: "Each corner atom is shared among 8 unit cells (8 corners x 1/8 = 1 atom), and each face-center atom is shared between 2 unit cells (6 faces x 1/2 = 3 atoms), giving 1 + 3 = 4 atoms per unit cell. This counting method — fractional contribution per atom — is the standard way to determine unit cell contents for any crystal structure."

- question: "The 14 Bravais lattices represent all possible ways to arrange points in three-dimensional space such that every point has an identical environment."
  type: true-false
  answer: true
  explanation: "Auguste Bravais proved in 1848 that there are exactly 14 distinct lattice types in 3D that satisfy translational symmetry — every lattice point sees the same arrangement of neighbors in the same orientations. These 14 lattices span the 7 crystal systems and differ by the placement of additional lattice points (body-centered, face-centered, base-centered) beyond the primitive corners. Any crystal structure, no matter how complex, maps onto one of these 14 lattice types."

- question: "In the rock salt structure, both the cation and anion sublattices independently form FCC arrangements. Why does this produce 6-fold coordination for both ions?"
  type: short-answer
  answer: "Each Na+ ion sits in an octahedral hole of the Cl- FCC sublattice, surrounded by 6 nearest-neighbor Cl- ions at the vertices of an octahedron. By symmetry, each Cl- is similarly surrounded by 6 Na+ ions. The interpenetrating FCC arrangement places every ion at the center of an octahedron formed by the other sublattice, giving coordination number 6 for both species."
  explanation: "The rock salt structure can be visualized as two interpenetrating FCC lattices offset by half a unit cell edge along each axis. The octahedral holes in an FCC lattice are exactly the right size for ions with radius ratios between about 0.414 and 0.732, which is why NaCl (ratio ~0.56) adopts this structure. If the cation were much smaller, it would rattle in the octahedral hole and the structure would become unstable — the system would prefer tetrahedral coordination instead (zinc blende)."

- question: "A body-centered cubic metal has a unit cell edge length of 2.87 Angstroms and an atomic mass of 55.85 g/mol. What is the density of this metal?"
  type: short-answer
  answer: "BCC has 2 atoms per unit cell. Density = (2 atoms x 55.85 g/mol) / (6.022 x 10^23 atoms/mol x (2.87 x 10^-8 cm)^3) = 7.87 g/cm^3. This is iron (alpha-Fe), confirming that the BCC structure with these parameters matches the known density of iron."
  explanation: "The density calculation from unit cell parameters is fundamental in crystallography: rho = nM/(N_A x a^3), where n is atoms per unit cell, M is molar mass, N_A is Avogadro's number, and a is the edge length. This formula works because the unit cell, by definition, tiles to fill all space — so the density of the unit cell equals the macroscopic density. Matching calculated density to known values is a standard check on proposed crystal structures."
```

## Explainer

Crystals are the most ordered state of matter. Unlike liquids or glasses, where atomic positions are random or only locally organized, a crystal has long-range order — if you know the position and identity of every atom in one small region, you can predict the contents of the entire solid by applying translation operations. The **unit cell** is the fundamental building block of this translational symmetry: the smallest parallelepiped that, when repeated in all three directions, reproduces the full crystal.

The geometry of the unit cell is defined by six parameters: three edge lengths (a, b, c) and three angles (alpha, beta, gamma). These parameters, combined with the lattice type, determine the **crystal system**. In the cubic system, a = b = c and all angles are 90 degrees, but three distinct lattice types exist: primitive (P), body-centered (I), and face-centered (F). The distinction matters because different lattice types pack atoms differently — FCC achieves 74% packing efficiency (the theoretical maximum for equal spheres), while BCC reaches only 68%. These packing differences directly determine properties like density, ductility, and slip systems in metals.

For ionic compounds, the structure depends not just on packing but on the **radius ratio** of cation to anion. Large cations relative to anions favor high coordination numbers (8, as in CsCl); intermediate ratios favor octahedral coordination (6, as in NaCl); small cations favor tetrahedral coordination (4, as in ZnS). This radius ratio rule is approximate — it ignores covalent character, polarization, and entropy — but it correctly predicts the structure of most simple ionic compounds and provides the starting framework for understanding more complex structures.

Counting atoms within a unit cell requires careful bookkeeping because atoms on corners, edges, and faces are shared with neighboring cells. A corner atom contributes 1/8, an edge atom 1/4, a face atom 1/2, and a body-center atom 1. This counting directly gives you stoichiometry (the ratio of different atoms in the formula unit) and enables density calculations from diffraction data. The connection between unit cell parameters, atom positions, and macroscopic properties like density is one of the most practically useful results in materials chemistry — it allows you to go from an X-ray diffraction pattern to a complete structural model of a new material.
