---
id: molecular-orbital-diagrams
title: Constructing Molecular Orbital Diagrams for Diatomics
domain: chemistry
course: physical-chemistry
prerequisites:
- id: quantum-chemistry-foundations
  type: hard
- id: molecular-orbital-theory-advanced
  type: soft
builds-toward:
- bonding-antibonding-orbitals
tags:
- MO-diagrams
- diatomics
- bond-order
- paramagnetism
- energy-levels
stage: advanced
status: draft
---

# Constructing Molecular Orbital Diagrams for Diatomics

## Core Idea
Molecular orbital (MO) diagrams are energy-level diagrams that show how atomic orbitals on separate atoms combine to form molecular orbitals shared across the molecule. For homonuclear diatomics, atomic orbitals of the same symmetry mix to produce bonding (lower energy) and antibonding (higher energy) MOs, and the filling order follows Aufbau, Pauli, and Hund principles. Bond order = (bonding electrons - antibonding electrons)/2 predicts bond strength and existence; the diagram also reveals magnetic properties directly, since unpaired electrons in degenerate MOs produce paramagnetism. A key subtlety is the s-p mixing (orbital ordering switch) that occurs for diatomics lighter than O2, where the sigma-2p orbital rises above the two pi-2p orbitals.

## How It's Best Learned
Construct MO diagrams for the full series Li2 through Ne2, filling electrons and computing bond orders at each step. Compare predicted magnetic behavior (paramagnetic vs diamagnetic) to experimental data -- the O2 case is the classic validation.

## Common Misconceptions
- Assuming the MO energy ordering is the same for all second-row diatomics; the s-p mixing reversal for B2, C2, and N2 changes the sigma/pi ordering below O2.
- Equating bond order with bond strength across different elements; bond order comparisons are most meaningful within the same pair of atoms or isoelectronic series.

## Explainer

From your study of quantum chemistry foundations and molecular orbital theory, you know that electrons in molecules occupy orbitals that extend over the entire molecule, not just individual atoms. A **molecular orbital (MO) diagram** is the visual tool for organizing these orbitals by energy and seeing how they arise from atomic orbital combinations. Building one for a homonuclear diatomic like O₂ or N₂ follows a systematic procedure that, once mastered, provides immediate predictions about bond strength, bond order, and magnetic behavior.

Start by placing the atomic orbital energy levels for each atom on the left and right sides of the diagram. For second-row diatomics, you use the 2s and 2p orbitals. Orbitals combine according to symmetry: the two 2s orbitals form a **σ₂s** (bonding) and **σ*₂s** (antibonding) pair. The 2p orbitals split by their orientation relative to the internuclear axis. The two p orbitals pointing along the axis (pz) combine to form **σ₂p** and **σ*₂p**, while the perpendicular pairs (px, py) form two degenerate **π₂p** (bonding) and **π*₂p** (antibonding) pairs. Every atomic orbital that goes in produces one bonding and one antibonding MO — orbital count is conserved.

The critical subtlety is the **s-p mixing** (also called s-p hybridization in the MO context). For lighter diatomics — Li₂ through N₂ — the 2s and 2p energy levels on the atoms are close enough that the σ₂s and σ₂p orbitals interact, pushing σ₂p up in energy above the π₂p orbitals. This gives the ordering: σ₂s < σ*₂s < π₂p < σ₂p < π*₂p < σ*₂p. For O₂ and F₂, the larger 2s-2p energy gap reduces this mixing, and the "normal" ordering holds: σ₂p drops below π₂p. Getting this switch right is essential — it determines whether B₂ and C₂ are paramagnetic or diamagnetic.

Once the energy levels are set, fill electrons from the bottom up following the **Aufbau principle**, **Pauli exclusion** (two electrons per orbital, opposite spins), and **Hund's rule** (fill degenerate orbitals singly before pairing). Then calculate **bond order = (bonding electrons − antibonding electrons)/2**. For O₂, you fill 12 electrons and get bond order 2 (a double bond), but the diagram also reveals two unpaired electrons in the degenerate π*₂p orbitals — correctly predicting that O₂ is **paramagnetic**, a fact that Lewis structures cannot explain. For N₂, bond order is 3 (a triple bond) with no unpaired electrons (diamagnetic). Ne₂ gives bond order 0 — confirming that neon does not form a stable diatomic. The MO diagram thus unifies bond strength, bond existence, and magnetic properties in a single framework.
