---
id: bacterial-transcription-and-operon-regulation
title: Bacterial Transcription and Operon Regulation
domain: biology
course: microbiology
prerequisites:
- id: gene-regulation-prokaryotes
  type: hard
- id: bacterial-chromosome-nucleoid-dna-organization
  type: soft
builds-toward:
- quorum-sensing
tags:
- transcription
- operons
- regulation
stage: advanced
status: draft
---

# Bacterial Transcription and Operon Regulation

## Core Idea
Bacterial RNA polymerase recognizes promoters via sigma factors and transcribes operons—coordinately regulated clusters of functionally related genes. Negative control (e.g., lac repressor) and positive control (e.g., CAP-cAMP) allow rapid adaptation to nutrient availability. This organization contrasts sharply with eukaryotic gene regulation.

## Questions

```yaml
- question: "E. coli cells are growing in medium containing both glucose and lactose. What is the predicted expression level of the lac operon, and why?"
  type: multiple-choice
  options:
    - "Fully expressed, because lactose is present and the lac repressor is inactivated by allolactose"
    - "Largely repressed, because glucose keeps cAMP levels low, preventing CAP-cAMP from activating transcription"
    - "Partially expressed, because one activating signal (lactose) and one inhibiting signal (glucose) cancel out"
    - "Completely silent, because glucose directly binds the lac promoter and blocks RNA polymerase"
  answer: 1
  explanation: "The lac operon functions as a logical AND gate: full expression requires lactose present (repressor off) AND glucose absent (CAP-cAMP on). When glucose is present, adenylyl cyclase is inhibited, cAMP levels fall, and CAP cannot form the CAP-cAMP complex needed to recruit RNA polymerase. Even though lactose is present and deactivates the repressor, the operon is transcribed at very low levels without positive CAP-cAMP activation. This catabolite repression ensures bacteria consume the most energetically favorable carbon source (glucose) before investing in enzymes for alternative sugars."

- question: "What is the functional significance of bacteria possessing multiple sigma factors?"
  type: multiple-choice
  options:
    - "Each sigma factor proofreads a different class of transcripts for errors before they are translated"
    - "Different sigma factors direct RNA polymerase to different sets of promoters, enabling global transcriptional reprogramming in response to environmental conditions"
    - "Multiple sigma factors serve as backup subunits in case the primary sigma factor is degraded"
    - "Multiple sigma factors allow several RNA polymerases to transcribe the same gene simultaneously, increasing output"
  answer: 1
  explanation: "Sigma factors are the address-recognition modules of RNA polymerase: they bind promoter sequences and determine which genes are transcribed. Bacteria maintain multiple sigma factors with different sequence specificities — σ⁷⁰ for housekeeping genes, σ³² for heat shock genes, σˢ for stationary-phase survival, σ⁵⁴ for nitrogen metabolism. By changing which sigma factor is loaded onto the core polymerase, the cell can globally redirect transcription to an entirely different set of genes. This is faster and more comprehensive than individually regulating hundreds of genes, making sigma factor switching a powerful regulatory strategy for responding to stress and environmental change."

- question: "Removing glucose from E. coli growth medium causes intracellular cAMP levels to rise, which promotes CAP-cAMP binding and boosts lac operon transcription."
  type: true-false
  answer: true
  explanation: "When glucose is present, it inhibits adenylyl cyclase (the enzyme that synthesizes cAMP from ATP), keeping cAMP low and CAP inactive. When glucose is removed, adenylyl cyclase activity increases, cAMP levels rise, and cAMP binds CAP. The CAP-cAMP complex then binds upstream of the lac promoter, bends the DNA, and directly contacts RNA polymerase, stimulating transcription roughly 50-fold. This explains catabolite repression: glucose's indirect effect on cAMP is the mechanism by which its presence suppresses lac operon expression."

- question: "In the lac operon system, the absence of glucose alone is sufficient to drive full lac operon transcription, even if lactose is also absent from the medium."
  type: true-false
  answer: false
  explanation: "Full lac operon expression requires two conditions simultaneously: lactose must be present (to generate allolactose, which inactivates the lac repressor) AND glucose must be absent (to raise cAMP levels and activate CAP). Without lactose, the lac repressor remains bound to the operator regardless of glucose levels, blocking transcription. CAP-cAMP activation increases transcriptional efficiency, but it cannot overcome a repressor that is physically blocking the polymerase. The AND logic prevents wasteful enzyme synthesis: there is no point in making lactose-metabolizing enzymes if there is no lactose to metabolize."

- question: "Why does E. coli express the lac operon at high levels only when lactose is present AND glucose is absent, and what does this two-condition requirement reveal about how bacteria prioritize energy sources?"
  type: short-answer
  answer: "The two conditions implement a nutrient hierarchy. Glucose is the preferred carbon source because it is metabolized more efficiently. By requiring glucose absence (high cAMP → active CAP) for full lac operon expression, the cell ensures it invests in lactose-metabolizing enzymes only when glucose is unavailable. Lactose presence (allolactose → repressor off) ensures the enzymes are made only when there is actually lactose to metabolize. The AND gate prevents two kinds of waste: making lactose enzymes when glucose is already available (unnecessary), and making them when lactose is absent even if glucose is gone (pointless). This regulatory logic is a general principle of bacterial metabolism — major catabolic operons are only fully activated when the preferred substrate is gone and the alternative substrate is present."
  explanation: "The broader principle is catabolite repression: glucose and its metabolites suppress the expression of operons for alternative carbon sources throughout the bacterial genome. This is not glucose directly repressing the lac operon — it is glucose indirectly keeping cAMP low and thus CAP inactive. The system is therefore responsive to the cell's overall metabolic state, not just to the presence of any one molecule."
```

## Explainer

You already understand the basics of prokaryotic gene regulation — that bacteria control which genes are expressed and when, primarily at the level of transcription. This topic builds on that foundation by examining how bacterial transcription machinery and operon architecture work together as an integrated regulatory system, enabling bacteria to respond to their environment with remarkable speed and efficiency.

**Bacterial RNA polymerase** is a multi-subunit enzyme (core enzyme: α₂ββ'ω) that cannot, on its own, find the right place to start transcribing. It needs a **sigma factor** (σ) to recognize promoter sequences. The primary sigma factor, **σ⁷⁰** in *E. coli*, directs transcription of housekeeping genes by recognizing conserved -10 and -35 promoter elements. But bacteria carry alternative sigma factors — σ³² for heat shock genes, σ⁵⁴ for nitrogen metabolism, σˢ for stationary-phase survival — that redirect the polymerase to entirely different sets of promoters. Think of sigma factors as interchangeable address labels: by swapping which sigma is loaded onto the polymerase, the cell can globally reprogram its transcriptional output in response to stress, starvation, or environmental change. This is faster than modifying individual gene regulators one by one.

The **operon** is the organizational unit that makes this system efficient. An operon clusters functionally related genes under a single promoter so they are transcribed together as one **polycistronic mRNA**. The *lac* operon is the classic example: the genes for lactose uptake (lacY) and cleavage (lacZ) are adjacent and co-transcribed, ensuring the cell never makes the transporter without the enzyme or vice versa. Regulation of this operon illustrates both major control strategies. **Negative control** comes from the **lac repressor**, a protein that binds the operator (a DNA sequence overlapping the promoter) and physically blocks RNA polymerase from transcribing. When allolactose (the inducer) binds the repressor, the repressor changes shape and falls off the DNA, allowing transcription. **Positive control** comes from **CAP** (catabolite activator protein), which binds upstream of the promoter only when complexed with **cAMP** — and cAMP levels are high only when glucose is absent. CAP-cAMP bends the DNA and helps recruit RNA polymerase, boosting transcription roughly 50-fold.

The interplay between these two controls creates a logical AND gate: the *lac* operon is fully expressed only when lactose is present (repressor removed) AND glucose is absent (CAP-cAMP active). This **catabolite repression** system ensures bacteria use the most energetically favorable carbon source first — glucose — before investing in enzymes for alternative sugars. The same regulatory logic applies across many operons: the *trp* operon uses a repressor activated by tryptophan (negative control of a biosynthetic pathway), while nitrogen-regulated operons use σ⁵⁴ and activator proteins. The common thread is that bacteria regulate transcription at the operon level to coordinate gene expression with metabolic need, a strategy that is fast, economical, and fundamentally different from the enhancer-based, single-gene regulation you will encounter in eukaryotic systems.
