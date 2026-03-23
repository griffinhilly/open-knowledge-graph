---
id: phenotypic-variation-populations
title: Phenotypic Variation and Genetic Basis
domain: biology
course: ecology-and-evolution
prerequisites:
- id: mendelian-genetics
  type: hard
- id: genetic-code
  type: soft
- id: population-genetics-intro
  type: soft
builds-toward:
- heritability-broad-sense-narrow-sense
- natural-selection-types-and-examples
tags:
- phenotypic-variation
- genetic-variation
- environmental-effects
stage: formal-systems
status: validated
---

# Phenotypic Variation and Genetic Basis

## Core Idea
Phenotypic variation in populations arises from both genetic differences and environmental variation. For selection to act, variation must be heritable—passed from parents to offspring. Not all variation is genetic; much may be environmental, making it invisible to natural selection. Understanding the genetic basis of variation is essential for predicting evolutionary responses.

## Questions

```yaml
- question: "A plant breeder selects the tallest plants from a population each generation and uses them as parents for the next. After five generations, the average height has barely changed. What is the most likely explanation?"
  type: multiple-choice
  options:
    - "The population does not have enough individuals to show a detectable evolutionary response"
    - "Most of the height variation in the population has an environmental rather than genetic basis, so selection cannot produce a heritable response"
    - "The plants adapted to the selection pressure by downregulating growth genes"
    - "Five generations is not enough time for natural selection to produce a measurable shift in mean height"
  answer: 1
  explanation: "If tall plants owe their height to favorable growing conditions rather than 'tall' alleles, their offspring will have no more growth-promoting alleles than average. Selection can only shift population means when the selected trait is heritable — when parents pass relevant alleles to offspring. Environmental variation in phenotype contributes to what you see but is invisible to natural selection. A failed selection response is one of the clearest signals that the variation being selected is mostly environmental rather than genetic."

- question: "Twin studies show that IQ scores are substantially heritable. Does this mean that educational interventions cannot raise IQ?"
  type: multiple-choice
  options:
    - "Yes — high heritability means the trait is primarily genetically determined, so environmental interventions will have minimal effect"
    - "No — heritability describes the proportion of variance within a population that is genetic, not whether the trait can be changed by altering the environment"
    - "Yes — if heritability exceeds 0.5, genetic factors dominate and environmental effects are negligible"
    - "No — twin studies systematically underestimate environmental effects and cannot be used to make inferences about individual plasticity"
  answer: 1
  explanation: "This is the most common and consequential misinterpretation of heritability. Heritability is a population statistic: it describes how much of the variation *among individuals in a specific population under current conditions* is attributable to genetic differences. It says nothing about whether a different environment would change all individuals' phenotypes. Height is highly heritable in well-nourished populations, yet average height has increased dramatically over the 20th century due to improved nutrition — a purely environmental change. High heritability and high environmental sensitivity are fully compatible."

- question: "A population in which all phenotypic variation is caused by environmental differences cannot evolve by natural selection, even if the trait under selection is strongly correlated with survival and reproduction."
  type: true-false
  answer: true
  explanation: "Natural selection requires heritable variation — differences among individuals that are transmitted from parent to offspring through genes. If all variation is environmental, selecting individuals with favorable phenotypes produces no change in allele frequencies, because those individuals do not carry special alleles to pass on. The selected trait will correlate with survival and reproduction, but the population's genetic composition — and therefore its mean phenotype under standard conditions — will not change. This is why heritability is the crucial quantity for predicting evolutionary response."

- question: "Observing high phenotypic variation in a population is reliable evidence that substantial genetic variation exists for natural selection to act upon."
  type: true-false
  answer: false
  explanation: "Phenotypic variation conflates genetic and environmental sources. A population planted across a range of soil types and rainfall regimes may show enormous variation in growth even if every individual is genetically identical. Conversely, a population with substantial genetic variation may show little phenotypic variation if the environment is highly uniform and genotype-by-environment interactions are small. Only partitioning the variance — through breeding experiments, parent-offspring regressions, or controlled common-garden studies — reveals how much variation is heritable."

- question: "Why can natural selection only act on the heritable portion of phenotypic variation, and what does this imply for predicting evolutionary responses in a population?"
  type: short-answer
  answer: "Selection acts by differentially transmitting alleles to the next generation: individuals with favorable phenotypes leave more offspring, and if those phenotypes reflect genetic differences, the relevant alleles become more common over time. If the favorable phenotype is instead caused by environmental luck, the individual's offspring will not inherit the advantage — there are no 'favorable environment' alleles. To predict evolutionary response, you must know heritability: the breeder's equation states that response to selection equals heritability times selection differential. Without heritability, even strong selection produces no evolutionary change."
  explanation: "This principle is practically critical. A conservation biologist asking whether a species can adapt to climate change needs to know whether the relevant traits (thermal tolerance, flowering time, drought resistance) have heritable variation. A crop breeder choosing which plants to cross needs to know whether yield differences between lines are genetic or due to field variation. Measuring phenotypic variation alone gives an upper bound on what selection could achieve; the heritable fraction tells you what it actually will achieve."
```

## Explainer

From Mendelian genetics, you know that alleles segregate and assort independently, producing offspring with different genotypes. From the genetic code, you know that genotype encodes the proteins and regulatory signals that build an organism. But when you look at a real population — say, a field of wildflowers varying in height — you are seeing **phenotypic variation**, the combined product of genetic differences, environmental differences, and their interaction. Disentangling these sources is the central challenge that connects genetics to evolution.

Consider plant height. Some variation is clearly genetic: tall parents tend to produce tall offspring because they pass on alleles that promote growth. But some variation is environmental: a genetically identical clone planted in rich soil grows taller than one in poor soil. And some is **genotype-by-environment interaction**: a genotype that thrives in wet conditions may perform poorly in dry ones, while another genotype shows the opposite pattern. When you observe a population, all three sources are mixed together in the phenotypes you see. A plant that appears tall might carry "tall" alleles, or it might simply have landed in a favorable microhabitat.

This distinction matters enormously for evolution because **natural selection can only act on heritable variation** — the portion of phenotypic differences that is transmitted from parent to offspring through genes. If all the height variation in a population were caused by soil quality, selecting the tallest plants as parents would not produce taller offspring in the next generation, because the parents' advantage was environmental, not genetic. Conversely, if most variation is genetic, selection on the tallest plants will shift the population mean upward. The fraction of total phenotypic variation attributable to genetic differences is called **heritability**, a concept you will study in depth soon.

This is why population geneticists care so much about partitioning variance. Measuring phenotypic variation alone tells you nothing about evolutionary potential — you must know how much of that variation has a genetic basis. Breeding experiments, twin studies, and parent-offspring regressions all exist to answer this question. The practical implications are immediate: a crop breeder selecting for yield needs heritable variation to make progress; a conservation biologist predicting whether a species can adapt to climate change needs to know whether the relevant traits have genetic variation to work with. Without heritable phenotypic variation, natural selection has no raw material, and evolution stalls.
