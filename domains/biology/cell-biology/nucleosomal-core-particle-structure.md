---
id: nucleosomal-core-particle-structure
title: Nucleosomal Core Particle Structure
domain: biology
course: cell-biology
prerequisites:
- id: dna-structure
  type: hard
- id: histone-modifications-epigenetic
  type: soft
builds-toward:
- chromatin-fiber-higher-order-structure
tags:
- nucleosome
- chromatin
- histones
stage: abstract-reasoning
status: draft
---

# Nucleosomal Core Particle Structure

## Core Idea
The nucleosome core particle comprises 147 base pairs of DNA wrapped 1.65 turns around an octamer of core histones (two copies each of H2A, H2B, H3, H4), representing the fundamental repeating unit of chromatin. Histone-DNA interactions are mediated by ionic and hydrogen bonding between the positively charged histone tails and the negatively charged DNA phosphate backbone. Nucleosomes position DNA on the histone surface, restricting access to transcription factors and recombination machinery, effectively repressing gene expression unless chromatin remodeling or histone modifications alter accessibility.

## How It's Best Learned
Isolate nucleosomal core particles by micrococcal nuclease digestion; determine positioning using DNA sequencing. Study nucleosome accessibility using DNase-seq or ATAC-seq; measure transcription factor binding to nucleosomal DNA.

## Common Misconceptions
- DNA wraps around histone cores outside-to-outside; DNA enters one side and exits the other. - Nucleosomes are permanent; they are dynamic structures constantly assembling and disassembling.

## Explainer

You already know that DNA is a long, negatively charged double helix — and from your study of histone modifications, you know that chemical tags on histone proteins influence gene activity. The **nucleosome** is the structure that connects these two ideas: it is the fundamental unit of DNA packaging in eukaryotic cells, and it determines whether a given stretch of DNA is accessible for transcription or locked away in silence.

Picture a thread wound around a spool. The thread is DNA — specifically, **147 base pairs** of it — and the spool is a disc-shaped protein complex called the **histone octamer**, composed of two copies each of histones H2A, H2B, H3, and H4. The DNA wraps 1.65 turns around the outside of this octamer, held in place by electrostatic attraction: the positively charged amino acid residues (lysine and arginine) on the histones grip the negatively charged phosphate backbone of the DNA. Between each nucleosome core particle sits a stretch of **linker DNA** (typically 20–80 bp), sometimes associated with linker histone H1, giving chromatin its classic "beads on a string" appearance under the electron microscope.

The critical insight is that wrapping DNA around nucleosomes is not just about fitting two meters of DNA into a nucleus a few micrometers across — it is a **regulatory mechanism**. When DNA is tightly wound on a nucleosome, transcription factors and RNA polymerase cannot easily access the underlying sequence. The cell must actively remodel or displace nucleosomes to turn genes on. **Chromatin remodeling complexes** use ATP hydrolysis to slide, eject, or restructure nucleosomes, exposing the DNA underneath. Meanwhile, the histone tails — flexible N-terminal extensions that protrude from the core particle — serve as platforms for the post-translational modifications you studied earlier. Acetylation of lysine residues neutralizes their positive charge, loosening the histone-DNA grip and promoting transcription. Methylation can either activate or repress genes depending on which residue is modified and how many methyl groups are added.

Nucleosomes are not static bricks cemented into place. They are **dynamic assemblies** that constantly breathe — transiently unwrapping and rewrapping — allowing brief windows of access even in relatively compact chromatin. This dynamic behavior, combined with the combinatorial language of histone modifications and the activity of remodeling enzymes, gives the cell exquisite control over which genes are expressed in which tissues at which times. Understanding the nucleosome as both a packaging unit and a regulatory gate is essential for grasping how the same genome can produce a neuron, a muscle cell, and a liver cell.
