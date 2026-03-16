---
id: dihybrid-inheritance-and-independent-assortment
title: Dihybrid Crosses and Mendel's Law of Independent Assortment
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: dihybrid-crosses
  type: hard
- id: mendelian-genetics
  type: hard
- id: monohybrid-inheritance-and-segregation
  type: hard
builds-toward:
- test-cross-analysis-determining-genotypes
- epistasis-and-complementary-genes
tags:
- independent-assortment
- 9-3-3-1-ratio
- chromosome-pairs
- dihybrid-test-cross
stage: formal-systems
status: draft
---

# Dihybrid Crosses and Mendel's Law of Independent Assortment

## Core Idea
Dihybrid crosses track two traits simultaneously, controlled by genes on different chromosomes. Mendel's Law of Independent Assortment predicts that different genes assort randomly during meiosis, producing a 9:3:3:1 phenotypic ratio in the F2 generation from a dihybrid cross (AaBb × AaBb): 9 A_B_, 3 A_bb, 3 aaB_, 1 aabb. Independent assortment reflects random segregation of different chromosome pairs during meiosis I. Test crosses (AaBb × aabb) produce a 1:1:1:1 ratio, allowing direct observation of gamete types and frequencies. Extensions to three or more genes demonstrate how to predict ratios for complex crosses using the product rule and branch diagrams, scaling to multi-locus problems.

## Explainer

From monohybrid crosses, you know that a heterozygous individual (Aa) produces gametes carrying A and a in equal proportions — Mendel's Law of Segregation. The dihybrid cross asks: what happens when you track two genes at once? If an individual is AaBb, it must put one allele of each gene into each gamete. The question is whether the A allele's destination influences which B allele travels with it. Mendel's **Law of Independent Assortment** says no — each gene segregates independently, so the AaBb parent produces four gamete types (AB, Ab, aB, ab) in equal frequency: 1/4 each.

The physical basis is the behavior of chromosomes during **meiosis I**. Each pair of homologous chromosomes lines up at the metaphase plate and segregates to opposite poles, but which pole each chromosome goes to is random and independent of every other pair. If the A gene is on chromosome 1 and the B gene is on chromosome 3, then whether chromosome 1's "A-carrying" copy goes left or right has no bearing on which direction chromosome 3's "B-carrying" copy moves. This independence at the chromosome level produces independence at the allele level — and that is what generates equal proportions of all four gamete types.

The classic **9:3:3:1 ratio** emerges when you cross two double heterozygotes (AaBb × AaBb). The easiest way to derive it is with the **product rule**: treat each gene separately as a monohybrid cross. For gene A alone, Aa × Aa gives 3/4 A_ : 1/4 aa. For gene B alone, Bb × Bb gives 3/4 B_ : 1/4 bb. Because the genes assort independently, you multiply the probabilities: P(A_ and B_) = 3/4 × 3/4 = 9/16, P(A_ and bb) = 3/4 × 1/4 = 3/16, P(aa and B_) = 1/4 × 3/4 = 3/16, P(aa and bb) = 1/4 × 1/4 = 1/16. This gives the 9:3:3:1 ratio. The same logic extends to three or more genes — a trihybrid cross (AaBbCc × AaBbCc) produces a 27:9:9:9:3:3:3:1 ratio, and each class can be calculated by multiplying the individual monohybrid probabilities.

The **test cross** is the diagnostic tool. Crossing AaBb × aabb means the homozygous recessive parent contributes only ab gametes, so every offspring's phenotype directly reveals which gamete the AaBb parent produced. If you see four phenotypic classes in a 1:1:1:1 ratio, the two genes are assorting independently. If instead you see an excess of parental combinations and a deficit of recombinant types, the genes are **linked** — located on the same chromosome — and independent assortment does not apply. Recognizing departures from the expected 1:1:1:1 test-cross ratio is exactly how geneticists first discovered linkage and began constructing genetic maps.
