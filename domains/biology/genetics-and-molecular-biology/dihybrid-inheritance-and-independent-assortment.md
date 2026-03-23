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

## Questions

```yaml
- question: "A cross between two dihybrid parents (AaBb × AaBb) is performed. What fraction of offspring are expected to show both dominant phenotypes (A_B_)?"
  type: multiple-choice
  options:
    - "1/2"
    - "3/4"
    - "9/16"
    - "1/4"
  answer: 2
  explanation: "By the product rule, each gene is treated independently as a monohybrid cross. Aa × Aa produces 3/4 A_ offspring, and Bb × Bb produces 3/4 B_ offspring. Because the genes assort independently, P(A_ and B_) = 3/4 × 3/4 = 9/16. Option A (1/2) is a common error from treating both genes together as if they behaved like a single heterozygous locus."

- question: "A researcher performs a test cross (AaBb × aabb) on two trait pairs. In experiment 1, offspring appear in roughly equal proportions of all four phenotypic classes. In experiment 2 with a different trait pair, offspring are mostly parental types (AB and ab) with very few recombinant types (Ab and aB). What do the results of experiment 2 indicate?"
  type: multiple-choice
  options:
    - "The second pair of genes violates the law of segregation"
    - "The two genes in the second cross are located on the same chromosome"
    - "The dominant alleles are more likely to be co-inherited due to allelic attraction"
    - "The second test cross had too few offspring to draw reliable conclusions"
  answer: 1
  explanation: "The 1:1:1:1 ratio in experiment 1 confirms independent assortment — all four gamete types are produced equally. The excess of parental combinations (AB, ab) and deficit of recombinant types (Ab, aB) in experiment 2 is the hallmark of gene linkage. When two genes reside on the same chromosome, their alleles tend to travel together during meiosis unless separated by recombination, producing a departure from the expected 1:1:1:1 ratio. Recognizing this deviation is exactly how geneticists first discovered linkage and began constructing genetic maps."

- question: "The 9:3:3:1 phenotypic ratio in a dihybrid F2 cross can be derived by treating each gene as an independent monohybrid cross and multiplying the resulting probabilities."
  type: true-false
  answer: true
  explanation: "This is the product rule in action. Because independent assortment means alleles at one locus segregate without influencing alleles at another, the probability of any two-locus outcome equals the product of the single-locus probabilities. For Aa × Aa, P(A_) = 3/4; for Bb × Bb, P(B_) = 3/4. Multiplying: P(A_B_) = 9/16, P(A_bb) = 3/16, P(aaB_) = 3/16, P(aabb) = 1/16 — yielding the 9:3:3:1 ratio. The product rule works precisely because the two events are independent."

- question: "Independent assortment applies to all pairs of genes in a diploid organism, regardless of their chromosomal location."
  type: true-false
  answer: false
  explanation: "Independent assortment only holds for genes on different (non-homologous) chromosomes. Genes on the same chromosome are physically linked and tend to be inherited together, producing departures from the expected 9:3:3:1 (F2) or 1:1:1:1 (test cross) ratios. The physical basis of independent assortment is the random orientation of homologous chromosome pairs at the metaphase plate during meiosis I — each pair orients independently of the others, but genes on the same chromosome ride the same chromosome and are not independent unless separated by crossing over."

- question: "Why does independent assortment produce equal frequencies of all four gamete types (AB, Ab, aB, ab) in a dihybrid parent (AaBb), and what is the physical chromosomal mechanism behind this?"
  type: short-answer
  answer: "In a dihybrid individual (AaBb), the A gene and the B gene reside on different chromosomes. During meiosis I, each homologous pair lines up at the metaphase plate and segregates to opposite poles independently of every other pair. Whether the A-carrying chromosome goes to the left pole or the right has no bearing on which pole the B-carrying chromosome moves toward. This random, independent segregation produces all four gamete combinations (AB, Ab, aB, ab) in equal proportion (1/4 each). If the two genes were on the same chromosome, their alleles would tend to travel together and gamete frequencies would no longer be equal."
  explanation: "The equal gamete frequencies are not an assumption but a consequence of meiotic chromosome behavior. Mendel discovered this ratio empirically decades before chromosomes were identified as the physical carriers of genes. This independence of different chromosome pairs is what makes the product rule valid for calculating multi-locus probabilities."
```

## Explainer

From monohybrid crosses, you know that a heterozygous individual (Aa) produces gametes carrying A and a in equal proportions — Mendel's Law of Segregation. The dihybrid cross asks: what happens when you track two genes at once? If an individual is AaBb, it must put one allele of each gene into each gamete. The question is whether the A allele's destination influences which B allele travels with it. Mendel's **Law of Independent Assortment** says no — each gene segregates independently, so the AaBb parent produces four gamete types (AB, Ab, aB, ab) in equal frequency: 1/4 each.

The physical basis is the behavior of chromosomes during **meiosis I**. Each pair of homologous chromosomes lines up at the metaphase plate and segregates to opposite poles, but which pole each chromosome goes to is random and independent of every other pair. If the A gene is on chromosome 1 and the B gene is on chromosome 3, then whether chromosome 1's "A-carrying" copy goes left or right has no bearing on which direction chromosome 3's "B-carrying" copy moves. This independence at the chromosome level produces independence at the allele level — and that is what generates equal proportions of all four gamete types.

The classic **9:3:3:1 ratio** emerges when you cross two double heterozygotes (AaBb × AaBb). The easiest way to derive it is with the **product rule**: treat each gene separately as a monohybrid cross. For gene A alone, Aa × Aa gives 3/4 A_ : 1/4 aa. For gene B alone, Bb × Bb gives 3/4 B_ : 1/4 bb. Because the genes assort independently, you multiply the probabilities: P(A_ and B_) = 3/4 × 3/4 = 9/16, P(A_ and bb) = 3/4 × 1/4 = 3/16, P(aa and B_) = 1/4 × 3/4 = 3/16, P(aa and bb) = 1/4 × 1/4 = 1/16. This gives the 9:3:3:1 ratio. The same logic extends to three or more genes — a trihybrid cross (AaBbCc × AaBbCc) produces a 27:9:9:9:3:3:3:1 ratio, and each class can be calculated by multiplying the individual monohybrid probabilities.

The **test cross** is the diagnostic tool. Crossing AaBb × aabb means the homozygous recessive parent contributes only ab gametes, so every offspring's phenotype directly reveals which gamete the AaBb parent produced. If you see four phenotypic classes in a 1:1:1:1 ratio, the two genes are assorting independently. If instead you see an excess of parental combinations and a deficit of recombinant types, the genes are **linked** — located on the same chromosome — and independent assortment does not apply. Recognizing departures from the expected 1:1:1:1 test-cross ratio is exactly how geneticists first discovered linkage and began constructing genetic maps.
