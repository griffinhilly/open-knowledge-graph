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
tags:
- heritability
- broad-sense
- narrow-sense
- additive-genetic-variance
stage: formal-systems
status: validated
---

# Heritability: Broad-Sense and Narrow-Sense

## Core Idea
Broad-sense heritability (H²) is the proportion of phenotypic variance due to all genetic effects. Narrow-sense heritability (h²) includes only additive genetic variance and determines the evolutionary response to selection: R = h²S. High heritability does not mean a trait is unmodifiable; context and environment determine whether traits can be changed.

## Questions

```yaml
- question: "Narrow-sense heritability (h²) for wheat grain yield in a farming region is 0.6, and the mean yield of selected high-yielding parents is 10 kg/plot above the population mean. What is the predicted response to selection (R)?"
  type: multiple-choice
  options:
    - "10 kg/plot — response equals the selection differential"
    - "6 kg/plot — response equals h² × S"
    - "0.6 kg/plot — response equals h² divided by S"
    - "16.7 kg/plot — response equals S divided by h²"
  answer: 1
  explanation: "The breeder's equation is R = h²S. With h² = 0.6 and S = 10, R = 0.6 × 10 = 6 kg/plot. Option A mistakes the selection differential for the response — that would only hold if h² = 1 (all phenotypic variation is additive genetic). The key insight is that only the additive fraction of phenotypic variation passes reliably from parent to offspring, so the response is always less than or equal to the selection differential."

- question: "Average human height has increased by roughly 10 cm over the past century due to improved nutrition. Narrow-sense heritability (h²) of height is approximately 0.8. These facts together imply which of the following?"
  type: multiple-choice
  options:
    - "A contradiction — high heritability means height is genetically fixed and cannot respond to environmental change"
    - "That heritability has declined over the century as the environment became more important"
    - "No contradiction — heritability measures sources of variation within a population, not whether a trait can be altered by the environment"
    - "That the height increase must have a genetic cause, since heritability is so high"
  answer: 2
  explanation: "High heritability means that most of the variation in height *among individuals in that population at that time* is explained by genetic differences — it says nothing about whether the trait can change in response to environmental interventions. Improved nutrition raised average height by shifting the entire distribution, not by changing the heritability. Option A is the classic misinterpretation. Option D reverses the logic: the secular trend in height is driven by environmental (nutritional) change, not genetic change, which is why it happened too fast for natural selection to explain."

- question: "A heritability estimate of zero for a trait in a given population means that genes play no role in producing that trait."
  type: true-false
  answer: false
  explanation: "Heritability measures the proportion of phenotypic *variance* attributable to genetic *differences* among individuals in a population. A heritability of zero means that genetic differences don't explain the observed variation — perhaps because everyone in the population shares the same relevant genotypes, or because environmental variation swamps genetic variation. Genes may still be absolutely necessary for the trait (you can't have the trait without the relevant genes), but if genetic variation is absent or irrelevant, heritability is zero. The concept measures differences, not presence/absence of genetic involvement."

- question: "Broad-sense heritability (H²) is always at least as large as narrow-sense heritability (h²) for the same trait in the same population."
  type: true-false
  answer: true
  explanation: "H² = V_G / V_P where V_G includes all genetic variance (additive + dominance + epistatic). h² = V_A / V_P where V_A is only the additive component. Since V_A is a subset of V_G, we always have V_A ≤ V_G and therefore h² ≤ H². They are equal only when all genetic variance is additive (no dominance or epistatic effects). In practice, traits with significant dominance or epistasis show H² substantially larger than h²."

- question: "Why is narrow-sense heritability (h²) more relevant than broad-sense heritability (H²) for predicting how a trait will respond to natural selection or selective breeding?"
  type: short-answer
  answer: "Because only additive genetic effects are reliably transmitted from parent to offspring. Dominance effects depend on which alleles pair together in each individual, and epistatic effects depend on combinations across loci — both are disrupted by segregation and recombination during reproduction. Additive effects, by contrast, contribute independently and predictably to offspring phenotypes. The breeder's equation R = h²S uses h² (not H²) precisely because only the additive fraction of genetic variance produces a heritable correlation between parent and offspring phenotypes."
  explanation: "H² can be high due to dominance and epistasis, creating the false impression that selection will produce rapid change. But if most of the genetic variance is non-additive, selected parents won't reliably pass their phenotypic advantage to their offspring, and selection response will be weak. This is why h² is the key parameter for animal and plant breeders and for evolutionary biologists modeling quantitative trait evolution."
```

## Explainer

You already know that individuals within a population vary in their phenotypes, and that some of this variation has a genetic basis while some comes from the environment. Heritability puts a number on how much of the phenotypic variation in a population is attributable to genetic differences. The key insight is that heritability is a property of a *population in a particular environment*, not a property of a trait itself. The same trait can have high heritability in one population and low heritability in another if environmental conditions differ.

**Broad-sense heritability** (H²) captures the total genetic contribution to phenotypic variance. It includes additive effects (where each allele contributes independently to the phenotype), dominance effects (where alleles at the same locus interact), and epistatic effects (where alleles at different loci interact). Think of H² as answering the question: "Of all the variation I see in this trait, how much disappears if I could make every individual genetically identical?" H² is useful for clonal organisms and selective breeding of inbred lines, but it has a critical limitation for predicting evolutionary change.

**Narrow-sense heritability** (h²) includes only the **additive genetic variance** — the portion of genetic variation where alleles have predictable, stackable effects on the phenotype. This is the heritability that matters for evolution, because natural selection acts on phenotypes, and only additive effects reliably pass from parent to offspring. The **breeder's equation** R = h²S formalizes this: the evolutionary response to selection (R) equals narrow-sense heritability times the selection differential (S, the difference between the mean of selected parents and the population mean). If h² is zero, no amount of selection will shift the population mean, because the phenotypic variation has no additive genetic basis to transmit.

A common and important trap is interpreting high heritability as meaning a trait is "genetic" and therefore fixed. Consider human height: heritability estimates often exceed 0.8, yet average height has increased dramatically over the past century due to improved nutrition. Heritability tells you about the *sources of variation within a population at a given time* — it says nothing about whether the trait can be changed by altering the environment. Similarly, a heritability of zero does not mean genes are irrelevant to the trait; it means that genetic *differences* do not explain the phenotypic *differences* in that particular population. Keeping these distinctions clear is essential for applying heritability correctly in evolutionary biology, agriculture, and behavioral genetics.
