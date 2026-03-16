---
id: alternative-splicing-mechanisms
title: Alternative Splicing and Protein Diversity
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: rna-splicing-mechanisms
  type: hard
- id: spliceosome-and-splicing-regulation
  type: hard
builds-toward:
- microrna-biogenesis-and-function
tags:
- post-transcriptional-regulation
- exon-skipping
- protein-isoforms
- gene-expression-diversity
stage: formal-systems
status: draft
---

# Alternative Splicing and Protein Diversity

## Core Idea
Alternative splicing allows a single gene to produce multiple mRNA variants and proteins by including or excluding different exons or using alternative splice sites. Humans use alternative splicing in ~95% of multi-exon genes, generating >100,000 different proteins from only ~20,000 genes. Defects in splicing regulation are implicated in many cancers and genetic diseases.

## How It's Best Learned
Study examples like immunoglobulin genes, where exon choice directly impacts protein function. Use visualization tools to see how different splice variants affect protein domain structure.

## Common Misconceptions
- Assuming each gene produces one protein (one gene → one protein paradigm is outdated).
- Thinking all introns are removed equally (splice site strength and regulatory proteins determine inclusion).
- Confusing alternative splicing with RNA editing.

## Explainer

From your study of RNA splicing, you know that introns are removed from pre-mRNA and exons are joined together by the spliceosome. In constitutive splicing, the same exons are always joined in the same order. **Alternative splicing** breaks this rule: the spliceosome can be directed to include or exclude specific exons, use alternative 5' or 3' splice sites within an exon, or even retain an intron — producing different mature mRNAs from the same gene. The result is that one gene can encode multiple distinct proteins, called **isoforms**, each with different functional properties.

There are several major patterns of alternative splicing. In **exon skipping** (the most common type in mammals), an entire exon is either included or left out. In **alternative 5' or 3' splice site selection**, the spliceosome chooses a different boundary within an exon, making it longer or shorter. In **intron retention**, an intron remains in the mature mRNA, often introducing a premature stop codon that truncates the protein. And in **mutually exclusive exons**, one of two or more exons is always included, but never more than one at a time. The Drosophila *Dscam* gene pushes this to an extreme — it can produce over 38,000 different mRNA variants through combinations of mutually exclusive exon choices, far more proteins than the fly has genes.

What determines which splice variant is produced? The answer lies in **splicing regulatory proteins** that bind to short sequence motifs in the pre-mRNA. **SR proteins** (serine/arginine-rich proteins) generally promote exon inclusion by binding to exonic splicing enhancers (ESEs), while **hnRNP proteins** typically promote exon skipping by binding to exonic or intronic splicing silencers. The balance between these activators and repressors varies by cell type, developmental stage, and physiological state, which is how different tissues produce different protein isoforms from the same gene. Neurons, for example, express splicing regulators that produce neuron-specific isoforms of many widely expressed genes.

Alternative splicing explains one of the great puzzles of genome biology: how humans, with roughly 20,000 protein-coding genes — not many more than a roundworm — generate the molecular complexity needed to build a brain, an immune system, and hundreds of specialized cell types. The answer is that the proteome is far larger than the genome. Immunoglobulin genes use alternative splicing to switch between membrane-bound and secreted forms of antibodies. The *calcitonin/CGRP* gene produces a hormone in thyroid cells but a neuropeptide in neurons, entirely through tissue-specific splicing. When splicing goes wrong — through mutations in splice sites, regulatory sequences, or the splicing machinery itself — the consequences can be severe, contributing to diseases from spinal muscular atrophy to certain cancers.
