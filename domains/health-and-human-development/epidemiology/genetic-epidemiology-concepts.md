---
id: genetic-epidemiology-concepts
title: 'Genetic Epidemiology: Heritability and Gene-Environment Interaction'
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: epidemiology-foundations
  type: hard
- id: population-genetics-intro
  type: soft
tags:
- genetic-epidemiology
- heritability
- gwas
- gene-environment-interaction
stage: expert
status: validated
---

# Genetic Epidemiology: Heritability and Gene-Environment Interaction

## Core Idea
Genetic epidemiology investigates genetic contributions to disease and gene-environment interactions. Heritability quantifies the proportion of population variance attributable to genetic factors, estimated via twin studies, family aggregation, or genome-wide association studies (GWAS). Understanding genetic susceptibility and its interaction with environmental exposures is essential for precision public health approaches.

## Questions

```yaml
- question: "Average height in the Netherlands increased by roughly 20 cm over the 20th century, yet height has an estimated heritability of ~0.8. Which interpretation is correct?"
  type: multiple-choice
  options:
    - "The heritability estimate must be wrong, since genetic traits cannot change this fast"
    - "The increase proves that height is mostly environmental, contradicting the heritability estimate"
    - "There is no contradiction: heritability measures variance within a population in a given environment, and improved nutrition altered the environment for everyone"
    - "Heritability of 0.8 means 80% of any individual's height is genetically determined, so the environmental change only explains 20% of the increase"
  answer: 2
  explanation: "Heritability is a population-level statistic measuring what fraction of trait *variance* in a given population and environment is attributable to genetic variance. A high heritability says nothing about whether the trait can change when the environment changes — it only says genes explain much of the *differences between people* in the current environment. When nutrition improved uniformly, it shifted the entire distribution upward without touching heritability, which depends on relative differences remaining genetically explained."

- question: "A GWAS for Type 2 diabetes identifies 100 SNPs, each with an odds ratio around 1.10, that together explain only 15% of the estimated heritability (~50%). What is the most likely explanation?"
  type: multiple-choice
  options:
    - "The heritability estimate from twin studies must be inflated by shared environments, so the true heritability is ~15%"
    - "Missing heritability likely comes from rare variants, gene-gene interactions, and limitations of additive variance decomposition not captured by common SNP arrays"
    - "The GWAS significance threshold of p < 5×10⁻⁸ is too stringent and is excluding real variants"
    - "GWAS cannot detect genetic contributions to complex diseases, so these 100 SNPs are likely false positives"
  answer: 1
  explanation: "The 'missing heritability' puzzle is a real and active research area. GWAS arrays are designed around common variants, so rare variants contributing to heritability are systematically missed. Gene-gene (epistatic) interactions and gene-environment interactions also contribute variance that standard additive heritability models don't fully capture. Option A is a genuine concern but doesn't explain the full gap; Option C is incorrect because the threshold is appropriate for genome-wide multiple testing correction."

- question: "Heritability (h²) is a property of a population in a specific environment, not a fixed property of a gene or trait."
  type: true-false
  answer: true
  explanation: "Heritability is defined as the proportion of population variance in a trait attributable to genetic variance, and both quantities depend on the environment. If everyone is exposed to the same uniform environment, environmental variance drops, and heritability appears to rise — not because genes became more important, but because the denominator (total variance) changed. The same trait can have different heritability estimates in different populations or environments."

- question: "A high heritability estimate for a disease means that environmental interventions (diet, lifestyle, medications) will be ineffective because the disease is primarily genetic."
  type: true-false
  answer: false
  explanation: "This is the most common misinterpretation of heritability. High heritability describes the sources of variance *between individuals in the current environment* — it says nothing about whether changing the environment could shift the entire distribution. PKU (phenylketonuria) is nearly 100% heritable yet completely preventable by removing phenylalanine from the diet. Heritability quantifies explanation of existing variation, not immutability."

- question: "Why does studying gene-environment (G×E) interaction require larger sample sizes than studying either genetic or environmental main effects alone?"
  type: short-answer
  answer: "Interaction effects — where the influence of a genetic variant depends on the presence of an environmental exposure — are smaller in effect size and harder to detect than main effects. Statistical tests for interactions have lower power because you are looking for differences in differences: does the genetic variant increase risk more in exposed than unexposed individuals? This requires stratifying the sample by exposure status, which reduces the effective sample size for each stratum, and the interaction term adds an extra degree of freedom."
  explanation: "In practical terms, a GWAS with 100,000 participants may have sufficient power to detect a main-effect SNP with OR = 1.10, but detecting a G×E interaction where the OR is 1.15 in exposed and 1.00 in unexposed might require 500,000+ participants. This is why G×E studies have historically been underpowered and results poorly replicated — the phenomena are real but demand biobank-scale data."
```

## Explainer

In classical epidemiology, you learned to measure disease burden, estimate incidence and prevalence, and distinguish association from causation using study designs like cohort studies and randomized trials. Genetic epidemiology adds a layer: it asks which individuals are genetically more or less susceptible to disease, and how genes interact with the environmental exposures you already know how to study. The foundational concept is **heritability** — but it is easily misunderstood, so a precise definition matters. Heritability (h²) is the proportion of **population-level variance** in a trait that is attributable to genetic variance. It is a property of a population in a specific environment, not a property of a gene. A trait can be 80% heritable and still be dramatically altered by an environmental change — height is highly heritable but Dutch average height rose ~20 cm over a century as nutrition improved.

**Twin studies** are the classical tool for estimating heritability. Monozygotic (MZ) twins share ~100% of their genome; dizygotic (DZ) twins share ~50% on average, like ordinary siblings. If MZ twins are more concordant for a trait than DZ twins, the excess concordance is attributed to genetic factors. The **ACE model** partitions variance into additive genetic effects (A), shared environment (C), and non-shared environment (E). The formula is simple: h² ≈ 2(rMZ − rDZ), where r is the correlation for the trait. This yields estimates like h² ≈ 0.80 for height, h² ≈ 0.50-0.60 for schizophrenia, h² ≈ 0.40-0.60 for Type 2 diabetes. A critical assumption — that MZ and DZ twin pairs experience equally similar environments — has been challenged empirically; MZ twins may be treated more similarly, upwardly biasing heritability estimates for some traits.

**Genome-wide association studies (GWAS)** take the heritability estimate as motivation and then ask: which specific genetic variants account for it? A GWAS genotypes hundreds of thousands to millions of **single nucleotide polymorphisms (SNPs)** across the genome and tests each one for association with a disease or trait, typically in thousands to hundreds of thousands of participants. The significance threshold is very stringent (p < 5 × 10⁻⁸) to correct for multiple testing across the genome. GWAS have identified thousands of robustly replicated loci for complex diseases — but the effect sizes are typically very small (odds ratios of 1.05-1.20), and together they explain only a fraction of the estimated heritability. This **"missing heritability"** puzzle remains active: it likely reflects rare variants not captured by common SNP arrays, gene-gene interactions, and limitations of the additive variance decomposition.

**Gene-environment (G×E) interaction** is the central target of precision public health. A genetic variant may increase risk only in the presence of a specific environmental exposure — or may modify how strongly an exposure raises risk. For example, variants in alcohol-metabolizing genes (ADH1B, ALDH2) dramatically alter whether alcohol consumption causes liver disease, esophageal cancer, and cardiovascular harm. Studying G×E requires large samples (interaction effects are harder to detect than main effects), careful measurement of both genetic and environmental exposures, and attention to confounding — the same epidemiological rigor you learned in foundations, now applied to two simultaneous exposures and their product. The ultimate goal is to identify who is most at risk given their genetic profile and their environment, enabling targeted prevention.
