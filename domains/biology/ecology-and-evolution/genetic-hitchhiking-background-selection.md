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

## Explainer

From your study of natural selection, you know that beneficial alleles increase in frequency and deleterious ones are purged. From population genetics, you know alleles at different loci can be statistically associated through **linkage disequilibrium** — they travel together on the same chromosome more often than chance predicts. Genetic hitchhiking and background selection are what happen when selection at one locus drags along neutral alleles at nearby loci, purely because of this physical linkage.

**Genetic hitchhiking** (also called a selective sweep) occurs when a new beneficial mutation arises and rapidly increases in frequency. As natural selection drives this allele toward fixation, all the neutral variants sitting on the same chromosomal segment get carried along for the ride. Imagine a crowded bus: one passenger (the beneficial allele) has a ticket to the destination, but everyone sitting nearby gets taken along whether they bought a ticket or not. The result is a region of reduced genetic variation surrounding the selected site — a "valley" of low diversity that population geneticists can detect in genomic data.

**Background selection** is the mirror image. Instead of beneficial alleles sweeping to fixation, deleterious mutations are continuously removed by purifying selection. Each time a deleterious allele is eliminated, the neutral variants linked to it on the same chromosome are lost too. This is a quieter, more constant process than hitchhiking — there is no dramatic sweep, just a steady erosion of neutral variation in regions of the genome where deleterious mutations are common and recombination is low.

Both processes share a critical implication: the fate of a neutral allele depends not just on drift and its own selective value (which is zero), but on what is happening at nearby selected loci. Regions of the genome with low recombination rates are most affected because linkage disequilibrium persists longer, giving selection more time to drag neutral variants along. This is why researchers observe that genomic regions near centromeres or in areas of low recombination consistently show reduced neutral diversity — a pattern that neither drift alone nor direct selection can explain. Understanding hitchhiking and background selection is essential for interpreting genome-wide patterns of variation and for distinguishing true targets of selection from neutral passengers.
