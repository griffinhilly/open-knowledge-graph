---
id: test-cross-analysis-determining-genotypes
title: 'Test Crosses: Determining Unknown Genotypes'
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: mendelian-genetics
  type: hard
- id: monohybrid-inheritance-and-segregation
  type: hard
- id: dihybrid-inheritance-and-independent-assortment
  type: soft
builds-toward:
- genetic-recombination-and-linkage-mapping
- chi-square-analysis-in-genetics
tags:
- test-cross
- backcross
- homozygous-recessive
- gamete-frequency
stage: formal-systems
status: draft
---

# Test Crosses: Determining Unknown Genotypes

## Core Idea
Test crosses (crossing an individual of unknown genotype with a homozygous recessive) reveal the gamete types produced by the heterozygous parent, directly exposing the genotype. The ratio of offspring classes reflects the frequencies of gamete types; for example, a monohybrid cross Aa × aa produces 1 Aa : 1 aa (1:1 phenotypic ratio), while a dihybrid AaBb × aabb produces 1 AaBb : 1 Aabb : 1 aaBb : 1 aabb (1:1:1:1). This method is powerful for determining whether genes are linked (deviation from expected ratios), and if linked, for estimating recombination frequency. Working with multiple test crosses allows construction of genetic maps and linear ordering of genes on chromosomes.

## Explainer

From Mendelian genetics you know that organisms carry two alleles for each gene, and that a dominant phenotype can mask the underlying genotype — a tall pea plant might be TT or Tt, and you cannot tell just by looking. The **test cross** is the classic experimental method for solving this problem. The strategy is elegantly simple: cross the individual of unknown genotype with a **homozygous recessive** individual (tt). Because the recessive parent can only contribute recessive alleles (t) to every offspring, the offspring phenotypes directly reveal what alleles the unknown parent donated. If the unknown parent is TT, every offspring gets one T and shows the dominant phenotype. If the unknown parent is Tt, half the offspring get T and half get t, producing a **1:1 phenotypic ratio** of dominant to recessive. The homozygous recessive parent acts like a genetic mirror — it contributes nothing to obscure the picture.

The power of the test cross becomes even clearer when you extend it to two genes simultaneously, building on your knowledge of dihybrid crosses and independent assortment. Cross an individual of unknown genotype (potentially AaBb) with a double homozygous recessive (aabb). If the two genes assort independently, you expect four offspring classes in equal proportions — **1:1:1:1** — representing the four possible gamete types (AB, Ab, aB, ab) from the heterozygous parent. Each offspring class directly corresponds to one gamete type, because the aabb parent contributes only recessive alleles. This makes the test cross a direct readout of gamete frequencies, which is why it is so powerful.

The real diagnostic value emerges when the results deviate from the expected 1:1:1:1 ratio. If two genes are **linked** — located on the same chromosome — they tend to be inherited together rather than assorting independently. In a test cross, linked genes produce an excess of **parental-type** offspring (combinations matching the original parent's chromosome arrangement) and a deficit of **recombinant-type** offspring (new combinations produced by crossing over). The **recombination frequency** — recombinants divided by total offspring — estimates the genetic distance between the two genes. A recombination frequency of 10% means the genes are about 10 map units (centimorgans) apart. By performing test crosses with multiple gene pairs and comparing recombination frequencies, you can determine the linear order of genes along a chromosome and build a **genetic map**. This is why the test cross is not just a diagnostic tool for individual genotypes — it is the foundational method of classical gene mapping.
