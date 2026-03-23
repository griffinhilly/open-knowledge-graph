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
stage: formal-systems
status: validated
---

# Anaphase-Promoting Complex and Cell Cycle Control

## Core Idea
The anaphase-promoting complex/cyclosome (APC/C) is a multisubunit ubiquitin ligase controlling cell cycle progression by targeting mitotic cyclins and securin for proteasomal degradation. APC/C remains inactive until phosphorylated and activated by binding Cdc20 coactivator, triggering securin destruction and sister chromatid separation, followed by cyclin B degradation and mitotic exit. This irreversible step enforces unidirectional cell cycle progression and prevents rereplication within a single cell cycle.

## How It's Best Learned
Measure APC/C activity in cell extracts using ubiquitination assays; track substrate degradation timing in live cells. Identify APC/C substrates and their degron sequences; test the sufficiency of minimal degrons.

## Common Misconceptions
- APC/C destroys all mitotic cyclins at once; E1 and B cyclins are degraded sequentially with distinct thresholds. - APC/C activation is irreversible; its activity remains high until mitosis exit when Cdh1 remains bound.

## Questions

```yaml
- question: "A researcher treats mitotic cells with a proteasome inhibitor that blocks all protein degradation. What would you expect to observe?"
  type: multiple-choice
  options:
    - "Cells complete mitosis normally, because APC/C can still ubiquitinate its substrates"
    - "Cells arrest at metaphase, unable to separate chromosomes, because securin cannot be degraded to release separase"
    - "Cells skip anaphase and proceed directly to cytokinesis"
    - "Cells re-enter S phase prematurely due to excess cyclin-CDK activity"
  answer: 1
  explanation: "APC/C works by ubiquitinating securin, which targets it for proteasomal degradation. If the proteasome is blocked, securin persists intact, keeping separase inactive. Without active separase, cohesin rings holding sister chromatids together cannot be cleaved — chromosomes cannot separate and the cell arrests at metaphase. This experiment illustrates that ubiquitination alone is not sufficient; it is the proteasomal destruction that does the work."

- question: "Why does the metaphase-to-anaphase transition use irreversible protein destruction rather than a reversible modification like phosphorylation?"
  type: multiple-choice
  options:
    - "Protein degradation is faster than phosphorylation and allows more rapid transitions"
    - "Phosphorylation is energetically too expensive for large-scale cell cycle transitions"
    - "Destruction of securin and cyclin B creates an irreversible commitment, preventing re-cohesion of separated chromatids"
    - "Degradation is easier for cells to fine-tune through receptor-mediated pathways"
  answer: 2
  explanation: "This is the key design logic of the APC/C switch. Phosphorylation can be reversed by phosphatases, allowing transitions to go backward. But once sister chromatids separate, reattachment would cause catastrophic chromosome missegregation. Protein destruction is permanent (until new synthesis) — so destroying securin and cyclin B makes the commitment irreversible. The cell cycle needs a one-way door at anaphase, and only proteolysis provides it."

- question: "APC/C is activated as soon as a cell enters mitosis, immediately destroying securin and all mitotic cyclins to initiate chromosome separation."
  type: true-false
  answer: false
  explanation: "APC/C is held inactive during prometaphase and metaphase by the spindle assembly checkpoint, which sequesters the coactivator Cdc20. Only after every chromosome achieves proper bipolar attachment to the spindle does the checkpoint release Cdc20 to activate APC/C. Even then, substrates are destroyed sequentially — securin first (enabling chromosome separation), then cyclin B (enabling mitotic exit). Simultaneous destruction of everything at once would lose the ordered progression APC/C is designed to enforce."

- question: "After mitosis is complete, APC/C remains active throughout G1, preventing premature re-entry into S phase."
  type: true-false
  answer: true
  explanation: "In G1, the coactivator Cdh1 replaces Cdc20 and keeps APC/C active, sustaining degradation of mitotic cyclins and other S-phase-promoting factors. This APC/C-Cdh1 activity must be actively overcome by rising cyclin levels before the cell can commit to a new round of DNA replication. This is an essential part of the mechanism that prevents rereplication within a single cell cycle."

- question: "Why is irreversible protein destruction — rather than reversible phosphorylation — the right mechanism for enforcing the metaphase-to-anaphase transition?"
  type: short-answer
  answer: "Because the transition must be one-way: once sister chromatids separate, they cannot safely be reattached. A reversible mechanism like phosphorylation could be undone by phosphatases, potentially allowing the cell to 'reverse' through the transition — which would produce catastrophic errors in chromosome segregation. By permanently destroying securin and cyclin B, APC/C creates an irreversible commitment. The cell can only move forward, and this unidirectionality is exactly what reliable chromosome segregation requires."
  explanation: "This principle — using irreversible molecular events to enforce commitment at critical transitions — appears throughout cell biology. The logic here is that the cost of a 'false positive' (premature irreversibility) is much lower than the cost of reversal (chromosome segregation errors). APC/C therefore acts as a biochemical ratchet: it only turns in one direction."
```

## Explainer

From your study of cell cycle regulation and checkpoints, you know that cyclin-CDK complexes drive the cell forward through each phase, and that checkpoints halt progression when conditions are not met. But the cell cycle also requires an irreversible switch — a mechanism that commits the cell to completing a transition with no turning back. The **anaphase-promoting complex/cyclosome (APC/C)** is that switch for the metaphase-to-anaphase transition, and it works by destroying key regulatory proteins through **ubiquitin-mediated proteolysis**.

The APC/C is a large, multisubunit **E3 ubiquitin ligase** — the enzyme that attaches chains of the small protein ubiquitin to target substrates, marking them for degradation by the **26S proteasome**. Unlike phosphorylation, which is easily reversed by phosphatases, protein destruction is permanent. Once the proteasome degrades a substrate, that protein is gone until the gene is transcribed and translated again. This irreversibility is exactly what the cell needs at anaphase: once sister chromatids separate, they cannot be reattached.

The APC/C achieves its timing through regulated activation by **coactivator proteins**. During metaphase, the spindle assembly checkpoint keeps APC/C inactive by sequestering its coactivator **Cdc20** through the mitotic checkpoint complex (MCC). Only when every chromosome achieves proper bipolar attachment to spindle microtubules does the checkpoint release Cdc20, which binds and activates APC/C. The first critical substrate is **securin**, the inhibitor of the protease **separase**. When APC/C-Cdc20 ubiquitinates securin, the proteasome degrades it, freeing separase to cleave the **cohesin** rings holding sister chromatids together. This is anaphase onset — the physical separation of chromosomes.

After securin destruction, APC/C targets **cyclin B** for degradation, which inactivates CDK1 (the mitotic kinase). Without CDK1 activity, the cell cannot maintain the mitotic state — the spindle disassembles, chromosomes decondense, the nuclear envelope reforms, and the cell exits mitosis. Later in G1, a second coactivator called **Cdh1** replaces Cdc20 and keeps APC/C active, ensuring that mitotic cyclins remain suppressed throughout G1 and preventing premature re-entry into S phase. This sustained APC/C-Cdh1 activity must be switched off by rising cyclin levels before the cell can commit to a new round of DNA replication. The APC/C thus enforces **unidirectional progression**: by permanently destroying the proteins that drove the previous phase, it ensures the cell cycle moves only forward, never backward.
