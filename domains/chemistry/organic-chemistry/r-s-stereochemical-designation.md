---
id: r-s-stereochemical-designation
title: R/S Stereochemical Nomenclature
domain: chemistry
course: organic-chemistry
prerequisites:
- id: enantiomers-and-chirality
  type: hard
builds-toward:
- meso-compounds-prochirality
tags:
- nomenclature
- stereochemistry
- cahn-ingold-prelog
- absolute-configuration
stage: formal-systems
status: draft
---

# R/S Stereochemical Nomenclature

## Core Idea
The Cahn-Ingold-Prelog system assigns R (Rectus) or S (Sinister) to any chiral stereocenter. Atoms bonded to the stereocenter are ranked by atomic number (highest = 1). Viewing the stereocenter with group 4 pointing away, if 1→2→3 proceeds clockwise, the center is R; counterclockwise is S. This system unambiguously names enantiomers regardless of chemical properties.

## Explainer

You already understand from chirality that a carbon with four different substituents creates a stereocenter with two non-superimposable mirror-image arrangements. The R/S system gives each arrangement an unambiguous name so that chemists worldwide can communicate exactly which enantiomer they mean. The key is the **Cahn-Ingold-Prelog (CIP) priority rules**, which rank the four groups attached to the stereocenter using atomic number as the primary criterion.

Start by looking at the four atoms directly bonded to the stereocenter. The atom with the highest atomic number gets **priority 1**, the next highest gets **priority 2**, and so on down to **priority 4** (the lowest). If two substituents start with the same atom — say, both begin with carbon — you move outward to the next set of atoms along each chain and compare again. Think of it as a tiebreaker tournament: you keep expanding outward until the groups differ. One important detail: double and triple bonds are treated as if each bonded atom appears twice or three times. A C=O is treated as if the carbon is bonded to two oxygens and the oxygen is bonded to two carbons. This "phantom atom" trick lets the priority rules handle unsaturation without any special cases.

Once you have ranked all four groups from 1 (highest) to 4 (lowest), orient the molecule so that **group 4 points away from you** — imagine it is sticking into the page or behind the steering wheel. Now trace a path from group 1 to group 2 to group 3. If that arc sweeps **clockwise**, the stereocenter is **R** (from the Latin rectus, meaning "right"). If the arc sweeps **counterclockwise**, it is **S** (sinister, meaning "left"). A useful trick when working with standard wedge-dash drawings: if group 4 is already on a dash (pointing away), you can read the configuration directly. If group 4 is on a wedge (pointing toward you), determine the 1→2→3 direction and then reverse your answer — clockwise becomes S, counterclockwise becomes R — because you are looking at the mirror image of the correct viewpoint.

The R/S designation is an absolute configuration label — it stays the same regardless of what solvent the molecule is in, what reaction produced it, or which direction it rotates plane-polarized light. This is what makes it so powerful: two chemists in different labs can refer to (S)-ibuprofen and know they mean the exact same spatial arrangement of atoms. Note that R/S has no systematic relationship to (+) or (−) optical rotation; you cannot predict one from the other without either an experiment or a calculation. The naming is purely geometric.
