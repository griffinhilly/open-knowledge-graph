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
stage: advanced
status: draft
---

# Sex-Linked Inheritance and X-Linked Genes

## Core Idea
X-linked genes show sex-specific segregation patterns because males (XY) have only one X chromosome (hemizygous), while females (XX) have two. X-linked recessive traits show different frequencies in males and females; hemizygous males expressing recessive alleles produce 1:1 ratios in crosses, whereas heterozygous females produce 1:1:1:1 ratios when crossed to males. Criss-cross inheritance occurs when a trait passes from affected males through carrier females to affected grandsons. Y-linked genes show strict patrilineal inheritance (no segregation or recombination with X). X-inactivation (lyonization) in female mammals randomly silences one X in each cell, creating a mosaic phenotype. Genomic imprinting can further modify X-linked inheritance patterns, especially for X-linked dominant conditions lethal in males.

## Explainer

From your work on Mendelian inheritance and chromosomal theory, you understand that genes on autosomes follow symmetric inheritance patterns — each parent contributes one allele, and the offspring's sex does not affect which alleles they receive. X-linked inheritance breaks this symmetry. The key insight is **hemizygosity**: males have only one X chromosome, so every X-linked allele they carry is expressed, whether it would be dominant or recessive in a female. A male cannot be a "carrier" of an X-linked recessive trait — he either has the allele and shows the phenotype, or he does not have it at all.

This asymmetry produces the distinctive pattern called **criss-cross inheritance**. Consider red-green color blindness, an X-linked recessive trait. An affected father passes his X chromosome to all of his daughters (who receive their Y from him? No — daughters get X from father, Y goes to sons). More precisely: an affected father (X^a Y) passes his X^a to every daughter, making them all carriers (X^A X^a), but passes only Y to sons, so no sons inherit the allele from him. The carrier daughters can then pass X^a to their sons, who — being hemizygous — express the trait. The phenotype thus skips a generation and crosses from one sex to the other: affected grandfather → carrier daughter → affected grandson.

Working out X-linked crosses requires careful attention to gamete production. A carrier female (X^A X^a) produces two types of eggs in equal proportion: X^A and X^a. A normal male (X^A Y) produces X^A and Y gametes. Crossing these yields four equally likely offspring: X^A X^A (normal female), X^A X^a (carrier female), X^A Y (normal male), and X^a Y (affected male). So 50% of sons are affected, but no daughters show the phenotype — though half are carriers. This 1:1 ratio among males, with zero affected females, is the hallmark of X-linked recessive inheritance and is markedly different from autosomal patterns.

**X-inactivation** adds another layer of complexity in females. Because females have two X chromosomes and males have one, mammals equalize X-linked gene dosage by randomly silencing one X in each cell early in development. The silenced X condenses into a **Barr body**. Since inactivation is random and occurs when the embryo has relatively few cells, a heterozygous female becomes a mosaic — patches of cells express one X, and patches express the other. Calico cats are the classic visible example: the orange and black fur patches reflect random inactivation of X chromosomes carrying different coat color alleles. In human genetics, X-inactivation explains why some carrier females show mild symptoms of X-linked conditions — if, by chance, a disproportionate number of cells inactivated the X carrying the normal allele, the mutant allele dominates in those tissues.
