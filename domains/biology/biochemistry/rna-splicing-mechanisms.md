---
id: rna-splicing-mechanisms
title: RNA Splicing Mechanisms
domain: biology
course: biochemistry
prerequisites:
- id: rna-processing
  type: hard
- id: rna-types-and-structure
  type: soft
builds-toward:
- translation-initiation-and-elongation
tags:
- splicing
- spliceosome
- introns
- exons
- lariat intermediate
stage: advanced
status: draft
---

# RNA Splicing Mechanisms

## Core Idea
RNA splicing is the removal of introns and ligation of exons in eukaryotic pre-mRNA, catalyzed by the spliceosome, a complex of small nuclear RNAs (snRNPs) and proteins. Splicing involves two transesterification reactions: the first cuts at the 5' splice site, releasing the intron lariat; the second ligates the upstream exon to the downstream exon. Alternative splicing, where different combinations of exons are joined, vastly increases proteomic diversity from a fixed number of genes. Errors in splicing are a major cause of genetic disease.

## Explainer

From your study of RNA processing, you know that eukaryotic genes are interrupted by non-coding **introns** that must be removed before the mRNA can be translated. Splicing is the molecular surgery that accomplishes this — precisely excising introns and joining the flanking **exons** into a continuous coding sequence. The precision required is extraordinary: a single nucleotide error would shift the reading frame and produce a nonfunctional protein. Understanding how the spliceosome achieves this accuracy reveals one of the most elegant molecular machines in the cell.

The spliceosome is not a static enzyme but a dynamic assembly of five **small nuclear ribonucleoprotein particles (snRNPs)** — U1, U2, U4, U5, and U6 — plus over 100 associated proteins. It assembles de novo on each intron. The process begins with **U1 snRNP** recognizing the **5' splice site** (nearly always a GU dinucleotide at the intron's start) through base-pairing between U1 snRNA and the pre-mRNA. Meanwhile, **U2 snRNP** binds the **branch point sequence** (a conserved adenosine typically 20–50 nucleotides upstream of the 3' splice site). The remaining snRNPs join as a preassembled U4/U6·U5 tri-snRNP, triggering extensive rearrangements that eject U1 and U4 and form the catalytically active spliceosome.

The chemistry itself consists of two sequential **transesterification** reactions — phosphodiester bond exchanges that require no external energy input. In **step 1**, the 2'-OH of the branch point adenosine attacks the phosphodiester bond at the 5' splice site. This simultaneously frees the upstream exon and creates the distinctive **lariat intermediate**, where the intron's 5' end is linked to the branch point via an unusual 2'-5' phosphodiester bond. In **step 2**, the free 3'-OH of the upstream exon attacks the phosphodiester bond at the 3' splice site (almost always an AG dinucleotide), ligating the two exons and releasing the intron lariat for degradation. The beauty of transesterification is that two bonds are broken and two are formed — the reaction is energetically neutral, requiring only precise positioning by the spliceosome.

The most profound consequence of splicing is **alternative splicing** — the regulated inclusion or exclusion of specific exons to produce different mRNAs from the same gene. A single gene with 10 alternatively spliced exons can theoretically produce over 1,000 distinct mRNA variants, each encoding a protein with different domains, binding properties, or regulatory features. This is how the human genome, with roughly 20,000 protein-coding genes, generates an estimated 80,000–100,000 distinct proteins. Alternative splicing is controlled by **splicing regulatory elements** (enhancers and silencers) within the pre-mRNA and by tissue-specific RNA-binding proteins (such as SR proteins and hnRNPs) that promote or repress particular splice site choices. Mutations that disrupt splice sites or regulatory elements account for an estimated 15–50% of disease-causing mutations in humans, underscoring that splicing fidelity is as important to gene expression as transcriptional accuracy.
