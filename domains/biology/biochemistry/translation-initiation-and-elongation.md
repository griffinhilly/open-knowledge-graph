---
id: translation-initiation-and-elongation
title: 'Translation: Initiation and Elongation'
domain: biology
course: biochemistry
prerequisites:
- id: translation
  type: hard
- id: ribosomes-and-protein-synthesis-intro
  type: soft
- id: rna-types-and-structure
  type: soft
builds-toward:
- post-translational-modifications
tags:
- translation
- ribosome
- tRNA
- initiation factors
- elongation factors
stage: advanced
status: draft
---

# Translation: Initiation and Elongation

## Core Idea
Translation is the synthesis of proteins from mRNA on the ribosome using tRNAs as adaptor molecules. Initiation requires recognition of the start codon (AUG) by the initiator tRNA (fMet-tRNA in bacteria, Met-tRNAi in eukaryotes) and assembly of the ribosome initiation complex with initiation factors (IF1/2/3 in bacteria, eIF1-5 in eukaryotes). Elongation proceeds through three steps (cognate tRNA selection, peptide bond formation, translocation) catalyzed by elongation factors (EF-Tu/G in bacteria, eEF1A/eEF2 in eukaryotes). Termination occurs upon recognition of stop codons (UAA/UAG/UGA) by release factors.

## Explainer

You already know that the ribosome reads mRNA to build proteins and that tRNAs serve as adaptor molecules, each carrying a specific amino acid matched to a three-nucleotide anticodon. The details of how this process actually works — how the machinery assembles, reads the message, and builds the chain — fall into three phases: **initiation**, **elongation**, and termination.

**Initiation** is the most regulated phase because it determines which mRNAs get translated and how efficiently. In bacteria, the small ribosomal subunit (30S) binds to a specific sequence on the mRNA called the **Shine-Dalgarno sequence**, which positions the start codon (AUG) in the correct reading frame. The initiator tRNA, carrying **N-formylmethionine (fMet)**, binds directly to this start codon with the help of three initiation factors (IF1, IF2, IF3). Only then does the large subunit (50S) join to form the complete 70S ribosome. In eukaryotes, the process is more elaborate: the small subunit (40S) is loaded with the initiator Met-tRNAᵢ and a suite of eukaryotic initiation factors (eIFs), then scans along the mRNA from the 5' cap until it finds the first AUG in a favorable sequence context (the Kozak sequence). The large subunit (60S) then joins to form the 80S ribosome. In both cases, the result is the same: a complete ribosome positioned at the start codon, with the initiator tRNA sitting in the **P site** (peptidyl site), ready for elongation.

**Elongation** is the repetitive heart of translation — a three-step cycle that adds one amino acid per round. First, an aminoacyl-tRNA (charged with the correct amino acid) is delivered to the **A site** (aminoacyl site) by elongation factor EF-Tu (bacteria) or eEF1A (eukaryotes), which uses GTP hydrolysis to ensure that only the tRNA with the correct anticodon is accepted — a **proofreading** step that gives translation its accuracy. Second, the ribosome catalyzes **peptide bond formation**: the amino acid in the P site is transferred onto the amino acid in the A site, extending the growing polypeptide by one residue. This reaction is catalyzed by the large subunit's peptidyl transferase activity, which is actually an RNA enzyme (ribozyme), not a protein. Third, **translocation** shifts the ribosome one codon forward along the mRNA, powered by EF-G (bacteria) or eEF2 (eukaryotes) and another round of GTP hydrolysis. The now-empty tRNA moves to the E site (exit site) and leaves, the peptidyl-tRNA moves from A to P, and a new codon is exposed in the empty A site. This cycle repeats at a rate of roughly 15–20 amino acids per second in bacteria.

The entire process consumes significant energy — two GTP molecules per amino acid added (one for tRNA selection, one for translocation), plus the ATP equivalents used earlier to charge each tRNA with its amino acid. This high energy cost buys accuracy and speed. The ribosome's error rate is approximately one wrong amino acid per 10,000 incorporated — remarkable given that it must discriminate between 20 different aminoacyl-tRNAs at each position using only three base pairs of codon-anticodon interaction. Translation continues until a **stop codon** (UAA, UAG, or UGA) enters the A site, where it is recognized not by a tRNA but by **release factors** that trigger hydrolysis of the completed polypeptide from the final tRNA, followed by disassembly of the ribosomal complex.
