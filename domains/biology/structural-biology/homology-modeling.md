---
id: homology-modeling
title: Homology Modeling
domain: biology
course: structural-biology
prerequisites:
- id: protein-folding-and-stability
  type: hard
- id: pairwise-sequence-alignment
  type: hard
builds-toward:
- alphafold-and-ml-prediction
- structure-based-drug-design
tags:
- homology-modeling
- comparative-modeling
- template-based
- loop-modeling
- MODELLER
stage: expert
status: validated
---
# Homology Modeling

## Core Idea
Homology modeling (comparative modeling) predicts a protein's three-dimensional structure based on its sequence similarity to one or more experimentally determined template structures. Because protein structure is more conserved than sequence during evolution, proteins sharing >30% sequence identity typically share the same overall fold, enabling structure prediction by copying the template's backbone and rebuilding side chains and loops. The process involves template identification (BLAST, HHpred), sequence-template alignment, model building (MODELLER, SWISS-MODEL), and model validation (DOPE score, Ramachandran analysis). Homology modeling was the dominant computational structural biology method before AlphaFold, and understanding its principles remains important for interpreting and evaluating all predicted structures.

## Questions

```yaml
- question: "Below approximately what sequence identity does homology modeling become unreliable, and why?"
  type: multiple-choice
  options:
    - "Below 90% — even small sequence differences make modeling impossible"
    - "Below approximately 25-30% — at this level, sequences may not be reliably alignable, and structural divergence (especially in loops and at the protein surface) becomes large enough that the template no longer accurately represents the target's structure"
    - "Below 50% — this is a hard cutoff for all proteins"
    - "Sequence identity is irrelevant for homology modeling"
  answer: 1
  explanation: "The 25-30% identity threshold (the 'twilight zone') reflects two compounding problems: first, sequence alignments become unreliable (insertions, deletions, and substitutions make it uncertain which residues correspond), producing alignment errors that propagate into structural errors. Second, even if the alignment is correct, proteins at this divergence level have typically diverged in loop conformations, surface features, and sometimes core packing. The backbone RMSD between proteins with 30% identity is typically 1.5-2.0 Angstroms, with much larger deviations in loops. Below 20% identity ('midnight zone'), even fold recognition becomes uncertain, and homology modeling is essentially guesswork without additional information."

- question: "The main source of error in homology models comes from inaccurate side chain placement."
  type: true-false
  answer: false
  explanation: "While side chain placement contributes to error (especially for non-conserved residues), the main source of error in homology models is loop modeling and alignment errors. Loops — the regions connecting secondary structure elements — diverge rapidly during evolution and cannot be accurately modeled from the template because they typically differ in length and conformation. Alignment errors (incorrectly matching target residues to template residues) produce systematic shifts in the model that affect large portions of the structure. Core backbone regions and conserved secondary structures are usually well-modeled; it is the variable loops and alignment-ambiguous regions that limit model accuracy."

- question: "AlphaFold has made homology modeling obsolete. Understanding homology modeling principles is no longer important."
  type: true-false
  answer: false
  explanation: "AlphaFold has dramatically improved structure prediction accuracy, but understanding homology modeling remains important for several reasons: (1) interpreting confidence scores — AlphaFold's pLDDT score and predicted aligned error are best understood through the lens of homology modeling difficulties (loops and domains with no homologs have low confidence for the same reasons they are hard to model by homology). (2) Understanding model limitations — homology modeling principles explain why certain regions of any predicted structure are unreliable. (3) Multi-template modeling and protein engineering — designing mutations, insertions, or chimeric proteins requires understanding structure-sequence relationships that homology modeling formalizes. (4) Validation — assessing whether a predicted structure is reasonable uses the same tools and principles developed for homology models."
```

## Explainer

For decades before AlphaFold, the most reliable method for predicting a protein's structure was to find a relative with a known structure and copy it. This is **homology modeling** — the computational analog of the evolutionary insight that structure is more conserved than sequence. Two proteins that diverged from a common ancestor millions of years ago may share only 30% of their amino acid sequence, yet their three-dimensional folds are remarkably similar. Homology modeling exploits this conservation to build a structural model of a target protein using one or more experimentally determined template structures.

The workflow has four steps. **Template identification**: search the PDB for structures with sequence similarity to the target, using BLAST (sequence search) or HHpred (profile-profile search, more sensitive for distant homologs). **Alignment**: align the target sequence to the template sequence, determining which residues correspond. This is the most error-prone step — insertions, deletions, and ambiguous regions in the alignment directly produce errors in the model. **Model building**: programs like MODELLER or SWISS-MODEL copy the template backbone for aligned regions, model insertions/deletions (loops) using ab initio or knowledge-based methods, place side chains using rotamer libraries, and optimize the model through energy minimization. **Validation**: assess model quality using statistical potential scores (DOPE), stereochemical checks (Ramachandran plot), and comparison to experimental data if available.

The accuracy of homology models depends primarily on the **sequence identity** to the template. Above 50% identity, models are typically excellent — backbone RMSD to the true structure is ~1 Angstrom, and most side chain orientations are correct. Between 30-50%, the core fold is reliable but loops and surface features have significant errors. Between 20-30% (the "twilight zone"), alignment uncertainty becomes the dominant error source, and model quality varies widely. Below 20%, fold recognition itself becomes unreliable. The most problematic regions in any homology model are **loops** (connecting secondary structure elements), which diverge rapidly in evolution and are modeled ab initio rather than copied from the template — loop modeling remains one of the hardest unsolved problems in computational structural biology.

AlphaFold has transformed this landscape by using deep learning to predict structures from sequence with accuracy rivaling experimental structures for many proteins. But the conceptual framework of homology modeling remains relevant: AlphaFold's multi-sequence alignment input is effectively an automated version of homology modeling's template search, and its confidence scores (pLDDT, PAE) flag the same regions — loops, disordered segments, domains without homologs — that challenge traditional homology modeling. Understanding why some regions are hard to predict (lack of evolutionary conservation, conformational flexibility, sequence-structure ambiguity) is essential for interpreting any predicted structure, whether from MODELLER or AlphaFold.
