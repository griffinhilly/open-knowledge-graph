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
stage: advanced
status: draft
---

# Unit Cells and Lattice Parameters

## Core Idea
A unit cell is the smallest repeating unit that, when stacked in three dimensions, recreates the entire crystal structure. Lattice parameters (edge lengths a, b, c and angles α, β, γ) define the unit cell geometry and are fundamental descriptors of crystal structure. Different crystal structures can share the same Bravais lattice but contain different atoms within the unit cell, leading to distinct properties.

## Explainer

From crystal structure classification, you know that atoms in crystals arrange in repeating, periodic patterns. The **unit cell** is the minimal building block of that pattern — the smallest volume element that, when tiled perfectly in three dimensions, recreates the entire crystal without gaps or overlaps. Think of it like a single tile in a mosaic: everything about the larger pattern is encoded in that one tile. The unit cell is not a physical object you can hold; it is the mathematical primitive from which the macroscopic crystal is constructed by translation along three axes.

The six **lattice parameters** — edge lengths a, b, c and interaxial angles α, β, γ — completely specify the unit cell geometry. For a cubic system (highest symmetry), a = b = c and α = β = γ = 90°, so a single number fully describes the structure. Most engineering metals fall in the cubic or hexagonal systems: FCC and BCC structures need only the edge length a; HCP structures need a and c. Triclinic systems (lowest symmetry) require all six independent parameters. Lattice parameters are typically 2–6 Ångströms (0.2–0.6 nm) — a scale invisible to all but X-rays or electrons, which is why X-ray diffraction is the standard measurement technique. Bragg's law, n λ = 2d sin θ, connects measurable diffraction angles to interplanar spacings, which are directly computed from lattice parameters.

The number of atoms per unit cell and their positions determine properties like **atomic packing factor** (APF) and theoretical density. Counting atoms in a unit cell requires accounting for sharing: a corner atom belongs to 8 adjacent unit cells (contributing 1/8 each), a face-center atom belongs to 2 cells (1/2 each), and a body-center atom belongs only to its own cell (1). FCC: 8×(1/8) + 6×(1/2) = 4 atoms per cell, APF = 0.74 — the densest possible packing of equal spheres. BCC: 8×(1/8) + 1 = 2 atoms per cell, APF = 0.68. Theoretical density follows from ρ = (n · A)/(V_c · N_A), connecting atomic-scale structure to macroscopic, measurable bulk density. If your experimental density deviates significantly from this calculation, it signals vacancies, substitutional impurities, or porosity.

Lattice parameters are not fixed constants — they respond to composition, temperature, and stress. Substituting a solute atom larger than the host (e.g., tin in copper) expands the lattice; smaller solute atoms contract it. Thermal expansion reflects increasing atomic vibration amplitude, widening average interatomic spacing and increasing a with temperature. Measuring lattice parameter shifts under applied mechanical load is the basis of X-ray stress analysis used in industrial quality control. These geometric relationships build directly toward **crystal planes and Miller indices**, where the lattice parameters establish the coordinate system used to describe the orientation of planes and directions within the crystal — essential for understanding slip systems, diffraction patterns, and anisotropic mechanical behavior.
