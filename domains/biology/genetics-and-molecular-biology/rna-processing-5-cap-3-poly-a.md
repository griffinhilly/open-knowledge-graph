---
id: rna-processing-5-cap-3-poly-a
title: 'eRNA Processing: 5'' Capping and 3'' Polyadenylation'
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: rna-processing
  type: hard
- id: transcription
  type: soft
builds-toward:
- intron-removal-and-splicing
- translation-initiation-start-codon
tags:
- 5-cap
- 7-methylguanosine
- poly-a-tail
- mRNA-stability
stage: formal-systems
status: draft
---

# eRNA Processing: 5' Capping and 3' Polyadenylation

## Core Idea
Eukaryotic pre-mRNA undergoes extensive post-transcriptional processing to become mature mRNA. A 7-methylguanosine cap is added to the 5' end immediately during transcription (before synthesis is complete), protecting the mRNA from 5' exonuclease degradation and aiding ribosome recognition via cap-binding proteins. A polyadenylate tail of ~200 adenine nucleotides is added to the 3' end after cleavage of the nascent transcript at a polyadenylation signal (typically AAUAAA), enhancing mRNA stability, facilitating nuclear export, and increasing translation efficiency. These modifications are essential for mRNA metabolism, gene expression, and localization.

## Explainer

From your study of RNA processing, you know that eukaryotic pre-mRNA must be extensively modified before it can function as a template for protein synthesis. Two of the earliest and most critical modifications are the addition of a **5' cap** and a **3' poly-A tail**. These are not decorative — they are functional requirements without which the mRNA would be rapidly destroyed, ignored by ribosomes, or trapped in the nucleus. Understanding why these modifications exist requires thinking about the hostile environment an mRNA molecule faces inside a cell.

The **5' cap** is a modified guanosine nucleotide (7-methylguanosine) linked to the first nucleotide of the mRNA through an unusual 5'-to-5' triphosphate bridge — the reverse of the normal 3'-to-5' phosphodiester bonds in RNA. This inverted linkage makes the 5' end chemically unrecognizable to exonucleases that normally degrade RNA from the 5' end, effectively putting a protective helmet on the molecule. Capping happens co-transcriptionally: the capping enzyme associates with RNA polymerase II and modifies the 5' end when the transcript is only about 20–30 nucleotides long, well before transcription is complete. Beyond protection, the cap serves as a molecular ID badge — the **cap-binding complex (CBC)** in the nucleus recognizes it for splicing and export, and **eIF4E** in the cytoplasm recognizes it to initiate translation. Without the cap, the ribosome cannot find the start of the message.

At the other end of the molecule, the **3' poly-A tail** is added through a two-step process. First, the pre-mRNA is cleaved at a specific site downstream of the **polyadenylation signal sequence** (AAUAAA in most mRNAs). Then **poly-A polymerase** adds approximately 200 adenine nucleotides to the free 3' end — without any DNA template. The poly-A tail is bound by **poly-A binding proteins (PABPs)**, which stabilize the mRNA against 3' exonuclease degradation and, remarkably, loop back to interact with the 5' cap-binding complex. This circularization of the mRNA through cap-PABP interactions enhances translation efficiency by allowing ribosomes that finish translating to be recycled directly back to the 5' end.

Together, the 5' cap and poly-A tail create a bookend system that protects the mRNA from both ends, marks it as a legitimate transcript (distinguishing it from foreign or aberrant RNA), enables nuclear export, and promotes efficient translation. The gradual shortening of the poly-A tail over time acts as a molecular clock for mRNA lifespan — once the tail is too short to bind PABPs effectively, the mRNA becomes vulnerable to degradation. This is why some mRNAs last minutes while others persist for hours: the rate of deadenylation, combined with cap integrity, determines how long each message survives in the cytoplasm.
