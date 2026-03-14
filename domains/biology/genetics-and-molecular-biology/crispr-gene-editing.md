---
id: crispr-gene-editing
title: CRISPR-Cas9 Gene Editing
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: molecular-cloning
  type: hard
- id: gene-regulation-eukaryotes
  type: hard
- id: dna-repair-mechanisms
  type: hard
tags:
- CRISPR
- Cas9
- guide RNA
- gene editing
- HDR
- NHEJ
- genome editing
stage: formal-systems
status: validated
---

# CRISPR-Cas9 Gene Editing

## Core Idea
CRISPR-Cas9 is an RNA-guided endonuclease system adapted from bacterial adaptive immunity that enables precise, programmable editing of genomic DNA. A single guide RNA (sgRNA) complementary to a 20-nucleotide target sequence directs the Cas9 protein to the desired locus, where it creates a double-strand break. The break is then repaired by either non-homologous end joining (NHEJ), which typically introduces insertions or deletions that disrupt gene function, or homology-directed repair (HDR), which uses a provided template to introduce precise edits. CRISPR has transformed biomedical research and is being developed for therapies for genetic diseases such as sickle cell disease.

## How It's Best Learned
Design a guide RNA for a gene of interest, verify that a PAM sequence (NGG) is present adjacent to the target, and predict both NHEJ and HDR outcomes. Discuss ethical considerations alongside the technical applications.

## Common Misconceptions
- CRISPR does not directly edit DNA; it creates a break that cellular repair machinery then mends — often imperfectly.
- Off-target cuts at sequences similar to the guide RNA are a real concern; high-fidelity Cas9 variants and careful guide design mitigate but do not eliminate this risk.
