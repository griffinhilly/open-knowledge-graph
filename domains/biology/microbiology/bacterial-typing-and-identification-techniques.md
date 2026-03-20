---
id: bacterial-typing-and-identification-techniques
title: Bacterial Typing and Identification Techniques
domain: biology
course: microbiology
prerequisites:
- id: diagnostic-microbiology
  type: hard
- id: dna-barcoding-markers
  type: soft
builds-toward:
- antimicrobial-susceptibility-testing
tags:
- identification
- typing
- diagnostics
stage: advanced
status: draft
---

# Bacterial Typing and Identification Techniques

## Core Idea
Bacterial identification uses morphology, biochemistry (carbohydrate fermentation, enzyme assays), immunology (serology), and DNA methods (16S rRNA, MALDI-TOF, whole-genome sequencing). Typing differentiates strains for epidemiology via PFGE, MLST, cgMLST, or core-genome phylogenomics.

## How It's Best Learned
Identify an unknown bacterial isolate using biochemical tests and 16S sequencing. Compare relatedness of clinical isolates using multilocus sequence typing.

## Common Misconceptions
A single phenotypic test is insufficient for definitive identification; multiple methods strengthen confidence. 16S rRNA sequencing cannot always resolve subspecies or differentiate closely related strains.

## Explainer

From diagnostic microbiology, you know the clinical imperative: when a patient presents with an infection, clinicians need to identify the causative organism quickly and accurately to guide treatment. Bacterial **identification** answers "what species is this?" while **typing** answers "which strain within that species?" — a distinction that matters both for treating individual patients and for tracking outbreaks through populations.

Classical identification begins at the **phenotypic level**. A Gram stain reveals whether the organism is Gram-positive or Gram-negative and whether it forms cocci, bacilli, or other morphologies — immediately narrowing the field. From there, **biochemical tests** probe the organism's metabolic capabilities: can it ferment lactose? Does it produce catalase or oxidase? Does it use citrate as a sole carbon source? Systems like the API strip run dozens of such tests simultaneously, producing a numerical profile that is matched against a reference database. While powerful and inexpensive, biochemical identification has limitations — some species share identical metabolic profiles, and slow-growing or fastidious organisms may give ambiguous results.

Modern identification increasingly relies on **molecular and mass spectrometric methods**. **16S rRNA gene sequencing**, which you encountered through DNA barcoding, compares the sequence of this universal bacterial gene against curated databases to assign genus and species. It works because the 16S gene evolves slowly enough to preserve phylogenetic signal but fast enough to differ between species. For rapid clinical identification, **MALDI-TOF mass spectrometry** has become transformative: it ionizes proteins from a bacterial colony and generates a spectral fingerprint that is matched against a reference library in seconds, providing species-level identification from a single colony with minimal hands-on time and reagent cost.

Typing goes a level deeper than species identification. During an outbreak — say, several patients in a hospital developing the same *Klebsiella pneumoniae* infection — you need to know whether they share the same strain (suggesting transmission within the hospital) or have independently acquired different strains. **Pulsed-field gel electrophoresis** (PFGE) cuts genomic DNA with rare-cutting restriction enzymes and separates the fragments by size, producing a characteristic banding pattern that serves as a genomic fingerprint. **Multilocus sequence typing** (MLST) sequences a handful of housekeeping genes and assigns each unique combination an allelic profile, enabling comparison across laboratories worldwide. The current gold standard, **whole-genome sequencing** (WGS) and core-genome MLST (cgMLST), provides single-nucleotide resolution, revealing not only whether isolates are related but exactly how closely — enabling epidemiologists to reconstruct transmission chains with extraordinary precision.
