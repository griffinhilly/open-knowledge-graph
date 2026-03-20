---
id: heritability-broad-sense-narrow-sense
title: 'Heritability: Broad-Sense and Narrow-Sense'
domain: biology
course: ecology-and-evolution
prerequisites:
- id: phenotypic-variation-populations
  type: hard
- id: quantitative-genetics-and-polygenic-traits
  type: soft
builds-toward:
- natural-selection-types-and-examples
- genetic-drift-in-small-populations
tags:
- heritability
- broad-sense
- narrow-sense
- additive-genetic-variance
stage: advanced
status: draft
---

# Heritability: Broad-Sense and Narrow-Sense

## Core Idea
Broad-sense heritability (H²) is the proportion of phenotypic variance due to all genetic effects. Narrow-sense heritability (h²) includes only additive genetic variance and determines the evolutionary response to selection: R = h²S. High heritability does not mean a trait is unmodifiable; context and environment determine whether traits can be changed.

## Explainer

You already know that individuals within a population vary in their phenotypes, and that some of this variation has a genetic basis while some comes from the environment. Heritability puts a number on how much of the phenotypic variation in a population is attributable to genetic differences. The key insight is that heritability is a property of a *population in a particular environment*, not a property of a trait itself. The same trait can have high heritability in one population and low heritability in another if environmental conditions differ.

**Broad-sense heritability** (H²) captures the total genetic contribution to phenotypic variance. It includes additive effects (where each allele contributes independently to the phenotype), dominance effects (where alleles at the same locus interact), and epistatic effects (where alleles at different loci interact). Think of H² as answering the question: "Of all the variation I see in this trait, how much disappears if I could make every individual genetically identical?" H² is useful for clonal organisms and selective breeding of inbred lines, but it has a critical limitation for predicting evolutionary change.

**Narrow-sense heritability** (h²) includes only the **additive genetic variance** — the portion of genetic variation where alleles have predictable, stackable effects on the phenotype. This is the heritability that matters for evolution, because natural selection acts on phenotypes, and only additive effects reliably pass from parent to offspring. The **breeder's equation** R = h²S formalizes this: the evolutionary response to selection (R) equals narrow-sense heritability times the selection differential (S, the difference between the mean of selected parents and the population mean). If h² is zero, no amount of selection will shift the population mean, because the phenotypic variation has no additive genetic basis to transmit.

A common and important trap is interpreting high heritability as meaning a trait is "genetic" and therefore fixed. Consider human height: heritability estimates often exceed 0.8, yet average height has increased dramatically over the past century due to improved nutrition. Heritability tells you about the *sources of variation within a population at a given time* — it says nothing about whether the trait can be changed by altering the environment. Similarly, a heritability of zero does not mean genes are irrelevant to the trait; it means that genetic *differences* do not explain the phenotypic *differences* in that particular population. Keeping these distinctions clear is essential for applying heritability correctly in evolutionary biology, agriculture, and behavioral genetics.
