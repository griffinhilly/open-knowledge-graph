---
id: neutral-theory-molecular
title: Neutral Theory of Molecular Evolution
domain: biology
course: evolutionary-biology
prerequisites:
- id: molecular-evolution
  type: hard
- id: population-genetics-intro
  type: hard
builds-toward:
- molecular-clock-hypothesis
- synonymous-nonsynonymous-substitutions
tags:
- molecular-evolution
- neutral-evolution
- population-genetics
stage: advanced
status: draft
---

# Neutral Theory of Molecular Evolution

## Core Idea
Kimura's neutral theory proposes that most molecular sequence variation and substitutions are neutral and evolve primarily by genetic drift rather than natural selection. The theory predicts that substitution rates depend only on mutation rates and that nucleotide diversity is determined by population size and mutation rate (μ = 4Neμ).

## Explainer

From your study of molecular evolution and population genetics, you understand that mutations arise constantly and that genetic drift causes random fluctuations in allele frequencies — fluctuations that are strongest in small populations. Motoo Kimura's **neutral theory of molecular evolution**, proposed in 1968, builds on these foundations with a surprising claim: the vast majority of mutations that become fixed in a population's DNA are not beneficial. They are selectively **neutral** — neither helping nor harming the organism — and they spread through populations by drift alone.

The mathematical elegance of the neutral theory comes from a key derivation. In a diploid population of effective size Ne, a new neutral mutation has a fixation probability of 1/(2Ne). Since there are 2Ne gene copies in the population and each mutates at rate μ per generation, the total number of new neutral mutations entering the population per generation is 2Ne × μ. Multiply the input rate by the fixation probability: 2Neμ × 1/(2Ne) = μ. The **substitution rate for neutral mutations equals the mutation rate**, regardless of population size. This is a profound result — it means the molecular clock ticks at a rate determined only by mutation, not by how large or small the population is.

The neutral theory does not claim that natural selection is unimportant for organismal evolution — it absolutely is. Rather, it claims that at the molecular level, most of the variation you observe (polymorphism within species) and most of the divergence you measure (substitutions between species) involves mutations with negligible fitness effects. Strongly deleterious mutations are removed by purifying selection and never contribute to divergence. Strongly beneficial mutations do fix by positive selection, but they are rare. The great middle ground — slightly deleterious to truly neutral mutations — dominates the molecular landscape.

The neutral theory provides a **null model** for molecular evolution, much like Hardy-Weinberg equilibrium provides a null model for population genetics. When you observe that a gene evolves faster or slower than the neutral prediction, that deviation is informative: faster substitution suggests positive selection driving change, while slower substitution reveals purifying selection constraining the sequence. Without the neutral baseline, you would have no framework for detecting selection from sequence data. The theory also predicts that nucleotide diversity within a population (θ) should equal 4Neμ, linking observable genetic variation directly to population size and mutation rate — a relationship that remains central to modern population genomics.
