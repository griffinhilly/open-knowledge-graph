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
status: validated
---

# Coalescent Theory and Population History

## Core Idea
Coalescent theory models how genetic lineages trace back to common ancestors under drift and mutation. The time to coalescence depends on effective population size: larger populations have deeper ancestry. Coalescent models predict patterns of genetic diversity and allow inference of population history (size changes, admixture, selection) from DNA sequence data.

## Questions

```yaml
- question: "Two populations of the same species are analyzed using coalescent methods. Population A shows very long average branch lengths in its gene trees; Population B shows short branches and shallow coalescence times. What does this most likely suggest?"
  type: multiple-choice
  options:
    - "Population A is currently larger than Population B based on census counts"
    - "Population A has had a larger effective population size historically, giving lineages longer expected waiting times before coalescing"
    - "Population B is under strong positive selection, which accelerates the rate of coalescence"
    - "Population A has a higher mutation rate, producing more sequence divergence between lineages"
  answer: 1
  explanation: "Under the coalescent, the expected time for two lineages to coalesce is 2Ne generations. Large Ne → long waiting times → deep, long branch lengths in gene trees. Short branches in Population B indicate historically small Ne. Crucially, this reflects *historical* effective population size — a recently expanded population may still show shallow gene trees reflecting its bottlenecked past even if it is currently large. Mutation rate affects branch length scaling but is a separate issue from the coalescence time structure."

- question: "A population rapidly expanded 50,000 years ago from a very small ancestral population. Its gene tree is expected to show which characteristic pattern?"
  type: multiple-choice
  options:
    - "Long internal branches leading to many deep coalescence events, reflecting the currently large population"
    - "A star-shaped genealogy: many short terminal branches converging rapidly on a single coalescence near the time of the ancestral bottleneck"
    - "A balanced, symmetrical tree because all lineages experience the same expansion"
    - "Very high pairwise nucleotide diversity because large populations generate proportionally more mutations"
  answer: 1
  explanation: "After a rapid expansion from a bottleneck, many lineages diverged during the expansion but must all trace back through the small ancestral population, where small Ne means coalescence happens rapidly. The result is a characteristic star-shaped phylogeny: many short terminal branches (representing lineages that diverged after the expansion) converging abruptly near the bottleneck. This is a diagnostic genetic signature of past bottleneck-then-expansion history."

- question: "Under coalescent theory, two gene copies sampled from a large population are expected to coalesce (share a common ancestor) more quickly than two copies from a small population."
  type: true-false
  answer: false
  explanation: "The relationship is opposite. In any given generation, the probability that two randomly chosen copies share a common parent is 1/(2Ne). A larger Ne means a *smaller* probability of coalescence per generation, and therefore a *longer* expected waiting time: E[T₂] = 2Ne generations. Small populations coalesce quickly; large populations accumulate deep genealogies. This is why genetic diversity (which scales with 4Neμ) is higher in large populations — lineages have more time to accumulate mutations before coalescing."

- question: "A population that recently underwent rapid expansion from a bottleneck produces a 'star-shaped' genealogy with many short terminal branches."
  type: true-false
  answer: true
  explanation: "Post-bottleneck expansion generates exactly this pattern. During the bottleneck, small Ne forces rapid coalescence — lineages merge quickly. After the expansion, many lineages persist for a long time before the sample is collected, accumulating mutations along short terminal branches. The many branches from the expansion all converge abruptly at the bottleneck, producing the star shape. This contrasts with a population of stable large size, which shows a more gradual, tree-like coalescence with variation in branch lengths."

- question: "Why does coalescent theory work backward in time rather than forward, and what advantage does this provide for analyzing DNA sequence data?"
  type: short-answer
  answer: "Coalescent theory works backward because it focuses only on the lineages present in the current sample, ignoring the vast majority of ancestral lineages that left no modern descendants. A forward-time population genetics model must track all individuals in every generation — computationally intractable for large populations. By starting with the sample and tracing lineages backward as they merge into common ancestors, the coalescent tracks only k lineages (the sample size), merging them in pairs. This makes the framework tractable regardless of population size, and it naturally generates predictions about the patterns of genetic variation in the sample — pairwise diversity, site frequency spectra, gene tree shapes — that can be directly compared to observed DNA sequence data to infer population history."
  explanation: "The efficiency gain is fundamental: the coalescent 'prunes' the genealogical tree to include only the branches relevant to explaining the data. This backward perspective also makes it natural to ask 'given this sample, what population history is most consistent with it?' — which is the statistical inference question we actually want to answer."
```

## Explainer

Traditional population genetics works forward in time: you start with a population, apply forces like mutation, drift, and selection, and predict how allele frequencies change generation by generation. **Coalescent theory** inverts this perspective entirely — it starts with a sample of present-day gene copies and traces their ancestry backward in time until they merge into common ancestors. This backward-looking approach turns out to be far more powerful for analyzing DNA sequence data, because it focuses only on the lineages that actually contributed to your sample, ignoring the vast majority of ancestral copies that left no modern descendants.

The core intuition is simple. Take two gene copies sampled from a population of effective size *N*<sub>e</sub> (a concept you already know from studying effective population size). In any given past generation, those two copies either came from the same parental copy — a **coalescence event** — or from different ones. In a diploid population, the probability that two randomly chosen copies share a parent in the previous generation is 1/(2*N*<sub>e</sub>). This means the expected time to coalescence for two lineages is 2*N*<sub>e</sub> generations. For larger samples, lineages coalesce in pairs, building a branching **gene tree** whose shape and branch lengths encode the population's demographic history. The key insight is that the waiting time between coalescence events depends directly on population size: large populations mean long waits (deep branches), small populations mean short waits (shallow branches).

This framework generates testable predictions about genetic diversity. Under a constant-sized, neutral population, coalescent theory predicts that the expected number of nucleotide differences between two sequences (pairwise diversity) is proportional to 4*N*<sub>e</sub>*μ*, where *μ* is the per-generation mutation rate. The shape of the gene tree also carries information: a population that expanded rapidly produces a **star-shaped genealogy** with many short terminal branches (because many lineages coexist for a long time before coalescing), while a population bottleneck produces a tree with long internal branches (lineages coalesce quickly when the population was small). By comparing observed patterns of genetic variation against coalescent predictions, researchers can infer whether a population has grown, shrunk, split, or mixed — all from a DNA sample collected today.

Modern applications extend the basic coalescent in several directions. The **structured coalescent** models populations subdivided into demes connected by migration, predicting how geographic structure shapes gene trees. **Coalescent with recombination** accounts for the fact that different segments of the genome may have different genealogies because recombination shuffles ancestral lineages. Bayesian coalescent methods (like BEAST and PSMC) fit complex demographic models to whole-genome data, reconstructing population size changes over hundreds of thousands of years. Coalescent theory has become the statistical backbone of population genomics, connecting the probability theory you know from conditional probability to the biological realities of ancestry, drift, and mutation in finite populations.
