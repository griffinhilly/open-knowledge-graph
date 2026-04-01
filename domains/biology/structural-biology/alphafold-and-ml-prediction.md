---
id: alphafold-and-ml-prediction
title: AlphaFold and ML Prediction
domain: biology
course: structural-biology
prerequisites:
- id: homology-modeling
  type: hard
- id: protein-folding-and-chaperones
  type: hard
builds-toward:
- structure-based-drug-design
tags:
- AlphaFold
- deep-learning
- structure-prediction
- pLDDT
- protein-folding
- AI
stage: expert
status: validated
---
# AlphaFold and ML Prediction

## Core Idea
AlphaFold (DeepMind, 2020) and related deep learning methods (RoseTTAFold, ESMFold, OpenFold) predict protein structures from amino acid sequence with accuracy approaching experimental methods, achieving median backbone RMSD of ~1 Angstrom on CASP14 targets. AlphaFold2 uses a neural network architecture that processes multiple sequence alignments (MSAs) and pairwise residue features through an iterative "Evoformer" module and a structure module that outputs 3D coordinates with per-residue confidence scores (pLDDT). AlphaFold has been applied to predict structures for virtually every known protein sequence (>200 million in the AlphaFold Protein Structure Database), transforming structural biology from an experimental bottleneck to a computationally accessible resource. Limitations include poor performance on intrinsically disordered regions, difficulty with multiple conformational states, and challenges with protein-protein and protein-ligand interactions.

## Questions

```yaml
- question: "AlphaFold2 produces a confidence score (pLDDT) for each residue. A region with pLDDT < 50 should be interpreted as:"
  type: multiple-choice
  options:
    - "A very accurate prediction that can be trusted for atomic-level analysis"
    - "A region where the prediction is unreliable — likely intrinsically disordered, flexible, or lacking evolutionary information from the multiple sequence alignment. The 3D coordinates in this region should not be interpreted as a meaningful structure"
    - "A region that must be confirmed by X-ray crystallography before any interpretation"
    - "An artifact of the neural network that has no biological meaning"
  answer: 1
  explanation: "pLDDT (predicted Local Distance Difference Test) ranges from 0-100, with >90 indicating high confidence (comparable to experimental structures), 70-90 indicating good but less reliable prediction, and <50 indicating low confidence. Low-pLDDT regions typically correspond to intrinsically disordered regions (which genuinely lack a single stable structure), flexible loops, or regions where the MSA provides insufficient evolutionary information. Importantly, low pLDDT is often biologically meaningful — it often correctly identifies disordered regions. But the specific 3D coordinates in these regions should not be trusted, as the model is essentially guessing."

- question: "AlphaFold has solved the protein structure prediction problem, making experimental structural biology unnecessary."
  type: true-false
  answer: false
  explanation: "AlphaFold has dramatically advanced structure prediction, but experimental structural biology remains essential for several reasons: (1) AlphaFold predicts a single static structure, while many proteins function through conformational changes — experimental methods (cryo-EM classification, NMR dynamics) capture multiple states. (2) AlphaFold does not reliably predict ligand binding poses, protein-protein interaction geometries, or the effects of post-translational modifications. (3) AlphaFold cannot predict structures of proteins without homologs in evolutionary databases (orphan proteins). (4) Novel folds, engineered proteins, and de novo designed proteins lack the evolutionary information AlphaFold relies on. (5) Experimental validation is required for drug design, mechanistic studies, and any high-stakes structural interpretation. AlphaFold generates hypotheses; experiments validate them."

- question: "Why does AlphaFold rely on multiple sequence alignments (MSAs), and what happens when the MSA is shallow (few homologs)?"
  type: short-answer
  answer: "MSAs encode evolutionary information: which residues co-evolve (mutate in a correlated manner), reflecting spatial proximity in the 3D structure. These co-evolutionary signals are the primary source of information that AlphaFold uses to infer residue-residue contacts and ultimately 3D structure. When the MSA is shallow (the target protein has few homologs in sequence databases, as for orphan proteins or recently evolved sequences), co-evolutionary signals are weak or absent, and AlphaFold's accuracy drops significantly. Single-sequence methods (like ESMFold, which uses protein language model embeddings instead of MSAs) partially address this but are generally less accurate than MSA-based methods. The dependence on evolutionary information means AlphaFold is least reliable where it is most needed — for structurally novel proteins."
  explanation: "AlphaFold3 has expanded to predict protein-nucleic acid complexes, protein-ligand interactions, and post-translational modifications, addressing some limitations of AlphaFold2. However, the fundamental dependence on evolutionary information remains, and accuracy for novel targets and interactions continues to be lower than for well-represented protein families."
```

## Explainer

The protein structure prediction problem — determining a protein's 3D structure from its amino acid sequence — was one of the grand challenges of computational biology for 50 years. At the biennial CASP competition (Critical Assessment of protein Structure Prediction), the best methods gradually improved from producing vague shapes to reasonable backbone traces. Then AlphaFold2 arrived at CASP14 in 2020 and essentially solved the problem for single-domain proteins, producing predictions indistinguishable from experimental structures for many targets.

AlphaFold2's architecture has two key innovations. The **Evoformer module** processes a multiple sequence alignment (MSA) of the target protein and its evolutionary relatives, extracting co-evolutionary signals — patterns of correlated mutations that indicate spatial proximity. If positions i and j consistently mutate together across species (when i mutates to a larger residue, j compensates by mutating to a smaller one), they are likely in contact in the 3D structure. The Evoformer uses attention mechanisms to process these signals across the MSA and a pairwise representation, iteratively refining the predicted residue-residue relationships. The **structure module** then converts these refined representations into 3D coordinates, outputting both the structure and per-residue confidence scores (pLDDT).

The impact has been transformative. The **AlphaFold Protein Structure Database** provides predicted structures for over 200 million protein sequences — essentially every known protein in UniProt. Structural biology has shifted from "we need to determine this structure" to "we already have a prediction — does it need experimental validation for this particular question?" For many applications (identifying homologs, understanding domain architecture, guiding mutagenesis), AlphaFold predictions are sufficient. For drug design, enzyme mechanism analysis, and studying conformational dynamics, experimental structures remain necessary because the details matter at a level where AlphaFold's predictions may not be reliable.

The limitations are instructive. AlphaFold predicts **a single static structure**, but many proteins function through conformational changes — an enzyme may need to open and close, a receptor may switch between active and inactive states. AlphaFold typically predicts the most common or most stable conformation, potentially missing functionally critical alternative states. **Intrinsically disordered regions** are correctly identified (low pLDDT) but their coordinates are meaningless. **Protein-protein interactions**, **protein-ligand binding**, and **post-translational modification effects** are not reliably predicted by AlphaFold2 (AlphaFold3 makes progress here but accuracy varies). And for proteins without evolutionary homologs (de novo designed proteins, orphan sequences), the MSA provides no useful information, and prediction accuracy degrades. AlphaFold has not replaced structural biology — it has redefined the questions structural biologists need to answer, shifting focus from routine structure determination to functional dynamics, molecular interactions, and the biology that predictions alone cannot reveal.
