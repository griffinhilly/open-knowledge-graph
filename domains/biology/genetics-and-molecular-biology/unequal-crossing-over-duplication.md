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

## Questions

```yaml
- question: "During meiosis, two chromosomes each carry tandem copies of a gene (copy 1 and copy 2). Instead of aligning copy 1 with copy 1, the recombination machinery aligns copy 1 on one chromosome with copy 2 on the other. What are the products of the resulting crossing over event?"
  type: multiple-choice
  options:
    - "Both chromosomes end up with two copies of the gene — both products gain a duplication"
    - "One chromosome gains an extra copy (duplication) while the other loses a copy (deletion) — the products are reciprocal consequences of the same misalignment"
    - "The misalignment is detected and repaired before crossing over occurs, producing no change"
    - "Both chromosomes end up with the original single copy because the misalignment creates a deletion in both"
  answer: 1
  explanation: "Unequal crossing over produces reciprocal products because the physical exchange is conserved: what one chromosome gains, the other must lose. If chromosome A aligns copy 1 opposite copy 2 on chromosome B, then the segment between them is exchanged; chromosome A receives an extra copy while chromosome B loses one. This reciprocity is a direct consequence of the mechanics of crossing over — no material is created or destroyed, it is exchanged."

- question: "Why is gene duplication through unequal crossing over evolutionarily important, rather than simply a replication error?"
  type: multiple-choice
  options:
    - "It increases genome size, which is always advantageous because larger genomes encode more protein diversity"
    - "It creates two copies where there was one, allowing one copy to accumulate mutations and acquire new functions while the original maintains its essential ancestral role"
    - "It primarily produces deletions that eliminate nonfunctional pseudogenes, streamlining the genome"
    - "It generates variation within a single gene, enabling that gene to simultaneously perform multiple contradictory functions"
  answer: 1
  explanation: "The evolutionary significance lies in the relaxation of selective constraint. A single-copy essential gene cannot tolerate most mutations — any change that impairs function is lethal or deleterious. After duplication, one copy continues to be selected to maintain ancestral function while the other is free to experiment. Over time the duplicate may evolve a new function (neofunctionalization), partition the original function (subfunctionalization), or degrade into a pseudogene. The globin, immunoglobulin, and olfactory receptor gene families all arose through this mechanism."

- question: "The recombination machinery aligns homologous chromosomes using physical chromosome position — it finds the matching segment by locating the same chromosomal address — which prevents tandem repeats from causing misalignment."
  type: true-false
  answer: false
  explanation: "This is the key misconception. The recombination machinery uses DNA sequence similarity, not chromosomal position, to find matching regions. It cannot 'know' that copy 1 and copy 2 are at different positions; it only sees that they share very similar sequences. When a chromosome contains tandem repeats with nearly identical sequences, the machinery can pair copy 1 on one chromosome with copy 2 on the other. This sequence-based recognition, rather than position-based recognition, is exactly what makes tandem repeats prone to unequal crossing over."

- question: "After gene duplication, one copy is free to accumulate mutations that would be lethal in a single-copy gene, because the other copy continues to maintain the original essential function."
  type: true-false
  answer: true
  explanation: "This redundancy is the engine of gene family evolution. When a gene exists in a single copy, purifying selection eliminates nearly all mutations that impair its function. After duplication, one copy is 'buffered' — it can tolerate loss-of-function mutations in the duplicate because the original still works. This relaxation of constraint allows exploration of sequence space that would otherwise be forbidden, and eventually produces new gene functions. The globin gene family's developmental specialization (embryonic, fetal, adult hemoglobins) is a direct product of this evolutionary freedom."

- question: "Explain why tandem repeats make unequal crossing over more likely, and describe what determines which product receives the duplication versus the deletion."
  type: short-answer
  answer: "Tandem repeats present the recombination machinery with multiple regions of near-identical sequence. Since alignment is sequence-based, copy 1 on one chromosome can pair with copy 2 on the other ('slippage'). Crossing over at this misaligned position exchanges unequal segments. Which product receives the duplication versus deletion is determined by the direction of the slip: the chromosome that gains the segment between the two different repeat copies receives an extra copy (duplication), while the partner chromosome loses that segment (deletion). The two outcomes are always reciprocal — the same misalignment event produces both simultaneously."
  explanation: "This mechanism explains why large gene families are especially concentrated in genomic regions with abundant tandem repeats. The olfactory receptor loci and immunoglobulin gene clusters are both tandemly arranged and have undergone extensive unequal crossing over throughout vertebrate evolution. The same mechanism also produces copy number variants (CNVs) that underlie many human phenotypic differences and disease susceptibilities."
```

## Explainer

From your study of meiotic recombination, you know that homologous chromosomes align precisely during prophase I and exchange segments through crossing over. This process normally works flawlessly because the recombination machinery aligns the chromosomes at corresponding positions — the same gene lines up with its homolog on the partner chromosome. **Unequal crossing over** is what happens when this alignment goes wrong, and understanding why it goes wrong requires thinking about what the recombination machinery actually "sees."

The machinery does not have a map of chromosome position — it relies on DNA sequence similarity to find matching regions. If a chromosome contains **tandem repeats** (multiple copies of a similar sequence arranged one after another), the recombination machinery can be tricked. Instead of aligning repeat copy 1 on one chromosome with repeat copy 1 on the other, it might align copy 1 with copy 2. When crossing over occurs at this misaligned position, the exchange is unequal: one recombinant chromosome gains an extra copy of the repeat (duplication), while the other loses a copy (deletion). Both products are reciprocal consequences of the same misalignment event.

The evolutionary significance of this error is profound. Gene duplication through unequal crossing over provides raw material for the evolution of new functions. Consider what happens after a gene is duplicated: the organism now has two copies where it previously had one. One copy continues to perform the original function — natural selection maintains it. The second copy is free from this constraint. It can accumulate mutations that would be lethal if they occurred in a single-copy gene, because the original is still functional. Over time, the duplicate may acquire a new function (**neofunctionalization**), divide the original function with its partner (**subfunctionalization**), or degrade into a nonfunctional **pseudogene**.

The globin gene family is a textbook example. The ancestral globin gene duplicated repeatedly through unequal crossing over, producing the cluster of alpha-like and beta-like globin genes found in modern vertebrates. Each copy diverged to produce hemoglobin variants tuned for different developmental stages: embryonic hemoglobin has high oxygen affinity for extracting oxygen from maternal blood, fetal hemoglobin has intermediate affinity, and adult hemoglobin releases oxygen efficiently to metabolically active tissues. Without unequal crossing over generating these duplicates, this elegant developmental regulation could not have evolved. The same mechanism generated the immunoglobulin superfamily and the olfactory receptor gene family — the largest gene family in the mammalian genome, with over a thousand members.
