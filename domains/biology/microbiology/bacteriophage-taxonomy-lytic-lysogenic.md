---
id: bacteriophage-taxonomy-lytic-lysogenic
title: 'Bacteriophages: Taxonomy and Lytic-Lysogenic Cycles'
domain: biology
course: microbiology
prerequisites:
- id: viral-classification-and-genome-types
  type: hard
- id: lysogenic-conversion-virulence-factors
  type: soft
builds-toward:
- crispr-cas-systems-bacterial-defense
tags:
- bacteriophages
- lytic
- lysogenic
stage: advanced
status: draft
---

# Bacteriophages: Taxonomy and Lytic-Lysogenic Cycles

## Core Idea
Bacteriophages (phages) are viruses that infect bacteria. The lytic cycle produces progeny and lyses the host; the lysogenic cycle integrates the prophage into the chromosome for dormant replication. Temperate phages can switch between cycles in response to stress. Phages are the most abundant organisms on Earth and shape microbial ecology and evolution.

## How It's Best Learned
Perform phage plaque assays to quantify viral titer. Observe lysogenic bacteria immune to superinfection by the same phage.

## Common Misconceptions
Lysogenic bacteria do not produce phage continuously—they are usually immune. Integration is not always exact; some prophages carry only partial genes, affecting virulence.

## Explainer

From viral classification, you know that viruses are categorized by their genome type (DNA or RNA, single- or double-stranded) and replication strategy. Bacteriophages — viruses that infect bacteria — follow these same principles but add a dimension that most animal viruses lack: the choice between immediate destruction of the host and long-term coexistence with it.

**Phage taxonomy** mirrors general viral classification. Phages are grouped into families based on morphology and genome type. The tailed phages (order *Caudovirales*) are the most abundant and well-studied, featuring an icosahedral head packed with double-stranded DNA and a tail apparatus that attaches to the bacterial surface and injects the genome. Other phage families include filamentous phages (like M13, with circular single-stranded DNA), RNA phages, and small icosahedral DNA phages. Despite this diversity, the core replication logic is the same: attach, inject genetic material, hijack the host's machinery, and produce progeny.

The critical distinction is between **lytic** and **lysogenic** life cycles. A strictly **lytic phage** (also called a virulent phage) follows a one-way path: it injects its DNA, immediately commandeers the host's ribosomes and polymerases to make phage proteins and replicate phage DNA, assembles new phage particles inside the cell, and then produces lysozyme or holin proteins that rupture the bacterial cell wall, releasing typically 50–200 new phage particles to infect neighboring cells. The entire cycle takes 20–60 minutes. From the bacterium's perspective, infection is a death sentence.

**Temperate phages** have a second option. After injecting their DNA, they can enter the **lysogenic cycle** instead: the phage genome integrates into the bacterial chromosome (becoming a **prophage**) and replicates passively every time the bacterium divides. The bacterium suffers no harm and is, in fact, immune to superinfection by the same phage type — a repressor protein encoded by the prophage blocks expression of lytic genes and prevents additional copies of the same phage from initiating a lytic cycle. The prophage can remain dormant for hundreds of bacterial generations. However, when the host cell encounters severe stress — DNA damage, UV radiation, nutrient starvation — the SOS response inactivates the repressor, the prophage excises from the chromosome, and the lytic cycle resumes. This "molecular bet-hedging" strategy allows temperate phages to ride along safely during good times and escape from a doomed host during bad times, making them extraordinarily successful in microbial ecosystems.
