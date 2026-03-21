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

## Questions

```yaml
- question: "A captive breeding program for an endangered species carefully pairs individuals with low pedigree relatedness. The primary goal of this practice is to:"
  type: multiple-choice
  options:
    - "Increase the rate of beneficial mutations by maximizing genetic diversity"
    - "Prevent deleterious recessive alleles from reaching homozygosity, thereby avoiding inbreeding depression"
    - "Reduce competition between related individuals for food and territory"
    - "Ensure phenotypic uniformity for consistent fitness in the reintroduction environment"
  answer: 1
  explanation: "The central risk of inbreeding is exposing the population's genetic load — the deleterious recessive alleles that were masked in heterozygotes. By pairing unrelated individuals, managers keep those alleles in heterozygous form where they are harmless. Option A misidentifies the mechanism (inbreeding doesn't affect mutation rates); option C describes a behavioral concern, not genetic; option D gets the goal backwards — managers often want phenotypic variation."

- question: "A population of self-fertilizing plants has maintained very high inbreeding coefficients for hundreds of generations but shows minimal inbreeding depression. The most likely explanation is:"
  type: multiple-choice
  options:
    - "Self-fertilization is a different mechanism from true inbreeding and doesn't expose recessive alleles"
    - "Plants lack the immune and reproductive systems through which inbreeding depression manifests"
    - "Repeated exposure of recessive alleles to selection over many generations has purged the most severely deleterious ones"
    - "Inbreeding depression only affects diploid species with sexual reproduction, not self-fertilizing plants"
  answer: 2
  explanation: "Purging is a real evolutionary phenomenon: when inbreeding repeatedly exposes deleterious recessives to homozygosity, selection removes the most harmful alleles over generations. A population with a long history of inbreeding may have a greatly reduced genetic load. Self-fertilizing plants absolutely can experience inbreeding depression (option A is false); plants do show depression in survival and fertility (B is false); inbreeding depression affects all diploids (D is false)."

- question: "Inbreeding depression occurs because mating between relatives creates new harmful mutations that were not present in the population before."
  type: true-false
  answer: false
  explanation: "Inbreeding does not generate new mutations. Inbreeding depression occurs because mating between relatives increases the probability that offspring inherit the same allele from both parents (identity by descent), exposing previously hidden deleterious recessive alleles that were masked in heterozygotes. The harmful alleles were already present in the population — inbreeding merely reveals the existing genetic load. This distinction is crucial: a population with a smaller genetic load will show less depression, regardless of inbreeding level."

- question: "The coefficient of inbreeding (F) measures the probability that an individual carries two alleles at a given locus that are identical by descent — both physical copies of the same ancestral allele."
  type: true-false
  answer: true
  explanation: "This is the precise definition. F is not about allele frequency similarity or phenotypic resemblance to relatives; it is specifically the probability of identity by descent (IBD). Two alleles are IBD if they trace back through the pedigree to the same single ancestral copy. For first-cousin offspring, F = 1/16; for sibling offspring, F = 1/4. Crucially, alleles can be the same variant (e.g., both 'A') without being IBD if they came from different ancestral copies."

- question: "Why does inbreeding increase the expression of fitness-reducing traits, and why does the severity of inbreeding depression vary between populations with the same level of inbreeding?"
  type: short-answer
  answer: "Inbreeding increases homozygosity at all loci, including those carrying deleterious recessive alleles. In heterozygotes, one functional allele masks the defective one; in homozygotes, the harmful phenotype is expressed. The severity of depression depends on the population's genetic load — the number and effect size of deleterious recessives present. Populations that have been inbreeding for many generations may have purged severe recessives through selection, leaving a reduced load; populations with a history of large, outbreeding size may carry many hidden deleterious alleles that only become exposed under inbreeding."
  explanation: "The key insight is that inbreeding acts as a revealer, not a creator, of genetic harm. Two populations with identical F values can show dramatically different levels of depression depending on their evolutionary history. This is why some naturally self-fertilizing species tolerate high inbreeding with little apparent cost, while others suffer severe decline."
```

## Explainer

Every individual carries a hidden burden of **deleterious recessive alleles** — mutations that reduce fitness but remain masked in heterozygotes because one functional copy of the gene is enough. In large, randomly mating populations, most individuals are heterozygous at these loci, and the harmful alleles stay invisible. Inbreeding changes this equation. When relatives mate, they share recent common ancestors, which means they are likely to carry copies of the same alleles inherited from those ancestors. Their offspring therefore have a much higher chance of receiving two identical copies — becoming homozygous — and when both copies are the broken version, the deleterious phenotype appears. This is **inbreeding depression**: the decline in average fitness that accompanies increased homozygosity.

The **coefficient of inbreeding (F)** puts a number on this risk. F measures the probability that the two alleles at any given locus in an individual are **identical by descent** — that is, both are physical copies of the same ancestral allele, not just the same variant by coincidence. For the offspring of first cousins, F = 1/16; for offspring of siblings, F = 1/4. You calculate F by tracing paths through the pedigree from one parent up to each common ancestor and back down to the other parent, counting the number of transmission steps. Each path contributes (1/2)^n to F, where n is the number of links in the path. If you studied effective population size, you'll recognize that F also rises predictably in small populations even without deliberate inbreeding — genetic drift forces alleles to fixation, and the average F across the population increases by approximately 1/(2Nₑ) each generation.

The practical consequences are severe. Inbred individuals show reduced survival, lower fertility, weaker immune function, and greater susceptibility to disease — effects documented across animals, plants, and fungi. In conservation biology, small endangered populations face an **extinction vortex** where declining numbers increase inbreeding, which reduces fitness, which further shrinks the population. Programs that manage captive breeding or reintroduction carefully track pedigrees and F values to minimize relatedness between mating pairs.

A crucial nuance is that inbreeding itself does not create harmful alleles — it merely exposes the **genetic load** that was already present but hidden in heterozygotes. A population that has been small for many generations may have already purged its most severely deleterious recessives through selection, because those alleles were repeatedly exposed to selection in homozygous form. This is why some naturally inbreeding species, like certain self-fertilizing plants, tolerate high F values with minimal depression. The severity of inbreeding depression depends on the population's history, the nature of its genetic load, and whether the harmful alleles have had time to be purged by selection.
