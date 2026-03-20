---
id: quantitative-genetics-and-polygenic-traits
title: Quantitative Genetics and Polygenic Traits
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: mendelian-genetics
  type: hard
- id: dihybrid-inheritance-and-independent-assortment
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
stage: advanced
status: draft
---

# Quantitative Genetics and Polygenic Traits

## Core Idea
Quantitative traits—controlled by multiple genes with small additive effects plus environmental variation—show continuous phenotypic distributions rather than discrete classes. The number of alleles at multiple loci determines phenotypic range and distribution shape; more loci produce more normal-like distributions. Heritability (h²), the proportion of phenotypic variance due to genetic factors, can be estimated from family data (h² = 2 × correlation between parent and offspring) or twin studies (h² = 2 × (correlation in MZ twins - correlation in DZ twins)). Selection response (R = h² × S, where S is selection differential) predicts breeding outcomes and illustrates the evolutionary significance of heritable variation. Quantitative trait loci (QTL) mapping identifies genomic regions affecting complex traits.

## Explainer

In Mendelian genetics, you learned that a single gene with dominant and recessive alleles produces discrete phenotypic classes — tall or short, purple or white. But most traits you observe in the real world do not sort neatly into two or three bins. Human height, skin color, grain yield in wheat, and blood pressure all show **continuous variation**, forming smooth, bell-shaped distributions across a population. This happens because these traits are influenced by many genes simultaneously — they are **polygenic traits**, and the branch of genetics that studies them is **quantitative genetics**.

The logic extends directly from what you already know about independent assortment. Consider a trait controlled by just two genes, each with two alleles that contribute additively. With one gene (Aa), you get three phenotypic doses: 0, 1, or 2 contributing alleles. With two genes (AaBb × AaBb), the offspring can have 0, 1, 2, 3, or 4 contributing alleles, producing five phenotypic classes in a 1:4:6:4:1 ratio — already beginning to approximate a bell curve. Scale this up to ten or twenty genes, add environmental variation on top, and the discrete steps blur into a smooth, continuous distribution. The **central limit theorem** from your statistics background explains why: the sum of many small, independent effects converges on a normal distribution.

The key analytical concept is **heritability** (h²), which measures what fraction of the total phenotypic variation in a population is attributable to genetic differences. If h² = 0.80 for height, that means 80% of the variation in height among individuals in that population is due to genetic variation, and 20% is due to environmental differences. Crucially, heritability is a population-level statistic, not an individual one — it does not mean 80% of your height is genetic. Heritability can be estimated from correlations between relatives: for parent-offspring data, h² ≈ 2 × the regression slope of offspring phenotype on mid-parent phenotype. Twin studies offer another route: h² ≈ 2 × (r_MZ − r_DZ), where identical twins share all genes and fraternal twins share half on average.

Heritability has a direct practical application in breeding and evolution through the **breeder's equation**: R = h² × S. Here S is the **selection differential** (the difference between the mean of selected parents and the population mean), and R is the **response to selection** (how much the offspring generation shifts). If you select the tallest 10% of wheat plants for replanting and S = 5 cm, a heritability of 0.6 predicts the next generation's mean will shift by 3 cm. This equation links quantitative genetics to evolutionary change — natural selection acts on heritable variation in exactly the same way. Modern **QTL mapping** takes this further by scanning the genome with molecular markers to locate the specific chromosomal regions harboring genes that contribute to quantitative traits, bridging the gap between the statistical framework of quantitative genetics and the molecular reality of individual genes.
