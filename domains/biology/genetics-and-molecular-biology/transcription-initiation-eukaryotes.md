---
id: transcription-initiation-eukaryotes
title: 'Eukaryotic Transcription Initiation: TFIID, Mediator, and Chromatin'
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: transcription
  type: hard
- id: gene-regulation-eukaryotes
  type: hard
- id: chromatin-remodeling-accessibility
  type: soft
- id: transcription-initiation-and-regulation
  type: soft
builds-toward:
- rna-polymerase-ii-and-ctd-regulation
- transcription-factors-and-gene-regulation
tags:
- tfiid
- tata-box
- initiator-elements
- mediator-complex
- chromatin-accessibility
stage: formal-systems
status: draft
---

# Eukaryotic Transcription Initiation: TFIID, Mediator, and Chromatin

## Core Idea
Eukaryotic transcription initiation is substantially more complex than prokaryotic, involving multiple general transcription factors (TFIID, TFIIB, TFIIE, TFIIF, TFIIH) that recognize core promoter elements including the TATA box (consensus TATAAA ~25 nucleotides upstream) and Initiator elements. Chromatin accessibility is a prerequisite—nucleosomes must be remodeled or displaced by chromatin remodeling complexes to expose the promoter. The Mediator complex, a large multiprotein complex, bridges enhancer-bound transcription factors and the RNA polymerase II preinitiation complex, enabling long-range transcriptional regulation across genomic distances. This architectural complexity allows precise developmental and environmental control of gene expression.

## Explainer

In prokaryotes, transcription initiation is relatively straightforward: a single sigma factor recognizes the promoter, and RNA polymerase binds and begins transcribing. Eukaryotic transcription initiation is fundamentally different in scale and complexity, requiring a large ensemble of proteins to assemble at the promoter before RNA polymerase II can begin work. Understanding why requires remembering what you learned about eukaryotic gene regulation and chromatin structure — the DNA is not naked and freely accessible but is wrapped around histones and packaged into chromatin.

The first barrier to transcription is **chromatin accessibility**. Before any transcription factor can reach the DNA, the nucleosomes occluding the promoter region must be moved or modified. **Chromatin remodeling complexes** (ATP-dependent machines like SWI/SNF) physically slide or eject nucleosomes, while histone-modifying enzymes add chemical marks (acetylation, methylation) that either loosen chromatin or recruit additional regulatory proteins. This is why chromatin state acts as a gatekeeper — a gene buried in tightly packed heterochromatin simply cannot be transcribed, regardless of what transcription factors are present in the cell.

Once the promoter is accessible, the **preinitiation complex (PIC)** assembles in an ordered sequence. The process typically begins with **TFIID**, a multi-subunit complex whose TBP (TATA-binding protein) subunit recognizes the **TATA box** — a conserved AT-rich sequence located about 25 base pairs upstream of the transcription start site. TBP binds the minor groove and bends the DNA sharply, creating a platform for subsequent factors. TFIID also contains **TAFs** (TBP-associated factors) that recognize other core promoter elements like the **Initiator (Inr)** element at the start site and downstream promoter elements. After TFIID binds, **TFIIB** joins and positions the polymerase, followed by **TFIIF** (which escorts RNA Pol II to the promoter), and then **TFIIE** and **TFIIH**. TFIIH is particularly important: its helicase activity melts the DNA double strand to form the transcription bubble, and its kinase activity phosphorylates the **C-terminal domain (CTD)** of RNA Pol II, triggering the transition from initiation to elongation.

The **Mediator complex** is the final critical piece and the key to understanding how eukaryotes achieve precise gene regulation. Mediator is a massive (~30-subunit) complex that acts as a molecular bridge between gene-specific **transcription factors** bound at distant enhancer elements and the general transcription machinery assembled at the core promoter. Enhancers can be located tens or hundreds of kilobases away from the promoter they regulate; DNA looping brings them into physical proximity with the promoter, and Mediator transmits the activating or repressing signals from enhancer-bound factors to the PIC. This architecture means that the decision to transcribe a gene integrates multiple inputs — developmental signals, environmental cues, chromatin state — all converging through Mediator onto the core machinery. The result is a system where a single gene can be regulated by dozens of enhancers and transcription factors, enabling the exquisite cell-type-specific expression patterns that define eukaryotic development.
