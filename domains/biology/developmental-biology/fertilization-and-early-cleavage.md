---
id: fertilization-and-early-cleavage
title: Fertilization and Early Cleavage
domain: biology
course: developmental-biology
prerequisites:
- id: meiosis
  type: hard
- id: cell-signaling-intro
  type: soft
tags:
- fertilization
- cleavage
- zygote
- blastomere
- polyspermy-block
stage: advanced
status: validated
---
# Fertilization and Early Cleavage

## Core Idea
Fertilization is the union of sperm and egg that restores the diploid chromosome number and activates the developmental program. Species-specific surface molecules ensure recognition, and fast (membrane depolarization) and slow (cortical reaction) blocks to polyspermy prevent multiple sperm from fertilizing the same egg. Following fertilization, the zygote undergoes cleavage — rapid mitotic divisions that partition the large egg cell into progressively smaller blastomeres without increasing total embryo volume. Cleavage patterns (radial, spiral, bilateral) are species-specific and determined by the amount and distribution of yolk. Early cleavage establishes the basic cell number and spatial relationships that set the stage for gastrulation.

## Questions

```yaml
- question: "Why does the cortical reaction serve as a slow block to polyspermy, and why is a fast block also needed?"
  type: multiple-choice
  options:
    - "The fast block is electrical (membrane depolarization) and acts within seconds but is temporary; the cortical reaction takes minutes to complete but creates a permanent physical barrier (the fertilization envelope) — together they ensure complete polyspermy prevention"
    - "The fast block kills extra sperm with enzymes; the cortical reaction blocks the egg's nucleus"
    - "The fast block only works in mammals; the cortical reaction only works in sea urchins"
    - "Both blocks are redundant — either one alone is sufficient"
  answer: 0
  explanation: "In sea urchins (the classic model), sperm contact triggers immediate membrane depolarization (fast block) that prevents additional sperm binding within 1-3 seconds. But this electrical block is transient. The cortical reaction — calcium wave-triggered exocytosis of cortical granules that modify the extracellular matrix into a hardened fertilization envelope — takes 30-60 seconds but creates a permanent physical and chemical barrier. The two mechanisms cover different time windows: the fast block provides immediate protection while the permanent slow block is being assembled."

- question: "During cleavage, cells divide but the embryo does not grow. The total cytoplasmic volume remains approximately constant while cell number increases."
  type: true-false
  answer: true
  explanation: "Cleavage divisions are unusual: they lack G1 and G2 phases, so cells divide without growing between divisions. The large egg cytoplasm is simply partitioned into progressively smaller cells (blastomeres). A frog egg might go from one cell to thousands of cells without any increase in total volume. This rapid subdivision distributes maternal mRNAs and proteins (deposited during oogenesis) into distinct cellular compartments, creating the first differences between cells based on which cytoplasmic determinants each blastomere inherits."

- question: "How does yolk distribution in the egg affect cleavage pattern?"
  type: short-answer
  answer: "Yolk is dense and impedes the cleavage furrow. In isolecithal eggs (even yolk distribution, as in sea urchins), cleavage is equal and symmetric. In mesolecithal eggs (moderate yolk concentrated at the vegetal pole, as in frogs), cleavage is unequal — vegetal blastomeres are larger because yolk slows furrow progression. In telolecithal eggs (massive yolk, as in birds and reptiles), cleavage is restricted to a small disc of cytoplasm (meroblastic discoidal cleavage) because the cleavage furrow cannot penetrate the dense yolk mass. Yolk distribution thus determines whether cleavage is holoblastic (complete) or meroblastic (partial) and influences the geometry of cell arrangement."
  explanation: "This relationship between yolk and cleavage pattern is one of the oldest observations in developmental biology. It demonstrates how a simple physical constraint (yolk density impeding cytokinesis) shapes the spatial organization of the early embryo, which in turn influences later developmental events."
```

## Explainer

Development begins with a single event — the fusion of two specialized cells — and immediately faces two challenges: preventing additional sperm from entering, and converting one giant cell into many smaller ones that can begin the work of building an organism. Fertilization and cleavage solve these problems and set the stage for everything that follows.

**Fertilization** involves species-specific molecular recognition (sperm surface proteins binding egg coat receptors), followed by sperm-egg membrane fusion and activation of the egg's developmental program. The egg, which has been arrested in meiosis, completes its final meiotic division and initiates a cascade of intracellular calcium release. This calcium wave triggers the **cortical reaction** — exocytosis of cortical granules that modify the egg's extracellular coat into a hardened fertilization envelope, creating a permanent barrier to additional sperm. In many species, an earlier **fast block** (membrane depolarization) provides immediate, temporary polyspermy prevention while the cortical reaction is being assembled. Polyspermy must be absolutely prevented because it introduces extra chromosomes, which is invariably lethal.

**Cleavage** begins almost immediately after fertilization. The zygote divides rapidly — in some species, every 30 minutes — without any cell growth between divisions. These are stripped-down cell cycles consisting only of S phase and M phase, powered entirely by maternal mRNAs and proteins stockpiled during oogenesis. The result is progressive subdivision of the egg's cytoplasm into smaller and smaller **blastomeres**, eventually forming a hollow ball called the blastula (in many species). The cleavage pattern is profoundly influenced by **yolk** — a nutrient reserve that varies enormously across species. Sea urchin eggs have little yolk and cleave symmetrically. Frog eggs have moderate, vegetally concentrated yolk and cleave unequally (vegetal cells are larger). Bird eggs have so much yolk that cleavage is restricted to a tiny cap of cytoplasm on top.

Cleavage is not merely a subdivision exercise — it has developmental consequences. Different regions of the egg cytoplasm contain different maternal determinants (mRNAs, transcription factors, signaling molecules deposited during oogenesis). As cleavage partitions the cytoplasm, these determinants are distributed unequally among blastomeres, creating the first molecular differences between cells. In many organisms, the cleavage-stage embryo contains cells already biased toward different fates by their cytoplasmic inheritance. This sets up the initial asymmetries that the subsequent processes of gastrulation and induction will elaborate into the body plan.
