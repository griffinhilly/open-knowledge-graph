---
id: purifying-selection
title: Purifying Selection and Deleterious Mutation Removal
domain: biology
course: evolutionary-biology
prerequisites:
- id: natural-selection
  type: hard
- id: selection-coefficient
  type: hard
- id: population-genetics-intro
  type: soft
builds-toward:
- mutation-selection-balance
- efficacy-selection-finite-populations
tags:
- selection
- constraint
- molecular-evolution
- fitness
stage: advanced
status: draft
---

# Purifying Selection and Deleterious Mutation Removal

## Core Idea
Purifying selection removes or reduces frequency of deleterious mutations by eliminating individuals carrying them. Explains why functional regions of genomes evolve slowly compared to neutral sites.

## Explainer

You already know from your study of natural selection that individuals with higher fitness leave more offspring, and from the selection coefficient that the magnitude of a fitness difference determines how quickly allele frequencies change. **Purifying selection** (also called **negative selection**) is the most pervasive form of natural selection in molecular evolution, but it works by removing rather than promoting — it eliminates harmful mutations before they can spread.

Consider a protein that performs an essential function, like hemoglobin carrying oxygen. Most random amino acid changes to this protein will disrupt its structure or function, reducing the organism's fitness. When such a **deleterious mutation** arises, individuals carrying it tend to survive less well or reproduce less successfully than those with the functional version. Over generations, the mutant allele is driven to low frequency or eliminated entirely. This is purifying selection in action: not favoring a new beneficial variant, but policing against damage to something that already works.

The signature of purifying selection is **evolutionary constraint** — functional sequences evolve more slowly than expected under neutrality. Compare the substitution rate of a critical enzyme's active site to a nearby stretch of junk DNA: the junk DNA accumulates mutations freely because changes there have no fitness consequence, while the active site remains nearly frozen across millions of years because almost every mutation there is deleterious and gets removed. The strength of purifying selection is quantified by the selection coefficient (s): a mutation with s = −0.01 reduces fitness by 1%, which in a large population is more than enough for selection to efficiently eliminate it. However, in small populations, drift can overpower weak purifying selection, allowing mildly deleterious mutations to drift to fixation — a critical interaction between drift and selection that shapes genome evolution.

Purifying selection explains several major patterns in comparative genomics. Protein-coding genes evolve slower than intergenic regions. First and second codon positions (which usually change the amino acid) evolve slower than third positions (which often don't). Regulatory elements critical for gene expression are conserved across species separated by hundreds of millions of years. Whenever you see a stretch of DNA that is more conserved than its surroundings, purifying selection is the most likely explanation — the sequence is doing something important, and mutations that break it are being culled. This logic underlies one of the most powerful tools in genomics: identifying functional elements by their evolutionary conservation.
