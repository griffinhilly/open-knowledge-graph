---
id: unit-cell-lattice-parameters
title: Unit Cells and Lattice Parameters
domain: engineering
course: materials-science
prerequisites:
- id: crystal-structure-classification
  type: hard
builds-toward:
- crystal-planes-miller-indices
tags:
- unit-cell
- lattice-parameter
- crystal-geometry
stage: formal-systems
status: validated
---

# Unit Cells and Lattice Parameters

## Core Idea
A unit cell is the smallest repeating unit that, when stacked in three dimensions, recreates the entire crystal structure. Lattice parameters (edge lengths a, b, c and angles α, β, γ) define the unit cell geometry and are fundamental descriptors of crystal structure. Different crystal structures can share the same Bravais lattice but contain different atoms within the unit cell, leading to distinct properties.

## Questions

```yaml
- question: "A student draws an FCC unit cell showing 8 corner atoms and 6 face-center atoms. A classmate says the unit cell contains 14 atoms — one for each atom visible in the diagram. What is the correct count?"
  type: multiple-choice
  options:
    - "14 — all atoms shown in the diagram belong to the unit cell"
    - "6 — only the face-center atoms belong fully; corner atoms are shared with other cells"
    - "4 — corner atoms contribute 1/8 each (total 1) and face-center atoms contribute 1/2 each (total 3)"
    - "2 — only atoms in the strict interior of the unit cell are counted"
  answer: 2
  explanation: "Atoms are shared between adjacent unit cells: each corner atom sits at the intersection of 8 unit cells, contributing 1/8 per cell; each face-center atom borders 2 cells, contributing 1/2 per cell. FCC: 8×(1/8) + 6×(1/2) = 1 + 3 = 4 atoms. The classmate's error of 14 is the most common misconception — the drawing shows atoms positioned at cell boundaries, but most of their 'mass' belongs to neighboring cells. The correct count of 4 is what gives FCC its high atomic packing factor of 0.74."

- question: "FCC has a higher atomic packing factor (0.74) than BCC (0.68). What is the primary reason?"
  type: multiple-choice
  options:
    - "FCC has more atoms per unit cell (4 vs 2), and the face-centered arrangement allows atoms to touch along the face diagonal, achieving closer packing"
    - "FCC atoms are smaller than BCC atoms, so they fit more tightly into the same lattice"
    - "BCC has a body-center atom that creates unavoidable voids between corner atoms"
    - "FCC has a larger unit cell volume than BCC, distributing atoms over more space and reducing overlap"
  answer: 0
  explanation: "In FCC, atoms touch along the face diagonal: 4r = a√2, giving the optimal relationship between atom radius and cell size. The face-centered arrangement gives each atom 12 nearest neighbors — the highest coordination number for equal-sphere packing — achieving the theoretical maximum packing of 74%. BCC atoms touch along the body diagonal (4r = a√3) with 8 nearest neighbors and 68% packing. The difference arises from the geometry of how spheres can nest together, not from differences in atom size."

- question: "A corner atom in a unit cell contributes exactly 1/8 of an atom to that cell because it is simultaneously shared among 8 adjacent unit cells that meet at that corner."
  type: true-false
  answer: true
  explanation: "In a three-dimensional crystal, each corner of a unit cell is where eight unit cells meet (imagine 8 cubes sharing a single corner point). The atom at that corner is shared equally among all 8 cells, contributing 1/8 to each. This convention ensures that when unit cells tile all of space, every atom is counted exactly once. The same logic gives face-center atoms a contribution of 1/2 (shared by 2 cells), edge atoms 1/4 (shared by 4 cells), and interior atoms 1 (belonging to one cell only)."

- question: "The lattice parameter 'a' of a pure metal is a fixed material constant that does not change with temperature or the addition of solute atoms."
  type: true-false
  answer: false
  explanation: "Lattice parameters are not fixed constants. Thermal expansion increases average interatomic spacing as atomic vibration amplitudes grow with temperature, measurably increasing 'a'. Substitutional solute atoms larger than the host expand the lattice (positive misfit strain); smaller solutes contract it. These changes are not negligible — X-ray diffraction measurements of lattice parameter shifts are used in industrial quality control to measure residual stress, composition gradients, and the degree of solid solution formation."

- question: "A materials engineer calculates the theoretical density of an aluminum sample from its FCC structure and lattice parameter (a = 4.05 Å), getting 2.70 g/cm³. The measured bulk density is 2.63 g/cm³. What does this discrepancy most likely indicate?"
  type: short-answer
  answer: "The lower-than-theoretical density indicates structural defects that reduce average mass per unit volume. The most likely causes are: vacancies (missing atoms at lattice sites, reducing the actual atom count per unit volume below the perfect-crystal prediction), porosity (voids that contribute volume without mass), or substitutional impurities of lower atomic mass than aluminum. The theoretical density formula ρ = (n·A)/(V_c · N_A) assumes every lattice site is occupied by the correct atom."
  explanation: "Conversely, a higher measured density would suggest a denser impurity phase or measurement error. This diagnostic use of density — comparing measured to theoretical — illustrates how macroscopic, easily measured properties directly reflect atomic-scale crystal structure, making lattice parameter calculations practically useful for quality control."
```

## Explainer

From crystal structure classification, you know that atoms in crystals arrange in repeating, periodic patterns. The **unit cell** is the minimal building block of that pattern — the smallest volume element that, when tiled perfectly in three dimensions, recreates the entire crystal without gaps or overlaps. Think of it like a single tile in a mosaic: everything about the larger pattern is encoded in that one tile. The unit cell is not a physical object you can hold; it is the mathematical primitive from which the macroscopic crystal is constructed by translation along three axes.

The six **lattice parameters** — edge lengths a, b, c and interaxial angles α, β, γ — completely specify the unit cell geometry. For a cubic system (highest symmetry), a = b = c and α = β = γ = 90°, so a single number fully describes the structure. Most engineering metals fall in the cubic or hexagonal systems: FCC and BCC structures need only the edge length a; HCP structures need a and c. Triclinic systems (lowest symmetry) require all six independent parameters. Lattice parameters are typically 2–6 Ångströms (0.2–0.6 nm) — a scale invisible to all but X-rays or electrons, which is why X-ray diffraction is the standard measurement technique. Bragg's law, n λ = 2d sin θ, connects measurable diffraction angles to interplanar spacings, which are directly computed from lattice parameters.

The number of atoms per unit cell and their positions determine properties like **atomic packing factor** (APF) and theoretical density. Counting atoms in a unit cell requires accounting for sharing: a corner atom belongs to 8 adjacent unit cells (contributing 1/8 each), a face-center atom belongs to 2 cells (1/2 each), and a body-center atom belongs only to its own cell (1). FCC: 8×(1/8) + 6×(1/2) = 4 atoms per cell, APF = 0.74 — the densest possible packing of equal spheres. BCC: 8×(1/8) + 1 = 2 atoms per cell, APF = 0.68. Theoretical density follows from ρ = (n · A)/(V_c · N_A), connecting atomic-scale structure to macroscopic, measurable bulk density. If your experimental density deviates significantly from this calculation, it signals vacancies, substitutional impurities, or porosity.

Lattice parameters are not fixed constants — they respond to composition, temperature, and stress. Substituting a solute atom larger than the host (e.g., tin in copper) expands the lattice; smaller solute atoms contract it. Thermal expansion reflects increasing atomic vibration amplitude, widening average interatomic spacing and increasing a with temperature. Measuring lattice parameter shifts under applied mechanical load is the basis of X-ray stress analysis used in industrial quality control. These geometric relationships build directly toward **crystal planes and Miller indices**, where the lattice parameters establish the coordinate system used to describe the orientation of planes and directions within the crystal — essential for understanding slip systems, diffraction patterns, and anisotropic mechanical behavior.
