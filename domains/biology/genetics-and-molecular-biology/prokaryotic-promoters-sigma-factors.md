---
id: prokaryotic-promoters-sigma-factors
title: Prokaryotic Promoters and Sigma Factors
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: gene-regulation-prokaryotes
  type: soft
- id: transcription
  type: soft
builds-toward:
- eukaryotic-promoters-tfiid-complex
- transcription-factors-binding-domains
tags:
- transcription
- prokaryotes
- promoters
- gene-regulation
stage: formal-systems
status: draft
---

# Prokaryotic Promoters and Sigma Factors

## Core Idea
Prokaryotic promoters contain conserved -10 (Pribnow) and -35 boxes recognized by RNA polymerase bound to a sigma factor. Different sigma factors (e.g., sigma-70, sigma-32) recognize different promoter sequences, allowing bacteria to switch gene expression in response to environmental stress. Sigma factor determines promoter specificity and initiates transcription.

## How It's Best Learned
Align prokaryotic promoter sequences and identify consensus motifs at -10 and -35 positions. Understand how sigma factor binds core polymerase and changes the specificity from non-specific (core alone) to specific (holoenzyme). Consider how alternative sigma factors activate stress-response genes.

## Common Misconceptions
- Assuming all bacterial promoters have equally strong -10 and -35 boxes.
- Not recognizing that sigma factor dissociates after transcription initiation, returning core polymerase to the pool.
- Confusing sigma factors with eukaryotic transcription factors—they have different mechanisms.

## Explainer

From your knowledge of transcription, you know that RNA polymerase synthesizes RNA from a DNA template. But RNA polymerase cannot simply bind anywhere on the genome and start transcribing — it needs to be directed to the right location. In prokaryotes, the system that accomplishes this targeting is remarkably elegant: a detachable protein subunit called a **sigma factor** associates with the core RNA polymerase enzyme to form the **holoenzyme**, and it is the sigma factor that recognizes and binds to specific DNA sequences upstream of genes — the promoter.

Prokaryotic promoters are defined by two conserved sequence elements located at specific positions upstream of the transcription start site. The **-10 element** (also called the **Pribnow box**), centered approximately 10 base pairs upstream of the start site, has the consensus sequence TATAAT. The **-35 element**, centered approximately 35 base pairs upstream, has the consensus TTGACA. The sigma factor makes direct contact with both of these elements, and the degree of match to the consensus determines **promoter strength** — how efficiently RNA polymerase binds and initiates transcription. A promoter with perfect matches at both positions will be transcribed frequently; one with poor matches will be transcribed rarely. The spacing between the -10 and -35 elements (optimally 17 base pairs) is also critical, because the sigma factor contacts both simultaneously and the DNA must present them on the same face of the helix.

The real power of this system lies in the existence of **alternative sigma factors**. The housekeeping sigma factor in *E. coli*, **σ⁷⁰** (sigma-70), recognizes the standard -10 and -35 elements and drives transcription of most genes during normal growth. But bacteria also carry genes for alternative sigma factors that recognize completely different promoter sequences. When the cell encounters heat shock, for example, **σ³²** (sigma-32) accumulates, associates with core polymerase, and redirects transcription to heat shock genes — chaperones and proteases that help the cell survive elevated temperatures. During nitrogen starvation, **σ⁵⁴** (sigma-54) activates a different set of genes. By swapping one sigma factor for another, the bacterium can globally reprogram its gene expression in a single step, without needing to modify the polymerase itself or the DNA.

An important detail is that sigma factor only participates in **initiation**. Once the polymerase has formed the open complex (melting the DNA strands at the -10 region) and begun synthesizing the first few nucleotides of RNA, the sigma factor **dissociates** from the core enzyme. The core polymerase then continues elongation on its own, and the released sigma factor is free to associate with another core enzyme and initiate transcription at a new promoter. This recycling mechanism means that the relative abundance of different sigma factors in the cell directly controls which promoters are active at any given moment — a simple but powerful regulatory logic that you will see elaborated in more complex forms when you study eukaryotic transcription factors and the TFIID complex.
