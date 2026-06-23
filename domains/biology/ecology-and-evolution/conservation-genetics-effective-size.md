---
id: conservation-genetics-effective-size
title: 'Conservation Genetics: Effective Population Size and Inbreeding'
domain: biology
course: ecology-and-evolution
prerequisites:
- id: effective-population-size
  type: hard
- id: genetic-drift-in-small-populations
  type: hard
- id: population-viability-analysis
  type: soft
- id: effective-population-size-ne-estimation
  type: hard
- id: inbreeding-depression-genetic-rescue
  type: soft
- id: population-bottleneck-drift-inbreeding
  type: soft
- id: population-genetic-structure-metapopulations
  type: soft
builds-toward:
- extinction-vortex-populations
- invasive-species-ecological-impacts
tags:
- conservation-genetics
- effective-size
- inbreeding-depression
- genetic-diversity
stage: formal-systems
status: validated
---

# Conservation Genetics: Effective Population Size and Inbreeding

## Core Idea
Effective population size (Ne) is smaller than census size and depends on sex ratio, reproductive variance, and fluctuations. Small Ne causes rapid drift and inbreeding depression. Conservation typically targets Ne > 500 to maintain genetic diversity and evolutionary potential. Managing gene flow and reintroduction restores Ne in fragmented populations.

## Questions

```yaml
- question: "A lion population in a reserve has 500 individuals, but genetic analysis reveals that only 10 males sire essentially all offspring while 490 females reproduce equally. Using the sex-ratio formula Ne = 4NmNf/(Nm + Nf), what is the approximate effective population size?"
  type: multiple-choice
  options:
    - "~500 — the census size is the relevant number for conservation management"
    - "~250 — the average of the breeding male and female counts"
    - "~40 — determined by the bottleneck of the small number of breeding males"
    - "~10 — because only the 10 breeding males contribute novel genetic material"
  answer: 2
  explanation: "Ne = 4 × 10 × 490 / (10 + 490) = 19,600 / 500 ≈ 39. The bottleneck imposed by the rare sex (here, the small number of breeding males) dramatically reduces Ne below the census size of 500. This is not an obscure formula edge case — it captures a fundamental biological reality. Every allele in the next generation must pass through one of those 10 males (or one of the 490 females). The genetic bottleneck is the rarer sex, regardless of how large the total population appears."

- question: "A species' population sizes over four generations were: 2000, 1000, 20, 800. Which calculation best estimates the long-term effective population size?"
  type: multiple-choice
  options:
    - "The arithmetic mean ≈ 955 — reflecting the average population experience"
    - "The most recent population size of 800 — since current size determines current drift"
    - "The harmonic mean ≈ 70 — because bottleneck generations dominate long-term genetic diversity"
    - "The minimum of 20 — because all diversity was lost in the crash generation"
  answer: 2
  explanation: "Long-term Ne is the harmonic mean: 4 / (1/2000 + 1/1000 + 1/20 + 1/800) = 4 / (0.0005 + 0.001 + 0.05 + 0.00125) ≈ 4 / 0.053 ≈ 75. The harmonic mean is dominated by the smallest value because the 1/Ne term for the bottleneck year (1/20 = 0.05) is nearly as large as all other terms combined. This is why a single severe bottleneck leaves a lasting genetic signature even after recovery — the harmonic mean remains depressed for generations. The arithmetic mean (955) dramatically overestimates genetic resilience."

- question: "A population with a current census size of 10,000 individuals could have an effective population size of only a few hundred due to historical bottlenecks and reproductive skew."
  type: true-false
  answer: true
  explanation: "Effective population size reflects the genetic history of a lineage, not just its current census. Two mechanisms explain this: first, a historical bottleneck permanently depresses long-term Ne via the harmonic mean effect, even after the population recovers numerically. Second, ongoing reproductive skew — a few dominant individuals siring most offspring — continuously reduces Ne below census size in each generation. The Florida panther, cheetah, and Northern elephant seal all show genetic signatures of small Ne despite having census sizes in the hundreds or thousands."

- question: "Inbreeding depression occurs because close relative mating causes new harmful mutations to arise more frequently."
  type: true-false
  answer: false
  explanation: "Inbreeding depression does not create new mutations — it exposes pre-existing ones. Most organisms carry deleterious recessive alleles that are harmlessly 'hidden' in heterozygous form (one functional copy masks one defective copy). When closely related individuals mate, their offspring have a much higher probability of being homozygous for the same recessive allele — both copies defective, with no functional copy to compensate. The harmful alleles were always there; inbreeding merely increases the probability they are expressed. This distinction matters for management: purging deleterious alleles requires exposure, not prevention, which creates a careful tradeoff in small-population conservation."

- question: "Why does a population bottleneck that occurred 50 generations ago continue to affect the genetic diversity of the current population, even after the population has recovered to large numbers?"
  type: short-answer
  answer: "Alleles that were lost during the bottleneck cannot be recovered by population growth alone. If an allele was at low frequency and was lost by genetic drift during the crash, no amount of reproduction by the survivors will recreate it — the only sources are new mutation (extremely rare) or gene flow from other populations. The harmonic mean effect means the bottleneck generation continues to suppress long-term Ne estimates. Additionally, the genetic drift during the bottleneck may have fixed deleterious alleles and eliminated beneficial ones, leaving a population that is less adaptable to future environmental challenges even though it appears numerically robust."
  explanation: "This is the key practical insight for conservation genetics: counting animals is not enough. A population that crashed to 30 individuals three generations ago and recovered to 3,000 has the genetic diversity of a population that never exceeded ~100 individuals, because the harmonic mean of 30 and 3,000 is dominated by the 30. Managing only current census size misses the genetic legacy of the bottleneck — hence the conservation target of Ne > 500, which requires far larger census sizes (typically 5–10× Ne) to achieve."
```

## Explainer

From your study of effective population size and genetic drift, you know that the rate at which populations lose genetic variation depends not on how many individuals you can count, but on how many are actually contributing genes to the next generation. Conservation genetics applies this principle to the urgent practical question: how small can a population get before it is genetically doomed?

The **effective population size (Ne)** is almost always smaller — often dramatically smaller — than the **census size (N)**. Three factors drive this gap. First, **unequal sex ratios**: if a population of 100 elephants has 10 breeding males and 90 females, Ne is calculated as 4 × (10 × 90) / (10 + 90) = 36, not 100. The bottleneck is the rarer sex. Second, **variance in reproductive success**: if a few dominant males sire most offspring while others sire none, the genetic contribution is concentrated in fewer individuals. Third, **population fluctuations**: Ne is disproportionately influenced by the smallest population size in a species' history. A population that crashes to 20 individuals during a drought and recovers to 10,000 will carry the genetic signature of that bottleneck for generations — the harmonic mean, not the arithmetic mean, determines long-term Ne.

Why does small Ne matter for conservation? Because genetic drift — the random loss of alleles — intensifies as Ne shrinks. In a population of Ne = 50, there is roughly a 1% chance per generation that any given allele is lost purely by chance. Over dozens of generations, this erodes genetic diversity relentlessly. Simultaneously, **inbreeding** becomes unavoidable in small populations: with fewer potential mates, individuals increasingly share recent ancestors. Inbreeding exposes deleterious recessive alleles that were safely hidden in heterozygous form, causing **inbreeding depression** — reduced survival, fertility, and disease resistance. The Florida panther population, reduced to about 25 individuals by the 1990s, showed kinked tails, heart defects, and poor sperm quality — classic inbreeding depression that was partially reversed by introducing Texas pumas to restore gene flow.

Conservation geneticists use two key thresholds. The **50/500 rule** suggests Ne > 50 to avoid severe inbreeding depression in the short term, and Ne > 500 to maintain enough genetic variation for long-term adaptive evolution. These numbers are guidelines, not guarantees — some species tolerate low Ne better than others depending on their history of purging deleterious alleles. Management strategies include **genetic rescue** (introducing individuals from other populations to increase Ne), **corridor creation** (reconnecting fragmented habitats to restore natural gene flow), and **captive breeding programs** that use pedigree analysis to minimize relatedness among mating pairs. The overarching goal is not simply to keep animals alive, but to maintain the genetic diversity that allows populations to adapt to future environmental changes.
