---
id: molecular-orbital-diagrams-and-bonding
title: Molecular Orbital Diagrams and Bond Order
domain: chemistry
course: physical-chemistry
prerequisites:
- id: molecular-orbital-theory-advanced
  type: hard
- id: orbital-theory-and-shapes
  type: hard
- id: quantum-mechanics-postulates-core
  type: soft
builds-toward:
- perturbation-theory-quantum-chemistry
- selection-rules-electronic-spectroscopy
tags:
- quantum
- bonding
- orbitals
- structure
stage: advanced
status: draft
---

# Molecular Orbital Diagrams and Bond Order

## Core Idea
Molecular orbital diagrams show how atomic orbitals combine to form bonding, antibonding, and nonbonding molecular orbitals in polyatomic molecules. Bond order—calculated as (bonding electrons − antibonding electrons) / 2—quantitatively relates orbital occupancy to bond strength and length. These diagrams provide a visual framework for understanding reactivity and spectroscopic properties.

## How It's Best Learned
Construct MO diagrams for small molecules (O₂, NO, F₂) by starting with atomic orbital energy levels, applying orbital overlap principles, and comparing predictions to experimental bond lengths and magnetic properties (paramagnetism). Verify bond orders using photoelectron spectroscopy data.

## Common Misconceptions
- Assuming higher bond order always means shorter, stronger bonds; actually, nonbonding electrons and occupied antibonding orbitals complicate this relationship. - Treating bonding and antibonding MOs as localized to atom pairs; they are delocalized over the entire molecular framework.

## Explainer

From molecular orbital theory, you know that when atoms combine to form molecules, their atomic orbitals mix to produce new orbitals that belong to the molecule as a whole. A **molecular orbital diagram** is the visual tool that organizes this information: atomic orbital energy levels are drawn on the left and right sides, and the molecular orbitals that form from their combination are drawn in the center, with lines connecting each MO to its parent atomic orbitals. The vertical axis represents energy, and electrons are filled into the molecular orbitals from lowest to highest energy, following the Aufbau principle and Hund's rule — exactly as you do for atomic electron configurations.

When two atomic orbitals of similar energy and compatible symmetry overlap, they produce two molecular orbitals: one lower in energy than either parent (**bonding**) and one higher (**antibonding**). The bonding MO has constructive interference of the wavefunctions — electron density builds up between the nuclei, pulling them together. The antibonding MO has destructive interference — a node between the nuclei depletes electron density there, and electrons in this orbital actively weaken the bond. Some atomic orbitals may lack a symmetry-compatible partner and pass through unchanged as **nonbonding** orbitals, contributing neither to bond strength nor weakness.

The **bond order** — calculated as (number of bonding electrons − number of antibonding electrons) / 2 — quantifies the net bonding effect. For O₂, the diagram predicts a bond order of 2 (a double bond), consistent with its bond length and strength. But the diagram reveals something Lewis structures cannot: O₂ has two unpaired electrons in its degenerate π* antibonding orbitals, making it paramagnetic. This is one of the great triumphs of MO theory — it explains O₂'s magnetism, which Lewis dot structures incorrectly predict as a non-issue. Similarly, the MO diagram for NO shows an odd electron in a π* orbital, giving a bond order of 2.5 and explaining its radical character.

Building diagrams for second-row diatomics requires knowing one important detail: for Li₂ through N₂, the σ₂p orbital lies above the π₂p orbitals (due to s-p mixing), while for O₂ and F₂, the σ₂p drops below the π₂p. Getting this ordering right is essential for correct electron configurations and magnetic predictions. Beyond diatomics, MO diagrams extend to polyatomic molecules through group theory and symmetry-adapted linear combinations of atomic orbitals, but the core logic remains the same: identify the symmetry-compatible orbital interactions, rank the resulting MOs by energy, fill electrons, and read off bond orders and electronic properties. The diagram is not just a bookkeeping device — it is a map of molecular electronic structure that predicts stability, reactivity, and spectroscopic behavior.
