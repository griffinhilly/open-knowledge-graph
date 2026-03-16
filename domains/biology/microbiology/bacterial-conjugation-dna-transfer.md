---
id: bacterial-conjugation-dna-transfer
title: Bacterial Conjugation and DNA Transfer
domain: biology
course: microbiology
prerequisites:
- id: bacterial-conjugation-plasmid-transfer
  type: hard
- id: bacterial-plasmids-and-extrachromosomal-elements
  type: soft
builds-toward:
- antibiotic-resistance-genetic-mechanisms
tags:
- conjugation
- dna-transfer
- mating
stage: formal-systems
status: draft
---

# Bacterial Conjugation and DNA Transfer

## Core Idea
Conjugation involves direct cell-to-cell contact via a pilus to transfer plasmids or chromosomal DNA. The donor synthesizes a complementary strand and pumps single-stranded DNA through the pore. This process disseminates antibiotic resistance genes globally and is a major driver of bacterial genetic diversity and pathogenesis.

## Explainer

You already understand that bacteria carry plasmids — small, self-replicating DNA circles — and that conjugation is one mechanism for transferring them between cells. Here we examine the molecular machinery and broader implications of conjugative DNA transfer in detail, because this process is the single most important driver of antibiotic resistance spread across bacterial populations.

The process begins with a **donor cell** (designated F⁺ or Hfr) that carries a conjugative plasmid encoding the genes for transfer machinery. The first visible step is the extension of a **sex pilus** — a long, hollow protein filament assembled from pilin subunits — that makes contact with a **recipient cell** (F⁻). The pilus then retracts, pulling the two cells into direct contact and forming a stable **mating pair** connected by a membrane channel called the **transferosome**. Think of the pilus as a grappling hook: it finds the target and reels it in, but the actual DNA transfer occurs through the channel formed at the junction, not through the pilus itself.

Once stable contact is established, a **relaxase** enzyme nicks one strand of the plasmid at a specific sequence called the **origin of transfer (oriT)**. The nicked single strand is then unwound and threaded 5′-to-3′ through the transferosome into the recipient cell, powered by a coupling protein that acts as a molecular pump. Simultaneously, both cells use DNA polymerase to synthesize the complementary strand — the donor rebuilds its double-stranded plasmid, and the recipient converts the incoming single strand into a complete double-stranded plasmid. The result: both cells now carry the plasmid, and the former F⁻ recipient becomes F⁺, capable of donating to other cells. This exponential spread is what makes conjugation so epidemiologically dangerous — a single resistance plasmid entering a bacterial population can sweep through it rapidly.

A special case occurs when the conjugative plasmid integrates into the bacterial chromosome, creating an **Hfr (high-frequency recombination) strain**. When an Hfr cell conjugates, it begins transferring chromosomal DNA starting from the integrated oriT. Because the entire chromosome takes about 100 minutes to transfer in *E. coli*, and mating pairs rarely remain stable that long, only genes close to the integration site typically make it across. The transferred chromosomal DNA can then recombine with the recipient's chromosome, introducing new alleles. This mechanism was historically used in interrupted mating experiments to map bacterial genes by their order of transfer. Conjugation can cross species barriers — even transferring DNA between gram-negative and gram-positive bacteria or from bacteria to yeast — making it a powerful force for horizontal gene flow across the microbial world.
