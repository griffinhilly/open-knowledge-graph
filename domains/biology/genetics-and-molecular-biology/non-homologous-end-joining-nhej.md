---
id: non-homologous-end-joining-nhej
title: Non-Homologous End Joining (NHEJ) and DSB Repair
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: dna-repair-mechanisms
  type: hard
builds-toward:
- crispr-gene-editing
tags:
- dna-repair
- non-homologous-end-joining
- nhej
- double-strand-break
stage: formal-systems
status: draft
---

# Non-Homologous End Joining (NHEJ) and DSB Repair

## Core Idea
NHEJ is a major pathway for double-strand break repair that directly ligates DNA ends without requiring homologous sequence. Ku70/Ku80 recognize and protect DNA ends; DNA-PK catalyzes processing; Ligase IV seals the nick. NHEJ is error-prone (may cause small insertions or deletions) but is rapid and active throughout the cell cycle.

## How It's Best Learned
Compare NHEJ and homologous recombination in terms of template requirement, accuracy, cell-cycle timing, and consequences of repair. Understand why NHEJ predominates at telomeres and in non-coding regions.

## Common Misconceptions
- Assuming NHEJ is the primary DSB repair pathway; HR may be preferred when homologs are available.
- Not recognizing that NHEJ can result in loss or gain of a few nucleotides at the break site.
- Thinking NHEJ is bad because it is error-prone; it provides a rapid repair option when accuracy is less critical than speed.

## Explainer

From your study of DNA repair mechanisms, you know that double-strand breaks (DSBs) are the most dangerous form of DNA damage — a single unrepaired DSB can trigger cell death or chromosomal rearrangements. Cells have two main strategies for fixing DSBs: homologous recombination (HR), which uses a sister chromatid as a template for accurate repair, and **non-homologous end joining (NHEJ)**, which directly glues the broken ends back together without any template. NHEJ trades accuracy for speed and availability — it works in any phase of the cell cycle, including G1 when no sister chromatid exists, making it the default DSB repair pathway in most mammalian cells.

The NHEJ pathway proceeds through a series of steps, each handled by a dedicated protein complex. First, the **Ku70/Ku80 heterodimer** — a ring-shaped protein — threads onto each broken DNA end and acts as a scaffold, protecting the ends from degradation by nucleases and recruiting downstream repair factors. Think of Ku as a molecular clamp that stabilizes the break site. Next, Ku recruits **DNA-PKcs** (DNA-dependent protein kinase catalytic subunit), which bridges the two ends and phosphorylates itself and other repair factors to activate processing. If the broken ends are not directly compatible (which they usually are not — DSBs often leave damaged or mismatched bases), processing enzymes like Artemis trim the ends to create ligatable termini.

The final step is ligation by the **XRCC4–Ligase IV complex**, which seals the nick and restores the phosphodiester backbone. The entire process can be completed within minutes — far faster than HR, which requires extensive strand invasion and DNA synthesis. However, the processing step is where errors creep in. Trimming damaged nucleotides from the break ends before ligation often removes a few base pairs, creating small **deletions**. Sometimes the polymerases μ and λ add a few nucleotides to fill gaps, creating small **insertions**. These insertions and deletions (collectively called **indels**) are the hallmark of NHEJ repair and the reason the pathway is described as error-prone.

Despite its imprecision, NHEJ is not a backup mechanism — it is essential. Cells that lack NHEJ components are hypersensitive to ionizing radiation (which causes DSBs) and show severe immunodeficiency because V(D)J recombination, the process that generates antibody diversity, relies on NHEJ to rejoin the programmed DSBs made during immune receptor gene rearrangement. NHEJ is also the pathway exploited by CRISPR-Cas9 gene editing: when Cas9 cuts a target site, NHEJ repair introduces indels that disrupt the reading frame, effectively knocking out the gene. Understanding NHEJ — its speed, its error profile, and its cell-cycle independence — is therefore crucial not only for understanding genome stability but also for designing and interpreting modern genome engineering experiments.
