---
id: homologous-recombination-rad51-complex
title: Homologous Recombination and the RAD51 Complex
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: meiotic-recombination-crossing-over
  type: soft
- id: dna-repair-mechanisms
  type: soft
builds-toward:
- non-homologous-end-joining-nhej
- genetic-mapping-recombination-frequency
tags:
- homologous-recombination
- rad51
- double-strand-break-repair
- dna-repair
stage: advanced
status: draft
---

# Homologous Recombination and the RAD51 Complex

## Core Idea
Homologous recombination repairs double-strand breaks and facilitates meiotic recombination. RAD51 protein replaces RPA on single-stranded DNA, forming a nucleoprotein filament. The filament invades homologous duplex DNA, forming a D-loop. DNA polymerase extends the invading 3' end, and resolution of the double Holiday junction completes recombination.

## How It's Best Learned
Follow the biochemical steps of homologous recombination: end resection by MRN/EXO1, RPA coating, RAD51 loading and filament formation, strand invasion, DNA synthesis, and resolution. Use electron microscopy or cryo-EM images to visualize D-loops and Holiday junctions.

## Common Misconceptions
- Assuming recombination always uses homologous template when some is ectopic or between non-allelic sequences.
- Not recognizing that the same machinery (RAD51, MRN) functions in both mitotic DSB repair and meiotic recombination.
- Thinking recombination is purely generative (creating new combinations) when it also serves a repair function.

## Explainer

From your study of meiotic recombination, you know that crossing over shuffles alleles between homologous chromosomes, generating genetic diversity. From DNA repair mechanisms, you know that double-strand breaks (DSBs) are among the most dangerous forms of DNA damage — a single unrepaired DSB can kill a cell. **Homologous recombination** (HR) is the molecular process that serves both purposes: it is the engine behind meiotic crossovers *and* the primary high-fidelity repair pathway for DSBs in somatic cells. The **RAD51 protein** is the central player in this process.

The pathway begins when a DSB is detected and processed. The MRN complex (Mre11-Rad50-Nbs1) recognizes the broken ends and, together with nucleases like EXO1, resects the 5' ends to generate long 3' single-stranded DNA (ssDNA) tails. These ssDNA tails are immediately coated by **RPA** (Replication Protein A), which prevents them from forming secondary structures and protects them from degradation. But RPA must be displaced before recombination can proceed — this is where RAD51 enters.

With the help of mediator proteins (BRCA2 in humans, Rad52 in yeast), **RAD51 replaces RPA** on the ssDNA, forming a helical nucleoprotein filament — a structure that looks like a stretched-out spring of protein wrapped around DNA. This RAD51 filament is the active search-and-invasion machine. It scans the genome for a homologous duplex DNA sequence (typically the sister chromatid in mitotic cells, or the homologous chromosome in meiosis), and when it finds a match, the filament catalyzes **strand invasion**: the ssDNA tail physically displaces one strand of the homologous duplex and pairs with the complementary strand, forming a structure called a **D-loop** (displacement loop). This is the step that gives HR its name — it requires a homologous template, which is what makes the repair accurate rather than error-prone.

Once the D-loop forms, DNA polymerase extends the invading 3' end using the homologous strand as a template, effectively copying the missing information across the break. The subsequent steps depend on the sub-pathway: in the classical **double Holliday junction** (dHJ) pathway, the second broken end is captured, two four-way junctions form, and their resolution by specialized nucleases produces either crossover or non-crossover products. In the **synthesis-dependent strand annealing** (SDSA) pathway — the predominant pathway in mitotic cells — the extended strand is displaced and re-anneals to the other broken end, always producing non-crossovers. The choice between these pathways is tightly regulated: meiotic cells favor dHJ resolution to generate the crossovers essential for chromosome segregation, while mitotic cells favor SDSA to avoid the loss of heterozygosity that crossovers would cause. Understanding RAD51-mediated HR provides the mechanistic foundation for topics ranging from genetic mapping to cancer biology, since mutations in HR genes (BRCA1, BRCA2, RAD51) are among the most clinically significant in human genetics.
