---
id: genetic-mapping
title: Genetic Mapping and Linkage
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: dihybrid-crosses
  type: hard
- id: chromosomal-theory-of-inheritance
  type: hard
- id: meiosis
  type: soft
- id: ratios
  type: soft
- id: simple-probability
  type: soft
- id: sex-linked-inheritance
  type: soft
- id: chi-square-test
  type: soft
- id: probability-axioms-and-rules
  type: soft
builds-toward:
- genomics-overview
tags:
- genetic map
- linkage
- recombination frequency
- centimorgans
- crossing over
stage: advanced
status: validated
---
# Genetic Mapping and Linkage

## Core Idea
Genes on the same chromosome are genetically linked and tend to be inherited together, violating independent assortment. However, crossing over during meiosis I exchanges segments between homologous chromosomes, producing recombinant gametes. The recombination frequency — the proportion of recombinant offspring in a testcross — is proportional to the physical distance between loci and is measured in centimorgans (cM), where 1 cM ≈ 1% recombination. By measuring recombination frequencies between many gene pairs, geneticists construct linkage maps that indicate the relative order and spacing of genes along chromosomes.

## How It's Best Learned
Work through two-point and three-point testcross problems, calculating recombination frequencies and constructing a simple linkage map. Note when double crossovers must be accounted for to get accurate distances.

## Common Misconceptions
- 50% recombination between two genes does not mean they are on different chromosomes; it means they assort independently (could be far apart on the same chromosome).
- Genetic distance in cM is not the same as physical distance in base pairs; recombination hot spots compress or expand the relationship.

## Questions

```yaml
- question: "In a testcross involving two linked genes, 18 out of 100 offspring are recombinant. What is the genetic distance between the two loci?"
  type: multiple-choice
  options:
    - "0.18 cM"
    - "1.8 cM"
    - "18 cM"
    - "82 cM"
  answer: 2
  explanation: "Recombination frequency = (recombinant offspring / total offspring) × 100 = (18/100) × 100 = 18%. By definition, 1 cM corresponds to 1% recombination, so the genetic distance is 18 cM. Options A and B confuse the percentage conversion; option D confuses recombinants with parental-type offspring."

- question: "If two genes show a 50% recombination frequency in a testcross, they must be located on different chromosomes."
  type: true-false
  answer: false
  explanation: "50% recombination means the two genes assort independently — but this can happen either because they are on different chromosomes OR because they are very far apart on the same chromosome (with so many crossovers between them that recombinant and parental gametes are equally likely). The 50% value is a ceiling imposed by random crossover placement, not proof of separate chromosomes."

- question: "Why is the maximum measurable recombination frequency between two loci 50%, regardless of how far apart they actually are on a chromosome?"
  type: short-answer
  answer: "When two loci are very far apart, crossovers occur so frequently between them that every gamete has roughly equal chances of being recombinant or parental. Multiple crossovers between the loci cancel each other out statistically, capping the observable recombination frequency at 50% — identical to what you would see for unlinked genes."
  explanation: "This 50% ceiling is why genetic distances estimated from two-point crosses become inaccurate for loci far apart: double (and higher-order) crossovers produce parental-type gametes and are therefore invisible in a simple recombination count. Three-point crosses and mapping functions like Haldane's or Kosambi's correct for this by accounting for the probability of multiple crossovers."
```

## Explainer

The chromosomal theory tells you that genes are on chromosomes and that linked genes tend to be co-inherited. Genetic mapping turns that qualitative observation into a quantitative tool: by measuring how often two linked genes get separated by crossing over, you can estimate how far apart they are on the chromosome.

The key event is crossing over during meiosis I prophase, when homologous chromosomes pair up and their non-sister chromatids physically exchange segments. If a crossover occurs between two loci, the alleles at those loci end up on recombinant chromosomes — combinations that were not present in the parent. If no crossover occurs between the loci, the gametes are parental types. The recombination frequency is simply the fraction of offspring (in a testcross against a homozygous recessive parent) that carry recombinant genotypes. By expressing this fraction as a percentage, you get centimorgans: 1 cM = 1% recombination frequency.

The practical procedure is a testcross. Cross a doubly heterozygous individual (AB/ab) against a homozygous recessive (ab/ab). Because the tester contributes only recessive alleles, the phenotype of each offspring directly reads out the gamete produced by the heterozygous parent. Count the two parental classes (AB and ab) and two recombinant classes (Ab and aB). The recombinant fraction is the map distance. Doing this for many pairs of genes across a chromosome builds up a linkage map showing their relative order and spacing.

There is an important ceiling to understand: the maximum observable recombination frequency is 50%. When two loci are very far apart, crossovers are so frequent between them that half the gametes end up recombinant by chance — indistinguishable from genes on separate chromosomes. This is why a 50% recombination result does not prove that two genes are unlinked; they might simply be far apart on the same chromosome. Three-point crosses help here, because the middle locus's position is informative even when the outer loci are saturated with crossovers.

Genetic distance in cM also does not equal physical distance in base pairs. Recombination hot spots — regions where crossovers are especially likely — can pack many cM into a small physical interval, while cold spots stretch many kilobases into just a centimorgan or two. Modern genomic sequencing has allowed direct comparison of genetic and physical maps, revealing this uneven landscape in detail. The utility of cM maps remains high, however, for predicting co-inheritance of alleles and for locating genes through linkage analysis in pedigrees.
