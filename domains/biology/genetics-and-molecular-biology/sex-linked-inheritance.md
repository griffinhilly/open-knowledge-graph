---
id: sex-linked-inheritance
title: Sex-Linked Inheritance
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: dominance-and-recessiveness
  type: hard
- id: chromosomal-theory-of-inheritance
  type: hard
- id: meiosis
  type: soft
builds-toward:
- genetic-mapping
- non-mendelian-inheritance
tags:
- X-linked
- sex chromosomes
- hemizygous
- carrier
- color blindness
stage: advanced
status: validated
---

# Sex-Linked Inheritance

## Core Idea
Genes located on the X chromosome follow sex-linked (X-linked) inheritance patterns that differ from autosomal patterns. Males are hemizygous for X-linked genes (carrying only one copy), so they express both dominant and recessive X-linked alleles. Females can be heterozygous carriers who do not express the recessive phenotype. Consequently, X-linked recessive traits such as color blindness and hemophilia appear far more frequently in males. Inheritance can be traced through pedigrees by noting that affected fathers cannot pass X-linked traits to sons (since sons receive the Y from father), but all daughters of affected fathers receive the X-linked allele.

## How It's Best Learned
Analyze pedigrees of X-linked recessive traits and identify carriers, affected individuals, and obligate transmitters. Practice writing sex-linked genotypes with correct notation (X^A, X^a, Y).

## Common Misconceptions
- Females can express X-linked recessive traits if they are homozygous (X^a X^a); they are not always just carriers.
- Not all sex-linked traits are X-linked; there are Y-linked (holandric) traits, though they are rare.

## Explainer

You already understand dominance and recessiveness from autosomal genetics: a heterozygous individual carrying one dominant and one recessive allele expresses the dominant phenotype. You also know from the chromosomal theory of inheritance that genes physically reside on chromosomes and segregate during meiosis. Sex-linked inheritance builds on both of these ideas but introduces a twist — the X and Y chromosomes are not equal partners, and that asymmetry changes everything about how certain traits are transmitted.

The critical fact is that **males are hemizygous** for X-linked genes. A male has one X chromosome (from his mother) and one Y chromosome (from his father), and the Y carries very few genes — almost none that correspond to genes on the X. This means a male who inherits a single recessive allele on his X chromosome has no second X allele to mask it. He will express the trait. A female, by contrast, has two X chromosomes, so she can be a **heterozygous carrier** — possessing one copy of a recessive allele without showing the phenotype, because her other X carries the dominant allele.

This asymmetry produces distinctive inheritance patterns visible in pedigrees. Consider **red-green color blindness**, an X-linked recessive trait. An affected father (X^a Y) passes his X^a to every daughter, making them all carriers (X^A X^a), but he passes only his Y to sons, so no son inherits the trait from an affected father. Instead, affected sons inherit the allele from their carrier mothers. If a carrier mother (X^A X^a) mates with an unaffected father (X^A Y), each son has a 50% chance of being affected (X^a Y) and each daughter has a 50% chance of being a carrier (X^A X^a). This **criss-cross pattern** — trait passes from affected grandfather through carrier daughter to affected grandson — is the hallmark of X-linked recessive inheritance.

The pedigree signature is unmistakable once you know what to look for: far more males are affected than females, the trait never passes directly from father to son, and every affected male can trace the allele back through his mother. Females can be affected, but only if they are **homozygous** (X^a X^a) — which requires both an affected father and a carrier mother, making it much rarer. When working through pedigree problems, the most reliable approach is to write out full genotypes using the X^A / X^a / Y notation, assign known genotypes first (affected males must be X^a Y, affected females must be X^a X^a), and then deduce carrier status by working backward through the family.
