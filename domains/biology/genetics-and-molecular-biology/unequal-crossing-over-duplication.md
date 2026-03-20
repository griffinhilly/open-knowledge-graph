---
id: unequal-crossing-over-duplication
title: Unequal Crossing Over and Gene Duplication
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: meiotic-recombination-crossing-over
  type: hard
- id: genome-duplications
  type: hard
builds-toward:
- copy-number-variation-cnv
tags:
- unequal-crossing-over
- tandem-duplication
- gene-duplication
- recombination-error
stage: advanced
status: draft
---

# Unequal Crossing Over and Gene Duplication

## Core Idea
Unequal crossing over occurs when recombination happens between misaligned homologous repeats or tandem gene duplicates, producing one product with a duplication and one with a deletion. This mechanism generates gene duplications that fuel evolutionary innovation: new gene duplicates can accumulate mutations and diverge functionally while the original maintains essential function. The immunoglobulin gene family evolved through repeated unequal crossing overs.

## Explainer

From your study of meiotic recombination, you know that homologous chromosomes align precisely during prophase I and exchange segments through crossing over. This process normally works flawlessly because the recombination machinery aligns the chromosomes at corresponding positions — the same gene lines up with its homolog on the partner chromosome. **Unequal crossing over** is what happens when this alignment goes wrong, and understanding why it goes wrong requires thinking about what the recombination machinery actually "sees."

The machinery does not have a map of chromosome position — it relies on DNA sequence similarity to find matching regions. If a chromosome contains **tandem repeats** (multiple copies of a similar sequence arranged one after another), the recombination machinery can be tricked. Instead of aligning repeat copy 1 on one chromosome with repeat copy 1 on the other, it might align copy 1 with copy 2. When crossing over occurs at this misaligned position, the exchange is unequal: one recombinant chromosome gains an extra copy of the repeat (duplication), while the other loses a copy (deletion). Both products are reciprocal consequences of the same misalignment event.

The evolutionary significance of this error is profound. Gene duplication through unequal crossing over provides raw material for the evolution of new functions. Consider what happens after a gene is duplicated: the organism now has two copies where it previously had one. One copy continues to perform the original function — natural selection maintains it. The second copy is free from this constraint. It can accumulate mutations that would be lethal if they occurred in a single-copy gene, because the original is still functional. Over time, the duplicate may acquire a new function (**neofunctionalization**), divide the original function with its partner (**subfunctionalization**), or degrade into a nonfunctional **pseudogene**.

The globin gene family is a textbook example. The ancestral globin gene duplicated repeatedly through unequal crossing over, producing the cluster of alpha-like and beta-like globin genes found in modern vertebrates. Each copy diverged to produce hemoglobin variants tuned for different developmental stages: embryonic hemoglobin has high oxygen affinity for extracting oxygen from maternal blood, fetal hemoglobin has intermediate affinity, and adult hemoglobin releases oxygen efficiently to metabolically active tissues. Without unequal crossing over generating these duplicates, this elegant developmental regulation could not have evolved. The same mechanism generated the immunoglobulin superfamily and the olfactory receptor gene family — the largest gene family in the mammalian genome, with over a thousand members.
