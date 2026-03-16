---
id: inbreeding-consequences
title: Inbreeding Depression and Coefficient of Inbreeding
domain: biology
course: evolutionary-biology
prerequisites:
- id: population-genetics-intro
  type: hard
- id: effective-population-size
  type: hard
tags:
- inbreeding
- genetic-load
- fitness
- conservation
stage: advanced
status: draft
---

# Inbreeding Depression and Coefficient of Inbreeding

## Core Idea
Inbreeding increases homozygosity, exposing recessive deleterious alleles and reducing overall fitness in inbreeding depression. The coefficient of inbreeding (F) quantifies the probability that two alleles are identical by descent. Small populations experience unavoidable inbreeding, which is a major concern in conservation biology and breeding programs.

## How It's Best Learned
Draw pedigrees and calculate inbreeding coefficients. Compare fitness loss across generations in small populations and in laboratory experiments.

## Common Misconceptions
- Inbreeding itself is harmful; it reveals the genetic load (deleterious recessive alleles) that was hidden in heterozygotes.
- Only animals experience inbreeding depression; plants with self-fertilization and clonal organisms also show strong depression.

## Explainer

Every individual carries a hidden burden of **deleterious recessive alleles** — mutations that reduce fitness but remain masked in heterozygotes because one functional copy of the gene is enough. In large, randomly mating populations, most individuals are heterozygous at these loci, and the harmful alleles stay invisible. Inbreeding changes this equation. When relatives mate, they share recent common ancestors, which means they are likely to carry copies of the same alleles inherited from those ancestors. Their offspring therefore have a much higher chance of receiving two identical copies — becoming homozygous — and when both copies are the broken version, the deleterious phenotype appears. This is **inbreeding depression**: the decline in average fitness that accompanies increased homozygosity.

The **coefficient of inbreeding (F)** puts a number on this risk. F measures the probability that the two alleles at any given locus in an individual are **identical by descent** — that is, both are physical copies of the same ancestral allele, not just the same variant by coincidence. For the offspring of first cousins, F = 1/16; for offspring of siblings, F = 1/4. You calculate F by tracing paths through the pedigree from one parent up to each common ancestor and back down to the other parent, counting the number of transmission steps. Each path contributes (1/2)^n to F, where n is the number of links in the path. If you studied effective population size, you'll recognize that F also rises predictably in small populations even without deliberate inbreeding — genetic drift forces alleles to fixation, and the average F across the population increases by approximately 1/(2Nₑ) each generation.

The practical consequences are severe. Inbred individuals show reduced survival, lower fertility, weaker immune function, and greater susceptibility to disease — effects documented across animals, plants, and fungi. In conservation biology, small endangered populations face an **extinction vortex** where declining numbers increase inbreeding, which reduces fitness, which further shrinks the population. Programs that manage captive breeding or reintroduction carefully track pedigrees and F values to minimize relatedness between mating pairs.

A crucial nuance is that inbreeding itself does not create harmful alleles — it merely exposes the **genetic load** that was already present but hidden in heterozygotes. A population that has been small for many generations may have already purged its most severely deleterious recessives through selection, because those alleles were repeatedly exposed to selection in homozygous form. This is why some naturally inbreeding species, like certain self-fertilizing plants, tolerate high F values with minimal depression. The severity of inbreeding depression depends on the population's history, the nature of its genetic load, and whether the harmful alleles have had time to be purged by selection.
