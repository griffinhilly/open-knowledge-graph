---
id: crystal-structure-classification
title: Crystal Systems and Bravais Lattices
domain: engineering
course: materials-science
prerequisites:
- id: atomic-bonding-in-materials
  type: hard
builds-toward:
- unit-cell-lattice-parameters
- point-defects-in-materials
tags:
- crystal-structure
- lattice
- symmetry
- bravais
stage: formal-systems
status: validated
---

# Crystal Systems and Bravais Lattices

## Core Idea
Atoms in crystalline solids arrange in repeating 3D periodic patterns defined by crystal systems and Bravais lattices. The seven crystal systems (cubic, tetragonal, orthorhombic, monoclinic, triclinic, hexagonal, rhombohedral) and fourteen possible Bravais lattices completely classify all possible periodic atomic arrangements in nature. This classification is essential for crystallography, structure prediction, and understanding how crystal geometry influences material properties.

## Questions

```yaml
- question: "Copper and aluminum are highly ductile, while zinc and magnesium are comparatively brittle at room temperature. Which crystal structure explanation best accounts for this difference?"
  type: multiple-choice
  options:
    - "Copper and aluminum have smaller unit cells, allowing atoms to rearrange more easily under stress"
    - "FCC metals have 12 close-packed slip systems, while hexagonal metals have fewer, restricting dislocation movement"
    - "Zinc and magnesium have triclinic crystal structures that create directional covalent bonds resisting deformation"
    - "BCC metals like zinc have lower atomic packing efficiency than FCC metals"
  answer: 1
  explanation: "Face-centered cubic metals (Cu, Al, Au) have 12 distinct {111}<110> slip systems, giving dislocations many paths to move — hence high ductility. Hexagonal close-packed metals (Zn, Mg) have only a few active slip planes at room temperature, limiting dislocation glide and resulting in lower ductility. Zinc is hexagonal, not triclinic or BCC — option D contains a factual error about zinc's structure."

- question: "A crystallographer finds a new mineral whose unit cell has equal edge lengths and equal inter-edge angles, but the angles are not 90°. Which Bravais lattice system does this belong to?"
  type: multiple-choice
  options:
    - "Cubic, because all edge lengths are equal"
    - "Tetragonal, because the angles deviate from 90°"
    - "Rhombohedral (trigonal), because all lengths are equal but angles are not 90°"
    - "Monoclinic, because one angle differs from the others"
  answer: 2
  explanation: "The rhombohedral (trigonal) system is defined by a = b = c and α = β = γ ≠ 90°. Cubic also has equal lengths but requires all angles to be exactly 90°. Tetragonal has two equal lengths (a = b ≠ c) with right angles. Monoclinic has all lengths different and exactly one non-right angle. The angle constraint is what distinguishes rhombohedral from cubic."

- question: "A body-centered cubic unit cell has lattice points primarily at the eight corners of the cube."
  type: true-false
  answer: false
  explanation: "A BCC cell has lattice points at all eight corners plus one additional point at the geometric center of the cube — hence 'body-centered.' The primitive cubic cell has corner points only. This central atom is a full lattice point equivalent to any corner atom; it is not an atom of a different type or a defect."

- question: "The seven crystal systems and fourteen Bravais lattices together form a complete classification — every periodic crystalline arrangement in three dimensions belongs to exactly one of these fourteen categories."
  type: true-false
  answer: true
  explanation: "This completeness is mathematically proven, not just empirically observed. By systematically applying all possible symmetry constraints to the six unit cell parameters (a, b, c, α, β, γ) and all valid centering types, exactly 14 distinct translational symmetries arise. No valid periodic arrangement falls outside this classification, and none of the 14 is redundant."

- question: "Why do face-centered cubic metals like copper tend to be more ductile than body-centered cubic metals like iron at room temperature? Explain in terms of crystal structure and slip systems."
  type: short-answer
  answer: "FCC metals have atoms packed densely along {111} planes in <110> directions, producing 12 independent slip systems. With many available slip planes and directions, dislocations can move and multiply easily under stress, allowing large plastic deformation before fracture. BCC metals have fewer close-packed planes, so fewer slip systems are active at room temperature, requiring higher shear stress to move dislocations and resulting in higher strength but lower ductility."
  explanation: "The number of slip systems directly controls how easily a crystal can deform plastically by dislocation glide. More slip systems mean more paths for dislocations to travel without encountering barriers, giving the material flexibility to deform rather than crack. This is why FCC metals are the workhorses of forming and drawing operations in manufacturing."
```

## Explainer

From your study of atomic bonding, you know that atoms attract and repel each other in ways governed by the type of bond — metallic, ionic, covalent, or van der Waals. In a crystalline solid, atoms settle into the lowest-energy arrangement, and that arrangement repeats perfectly in three dimensions. This periodicity is not accidental: it is the natural result of atoms packing to maximize attractive interactions while maintaining stable bond angles and distances. The mathematical framework for classifying all possible periodic arrangements is the language of **crystal systems** and **Bravais lattices**.

A **crystal system** is defined by the geometry of the **unit cell** — the smallest repeating box that, when stacked in three directions, generates the entire crystal. The unit cell is described by three edge lengths (a, b, c) and three angles (α, β, γ) between them. Imposing different constraints on these six parameters yields exactly seven distinct crystal systems. The simplest and most symmetric is cubic (a = b = c, all angles 90°), which describes many metals (iron, copper, aluminum) and simple ionic solids. Tetragonal is like cubic but with one axis stretched (a = b ≠ c). Orthorhombic allows all three lengths to differ while keeping all right angles. Monoclinic tilts one axis (one angle ≠ 90°). Triclinic allows everything to differ — the lowest symmetry. Hexagonal uses a rhombus-shaped base with a 120° angle, describing graphite, zinc, and titanium. Rhombohedral (also called trigonal) has equal lengths and equal angles but angles ≠ 90°.

Within each crystal system, there can be multiple **Bravais lattices** depending on whether there are additional lattice points at face centers or body centers. A **primitive** lattice has points only at the unit cell corners; a **body-centered** lattice adds a point in the center of the cell; **face-centered** puts points at the center of each face; **base-centered** adds points only to two opposite faces. Not all centering types are distinct for all crystal systems — some combinations are equivalent to a simpler primitive cell with a smaller unit cell. Accounting for all valid combinations across the seven crystal systems yields exactly 14 distinct Bravais lattices. These 14 lattices are the complete catalog of all possible periodic translational symmetries in three dimensions — no more, no less.

Why does this classification matter for material properties? Because crystal geometry directly controls atomic packing density, slip systems for dislocation movement, anisotropy of mechanical and electrical properties, and how X-rays diffract from the structure. Face-centered cubic metals (copper, aluminum, gold) have 12 slip systems and deform easily, making them highly ductile. Body-centered cubic metals (iron at room temperature) have fewer close-packed slip systems and require higher stress to move dislocations, contributing to higher strength and lower ductility at low temperatures. The hexagonal system has a limited number of slip planes, which is why zinc and magnesium are more brittle than FCC metals. Every structure-property relationship in materials science ultimately traces back to the crystal system and lattice type.
