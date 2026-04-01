---
id: genome-assembly
title: Genome Assembly
domain: biology
course: genomics-and-bioinformatics
prerequisites:
- id: dna-sequencing-technologies
  type: hard
- id: genome-structure-and-organization
  type: hard
builds-toward:
- comparative-genomics
- metagenomics
- long-read-sequencing
tags:
- de-novo-assembly
- reference-guided
- contigs
- scaffolds
- de-Bruijn-graph
- N50
stage: advanced
status: validated
---
# Genome Assembly

## Core Idea
Genome assembly reconstructs a complete genome sequence from millions of short sequencing reads. De novo assembly builds the genome without a reference, typically using overlap-layout-consensus (for long reads) or de Bruijn graph approaches (for short reads). Reference-guided assembly maps reads to an existing reference genome. Assembly quality is measured by metrics like N50 (the contig length at which half the assembly is in contigs of that length or longer), total assembly size, and completeness (e.g., BUSCO scores). Repetitive sequences are the primary obstacle, creating ambiguities that fragment the assembly.

## How It's Best Learned
Assemble a small bacterial genome (~5 Mb) from simulated Illumina reads using SPAdes. Examine the output: count contigs, compute N50, and identify where the assembly broke — typically at repetitive elements. Then compare to an assembly of the same genome using long reads.

## Common Misconceptions
- Assembly does not produce one continuous sequence per chromosome; most assemblies consist of hundreds to thousands of contigs with gaps.
- Higher sequencing depth does not always improve assembly; after a certain point, additional reads add diminishing returns and more computational cost.

## Questions

```yaml
- question: "What does an N50 value of 50 kb mean for a genome assembly?"
  type: multiple-choice
  options: ["The assembly contains exactly 50 contigs", "50% of the reads are longer than 50 kb", "Half of the total assembled sequence is contained in contigs of 50 kb or longer", "The average contig length is 50 kb"]
  answer: 2
  explanation: "N50 is calculated by sorting contigs from longest to shortest and summing their lengths until the cumulative sum reaches 50% of the total assembly size. The length of the contig that crosses the 50% threshold is the N50. An N50 of 50 kb means that contigs of 50 kb or longer collectively account for at least half the assembly. It is a measure of contiguity, not count or average."

- question: "Repetitive sequences longer than the sequencing read length do not pose any special challenge for genome assembly."
  type: true-false
  answer: false
  explanation: "Repeats longer than the read length are the primary challenge in genome assembly. When a read falls entirely within a repeat, it is identical (or nearly so) to reads from other copies of the same repeat elsewhere in the genome. The assembler cannot determine which genomic location the read came from, leading to collapsed repeats (multiple copies assembled as one), misjoins, or breaks in the assembly at repeat boundaries. This is why long-read technologies, which can span entire repeat elements, dramatically improve assembly contiguity."

- question: "Explain the difference between de novo assembly and reference-guided assembly, and when you would choose each approach."
  type: short-answer
  answer: "De novo assembly reconstructs the genome from reads alone, without using any existing reference sequence. It is necessary when no closely related reference exists (novel organisms, highly divergent strains) and when you want to detect structural variants, novel sequences, or rearrangements that a reference would miss. Reference-guided assembly maps reads to an existing reference genome and calls variants relative to it. It is faster, less computationally demanding, and appropriate when a high-quality reference from a closely related organism is available and the goal is to identify variants rather than discover novel genomic content."
  explanation: "In practice, many projects use both: reference-guided assembly for variant calling and a de novo assembly to capture sequences absent from the reference. The human genome reference (GRCh38) is the backbone of most human genomics, but de novo assembly of individual genomes has revealed substantial structural variation missed by reference-guided approaches."
```

## Explainer

Sequencing technologies produce reads — short stretches of determined sequence, typically 150-300 bp for Illumina or 10,000-100,000+ bp for long-read platforms. A human genome is 3.2 billion base pairs. Assembly is the computational process of piecing millions of overlapping reads back together into the original genome sequence, like solving a jigsaw puzzle with billions of pieces, many of which look identical.

For **short-read assembly**, the dominant approach uses **de Bruijn graphs**. The algorithm breaks each read into overlapping k-mers (subsequences of length k, typically 21-127 bp), builds a graph where each k-mer is a node and overlapping k-mers are connected by edges, then finds paths through the graph that represent the original sequences. The advantage over simple overlap-based methods is computational efficiency — building pairwise overlaps for billions of reads is prohibitively expensive, while k-mer graph construction is linear in the number of reads. Tools like SPAdes, MEGAHIT, and Velvet use this approach with various refinements.

For **long-read assembly**, overlap-layout-consensus (OLC) methods are more natural. Because long reads span repetitive regions, the overlap graph is less tangled, and the assembler can resolve structures that short reads cannot. Tools like Canu, Hifiasm, and Flye are designed for long reads. The tradeoff is that long reads historically had higher error rates (5-15% for PacBio CLR, 5-10% for Oxford Nanopore), requiring consensus correction. Modern PacBio HiFi reads achieve 99.9% accuracy at 15-20 kb lengths, combining the advantages of both worlds.

Assembly quality is assessed by multiple metrics. **N50** measures contiguity — a higher N50 means longer unbroken sequences. **BUSCO** (Benchmarking Universal Single-Copy Orthologs) checks whether expected conserved genes are present and complete, measuring biological completeness rather than just contiguity. Total assembly size should approximate the expected genome size. The gap between a fragmented draft assembly (thousands of contigs) and a finished, chromosome-level assembly is enormous, and closing that gap typically requires combining multiple data types: short reads for base accuracy, long reads for contiguity, and scaffolding technologies (Hi-C, optical mapping) to order and orient contigs into chromosome-scale sequences.
