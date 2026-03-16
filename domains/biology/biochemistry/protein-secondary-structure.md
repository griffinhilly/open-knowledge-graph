---
id: protein-secondary-structure
title: Protein Secondary Structure
domain: biology
course: biochemistry
prerequisites:
- id: protein-primary-structure
  type: hard
- id: peptide-bonds-and-polypeptide-formation
  type: hard
builds-toward:
- protein-tertiary-structure
- enzyme-structure-and-function
tags:
- secondary structure
- alpha helix
- beta sheet
- hydrogen bonding
- Ramachandran plot
stage: advanced
status: draft
---

# Protein Secondary Structure

## Core Idea
Secondary structure refers to repeating, hydrogen-bonded conformations of the polypeptide backbone, primarily alpha-helices and beta-sheets, as well as loops and turns. These structures are stabilized by hydrogen bonds between backbone carbonyl oxygens and backbone amide hydrogens, independent of side-chain identity. The phi (φ) and psi (ψ) dihedral angles of the backbone are restricted to energetically favorable regions (Ramachandran plot), which explains why only certain secondary structures are observed.

## How It's Best Learned
Use molecular visualization software (Jmol, PyMOL) to examine real protein structures and identify alpha-helices and beta-sheets. Study the Ramachandran plot and understand which amino acids (e.g., proline, glycine) are secondary-structure breakers.

## Common Misconceptions
- Assuming all proteins are mostly alpha-helix; many proteins have significant beta-sheet, coil, or loop content.
- Not recognizing that secondary structure propensities vary; some amino acids prefer helices, others prefer strands.
- Forgetting that glycine and proline are destabilizers; glycine is too flexible (no side chain constraints) and proline breaks alpha-helices.

## Explainer

You know from studying primary structure that a protein's amino acid sequence is a linear chain of residues connected by peptide bonds. But a linear chain does not just flop around randomly — the polypeptide backbone folds into regular, repeating patterns stabilized by hydrogen bonds between backbone atoms. These repeating patterns are **secondary structure**, and the two most common forms are the **alpha-helix** and the **beta-sheet**.

In an **alpha-helix**, the polypeptide backbone coils into a right-handed spiral. Each backbone carbonyl oxygen (C=O) forms a hydrogen bond with the amide hydrogen (N-H) of the residue four positions ahead in the sequence. This i → i+4 hydrogen bonding pattern creates a compact, rod-like structure with 3.6 residues per turn. The side chains project outward from the helix, away from the backbone core. Alpha-helices are common in membrane-spanning proteins (where hydrophobic side chains face the lipid bilayer) and in structural proteins like keratin, where coiled-coil arrangements of helices provide tensile strength.

In a **beta-sheet**, the backbone is nearly fully extended, and hydrogen bonds form between adjacent strand segments rather than within a single stretch. The strands can run in the same direction (**parallel**) or in opposite directions (**antiparallel**), and the hydrogen bonding geometry differs slightly between the two arrangements. Antiparallel sheets have straighter, stronger hydrogen bonds. Beta-sheets form flat, rigid surfaces and are common in structural proteins like silk fibroin and in the core of many globular proteins. **Turns** and **loops** connect helices and sheets, allowing the polypeptide to change direction; beta-turns, often involving proline and glycine, are particularly common connectors.

What determines which secondary structure a given stretch of sequence will adopt? The answer lies in the **Ramachandran plot**, which maps the energetically allowed combinations of the two backbone dihedral angles **phi (φ)** and **psi (ψ)** for each residue. Steric clashes between backbone atoms and side chains restrict most residues to a few allowed regions on this plot — and these regions correspond precisely to alpha-helices, beta-sheets, and a few other conformations. **Glycine**, lacking a side chain, has an unusually broad range of allowed angles, which makes it too flexible to sustain regular secondary structure but ideal for tight turns. **Proline**, with its cyclic side chain bonded back to the backbone nitrogen, locks phi at approximately -60° and cannot donate a backbone hydrogen bond, making it a helix-breaker that often signals the end of an alpha-helix or the start of a turn. Understanding secondary structure is the essential bridge between sequence and the three-dimensional folding (tertiary structure) that determines a protein's function.
