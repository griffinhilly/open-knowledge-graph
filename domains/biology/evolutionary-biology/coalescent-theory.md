---
id: coalescent-theory
title: Coalescent Theory
domain: biology
course: evolutionary-biology
prerequisites:
- id: genetic-drift
  type: hard
- id: probability-axioms
  type: hard
- id: exponential-distribution
  type: soft
builds-toward:
- demographic-inference
- molecular-dating
tags:
- population-genetics
- theory
- molecular
stage: advanced
status: draft
---

# Coalescent Theory

## Core Idea
Coalescent theory models the genealogy of a sample of genes, tracing lineages backward in time to their common ancestor. The theory predicts that expected time to coalescence depends on effective population size (Ne) and provides a framework for inferring past population sizes, divergence times, and gene flow from sequence data.

## Explainer

Most of population genetics works forward in time: you start with a population, apply selection, drift, and mutation, and predict what the gene pool looks like in the future. Coalescent theory inverts this perspective entirely. Instead of simulating an entire population forward, you start with a sample of gene copies observed today and trace their ancestry **backward in time** until they converge on a single common ancestor. This backward-looking approach turns out to be enormously more efficient and powerful for analyzing genetic data.

The core logic builds on genetic drift, which you already understand. In a finite population of effective size Ne, each gene copy in the current generation was randomly drawn from the previous generation. If you pick two gene copies from the present, there is a probability of 1/(2Ne) that they were copied from the same parental gene copy in the previous generation — that is, that they **coalesce** one generation back. If they did not coalesce, you look back another generation, and another, each time with the same probability. The waiting time until two lineages coalesce follows a geometric distribution (approximated by an **exponential distribution** with rate 1/(2Ne), connecting to your probability prerequisites). For a sample of k lineages, any pair can coalesce, so the rate increases combinatorially: with k lineages, there are k(k-1)/2 possible pairs, and the total coalescence rate is k(k-1)/(4Ne). This means the first coalescent event in a large sample happens quickly, and the last two lineages take the longest to merge — the tree is characteristically long-branched near its root.

The resulting **gene tree** — the genealogical tree of the sampled gene copies — encodes information about the population's history. In a large population, coalescent events are spread over many generations, producing a tree with long branches. In a small population, lineages coalesce rapidly, producing a compact tree. If the population experienced a bottleneck, many lineages coalesce in the narrow window of small size, creating a burst of coalescent events. A population expansion produces the opposite pattern: lineages persist independently for a long time. By fitting coalescent models to the shapes and branch lengths of gene trees reconstructed from DNA sequence data, researchers can **infer demographic history** — estimating past population sizes, timing of bottlenecks, and rates of migration between populations.

What makes coalescent theory transformative is its computational efficiency and its natural connection to data. Simulating an entire population of millions forward through thousands of generations is computationally expensive and wasteful — most lineages in the population are irrelevant to the sample you actually sequenced. The coalescent ignores all those irrelevant lineages and models only the ancestry of your sample, dramatically reducing computational cost. This efficiency has made coalescent-based methods the standard framework for population genetic inference, phylogeography, and demographic reconstruction from genomic data.
