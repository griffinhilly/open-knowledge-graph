---
id: nucleotide-synthesis
title: Nucleotide Synthesis Pathways (De Novo and Salvage)
domain: biology
course: biochemistry
prerequisites:
- id: organic-chemistry-intro
  type: hard
builds-toward:
- dna-replication-machinery
- transcription-initiation-and-regulation
tags:
- nucleotide synthesis
- purine
- pyrimidine
- de novo
- salvage pathway
stage: advanced
status: draft
---

# Nucleotide Synthesis Pathways (De Novo and Salvage)

## Core Idea
Nucleotides are synthesized through two pathways: de novo synthesis (building the base and ribose ring from simpler precursors) and salvage pathways (recycling bases and nucleosides from degraded nucleic acids). De novo purine synthesis begins with PRPP and constructs the purine ring while attached to ribose, producing IMP, then AMP and GMP. De novo pyrimidine synthesis first completes the pyrimidine ring as orotate, then attaches to PRPP, producing UMP, then CTP and dTTP. Both pathways are tightly regulated by feedback inhibition and require multiple vitamin cofactors (folate, B12).

## Explainer

Every time a cell divides, it must duplicate its entire genome — billions of nucleotides assembled with precision. Nucleotides are also the currency of energy transfer (ATP, GTP), signaling (cAMP, cGMP), and coenzyme function (NAD⁺, FAD, CoA). Given your foundation in organic chemistry, you can appreciate that building these complex molecules from scratch is no small feat. Cells solve this challenge through two complementary strategies: **de novo synthesis** (building nucleotides from simple precursors) and **salvage pathways** (recycling bases from degraded nucleic acids).

De novo **purine** synthesis is distinctive because the purine ring is assembled piece by piece *while already attached to ribose-5-phosphate*. The starting material is **PRPP** (5-phosphoribosyl-1-pyrophosphate), and atoms from glutamine, glycine, aspartate, CO₂, and N¹⁰-formyl-THF (a folate derivative) are added in a ten-step sequence to build the first complete purine nucleotide: **IMP** (inosine monophosphate). IMP sits at a branch point — it can be converted to AMP (via aspartate addition) or GMP (via oxidation and amination). Notably, AMP synthesis requires GTP, and GMP synthesis requires ATP, creating a built-in balancing mechanism that keeps purine pools in proportion.

De novo **pyrimidine** synthesis takes the opposite approach: the ring is built first as a free base, and sugar is attached afterward. Carbamoyl phosphate (from glutamine and CO₂) condenses with aspartate to begin ring construction, ultimately producing **orotate** — the completed pyrimidine ring. Only then does orotate react with PRPP to become orotidylate, which is decarboxylated to **UMP**. From UMP, cells produce CTP (by amination of UTP) and the deoxythymidylate (dTMP) needed for DNA synthesis. The enzyme **thymidylate synthase**, which converts dUMP to dTMP using a folate cofactor, is a critical drug target — chemotherapy agents like 5-fluorouracil and methotrexate block this step, starving rapidly dividing cancer cells of the thymidine they need to replicate DNA.

**Salvage pathways** are energetically cheaper alternatives that reclaim free bases (hypoxanthine, guanine, adenine) released during normal nucleic acid turnover and reattach them to PRPP. The enzyme **HGPRT** (hypoxanthine-guanine phosphoribosyltransferase) is the best-known salvage enzyme; its complete deficiency causes Lesch-Nyhan syndrome, a devastating neurological disorder that reveals how dependent the brain is on purine recycling. Both de novo and salvage pathways are regulated by **feedback inhibition** — the end products (AMP, GMP, UMP, CTP) inhibit early committed steps in their own synthesis, ensuring that nucleotide pools stay balanced without overproduction.
