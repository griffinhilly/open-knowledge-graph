---
id: dihybrid-crosses
title: Dihybrid Crosses and Independent Assortment
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: dominance-and-recessiveness
  type: hard
- id: mendelian-genetics
  type: hard
- id: simple-probability
  type: soft
- id: combinations
  type: soft
- id: probability-axioms-and-rules
  type: soft
builds-toward:
- genetic-mapping
tags:
- dihybrid cross
- independent assortment
- 9:3:3:1 ratio
- gamete formation
stage: abstract-reasoning
status: validated
---

# Dihybrid Crosses and Independent Assortment

## Core Idea
A dihybrid cross tracks the simultaneous inheritance of two independent gene loci. When two heterozygous parents (AaBb × AaBb) are crossed, the 16-square Punnett grid predicts the classic 9:3:3:1 phenotypic ratio among offspring. This ratio arises because each locus independently segregates and assorts, and the two loci contribute multiplicatively to the outcome. Deviations from 9:3:3:1 signal either gene linkage (loci on the same chromosome) or epistasis (allele interaction between loci). Forked-line (branch diagram) methods provide an efficient alternative to large Punnett squares.

## How It's Best Learned
Complete a full 16-square Punnett grid for a dihybrid cross and tally the phenotypic classes. Then use the forked-line method for the same cross and confirm the results match.

## Common Misconceptions
- Students sometimes apply the 9:3:3:1 ratio even when genes are linked, where it does not apply.
- Each locus still segregates 3:1 on its own; the 9:3:3:1 ratio is the product of two independent 3:1 ratios.

## Explainer

You already know from Mendelian genetics that a monohybrid cross between two heterozygotes (Aa × Aa) produces a 3:1 phenotypic ratio — three dominant to one recessive. A **dihybrid cross** asks what happens when you track two genes at the same time. The key insight from Mendel's **law of independent assortment** is that alleles at different loci segregate into gametes independently of each other, provided the genes are on different chromosomes (or far apart on the same chromosome). This means you can treat each gene separately and then multiply the results.

Consider a cross between two plants heterozygous for both seed shape (Rr) and seed color (Yy): RrYy × RrYy. A heterozygous parent can produce four types of gametes — RY, Ry, rY, and ry — each with equal probability of 1/4. You can verify this by thinking about meiosis: the R and r alleles segregate independently of the Y and y alleles, so all four combinations are equally likely. When two such parents cross, combining 4 gamete types from each parent gives 4 × 4 = 16 equally likely offspring combinations. Drawing these out in a **16-square Punnett grid** and tallying the phenotypes gives the classic **9:3:3:1 ratio**: 9 showing both dominant traits, 3 showing the first dominant and second recessive, 3 showing the first recessive and second dominant, and 1 showing both recessive traits.

The **forked-line method** (also called the branch diagram) provides a faster alternative that makes the multiplicative logic explicit. First, solve the monohybrid ratio for gene 1: 3/4 dominant, 1/4 recessive. Then, for each of those outcomes, branch into the monohybrid ratio for gene 2: 3/4 dominant, 1/4 recessive. Multiplying along each branch gives 9/16, 3/16, 3/16, and 1/16 — the same 9:3:3:1 result without drawing 16 squares. This method scales easily to trihybrid or even higher crosses: a trihybrid gives 27:9:9:9:3:3:3:1, which is simply three independent 3:1 ratios multiplied together (yielding 64 combinations total).

The real power of the 9:3:3:1 ratio is as a **null hypothesis**. When you observe offspring from a dihybrid cross and the ratio deviates significantly from 9:3:3:1, something interesting is happening. If you see a 3:1 ratio for one phenotypic class where you expected two separate classes, the genes may be **linked** — located close together on the same chromosome, so they do not assort independently. If you see modified ratios like 9:7, 12:3:1, or 9:3:4, the genes likely show **epistasis**, where the product of one gene influences the expression of another. In each case, the deviation tells you something about the biological relationship between the two genes that the 9:3:3:1 baseline would not reveal. Mastering the expected ratio is therefore the essential first step to recognizing and interpreting departures from it.
