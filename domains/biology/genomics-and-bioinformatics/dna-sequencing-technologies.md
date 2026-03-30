---
id: dna-sequencing-technologies
title: DNA Sequencing Technologies
domain: biology
course: genomics-and-bioinformatics
prerequisites:
- id: dna-structure
  type: hard
- id: dna-replication
  type: hard
- id: pcr
  type: soft
- id: gel-electrophoresis
  type: soft
builds-toward:
- genome-assembly
- rna-seq-analysis-pipeline
- long-read-sequencing
- variant-calling-and-gwas
tags:
- Sanger-sequencing
- next-generation-sequencing
- Illumina
- sequencing-by-synthesis
- read-length
stage: advanced
status: validated
---
# DNA Sequencing Technologies

## Core Idea
DNA sequencing determines the precise order of nucleotides in a DNA molecule. Sanger sequencing (1977) uses chain-terminating dideoxynucleotides to produce fragments of every possible length, separated by size to read the sequence. Next-generation sequencing (NGS) platforms like Illumina massively parallelize sequencing-by-synthesis, generating millions to billions of short reads (75-300 bp) simultaneously at dramatically lower cost per base. Each technology involves tradeoffs between read length, accuracy, throughput, and cost that determine its suitability for different applications.

## How It's Best Learned
Trace through the Sanger method manually: draw a template strand, show how ddNTPs terminate chains at every position, and reconstruct the sequence from the resulting ladder. Then compare the conceptual workflow to Illumina sequencing-by-synthesis, noting what changed (parallelization, detection method) and what stayed the same (complementary strand synthesis with modified nucleotides).

## Common Misconceptions
- Sanger sequencing is not obsolete — it remains the gold standard for validating individual sequences and is widely used for targeted sequencing of single genes.
- Higher throughput does not mean better for every application; Sanger's long reads (~800 bp) and high per-read accuracy make it preferable when sequencing a single amplicon.

## Questions

```yaml
- question: "What is the fundamental principle that allows Sanger sequencing to determine DNA sequence?"
  type: multiple-choice
  options: ["Hybridization of labeled probes to the target sequence", "Random fragmentation followed by mass spectrometry", "Chain termination by dideoxynucleotides producing fragments of every possible length", "Repeated cycles of denaturation, annealing, and extension"]
  answer: 2
  explanation: "Sanger sequencing works by including dideoxynucleotides (ddNTPs) in the synthesis reaction. When a ddNTP is incorporated instead of a normal dNTP, the chain terminates because ddNTPs lack the 3'-OH group needed for the next phosphodiester bond. By running the reaction with all four ddNTPs (each labeled with a different fluorescent dye), fragments terminating at every position are produced. Separating these fragments by size (capillary electrophoresis) and reading the fluorescent labels from smallest to largest gives the sequence."

- question: "Illumina sequencing generates reads that are typically 10,000-50,000 base pairs long."
  type: true-false
  answer: false
  explanation: "Illumina reads are short, typically 75-300 base pairs depending on the platform and protocol. The strength of Illumina sequencing is not read length but massive parallelism — generating hundreds of millions to billions of reads simultaneously, producing terabases of data per run at very low cost per base. Long reads (10,000+ bp) are the domain of third-generation platforms like PacBio and Oxford Nanopore, which are covered in the long-read sequencing topic."

- question: "Explain why the transition from Sanger to next-generation sequencing enabled whole-genome sequencing to become routine."
  type: short-answer
  answer: "Sanger sequencing processes one fragment at a time through capillary electrophoresis, limiting throughput to roughly 1,000 reads per instrument per day. Sequencing a human genome required years and billions of dollars. NGS platforms parallelize the process by performing millions of sequencing reactions simultaneously on a flow cell surface, increasing throughput by orders of magnitude while reducing per-base cost by roughly a million-fold. A human genome that took 13 years and $3 billion with Sanger can now be sequenced in days for under $1,000."
  explanation: "The key innovation was not a fundamentally different chemistry but massive parallelization. Illumina's sequencing-by-synthesis still relies on polymerase-mediated nucleotide incorporation and fluorescent detection, but it does so for billions of clusters simultaneously rather than one capillary at a time. This throughput revolution enabled routine genome sequencing, transcriptomics, epigenomics, and metagenomics."
```

## Explainer

DNA sequencing is the enabling technology of modern genomics — virtually every topic in this course depends on it. Understanding the principles, capabilities, and limitations of sequencing technologies is essential for designing experiments, interpreting data, and appreciating why certain computational challenges exist.

**Sanger sequencing** (also called chain-termination sequencing) was developed by Frederick Sanger in 1977 and dominated for nearly three decades. The method exploits modified nucleotides — dideoxynucleotides (ddNTPs) — that lack the 3'-hydroxyl group required for chain elongation. When a DNA polymerase incorporates a ddNTP instead of a normal dNTP, synthesis terminates at that position. By running the reaction with a mixture of normal dNTPs and a small proportion of fluorescently labeled ddNTPs, the polymerase produces fragments that terminate at every possible position in the template. Capillary electrophoresis separates these fragments by size, and a laser reads the fluorescent label on each fragment as it passes the detector. Reading the colors from smallest to largest fragment gives the sequence. Sanger reads are long (~800 bp) and highly accurate (99.99%), but throughput is limited to one read per capillary.

**Next-generation sequencing (NGS)**, exemplified by Illumina's platform, achieved a throughput revolution by parallelizing sequencing-by-synthesis across millions of clusters on a glass flow cell. The workflow begins by fragmenting the DNA, ligating adapters, and amplifying fragments on the flow cell surface to form clusters of identical molecules. Sequencing proceeds by adding fluorescently labeled reversible terminators — modified nucleotides that allow incorporation of exactly one base per cycle, followed by imaging to identify which base was added, then chemical removal of the terminator to allow the next cycle. After 75-300 cycles, each cluster has produced one read. Because millions of clusters are sequenced simultaneously, a single Illumina run can generate hundreds of gigabases of data.

The choice of sequencing technology depends on the application. Sanger remains preferred for validating specific mutations, sequencing single genes, and applications where per-read accuracy matters more than throughput. Illumina dominates for whole-genome sequencing, RNA-seq, ChIP-seq, and any application requiring deep, cost-effective coverage. The short read lengths of Illumina (75-300 bp) create challenges for genome assembly in repetitive regions and for resolving structural variants, which motivated the development of third-generation long-read technologies. Each technology's strengths and limitations propagate directly into the computational methods used to analyze its output.
