---
id: coalescent-theory-population
title: Coalescent Theory and Population History
domain: biology
course: evolutionary-biology
prerequisites:
- id: effective-population-size
  type: hard
- id: conditional-probability
  type: soft
tags:
- coalescent-theory
- population-history
- genetic-diversity
- ancestry
stage: advanced
status: draft
---

# Coalescent Theory and Population History

## Core Idea
Coalescent theory models how genetic lineages trace back to common ancestors under drift and mutation. The time to coalescence depends on effective population size: larger populations have deeper ancestry. Coalescent models predict patterns of genetic diversity and allow inference of population history (size changes, admixture, selection) from DNA sequence data.

## Explainer

Traditional population genetics works forward in time: you start with a population, apply forces like mutation, drift, and selection, and predict how allele frequencies change generation by generation. **Coalescent theory** inverts this perspective entirely — it starts with a sample of present-day gene copies and traces their ancestry backward in time until they merge into common ancestors. This backward-looking approach turns out to be far more powerful for analyzing DNA sequence data, because it focuses only on the lineages that actually contributed to your sample, ignoring the vast majority of ancestral copies that left no modern descendants.

The core intuition is simple. Take two gene copies sampled from a population of effective size *N*<sub>e</sub> (a concept you already know from studying effective population size). In any given past generation, those two copies either came from the same parental copy — a **coalescence event** — or from different ones. In a diploid population, the probability that two randomly chosen copies share a parent in the previous generation is 1/(2*N*<sub>e</sub>). This means the expected time to coalescence for two lineages is 2*N*<sub>e</sub> generations. For larger samples, lineages coalesce in pairs, building a branching **gene tree** whose shape and branch lengths encode the population's demographic history. The key insight is that the waiting time between coalescence events depends directly on population size: large populations mean long waits (deep branches), small populations mean short waits (shallow branches).

This framework generates testable predictions about genetic diversity. Under a constant-sized, neutral population, coalescent theory predicts that the expected number of nucleotide differences between two sequences (pairwise diversity) is proportional to 4*N*<sub>e</sub>*μ*, where *μ* is the per-generation mutation rate. The shape of the gene tree also carries information: a population that expanded rapidly produces a **star-shaped genealogy** with many short terminal branches (because many lineages coexist for a long time before coalescing), while a population bottleneck produces a tree with long internal branches (lineages coalesce quickly when the population was small). By comparing observed patterns of genetic variation against coalescent predictions, researchers can infer whether a population has grown, shrunk, split, or mixed — all from a DNA sample collected today.

Modern applications extend the basic coalescent in several directions. The **structured coalescent** models populations subdivided into demes connected by migration, predicting how geographic structure shapes gene trees. **Coalescent with recombination** accounts for the fact that different segments of the genome may have different genealogies because recombination shuffles ancestral lineages. Bayesian coalescent methods (like BEAST and PSMC) fit complex demographic models to whole-genome data, reconstructing population size changes over hundreds of thousands of years. Coalescent theory has become the statistical backbone of population genomics, connecting the probability theory you know from conditional probability to the biological realities of ancestry, drift, and mutation in finite populations.
