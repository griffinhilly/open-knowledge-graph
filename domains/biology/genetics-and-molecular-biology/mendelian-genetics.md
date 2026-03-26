---
id: mendelian-genetics
title: Mendelian Genetics
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: meiosis
  type: hard
- id: chromosomal-theory-of-inheritance
  type: hard
- id: simple-probability
  type: soft
- id: ratios
  type: soft
- id: probability-axioms-and-rules
  type: soft
- id: chi-square-test
  type: soft
builds-toward:
- dominance-and-recessiveness
- dihybrid-crosses
- population-genetics-intro
tags:
- Mendel
- law of segregation
- law of independent assortment
- monohybrid cross
- Punnett square
stage: formal-systems
status: validated
---

# Mendelian Genetics

## Core Idea
Gregor Mendel's experiments with pea plants established two fundamental laws of inheritance. The Law of Segregation states that each organism carries two alleles for each trait, and these alleles separate into different gametes during meiosis, each gamete carrying one allele. The Law of Independent Assortment states that alleles of different genes assort independently into gametes — provided those genes are on different (or very distant) chromosomes. Punnett squares and probability calculations derived from these laws predict phenotypic and genotypic ratios among offspring.

## How It's Best Learned
Perform monohybrid and dihybrid Punnett square problems and verify that the 3:1 and 9:3:3:1 ratios emerge from the laws. Work backward from phenotypic ratios to infer parental genotypes.

## Common Misconceptions
- Independent assortment applies only to genes on different chromosomes; linked genes violate this law.
- The 3:1 ratio is the expected average over many offspring, not a guarantee in any single cross.

## Questions

```yaml
- question: "In a monohybrid cross between two heterozygous parents (Aa × Aa), what fraction of offspring are expected to be homozygous recessive (aa)?"
  type: multiple-choice
  options:
    - "1/2"
    - "1/4"
    - "3/4"
    - "0 — two dominant-phenotype parents cannot produce recessive offspring"
  answer: 1
  explanation: "From the Punnett square for Aa × Aa, the four equally probable outcomes are AA, Aa, Aa, aa — giving a 1:2:1 genotypic ratio. Only 1 in 4 offspring is expected to be aa (homozygous recessive). Option D is a common misconception: heterozygous parents show the dominant phenotype but carry one recessive allele, which can be passed to offspring."

- question: "Two genes located on the same chromosome generally follow Mendel's Law of Independent Assortment."
  type: true-false
  answer: false
  explanation: "Independent assortment holds when genes are on different chromosomes (or very far apart on the same chromosome). Genes physically close together on the same chromosome are linked and tend to be inherited together, violating independent assortment. Mendel's original results worked because the seven traits he chose happen to be on different chromosomes or far enough apart to behave independently — he was lucky in his choice of traits."

- question: "A family has four children, all showing the dominant phenotype. Both parents are heterozygous (Aa). Is this result surprising? Why or why not?"
  type: short-answer
  answer: "No, this is not surprising. Each child independently has a 3/4 probability of showing the dominant phenotype. The probability that all four show it is (3/4)⁴ ≈ 0.32, or about 32% — quite common. The 3:1 ratio is an expectation over many offspring, not a guarantee for any specific family."
  explanation: "Mendel's ratios are probabilistic: each offspring is an independent event with fixed probabilities derived from the parents' genotypes. Small sample sizes (like a family of four) frequently deviate from expected ratios. This is why Mendel needed hundreds of plants per cross to reliably observe the 3:1 ratio, and why chi-square tests are used to assess whether observed deviations are within expected random variation."
```

## Explainer

Gregor Mendel's genius was in choosing the right organism, the right traits, and the right quantities. By crossing thousands of pea plants over years and counting offspring carefully, he discovered that inheritance follows predictable mathematical ratios — not a blending of parental traits, as most biologists of his era assumed.

The **Law of Segregation** addresses a single gene. Each organism carries two alleles for each trait (one inherited from each parent). When the organism forms gametes during meiosis, the two alleles separate, so each gamete carries exactly one. If a parent is heterozygous (Aa), half its gametes carry A and half carry a. This is why crossing two heterozygotes (Aa × Aa) yields a 1:2:1 genotypic ratio (AA : Aa : aa) and — if A is dominant — a 3:1 phenotypic ratio. You should think of a Punnett square as a multiplication of two independent probability distributions: each gamete from each parent is chosen independently with known probabilities.

The **Law of Independent Assortment** extends this to two genes simultaneously. If Gene 1 and Gene 2 are on different chromosomes, the allele a gamete inherits at Gene 1 has no effect on which allele it inherits at Gene 2. This is because chromosomes assort independently during meiosis I. A dihybrid cross (AaBb × AaBb) therefore yields a 9:3:3:1 phenotypic ratio — derivable by multiplying the two independent 3:1 ratios: (3A_:1aa) × (3B_:1bb) = 9A_B_:3A_bb:3aaB_:1aabb. This multiplicative structure is exactly the probability rule for independent events you studied in probability.

An important limitation: independent assortment fails for linked genes — genes physically close together on the same chromosome. When chromosomes don't recombine in the region between two genes, those alleles travel together into the same gamete more often than chance would predict. Mendel's original seven traits happened to be on different chromosomes or far enough apart to behave independently — a fortunate accident that let him discover the clean laws. Linkage and recombination, which you will study next, reveal the more complex reality beneath Mendel's elegant rules.

Finally, remember that Mendel's ratios are statements about probability, not guarantees about specific families. Each offspring is an independent event. A 3:1 ratio means each offspring has a 3/4 probability of showing the dominant phenotype. In any small sample — a family of four, say — you will often see 4:0, 2:2, or 3:1 by chance. The expected ratio emerges reliably only across large numbers of crosses, which is why Mendel's sample sizes and statistical intuition were far ahead of his time.
