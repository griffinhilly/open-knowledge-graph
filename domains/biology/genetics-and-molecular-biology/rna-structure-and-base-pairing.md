---
id: rna-structure-and-base-pairing
title: RNA Structure and Intramolecular Base Pairing
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: rna-types-and-structure
  type: hard
builds-toward:
- rna-processing-5-cap-3-poly-a
- intron-removal-and-splicing
- ribosomal-rna-and-ribosome-assembly
- small-rnas-mirna-and-rnai
tags:
- secondary-structure
- hairpins
- pseudoknots
- self-complementarity
stage: formal-systems
status: draft
---

# RNA Structure and Intramolecular Base Pairing

## Core Idea
RNA's single-stranded nature and 2' hydroxyl group on the ribose sugar enable complex intramolecular base pairing and secondary structures absent in DNA. Self-complementary sequences within RNA form stable hairpin (stem-loop) structures, bulges, and internal loops; more complex tertiary structures include pseudoknots and exposed single-stranded regions (junctions) that serve as binding sites. These structures are critical for RNA function—they protect coding sequences, create binding sites for proteins and other RNAs, and facilitate RNA catalysis. Thermodynamic stability and kinetic accessibility (formation rates) determine which secondary structures form under physiological conditions.

## Explainer

From your study of RNA types and structure, you know that RNA is single-stranded and built from four nucleotides (A, U, G, C). But the fact that RNA is single-stranded is precisely what makes it structurally versatile. Unlike DNA, which is locked into a double helix with its complementary strand, a single RNA molecule is free to fold back on itself. Wherever a stretch of sequence is complementary to another stretch within the same molecule, those regions can base-pair — A with U, G with C — forming local double-helical segments. The result is a rich repertoire of **secondary structures** that DNA simply cannot achieve on its own.

The most common structural motif is the **hairpin** (or stem-loop): a short double-stranded "stem" formed by complementary sequences, capped by a single-stranded "loop" of unpaired nucleotides where the strand turns back on itself. Picture folding a piece of ribbon so that two halves stick together while the fold at the top forms a loop — that is a hairpin. Hairpins are everywhere in biology: they signal transcription termination in bacteria, protect mRNA from degradation, and serve as recognition sites for RNA-binding proteins. Beyond hairpins, RNA forms **bulges** (unpaired nucleotides on one side of a stem), **internal loops** (unpaired nucleotides on both sides), and **junctions** where multiple stems meet.

RNA structure goes further still. **Tertiary structures** arise when secondary structure elements interact with each other through long-range contacts. A **pseudoknot** forms when nucleotides in a loop base-pair with a sequence outside that hairpin, threading the RNA through itself in a knot-like topology. These tertiary interactions create compact, three-dimensional shapes that are essential for function — the catalytic core of the ribosome, for example, is an elaborately folded RNA whose precise three-dimensional architecture positions substrates for peptide bond formation.

The RNA also has a chemical advantage over DNA that enables this structural complexity: the **2' hydroxyl group** on the ribose sugar. This extra hydroxyl participates in hydrogen bonds that stabilize tertiary folds, allows RNA to adopt the A-form helix geometry (wider and shallower than DNA's B-form), and makes RNA capable of catalysis — as seen in ribozymes. Which structures actually form depends on thermodynamics (the most stable base-paired arrangement is favored) and kinetics (RNA folds as it is being transcribed, so the first complementary sequences to emerge pair first, sometimes trapping the molecule in a structure that is not the global energy minimum). This interplay between stability and folding order means that the same RNA sequence can adopt different structures under different conditions — a property cells exploit for regulation, as you will see in topics like transcriptional attenuation.
