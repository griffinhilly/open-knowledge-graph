---
id: mating-patterns-inbreeding-assortative
title: 'Mating Patterns: Inbreeding and Assortative Mating'
domain: biology
course: ecology-and-evolution
prerequisites:
- id: population-genetics-intro
  type: hard
- id: hardy-weinberg-equilibrium
  type: soft
builds-toward:
- population-genetic-structure-metapopulations
- speciation
tags:
- mating
- inbreeding
- assortative-mating
- random-mating
stage: formal-systems
status: validated
---

# Mating Patterns: Inbreeding and Assortative Mating

## Core Idea
Mating patterns deviate from random when individuals preferentially mate with relatives (inbreeding) or with similar phenotypes (assortative mating). Inbreeding increases homozygosity and exposes deleterious recessive alleles. Assortative mating increases linkage disequilibrium and can drive sympatric divergence.

## Questions

```yaml
- question: "A population of self-fertilizing plants undergoes many generations of inbreeding. Compared to a randomly mating population with identical allele frequencies, the inbred population will show:"
  type: multiple-choice
  options:
    - "Lower frequencies of deleterious recessive alleles, because inbreeding causes selection against them"
    - "More heterozygotes, because inbreeding produces more diverse genotype combinations"
    - "More homozygotes and greater expression of recessive traits, because inbreeding exposes alleles that were previously hidden in heterozygotes"
    - "Changed allele frequencies at all loci, because inbreeding directly alters which alleles are passed on"
  answer: 2
  explanation: "Inbreeding shifts genotype frequencies toward homozygosity without changing allele frequencies. Many deleterious alleles are recessive and phenotypically hidden in heterozygotes — carriers do not suffer their effects. Inbreeding increases the probability that two copies of the same allele (identical by descent) end up in the same individual, converting heterozygous carriers into affected homozygotes. This exposure of deleterious recessives is the mechanism of inbreeding depression. Option D is a critical misconception: allele frequencies are not changed by non-random mating alone."

- question: "In a bird population, large-bodied birds preferentially mate with other large-bodied birds (positive assortative mating). The primary evolutionary consequence of this mating pattern is:"
  type: multiple-choice
  options:
    - "Reduced homozygosity genome-wide, because assortative mating increases genetic mixing"
    - "Increased frequency of 'large body' alleles throughout the genome due to selection"
    - "Increased linkage disequilibrium among loci contributing to body size, as alleles for large body size become statistically associated"
    - "Inbreeding depression similar to that seen in close-relative mating"
  answer: 2
  explanation: "Positive assortative mating increases homozygosity specifically at loci controlling the assorted trait, and builds linkage disequilibrium: alleles at multiple loci that all contribute to large body size become statistically associated because large-bodied birds (who carry many 'large' alleles) disproportionately mate with each other. This is distinct from inbreeding, which affects the whole genome indiscriminately, not just trait-relevant loci. Allele frequencies at the body-size loci do not change due to assortative mating alone — only their statistical associations change."

- question: "Inbreeding in a population directly changes the frequencies of alleles over generations, which is why it is an evolutionary force equivalent to selection or genetic drift."
  type: true-false
  answer: false
  explanation: "This is a fundamental misconception. Inbreeding redistributes existing alleles into different genotype combinations — specifically, it increases homozygosity and decreases heterozygosity — but it does not by itself change allele frequencies. The same alleles are present in the same proportions; they are just combined differently. Inbreeding can interact with selection (by exposing recessive alleles to selection) or with drift (in small populations), and those secondary effects can change allele frequencies. But the act of inbreeding alone is not an evolutionary force in the allele-frequency sense."

- question: "Inbreeding depression results from inbreeding increasing homozygosity, which exposes deleterious recessive alleles that were previously hidden in heterozygous individuals and therefore sheltered from selection."
  type: true-false
  answer: true
  explanation: "This is the core mechanism of inbreeding depression. In a randomly mating population, many deleterious recessives exist at low frequency and are mainly found in heterozygotes, where the dominant allele masks their effect. Inbreeding raises the probability that two copies of the same recessive allele (identical by descent) meet in one individual, converting carriers into affected homozygotes. The result is reduced survival, fertility, and health in inbred individuals relative to outbred ones — a pattern observed across animals, plants, and humans."

- question: "How does inbreeding differ from positive assortative mating in terms of which parts of the genome are affected, and what are the distinct evolutionary consequences of each?"
  type: short-answer
  answer: "Inbreeding increases homozygosity uniformly across the entire genome, because it is based on overall relatedness: mating with a relative means sharing alleles at many loci due to common ancestry. Positive assortative mating increases homozygosity only at loci that control the trait being assorted — body size, plumage color, etc. — leaving the rest of the genome unaffected. Evolutionarily, inbreeding primarily exposes deleterious recessives genome-wide, causing inbreeding depression and reducing fitness. Assortative mating builds linkage disequilibrium among trait-relevant loci, reduces gene flow between phenotypically distinct groups, and can drive sympatric divergence if the assorted trait is ecologically relevant — eventually contributing to speciation without geographic isolation."
  explanation: "The key distinction is scope: inbreeding is a whole-genome phenomenon driven by pedigree relatedness; assortative mating is a targeted phenomenon driven by phenotypic similarity. Both produce non-random genotype distributions, but through different mechanisms and with different consequences."
```

## Explainer

The Hardy-Weinberg model you studied earlier assumes random mating — every individual is equally likely to mate with any other individual in the population. Real populations almost never meet this assumption. **Non-random mating** occurs whenever mate choice is biased by relatedness, phenotype, or proximity, and it systematically changes genotype frequencies even when it does not directly change allele frequencies. Understanding how mating patterns deviate from random is essential for predicting evolutionary trajectories.

**Inbreeding** occurs when relatives mate more often than expected by chance. The most intuitive measure is the **inbreeding coefficient** (*F*), which quantifies the probability that two alleles at a locus in an individual are identical by descent — meaning they trace back to the same copy in a recent ancestor. When *F* increases, heterozygosity decreases and homozygosity increases across the genome. This matters because many deleterious alleles are recessive: they cause harm only when homozygous. In a randomly mating population, these alleles hide safely in heterozygotes. Inbreeding strips away that protection, exposing them. The result is **inbreeding depression** — reduced survival and reproduction in inbred individuals. You see this starkly in small, isolated populations: cheetahs with low genetic diversity and high disease susceptibility, or inbred captive populations with elevated rates of developmental abnormalities.

**Assortative mating** is different from inbreeding because it operates on phenotype rather than pedigree. In **positive assortative mating**, individuals preferentially mate with others who share a trait — large birds pairing with large birds, or humans tending to marry partners of similar height. This increases homozygosity specifically at loci controlling the assorted trait, while leaving the rest of the genome unaffected. Crucially, positive assortative mating also builds **linkage disequilibrium**: alleles at different loci that both contribute to the preferred phenotype become statistically associated, because individuals carrying "large" alleles at multiple loci disproportionately mate with each other. **Negative assortative mating** (disassortative mating), where opposites attract, has the reverse effect — it maintains heterozygosity and can stabilize polymorphisms, as seen in MHC-based mate choice in many vertebrates.

The evolutionary consequences extend beyond single-generation genotype shifts. Prolonged positive assortative mating on ecologically relevant traits can drive **sympatric divergence** — populations splitting into distinct forms without geographic isolation. If large-bodied fish preferentially mate with other large-bodied fish and small-bodied fish do the same, gene flow between the two size classes decreases, and natural selection can push them further apart. This connects mating patterns directly to speciation, one of the topics this concept builds toward. Inbreeding in small populations, meanwhile, interacts with genetic drift to erode adaptive potential, making it a central concern in conservation genetics and metapopulation management.
