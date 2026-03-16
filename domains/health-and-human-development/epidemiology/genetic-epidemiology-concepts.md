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
stage: advanced
status: draft
---

# Genetic Epidemiology: Heritability and Gene-Environment Interaction

## Core Idea
Genetic epidemiology investigates genetic contributions to disease and gene-environment interactions. Heritability quantifies the proportion of population variance attributable to genetic factors, estimated via twin studies, family aggregation, or genome-wide association studies (GWAS). Understanding genetic susceptibility and its interaction with environmental exposures is essential for precision public health approaches.

## Explainer

In classical epidemiology, you learned to measure disease burden, estimate incidence and prevalence, and distinguish association from causation using study designs like cohort studies and randomized trials. Genetic epidemiology adds a layer: it asks which individuals are genetically more or less susceptible to disease, and how genes interact with the environmental exposures you already know how to study. The foundational concept is **heritability** — but it is easily misunderstood, so a precise definition matters. Heritability (h²) is the proportion of **population-level variance** in a trait that is attributable to genetic variance. It is a property of a population in a specific environment, not a property of a gene. A trait can be 80% heritable and still be dramatically altered by an environmental change — height is highly heritable but Dutch average height rose ~20 cm over a century as nutrition improved.

**Twin studies** are the classical tool for estimating heritability. Monozygotic (MZ) twins share ~100% of their genome; dizygotic (DZ) twins share ~50% on average, like ordinary siblings. If MZ twins are more concordant for a trait than DZ twins, the excess concordance is attributed to genetic factors. The **ACE model** partitions variance into additive genetic effects (A), shared environment (C), and non-shared environment (E). The formula is simple: h² ≈ 2(rMZ − rDZ), where r is the correlation for the trait. This yields estimates like h² ≈ 0.80 for height, h² ≈ 0.50-0.60 for schizophrenia, h² ≈ 0.40-0.60 for Type 2 diabetes. A critical assumption — that MZ and DZ twin pairs experience equally similar environments — has been challenged empirically; MZ twins may be treated more similarly, upwardly biasing heritability estimates for some traits.

**Genome-wide association studies (GWAS)** take the heritability estimate as motivation and then ask: which specific genetic variants account for it? A GWAS genotypes hundreds of thousands to millions of **single nucleotide polymorphisms (SNPs)** across the genome and tests each one for association with a disease or trait, typically in thousands to hundreds of thousands of participants. The significance threshold is very stringent (p < 5 × 10⁻⁸) to correct for multiple testing across the genome. GWAS have identified thousands of robustly replicated loci for complex diseases — but the effect sizes are typically very small (odds ratios of 1.05-1.20), and together they explain only a fraction of the estimated heritability. This **"missing heritability"** puzzle remains active: it likely reflects rare variants not captured by common SNP arrays, gene-gene interactions, and limitations of the additive variance decomposition.

**Gene-environment (G×E) interaction** is the central target of precision public health. A genetic variant may increase risk only in the presence of a specific environmental exposure — or may modify how strongly an exposure raises risk. For example, variants in alcohol-metabolizing genes (ADH1B, ALDH2) dramatically alter whether alcohol consumption causes liver disease, esophageal cancer, and cardiovascular harm. Studying G×E requires large samples (interaction effects are harder to detect than main effects), careful measurement of both genetic and environmental exposures, and attention to confounding — the same epidemiological rigor you learned in foundations, now applied to two simultaneous exposures and their product. The ultimate goal is to identify who is most at risk given their genetic profile and their environment, enabling targeted prevention.
