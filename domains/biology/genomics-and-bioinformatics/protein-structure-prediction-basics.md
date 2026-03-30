---
id: protein-structure-prediction-basics
title: Protein Structure Prediction Basics
domain: biology
course: genomics-and-bioinformatics
prerequisites:
- id: translation
  type: hard
- id: amino-acid-structure-and-properties
  type: hard
- id: multiple-sequence-alignment
  type: soft
- id: blast-and-database-searching
  type: soft
builds-toward:
- machine-learning-in-genomics
- proteomics-data-analysis
tags:
- protein-folding
- homology-modeling
- AlphaFold
- secondary-structure
- tertiary-structure
stage: advanced
status: validated
---
# Protein Structure Prediction Basics

## Core Idea
Protein structure prediction aims to determine a protein's three-dimensional structure from its amino acid sequence. Homology modeling builds a structure by mapping the target sequence onto an experimentally determined template structure from a related protein. Threading (fold recognition) matches sequences to known structural folds even without clear sequence homology. Ab initio methods predict structure from physical principles or learned patterns without templates. AlphaFold2 revolutionized the field by using deep learning on multiple sequence alignments and structural databases to predict structures with near-experimental accuracy for most proteins.

## How It's Best Learned
Submit a protein sequence to the AlphaFold database and examine the predicted structure, paying attention to the per-residue confidence score (pLDDT). Compare regions of high and low confidence to known structural features (ordered domains vs. disordered loops). Then try homology modeling with SWISS-MODEL for the same protein and compare approaches.

## Common Misconceptions
- AlphaFold does not simulate the physical process of protein folding — it predicts the final folded structure using learned patterns from known structures and evolutionary co-variation.
- Predicted structures are not experimental data; confidence scores (pLDDT, PAE) must be checked, and low-confidence regions may not be reliable for detailed functional interpretation.

## Questions

```yaml
- question: "What is the key input that enables AlphaFold2 to predict protein structures with high accuracy?"
  type: multiple-choice
  options: ["The protein's mRNA sequence and ribosome binding sites", "A multiple sequence alignment of evolutionary relatives of the target protein", "The protein's experimentally measured circular dichroism spectrum", "The crystal structure of a closely related protein"]
  answer: 1
  explanation: "AlphaFold2's architecture relies heavily on a multiple sequence alignment (MSA) of homologous sequences. The patterns of amino acid co-variation in the MSA encode information about which residues are in spatial proximity — if two positions co-vary across evolution, they likely interact in the folded structure. The Evoformer module processes this co-evolutionary information alongside pairwise residue features to build a representation that the structure module converts into 3D coordinates. When few homologs are available, prediction accuracy typically decreases."

- question: "Homology modeling can only produce a reliable structure if the target protein shares at least 90% sequence identity with a template."
  type: true-false
  answer: false
  explanation: "Homology modeling can produce useful structures at much lower sequence identity, though accuracy decreases with divergence. Above 50% identity, models are typically reliable for backbone placement and many functional inferences. Between 30-50%, models are useful for overall fold and some functional predictions but less reliable for side-chain positioning. Below 30% (the 'twilight zone'), homology detection itself becomes unreliable, and threading or ab initio methods may be more appropriate. The 90% threshold is far too conservative."

- question: "Explain why a region of a protein with a low AlphaFold pLDDT score should be interpreted differently from a region with a high score."
  type: short-answer
  answer: "The pLDDT (predicted local distance difference test) score ranges from 0-100 and reflects AlphaFold's confidence in its prediction for each residue. High scores (>90) indicate that the predicted position is likely very close to the true structure and can be used for detailed structural analysis. Scores between 70-90 suggest the backbone is probably correct but side-chain positions may be approximate. Low scores (<50) often correspond to intrinsically disordered regions, flexible loops, or regions where the model lacks sufficient evolutionary information — these predicted coordinates should not be treated as reliable structural features."
  explanation: "Low pLDDT regions are not necessarily prediction failures — they may accurately reflect genuine structural disorder. The predicted aligned error (PAE) provides complementary information about the relative positions of domains, helping distinguish disordered regions from cases where domains are well-predicted individually but their relative orientation is uncertain."
```

## Explainer

The amino acid sequence of a protein determines its three-dimensional structure, which in turn determines its function. But going from sequence to structure computationally — the "protein folding problem" — was one of the grand challenges of biology for fifty years. Understanding the approaches, even at a high level, is essential because structural information increasingly drives functional annotation, drug design, and interpretation of genetic variants.

**Homology modeling** is the oldest and most intuitive approach. If a protein's sequence is similar to a protein whose structure has been experimentally determined (by X-ray crystallography, cryo-EM, or NMR), you can use that known structure as a template. The steps are: find a template using BLAST or HMM searches against structural databases (PDB), align the target sequence to the template, build a model by copying the template's backbone coordinates and adjusting for insertions, deletions, and substitutions, then refine the model. Accuracy depends on sequence identity to the template: above 50%, models are generally reliable; below 30%, the alignment becomes uncertain and the model unreliable.

**Threading** (fold recognition) extends this idea to cases where sequence similarity is undetectable but structural similarity exists — proteins can adopt similar folds despite having diverged beyond sequence recognition. Threading methods fit the target sequence into each fold in a library of known structures and evaluate the compatibility using energy functions. This approach bridges the gap between homology modeling and truly ab initio prediction, recognizing that the universe of protein folds is much smaller than the universe of protein sequences.

**AlphaFold2** (2020) transformed the field by achieving near-experimental accuracy for most protein domains. Its key insight is that evolutionary co-variation in multiple sequence alignments encodes structural contact information — if two positions consistently co-vary across homologous sequences, the corresponding residues likely interact in 3D. AlphaFold2's neural network architecture (particularly the Evoformer module) processes MSA features and pairwise residue relationships through iterative attention mechanisms, producing 3D coordinates along with confidence estimates. The AlphaFold Protein Structure Database now contains predicted structures for over 200 million proteins, making structural information available for essentially every known protein sequence. However, AlphaFold predictions still carry uncertainty (reflected in pLDDT and PAE scores), and the method struggles with proteins that lack many homologs, intrinsically disordered regions, and complexes whose interaction partners are not specified.
