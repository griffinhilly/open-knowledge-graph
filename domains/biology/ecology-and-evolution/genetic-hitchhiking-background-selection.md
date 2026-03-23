---
id: genetic-hitchhiking-background-selection
title: Genetic Hitchhiking and Background Selection
domain: biology
course: ecology-and-evolution
prerequisites:
- id: natural-selection
  type: hard
- id: population-genetics-intro
  type: hard
- id: linkage-disequilibrium-evolutionary
  type: soft
builds-toward:
- molecular-evolution
- effective-population-size
tags:
- hitchhiking
- selection
- linkage
- variation
stage: formal-systems
status: draft
---

# Genetic Hitchhiking and Background Selection

## Core Idea
Genetic hitchhiking occurs when neutral alleles increase in frequency because they are physically linked to alleles under positive selection. Conversely, background selection reduces neutral variation when deleterious alleles are removed along with linked variation. Both processes mean that neutral evolution is not independent of linked selection.

## Questions

```yaml
- question: "A genomic study finds a region with strikingly low genetic diversity surrounding a locus that appears to have recently increased rapidly in frequency from low to near-fixation. What process most likely explains this pattern?"
  type: multiple-choice
  options:
    - "Background selection removing deleterious alleles and nearby neutral variants"
    - "A selective sweep in which a beneficial allele dragged linked neutral variants to high frequency"
    - "Random genetic drift reducing variation in a small local population"
    - "A mutation hotspot that repeatedly generates new alleles and keeps diversity low"
  answer: 1
  explanation: "The key signature of a selective sweep (genetic hitchhiking) is a 'valley' of reduced diversity centered on the rapidly selected locus. When a beneficial allele sweeps to fixation, it carries all the neutral variants physically linked to it on the same chromosomal segment — eliminating variation across that region. The rapid increase in frequency (the sweep trajectory) distinguishes this from background selection, which operates continuously and produces a more gradual, region-wide reduction in diversity without the sharp central valley. Drift alone (option C) would reduce diversity genome-wide, not create a localized pattern centered on a specific locus."

- question: "Why do genomic regions near centromeres and other areas with low recombination rates show systematically reduced neutral genetic diversity?"
  type: multiple-choice
  options:
    - "Centromeres accumulate more mutations, which are then purged by selection along with nearby variation"
    - "Low recombination means linkage disequilibrium persists longer, so both hitchhiking and background selection affect larger chromosomal regions"
    - "Centromeres are transcriptionally silenced, preventing neutral mutations from being visible to selection"
    - "Genetic drift operates more strongly near centromeres because those regions replicate later in S phase"
  answer: 1
  explanation: "Recombination is the mechanism that breaks up linkage disequilibrium — the statistical association between alleles at nearby loci. In regions with low recombination, LD persists across longer physical distances and for more generations. This means that when selection acts on one locus (either positively driving a sweep or negatively purging deleterious variants), its effect on linked neutral variation extends over a larger chromosomal neighborhood. High-recombination regions experience the same selection events but LD decays quickly, insulating neighboring neutral loci from the effect. The pattern of reduced diversity near centromeres is one of the strongest empirical signatures of linked selection in genome data."

- question: "A neutral allele can increase or decrease in frequency not because of its own properties, but solely because of selection acting on a physically linked locus in the same chromosomal region."
  type: true-false
  answer: true
  explanation: "This is the core insight of both hitchhiking and background selection: the fate of a neutral allele is not independent of linked selection. In hitchhiking, a neutral allele increases in frequency because it sits on the same chromosome segment as a beneficial allele sweeping to fixation. In background selection, neutral alleles are lost because they happen to be linked to deleterious alleles being purged by purifying selection. In both cases, the neutral allele's own selective value is zero — it is an innocent bystander to selection occurring nearby."

- question: "A neutral allele's evolutionary fate is determined solely by random genetic drift, independent of selection at other loci in the genome."
  type: true-false
  answer: false
  explanation: "This is the key misconception that hitchhiking and background selection correct. Neutral theory in its original formulation predicted that neutral alleles evolve by drift alone — but this assumes that loci evolve independently. When selection acts on a nearby locus and the two are physically linked (in linkage disequilibrium), the neutral allele's frequency changes along with the selected allele. This 'linked selection' effect is strongest in low-recombination regions and can be comparable in magnitude to drift in large populations, meaning that much of the variation we observe in neutral diversity across genomes reflects the influence of linked selection, not just drift."

- question: "Explain the conceptual difference between genetic hitchhiking and background selection, and describe the genomic signature each produces."
  type: short-answer
  answer: "Genetic hitchhiking (selective sweep) occurs when a beneficial mutation rises to fixation by positive selection and carries linked neutral alleles along, creating a localized 'valley' of reduced diversity centered on the selected site — diversity is low near the sweep and recovers with distance. Background selection occurs when deleterious alleles are continuously eliminated by purifying selection along with the neutral alleles linked to them, producing a more diffuse, region-wide reduction in neutral diversity rather than a sharp central valley. Hitchhiking is episodic and directional; background selection is ongoing and constant. Both processes reduce diversity most in regions where recombination is low, because LD persists longer and the 'footprint' of selection extends further."
  explanation: "The distinction matters for interpretation of genomic data: a sharp, localized valley of diversity with a rapid change in allele frequency at the center suggests a recent sweep; broad, gradual reduction in diversity across a chromosomal region, especially near centromeres, is more consistent with background selection. In practice both processes operate simultaneously, and distinguishing them requires population genetic modeling."
```

## Explainer

From your study of natural selection, you know that beneficial alleles increase in frequency and deleterious ones are purged. From population genetics, you know alleles at different loci can be statistically associated through **linkage disequilibrium** — they travel together on the same chromosome more often than chance predicts. Genetic hitchhiking and background selection are what happen when selection at one locus drags along neutral alleles at nearby loci, purely because of this physical linkage.

**Genetic hitchhiking** (also called a selective sweep) occurs when a new beneficial mutation arises and rapidly increases in frequency. As natural selection drives this allele toward fixation, all the neutral variants sitting on the same chromosomal segment get carried along for the ride. Imagine a crowded bus: one passenger (the beneficial allele) has a ticket to the destination, but everyone sitting nearby gets taken along whether they bought a ticket or not. The result is a region of reduced genetic variation surrounding the selected site — a "valley" of low diversity that population geneticists can detect in genomic data.

**Background selection** is the mirror image. Instead of beneficial alleles sweeping to fixation, deleterious mutations are continuously removed by purifying selection. Each time a deleterious allele is eliminated, the neutral variants linked to it on the same chromosome are lost too. This is a quieter, more constant process than hitchhiking — there is no dramatic sweep, just a steady erosion of neutral variation in regions of the genome where deleterious mutations are common and recombination is low.

Both processes share a critical implication: the fate of a neutral allele depends not just on drift and its own selective value (which is zero), but on what is happening at nearby selected loci. Regions of the genome with low recombination rates are most affected because linkage disequilibrium persists longer, giving selection more time to drag neutral variants along. This is why researchers observe that genomic regions near centromeres or in areas of low recombination consistently show reduced neutral diversity — a pattern that neither drift alone nor direct selection can explain. Understanding hitchhiking and background selection is essential for interpreting genome-wide patterns of variation and for distinguishing true targets of selection from neutral passengers.
