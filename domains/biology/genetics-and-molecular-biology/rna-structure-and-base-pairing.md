---
id: rna-structure-and-base-pairing
title: RNA Structure and Intramolecular Base Pairing
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: rna-types-and-structure
  type: hard
builds-toward:
- rna-processing
- intron-removal-and-splicing
- ribosomal-rna-and-ribosome-assembly
- small-rnas-mirna-and-rnai
tags:
- secondary-structure
- hairpins
- pseudoknots
- self-complementarity
stage: formal-systems
status: validated
---

# RNA Structure and Intramolecular Base Pairing

## Core Idea
RNA's single-stranded nature and 2' hydroxyl group on the ribose sugar enable complex intramolecular base pairing and secondary structures absent in DNA. Self-complementary sequences within RNA form stable hairpin (stem-loop) structures, bulges, and internal loops; more complex tertiary structures include pseudoknots and exposed single-stranded regions (junctions) that serve as binding sites. These structures are critical for RNA function—they protect coding sequences, create binding sites for proteins and other RNAs, and facilitate RNA catalysis. Thermodynamic stability and kinetic accessibility (formation rates) determine which secondary structures form under physiological conditions.

## Questions

```yaml
- question: "A synthetic RNA molecule has the sequence: [region A]–[linker]–[reverse complement of A]. When placed in solution, what secondary structure will it most likely form?"
  type: multiple-choice
  options:
    - "A double helix with a second RNA molecule, because region A and its reverse complement are complementary"
    - "A hairpin (stem-loop), because the self-complementary regions within the single strand can base-pair intramolecularly, with the linker forming the loop"
    - "A random coil, because RNA is too flexible to maintain stable secondary structure without proteins"
    - "A linear double-stranded segment, because complementary sequences always pair in a straight anti-parallel arrangement"
  answer: 1
  explanation: "Because RNA is single-stranded and free to fold, a region that is complementary to another part of the same molecule will base-pair intramolecularly. The reverse complement of region A is exactly what A needs as a base-pairing partner — so the molecule folds back on itself, A pairs with its reverse complement, and the linker region forms the loop at the top. This hairpin formation is the fundamental mechanism of RNA secondary structure and is driven by the same A–U and G–C pairing rules as intermolecular duplexes."

- question: "Why can RNA perform catalytic reactions (as in ribozymes and the ribosomal peptidyl transferase center) while DNA generally cannot?"
  type: multiple-choice
  options:
    - "RNA is single-stranded, so all its bases are always accessible to reactants"
    - "The 2' hydroxyl on ribose enables hydrogen bonding that stabilizes compact three-dimensional folds and can participate directly in catalytic chemistry — capabilities unavailable to DNA"
    - "RNA contains uracil instead of thymine, and uracil is a more chemically reactive base"
    - "RNA is thermally less stable than DNA, making its bonds easier to break and reform during catalysis"
  answer: 1
  explanation: "The 2' hydroxyl is the critical chemical difference between RNA and DNA. It participates in hydrogen bonds that stabilize tertiary folds, forces the A-form helix geometry (wider and shallower than DNA's B-form), and can directly participate in nucleophilic attack during ribozyme-catalyzed reactions. DNA lacks the 2'-OH and is structurally locked into B-form duplexes — informationally stable but catalytically inert. RNA's ability to fold into precise three-dimensional architectures is what gives it catalytic capability."

- question: "The secondary structure that an RNA molecule adopts is always the arrangement of base pairs with the greatest overall thermodynamic stability — the global energy minimum."
  type: true-false
  answer: false
  explanation: "RNA folds as it is being transcribed, not after the complete sequence is available. The first complementary sequences to emerge pair first, sometimes trapping the molecule in a kinetically accessible but thermodynamically suboptimal structure. The final structure reflects both thermodynamic stability and folding kinetics — the same sequence can adopt different structures depending on transcription rate, temperature, ion concentrations, and the presence of RNA chaperones. Cells exploit this kinetic control for gene regulation, as in transcriptional attenuation."

- question: "A pseudoknot forms when nucleotides in an RNA loop base-pair with a sequence outside the hairpin, creating a topology more complex than a simple stem-loop."
  type: true-false
  answer: true
  explanation: "In a simple hairpin, the loop nucleotides are unpaired and accessible. A pseudoknot forms when some of those loop nucleotides base-pair with a single-stranded region outside the stem, threading the RNA through itself in a knot-like topology that cannot be drawn in two dimensions without crossing lines. Pseudoknots create compact, stable three-dimensional structures found in the catalytic cores of ribozymes and in ribosomal frameshifting signals — their precise topology is essential to their function."

- question: "Why does the single-stranded nature of RNA make it structurally more versatile and functionally more diverse than double-stranded DNA?"
  type: short-answer
  answer: "Because RNA is single-stranded, it is free to fold back on itself wherever complementary sequences exist within the same molecule. This intramolecular base pairing creates hairpins, bulges, internal loops, junctions, and pseudoknots — a rich repertoire of secondary and tertiary structures. DNA is locked into a regular double helix with its complement, structurally uniform and functionally limited to information storage. RNA's diverse folds create specific binding sites for proteins and other RNAs, enable catalytic activity (ribozymes), regulate gene expression (attenuation, riboswitches), and allow the same sequence to adopt different structures under different conditions. The 2' hydroxyl further enables the A-form helix and direct participation in catalysis."
  explanation: "The 'RNA world' hypothesis — that early life used RNA as both genetic material and catalyst — is grounded in precisely this dual capability. RNA can store information (like DNA) AND act as a functional molecule (like protein) because its single-stranded nature plus the 2'-OH give it structural versatility that neither DNA alone nor unfolded polymers can match."
```

## Explainer

From your study of RNA types and structure, you know that RNA is single-stranded and built from four nucleotides (A, U, G, C). But the fact that RNA is single-stranded is precisely what makes it structurally versatile. Unlike DNA, which is locked into a double helix with its complementary strand, a single RNA molecule is free to fold back on itself. Wherever a stretch of sequence is complementary to another stretch within the same molecule, those regions can base-pair — A with U, G with C — forming local double-helical segments. The result is a rich repertoire of **secondary structures** that DNA simply cannot achieve on its own.

The most common structural motif is the **hairpin** (or stem-loop): a short double-stranded "stem" formed by complementary sequences, capped by a single-stranded "loop" of unpaired nucleotides where the strand turns back on itself. Picture folding a piece of ribbon so that two halves stick together while the fold at the top forms a loop — that is a hairpin. Hairpins are everywhere in biology: they signal transcription termination in bacteria, protect mRNA from degradation, and serve as recognition sites for RNA-binding proteins. Beyond hairpins, RNA forms **bulges** (unpaired nucleotides on one side of a stem), **internal loops** (unpaired nucleotides on both sides), and **junctions** where multiple stems meet.

RNA structure goes further still. **Tertiary structures** arise when secondary structure elements interact with each other through long-range contacts. A **pseudoknot** forms when nucleotides in a loop base-pair with a sequence outside that hairpin, threading the RNA through itself in a knot-like topology. These tertiary interactions create compact, three-dimensional shapes that are essential for function — the catalytic core of the ribosome, for example, is an elaborately folded RNA whose precise three-dimensional architecture positions substrates for peptide bond formation.

The RNA also has a chemical advantage over DNA that enables this structural complexity: the **2' hydroxyl group** on the ribose sugar. This extra hydroxyl participates in hydrogen bonds that stabilize tertiary folds, allows RNA to adopt the A-form helix geometry (wider and shallower than DNA's B-form), and makes RNA capable of catalysis — as seen in ribozymes. Which structures actually form depends on thermodynamics (the most stable base-paired arrangement is favored) and kinetics (RNA folds as it is being transcribed, so the first complementary sequences to emerge pair first, sometimes trapping the molecule in a structure that is not the global energy minimum). This interplay between stability and folding order means that the same RNA sequence can adopt different structures under different conditions — a property cells exploit for regulation, as you will see in topics like transcriptional attenuation.
