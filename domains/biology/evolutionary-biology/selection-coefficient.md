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
status: validated
---

# Selection Coefficient

## Core Idea
The selection coefficient (s) quantifies the strength of selection against a genotype, ranging from 0 (no selection) to 1 (lethal). It represents the relative reduction in fitness compared to the most-fit genotype. Selection strength determines the rate at which allele frequencies change per generation.

## How It's Best Learned
Start with simple two-allele systems and calculate changes in allele frequency using s values. Then apply to real datasets comparing fitness across phenotypes.

## Common Misconceptions
- s = 1 doesn't mean all individuals of that genotype die in one generation; it affects reproduction rates.
- Selection coefficient is independent of allele frequency (frequency-dependent selection is a separate phenomenon).

## Questions

```yaml
- question: "A recessive deleterious allele (h = 0) with selection coefficient s = 0.5 is present at very low frequency (q = 0.001) in a large population. Why does natural selection eliminate it so slowly despite the strong selection pressure?"
  type: multiple-choice
  options:
    - "The selection coefficient weakens as the allele becomes rare, reducing selection pressure at low frequency"
    - "Almost all copies of the allele are in heterozygotes, where h = 0 means the allele confers no fitness disadvantage and is invisible to selection"
    - "Genetic drift counteracts selection when allele frequency is very low, effectively neutralizing it in large populations"
    - "The allele mutates to a neutral form once it becomes sufficiently rare"
  answer: 1
  explanation: "When a recessive allele is rare, the vast majority of copies exist in heterozygotes (Aa), not homozygotes (aa). With h = 0 (completely recessive), heterozygotes have the same fitness as AA — the allele has no fitness effect when paired with a dominant copy. Selection only 'sees' the allele in the rare aa homozygotes. At q = 0.001, the frequency of aa homozygotes is only q² = 0.000001, so the allele is almost completely hidden from selection. This sheltering of recessive alleles in heterozygotes is why deleterious recessive mutations persist for thousands of generations. Option A is a misconception: s is a constant in this model — frequency-dependent selection is a separate phenomenon."

- question: "An allele with selection coefficient s = 0.0001 exists in two populations: one with effective population size N = 1,000 and one with N = 10,000,000. In which population is drift most likely to cause this allele to increase in frequency despite being slightly deleterious?"
  type: multiple-choice
  options:
    - "The large population (N = 10,000,000) — more individuals means more random variation in offspring number"
    - "The small population (N = 1,000) — the threshold for selection to overcome drift is 1/(2N) = 0.0005, which exceeds s = 0.0001"
    - "Both populations equally — the selection coefficient alone determines allele fate, not population size"
    - "Neither — any s > 0 means selection reliably eliminates the allele regardless of population size"
  answer: 1
  explanation: "The key threshold is s vs. 1/(2N). When s < 1/(2N), genetic drift is stronger than selection and the allele behaves as if neutral — it can increase or decrease by chance alone. For N = 1,000: 1/(2×1,000) = 0.0005, which exceeds s = 0.0001, so drift dominates and the allele can drift toward fixation despite being harmful. For N = 10,000,000: 1/(2×10,000,000) ≈ 0.00000005, far less than s, so selection dominates and reliably eliminates the allele. This is the foundation of nearly neutral theory: alleles that are effectively neutral in small populations are effectively selected against in large ones."

- question: "A selection coefficient of s = 1 means that all individuals carrying the affected genotype will die before reaching reproductive age."
  type: true-false
  answer: false
  explanation: "s = 1 means the genotype has zero relative fitness — it contributes no offspring to the next generation compared to the most-fit genotype. This can happen through failure to reproduce, sterility, or any mechanism yielding zero reproductive output, not necessarily death before adulthood. Additionally, if the allele is recessive and h < 1, only the homozygous genotype (aa) has fitness 1 − s = 0; heterozygotes (Aa) may still reproduce and carry the allele forward. The selection coefficient is defined in terms of relative reproductive contribution, not survival."

- question: "Selection is most effective at changing allele frequencies when the allele under selection is at intermediate frequency — it slows when the allele is either very rare or very common."
  type: true-false
  answer: true
  explanation: "The per-generation change in allele frequency (Δq) under selection depends on both s and the current frequency q. When q is very small, there are few copies to select against and most recessive alleles are sheltered in heterozygotes — progress is slow. When q is very large (allele nearly fixed), only rare copies of the alternative allele are under selection — again slow change. The rate peaks at intermediate frequencies where both allele types are common and phenotypic differences are most visible. This frequency-dependence of selection effectiveness shapes the entire trajectory of allele frequency change."

- question: "Why does the effectiveness of natural selection in eliminating a deleterious recessive allele decline as that allele becomes rarer in the population?"
  type: short-answer
  answer: "As the frequency q of a recessive allele decreases, the proportion of allele copies found in homozygotes (aa, frequency q²) drops much faster than the frequency itself — at q = 0.1, about 9% of allele copies are in visible homozygotes; at q = 0.01, only about 1%. Most copies shelter in heterozygotes (Aa, frequency 2pq), which are phenotypically identical to dominant homozygotes (AA) when h = 0. Since selection acts only on expressed phenotypes, the sheltered copies in heterozygotes escape selection entirely. The result is diminishing returns: selection efficiently purges visible homozygous alleles early but becomes increasingly ineffective as remaining copies concentrate in the invisible heterozygote pool."
  explanation: "This asymptotic elimination explains why harmful recessive alleles like those causing cystic fibrosis persist at low but nonzero frequencies — selection pressure becomes negligible long before the allele disappears, and recurrent mutation continually replenishes it."
```

## Explainer

From your study of natural selection, you know that some genotypes leave more offspring than others — that is what fitness means. The **selection coefficient** (denoted **s**) puts a number on this difference. It measures the fractional reduction in fitness of a genotype relative to the fittest genotype in the population. If the fittest genotype has fitness 1.0 and a less-fit genotype has fitness 0.95, then s = 0.05 for that genotype. Think of s as a "fitness tax" — each generation, individuals with that genotype contribute 5% fewer offspring to the next generation compared to the optimal genotype.

The value of s determines how fast natural selection can change allele frequencies. When s is large (say 0.5 or higher), selection is strong and allele frequencies change rapidly — a lethal allele with s = 1.0 is eliminated from homozygotes in a single generation. When s is small (say 0.001), selection is weak and allele frequencies change very slowly, requiring hundreds or thousands of generations for a noticeable shift. This is where population genetics connects to neutral theory: if s is smaller than roughly 1/(2N), where N is the effective population size, then drift overwhelms selection and the allele behaves as if it were neutral. In a population of 10,000, an allele with s = 0.00001 is effectively invisible to selection.

To see how s works in practice, consider a simple model with two alleles, A and a. Assign fitness 1.0 to AA, fitness 1 - hs to the heterozygote Aa (where **h** is the dominance coefficient), and fitness 1 - s to aa. If A is fully dominant (h = 0), the heterozygote has the same fitness as AA, and selection only "sees" the recessive allele when it appears in homozygotes. If h = 0.5, the heterozygote is exactly intermediate — this is codominance from a fitness perspective. The rate of change in allele frequency per generation depends on both s and the current allele frequency. Selection is most effective at changing allele frequencies when the less-fit allele is at intermediate frequency; it slows dramatically when the allele is very rare because most copies hide in heterozygotes (if recessive) or are already nearly fixed (if dominant).

Real-world selection coefficients span an enormous range. The sickle-cell allele in malaria-endemic regions illustrates this beautifully: in homozygotes (ss), s ≈ 0.8 due to severe anemia, but in heterozygotes (Ss), the allele actually confers a fitness advantage against malaria, creating **balancing selection**. Pesticide resistance mutations may have s close to 0 in the absence of pesticide but become strongly advantageous (negative s for the susceptible allele) when pesticide is applied. By quantifying selection this way, population geneticists can predict how quickly an advantageous allele will spread, how long a deleterious allele will persist, and whether drift or selection is the dominant force shaping a particular gene — the foundation for all quantitative evolutionary prediction.
