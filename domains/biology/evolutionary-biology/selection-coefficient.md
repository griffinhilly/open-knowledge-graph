---
id: selection-coefficient
title: Selection Coefficient
domain: biology
course: evolutionary-biology
prerequisites:
- id: natural-selection
  type: hard
- id: population-genetics-intro
  type: hard
builds-toward:
- directional-selection
- balancing-selection
- fitness-landscape
tags:
- population-genetics
- selection
- quantitative
stage: advanced
status: draft
---

# Selection Coefficient

## Core Idea
The selection coefficient (s) quantifies the strength of selection against a genotype, ranging from 0 (no selection) to 1 (lethal). It represents the relative reduction in fitness compared to the most-fit genotype. Selection strength determines the rate at which allele frequencies change per generation.

## How It's Best Learned
Start with simple two-allele systems and calculate changes in allele frequency using s values. Then apply to real datasets comparing fitness across phenotypes.

## Common Misconceptions
- s = 1 doesn't mean all individuals of that genotype die in one generation; it affects reproduction rates.
- Selection coefficient is independent of allele frequency (frequency-dependent selection is a separate phenomenon).

## Explainer

From your study of natural selection, you know that some genotypes leave more offspring than others — that is what fitness means. The **selection coefficient** (denoted **s**) puts a number on this difference. It measures the fractional reduction in fitness of a genotype relative to the fittest genotype in the population. If the fittest genotype has fitness 1.0 and a less-fit genotype has fitness 0.95, then s = 0.05 for that genotype. Think of s as a "fitness tax" — each generation, individuals with that genotype contribute 5% fewer offspring to the next generation compared to the optimal genotype.

The value of s determines how fast natural selection can change allele frequencies. When s is large (say 0.5 or higher), selection is strong and allele frequencies change rapidly — a lethal allele with s = 1.0 is eliminated from homozygotes in a single generation. When s is small (say 0.001), selection is weak and allele frequencies change very slowly, requiring hundreds or thousands of generations for a noticeable shift. This is where population genetics connects to neutral theory: if s is smaller than roughly 1/(2N), where N is the effective population size, then drift overwhelms selection and the allele behaves as if it were neutral. In a population of 10,000, an allele with s = 0.00001 is effectively invisible to selection.

To see how s works in practice, consider a simple model with two alleles, A and a. Assign fitness 1.0 to AA, fitness 1 - hs to the heterozygote Aa (where **h** is the dominance coefficient), and fitness 1 - s to aa. If A is fully dominant (h = 0), the heterozygote has the same fitness as AA, and selection only "sees" the recessive allele when it appears in homozygotes. If h = 0.5, the heterozygote is exactly intermediate — this is codominance from a fitness perspective. The rate of change in allele frequency per generation depends on both s and the current allele frequency. Selection is most effective at changing allele frequencies when the less-fit allele is at intermediate frequency; it slows dramatically when the allele is very rare because most copies hide in heterozygotes (if recessive) or are already nearly fixed (if dominant).

Real-world selection coefficients span an enormous range. The sickle-cell allele in malaria-endemic regions illustrates this beautifully: in homozygotes (ss), s ≈ 0.8 due to severe anemia, but in heterozygotes (Ss), the allele actually confers a fitness advantage against malaria, creating **balancing selection**. Pesticide resistance mutations may have s close to 0 in the absence of pesticide but become strongly advantageous (negative s for the susceptible allele) when pesticide is applied. By quantifying selection this way, population geneticists can predict how quickly an advantageous allele will spread, how long a deleterious allele will persist, and whether drift or selection is the dominant force shaping a particular gene — the foundation for all quantitative evolutionary prediction.
