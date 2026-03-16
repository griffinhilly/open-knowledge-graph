---
id: efficacy-selection-finite-populations
title: Efficacy of Selection in Finite Populations
domain: biology
course: evolutionary-biology
prerequisites:
- id: natural-selection
  type: hard
- id: genetic-drift
  type: hard
- id: effective-population-size
  type: hard
builds-toward:
- nearly-neutral-evolution
- evolvability
tags:
- selection
- drift
- population-size
- efficacy
stage: advanced
status: draft
---

# Efficacy of Selection in Finite Populations

## Core Idea
Selection efficacy depends on selection coefficient relative to drift. When |s| << 1/(2Ne), drift dominates and selection fails to prevent fixation of deleterious alleles. Critical threshold determines whether selection or drift governs molecular evolution.

## Explainer

You understand natural selection as a deterministic force that increases the frequency of beneficial alleles and removes deleterious ones. You also understand genetic drift as a stochastic force that causes random fluctuations in allele frequencies, especially in small populations. The question at the heart of this topic is: **when does selection actually work?** In an idealized infinite population, even the tiniest fitness difference would eventually be resolved by selection. But real populations are finite, and drift introduces noise that can swamp weak selective signals.

The critical insight is a threshold relationship between the **selection coefficient** (s) and the **effective population size** (Ne). When the absolute value of s is much greater than 1/(2Ne), selection dominates: beneficial alleles are very likely to increase in frequency, and deleterious alleles are very likely to be removed. The population is large enough that drift cannot overpower the fitness difference. But when |s| is much less than 1/(2Ne), drift dominates: the allele's fate is determined almost entirely by chance, regardless of whether it is beneficial or deleterious. The mutation is effectively **neutral** from evolution's perspective, even if it has a real, measurable effect on fitness. The boundary region where |s| ≈ 1/(2Ne) is where the contest between selection and drift is most uncertain.

A concrete example makes this tangible. Consider a mutation that reduces fitness by 0.01% (s = -0.0001). In a population with Ne = 1,000,000, the quantity 2Ne·s = 200, far greater than 1 — selection efficiently purges this mutation. But in a population with Ne = 1,000, 2Ne·s = 0.2, much less than 1 — drift dominates, and this mildly deleterious mutation can easily drift to fixation as if it were neutral. The same mutation, with the same fitness effect, has completely different evolutionary fates depending on population size. This is why small populations accumulate slightly deleterious mutations — a process called **genetic deterioration** or mutational meltdown in extreme cases.

This threshold has profound implications for molecular evolution. Most mutations in protein-coding genes are mildly deleterious, with selection coefficients in the range where population size determines their fate. In large populations (many bacteria, some insects), purifying selection is efficient and genomes stay lean. In small populations (many vertebrates, island species, endangered populations), weakly deleterious mutations accumulate because drift shields them from selection. This framework also explains why species with small effective population sizes tend to have larger genomes with more noncoding DNA, more pseudogenes, and more transposable elements — the genomic "junk" persists because selection is too weak relative to drift to remove it. The efficacy of selection is thus not a fixed property of a mutation but an emergent property of the mutation-population system.
