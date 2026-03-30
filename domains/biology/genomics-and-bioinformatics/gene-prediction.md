---
id: gene-prediction
title: Gene Prediction and Annotation
domain: biology
course: genomics-and-bioinformatics
prerequisites:
- id: genome-structure-and-organization
  type: hard
- id: transcription
  type: hard
- id: translation
  type: hard
- id: rna-processing
  type: soft
- id: pairwise-sequence-alignment
  type: soft
builds-toward:
- functional-annotation
- rna-seq-analysis-pipeline
tags:
- gene-finding
- ORF
- ab-initio
- hidden-markov-model
- gene-annotation
stage: advanced
status: validated
---
# Gene Prediction and Annotation

## Core Idea
Gene prediction identifies the locations and structures of genes within a genome sequence. Ab initio methods use statistical models (often hidden Markov models) trained on known gene features — start codons, splice sites, codon usage bias, and stop codons — to predict genes from sequence alone. Evidence-based methods use experimental data (ESTs, RNA-seq, protein alignments) to confirm or refine predictions. Modern annotation pipelines combine both approaches, integrating computational predictions with transcript evidence and cross-species homology to produce high-confidence gene models.

## How It's Best Learned
Take a 100-kb unannotated bacterial sequence and find open reading frames using simple criteria (start codon, no internal stop, length threshold). Then try the same on a eukaryotic sequence and observe how introns make simple ORF-finding fail. Compare your manual predictions against an automated pipeline's output.

## Common Misconceptions
- Finding an open reading frame does not mean you have found a gene — many ORFs occur by chance, especially short ones.
- Gene prediction in prokaryotes is far easier than in eukaryotes because prokaryotic genes lack introns and have simpler regulatory structures.

## Questions

```yaml
- question: "Why is gene prediction significantly more difficult in eukaryotic genomes compared to prokaryotic genomes?"
  type: multiple-choice
  options: ["Eukaryotic genomes are always larger", "Eukaryotic genes contain introns that interrupt coding sequences, requiring splice site prediction", "Eukaryotic organisms have more genes", "Eukaryotic DNA uses different base pairs"]
  answer: 1
  explanation: "The primary difficulty is introns. Prokaryotic genes are contiguous — an ORF search reliably identifies them. Eukaryotic genes are split into exons and introns, so the coding sequence is fragmented across the genomic DNA. The gene predictor must identify each exon boundary (splice donor and acceptor sites), assemble the correct combination of exons, and distinguish real splice sites from the many sequences that resemble them. Alternative splicing adds further complexity."

- question: "An ab initio gene predictor uses only the DNA sequence and statistical models to predict genes, without any experimental evidence."
  type: true-false
  answer: true
  explanation: "Ab initio (from the beginning) gene predictors rely entirely on sequence features and statistical models — typically hidden Markov models trained on known genes from the same or related species. They recognize patterns like codon usage bias, splice site consensus sequences, promoter elements, and polyadenylation signals. While powerful, they are less accurate than evidence-based methods that incorporate RNA-seq data or protein alignments, which is why modern pipelines combine both approaches."

- question: "Explain why RNA-seq data is particularly valuable for refining eukaryotic gene predictions."
  type: short-answer
  answer: "RNA-seq captures the actual transcripts produced by cells, directly revealing which regions of the genome are transcribed and how exons are spliced together. Reads that span exon-exon junctions provide definitive evidence for intron locations and alternative splicing patterns. This experimental evidence resolves ambiguities that ab initio methods cannot — such as which of several possible splice sites is actually used, whether a predicted gene is truly expressed, and the full diversity of transcript isoforms."
  explanation: "Before RNA-seq, gene annotation relied heavily on ESTs (expressed sequence tags) and cDNA libraries, which had limited coverage and tissue representation. RNA-seq provides comprehensive, quantitative, tissue-specific transcript evidence that has dramatically improved annotation quality in every genome where it has been applied."
```

## Explainer

A newly assembled genome is essentially a very long string of A, T, G, and C. The immediate question is: where are the genes? Gene prediction — also called gene finding or genome annotation — is the process of identifying the positions, boundaries, and structures of all genes in a genome sequence. The approaches and difficulty vary enormously between prokaryotes and eukaryotes.

In **prokaryotes**, gene prediction is relatively straightforward. Genes are contiguous (no introns), tightly packed, and account for 85-95% of the genome. An open reading frame (ORF) — a stretch of DNA from a start codon (ATG) to an in-frame stop codon (TAA, TAG, TGA) — that exceeds a length threshold (typically ~300 bp) is very likely a real gene. Tools like Prodigal and Glimmer use additional signals like ribosome binding sites (Shine-Dalgarno sequences) and codon usage statistics to distinguish real genes from chance ORFs with high accuracy, typically predicting 95-99% of genes correctly.

**Eukaryotic** gene prediction is fundamentally harder. Genes are split into exons and introns, so the coding sequence is scattered across genomic DNA. A human gene might span 50 kb of DNA but produce an mRNA of only 2 kb after splicing. The predictor must identify each exon, correctly call the splice donor (GT) and acceptor (AG) sites at intron boundaries, and assemble the right combination of exons — all while dealing with the fact that GT and AG dinucleotides occur frequently by chance. Ab initio methods like Augustus and GeneMark use hidden Markov models (HMMs) that model the statistical properties of exons, introns, intergenic regions, and splice sites to find the most probable gene structure. But accuracy from sequence alone is limited, especially for short exons, long introns, and genes with non-canonical features.

Modern genome annotation therefore combines multiple lines of evidence. RNA-seq data shows exactly which parts of the genome are transcribed and, through junction-spanning reads, how exons are spliced. Protein alignments from related species identify conserved coding regions. Known protein domains (from databases like Pfam) flag functional elements. Pipelines like MAKER and BRAKER integrate ab initio predictions with all available evidence, scoring each gene model by the amount of supporting data. The result is not a single answer but a ranked set of gene models with confidence levels — reflecting the reality that gene annotation is an ongoing refinement process that improves as more evidence accumulates.
