---
id: r-s-nomenclature-cahn-ingold-prelog-rules
title: R/S Nomenclature and Cahn-Ingold-Prelog Priority Rules
domain: chemistry
course: organic-chemistry
prerequisites:
- id: enantiomers-and-chirality
  type: hard
- id: fischer-projection-and-wedge-dash
  type: hard
builds-toward:
- stereoisomer-enumeration
- walden-inversion-sn2
tags:
- absolute-configuration
- r-s-nomenclature
- cip-rules
- chiral-center
stage: advanced
status: draft
---

# R/S Nomenclature and Cahn-Ingold-Prelog Priority Rules

## Core Idea
The Cahn-Ingold-Prelog rules assign priorities 1-4 to groups on a chiral center based on atomic number, then by atomic weight of attached atoms, then by examining second and third atoms iteratively. Once priorities are assigned, viewing the molecule with group 4 away and tracing 1→2→3 clockwise gives R (rectus); counterclockwise gives S (sinister). This absolute configuration system uniquely specifies each enantiomer.

## Explainer

You already know that a chiral center with four different substituents exists as two non-superimposable mirror images — enantiomers. But calling them "left" and "right" is ambiguous. The **Cahn-Ingold-Prelog (CIP) priority rules** provide an unambiguous naming system that assigns every chiral center an absolute configuration of either **R** (rectus, Latin for "right") or **S** (sinister, Latin for "left"), independent of how you draw or orient the molecule.

The system works in two stages: assign priorities, then determine direction. To assign priorities, look at the four atoms directly bonded to the chiral center and rank them by atomic number — higher atomic number gets higher priority. So iodine (53) beats bromine (35) beats chlorine (17) beats fluorine (9) beats oxygen (8) beats carbon (6) beats hydrogen (1). When two substituents start with the same atom, you move outward to the next atoms along each chain and compare again — this is the "tie-breaking" procedure. Double and triple bonds are treated as if each bonded atom appears twice or three times (a C=O is treated as C bonded to O,O and O bonded to C,C). This recursive comparison continues until the tie breaks.

Once you have priorities 1 through 4, orient the molecule so that priority 4 (the lowest — often hydrogen) points away from you, like the steering column of a car. Now trace a path from priority 1 → 2 → 3. If that path is **clockwise**, the center is R. If it is **counterclockwise**, the center is S. A practical shortcut when working with Fischer projections: if group 4 is on a horizontal bond (pointing toward you rather than away), the apparent rotation gives the wrong answer — so you assign the opposite designation.

The power of this system is that R and S designations are absolute — they do not depend on the orientation of your drawing, whether you use a wedge-dash diagram or a Fischer projection, or which enantiomer you happened to draw first. Two chemists on different continents can communicate the exact three-dimensional arrangement of a molecule using just a single letter. This becomes critical when you encounter reactions like SN2 that invert configuration: you can precisely state that an R substrate gives an S product, tracking stereochemistry through each mechanistic step.
