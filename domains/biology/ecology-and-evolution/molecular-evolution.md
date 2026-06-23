---
id: molecular-evolution
title: Molecular Evolution and Molecular Clocks
domain: biology
course: ecology-and-evolution
prerequisites:
- id: dna-mutations
  type: hard
- id: phylogenetics-intro
  type: hard
- id: genetic-drift
  type: soft
- id: hardy-weinberg-equilibrium
  type: soft
- id: cladistics-and-systematics
  type: soft
builds-toward: []
tags:
- molecular-clock
- neutral-theory
- sequence-divergence
- substitution
stage: formal-systems
status: validated
---
# Molecular Evolution and Molecular Clocks

## Core Idea
Molecular evolution studies changes in DNA, RNA, and protein sequences over evolutionary time. The neutral theory of molecular evolution proposes that most molecular variation is selectively neutral, with substitution rates governed by mutation rates rather than selection. Molecular clocks exploit the approximately constant rate of neutral substitutions to date divergence events when calibrated against the fossil record. Synonymous (silent) substitutions accumulate faster than nonsynonymous (amino-acid-changing) ones under purifying selection.

## How It's Best Learned
Calculate pairwise sequence divergence between homologous genes in related species and use a known calibration point to estimate divergence time. Compare synonymous vs. nonsynonymous substitution rates (dN/dS) to infer whether a gene is under purifying selection, neutral drift, or positive selection.

## Common Misconceptions
- Molecular clocks are not perfectly constant — rate variation among lineages and sites requires careful calibration.
- Most mutations are not neutral; negative (purifying) selection removes many, while molecular clock analysis focuses on those that are.

## Questions

```yaml
- question: "A gene is found to have a dN/dS ratio of 3.2, where dN is the rate of nonsynonymous substitutions and dS is the rate of synonymous substitutions. What does this indicate?"
  type: multiple-choice
  options: ["The gene is under strong purifying selection", "The gene is evolving neutrally", "The gene is under positive (diversifying) selection", "The gene has a higher-than-average mutation rate"]
  answer: 2
  explanation: "Under purifying selection, harmful nonsynonymous changes are removed, so dN < dS and dN/dS < 1. Under strict neutrality, dN ≈ dS and dN/dS ≈ 1. A dN/dS ratio > 1 means nonsynonymous substitutions are accumulating faster than synonymous ones — more amino acid changes are being fixed than expected by chance alone, indicating that natural selection is actively favoring protein sequence change. This is the signature of positive selection."

- question: "Molecular clocks provide a reliable, constant rate of DNA substitution that can be used to date divergence events without any external calibration."
  type: true-false
  answer: false
  explanation: "Molecular clocks are not perfectly constant — substitution rates vary across lineages (due to differences in generation time, metabolic rate, and population size) and across sites within a gene. Reliable molecular clock estimates require calibration using at least one independently dated event, typically from the fossil record or a geological event (e.g., a land bridge formation). Uncalibrated clocks can produce divergence estimates that are off by tens of millions of years."

- question: "Explain why synonymous substitutions accumulate faster than nonsynonymous substitutions in most protein-coding genes."
  type: short-answer
  answer: "Synonymous (silent) substitutions change the DNA sequence but not the amino acid sequence of the encoded protein, due to redundancy in the genetic code. Because they do not alter protein function, they are largely invisible to natural selection and accumulate at a rate close to the mutation rate. Nonsynonymous substitutions change the amino acid sequence and therefore affect protein structure and function. Most such changes are harmful and are removed by purifying selection before they can spread through the population, reducing the observed substitution rate. Only rarely do nonsynonymous changes improve fitness and get fixed."
  explanation: "This question connects to the neutral theory: the substitution rate equals the mutation rate only for truly neutral changes. Synonymous substitutions approximate neutrality because the protein is unchanged. Most nonsynonymous substitutions are subject to selection — usually negative — which slows their fixation rate far below the underlying mutation rate. The dN/dS ratio formalizes this comparison and is one of the most widely used tests for natural selection at the molecular level."
```

## Explainer

When you study DNA mutations, you learn about the kinds of changes that can occur in a sequence — substitutions, insertions, deletions. Molecular evolution asks a deeper question: of all the mutations that arise, which ones actually spread through populations and persist over evolutionary time, and at what rate? The answers reveal both the forces shaping genome evolution and a surprisingly precise way to tell time using DNA.

The **neutral theory of molecular evolution**, proposed by Motoo Kimura in the late 1960s, was initially controversial but is now central to molecular biology. The key claim is that the vast majority of DNA sequence differences between species are not driven by natural selection — they are selectively neutral, having neither a beneficial nor a harmful effect on the organism. Under neutral theory, the rate at which neutral mutations spread through a population (the substitution rate) equals the mutation rate, regardless of population size. This is because neutral mutations fix by genetic drift alone.

This leads directly to the **molecular clock** concept. If neutral substitutions accumulate at a roughly constant rate over time, then the number of sequence differences between two species is proportional to the time since their common ancestor. Calibrate that rate against a known divergence event (from the fossil record, for example), and you can estimate when any two lineages split. In practice, rates vary across lineages and sites, so modern molecular dating uses sophisticated statistical models that account for rate variation — but the core logic remains.

A key analytical tool is the **dN/dS ratio**: the rate of nonsynonymous substitutions (those that change the amino acid) divided by the rate of synonymous substitutions (those that do not, due to genetic code redundancy). Synonymous substitutions are largely neutral and accumulate close to the mutation rate. Nonsynonymous substitutions usually affect protein function, so most are harmful and are removed by purifying selection, making dN < dS and dN/dS < 1 for most genes. When dN/dS ≈ 1, the gene appears to be evolving neutrally. When dN/dS > 1, amino acid changes are spreading faster than expected by chance — a signature of **positive selection**, meaning the protein is adaptively changing. This ratio is one of the most powerful tools for identifying genes that are under selection in genome-wide studies.
