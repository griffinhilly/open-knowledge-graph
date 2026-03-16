---
id: crystal-lattice-systems-classification
title: Crystal Lattice Systems and Classification
domain: engineering
course: materials-science
prerequisites:
- id: atomic-bonding-engineering-materials
  type: hard
builds-toward:
- crystallographic-planes-directions
- point-defects-and-vacancies
- grain-boundaries-and-interfaces-materials
tags:
- crystal-systems
- lattice
- bravais
- cubic
- hexagonal
stage: formal-systems
status: draft
---

# Crystal Lattice Systems and Classification

## Core Idea
Crystals are periodic 3D arrangements of atoms in space, classified into seven crystal systems (cubic, tetragonal, orthorhombic, monoclinic, triclinic, hexagonal, trigonal) and 14 Bravais lattices. Each system has characteristic symmetry properties and lattice parameters (a, b, c, α, β, γ) that define the unit cell geometry and determine how atoms pack.

## Explainer

From atomic bonding, you understand that atoms in a solid are held in place by bonds — covalent, ionic, or metallic — that have preferred lengths and angles. When a material solidifies slowly from the melt, atoms settle into the lowest-energy arrangement: a periodic, repeating 3D pattern called a **crystal lattice**. The periodicity is what makes crystalline materials fundamentally different from amorphous solids (like glass), where atoms are frozen in random arrangements. In a crystal, if you know where one atom is and you know the **unit cell** — the smallest repeating box — you know where every atom in the material is.

The **lattice parameters** (a, b, c, α, β, γ) define the unit cell: a, b, c are the edge lengths along three axes, and α, β, γ are the angles between those axes. The seven **crystal systems** are defined by symmetry constraints on these parameters. The most symmetric is **cubic** (a = b = c, α = β = γ = 90°), where the unit cell is a perfect cube. The least symmetric is **triclinic** (a ≠ b ≠ c, α ≠ β ≠ γ ≠ 90°), where all parameters are independent. The progression between them — tetragonal (one axis different), orthorhombic (all lengths different but right angles), monoclinic (one angle different), and hexagonal/trigonal — can be thought of as progressively removing symmetry from the perfect cube.

The **14 Bravais lattices** refine this classification by asking: within each crystal system, can additional lattice points be placed (at body centers or face centers) while maintaining the required symmetry? For example, the cubic system has three Bravais lattices: simple cubic (SC, atoms only at corners), **body-centered cubic** (BCC, corners plus one atom at the body center), and **face-centered cubic** (FCC, corners plus atoms at each face center). BCC iron at room temperature and FCC aluminum are canonical examples. The FCC lattice is the densest cubic packing, with an atomic packing factor of 74%; BCC is slightly less dense at 68%. These packing differences directly affect density, diffusion rates, and the slip systems available for plastic deformation.

Why does this classification matter for engineering? Because crystal structure governs almost every property you care about. FCC metals (Al, Cu, Ni, Au) are generally more ductile than BCC metals (Fe, W, Cr) because FCC has more equivalent slip planes for dislocations to move. Hexagonal close-packed (HCP) metals (Ti, Mg, Zn) have fewer slip systems and tend to be less ductile at room temperature. The crystal structure also determines cleavage planes (where brittle fracture occurs), anisotropy of elastic modulus, and even optical and electrical properties. When you later study crystallographic planes and directions, you will use the **Miller index** notation that builds directly on the unit cell coordinate system introduced here.

