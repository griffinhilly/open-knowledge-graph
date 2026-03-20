---
id: population-genetics-intro
title: Population Genetics and Hardy-Weinberg Equilibrium
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: mendelian-genetics
  type: hard
- id: dna-mutations
  type: soft
- id: non-mendelian-inheritance
  type: soft
- id: simple-probability
  type: soft
- id: probability-axioms
  type: soft
tags:
- Hardy-Weinberg
- allele frequency
- genetic drift
- natural selection
- population genetics
stage: advanced
status: validated
---

# Population Genetics and Hardy-Weinberg Equilibrium

## Core Idea
Population genetics studies how allele and genotype frequencies change across generations in a population. The Hardy-Weinberg principle states that, under idealized conditions (large population, random mating, no mutation, migration, or selection), allele frequencies remain constant from generation to generation, and genotype frequencies satisfy p² + 2pq + q² = 1. Deviations from Hardy-Weinberg equilibrium signal one or more evolutionary forces acting on the population. Natural selection, genetic drift, mutation, gene flow, and non-random mating all alter allele frequencies, driving evolutionary change.

## How It's Best Learned
Calculate expected Hardy-Weinberg genotype frequencies from observed allele frequencies and test for deviations using chi-square analysis. Practice identifying which violation of assumptions would cause each type of deviation.

## Common Misconceptions
- Hardy-Weinberg is a null model, not a description of real populations; it is useful precisely because real populations deviate from it.
- p + q = 1 describes allele frequencies, not genotype frequencies; p² + 2pq + q² = 1 describes genotype frequencies.

## Questions

```yaml
- question: "A population is in Hardy-Weinberg equilibrium for a gene with alleles A (frequency p = 0.6) and a (frequency q = 0.4). What is the expected frequency of heterozygotes (Aa)?"
  type: multiple-choice
  options: ["0.24", "0.48", "0.16", "0.36"]
  answer: 1
  explanation: "The frequency of heterozygotes is 2pq = 2(0.6)(0.4) = 0.48. A common error is computing pq = 0.24 and forgetting the factor of 2, which accounts for the two ways to be heterozygous (receiving A from mother and a from father, or vice versa)."

- question: "The equation p + q = 1 describes the frequencies of genotypes in a Hardy-Weinberg population."
  type: true-false
  answer: false
  explanation: "p + q = 1 describes *allele* frequencies — p is the frequency of one allele, q of the other, and together they must sum to 1. *Genotype* frequencies are described by p² + 2pq + q² = 1, which is the expanded form of (p + q)². Confusing these two equations is one of the most common errors in population genetics problems."

- question: "A population is found to have significantly more homozygous individuals than Hardy-Weinberg predicts. Name one evolutionary mechanism that could cause this deviation and explain why it would produce an excess of homozygotes."
  type: short-answer
  answer: "Non-random mating (inbreeding) causes individuals to preferentially mate with relatives, increasing the probability that both copies of a gene descend from the same ancestor and are therefore identical. This increases homozygosity beyond H-W expectations without changing allele frequencies. Alternatively, strong disruptive selection against heterozygotes would reduce 2pq below predicted levels."
  explanation: "This tests whether students understand H-W as a null model: deviations reveal which assumptions are violated. An excess of homozygotes specifically points to mechanisms that reduce heterozygosity — inbreeding, assortative mating, or selection against heterozygotes — rather than mechanisms like drift or mutation that shift allele frequencies."
```

## Explainer

From Mendelian genetics, you know how traits are inherited in single crosses: dominant and recessive alleles segregate according to predictable ratios. Population genetics asks a different question: across an entire population breeding over many generations, how do allele frequencies change — or stay the same?

The Hardy-Weinberg principle answers the "stay the same" case. Under five idealized conditions — infinite population size, random mating, no mutation, no migration, and no natural selection — allele frequencies remain constant indefinitely. If allele A has frequency p and allele a has frequency q (with p + q = 1), then genotype frequencies in the next generation will be p² (AA), 2pq (Aa), and q² (aa). This is simply the result of random mating: each offspring independently draws one allele from each parent at random, so the probability of AA is p × p = p². The 2pq term for heterozygotes gets the factor of 2 because there are two ways to combine the alleles (A from mom and a from dad, or vice versa).

The real power of Hardy-Weinberg is not as a description of real populations — those five conditions are never all met simultaneously — but as a **null model**. It tells you what to expect if *nothing* is happening evolutionarily. When you observe a population and its genotype frequencies deviate from p² + 2pq + q², that deviation is a signal. An excess of homozygotes suggests inbreeding or assortative mating. A shift in allele frequencies over generations suggests selection, drift, or gene flow. Hardy-Weinberg equilibrium is the baseline; evolution is the deviation from it.

Keep careful track of what p and q describe: they are **allele frequencies**, not genotype frequencies. In a population where 36% of individuals are homozygous recessive (aa), q² = 0.36, so q = 0.6 and p = 0.4. From those allele frequencies you can calculate all three expected genotype frequencies. This inferential direction — from observable genotype counts back to allele frequencies, then forward to predictions — is the core workflow of population genetics analysis.
