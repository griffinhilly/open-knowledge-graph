---
id: monohybrid-inheritance-and-segregation
title: Monohybrid Crosses and Mendel's Law of Segregation
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: mendelian-genetics
  type: hard
- id: meiosis
  type: soft
- id: dominance-and-recessiveness
  type: soft
builds-toward:
- dihybrid-inheritance-and-independent-assortment
- test-cross-analysis-determining-genotypes
tags:
- segregation
- 3-1-ratio
- gamete-formation
- punnett-square
stage: advanced
status: draft
---

# Monohybrid Crosses and Mendel's Law of Segregation

## Core Idea
Monohybrid crosses track a single trait segregating in two allelic forms. Mendel's Law of Segregation states that alleles segregate during meiosis such that each gamete receives one allele; random union of gametes from heterozygous parents (Aa × Aa) produces the characteristic 3:1 (dominant:recessive) phenotypic ratio in the F2 generation. Genotypic ratios are 1 AA : 2 Aa : 1 aa, reflecting the random assortment of alleles. Genetic notation using allele symbols (e.g., A for dominant, a for recessive) and Punnett squares allow prediction of offspring genotypes and phenotypes. Deviations from expected 3:1 ratios reveal complications such as lethal alleles, incomplete dominance, and codominance.

## Questions

```yaml
- question: "An Aa × Aa cross produces only 75 living offspring instead of the expected 100, and the phenotypic ratio in living offspring is 2:1 (dominant:recessive) rather than 3:1. What is the most likely explanation?"
  type: multiple-choice
  options:
    - "The dominant allele A is incompletely dominant, producing an intermediate phenotype in heterozygotes"
    - "The homozygous dominant genotype (AA) is lethal, causing those offspring to die before scoring"
    - "The cross was actually Aa × aa, not Aa × Aa"
    - "Environmental conditions favored recessive phenotype survival"
  answer: 1
  explanation: "When AA is lethal, the expected genotypic output of Aa × Aa is still 1 AA : 2 Aa : 1 aa — but the AA class dies. The surviving offspring are 2 Aa (dominant phenotype) : 1 aa (recessive phenotype), producing a 2:1 phenotypic ratio. This also explains the reduced total offspring count. Incomplete dominance would give a 1:2:1 phenotypic ratio with three distinct phenotype classes, not a 2:1. The 2:1 ratio in living offspring with reduced counts is a hallmark of a recessive lethal in combination with a dominant phenotype."

- question: "From an F2 generation produced by Aa × Aa, which offspring genotypes will breed true (produce uniform offspring) if self-crossed?"
  type: multiple-choice
  options:
    - "Only the recessive homozygotes (aa)"
    - "Both homozygous genotypes (AA and aa), but not the heterozygotes (Aa)"
    - "All three genotypes breed true because F2 represents a stable generation"
    - "Only the dominant phenotype individuals, since they carry the dominant allele"
  answer: 1
  explanation: "Only homozygous individuals breed true. AA × AA produces all AA offspring; aa × aa produces all aa offspring — in both cases, all offspring show one uniform phenotype. Heterozygotes (Aa) do not breed true: Aa × Aa again produces 1 AA : 2 Aa : 1 aa, with both phenotypes present. The common error is to assume all 'dominant phenotype' individuals breed true — but 2/3 of dominant-phenotype F2 offspring are Aa heterozygotes, which will not."

- question: "The Law of Segregation is grounded in the physical separation of homologous chromosomes during meiosis I, not just a statistical rule about probability."
  type: true-false
  answer: true
  explanation: "Mendel derived the law statistically from pea plant crosses, but its physical basis was discovered later: homologous chromosomes (carrying the two alleles of a gene) line up and separate during meiosis I, each going to a different daughter cell. This physical separation is not probabilistic — it is a mechanical process that can be observed microscopically. The 1:1 allele ratio in gametes is a direct consequence of this physical separation, not an assumption."

- question: "In a standard Aa × Aa cross, 75% of F2 offspring show the dominant phenotype, which means 75% of F2 offspring carry at least one dominant allele."
  type: true-false
  answer: true
  explanation: "Both statements are true and consistent. The F2 genotypic ratio is 1 AA : 2 Aa : 1 aa. Of the four equally likely outcomes, three (AA, Aa, aA) carry at least one A allele and show the dominant phenotype, giving 75%. The fourth (aa) carries no A allele and shows the recessive phenotype. This is not a misconception — it is correct, unlike the common error of thinking that 75% are homozygous dominant (only 25% are)."

- question: "Explain why a 1:2:1 phenotypic ratio (rather than 3:1) from an Aa × Aa cross indicates incomplete dominance rather than complete dominance."
  type: short-answer
  answer: "With complete dominance, AA and Aa are phenotypically identical because A fully masks a. So three genotype classes (1 AA : 2 Aa : 1 aa) collapse into two phenotype classes (3 dominant : 1 recessive). With incomplete dominance, A does not fully mask a, so heterozygotes (Aa) display an intermediate phenotype distinct from both homozygotes. The three genotype classes now produce three distinct phenotypes — one for AA, one for Aa (intermediate), and one for aa — giving a 1:2:1 phenotypic ratio that directly mirrors the genotypic ratio."
  explanation: "The 3:1 ratio depends entirely on AA and Aa being phenotypically indistinguishable. Incomplete dominance breaks this equivalence: the heterozygote is visibly different from both homozygotes, so you see all three genotypic classes expressed as distinct phenotypes. Classic examples include snapdragon flower color (red × white → pink heterozygotes) and familial hypercholesterolemia (intermediate cholesterol levels in heterozygotes). The phenotypic ratio thus directly reveals the dominance relationship."
```

## Explainer

From Mendelian genetics, you know that traits are controlled by discrete hereditary units (genes) that come in variant forms (alleles), and from your understanding of dominance and recessiveness, you know that a dominant allele masks the expression of a recessive allele in heterozygotes. A **monohybrid cross** puts these ideas into quantitative practice by tracking a single gene with two alleles through a controlled mating and predicting the exact ratios of offspring genotypes and phenotypes.

The logic begins with **Mendel's Law of Segregation**: each diploid organism carries two alleles for a given gene (one from each parent), and these two alleles separate during gamete formation so that each gamete carries exactly one. If you cross two organisms that are both heterozygous for a trait — say, Aa × Aa — each parent produces two types of gametes in equal proportion: half carry A, half carry a. A **Punnett square** is simply a grid that maps all possible combinations of one gamete from each parent. With Aa × Aa, the square gives four equally likely outcomes: AA, Aa, aA, and aa. This yields a **genotypic ratio** of 1 AA : 2 Aa : 1 aa. Since A is dominant over a, both AA and Aa individuals show the dominant phenotype, giving the famous **3:1 phenotypic ratio** (3 dominant : 1 recessive).

The physical basis for segregation is **meiosis**. During meiosis I, homologous chromosomes — and the alleles they carry — are pulled to opposite poles of the cell. This is not a statistical abstraction; it is a literal, physical separation that you can trace under a microscope. Each resulting gamete inherits one member of each homologous pair, which is why each gamete gets exactly one allele per gene. The 3:1 ratio in the F2 generation is therefore a direct, predictable consequence of the mechanics of meiosis combined with random fertilization.

The power of the monohybrid framework is that it generates testable predictions. If you observe 3:1 in the F2, you can infer that the parents were heterozygous and the trait follows simple dominance. If you see a 1:1 ratio instead, one parent was likely heterozygous and the other homozygous recessive — a **test cross**. Deviations from 3:1 are not failures of Mendelian genetics but clues to additional complexity: a 1:2:1 phenotypic ratio suggests **incomplete dominance** (heterozygotes have an intermediate phenotype), while a 2:1 ratio in living offspring suggests a **lethal allele** (homozygous dominant is lethal, removing one expected class). Each deviation tells you something specific about the allelic interaction, making the monohybrid cross not just a prediction tool but a diagnostic one — the foundation on which all more complex genetic analysis is built.
