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
status: validated
---

# Selection Coefficients and Fitness Measures

## Core Idea
The selection coefficient (s) quantifies the strength of selection: it is the reduction in fitness of a genotype relative to the wild-type (s ranges 0 to 1). Selection acts on phenotypes, and its effectiveness depends on both the selection coefficient and allele frequency. Weak selection (s << 1/Ne) can be overcome by drift in small populations.

## Questions

```yaml
- question: "Two populations carry the same deleterious allele with s = 0.0001. Population 1 has Ne = 200; Population 2 has Ne = 100,000. In which population is selection most likely to systematically eliminate this allele?"
  type: multiple-choice
  options:
    - "Population 1 — smaller populations have stronger selection because fewer competing alleles reduce interference"
    - "Population 2 — s exceeds 1/(2Ne), so selection is effective and will drive the allele down"
    - "Population 1 — genetic drift in small populations removes deleterious alleles more quickly than selection"
    - "Both populations equally — any allele with s > 0 will eventually be eliminated by selection"
  answer: 1
  explanation: "For Population 1, 1/(2Ne) = 1/400 = 0.0025. Since s = 0.0001 << 0.0025, the allele is below the drift threshold — effectively neutral, and its fate is governed by chance. For Population 2, 1/(2Ne) = 1/200,000 = 0.000005. Since s = 0.0001 >> 0.000005, selection is effective and will systematically reduce the allele's frequency. Option 3 is the key misconception: below the drift threshold, even deleterious alleles can fix by chance, regardless of their s value."

- question: "A mildly deleterious recessive allele (s = 0.02 in homozygotes) is present at low frequency (q = 0.02) in a large population. Why does natural selection eliminate it only slowly?"
  type: multiple-choice
  options:
    - "Because s = 0.02 is below the drift threshold in all populations"
    - "Because at low frequency, most copies are in heterozygotes, where the recessive allele is unexpressed and shielded from selection"
    - "Because genetic drift counteracts selection in all large populations"
    - "Because Δq ≈ −spq is positive when q is small, causing the allele to increase before it declines"
  answer: 1
  explanation: "At q = 0.02, most copies of the allele are carried in heterozygotes (approximately 2pq carriers vs. q² homozygotes). In heterozygotes, the recessive allele is phenotypically unexpressed, so selection cannot act on those copies. Only the rare homozygotes (frequency q² = 0.0004) face the full fitness cost of s = 0.02. This 'hiding' of recessive alleles in heterozygous carriers is why recessive deleterious alleles can persist at low frequencies indefinitely, and why the last traces of a deleterious recessive are extremely difficult to eliminate by selection."

- question: "A selection coefficient of s = 0 means the allele reduces fitness to zero and is lethal."
  type: true-false
  answer: false
  explanation: "This reverses the scale. A selection coefficient of s = 0 means no fitness difference — the allele is selectively neutral. A selection coefficient of s = 1 means the allele is lethal (relative fitness w = 1 − s = 0). Values between 0 and 1 represent intermediate fitness costs. This sign convention — zero means neutral, one means lethal — is essential for correctly interpreting all quantitative evolutionary genetics results."

- question: "In a very small population, a slightly deleterious allele (small positive s) can increase in frequency and potentially become fixed, despite being actively opposed by natural selection."
  type: true-false
  answer: true
  explanation: "When s << 1/(2Ne), random genetic drift dominates over selection. Even deleterious alleles behave as effectively neutral and can increase in frequency or fix by chance. This is the quantitative foundation of the nearly neutral theory and explains why slightly deleterious mutations accumulate in small, inbred populations — their s values fall below the drift threshold where selection can no longer reliably oppose them. Larger effective population sizes make selection more powerful relative to drift."

- question: "Explain the concept of 'effective neutrality' and why the same mutation can behave differently in populations of different sizes."
  type: short-answer
  answer: "A mutation is effectively neutral when its selection coefficient s is smaller than the magnitude of genetic drift, approximately 1/(2Ne). Below this threshold, random sampling of alleles each generation introduces fluctuations larger than the selective signal, so the allele's fate is governed by chance rather than fitness. The same mutation with s = 0.0005 is effectively neutral in a small population (Ne = 500, drift threshold = 0.001 > s) but detectably deleterious in a large population (Ne = 10,000, drift threshold = 0.00005 < s). Whether selection or drift dominates depends on the ratio 2Ne·s, not on s alone."
  explanation: "This concept explains several key observations: why small bottlenecked populations accumulate deleterious mutations (reduced Ne lowers the drift threshold), why molecular evolution rates differ between lineages with different Ne values, and why conservation of small populations is genetically perilous beyond just the immediate risk of inbreeding. The nearly neutral theory uses this logic to explain why much molecular variation shows patterns intermediate between strict neutrality and strong selection."
```

## Explainer

From studying fitness landscapes, you understand that different genotypes have different reproductive success — some are better adapted to their environment than others. The **selection coefficient** (*s*) puts a precise number on this difference. By convention, the fittest genotype in the population is assigned a relative fitness of *w* = 1, and less fit genotypes are assigned *w* = 1 − *s*. So if a mutant allele reduces fitness by 1%, its selection coefficient is *s* = 0.01 and its relative fitness is 0.99. An *s* of 0 means no fitness difference (the allele is selectively neutral), and an *s* of 1 means the allele is lethal.

This simple number turns out to be enormously powerful because it lets you predict how allele frequencies will change over generations. The change in frequency of a deleterious allele per generation is approximately Δ*q* ≈ −*spq*, where *p* and *q* are the frequencies of the two alleles. Notice that selection is most effective at intermediate allele frequencies (when both *p* and *q* are substantial) and weak when the allele is very rare or very common. A strongly deleterious allele (*s* = 0.1) at a frequency of 0.5 will decline rapidly, but once it becomes rare, selection has diminishing power to eliminate it further — this is why deleterious recessive alleles can persist at low frequencies in populations, hidden from selection in heterozygous carriers.

The critical insight is the relationship between selection and **genetic drift**. In a finite population of effective size *N*_e, random sampling of alleles each generation introduces noise. Selection can reliably drive an allele's frequency up or down only when *s* is substantially larger than 1/(2*N*_e). When *s* << 1/(2*N*_e), the allele's fate is governed primarily by drift — it behaves as if it were neutral, regardless of its actual fitness effect. For a population of effective size 10,000, this threshold is about *s* = 0.00005. Mutations with selection coefficients below this value are "effectively neutral" and can fix or be lost by chance. This is the quantitative foundation of the nearly neutral theory and explains why slightly deleterious mutations accumulate in small populations: their *s* values fall below the drift threshold.

Understanding selection coefficients also clarifies why measuring selection in nature is difficult. Most beneficial mutations have small effects (*s* on the order of 0.001 to 0.01), meaning they shift allele frequencies only slightly each generation. Detecting such changes requires either very large population samples, many generations of observation, or molecular signatures of selection in DNA sequences. Conversely, the rare mutations with large *s* values — such as antibiotic resistance alleles in bacteria exposed to antibiotics, where *s* for the sensitive allele can approach 1 — produce dramatic frequency shifts observable in real time, making microbial evolution one of the best systems for studying selection coefficients empirically.
