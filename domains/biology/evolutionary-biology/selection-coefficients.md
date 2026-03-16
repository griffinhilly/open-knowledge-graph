---
id: selection-coefficients
title: Selection Coefficients and Fitness Measures
domain: biology
course: evolutionary-biology
prerequisites:
- id: fitness-landscape
  type: hard
builds-toward:
- directional-stabilizing-selection
- mutation-selection-balance
- balancing-selection
tags:
- selection
- fitness
- s-coefficient
- relative-fitness
stage: advanced
status: draft
---

# Selection Coefficients and Fitness Measures

## Core Idea
The selection coefficient (s) quantifies the strength of selection: it is the reduction in fitness of a genotype relative to the wild-type (s ranges 0 to 1). Selection acts on phenotypes, and its effectiveness depends on both the selection coefficient and allele frequency. Weak selection (s << 1/Ne) can be overcome by drift in small populations.

## Explainer

From studying fitness landscapes, you understand that different genotypes have different reproductive success — some are better adapted to their environment than others. The **selection coefficient** (*s*) puts a precise number on this difference. By convention, the fittest genotype in the population is assigned a relative fitness of *w* = 1, and less fit genotypes are assigned *w* = 1 − *s*. So if a mutant allele reduces fitness by 1%, its selection coefficient is *s* = 0.01 and its relative fitness is 0.99. An *s* of 0 means no fitness difference (the allele is selectively neutral), and an *s* of 1 means the allele is lethal.

This simple number turns out to be enormously powerful because it lets you predict how allele frequencies will change over generations. The change in frequency of a deleterious allele per generation is approximately Δ*q* ≈ −*spq*, where *p* and *q* are the frequencies of the two alleles. Notice that selection is most effective at intermediate allele frequencies (when both *p* and *q* are substantial) and weak when the allele is very rare or very common. A strongly deleterious allele (*s* = 0.1) at a frequency of 0.5 will decline rapidly, but once it becomes rare, selection has diminishing power to eliminate it further — this is why deleterious recessive alleles can persist at low frequencies in populations, hidden from selection in heterozygous carriers.

The critical insight is the relationship between selection and **genetic drift**. In a finite population of effective size *N*_e, random sampling of alleles each generation introduces noise. Selection can reliably drive an allele's frequency up or down only when *s* is substantially larger than 1/(2*N*_e). When *s* << 1/(2*N*_e), the allele's fate is governed primarily by drift — it behaves as if it were neutral, regardless of its actual fitness effect. For a population of effective size 10,000, this threshold is about *s* = 0.00005. Mutations with selection coefficients below this value are "effectively neutral" and can fix or be lost by chance. This is the quantitative foundation of the nearly neutral theory and explains why slightly deleterious mutations accumulate in small populations: their *s* values fall below the drift threshold.

Understanding selection coefficients also clarifies why measuring selection in nature is difficult. Most beneficial mutations have small effects (*s* on the order of 0.001 to 0.01), meaning they shift allele frequencies only slightly each generation. Detecting such changes requires either very large population samples, many generations of observation, or molecular signatures of selection in DNA sequences. Conversely, the rare mutations with large *s* values — such as antibiotic resistance alleles in bacteria exposed to antibiotics, where *s* for the sensitive allele can approach 1 — produce dramatic frequency shifts observable in real time, making microbial evolution one of the best systems for studying selection coefficients empirically.
