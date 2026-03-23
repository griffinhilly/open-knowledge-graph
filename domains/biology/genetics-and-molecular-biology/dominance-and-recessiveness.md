---
id: dominance-and-recessiveness
title: Dominance, Recessiveness, and Allelic Interactions
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: mendelian-genetics
  type: hard
builds-toward:
- non-mendelian-inheritance
- dihybrid-crosses
- sex-linked-inheritance
tags:
- dominance
- recessiveness
- allele
- genotype
- phenotype
- heterozygote
stage: formal-systems
status: validated
---

# Dominance, Recessiveness, and Allelic Interactions

## Core Idea
An allele is dominant when its phenotype appears in a heterozygote (Aa), masking the expression of the recessive allele. Dominance reflects molecular mechanisms: often the dominant allele produces a functional protein and the recessive allele does not, so one functional copy is sufficient. The genotype describes the two alleles present; the phenotype is the observable trait. Homozygous dominant (AA) and heterozygous (Aa) individuals share the same phenotype under complete dominance, but heterozygotes can be identified through test crosses with homozygous recessive (aa) individuals.

## How It's Best Learned
Work through test cross problems to determine unknown genotypes. Connect dominant/recessive patterns to molecular mechanisms such as loss-of-function vs. gain-of-function mutations.

## Common Misconceptions
- Dominant does not mean more common in a population; many dominant alleles are rare.
- Recessive traits are not 'weaker'; they are simply masked in heterozygotes.

## Questions

```yaml
- question: "A pea plant shows tall stem height (the dominant phenotype). You want to determine whether it is TT or Tt. Which cross would conclusively reveal heterozygosity, and what result would confirm it?"
  type: multiple-choice
  options:
    - "Cross with another tall plant; if any short offspring appear, the original was heterozygous"
    - "Cross with a homozygous recessive (tt) plant; if any short offspring appear, the original was heterozygous (Tt)"
    - "Cross with a homozygous recessive (tt) plant; if all offspring are tall, the original is definitively TT"
    - "Self-fertilize; a 3:1 ratio proves the original was Tt"
  answer: 1
  explanation: "The test cross — mating an unknown genotype with the homozygous recessive (tt) — is the definitive tool. A Tt × tt cross yields 50% Tt (tall) and 50% tt (short); any short offspring prove the unknown parent contributed a t allele, confirming Tt. Option 2 is incomplete: all-tall offspring from a test cross make TT probable but not certain with small samples (by chance, a Tt × tt cross could produce all tall offspring). Option 0 is insufficient because crossing two tall plants (both possibly Tt) might yield 0 short offspring by chance."

- question: "A geneticist discovers a new dominant disorder and says: 'This allele must be common in the population since dominant alleles always spread quickly.' Why is this reasoning flawed?"
  type: multiple-choice
  options:
    - "Dominant alleles cannot cause disease — only recessive alleles cause genetic disorders"
    - "Allele frequency is determined by selection, genetic drift, and mutation rate — not by dominance. Many dominant alleles are rare; many recessive alleles are common"
    - "The disorder being dominant means heterozygotes are always affected, which would rapidly eliminate the allele"
    - "Dominant alleles only spread quickly in small populations, not large ones"
  answer: 1
  explanation: "Dominance and population frequency are completely independent. Huntington's disease is caused by a dominant allele yet is rare because it reduces fitness after reproductive age. The sickle cell allele is recessive yet common in malaria-endemic regions because heterozygous carriers have a survival advantage. Allele frequency is governed by natural selection, genetic drift, mutation pressure, and gene flow — none of which depend on whether the allele is dominant or recessive."

- question: "A dominant allele is stronger, more functional, or biologically superior to its recessive counterpart."
  type: true-false
  answer: false
  explanation: "Dominance is purely a description of what phenotype appears in a heterozygote — it carries no implication of superiority or functionality. Huntington's disease is caused by a dominant gain-of-function mutation that is severely harmful. Many recessive alleles encode fully functional proteins. 'Dominant' and 'recessive' are relational labels describing expression patterns in heterozygotes, not rankings of quality or biological value."

- question: "Two individuals with identical phenotypes can have different genotypes, and a test cross is required to reveal this hidden genetic difference."
  type: true-false
  answer: true
  explanation: "Under complete dominance, both AA and Aa individuals express the dominant phenotype and are phenotypically indistinguishable. Their genotypes differ, but the recessive allele in the heterozygote is masked. A test cross with a homozygous recessive (aa) reveals the difference: Aa × aa produces 50% recessive-phenotype offspring, while AA × aa produces none. This is the foundational logic of Mendelian genetic analysis — phenotype alone cannot distinguish AA from Aa."

- question: "Why are most newly arising loss-of-function mutations recessive, and what molecular mechanism underlies this pattern?"
  type: short-answer
  answer: "Most genes encode enzymes or structural proteins, and for many, a single functional copy produces enough product to carry out the normal biological function (haplosufficiency). A loss-of-function mutation breaks one copy, but the second working copy compensates. In a heterozygote, half the normal protein amount is still sufficient, so the mutant allele is invisible phenotypically — it is recessive. Only when both copies are non-functional (homozygous recessive) does the phenotype appear."
  explanation: "This molecular logic also explains when dominant mutations arise: either as gain-of-function (the mutant protein does something harmful the normal protein doesn't) or as haploinsufficiency (the gene is so dosage-sensitive that one copy is not enough for normal function). These are less common mechanisms, which is why most newly arising mutations are recessive and why genetic disease often requires inheriting two defective copies."
```

## Explainer

From Mendelian genetics, you know that organisms carry two copies of each gene (one from each parent) and that these copies — **alleles** — may differ. Dominance and recessiveness describe what happens when those two alleles are different. If an individual with genotype Aa looks the same as one with genotype AA, then the A allele is **dominant** and the a allele is **recessive**. The heterozygote's phenotype is determined entirely by the dominant allele; the recessive allele is present in the genome but invisible in the organism's appearance or function.

The molecular reason for dominance is usually straightforward. Most genes encode enzymes or structural proteins, and for many genes, one functional copy produces enough protein to do the job. Consider an enzyme in a metabolic pathway: an individual with genotype Aa has one allele making functional enzyme and one making nonfunctional enzyme. If half the normal enzyme quantity is still sufficient to catalyze the reaction at a normal rate, the heterozygote is indistinguishable from the homozygous dominant — this is called **haplosufficiency**. The recessive allele is typically a **loss-of-function** mutation (a broken version of the gene), and dominance simply reflects the fact that one working copy is enough. This is why most newly arising deleterious mutations are recessive: they break one copy, but the other copy compensates.

The critical distinction to master is between **genotype** and **phenotype**. Two individuals can look identical (same phenotype) while carrying different genotypes — AA and Aa both show the dominant phenotype under complete dominance. The only way to distinguish them is a **test cross**: mate the unknown individual with a homozygous recessive (aa). If any offspring show the recessive phenotype, the unknown parent must have been Aa, because the recessive offspring must have received an a allele from each parent. If all offspring show the dominant phenotype, the parent is likely AA (though large sample sizes are needed for confidence, since Aa × aa produces 50% dominant and 50% recessive on average).

Finally, complete dominance is not the only possibility — it is just the simplest case. In **incomplete dominance**, the heterozygote has an intermediate phenotype (red × white flowers producing pink). In **codominance**, both alleles are fully expressed simultaneously (AB blood type, where both A and B surface antigens are present). These variations do not violate Mendel's laws of segregation; they simply reflect cases where one functional copy of a gene is not enough to produce the full dominant phenotype, or where both allele products are independently detectable. Understanding these allelic interactions prepares you for the more complex inheritance patterns — epistasis, polygenic traits, and sex-linkage — that build on this foundation.
