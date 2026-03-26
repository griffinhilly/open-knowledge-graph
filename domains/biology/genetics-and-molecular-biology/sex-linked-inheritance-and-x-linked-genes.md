---
id: sex-linked-inheritance-and-x-linked-genes
title: Sex-Linked Inheritance and X-Linked Genes
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: sex-linked-inheritance
  type: hard
- id: monohybrid-inheritance-and-segregation
  type: soft
- id: chromosomal-theory-of-inheritance
  type: soft
builds-toward:
- x-inactivation-and-dosage-compensation
- genomic-imprinting-and-parent-of-origin-effects
tags:
- x-linked
- hemizygous
- y-linked
- criss-cross-inheritance
stage: formal-systems
status: validated
---

# Sex-Linked Inheritance and X-Linked Genes

## Core Idea
X-linked genes show sex-specific segregation patterns because males (XY) have only one X chromosome (hemizygous), while females (XX) have two. X-linked recessive traits show different frequencies in males and females; hemizygous males expressing recessive alleles produce 1:1 ratios in crosses, whereas heterozygous females produce 1:1:1:1 ratios when crossed to males. Criss-cross inheritance occurs when a trait passes from affected males through carrier females to affected grandsons. Y-linked genes show strict patrilineal inheritance (no segregation or recombination with X). X-inactivation (lyonization) in female mammals randomly silences one X in each cell, creating a mosaic phenotype. Genomic imprinting can further modify X-linked inheritance patterns, especially for X-linked dominant conditions lethal in males.

## Questions

```yaml
- question: "A woman who is a carrier for X-linked red-green color blindness (X^A X^a) has children with a man who has normal color vision (X^A Y). What fraction of their sons will be color blind?"
  type: multiple-choice
  options:
    - "1/4, because both parents contribute alleles and only one in four offspring combinations produces an affected male"
    - "1/2, because the carrier mother passes X^a to half her sons, who — being hemizygous — immediately express the trait"
    - "0, because the father has normal color vision and sons inherit his Y chromosome, not his X with the recessive allele"
    - "All sons, because X-linked recessive traits always affect every male offspring when the mother is a carrier"
  answer: 1
  explanation: "The carrier mother (X^A X^a) produces X^A and X^a eggs in equal proportion. Sons inherit their X from their mother and Y from their father. Sons receiving X^a are hemizygous — they have no second X allele to mask the recessive — so they express the trait. Sons receiving X^A are unaffected. Therefore exactly 1/2 of sons are color blind. Option C is a common error: sons do not inherit their X from their father; they inherit the Y. The father's X-linked genotype has no bearing on his sons' X-linked traits."

- question: "A clinician observes that a grandfather has an X-linked recessive disease, his son is unaffected, but his grandson (the son's son) is affected. What inheritance pattern explains how the disease jumped a generation in the male line?"
  type: multiple-choice
  options:
    - "The disease is recessive, so it was hidden in every intermediate generation by dominant alleles from both X chromosomes"
    - "Criss-cross inheritance: the grandfather passed his X^a to his daughter (an obligate carrier), who passed it to her son — the allele passed through a carrier female between two affected males"
    - "The grandson independently acquired the allele through a new spontaneous mutation unrelated to his great-grandfather"
    - "X-linked conditions can spontaneously reappear after skipping several male generations because of meiotic recombination between the allele and its centromere"
  answer: 1
  explanation: "This is the defining pattern of criss-cross inheritance in X-linked recessive conditions. The grandfather (X^a Y) passed his X^a to all his daughters, making them obligate carriers (X^A X^a). His son received the Y — no X-linked disease allele. The carrier daughter then passed X^a to her son, who is hemizygous and expresses the trait. The allele skipped a generation in the male line by traveling through a carrier female. The grandfather-to-grandson transmission through carrier daughters is the hallmark pattern."

- question: "An affected father (X^a Y) with an X-linked recessive condition passes his disease allele to his sons, potentially making them affected as well."
  type: true-false
  answer: false
  explanation: "Fathers pass their Y chromosome to sons and their X chromosome to daughters. An affected father (X^a Y) therefore passes X^a to every daughter — making them all obligate carriers — but passes only Y to sons, so no son inherits the disease allele from him. This asymmetry is the defining feature of X-linked inheritance: the allele cannot pass directly from affected father to affected son. It must traverse a generation through a carrier daughter first."

- question: "Because X-inactivation is random, heterozygous carrier females will generally have exactly 50% of their cells expressing the mutant allele, producing a predictable intermediate phenotype that is consistent across most carriers."
  type: true-false
  answer: false
  explanation: "X-inactivation is random but occurs early in embryonic development when the embryo has very few cells. The clonal expansion that follows those few founding cells means the actual ratio of cells expressing each X can deviate substantially from 50:50 by chance — a phenomenon called skewed X-inactivation. Some carrier females may have >80% of cells expressing the mutant allele and show significant symptoms; others may be essentially unaffected. This explains why X-linked conditions show variable expressivity in carrier females."

- question: "Why can males never be 'carriers' of X-linked recessive traits, and how does this explain why X-linked recessive diseases are far more common in males than in females?"
  type: short-answer
  answer: "Males have only one X chromosome (they are hemizygous for X-linked loci). Every allele they carry on that X is expressed directly — there is no second X allele that could mask a recessive allele. A male either carries the recessive allele and expresses the phenotype, or does not carry it. 'Carrier' status requires being heterozygous — having one dominant and one recessive allele — which is only possible with two copies of the locus. Females, with two X chromosomes, can carry the recessive allele on one X while the dominant allele on the other X prevents expression; these females are carriers without being affected. Because a female must receive the recessive allele from both parents to be affected, and a male needs only one copy from his mother, X-linked recessive conditions are overwhelmingly more common in males."
  explanation: "This hemizygosity principle is the master key to X-linked inheritance patterns. Once a student truly grasps that males cannot be carriers, the asymmetric frequencies, the criss-cross pattern, and the obligate carrier status of daughters of affected fathers all follow directly."
```

## Explainer

From your work on Mendelian inheritance and chromosomal theory, you understand that genes on autosomes follow symmetric inheritance patterns — each parent contributes one allele, and the offspring's sex does not affect which alleles they receive. X-linked inheritance breaks this symmetry. The key insight is **hemizygosity**: males have only one X chromosome, so every X-linked allele they carry is expressed, whether it would be dominant or recessive in a female. A male cannot be a "carrier" of an X-linked recessive trait — he either has the allele and shows the phenotype, or he does not have it at all.

This asymmetry produces the distinctive pattern called **criss-cross inheritance**. Consider red-green color blindness, an X-linked recessive trait. An affected father passes his X chromosome to all of his daughters (who receive their Y from him? No — daughters get X from father, Y goes to sons). More precisely: an affected father (X^a Y) passes his X^a to every daughter, making them all carriers (X^A X^a), but passes only Y to sons, so no sons inherit the allele from him. The carrier daughters can then pass X^a to their sons, who — being hemizygous — express the trait. The phenotype thus skips a generation and crosses from one sex to the other: affected grandfather → carrier daughter → affected grandson.

Working out X-linked crosses requires careful attention to gamete production. A carrier female (X^A X^a) produces two types of eggs in equal proportion: X^A and X^a. A normal male (X^A Y) produces X^A and Y gametes. Crossing these yields four equally likely offspring: X^A X^A (normal female), X^A X^a (carrier female), X^A Y (normal male), and X^a Y (affected male). So 50% of sons are affected, but no daughters show the phenotype — though half are carriers. This 1:1 ratio among males, with zero affected females, is the hallmark of X-linked recessive inheritance and is markedly different from autosomal patterns.

**X-inactivation** adds another layer of complexity in females. Because females have two X chromosomes and males have one, mammals equalize X-linked gene dosage by randomly silencing one X in each cell early in development. The silenced X condenses into a **Barr body**. Since inactivation is random and occurs when the embryo has relatively few cells, a heterozygous female becomes a mosaic — patches of cells express one X, and patches express the other. Calico cats are the classic visible example: the orange and black fur patches reflect random inactivation of X chromosomes carrying different coat color alleles. In human genetics, X-inactivation explains why some carrier females show mild symptoms of X-linked conditions — if, by chance, a disproportionate number of cells inactivated the X carrying the normal allele, the mutant allele dominates in those tissues.
