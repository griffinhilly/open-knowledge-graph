---
id: next-generation-sequencing-ngs
title: Next Generation Sequencing Technologies and Platforms
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: pcr
  type: hard
- id: genomics-overview
  type: hard
builds-toward:
- variant-annotation-interpretation
tags:
- ngs
- next-generation-sequencing
- illumina
- dna-sequencing
- high-throughput-sequencing
stage: formal-systems
status: draft
---

# Next Generation Sequencing Technologies and Platforms

## Core Idea
Next-generation sequencing (NGS) technologies sequence millions of DNA fragments in parallel, vastly outpacing Sanger sequencing in throughput and cost. Illumina sequencing uses reversible terminator chemistry, Ion Torrent uses semiconductor sensing of pH changes, and long-read technologies (PacBio, Oxford Nanopore) sequence 10-100 kb fragments. NGS enables whole-genome/exome sequencing, RNA-seq, ChIP-seq, and targeted variant detection, revolutionizing genomics and diagnostics.

## Explainer

From your knowledge of PCR and genomics, you understand that DNA can be amplified in vitro and that genomes contain vast amounts of information encoded in nucleotide sequences. The challenge that **next-generation sequencing** (NGS) solves is reading that information at massive scale. Sanger sequencing, the gold standard for decades, reads one fragment at a time and tops out at about 96 reactions per run. NGS platforms read millions to billions of fragments simultaneously, dropping the cost of sequencing a human genome from roughly $100 million (in 2001) to under $1,000.

The most widely used NGS platform, **Illumina sequencing**, works through a method called sequencing by synthesis. First, genomic DNA is fragmented into short pieces (typically 150–300 bp), and short adapter sequences are ligated to both ends. These adapted fragments are washed across a glass slide (flow cell) coated with complementary oligonucleotides, where each fragment binds and is amplified into a tight cluster of identical copies through **bridge amplification** — a localized PCR-like process on the surface. Each cluster contains roughly 1,000 identical copies of one original fragment, providing enough signal to detect. During sequencing, fluorescently labeled nucleotides with reversible terminators are added one at a time. After each incorporation, a camera photographs the entire flow cell, recording which base was added at each cluster. The terminator is then chemically removed, and the next cycle begins. Over hundreds of cycles, the sequence of each cluster is read out base by base.

Other platforms take different approaches. **Ion Torrent** detects the hydrogen ion released each time a nucleotide is incorporated, using a semiconductor chip — essentially a miniaturized pH meter for each well. It is fast and inexpensive but less accurate for homopolymer stretches (runs of the same base). **Long-read technologies** address a fundamental limitation of short-read platforms: when reads are only 150 bp, assembling them into a complete genome is like reconstructing a book from confetti. **PacBio** (Single Molecule Real-Time) watches a single polymerase incorporate fluorescent nucleotides in real time through a tiny well called a zero-mode waveguide, producing reads of 10–25 kb. **Oxford Nanopore** threads single-stranded DNA through a protein pore embedded in a membrane, measuring changes in electrical current as each base passes through, yielding reads that can exceed 100 kb.

The downstream applications of NGS extend far beyond simply reading a genome. **Whole-exome sequencing** targets only the protein-coding regions (~1.5% of the genome), making clinical variant detection affordable. **RNA-seq** sequences the transcriptome, revealing which genes are active and at what levels in a given tissue or condition. **ChIP-seq** identifies where proteins bind across the genome by immunoprecipitating protein-DNA complexes before sequencing. In each case, the raw output is millions of short sequence reads that must be computationally aligned to a reference genome and analyzed for variants, expression levels, or binding peaks. The shift from "one gene at a time" to "all genes at once" has made NGS the central technology platform of modern genomics, clinical genetics, and molecular biology research.
