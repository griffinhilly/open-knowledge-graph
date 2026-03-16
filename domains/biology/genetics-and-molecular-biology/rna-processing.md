---
id: rna-processing
title: RNA Processing and Splicing
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: transcription
  type: hard
- id: rna-types-and-structure
  type: hard
builds-toward:
- gene-regulation-eukaryotes
- translation
tags:
- splicing
- introns
- exons
- 5' cap
- poly-A tail
- pre-mRNA
stage: formal-systems
status: validated
---

# RNA Processing and Splicing

## Core Idea
In eukaryotes, the primary RNA transcript (pre-mRNA) undergoes three major processing steps before export to the cytoplasm: addition of a 7-methylguanosine cap at the 5' end, cleavage and polyadenylation at the 3' end, and splicing of introns by the spliceosome. The cap and poly-A tail protect the mRNA from degradation and aid translation initiation. Splicing removes non-coding intron sequences and joins exons; alternative splicing of the same pre-mRNA can produce multiple protein isoforms from a single gene, greatly expanding proteomic diversity.

## How It's Best Learned
Diagram the pre-mRNA and trace each processing event in order. Work through an example of alternative splicing to see how exon inclusion or skipping produces different proteins.

## Common Misconceptions
- Prokaryotes do not perform RNA splicing because their genes lack introns — this is a eukaryote-specific process.
- Introns are not 'junk'; many contain regulatory sequences and non-coding RNA genes.

## Explainer

From your study of transcription, you know that RNA polymerase reads a DNA template and synthesizes an RNA copy. In prokaryotes, that transcript is essentially ready to be translated — ribosomes can even begin translating the mRNA while it is still being transcribed. Eukaryotes, however, insert an entire processing pipeline between transcription and translation. The initial transcript, called **pre-mRNA**, must be modified in three major ways before it can leave the nucleus: capping, polyadenylation, and splicing.

The **5' cap** is a modified guanosine nucleotide (7-methylguanosine) added to the very first nucleotide of the transcript through an unusual 5'-to-5' triphosphate linkage. This cap serves as a molecular passport — it protects the mRNA from exonuclease degradation, signals the ribosome where to begin translation, and helps the mRNA get exported through the nuclear pore. At the other end, the **3' poly-A tail** is added after a specific cleavage event downstream of a polyadenylation signal (typically AAUAAA). An enzyme called poly-A polymerase then adds a string of 100–250 adenine nucleotides. Like the cap, the poly-A tail stabilizes the transcript and aids in translation initiation. Together, these two modifications act like protective bookends.

The most dramatic processing step is **splicing**, in which non-coding sequences called **introns** are removed and the remaining coding sequences, called **exons**, are joined together. This is carried out by the **spliceosome**, a large complex of small nuclear ribonucleoproteins (snRNPs, pronounced "snurps") that recognizes conserved sequences at intron-exon boundaries — the 5' splice site, the branch point, and the 3' splice site. The spliceosome catalyzes two transesterification reactions: first, the 2'-OH of an adenosine at the branch point attacks the 5' splice site, creating a lariat-shaped intermediate; second, the free 3'-OH of the upstream exon attacks the 3' splice site, joining the exons and releasing the intron lariat for degradation.

What makes splicing especially powerful is **alternative splicing** — the ability to include or exclude particular exons in different cell types or developmental stages. A single gene can produce multiple distinct protein isoforms this way. The Drosophila *Dscam* gene, for example, can theoretically generate over 38,000 different mRNA variants from a single gene through combinatorial exon selection. In humans, it is estimated that over 90% of multi-exon genes undergo alternative splicing, which is one reason the human proteome is far more complex than the roughly 20,000 protein-coding genes in the genome would suggest. Splicing regulation involves additional proteins — **SR proteins** that promote exon inclusion and **hnRNPs** that can cause exon skipping — creating a splicing code that rivals transcriptional regulation in its complexity.
