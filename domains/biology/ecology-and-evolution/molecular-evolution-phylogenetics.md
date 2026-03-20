---
id: molecular-evolution-phylogenetics
title: Molecular Evolution and Phylogenetic Inference
domain: biology
course: ecology-and-evolution
prerequisites:
- id: molecular-evolution
  type: hard
- id: phylogenetics-intro
  type: soft
- id: dna-sequence-divergence
  type: soft
builds-toward:
- extinction-rates-phylogenetic-patterns
tags:
- molecular-evolution
- phylogenetics
- molecular-clock
- neutral-theory
stage: advanced
status: draft
---

# Molecular Evolution and Phylogenetic Inference

## Core Idea
DNA and protein sequences accumulate mutations over time, allowing inference of evolutionary relationships and divergence times. The molecular clock hypothesis proposes mutations accumulate at relatively constant rates, enabling dating. Phylogenetic methods (parsimony, likelihood, Bayesian) reconstruct evolutionary trees. Most nucleotide evolution is neutral.

## Explainer

From your study of molecular evolution, you know that DNA sequences change over time through mutation, and that most of these changes are selectively neutral — they neither help nor harm the organism. From phylogenetics, you know that shared derived characters can reveal which species are more closely related. Molecular evolution and phylogenetics fuse these ideas: instead of comparing bones or body plans, we compare DNA and protein sequences directly, using the accumulated differences as a record of evolutionary history written in the genome itself.

The central concept is the **molecular clock**. If neutral mutations accumulate at a roughly constant rate per generation, then the number of sequence differences between two species is proportional to the time since they diverged from a common ancestor. Compare the hemoglobin gene in humans and mice: the more substitutions you count, the longer ago those lineages split. Calibrate the clock using a fossil with a known date — say, the oldest primate fossil at 55 million years — and you can estimate divergence times for lineages that left no fossils at all. The clock is not perfectly constant (rates vary across genes, lineages, and time periods), but statistical models can account for this variation, making molecular dating a powerful complement to the fossil record.

**Phylogenetic inference** uses sequence data to reconstruct the branching pattern of evolution — the tree of life. Three major approaches compete. **Parsimony** finds the tree requiring the fewest total mutations, appealing in its simplicity but sometimes misleading when mutation rates vary across branches. **Maximum likelihood** evaluates which tree best explains the observed sequences under an explicit model of how DNA evolves (including different rates for transitions versus transversions, or variation across sites). **Bayesian methods** extend likelihood by incorporating prior information and producing probability distributions over possible trees rather than a single best estimate. All three approaches align sequences, compare them position by position, and search the vast space of possible tree topologies for the one that best fits the data.

A key insight from this field is that most molecular evolution is **neutral** — the majority of substitutions that accumulate between species were invisible to natural selection. This is not a statement that most mutations are unimportant; rather, it means that the mutations which persist long enough to be observed in species comparisons are overwhelmingly ones that had no fitness effect. Strongly deleterious mutations are removed by selection before they can spread, and strongly beneficial ones are rare. The neutral background provides the steady tick of the molecular clock, while departures from neutrality — genes evolving faster or slower than expected — flag regions under positive or purifying selection, revealing where adaptation has left its molecular signature.
