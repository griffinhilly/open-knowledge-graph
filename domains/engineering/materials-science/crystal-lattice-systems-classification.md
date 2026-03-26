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
status: validated
---

# Crystal Lattice Systems and Classification

## Core Idea
Crystals are periodic 3D arrangements of atoms in space, classified into seven crystal systems (cubic, tetragonal, orthorhombic, monoclinic, triclinic, hexagonal, trigonal) and 14 Bravais lattices. Each system has characteristic symmetry properties and lattice parameters (a, b, c, α, β, γ) that define the unit cell geometry and determine how atoms pack.

## Questions

```yaml
- question: "FCC metals (e.g., aluminum, copper) are generally more ductile at room temperature than BCC metals (e.g., iron at room temperature). The primary crystallographic reason is that FCC..."
  type: multiple-choice
  options:
    - "has a higher atomic packing factor (74% vs. 68%), reducing internal void space that would initiate cracks"
    - "has 12 equivalent slip systems on {111} close-packed planes, enabling dislocation movement in many orientations under applied stress"
    - "atoms are smaller and lighter, allowing more rapid atomic rearrangement during deformation"
    - "unit cells have fewer atoms, so dislocations travel shorter distances between obstacles"
  answer: 1
  explanation: "Ductility requires dislocations to move through the crystal — a process called slip. Slip occurs most easily on close-packed planes in close-packed directions. FCC has four equivalent {111} close-packed planes, each with three close-packed <110> directions, giving 12 equivalent slip systems. With so many geometrically equivalent paths for slip, at least one slip system is favorably oriented for almost any applied stress direction, enabling extensive plastic deformation. BCC has no truly close-packed plane, giving fewer active slip systems at typical stress levels, making it harder and less ductile."

- question: "A cubic unit cell (a = b = c, α = β = γ = 90°) is described as having atoms at all 8 corners plus one atom at the exact center of the cell. This describes a..."
  type: multiple-choice
  options:
    - "Face-centered cubic (FCC) lattice"
    - "Body-centered cubic (BCC) lattice"
    - "Simple hexagonal lattice"
    - "Tetragonal lattice with a body center"
  answer: 1
  explanation: "The description precisely defines BCC: corner atoms (shared among 8 unit cells, contributing 8 × 1/8 = 1 effective atom) plus one atom at the body center (entirely inside the unit cell) = 2 atoms per unit cell. FCC has atoms at corners plus one atom at the center of each of the 6 faces (6 × 1/2 = 3 effective face-center atoms, plus 1 corner = 4 atoms per unit cell). The body-center atom is at coordinates (1/2, 1/2, 1/2) — equidistant from all corners. Common BCC metals include iron (at room temperature), tungsten, and chromium."

- question: "Placing additional lattice points at body centers or face centers within a unit cell is a geometric option available primarily to the cubic crystal system."
  type: true-false
  answer: false
  explanation: "Body-centering and face-centering are available in multiple crystal systems, giving rise to the 14 Bravais lattices across 7 crystal systems. For example, body-centered tetragonal (BCT) is a distinct Bravais lattice used by martensite in steel. Face-centered orthorhombic and body-centered orthorhombic also exist. The 14 Bravais lattices are the exhaustive classification of all possible periodic 3D lattice types consistent with crystallographic symmetry — most crystal systems have 2–4 Bravais variants, not just a simple primitive cell."

- question: "The seven crystal systems are fully defined by specifying constraints on the six lattice parameters (a, b, c, α, β, γ) — for example, cubic requires a = b = c and α = β = γ = 90°."
  type: true-false
  answer: true
  explanation: "Each crystal system is characterized by symmetry constraints on the unit cell parameters. Cubic: a = b = c, α = β = γ = 90°. Tetragonal: a = b ≠ c, α = β = γ = 90°. Orthorhombic: a ≠ b ≠ c, α = β = γ = 90°. Monoclinic: a ≠ b ≠ c, α = γ = 90° ≠ β. Triclinic: no constraints. Hexagonal: a = b ≠ c, α = β = 90°, γ = 120°. These parameter constraints are a direct expression of the underlying point group symmetry — higher symmetry means more parameter equalities."

- question: "HCP (hexagonal close-packed) metals are generally less ductile than FCC metals at room temperature, even though both have the same theoretical atomic packing factor of 74%. Explain why."
  type: short-answer
  answer: "Both HCP and FCC achieve the same packing density, but their 3D arrangements of close-packed layers differ in stacking sequence (ABABAB vs. ABCABC) and available slip systems. HCP's only close-packed plane is the basal plane {0001}, providing just 3 slip systems at typical temperatures. FCC has 4 equivalent {111} planes, each with 3 directions, giving 12 slip systems. With fewer geometrically equivalent paths for dislocation movement, HCP crystals cannot accommodate applied stresses in arbitrary directions through slip, and they fracture instead. Adding temperature can activate non-basal slip in HCP metals, which is why titanium and magnesium are more ductile at elevated temperatures."
  explanation: "Packing efficiency tells you how much space atoms occupy — it says nothing about directionality of slip. Ductility is controlled by the number and equivalence of slip systems, which depends on crystal symmetry and which planes are close-packed. FCC's higher cubic symmetry gives four equivalent close-packed planes; HCP's lower hexagonal symmetry restricts close packing to one basal plane. This structural difference, not packing density, drives the ductility contrast."
```

## Explainer

From atomic bonding, you understand that atoms in a solid are held in place by bonds — covalent, ionic, or metallic — that have preferred lengths and angles. When a material solidifies slowly from the melt, atoms settle into the lowest-energy arrangement: a periodic, repeating 3D pattern called a **crystal lattice**. The periodicity is what makes crystalline materials fundamentally different from amorphous solids (like glass), where atoms are frozen in random arrangements. In a crystal, if you know where one atom is and you know the **unit cell** — the smallest repeating box — you know where every atom in the material is.

The **lattice parameters** (a, b, c, α, β, γ) define the unit cell: a, b, c are the edge lengths along three axes, and α, β, γ are the angles between those axes. The seven **crystal systems** are defined by symmetry constraints on these parameters. The most symmetric is **cubic** (a = b = c, α = β = γ = 90°), where the unit cell is a perfect cube. The least symmetric is **triclinic** (a ≠ b ≠ c, α ≠ β ≠ γ ≠ 90°), where all parameters are independent. The progression between them — tetragonal (one axis different), orthorhombic (all lengths different but right angles), monoclinic (one angle different), and hexagonal/trigonal — can be thought of as progressively removing symmetry from the perfect cube.

The **14 Bravais lattices** refine this classification by asking: within each crystal system, can additional lattice points be placed (at body centers or face centers) while maintaining the required symmetry? For example, the cubic system has three Bravais lattices: simple cubic (SC, atoms only at corners), **body-centered cubic** (BCC, corners plus one atom at the body center), and **face-centered cubic** (FCC, corners plus atoms at each face center). BCC iron at room temperature and FCC aluminum are canonical examples. The FCC lattice is the densest cubic packing, with an atomic packing factor of 74%; BCC is slightly less dense at 68%. These packing differences directly affect density, diffusion rates, and the slip systems available for plastic deformation.

Why does this classification matter for engineering? Because crystal structure governs almost every property you care about. FCC metals (Al, Cu, Ni, Au) are generally more ductile than BCC metals (Fe, W, Cr) because FCC has more equivalent slip planes for dislocations to move. Hexagonal close-packed (HCP) metals (Ti, Mg, Zn) have fewer slip systems and tend to be less ductile at room temperature. The crystal structure also determines cleavage planes (where brittle fracture occurs), anisotropy of elastic modulus, and even optical and electrical properties. When you later study crystallographic planes and directions, you will use the **Miller index** notation that builds directly on the unit cell coordinate system introduced here.

