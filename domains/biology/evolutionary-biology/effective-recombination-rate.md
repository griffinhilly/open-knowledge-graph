---
id: effective-recombination-rate
title: Effective Recombination Rate and Linked Selection
domain: biology
course: evolutionary-biology
prerequisites:
- id: recombination-evolution
  type: hard
- id: efficacy-selection-finite-populations
  type: hard
- id: linkage-disequilibrium-evolutionary
  type: hard
builds-toward:
- molecular-evolution-rates
tags:
- recombination
- linked-selection
- efficacy
- evolution
stage: advanced
status: draft
---

# Effective Recombination Rate and Linked Selection

## Core Idea
The effective recombination rate experienced by a locus depends on local recombination and linkage to other sites under selection. Even modest recombination is reduced effective when linked to many selected sites, reducing efficacy of selection genome-wide.

## Explainer

From your study of recombination in evolution and linkage disequilibrium, you know that recombination breaks apart associations between alleles at different loci, allowing natural selection to act on each variant more independently. The **effective recombination rate** is the rate at which recombination actually succeeds in decoupling a focal locus from its genomic neighborhood — and it is often much lower than the raw, physical recombination rate would suggest.

The physical recombination rate tells you how often crossovers occur between two positions on a chromosome during meiosis. But a crossover only matters evolutionarily if it separates alleles that are in linkage disequilibrium — alleles whose association affects their joint fate under selection. If a neutral mutation sits in a genomic region where many neighboring sites are under selection (either positive or purifying), selection on those neighbors drags the neutral variant along for the ride. This **linked selection** effect means that even though crossovers may be occurring at the normal physical rate, the focal locus behaves as if recombination were much rarer, because selection at linked sites keeps regenerating the associations that recombination tries to break down.

Two specific forms of linked selection drive this reduction. **Background selection** occurs when purifying selection continuously removes deleterious mutations and, with them, any neutral variants that happen to sit on the same haplotype. This reduces the effective population size experienced by neutral loci in low-recombination regions, which from your understanding of selection efficacy in finite populations means that drift becomes stronger and selection on weakly beneficial mutations becomes less effective. **Selective sweeps** occur when a strongly beneficial mutation rises to fixation, carrying with it a swath of linked neutral variation — a "hitchhiking" event that locally eliminates diversity and linkage disequilibrium. In regions where sweeps occur frequently, the effective recombination rate drops because new associations are constantly being created and driven to fixation faster than recombination can dismantle them.

The practical consequences are visible across genomes. Regions of low recombination — near centromeres, on sex chromosomes, or in chromosomal inversions — consistently show lower genetic diversity, higher linkage disequilibrium, and a greater accumulation of slightly deleterious mutations than high-recombination regions. This pattern, observed across species from *Drosophila* to humans, confirms that effective recombination rate, not just physical recombination rate, determines how efficiently selection can operate. For evolutionary biology, this means that genome architecture — where recombination hotspots and coldspots fall — shapes the distribution of adaptive and deleterious variation, influencing everything from the rate of molecular evolution to the long-term fate of non-recombining genomic regions like Y chromosomes.
