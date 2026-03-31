---
id: model-organisms-development
title: Model Organisms
domain: biology
course: developmental-biology
prerequisites:
- id: gastrulation
  type: hard
- id: cell-fate-determination
  type: soft
builds-toward: []
tags:
- model-organisms
- Drosophila
- C-elegans
- Xenopus
- zebrafish
- mouse
- Arabidopsis
stage: expert
status: validated
---
# Model Organisms

## Core Idea
Developmental biology relies on a small set of model organisms, each chosen for specific experimental advantages: Drosophila melanogaster (rapid genetics, powerful mutant screens, accessible embryo), C. elegans (invariant cell lineage, transparency, RNAi tractability), Xenopus laevis (large accessible embryos ideal for microsurgery and biochemistry), zebrafish (optical transparency, genetic screens, vertebrate with rapid external development), and mouse (mammalian physiology, gene targeting, relevance to human disease). Each model organism has revealed different aspects of developmental biology — the logic of genetic screens (Drosophila), the deterministic cell lineage (C. elegans), embryonic induction (Xenopus), live imaging of development (zebrafish), and mammalian-specific mechanisms (mouse). Comparing developmental mechanisms across models reveals conserved principles and lineage-specific innovations.

## Questions

```yaml
- question: "Why was Drosophila melanogaster the organism in which the genetic logic of body plan patterning was first worked out?"
  type: multiple-choice
  options:
    - "Drosophila is the most complex organism and therefore the most informative"
    - "Drosophila combines rapid generation time, powerful forward genetics (mutagenesis screens), externally developing embryos with visible segmentation, and a compact genome — enabling systematic identification of genes controlling body plan patterning"
    - "Drosophila was the only available research organism at the time"
    - "Drosophila development is simpler than all other animals and therefore easier to study"
  answer: 1
  explanation: "Nusslein-Volhard and Wieschaus performed saturating mutagenesis screens in Drosophila (Nobel Prize, 1995), systematically identifying genes required for embryonic patterning. This was possible because of Drosophila's short generation time (10 days), the ease of screening thousands of mutagenized lines for visible body plan defects (missing segments, homeotic transformations), and the compact genome that made it feasible to identify mutations by genetic mapping. The segmented body plan provided a clear readout — disrupted segment pattern was immediately visible. These practical advantages, combined with decades of prior genetic work, made Drosophila the system where the molecular logic of development was first cracked."

- question: "C. elegans has an invariant cell lineage — every individual of the species undergoes exactly the same sequence of cell divisions, producing the same 959 somatic cells. This means cell-cell signaling plays no role in C. elegans development."
  type: true-false
  answer: false
  explanation: "The invariant lineage might suggest that development is entirely cell-autonomous (determined by lineage history alone), but cell-cell signaling is essential at many points. Vulval induction requires EGF signaling from the anchor cell, and lateral inhibition via Notch ensures the correct vulval cell pattern. Asymmetric cell divisions in the early embryo depend on cell-cell interactions. The invariant lineage reflects the outcome of both cell-autonomous determinants and stereotyped cell-cell signaling events — the signaling is just as invariant as the lineage itself. If signaling is disrupted (by mutation or laser ablation of the inducing cell), the lineage becomes abnormal."

- question: "What experimental advantages does the zebrafish offer that neither Drosophila nor mouse can provide?"
  type: short-answer
  answer: "Zebrafish embryos are optically transparent, allowing live imaging of every cell division, migration, and differentiation event in a developing vertebrate in real time. Combined with fluorescent transgenic reporters, this enables watching gene expression dynamics, cell lineage tracing, and morphogenetic movements in vivo. Zebrafish also develop externally (unlike mice) and rapidly (major organs form within 24 hours), are small enough for high-throughput drug screens (embryos fit in 96-well plates), and are genetically tractable (forward genetic screens and CRISPR editing). This combination of vertebrate biology, optical transparency, and high-throughput tractability is unique to zebrafish."
  explanation: "Zebrafish have become the organism of choice for in vivo imaging of vertebrate development and for large-scale chemical screens to identify drugs that affect specific developmental processes. Their transparency solves a fundamental problem: in mice, development occurs inside the mother and inside opaque tissues, making live observation impossible without invasive procedures."
```

## Explainer

No single organism can reveal all of developmental biology. Each model organism offers a different window into how embryos build themselves, and the field's progress has depended on matching the right question to the right organism. The choice of model is not arbitrary — each was selected for specific experimental advantages that make certain questions answerable.

**Drosophila melanogaster** opened the modern era of developmental genetics. Its short generation time (10 days), ease of mutagenesis, visible segmented body plan, and compact genome enabled the systematic forward genetic screens by Nusslein-Volhard and Wieschaus that identified the gap genes, pair-rule genes, segment polarity genes, and homeotic selector genes controlling body plan patterning. Nearly every major concept in developmental genetics — morphogen gradients, homeotic transformations, signaling pathway logic — was first established in the fly. The tools developed in Drosophila (GAL4/UAS expression system, FLP-FRT clonal analysis, balancer chromosomes) remain unmatched for genetic sophistication.

**C. elegans** contributed the concept of an invariant cell lineage: John Sulston traced every cell division from the single-cell zygote to the 959 somatic cells of the adult, creating a complete fate map. This lineage allowed the systematic identification of genes controlling cell fate decisions (including the discovery of programmed cell death by Horvitz — Nobel Prize). C. elegans was also the first animal where **RNA interference** was discovered (Fire and Mello — Nobel Prize), providing a reverse genetic tool that was rapidly adopted across biology. Its transparency enables live observation, and its simplicity (302 neurons, known connectome) makes it a powerful system for understanding how gene networks specify cell fates.

**Xenopus laevis** has been the organism of choice for studying embryonic induction and early morphogenesis because its large, accessible eggs can be microsurgically manipulated — transplanting tissue, injecting mRNA, and recombining explants. Spemann's organizer experiments were performed in salamanders (a related amphibian), and Xenopus has been the primary system for working out the molecular basis of these inductive interactions. Biochemical approaches (cell-free egg extracts for studying cell cycle regulation and DNA replication) complement the embryological tradition.

**Zebrafish** combines vertebrate biology with the experimental accessibility of an invertebrate. Transparent embryos that develop externally in 24 hours, combined with fluorescent transgenic lines, enable real-time live imaging of vertebrate development at single-cell resolution. Forward genetic screens (comparable in scale to Drosophila) have identified vertebrate-specific developmental genes, and CRISPR has made reverse genetics routine. **Mouse** remains essential as the closest model to human development and the system where gene targeting (knockouts, conditional alleles) was pioneered. Mammalian-specific features — placentation, decidualization, X-inactivation, imprinting — can only be studied in a mammalian system. Each model organism contributes unique insights, and the deepest understanding of developmental principles comes from comparing mechanisms across all of them.
