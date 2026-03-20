---
id: crystal-structure-classification
title: Crystal Systems and Bravais Lattices
domain: engineering
course: materials-science
prerequisites:
- id: atomic-bonding-materials
  type: hard
builds-toward:
- unit-cell-lattice-parameters
- point-defects-in-materials
tags:
- crystal-structure
- lattice
- symmetry
- bravais
stage: advanced
status: draft
---

# Crystal Systems and Bravais Lattices

## Core Idea
Atoms in crystalline solids arrange in repeating 3D periodic patterns defined by crystal systems and Bravais lattices. The seven crystal systems (cubic, tetragonal, orthorhombic, monoclinic, triclinic, hexagonal, rhombohedral) and fourteen possible Bravais lattices completely classify all possible periodic atomic arrangements in nature. This classification is essential for crystallography, structure prediction, and understanding how crystal geometry influences material properties.

## Explainer

From your study of atomic bonding, you know that atoms attract and repel each other in ways governed by the type of bond — metallic, ionic, covalent, or van der Waals. In a crystalline solid, atoms settle into the lowest-energy arrangement, and that arrangement repeats perfectly in three dimensions. This periodicity is not accidental: it is the natural result of atoms packing to maximize attractive interactions while maintaining stable bond angles and distances. The mathematical framework for classifying all possible periodic arrangements is the language of **crystal systems** and **Bravais lattices**.

A **crystal system** is defined by the geometry of the **unit cell** — the smallest repeating box that, when stacked in three directions, generates the entire crystal. The unit cell is described by three edge lengths (a, b, c) and three angles (α, β, γ) between them. Imposing different constraints on these six parameters yields exactly seven distinct crystal systems. The simplest and most symmetric is cubic (a = b = c, all angles 90°), which describes many metals (iron, copper, aluminum) and simple ionic solids. Tetragonal is like cubic but with one axis stretched (a = b ≠ c). Orthorhombic allows all three lengths to differ while keeping all right angles. Monoclinic tilts one axis (one angle ≠ 90°). Triclinic allows everything to differ — the lowest symmetry. Hexagonal uses a rhombus-shaped base with a 120° angle, describing graphite, zinc, and titanium. Rhombohedral (also called trigonal) has equal lengths and equal angles but angles ≠ 90°.

Within each crystal system, there can be multiple **Bravais lattices** depending on whether there are additional lattice points at face centers or body centers. A **primitive** lattice has points only at the unit cell corners; a **body-centered** lattice adds a point in the center of the cell; **face-centered** puts points at the center of each face; **base-centered** adds points only to two opposite faces. Not all centering types are distinct for all crystal systems — some combinations are equivalent to a simpler primitive cell with a smaller unit cell. Accounting for all valid combinations across the seven crystal systems yields exactly 14 distinct Bravais lattices. These 14 lattices are the complete catalog of all possible periodic translational symmetries in three dimensions — no more, no less.

Why does this classification matter for material properties? Because crystal geometry directly controls atomic packing density, slip systems for dislocation movement, anisotropy of mechanical and electrical properties, and how X-rays diffract from the structure. Face-centered cubic metals (copper, aluminum, gold) have 12 slip systems and deform easily, making them highly ductile. Body-centered cubic metals (iron at room temperature) have fewer close-packed slip systems and require higher stress to move dislocations, contributing to higher strength and lower ductility at low temperatures. The hexagonal system has a limited number of slip planes, which is why zinc and magnesium are more brittle than FCC metals. Every structure-property relationship in materials science ultimately traces back to the crystal system and lattice type.
