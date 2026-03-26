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
stage: formal-systems
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

## Questions

```yaml
- question: "A man with red-green color blindness (X-linked recessive) has children with a woman who has normal vision and no family history of color blindness. Which of the following best describes the expected outcomes for their children?"
  type: multiple-choice
  options:
    - "All sons will be color blind; all daughters will have normal vision"
    - "All daughters will be carriers; all sons will have normal vision"
    - "Half of sons will be color blind; half of daughters will be carriers"
    - "No children will be color blind; daughters will be obligate carriers"
  answer: 3
  explanation: "The affected father's genotype is X^a Y. The unaffected, non-carrier mother's genotype is X^A X^A. All daughters receive X^a from their father and X^A from their mother — making every daughter a carrier (X^A X^a). All sons receive Y from their father and X^A from their mother — so no son is affected. The common misconception (option A) is that an affected father passes the trait to sons, but sons inherit the Y chromosome from their father, not the X. The X-linked allele from the father goes only to daughters."

- question: "A carrier mother (X^A X^a) and an unaffected father (X^A Y) have children. What is the probability that a son will be color blind?"
  type: multiple-choice
  options:
    - "0% — the father is unaffected, so sons cannot inherit the allele"
    - "25% — one in four children overall will be affected"
    - "50% — each son has a 50% chance of receiving X^a from his mother"
    - "100% — any son of a carrier mother will be affected"
  answer: 2
  explanation: "Sons inherit their X chromosome from their mother (the Y comes from their father). The carrier mother has genotype X^A X^a, so each son has an equal chance of receiving X^A (unaffected) or X^a (affected). Males are hemizygous — receiving X^a with no second X to mask it, they will be color blind. So the probability for each son is 50%. Option A is the classic criss-cross confusion: affected sons do NOT get the allele from their father. Option B confuses the probability for 'any child' with the probability for 'a son specifically.'"

- question: "A female can rarely be affected by an X-linked recessive condition — she can mainly be a carrier."
  type: true-false
  answer: false
  explanation: "Females CAN be affected by X-linked recessive conditions if they are homozygous (X^a X^a) — inheriting the recessive allele from both parents. This requires an affected father (who contributes X^a) and a carrier or affected mother (who also contributes X^a). While this is far rarer than male expression, it does occur. The statement confuses 'less likely' with 'impossible.' Women are affected less frequently because they need two copies of the allele; men are affected with a single copy because they are hemizygous."

- question: "An affected father with an X-linked recessive condition cannot pass the trait directly to any of his sons."
  type: true-false
  answer: true
  explanation: "This is the defining pedigree rule for X-linked recessive inheritance. Fathers pass their Y chromosome to sons and their X chromosome to daughters. An affected father (X^a Y) therefore gives all daughters X^a (making them obligate carriers) and gives all sons Y (passing no X-linked allele whatsoever). Affected sons inherit the allele from their carrier mothers, not their fathers. This 'no father-to-son transmission' pattern is a diagnostic signature in pedigree analysis for X-linked traits."

- question: "Why do X-linked recessive traits appear far more frequently in males than in females, and what condition would be required for a female to be affected?"
  type: short-answer
  answer: "Males are hemizygous — they carry only one X chromosome. A single recessive allele on that X is sufficient to produce the phenotype because there is no second allele to mask it. Females have two X chromosomes and can be heterozygous carriers, with one dominant allele suppressing expression of the recessive allele. For a female to be affected, she must be homozygous (X^a X^a), which requires inheriting the recessive allele from both parents — an affected father and a carrier or affected mother."
  explanation: "The hemizygosity of males is the central concept. It means that the usual dominance/recessiveness logic — requiring two copies of a recessive allele for expression — does not apply to males for X-linked genes. One copy is all they have, so one copy is expressed. This asymmetry between sexes is the key feature distinguishing X-linked inheritance from autosomal inheritance."
```

## Explainer

You already understand dominance and recessiveness from autosomal genetics: a heterozygous individual carrying one dominant and one recessive allele expresses the dominant phenotype. You also know from the chromosomal theory of inheritance that genes physically reside on chromosomes and segregate during meiosis. Sex-linked inheritance builds on both of these ideas but introduces a twist — the X and Y chromosomes are not equal partners, and that asymmetry changes everything about how certain traits are transmitted.

The critical fact is that **males are hemizygous** for X-linked genes. A male has one X chromosome (from his mother) and one Y chromosome (from his father), and the Y carries very few genes — almost none that correspond to genes on the X. This means a male who inherits a single recessive allele on his X chromosome has no second X allele to mask it. He will express the trait. A female, by contrast, has two X chromosomes, so she can be a **heterozygous carrier** — possessing one copy of a recessive allele without showing the phenotype, because her other X carries the dominant allele.

This asymmetry produces distinctive inheritance patterns visible in pedigrees. Consider **red-green color blindness**, an X-linked recessive trait. An affected father (X^a Y) passes his X^a to every daughter, making them all carriers (X^A X^a), but he passes only his Y to sons, so no son inherits the trait from an affected father. Instead, affected sons inherit the allele from their carrier mothers. If a carrier mother (X^A X^a) mates with an unaffected father (X^A Y), each son has a 50% chance of being affected (X^a Y) and each daughter has a 50% chance of being a carrier (X^A X^a). This **criss-cross pattern** — trait passes from affected grandfather through carrier daughter to affected grandson — is the hallmark of X-linked recessive inheritance.

The pedigree signature is unmistakable once you know what to look for: far more males are affected than females, the trait never passes directly from father to son, and every affected male can trace the allele back through his mother. Females can be affected, but only if they are **homozygous** (X^a X^a) — which requires both an affected father and a carrier mother, making it much rarer. When working through pedigree problems, the most reliable approach is to write out full genotypes using the X^A / X^a / Y notation, assign known genotypes first (affected males must be X^a Y, affected females must be X^a X^a), and then deduce carrier status by working backward through the family.
