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

## Questions

```yaml
- question: "The human genome contains approximately 20,000 protein-coding genes, yet scientists identify well over 100,000 distinct protein isoforms in human cells. The primary explanation for this discrepancy is:"
  type: multiple-choice
  options:
    - "Widespread gene duplication events that create multiple copies of each gene"
    - "Post-translational modifications that chemically alter proteins after they are made"
    - "Alternative splicing, in which a single pre-mRNA is spliced in multiple ways to produce distinct mRNA and protein sequences"
    - "RNA editing events that change individual nucleotides in mRNA sequences after transcription"
  answer: 2
  explanation: "Alternative splicing is the primary driver of proteomic complexity beyond genome complexity. An estimated 95% of human multi-exon genes undergo alternative splicing, and some genes produce thousands of isoforms — the fruit fly DSCAM gene can generate over 38,000 splice variants from a single gene. Post-translational modifications and RNA editing both contribute to protein diversity, but alternative splicing generates distinct protein sequences (different amino acid chains), not just chemical modifications of a single sequence."

- question: "During spliceosome-mediated intron removal, what is the first chemical event?"
  type: multiple-choice
  options:
    - "The 3' splice site is cleaved, releasing the downstream exon"
    - "The two exons are ligated together by the U5 snRNP"
    - "The 2'-hydroxyl of the branch point adenosine attacks the 5' splice site, forming a lariat structure"
    - "U1 snRNP cleaves the intron at the GU dinucleotide to initiate removal"
  answer: 2
  explanation: "The first transesterification reaction is an attack by the 2'-OH of the branch point adenosine on the phosphodiester bond at the 5' splice site. This simultaneously cleaves the 5' end of the intron from the upstream exon and forms an unusual 2'-5' phosphodiester bond between the intron's 5' end and the branch point, creating the characteristic lariat structure. The second reaction then joins the two exons together and releases the lariat intron. U1 snRNP recognizes the 5' splice site but does not itself perform the cleavage."

- question: "Each protein-coding gene in a eukaryotic cell encodes exactly one protein sequence, produced through a single, fixed splicing pattern."
  type: true-false
  answer: false
  explanation: "Alternative splicing allows single genes to produce multiple distinct protein sequences through selective exon inclusion/skipping, intron retention, and use of alternative 5' or 3' splice sites. Approximately 95% of human multi-exon genes undergo alternative splicing, and this process is regulated in a tissue-specific and developmental stage-specific manner. The same gene can produce an isoform that is expressed in neurons but not liver cells, or during embryonic development but not in adults — dramatically expanding the functional repertoire encoded by the genome."

- question: "The catalytic activity of the spliceosome — the actual chemistry of intron removal — is carried out by RNA components (snRNAs) rather than protein components."
  type: true-false
  answer: true
  explanation: "The spliceosome is a ribozyme-like machine. Through conformational rearrangements during assembly, U6 snRNA (which displaces U1 at the 5' splice site) and U2 snRNA (bound to the branch point) form the catalytic core. Metal ions coordinated by the U6 snRNA facilitate the transesterification chemistry. This RNA-based catalysis is consistent with the RNA world hypothesis — that RNA originally performed catalytic functions now shared with or delegated to proteins — and is analogous to the peptidyl transferase activity of the ribosome, which is also RNA-based."

- question: "Why would a single-nucleotide error at a 5' or 3' splice site be particularly catastrophic for the resulting protein, compared to a point mutation in the middle of an exon?"
  type: short-answer
  answer: "Splice site mutations disrupt the spliceosome's recognition of the intron boundary, causing mis-splicing. If the correct splice site is lost, the spliceosome may skip the nearby exon entirely (losing that coding sequence), retain the intron (inserting non-coding sequence into the mRNA), or activate a nearby cryptic splice site (shifting the exon boundary). Exon skipping and intron retention almost always shift the reading frame by a number of nucleotides not divisible by three, causing a frameshift in all downstream codons — typically producing a premature stop codon and a truncated, nonfunctional protein. A point mutation within an exon may cause a missense substitution affecting one amino acid, which may be tolerable; a splice site mutation affects every single codon downstream of the error."
  explanation: "This explains why many human genetic diseases — including forms of spinal muscular atrophy, Duchenne muscular dystrophy, and beta-thalassemia — are caused by splice site mutations rather than coding sequence mutations. It also drives therapeutic approaches: antisense oligonucleotides can be designed to block cryptic splice sites or restore normal splicing in diseases caused by splice-site mutations, an approach that has produced approved treatments for spinal muscular atrophy."
```

## Explainer

From RNA splicing mechanisms, you know that eukaryotic genes are interrupted by non-coding sequences (introns) that must be removed before the mRNA can be translated. The **spliceosome** is the molecular machine responsible for this precise surgery, and understanding how it works reveals one of the most elegant processes in molecular biology — one where RNA, not protein, performs the catalysis.

The spliceosome assembles step by step on each intron. First, the **U1 snRNP** recognizes the 5' splice site by base-pairing its RNA component with the conserved GU dinucleotide and surrounding sequence at the intron's beginning. Meanwhile, the **branch point sequence** — a conserved adenosine residue located 20–50 nucleotides upstream of the 3' splice site — is recognized by **U2 snRNP**. The U4/U6 and U5 snRNPs then join, forming the complete spliceosome. Through a series of RNA-RNA rearrangements, U6 displaces U1 at the 5' splice site and U4 is released, activating the catalytic core. The chemistry itself consists of two **transesterification reactions**: in the first, the 2'-hydroxyl of the branch point adenosine attacks the 5' splice site, cleaving the RNA and forming a **lariat** — a looped structure where the intron's 5' end is joined to the branch point by an unusual 2'-5' phosphodiester bond. In the second reaction, the freed 3'-hydroxyl of the upstream exon attacks the 3' splice site, ligating the two exons together and releasing the lariat intron for degradation.

What makes this process remarkable is its precision — a single-nucleotide error would shift the reading frame and destroy the protein. The conserved splice site sequences (the **GU-AG rule**) and the branch point provide the primary signals, but they are not sufficient on their own. Additional sequences within exons and introns, called **exonic splicing enhancers (ESEs)** and **intronic splicing enhancers (ISEs)**, recruit SR proteins and other factors that help the spliceosome distinguish true splice sites from the many similar sequences scattered throughout introns. This regulatory layer is what makes **alternative splicing** possible.

**Alternative splicing** is the process by which a single pre-mRNA can be spliced in multiple different ways to produce distinct mature mRNAs — and therefore distinct proteins — from the same gene. Exons can be skipped, introns can be retained, and alternative 5' or 3' splice sites can be selected, all depending on which regulatory proteins are present in a given cell type or developmental stage. The human *DSCAM* gene in fruit flies can generate over 38,000 splice variants — more than twice the number of genes in the entire genome. In humans, an estimated 95% of multi-exon genes undergo alternative splicing. This means that the proteome is vastly larger than the genome, and understanding splicing regulation is essential for understanding how the same genetic information produces hundreds of distinct cell types in a single organism.
