---
id: centrosome-microtubule-organization
title: Centrosome Function and Microtubule Organizing Centers
domain: biology
course: cell-biology
prerequisites:
- id: organelles-overview
  type: soft
builds-toward:
- cilia-flagella-function
tags:
- centrosome
- mtoc
- microtubules
- centrioles
stage: formal-systems
status: validated
---

# Centrosome Function and Microtubule Organizing Centers

## Core Idea
The centrosome, containing two centrioles and pericentriolar material (γ-TuRC: gamma-tubulin ring complex), acts as the cell's main microtubule-organizing center (MTOC), nucleating minus-end-anchored microtubules that radiate outward. During S phase, the centrosome duplicates; the two centrosomes separate during mitosis to become spindle poles, ensuring proper chromosome segregation. Centrosome amplification (more than two) causes multipolar spindles and chromosomal instability; it is associated with genomic instability and cancer.

## Questions

```yaml
- question: "What would most likely happen if a cell had a mutation preventing centrosome duplication during S phase?"
  type: multiple-choice
  options:
    - "The cell would fail to replicate its DNA because centrosomes are required for replication"
    - "The cell would enter mitosis with one centrosome, forming an asymmetric spindle that risks unequal chromosome distribution"
    - "The cell would immediately undergo apoptosis because centrosomes are required for survival signals"
    - "Transcription would halt because centrosomes organize gene expression"
  answer: 1
  explanation: "Centrosome duplication in S phase produces two centrosomes that separate to become bipolar spindle poles in mitosis. Without duplication, the cell enters mitosis with one centrosome and cannot form a proper bipolar spindle — leading to a monopolar or asymmetric arrangement that cannot correctly segregate chromosomes to two daughter cells. Centrosomes are not required for DNA replication or transcription; their role is specifically in organizing the mitotic spindle."

- question: "A cancer cell is found to have four centrosomes instead of two. Which outcome is most directly caused by this amplification?"
  type: multiple-choice
  options:
    - "Faster DNA replication due to additional replication origins at each centrosome"
    - "Multipolar mitotic spindles that pull chromosomes in more than two directions, causing missegregation"
    - "Permanent cell cycle arrest because the spindle assembly checkpoint detects extra centrosomes"
    - "Increased transcription of oncogenes because centrosomes activate gene expression programs"
  answer: 1
  explanation: "Centrosome amplification causes multipolar spindles — three or more poles pulling chromosomes in multiple directions. This leads to chromosomal missegregation. While some cells survive by clustering extra centrosomes into a pseudo-bipolar arrangement, this introduces merotelic attachments producing chromosomal instability (CIN): persistent gains and losses of whole chromosomes. CIN is a hallmark of many aggressive cancers, which is why centrosome amplification correlates with poor prognosis."

- question: "The γ-TuRC in the centrosome caps the minus end of each microtubule it nucleates, so the growing plus end extends outward into the cytoplasm."
  type: true-false
  answer: true
  explanation: "γ-TuRC (gamma-tubulin ring complex) provides the minus-end template from which alpha/beta-tubulin dimers polymerize. Because it caps the minus end, microtubules grow only from their plus ends — extending outward from the centrosome toward the cell periphery. This directionality creates the radial array of microtubules emanating from the centrosome and, during mitosis, the spindle fibers that attach to chromosomes at their kinetochores."

- question: "Centrosome duplication is a conservative process: the two original centrioles are degraded, and two entirely new centrosomes are assembled during S phase."
  type: true-false
  answer: false
  explanation: "Centrosome duplication is semi-conservative, analogous to DNA replication. Each existing centriole serves as a template for assembling one new centriole. By G2, each centrosome contains one old (mother) centriole and one new (daughter) centriole. The original centrioles are not degraded — they persist and are distributed to daughter cells. This semi-conservative mechanism ensures each daughter cell inherits a fully functional centrosome."

- question: "Why does centrosome amplification cause chromosomal instability rather than simply killing the cell in the division where it first occurs?"
  type: short-answer
  answer: "Extra centrosomes can cluster together to form pseudo-bipolar spindles, allowing the cell to divide and survive. However, clustering introduces errors in chromosome-spindle attachments (merotelic attachments), causing some chromosomes to be pulled toward the wrong pole at a low but persistent rate. Each division produces daughters with slightly abnormal chromosome numbers, which continue dividing and accumulating further errors — ratcheting up instability over generations rather than causing immediate cell death."
  explanation: "Chromosomal instability is a rate, not a single catastrophic event. Clustering allows survival at the cost of ongoing missegregation. Each affected division has an elevated chance of producing aneuploid daughters, and those daughters can accumulate additional chromosome imbalances over time. This compounding instability drives cancer progression — it is the mechanism by which centrosome amplification contributes to aggressive tumor behavior rather than simply eliminating aberrant cells."
```

## Explainer

From your overview of organelles, you know that eukaryotic cells contain specialized compartments with distinct functions. The **centrosome** is the organelle responsible for organizing the cell's microtubule network — it is the primary **microtubule-organizing center (MTOC)** in most animal cells. Think of it as a control tower that determines where microtubules originate and in which direction they grow.

A centrosome consists of two components: a pair of **centrioles** and a surrounding cloud of **pericentriolar material (PCM)**. Each centriole is a barrel-shaped structure made of nine triplets of microtubules arranged in a pinwheel pattern. The centrioles serve as a scaffold, but the real functional component is the PCM, which contains the **gamma-tubulin ring complex (γ-TuRC)**. γ-TuRC is a ring-shaped assembly of gamma-tubulin proteins that serves as a template for microtubule nucleation — it provides the seed from which alpha/beta-tubulin dimers begin to polymerize. Because γ-TuRC caps the **minus end** of each microtubule, the growing **plus end** extends outward into the cytoplasm. This creates the characteristic radial array of microtubules emanating from the centrosome near the nucleus.

The centrosome has its own duplication cycle, tightly coordinated with the cell cycle. During **S phase**, the two centrioles within the centrosome separate slightly, and each serves as a template for assembling a new centriole — a process called **semi-conservative duplication**, analogous to DNA replication. By G2, the cell has two centrosomes, each containing one old and one new centriole. When mitosis begins, the two centrosomes migrate to opposite poles of the cell and nucleate the microtubules of the **mitotic spindle**. This bipolar arrangement is essential: kinetochore microtubules from each pole attach to opposite sides of each chromosome, ensuring that when the cell divides, each daughter receives one complete set of chromosomes.

What happens when centrosome duplication goes wrong is clinically significant. **Centrosome amplification** — the presence of more than two centrosomes — produces **multipolar spindles**, which pull chromosomes in three or more directions and cause catastrophic missegregation. Cells with extra centrosomes often cluster them into pseudo-bipolar spindles to survive, but this clustering introduces attachment errors that lead to **chromosomal instability (CIN)**: gains and losses of whole chromosomes in daughter cells. CIN is a hallmark of many aggressive cancers, and centrosome amplification is observed in a wide range of tumor types. Understanding centrosome biology thus connects organelle structure to one of the fundamental mechanisms of genome instability in cancer.
