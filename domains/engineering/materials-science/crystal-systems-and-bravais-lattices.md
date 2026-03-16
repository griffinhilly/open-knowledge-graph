---
id: crystal-systems-and-bravais-lattices
title: Crystal Systems and Bravais Lattices
domain: engineering
course: materials-science
prerequisites:
- id: crystal-structure-basics
  type: hard
- id: atomic-bonding-in-materials
  type: soft
builds-toward:
- miller-indices
- elastic-anisotropy
- x-ray-diffraction-materials
tags:
- crystal-geometry
- symmetry
- lattice-structures
stage: formal-systems
status: draft
---

# Crystal Systems and Bravais Lattices

## Core Idea
Crystals are classified into seven crystal systems (cubic, tetragonal, orthotropic, hexagonal, trigonal, monoclinic, triclinic) based on unit cell geometry. Each system contains one or more Bravais lattices—14 total—that describe the repeating pattern of lattice points in space. This classification enables systematic prediction of crystal properties and symmetry-allowed transformations.

## How It's Best Learned
Study unit cell dimensions and angles for each system, then explore how symmetry operations and lattice translations generate distinct Bravais lattices. Crystallographic databases and 3D models are invaluable for visualizing three-dimensional arrangements.

## Common Misconceptions
Crystal systems and Bravais lattices are not the same: systems describe geometry while lattices describe point arrangements. Not all systems have multiple lattices; cubic has three while monoclinic has two.

## Explainer

From your crystal structure basics, you know that crystalline materials are built from a repeating unit cell — a small box that tiles space perfectly. The next question is: how many fundamentally different shapes can that box take? The answer is seven, and these are the **seven crystal systems**. The systems are distinguished by the relationships among the three unit cell edge lengths (a, b, c) and the angles between them (α, β, γ). The most symmetric system, **cubic**, has a = b = c and all right angles. Reducing symmetry progressively gives you tetragonal (a = b ≠ c, all 90°), orthorhombic (all different lengths, all 90°), hexagonal (a = b ≠ c, with a 120° angle), trigonal (rhombohedral — equal lengths but non-right angles), monoclinic (all different lengths, one non-right angle), and triclinic (the least symmetric: all different lengths and all angles different from 90°).

The crystal systems tell you about geometry, but the **Bravais lattices** go deeper: they describe how lattice points are actually arranged in space, accounting for the possibility of additional lattice points beyond the corners of the unit cell. Within the cubic system, for example, you can have a **primitive** (P) lattice with points only at corners, a **body-centered** (I) lattice with an additional point at the center of the cube, or a **face-centered** (F) lattice with additional points at the center of each face. These three are physically distinct — they have different packing efficiencies, different nearest-neighbor distances, and different x-ray diffraction patterns. Across all seven crystal systems, counting all possible primitive and centered variants consistent with each system's symmetry, you arrive at exactly **14 Bravais lattices**. The French crystallographer Auguste Bravais proved in 1848 that no other distinct periodic point arrangements are possible in three dimensions.

Why does this classification matter? Because symmetry constrains physical properties. A cubic crystal is isotropic in many properties — its elastic stiffness, thermal expansion, and electrical conductivity are the same in any direction. A triclinic crystal has no such symmetry and is fully anisotropic — all properties can differ along x, y, and z. This connects directly to your future study of elastic anisotropy and Miller indices: once you know the Bravais lattice, you know which crystal directions and planes are symmetry-equivalent, which determines which reflections appear in an x-ray diffraction pattern (the systematic absences) and how the material will respond to applied stresses in different orientations.

The most practically important lattices for metals are the three cubic ones and the hexagonal lattice. Iron (and steel) transforms between body-centered cubic (BCC) and face-centered cubic (FCC) depending on temperature — a fact that underlies all of heat treatment. Aluminum, copper, and nickel are FCC; tungsten and chromium are BCC; zinc, magnesium, and titanium are hexagonal close-packed (HCP, which is the hexagonal Bravais lattice with a two-atom basis). The different packing geometries directly determine how many slip systems are available for plastic deformation: FCC has 12 slip systems and deforms easily, while HCP has only 3 and is more brittle. Learning to recognize a Bravais lattice from its geometry is the first step toward predicting how any crystalline material will behave under load, heat, or radiation.
