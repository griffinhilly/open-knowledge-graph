---
id: reverse-transcription-mechanism
title: Reverse Transcription and Retroviral Replication
domain: biology
course: microbiology
prerequisites:
- id: viral-replication-rna-polymerase
  type: hard
- id: dna-polymerase-structure-and-fidelity
  type: soft
tags:
- reverse-transcription
- retrovirus
- rna-dependent-dna
stage: advanced
status: draft
---

# Reverse Transcription and Retroviral Replication

## Core Idea
Retroviruses and related elements use reverse transcriptase to convert their RNA genome into DNA, which is integrated into the host genome. The enzyme synthesizes a cDNA strand complementary to viral RNA, degrades the RNA template, and synthesizes the second DNA strand. This allows long-term viral persistence but is error-prone, driving rapid evolution and drug resistance.

## Explainer

You already know that RNA viruses use RNA-dependent RNA polymerase to copy their genomes, and that DNA polymerases synthesize new DNA strands with high fidelity using a template. **Reverse transcriptase** (RT) breaks the central dogma's usual flow by doing something neither of those enzymes does: it reads an RNA template and writes a DNA copy. This enzyme is the defining feature of retroviruses like HIV and is what makes their replication strategy fundamentally different from other RNA viruses.

The process unfolds in several carefully orchestrated steps. RT first uses a host tRNA as a primer to synthesize a single-stranded **complementary DNA** (cDNA) copy of the viral RNA genome. As it works, a built-in RNase H activity degrades the RNA template strand behind it — the enzyme is essentially erasing the original as it copies. RT then synthesizes the second DNA strand using the cDNA as a template, producing a double-stranded DNA molecule called the **provirus**. This provirus is integrated into the host cell's chromosomal DNA by another viral enzyme, integrase, where it can persist for the lifetime of the cell and be inherited by all daughter cells.

What makes reverse transcription biologically consequential is its error rate. Unlike the DNA polymerases you studied, reverse transcriptase lacks proofreading exonuclease activity. It makes roughly one error per 10,000 nucleotides — orders of magnitude worse than cellular DNA polymerase. For a ~10 kb HIV genome, this means nearly every new viral copy contains at least one mutation. This extreme mutation rate is a double-edged sword: most mutations are deleterious and produce defective virions, but the sheer number of variants generated means that drug-resistant or immune-evasive mutants arise rapidly within a patient. This is precisely why HIV treatment requires combination antiretroviral therapy — targeting RT alone leaves enough evolutionary room for resistance to emerge.

Reverse transcription is not limited to retroviruses. **Retrotransposons**, which make up roughly 40% of the human genome, use the same enzymatic logic to copy and paste themselves throughout chromosomal DNA. Hepatitis B virus also employs reverse transcription, though it packages DNA rather than RNA in its virions. Understanding this mechanism therefore connects viral biology to genome evolution and reveals why RT inhibitors like AZT and tenofovir are cornerstones of antiviral pharmacology.
