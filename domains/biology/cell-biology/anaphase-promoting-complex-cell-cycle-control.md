---
id: anaphase-promoting-complex-cell-cycle-control
title: Anaphase-Promoting Complex and Cell Cycle Control
domain: biology
course: cell-biology
prerequisites:
- id: cell-cycle-checkpoints-cancer
  type: hard
- id: cell-cycle-regulation
  type: hard
builds-toward:
- mitosis
tags:
- APC
- ubiquitin-ligase
- cell-cycle
stage: abstract-reasoning
status: draft
---

# Anaphase-Promoting Complex and Cell Cycle Control

## Core Idea
The anaphase-promoting complex/cyclosome (APC/C) is a multisubunit ubiquitin ligase controlling cell cycle progression by targeting mitotic cyclins and securin for proteasomal degradation. APC/C remains inactive until phosphorylated and activated by binding Cdc20 coactivator, triggering securin destruction and sister chromatid separation, followed by cyclin B degradation and mitotic exit. This irreversible step enforces unidirectional cell cycle progression and prevents rereplication within a single cell cycle.

## How It's Best Learned
Measure APC/C activity in cell extracts using ubiquitination assays; track substrate degradation timing in live cells. Identify APC/C substrates and their degron sequences; test the sufficiency of minimal degrons.

## Common Misconceptions
- APC/C destroys all mitotic cyclins at once; E1 and B cyclins are degraded sequentially with distinct thresholds. - APC/C activation is irreversible; its activity remains high until mitosis exit when Cdh1 remains bound.

## Explainer

From your study of cell cycle regulation and checkpoints, you know that cyclin-CDK complexes drive the cell forward through each phase, and that checkpoints halt progression when conditions are not met. But the cell cycle also requires an irreversible switch — a mechanism that commits the cell to completing a transition with no turning back. The **anaphase-promoting complex/cyclosome (APC/C)** is that switch for the metaphase-to-anaphase transition, and it works by destroying key regulatory proteins through **ubiquitin-mediated proteolysis**.

The APC/C is a large, multisubunit **E3 ubiquitin ligase** — the enzyme that attaches chains of the small protein ubiquitin to target substrates, marking them for degradation by the **26S proteasome**. Unlike phosphorylation, which is easily reversed by phosphatases, protein destruction is permanent. Once the proteasome degrades a substrate, that protein is gone until the gene is transcribed and translated again. This irreversibility is exactly what the cell needs at anaphase: once sister chromatids separate, they cannot be reattached.

The APC/C achieves its timing through regulated activation by **coactivator proteins**. During metaphase, the spindle assembly checkpoint keeps APC/C inactive by sequestering its coactivator **Cdc20** through the mitotic checkpoint complex (MCC). Only when every chromosome achieves proper bipolar attachment to spindle microtubules does the checkpoint release Cdc20, which binds and activates APC/C. The first critical substrate is **securin**, the inhibitor of the protease **separase**. When APC/C-Cdc20 ubiquitinates securin, the proteasome degrades it, freeing separase to cleave the **cohesin** rings holding sister chromatids together. This is anaphase onset — the physical separation of chromosomes.

After securin destruction, APC/C targets **cyclin B** for degradation, which inactivates CDK1 (the mitotic kinase). Without CDK1 activity, the cell cannot maintain the mitotic state — the spindle disassembles, chromosomes decondense, the nuclear envelope reforms, and the cell exits mitosis. Later in G1, a second coactivator called **Cdh1** replaces Cdc20 and keeps APC/C active, ensuring that mitotic cyclins remain suppressed throughout G1 and preventing premature re-entry into S phase. This sustained APC/C-Cdh1 activity must be switched off by rising cyclin levels before the cell can commit to a new round of DNA replication. The APC/C thus enforces **unidirectional progression**: by permanently destroying the proteins that drove the previous phase, it ensures the cell cycle moves only forward, never backward.
