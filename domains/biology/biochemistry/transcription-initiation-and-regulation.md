---
id: transcription-initiation-and-regulation
title: Transcription Initiation and Gene Regulation
domain: biology
course: biochemistry
prerequisites:
- id: transcription
  type: hard
- id: nucleotide-synthesis
  type: soft
builds-toward:
- rna-splicing-mechanisms
- gene-regulation-eukaryotes
tags:
- transcription
- promoter
- transcription factors
- chromatin
- histone acetylation
stage: advanced
status: draft
---

# Transcription Initiation and Gene Regulation

## Core Idea
In eukaryotes, transcription of protein-coding genes is initiated by RNA Polymerase II in response to transcription factor binding at promoter elements (TATA box, CAAT box, GC box) and enhancers. Chromatin structure, mediated by histones and nucleosomes, suppresses transcription through repressive marks (H3K27me3) and activates transcription through permissive marks (H3K4me3, H3K9ac). The Mediator complex bridges transcription factors to RNA Pol II. Transcription is dynamic and subject to regulation at multiple levels: chromatin remodeling, transcription factor availability, and RNA Pol II pausing and elongation control.

## Explainer

From your understanding of basic transcription, you know that RNA polymerase reads a DNA template to synthesize RNA. But in eukaryotes, transcription initiation is not as simple as the polymerase finding a gene and starting. Eukaryotic DNA is wrapped around histone proteins into **nucleosomes**, which compact the genome but also physically block RNA polymerase from accessing most genes. The central question of gene regulation is: how does the cell decide which genes to unwrap and transcribe, and when?

The answer begins at the **promoter**, a DNA sequence upstream of the gene's transcription start site. The best-known promoter element is the **TATA box** (consensus TATAAA, located ~25–30 base pairs upstream), which is recognized by **TATA-binding protein (TBP)**, a subunit of the general transcription factor TFIID. TBP binding bends the DNA sharply, creating a platform for the sequential assembly of TFIIA, TFIIB, TFIIF (which escorts RNA Pol II to the promoter), TFIIE, and TFIIH. This assembly — the **pre-initiation complex (PIC)** — is necessary but not sufficient for robust transcription. TFIIH has helicase activity that unwinds ~11 base pairs of DNA to form the transcription bubble, and its kinase subunit phosphorylates the **C-terminal domain (CTD)** of RNA Pol II, triggering the transition from initiation to elongation.

But the PIC alone produces only low-level (basal) transcription. To achieve the thousand-fold differences in gene expression that distinguish a liver cell from a neuron, cells use **transcription factors** that bind **enhancer** sequences — regulatory DNA elements that can sit tens or even hundreds of kilobases away from the promoter. Enhancer-bound activators communicate with the PIC through the **Mediator complex**, a large multi-subunit assembly that acts as a molecular bridge. Activators recruit Mediator, which in turn stabilizes the PIC and stimulates RNA Pol II activity. Conversely, repressors recruit corepressor complexes that block Mediator interaction or actively silence the gene.

Layered on top of this is **chromatin regulation**. Histones carry chemical modifications on their N-terminal tails — acetylation, methylation, phosphorylation — that either open or close chromatin. **Histone acetylation** (e.g., H3K9ac, H3K27ac), catalyzed by histone acetyltransferases (HATs) recruited by activators, neutralizes the positive charge on lysine residues, loosening the histone-DNA interaction and making the promoter accessible. **Histone methylation** can be activating (H3K4me3 at active promoters) or repressive (H3K27me3, deposited by Polycomb complexes to silence developmental genes). ATP-dependent **chromatin remodeling complexes** like SWI/SNF physically slide or eject nucleosomes from promoters. The combinatorial pattern of histone marks — sometimes called the "histone code" — determines whether a given stretch of DNA is poised for transcription, actively transcribed, or stably silenced. This multi-layered system — promoter elements, transcription factors, Mediator, and chromatin state — gives eukaryotic cells extraordinarily precise control over which genes are expressed in which cell types and at what levels.
