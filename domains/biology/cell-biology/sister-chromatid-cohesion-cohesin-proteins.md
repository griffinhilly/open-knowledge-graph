---
id: sister-chromatid-cohesion-cohesin-proteins
title: Sister Chromatid Cohesion and Cohesin
domain: biology
course: cell-biology
prerequisites:
- id: dna-replication
  type: hard
- id: mitosis
  type: hard
builds-toward:
- anaphase-promoting-complex-cell-cycle-control
tags:
- sister-chromatids
- cohesin
- chromosome-segregation
stage: advanced
status: draft
---

# Sister Chromatid Cohesion and Cohesin

## Core Idea
Sister chromatid cohesion, mediated by the cohesin ring complex (SMC1, SMC3, SCC1, SCC3 subunits), holds newly replicated chromatids together until anaphase onset. Cohesin is loaded onto DNA by Scc2/Scc4 during S phase and forms large rings believed to topologically entrap sister chromatids. Cohesion is released in two stages: arm (non-centromeric) cohesion dissolves during prophase via Wapl-mediated release, while centromeric cohesion persists until APC/C-triggered securin degradation during anaphase.

## How It's Best Learned
Track cohesin loading and dynamics using time-lapse fluorescence microscopy; measure cohesion strength using anaphase bridge assays. Examine cohesin structure by cryo-EM; test its DNA-entrapping function experimentally.

## Common Misconceptions
- Cohesin glues chromatids together via adhesion; it topologically entraps DNA in a ring structure. - All cohesion is released at once; arm and centromeric cohesion have distinct release mechanisms.

## Explainer

From your study of DNA replication and mitosis, you know that each chromosome is copied during S phase, producing two identical **sister chromatids** joined at the centromere. You also know that during mitosis, these sisters must be pulled apart to opposite poles of the cell. But what physically holds them together in the first place? The answer is a ring-shaped protein complex called **cohesin**.

Cohesin is built from four core subunits — **SMC1**, **SMC3**, **SCC1** (also called Rad21), and **SCC3** — that form a large ring roughly 40 nanometers in diameter. The prevailing model is that this ring **topologically entraps** both sister chromatids: rather than binding to DNA through chemical adhesion (like a glue), the ring encircles both DNA molecules, threading them through its interior like two threads through a single loop. This entrapping mechanism is elegant because it holds the sisters together without covalently modifying the DNA and can be released simply by opening the ring.

Cohesin is loaded onto chromosomes by the **Scc2/Scc4** loader complex during S phase, as replication forks pass through. The timing is critical: cohesion must be established behind the replication fork so that newly synthesized sister chromatids are captured together. Once loaded, cohesin holds sisters together along their entire length — not just at the centromere. This is where the **two-step release** mechanism becomes important. During prophase, a protein called **Wapl** removes cohesin from chromosome arms, allowing the arms to separate and chromosomes to condense into the compact X-shaped structures visible under the microscope. However, centromeric cohesin is protected from Wapl by the protein Shugoshin, keeping sisters connected at the centromere.

The final release occurs at the **metaphase-to-anaphase transition**. The anaphase-promoting complex (APC/C) triggers destruction of securin, which had been inhibiting the protease separase. Once freed, separase cleaves the SCC1 subunit of centromeric cohesin, opening the ring and allowing sister chromatids to separate. This two-stage system — prophase arm removal followed by anaphase centromeric cleavage — ensures that chromatids remain connected at the centromere long enough for proper spindle attachment, but separate cleanly when the cell is ready to divide. Defects in cohesin or its regulators lead to chromosome missegregation, aneuploidy, and are implicated in both cancer and developmental disorders like Cornelia de Lange syndrome.
