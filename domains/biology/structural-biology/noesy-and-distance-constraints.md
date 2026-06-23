---
id: noesy-and-distance-constraints
title: NOESY and Distance Constraints
domain: biology
course: structural-biology
prerequisites:
- id: nmr-for-proteins
  type: hard
tags:
- NOESY
- NOE
- distance-restraint
- cross-relaxation
- structure-calculation
stage: expert
status: validated
---
# NOESY and Distance Constraints

## Core Idea
The Nuclear Overhauser Effect Spectroscopy (NOESY) experiment detects through-space proximity between hydrogen atoms by measuring the cross-relaxation between nuclei that are close in three-dimensional space (typically less than 5 Angstroms), regardless of their connectivity through covalent bonds. NOESY cross-peaks provide distance restraints — the closer two protons, the stronger the NOE signal. A network of thousands of such distance restraints (short, medium, and long-range) provides the primary experimental data for NMR protein structure determination. Long-range NOEs (between residues far apart in sequence but close in space) are the most valuable because they define the protein's three-dimensional fold.

## Questions

```yaml
- question: "An NOE is observed between a proton on residue 10 and a proton on residue 85. What type of structural information does this provide?"
  type: multiple-choice
  options:
    - "Residues 10 and 85 are connected by a covalent bond"
    - "Residues 10 and 85 are close in three-dimensional space (<5 Angstroms apart), even though they are far apart in the amino acid sequence — this long-range NOE constrains the protein's tertiary fold"
    - "Residue 10 is exactly 85 Angstroms from the protein surface"
    - "Residues 10-85 form a contiguous alpha helix"
  answer: 1
  explanation: "This is a long-range NOE — the most structurally informative type. It tells you that residues 10 and 85, which are 75 residues apart in the primary sequence, must be close in the folded protein's 3D structure. This constrains the global fold: it rules out all structures where these residues are far apart. A network of such long-range NOEs, combined with short-range NOEs (defining local secondary structure) and medium-range NOEs (defining helix/turn geometry), collectively determines the complete three-dimensional structure."

- question: "NOE intensity is proportional to the inverse sixth power of the distance between two protons (1/r^6). This means NOEs can reliably measure distances up to 10 Angstroms."
  type: true-false
  answer: false
  explanation: "The 1/r^6 dependence means that NOE intensity drops off extremely rapidly with distance. Doubling the distance reduces the intensity by a factor of 64 (2^6). In practice, NOEs are detectable only for proton pairs separated by less than about 5 Angstroms — signals from more distant pairs are too weak to distinguish from noise. This sharp distance cutoff is actually useful: it means that every observed NOE provides a reliable upper-bound distance restraint. NOEs are typically categorized into strong (<2.5 A), medium (2.5-3.5 A), and weak (3.5-5.0 A) distance bins rather than precise distance measurements, because quantitative NOE-to-distance conversion is complicated by spin diffusion, dynamics, and peak overlap."

- question: "Why are long-range NOEs more important for defining the protein fold than short-range NOEs?"
  type: short-answer
  answer: "Short-range NOEs (between residues i and i+1 to i+4) define local secondary structure — sequential backbone NOEs indicate helices, sheets, and turns. These constrain the backbone conformation locally but do not determine how secondary structure elements pack against each other in 3D space. Long-range NOEs (between residues more than 5 positions apart in sequence) constrain the relative positions of distant parts of the polypeptide chain — defining which helix packs against which sheet, which loops are close together, and how the overall fold is organized. A protein with only short-range NOEs would have defined secondary structure but unknown tertiary fold (like knowing the bricks but not the house plan). Long-range NOEs provide the blueprint for the three-dimensional architecture."
  explanation: "In practice, the completeness of long-range NOE assignments often determines the quality of the NMR structure. Automated NOE assignment algorithms (like CYANA's CANDID or ARIA) have greatly improved the completeness and accuracy of NOE networks, enabling routine NMR structure determination for proteins up to ~25 kDa."
```

## Explainer

The Nuclear Overhauser Effect is the physical phenomenon that makes NMR protein structure determination possible. When two hydrogen atoms are close in space, their nuclear spins interact through a process called **cross-relaxation**: if one spin is perturbed (by radiofrequency irradiation), it affects the magnetization of its nearby neighbors. This interaction depends on the distance between the nuclei — specifically, the cross-relaxation rate is proportional to **1/r^6** — making it extraordinarily sensitive to proximity. The **NOESY experiment** measures these cross-relaxation interactions systematically, producing a 2D spectrum where each cross-peak connects two protons that are close in space.

The key insight is that the NOE is a **through-space** interaction — it reports on three-dimensional proximity regardless of covalent connectivity. Two protons can be 100 residues apart in the amino acid sequence but produce a strong NOE if they are less than 5 Angstroms apart in the folded protein. This is exactly the information needed to determine the 3D fold: NOEs between sequentially distant but spatially close residues reveal how the polypeptide chain folds back on itself, how helices pack against sheets, and how the hydrophobic core is organized.

**Structure determination** from NOE data is a constraint satisfaction problem. Each observed NOE provides an **upper-bound distance restraint**: the two protons must be within ~5 Angstroms (for a weak NOE) or within ~2.5 Angstroms (for a strong NOE). A typical well-determined NMR structure uses 2,000-4,000 NOE distance restraints, supplemented by backbone dihedral angle restraints (from chemical shifts via TALOS) and sometimes residual dipolar couplings (from partial molecular alignment). Computational algorithms (simulated annealing in torsion angle space, implemented in programs like CYANA and Xplor-NIH) search for structures that simultaneously satisfy all restraints while maintaining good stereochemistry. The result is an **ensemble** of 20-40 structures, all consistent with the data, whose convergence (or lack thereof) directly reveals which regions are well-defined and which are flexible.

The practical challenges include **spectral overlap** (many protons have similar chemical shifts, making it hard to identify which peaks are which), **spin diffusion** (NOE transfer through intermediate protons can generate artifactual long-range NOEs), and **dynamics** (conformational averaging can modulate NOE intensities). Three-dimensional and four-dimensional NMR experiments (separating protons by their attached 13C or 15N chemical shift) address overlap, and careful analysis protocols handle spin diffusion and dynamics. Despite these challenges, NMR structure determination by NOESY distance restraints has produced thousands of protein structures in the PDB, uniquely capturing the solution-state, dynamic nature of biomolecules.
