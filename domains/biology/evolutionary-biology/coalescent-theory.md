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

## Questions

```yaml
- question: "Two researchers study the same population. Researcher A simulates all 10,000 individuals forward for 1,000 generations. Researcher B uses the coalescent to trace the ancestry of 50 sampled gene copies backward in time. Which claim about Researcher B's approach is most accurate?"
  type: multiple-choice
  options:
    - "Researcher B's approach is less accurate because it ignores most individuals in the population"
    - "Researcher B's approach is more computationally efficient because it models only the ancestry of the actual sample, discarding irrelevant lineages"
    - "Researcher B's approach requires knowing the full genealogy of all 10,000 individuals before it can begin"
    - "Researcher B's approach is only valid if the population has constant size over time"
  answer: 1
  explanation: "The computational power of coalescent theory is that it ignores the vast majority of individuals in the population who left no ancestors in the current sample. Forward simulations must track all individuals; most of their lineages die out before the present and contribute nothing to the sample's genealogy. The coalescent skips all that wasted computation, modeling only the ancestry of the sampled genes. This is not a loss of accuracy — it is a more efficient parameterization of the same probability model."

- question: "A population experienced a severe bottleneck (dramatic reduction in size) several thousand generations ago. What signature in the gene tree of a present-day sample would indicate this bottleneck?"
  type: multiple-choice
  options:
    - "Long, evenly spaced branches throughout the tree indicating slow, steady coalescence at all times"
    - "A burst of coalescent events concentrated in the period of small population size, with most lineages merging during that narrow window"
    - "No effect — coalescence rate depends only on sample size, not effective population size"
    - "Lineages that fail to coalesce at all, creating an unresolved polytomy at the root"
  answer: 1
  explanation: "Coalescence rate is k(k−1)/(4Ne): when Ne is small, lineages coalesce rapidly. A bottleneck creates a narrow window of very small Ne through which many lineages must pass, causing a burst of coalescent events clustered in time. This is visible in the gene tree as a star-like cluster of nodes at the depth corresponding to the bottleneck. A population expansion has the opposite signature: lineages persist independently for many generations, producing a tree with many long, parallel branches that coalesce only near the root."

- question: "In coalescent theory, the expected time for two randomly sampled gene copies to coalesce to their common ancestor increases with effective population size (Ne)."
  type: true-false
  answer: true
  explanation: "The probability that two gene copies coalesce in a single generation is 1/(2Ne). The expected waiting time is 2Ne generations. A larger population means any two copies are less likely to share the same parent in any given generation, so coalescence takes longer on average. This is the direct connection between Ne and the branch lengths in gene trees — larger populations produce longer branches and more ancient common ancestors."

- question: "Coalescent theory traces the evolution of an entire population forward in time, predicting which lineages will survive to the present generation."
  type: true-false
  answer: false
  explanation: "This describes forward-time population simulation, which is the opposite of coalescent theory. Coalescent theory starts from a sample of present-day gene copies and traces their ancestry *backward* in time until all lineages converge on a single common ancestor (the MRCA). By reversing the direction of time, it avoids simulating the many lineages in the population that are irrelevant to the sample, making it dramatically more efficient for inference from genetic data."

- question: "Why is coalescent theory especially efficient for analyzing genomic data compared to forward-time population simulations?"
  type: short-answer
  answer: "Forward-time simulation must track every individual in the population through every generation, even though most lineages are irrelevant to the sample eventually observed. Coalescent theory focuses only on the ancestry of the sampled gene copies, modeling their genealogy backward in time and ignoring all population members who left no descendants in the sample. For large populations (Ne = millions) over many generations, this reduces computational cost by orders of magnitude. Additionally, the coalescent directly parameterizes the quantities of interest — coalescence times and tree topology — in terms of population genetic parameters (Ne, migration rates), making it ideal for statistical inference."
  explanation: "The key insight is that the coalescent is not an approximation — it is the exact probability distribution over genealogies of a sample, just computed from the sample's perspective rather than the population's perspective. The efficiency gain comes from discarding irrelevant lineages, not from sacrificing precision."
```

## Explainer

Most of population genetics works forward in time: you start with a population, apply selection, drift, and mutation, and predict what the gene pool looks like in the future. Coalescent theory inverts this perspective entirely. Instead of simulating an entire population forward, you start with a sample of gene copies observed today and trace their ancestry **backward in time** until they converge on a single common ancestor. This backward-looking approach turns out to be enormously more efficient and powerful for analyzing genetic data.

The core logic builds on genetic drift, which you already understand. In a finite population of effective size Ne, each gene copy in the current generation was randomly drawn from the previous generation. If you pick two gene copies from the present, there is a probability of 1/(2Ne) that they were copied from the same parental gene copy in the previous generation — that is, that they **coalesce** one generation back. If they did not coalesce, you look back another generation, and another, each time with the same probability. The waiting time until two lineages coalesce follows a geometric distribution (approximated by an **exponential distribution** with rate 1/(2Ne), connecting to your probability prerequisites). For a sample of k lineages, any pair can coalesce, so the rate increases combinatorially: with k lineages, there are k(k-1)/2 possible pairs, and the total coalescence rate is k(k-1)/(4Ne). This means the first coalescent event in a large sample happens quickly, and the last two lineages take the longest to merge — the tree is characteristically long-branched near its root.

The resulting **gene tree** — the genealogical tree of the sampled gene copies — encodes information about the population's history. In a large population, coalescent events are spread over many generations, producing a tree with long branches. In a small population, lineages coalesce rapidly, producing a compact tree. If the population experienced a bottleneck, many lineages coalesce in the narrow window of small size, creating a burst of coalescent events. A population expansion produces the opposite pattern: lineages persist independently for a long time. By fitting coalescent models to the shapes and branch lengths of gene trees reconstructed from DNA sequence data, researchers can **infer demographic history** — estimating past population sizes, timing of bottlenecks, and rates of migration between populations.

What makes coalescent theory transformative is its computational efficiency and its natural connection to data. Simulating an entire population of millions forward through thousands of generations is computationally expensive and wasteful — most lineages in the population are irrelevant to the sample you actually sequenced. The coalescent ignores all those irrelevant lineages and models only the ancestry of your sample, dramatically reducing computational cost. This efficiency has made coalescent-based methods the standard framework for population genetic inference, phylogeography, and demographic reconstruction from genomic data.
