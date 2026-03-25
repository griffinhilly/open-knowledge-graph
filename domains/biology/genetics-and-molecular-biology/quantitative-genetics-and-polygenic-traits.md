---
id: quantitative-genetics-and-polygenic-traits
title: Quantitative Genetics and Polygenic Traits
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: mendelian-genetics
  type: hard
- id: dihybrid-crosses
  type: soft
- id: chi-square-analysis-in-genetics
  type: soft
- id: linear-regression
  type: soft
- id: statistics-probability
  type: soft
tags:
- polygenic-inheritance
- heritability
- selection-response
- quantitative-trait
stage: formal-systems
status: validated
---

# Quantitative Genetics and Polygenic Traits

## Core Idea
Quantitative traits—controlled by multiple genes with small additive effects plus environmental variation—show continuous phenotypic distributions rather than discrete classes. The number of alleles at multiple loci determines phenotypic range and distribution shape; more loci produce more normal-like distributions. Heritability (h²), the proportion of phenotypic variance due to genetic factors, can be estimated from family data (h² = 2 × correlation between parent and offspring) or twin studies (h² = 2 × (correlation in MZ twins - correlation in DZ twins)). Selection response (R = h² × S, where S is selection differential) predicts breeding outcomes and illustrates the evolutionary significance of heritable variation. Quantitative trait loci (QTL) mapping identifies genomic regions affecting complex traits.

## Questions

```yaml
- question: "A study reports that the heritability of height in a large European population is h² = 0.80. Which interpretation is correct?"
  type: multiple-choice
  options:
    - "80% of any individual's height is determined by their genes"
    - "In this population, 80% of the variation in height between individuals is attributable to genetic differences"
    - "80% of the population has their height primarily controlled by genetics"
    - "Environmental factors can account for at most 20% of height in any single person"
  answer: 1
  explanation: "Heritability is a population-level statistic about variance, not an individual-level claim. h² = 0.80 means that 80% of the phenotypic variance in height among people in that population is due to genetic variance. It says nothing about how much of any one person's height is 'caused' by their genes — that question doesn't have a meaningful answer in the same framework."

- question: "A wheat breeder selects plants whose average height is 10 cm above the population mean (selection differential S = 10 cm). If heritability for height is h² = 0.40, what is the predicted mean height gain in the next generation?"
  type: multiple-choice
  options:
    - "40 cm, because the response scales with 1/h²"
    - "10 cm, because the selection differential is fully transmitted"
    - "4 cm, applying the breeder's equation R = h² × S"
    - "25 cm, because h² represents the proportion of variation not lost to environment"
  answer: 2
  explanation: "The breeder's equation R = h² × S gives R = 0.40 × 10 = 4 cm. Only the heritable fraction of the selection differential is transmitted to offspring. The selection differential of 10 cm includes both genetic and environmental components; heritability filters out the non-heritable part."

- question: "A heritability estimate of 0.85 for IQ obtained in one high-income Western population can be directly generalized to predict that IQ heritability will also be near 0.85 in low-income populations with greater environmental variation."
  type: true-false
  answer: false
  explanation: "Heritability is a population-specific statistic that depends on the amount of genetic and environmental variance present in that population. When environmental variation is greater (as in resource-poor settings), a larger fraction of phenotypic variance may be attributable to environment, and h² will be lower. The same trait can have very different heritabilities in different populations or environments."

- question: "Polygenic traits show approximately normal phenotypic distributions in populations partly because the combined effect of many small, independent allele contributions tends toward a normal distribution as the number of loci increases."
  type: true-false
  answer: true
  explanation: "This follows directly from the central limit theorem: the sum of many small, independent random variables — here, the additive contributions of alleles at many loci — converges on a normal distribution as the number of terms grows. With just a few loci, the distribution is stepped; with many loci plus environmental variation, it smooths into a bell curve."

- question: "Explain why heritability is described as a property of a population in a specific environment, rather than a fixed property of a trait. What would happen to the heritability of a trait if all individuals in the population were raised in identical environments?"
  type: short-answer
  answer: "Heritability = V_genetic / V_phenotypic. If all individuals experience identical environments, V_environmental approaches zero, so V_phenotypic ≈ V_genetic, and h² approaches 1.0 — regardless of how 'genetic' the trait really is. Conversely, if a population is genetically homogeneous but environments vary widely, h² approaches zero. This shows that heritability reflects the balance of genetic vs. environmental variance in a particular population and environment, not an intrinsic property of the trait itself."
```

## Explainer

In Mendelian genetics, you learned that a single gene with dominant and recessive alleles produces discrete phenotypic classes — tall or short, purple or white. But most traits you observe in the real world do not sort neatly into two or three bins. Human height, skin color, grain yield in wheat, and blood pressure all show **continuous variation**, forming smooth, bell-shaped distributions across a population. This happens because these traits are influenced by many genes simultaneously — they are **polygenic traits**, and the branch of genetics that studies them is **quantitative genetics**.

The logic extends directly from what you already know about independent assortment. Consider a trait controlled by just two genes, each with two alleles that contribute additively. With one gene (Aa), you get three phenotypic doses: 0, 1, or 2 contributing alleles. With two genes (AaBb × AaBb), the offspring can have 0, 1, 2, 3, or 4 contributing alleles, producing five phenotypic classes in a 1:4:6:4:1 ratio — already beginning to approximate a bell curve. Scale this up to ten or twenty genes, add environmental variation on top, and the discrete steps blur into a smooth, continuous distribution. The **central limit theorem** from your statistics background explains why: the sum of many small, independent effects converges on a normal distribution.

The key analytical concept is **heritability** (h²), which measures what fraction of the total phenotypic variation in a population is attributable to genetic differences. If h² = 0.80 for height, that means 80% of the variation in height among individuals in that population is due to genetic variation, and 20% is due to environmental differences. Crucially, heritability is a population-level statistic, not an individual one — it does not mean 80% of your height is genetic. Heritability can be estimated from correlations between relatives: for parent-offspring data, h² ≈ 2 × the regression slope of offspring phenotype on mid-parent phenotype. Twin studies offer another route: h² ≈ 2 × (r_MZ − r_DZ), where identical twins share all genes and fraternal twins share half on average.

Heritability has a direct practical application in breeding and evolution through the **breeder's equation**: R = h² × S. Here S is the **selection differential** (the difference between the mean of selected parents and the population mean), and R is the **response to selection** (how much the offspring generation shifts). If you select the tallest 10% of wheat plants for replanting and S = 5 cm, a heritability of 0.6 predicts the next generation's mean will shift by 3 cm. This equation links quantitative genetics to evolutionary change — natural selection acts on heritable variation in exactly the same way. Modern **QTL mapping** takes this further by scanning the genome with molecular markers to locate the specific chromosomal regions harboring genes that contribute to quantitative traits, bridging the gap between the statistical framework of quantitative genetics and the molecular reality of individual genes.
