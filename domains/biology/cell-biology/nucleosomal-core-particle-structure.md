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
stage: formal-systems
status: draft
---

# Nucleosomal Core Particle Structure

## Core Idea
The nucleosome core particle comprises 147 base pairs of DNA wrapped 1.65 turns around an octamer of core histones (two copies each of H2A, H2B, H3, H4), representing the fundamental repeating unit of chromatin. Histone-DNA interactions are mediated by ionic and hydrogen bonding between the positively charged histone tails and the negatively charged DNA phosphate backbone. Nucleosomes position DNA on the histone surface, restricting access to transcription factors and recombination machinery, effectively repressing gene expression unless chromatin remodeling or histone modifications alter accessibility.

## How It's Best Learned
Isolate nucleosomal core particles by micrococcal nuclease digestion; determine positioning using DNA sequencing. Study nucleosome accessibility using DNase-seq or ATAC-seq; measure transcription factor binding to nucleosomal DNA.

## Common Misconceptions
- DNA wraps around histone cores outside-to-outside; DNA enters one side and exits the other. - Nucleosomes are permanent; they are dynamic structures constantly assembling and disassembling.

## Questions

```yaml
- question: "A researcher observes that a gene's promoter is tightly wrapped in nucleosomes in a differentiated cell but shows nucleosome-free regions in a stem cell. The most direct explanation is:"
  type: multiple-choice
  options:
    - "The stem cell's DNA has been chemically modified, altering the promoter sequence"
    - "Chromatin remodeling complexes have used ATP hydrolysis to reposition or eject nucleosomes at the promoter, exposing the DNA"
    - "The gene's promoter sequence differs between cell types due to somatic mutation"
    - "Histones are absent in stem cells, leaving all DNA as naked double helix"
  answer: 1
  explanation: "Nucleosome positioning is a regulatory mechanism, not a fixed structural feature. Chromatin remodeling complexes (such as SWI/SNF) use ATP hydrolysis to slide, eject, or restructure nucleosomes, creating nucleosome-free regions that allow transcription factors and RNA polymerase to bind. This is how the same genome produces different gene expression patterns in different cell types — through differential nucleosome occupancy at regulatory regions, not changes to the DNA sequence itself."

- question: "Which statement about nucleosome dynamics is most accurate?"
  type: multiple-choice
  options:
    - "Nucleosomes are permanent structures that require cell division to be reorganized"
    - "The histone octamer binds DNA irreversibly through covalent bonds, requiring enzymatic cleavage to release"
    - "Nucleosomes constantly breathe — transiently unwrapping and rewrapping — allowing brief windows of DNA access even in compact chromatin"
    - "The nucleosome remains fully intact and undisturbed during transcription as RNA polymerase loops around it"
  answer: 2
  explanation: "Nucleosomes are dynamic assemblies held together by electrostatic and hydrogen bonds that allow transient unwrapping. This 'breathing' creates brief exposures of nucleosomal DNA, enabling transcription factors to probe for binding sites even in relatively compact chromatin. Full transcriptional activation typically requires chromatin remodeling complexes to more stably displace or reposition nucleosomes, but even without active remodeling, the inherent dynamics of nucleosome breathing provide a baseline level of DNA accessibility."

- question: "The ionic attraction between positively charged histone residues and negatively charged DNA phosphate groups is a primary force holding the nucleosome together."
  type: true-false
  answer: true
  explanation: "The histone octamer is enriched in lysine and arginine residues, which carry positive charges at physiological pH. These form electrostatic interactions with the negatively charged phosphate backbone of the DNA double helix. This is why histone acetylation — which adds an acetyl group to lysine, neutralizing its positive charge — weakens histone-DNA contacts and loosens chromatin structure, directly demonstrating that charge-based attraction is the primary physical mechanism of nucleosome assembly."

- question: "The primary biological purpose of the nucleosome is DNA compaction — fitting the genome into the nucleus — and gene regulation is an incidental byproduct of this packaging."
  type: true-false
  answer: false
  explanation: "Nucleosome positioning is a central mechanism of gene regulation, not a byproduct of compaction. Cells invest substantial energy in ATP-dependent chromatin remodeling complexes and an elaborate system of histone post-translational modifications precisely to control which regions are nucleosome-occupied (repressed) versus nucleosome-free (accessible). The same genome produces ~200 distinct cell types in the human body largely through differential nucleosome positioning and histone modification, demonstrating that regulation is a primary — not incidental — function."

- question: "How does histone acetylation facilitate gene expression, and what does this reveal about the nucleosome's role as a regulatory element?"
  type: short-answer
  answer: "Acetylation adds an acetyl group to lysine residues on histone tails, neutralizing their positive charge. This reduces electrostatic attraction between the histone octamer and the negatively charged DNA phosphate backbone, loosening the DNA-histone grip and creating more open chromatin. Transcription factors and RNA polymerase can then access the underlying DNA sequence. This reveals that the nucleosome is an adjustable gate: by chemically modifying histone tails, the cell dynamically tunes DNA accessibility. The nucleosome is not merely a structural spool but the primary unit of epigenetic regulation."
  explanation: "The consequence is profound: the same DNA sequence can be silenced or expressed depending on the post-translational modification state of the histones packaging it. This is the molecular basis for cell-type-specific gene expression from a single genome — and it explains why histone-modifying enzymes (acetyltransferases, deacetylases, methyltransferases) are major targets in cancer therapy."
```

## Explainer

You already know that DNA is a long, negatively charged double helix — and from your study of histone modifications, you know that chemical tags on histone proteins influence gene activity. The **nucleosome** is the structure that connects these two ideas: it is the fundamental unit of DNA packaging in eukaryotic cells, and it determines whether a given stretch of DNA is accessible for transcription or locked away in silence.

Picture a thread wound around a spool. The thread is DNA — specifically, **147 base pairs** of it — and the spool is a disc-shaped protein complex called the **histone octamer**, composed of two copies each of histones H2A, H2B, H3, and H4. The DNA wraps 1.65 turns around the outside of this octamer, held in place by electrostatic attraction: the positively charged amino acid residues (lysine and arginine) on the histones grip the negatively charged phosphate backbone of the DNA. Between each nucleosome core particle sits a stretch of **linker DNA** (typically 20–80 bp), sometimes associated with linker histone H1, giving chromatin its classic "beads on a string" appearance under the electron microscope.

The critical insight is that wrapping DNA around nucleosomes is not just about fitting two meters of DNA into a nucleus a few micrometers across — it is a **regulatory mechanism**. When DNA is tightly wound on a nucleosome, transcription factors and RNA polymerase cannot easily access the underlying sequence. The cell must actively remodel or displace nucleosomes to turn genes on. **Chromatin remodeling complexes** use ATP hydrolysis to slide, eject, or restructure nucleosomes, exposing the DNA underneath. Meanwhile, the histone tails — flexible N-terminal extensions that protrude from the core particle — serve as platforms for the post-translational modifications you studied earlier. Acetylation of lysine residues neutralizes their positive charge, loosening the histone-DNA grip and promoting transcription. Methylation can either activate or repress genes depending on which residue is modified and how many methyl groups are added.

Nucleosomes are not static bricks cemented into place. They are **dynamic assemblies** that constantly breathe — transiently unwrapping and rewrapping — allowing brief windows of access even in relatively compact chromatin. This dynamic behavior, combined with the combinatorial language of histone modifications and the activity of remodeling enzymes, gives the cell exquisite control over which genes are expressed in which tissues at which times. Understanding the nucleosome as both a packaging unit and a regulatory gate is essential for grasping how the same genome can produce a neuron, a muscle cell, and a liver cell.
