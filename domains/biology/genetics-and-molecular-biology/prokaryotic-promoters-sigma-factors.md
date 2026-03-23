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

## Questions

```yaml
- question: "A bacterium encounters heat shock. A researcher observes that hundreds of heat shock genes are rapidly activated while most housekeeping genes are simultaneously downregulated. What single mechanism best explains this global shift?"
  type: multiple-choice
  options:
    - "The cell mutates the promoters of all heat shock genes to make them stronger"
    - "Ribosomes preferentially translate heat shock mRNAs due to special sequence elements"
    - "The heat shock sigma factor (σ³²) accumulates, competes with σ⁷⁰ for core polymerase, and redirects transcription to promoters with σ³²-specific -10 and -35 sequences"
    - "The cell degrades core RNA polymerase and synthesizes a new polymerase specialized for heat shock genes"
  answer: 2
  explanation: "The sigma factor swap is the elegance of prokaryotic transcriptional regulation. Under normal conditions, σ⁷⁰ is dominant and drives housekeeping gene expression. Under heat shock, σ³² is synthesized and stabilized. Because sigma factors compete for a limited pool of core polymerase, more σ³²-holoenzyme forms at the expense of σ⁷⁰-holoenzyme. The result: hundreds of genes regulated by σ³² promoters are upregulated while σ⁷⁰-dependent genes get fewer holoenzymes — a global reprogramming achieved by changing one protein."

- question: "What is the significance of sigma factor dissociating from core polymerase after transcription initiation?"
  type: multiple-choice
  options:
    - "It means core polymerase must be re-synthesized before initiating transcription at another gene"
    - "It means sigma factor can be recycled — freed sigma associates with new core polymerases to initiate transcription at other promoters, making initiation rate sensitive to sigma abundance"
    - "It means elongation is more error-prone than initiation because sigma factor normally ensures fidelity"
    - "It prevents the sigma factor sequence from being transcribed into the mRNA"
  answer: 1
  explanation: "Sigma factor is a catalytic component for initiation: it helps core polymerase find and melt the promoter, then dissociates and is free to function again. This recycling mechanism means that the relative abundance of different sigma factors in the cell directly controls which promoters are active. A small pool of σ³² can initiate transcription at many heat shock promoters in sequence. The recycling also means that sigma factor stoichiometry is not 1:1 with active transcription units."

- question: "Core RNA polymerase (without sigma factor) can initiate transcription at specific gene promoters, but does so less efficiently than the holoenzyme."
  type: true-false
  answer: false
  explanation: "Core polymerase alone cannot initiate transcription at specific promoters at all — it binds DNA non-specifically and cannot recognize or melt the promoter in a directed way. Promoter specificity is entirely provided by the sigma factor. Without sigma, core polymerase would transcribe random genomic sequences. The holoenzyme (core + sigma) is the functional unit for specific, regulated transcription initiation."

- question: "The spacing between the -10 and -35 promoter elements affects promoter strength because sigma factor must contact both elements simultaneously on the same face of the DNA helix."
  type: true-false
  answer: true
  explanation: "Sigma factor makes direct protein-DNA contacts at both the -10 (TATAAT) and -35 (TTGACA) elements. Because the sigma factor is a rigid structure, the optimal spacing between these elements (approximately 17 bp, corresponding to about 1.6 helical turns) ensures they are presented on the same face of the double helix so sigma can bridge them simultaneously. Promoters with suboptimal spacing have reduced sigma binding affinity and are therefore weaker — fewer holoenzyme binding events per unit time."

- question: "Explain how a single bacterium can rapidly reprogram the expression of hundreds of genes in response to environmental stress, using only the sigma factor mechanism."
  type: short-answer
  answer: "By changing which sigma factor is most abundant. The cell synthesizes or stabilizes an alternative sigma factor (e.g., σ³² for heat shock), which competes with the housekeeping σ⁷⁰ for binding to core polymerase. The dominant sigma factor determines which promoter sequences are recognized, effectively redirecting the entire transcriptional machinery to a new set of genes — without altering the polymerase itself or the DNA."
  explanation: "This is one of biology's most elegant regulatory solutions: a single regulatory variable (sigma factor identity) controls global gene expression. The mechanism is analogous to software: the core polymerase is the hardware, and the sigma factor is the program loaded into it. Swapping programs changes which genes are transcribed. The recycling of sigma after initiation, and competition between sigma factors for core polymerase, ensures that the regulatory response is graded: the more alternative sigma, the more of the stress-response genes are expressed."
```

## Explainer

From your knowledge of transcription, you know that RNA polymerase synthesizes RNA from a DNA template. But RNA polymerase cannot simply bind anywhere on the genome and start transcribing — it needs to be directed to the right location. In prokaryotes, the system that accomplishes this targeting is remarkably elegant: a detachable protein subunit called a **sigma factor** associates with the core RNA polymerase enzyme to form the **holoenzyme**, and it is the sigma factor that recognizes and binds to specific DNA sequences upstream of genes — the promoter.

Prokaryotic promoters are defined by two conserved sequence elements located at specific positions upstream of the transcription start site. The **-10 element** (also called the **Pribnow box**), centered approximately 10 base pairs upstream of the start site, has the consensus sequence TATAAT. The **-35 element**, centered approximately 35 base pairs upstream, has the consensus TTGACA. The sigma factor makes direct contact with both of these elements, and the degree of match to the consensus determines **promoter strength** — how efficiently RNA polymerase binds and initiates transcription. A promoter with perfect matches at both positions will be transcribed frequently; one with poor matches will be transcribed rarely. The spacing between the -10 and -35 elements (optimally 17 base pairs) is also critical, because the sigma factor contacts both simultaneously and the DNA must present them on the same face of the helix.

The real power of this system lies in the existence of **alternative sigma factors**. The housekeeping sigma factor in *E. coli*, **σ⁷⁰** (sigma-70), recognizes the standard -10 and -35 elements and drives transcription of most genes during normal growth. But bacteria also carry genes for alternative sigma factors that recognize completely different promoter sequences. When the cell encounters heat shock, for example, **σ³²** (sigma-32) accumulates, associates with core polymerase, and redirects transcription to heat shock genes — chaperones and proteases that help the cell survive elevated temperatures. During nitrogen starvation, **σ⁵⁴** (sigma-54) activates a different set of genes. By swapping one sigma factor for another, the bacterium can globally reprogram its gene expression in a single step, without needing to modify the polymerase itself or the DNA.

An important detail is that sigma factor only participates in **initiation**. Once the polymerase has formed the open complex (melting the DNA strands at the -10 region) and begun synthesizing the first few nucleotides of RNA, the sigma factor **dissociates** from the core enzyme. The core polymerase then continues elongation on its own, and the released sigma factor is free to associate with another core enzyme and initiate transcription at a new promoter. This recycling mechanism means that the relative abundance of different sigma factors in the cell directly controls which promoters are active at any given moment — a simple but powerful regulatory logic that you will see elaborated in more complex forms when you study eukaryotic transcription factors and the TFIID complex.
