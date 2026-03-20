---
id: gel-electrophoresis
title: Gel Electrophoresis
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: dna-structure
  type: hard
- id: electrochemistry-basics
  type: soft
- id: chromatography-fundamentals
  type: soft
builds-toward:
- pcr
- recombinant-dna-technology
- genomics-overview
tags:
- gel electrophoresis
- agarose
- PAGE
- DNA separation
- molecular weight
stage: advanced
status: validated
---

# Gel Electrophoresis

## Core Idea
Gel electrophoresis separates nucleic acids or proteins by size using an electric field. DNA molecules (negatively charged due to phosphate groups) migrate through an agarose or polyacrylamide gel matrix toward the positive electrode; smaller fragments migrate farther in a given time. Fragment sizes are determined by comparison to a molecular weight ladder run alongside samples. Ethidium bromide or fluorescent dyes intercalate into DNA and allow visualization under UV light. SDS-PAGE (sodium dodecyl sulfate polyacrylamide gel electrophoresis) separates proteins by molecular weight after denaturation.

## How It's Best Learned
Interpret gel images by comparing band positions to a standard ladder. Predict the expected band pattern before running a gel (e.g., after restriction digestion) and reconcile with the actual result.

## Common Misconceptions
- Smaller DNA fragments migrate faster, not larger — the gel matrix acts as a sieve.
- A single bright band does not necessarily mean a single sequence; it means fragments of the same size, which could originate from many identical copies.

## Explainer

From your knowledge of DNA structure, you know that the sugar-phosphate backbone gives DNA a uniform **negative charge** — one negative charge per phosphate group, per nucleotide. This means that unlike proteins, whose charge varies with amino acid composition, every DNA fragment has a charge-to-mass ratio that is essentially constant regardless of sequence. This property is what makes gel electrophoresis such a clean separation technique for nucleic acids: when you place DNA in an electric field, all fragments migrate toward the positive electrode, and the only variable determining how far they travel is size.

The gel matrix — typically **agarose** for DNA or **polyacrylamide** for smaller fragments and proteins — acts as a molecular sieve. Think of it as a dense forest: small molecules can weave through the gaps easily and move quickly, while large molecules get tangled and slowed. When you apply a voltage across the gel, smaller DNA fragments migrate farther from the wells (the loading point) in a given time, producing a separation by size. By running a **molecular weight ladder** (a mixture of fragments of known sizes) alongside your samples, you can estimate the size of any unknown fragment by comparing its migration distance to the ladder. The relationship between migration distance and the logarithm of fragment size is approximately linear within the effective separation range of the gel.

To actually see the separated DNA, you need a visualization method. The most common is staining with **ethidium bromide** or safer alternatives like SYBR Safe, which are fluorescent dyes that intercalate between the stacked base pairs of double-stranded DNA. Under ultraviolet light, the dye-DNA complex fluoresces, revealing bands wherever DNA has accumulated. A brighter band means more DNA of that size — so band intensity is proportional to the mass of DNA present. This is important for interpreting results: after a restriction enzyme digestion, for example, each band represents fragments of a particular size, and the pattern of bands is a diagnostic fingerprint of the DNA sample.

For proteins, the situation requires an extra step because proteins vary in charge, shape, and size. **SDS-PAGE** solves this by denaturing proteins with the detergent sodium dodecyl sulfate (SDS), which unfolds them into linear chains and coats them with uniform negative charge proportional to their length. This allows separation by molecular weight alone, analogous to how DNA separates. Gel electrophoresis is foundational to nearly every molecular biology workflow — from verifying PCR products and checking restriction digests to analyzing protein expression — and understanding how it works prepares you for more advanced techniques like Southern blotting, Western blotting, and capillary electrophoresis used in DNA sequencing.
