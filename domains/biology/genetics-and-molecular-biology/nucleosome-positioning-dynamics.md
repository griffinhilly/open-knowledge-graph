---
id: nucleosome-positioning-dynamics
title: Nucleosome Positioning and Occupancy Dynamics
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: nucleosomal-core-particle-structure
  type: hard
- id: chromatin-fiber-higher-order-structure
  type: hard
builds-toward:
- chromatin-accessibility-and-remodeling-complexes
tags:
- nucleosome-positioning
- chromatin-organization
- nucleosome-occupancy
- gene-activation
stage: advanced
status: draft
---

# Nucleosome Positioning and Occupancy Dynamics

## Core Idea
Nucleosome positioning is not random but determined by DNA sequence preferences, histone-DNA binding energy, and chromatin remodeling factor activity. Promoter regions typically have nucleosome-depleted regions upstream of the transcription start site, while gene bodies display periodic nucleosome spacing. Nucleosome positioning is dynamic: nucleosomes are displaced during transcription initiation and rapidly reassembled afterward, and dynamic repositioning regulates access to regulatory DNA.

## Explainer

From your study of nucleosome structure, you know that each nucleosome consists of approximately 147 base pairs of DNA wrapped around a histone octamer, and that nucleosomes are the fundamental repeating unit of chromatin. But knowing the structure raises a critical question: *where* along the genome do nucleosomes sit? If nucleosomes were positioned randomly, every stretch of DNA would be equally accessible. In reality, nucleosome positioning is highly regulated, and it profoundly determines which genes can be read and which are locked away.

Three factors determine where nucleosomes form. First, **DNA sequence preferences**: DNA does not bend equally well everywhere. Sequences with regularly spaced A/T dinucleotides every ~10 base pairs (matching the helical repeat) curve naturally around the histone octamer and form stable nucleosomes, while stiff poly(dA:dT) tracts resist wrapping and tend to exclude nucleosomes. Second, **ATP-dependent chromatin remodeling complexes** — enzymes like SWI/SNF, ISWI, and RSC — actively slide, eject, or restructure nucleosomes, overriding sequence preferences when the cell needs to change access patterns. Third, **competition from other DNA-binding proteins**: transcription factors and the transcription machinery itself can displace nucleosomes or prevent their reassembly at specific locations.

The most functionally important positioning feature is the **nucleosome-depleted region (NDR)** found at most active promoters. In yeast and other eukaryotes, a gap of roughly 150–200 base pairs immediately upstream of the transcription start site is kept clear of nucleosomes, flanked by well-positioned nucleosomes called the **−1 and +1 nucleosomes**. The NDR provides an open landing pad where transcription factors and RNA polymerase can access the DNA. Downstream into the gene body, nucleosomes are arranged in a regular, evenly spaced array — each positioned relative to the +1 nucleosome like dominoes set at fixed intervals. This ordered arrangement is established by remodeling complexes that use the +1 nucleosome as an anchor and space subsequent nucleosomes at regular intervals.

Nucleosome positioning is not static — it is **dynamically regulated** in response to cellular signals. When a gene is activated, remodeling complexes evict or slide nucleosomes away from the promoter to expose transcription factor binding sites. During transcription elongation, RNA polymerase must plow through nucleosomes in the gene body; histone chaperones partially disassemble nucleosomes ahead of the polymerase and reassemble them behind it, maintaining chromatin integrity while permitting transcription. When a gene is silenced, nucleosomes are repositioned to cover the promoter and block access. This constant reshuffling means that nucleosome positions represent a dynamic equilibrium between assembly and disassembly forces, and shifts in that equilibrium are a primary mechanism by which cells turn genes on and off.
