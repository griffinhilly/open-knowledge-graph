---
id: intron-removal-and-splicing
title: Intron Splicing and Alternative Splicing
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: rna-splicing-mechanisms
  type: hard
- id: gene-expression-overview
  type: soft
builds-toward:
- translation-initiation-start-codon
- small-rnas-mirna-and-rnai
tags:
- spliceosome
- transesterification
- lariat
- alternative-splicing
stage: formal-systems
status: draft
---

# Intron Splicing and Alternative Splicing

## Core Idea
Introns are removed from pre-mRNA by the spliceosome, a large ribonucleoprotein complex containing five snRNPs (U1, U2, U4, U5, U6) and >100 proteins. The spliceosome recognizes conserved sequences at intron boundaries (typically GU at the 5' splice site and AG at the 3' splice site, the 'GU-AG rule') and catalyzes two sequential transesterification reactions: the first cleaves the 5' splice site, forming a lariat structure, and the second ligates exons while releasing the intron. Alternative splicing allows a single gene to produce multiple protein variants through selective inclusion or exclusion of exons, greatly increasing proteomic diversity and enabling tissue-specific or developmental stage-specific protein isoforms.

## Explainer

From RNA splicing mechanisms, you know that eukaryotic genes are interrupted by non-coding sequences (introns) that must be removed before the mRNA can be translated. The **spliceosome** is the molecular machine responsible for this precise surgery, and understanding how it works reveals one of the most elegant processes in molecular biology — one where RNA, not protein, performs the catalysis.

The spliceosome assembles step by step on each intron. First, the **U1 snRNP** recognizes the 5' splice site by base-pairing its RNA component with the conserved GU dinucleotide and surrounding sequence at the intron's beginning. Meanwhile, the **branch point sequence** — a conserved adenosine residue located 20–50 nucleotides upstream of the 3' splice site — is recognized by **U2 snRNP**. The U4/U6 and U5 snRNPs then join, forming the complete spliceosome. Through a series of RNA-RNA rearrangements, U6 displaces U1 at the 5' splice site and U4 is released, activating the catalytic core. The chemistry itself consists of two **transesterification reactions**: in the first, the 2'-hydroxyl of the branch point adenosine attacks the 5' splice site, cleaving the RNA and forming a **lariat** — a looped structure where the intron's 5' end is joined to the branch point by an unusual 2'-5' phosphodiester bond. In the second reaction, the freed 3'-hydroxyl of the upstream exon attacks the 3' splice site, ligating the two exons together and releasing the lariat intron for degradation.

What makes this process remarkable is its precision — a single-nucleotide error would shift the reading frame and destroy the protein. The conserved splice site sequences (the **GU-AG rule**) and the branch point provide the primary signals, but they are not sufficient on their own. Additional sequences within exons and introns, called **exonic splicing enhancers (ESEs)** and **intronic splicing enhancers (ISEs)**, recruit SR proteins and other factors that help the spliceosome distinguish true splice sites from the many similar sequences scattered throughout introns. This regulatory layer is what makes **alternative splicing** possible.

**Alternative splicing** is the process by which a single pre-mRNA can be spliced in multiple different ways to produce distinct mature mRNAs — and therefore distinct proteins — from the same gene. Exons can be skipped, introns can be retained, and alternative 5' or 3' splice sites can be selected, all depending on which regulatory proteins are present in a given cell type or developmental stage. The human *DSCAM* gene in fruit flies can generate over 38,000 splice variants — more than twice the number of genes in the entire genome. In humans, an estimated 95% of multi-exon genes undergo alternative splicing. This means that the proteome is vastly larger than the genome, and understanding splicing regulation is essential for understanding how the same genetic information produces hundreds of distinct cell types in a single organism.
