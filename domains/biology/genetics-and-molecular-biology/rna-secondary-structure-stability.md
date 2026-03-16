---
id: rna-secondary-structure-stability
title: RNA Secondary Structure and Folding Thermodynamics
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: rna-structure-and-base-pairing
  type: hard
- id: amino-acid-structure-and-properties
  type: soft
builds-toward:
- alternative-splicing-mechanisms
tags:
- rna-folding
- secondary-structure
- thermodynamic-stability
- structure-function
stage: formal-systems
status: draft
---

# RNA Secondary Structure and Folding Thermodynamics

## Core Idea
RNA molecules fold into complex secondary structures (hairpins, bulges, internal loops) through Watson-Crick base pairing and non-Watson-Crick interactions (wobble, Hoogsteen). The stability of these structures depends on base stacking energy and entropic costs, making longer stems and G-C rich regions more stable. RNA tertiary structure involves pseudoknots and long-range interactions that are crucial for catalytic function in ribozymes and ribosomal RNA.

## How It's Best Learned
Use free energy minimization algorithms like Mfold or RNAfold to predict secondary structures and compare predictions to experimental structures. Study how thermodynamic stability relates to function in regulatory RNAs.

## Common Misconceptions
- Assuming one 'correct' secondary structure (RNA ensembles contain multiple structures in dynamic equilibrium).
- Thinking temperature has minimal effect on RNA structure (it dramatically affects base pairing stability).
- Confusing thermodynamic stability with biological function.

## Explainer

From your study of RNA structure and base pairing, you know that RNA is single-stranded but can fold back on itself to form intramolecular base pairs. These base pairs are not random — they organize into recognizable **secondary structure motifs** that determine how an RNA molecule behaves in the cell. The most common motif is the **stem-loop** (or hairpin), where a stretch of complementary bases pairs to form a double-helical stem, connected by a loop of unpaired nucleotides at the turn. Other motifs include **bulges** (unpaired bases on one side of a stem), **internal loops** (unpaired bases on both sides), and **junctions** where three or more stems meet. Together, these elements define the secondary structure — the pattern of base pairing throughout the molecule.

The stability of each structural element comes down to thermodynamics. **Base stacking** — the hydrophobic and van der Waals interactions between adjacent, vertically stacked bases — is actually the dominant stabilizing force, even more than the hydrogen bonds between paired bases. G-C pairs are more stable than A-U pairs because they form three hydrogen bonds instead of two and stack more favorably. Longer stems are more stable because they accumulate more stacking energy. Working against stability is the **entropic cost** of constraining a flexible single-stranded molecule into a rigid folded structure — every base pair reduces the conformational freedom of the chain. The net stability of any structure is the balance between these favorable enthalpic contributions and unfavorable entropic costs, expressed as **free energy** (ΔG). More negative ΔG means a more stable structure.

A critical insight is that RNA does not exist as a single, frozen structure. At physiological temperature, an RNA molecule samples an **ensemble** of conformations, spending more time in lower-energy states but transiently visiting higher-energy alternatives. This dynamic behavior matters because some RNAs function by switching between conformations — **riboswitches** in bacteria, for example, change shape when they bind a small molecule, turning gene expression on or off. Computational tools like Mfold and RNAfold predict the minimum free energy structure by summing nearest-neighbor stacking parameters for every possible base-pairing arrangement, but the biologically relevant structure may not always be the thermodynamic minimum — proteins, ions (especially Mg²⁺), and the kinetics of co-transcriptional folding all influence which structure forms in vivo.

Beyond secondary structure, RNA can form **tertiary interactions** — long-range contacts between distant parts of the molecule. **Pseudoknots**, where a loop base-pairs with a region outside its own stem, are the most common tertiary motif and are critical for the function of ribozymes and the ribosome. These higher-order structures are what give catalytic RNAs their three-dimensional architecture, positioning functional groups precisely for chemical reactions. Understanding how secondary structure elements assemble into tertiary folds connects directly to understanding how the ribosome — itself largely an RNA machine — catalyzes peptide bond formation.
