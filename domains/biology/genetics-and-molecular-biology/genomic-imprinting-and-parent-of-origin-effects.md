---
id: genomic-imprinting-and-parent-of-origin-effects
title: Genomic Imprinting and Parent-of-Origin Effects
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: non-mendelian-inheritance
  type: hard
- id: epigenetics-intro
  type: soft
- id: dna-methylation-and-epigenetic-silencing
  type: soft
builds-toward:
- x-inactivation-and-dosage-compensation
tags:
- genomic-imprinting
- parent-of-origin
- prader-willi
- angelman-syndrome
stage: formal-systems
status: draft
---

# Genomic Imprinting and Parent-of-Origin Effects

## Core Idea
Genomic imprinting is the epigenetic silencing of one parental allele during gametogenesis, such that gene expression depends critically on parent-of-origin. Imprinting is established through DNA methylation and repressive histone modifications during gametogenesis and is maintained through cell division via hemimethylated DNA recognition. The phenomenon violates Mendelian expectations: identical heterozygous genotypes produce different phenotypes depending on which parent contributed the mutant allele. Imprinted gene clusters are controlled by imprinting control regions (ICRs) that coordinate silencing of multiple genes. Defects in imprinting cause disorders such as Prader-Willi syndrome (paternal Igf2r imprinting defect), Angelman syndrome (maternal UBE3A silencing), and Beckwith-Wiedemann syndrome; some cancers show abnormal imprinting of growth-promoting genes.

## Questions

```yaml
- question: "A child is born with a deletion of chromosomal region 15q11-q13 on the paternal chromosome. Which syndrome would you expect, and why?"
  type: multiple-choice
  options:
    - "Prader-Willi syndrome — paternally expressed genes in this region are deleted, and the maternal copies are silenced by imprinting and cannot compensate"
    - "Angelman syndrome — UBE3A is paternally expressed, so deleting the paternal copy eliminates the only active allele"
    - "Neither syndrome — the intact maternal copy of all genes in this region will fully compensate for the paternal deletion"
    - "Beckwith-Wiedemann syndrome — paternal deletions at 15q11 cause overgrowth through loss of growth restraint"
  answer: 0
  explanation: "Prader-Willi syndrome results from loss of paternally expressed genes at 15q11-q13. When the paternal chromosome is deleted, these genes are gone — and the maternal copies of those genes are already silenced by imprinting, so they cannot rescue. Angelman syndrome (option B) is wrong because UBE3A is maternally expressed (it's the maternal copy that's active); loss of the paternal chromosome leaves the maternal UBE3A intact. This is the key insight: for imprinted genes, parent-of-origin determines which copy counts."

- question: "A patient with Prader-Willi syndrome has two chromosomes 15 — one normal maternal copy and one paternal copy with a deletion. A clinician asks why the intact maternal chromosome cannot compensate for the missing paternal genes. The best explanation is:"
  type: multiple-choice
  options:
    - "The maternal copy of Prader-Willi-associated genes is silenced by imprinting and cannot be expressed regardless of what happens to the paternal copy"
    - "The deletion on the paternal chromosome contains a dominant-negative element that actively suppresses maternal gene expression"
    - "Maternal versions of these genes encode functionally inferior protein variants that cannot substitute for paternal-origin proteins"
    - "The deletion also removes shared regulatory sequences needed to drive expression from either chromosome"
  answer: 0
  explanation: "This is the core principle of genomic imprinting: the 'backup' copy doesn't work because it's been epigenetically silenced based on its parent-of-origin. For the genes that cause Prader-Willi syndrome, the rule is 'only the paternal copy is expressed.' The maternal copies are silenced by methylation at the imprinting control region. Having two copies is irrelevant if the rule is that one is always off — and which one is off is fixed by which parent contributed it."

- question: "Genomic imprinting is consistent with standard Mendelian inheritance because phenotype depends on which alleles are present, not which parent contributed them."
  type: true-false
  answer: false
  explanation: "Genomic imprinting directly violates this Mendelian expectation. For imprinted genes, parent-of-origin is the critical variable — two children with identical genotypes can have completely different diseases depending on whether the mutant allele came from the mother or father. Prader-Willi and Angelman syndromes both involve the 15q11-q13 region but arise from defects in opposite parental contributions. This is why family pedigrees of imprinting disorders show unusual inheritance patterns that cannot be explained by standard dominance and recessiveness."

- question: "The parental conflict hypothesis proposes that paternally expressed genes tend to promote fetal resource extraction while maternally expressed genes tend to restrain it — reflecting divergent evolutionary interests between maternal and paternal genomes."
  type: true-false
  answer: true
  explanation: "In species where females can mate with multiple males, a father's genetic interest is maximizing the growth of his current offspring (regardless of cost to the mother's other offspring by different fathers), while the mother's interest is balancing investment across all her offspring. Imf2 (paternally expressed, growth-promoting) and Igf2r (maternally expressed, growth-restraining, sequesters IGF2) exemplify this tug-of-war. The parental conflict hypothesis explains why imprinting evolved as an adaptive system despite its apparent riskiness."

- question: "Why do Prader-Willi and Angelman syndromes arise from defects in the same chromosomal region, and what does this reveal about the logic of genomic imprinting?"
  type: short-answer
  answer: "Prader-Willi results from loss of paternally expressed genes at 15q11-q13 (paternal deletion, maternal uniparental disomy, or imprinting defects); Angelman results from loss of the maternally expressed gene UBE3A in the same region (maternal deletion or paternal uniparental disomy). Same region, opposite parental origin, completely different clinical syndromes. This demonstrates that for imprinted genes, each parental chromosome contributes a non-interchangeable set of active genes — losing one parental copy is not rescued by doubling the other, because the other is already silenced."
  explanation: "The existence of two such distinct syndromes at the same locus provides compelling clinical evidence that imprinting is real, robust, and consequential. It also explains why uniparental disomy — having two copies from the same parent — causes disease even without any mutation, because you end up with two silenced copies or two active copies of genes that should have exactly one of each."
```

## Explainer

In standard Mendelian genetics, it doesn't matter which parent contributed a particular allele — a dominant allele from the mother works the same as one from the father. **Genomic imprinting** is a striking exception. For a small but critically important set of genes (around 100–200 in mammals), the cell "remembers" which parent each allele came from and silences one copy based on that parental origin. The result is functional **monoallelic expression**: only the maternal or only the paternal copy is active, even though both are present in the genome.

The molecular mechanism relies on the **epigenetic** tools you've encountered in your prerequisite study — primarily **DNA methylation**. During gametogenesis, imprinting marks are erased in primordial germ cells and then re-established in a sex-specific pattern. In the developing egg, certain genes get methylated (silenced); in the developing sperm, a different set gets methylated. After fertilization, these marks persist through every cell division because maintenance methyltransferases recognize hemimethylated DNA at replication forks and copy the methyl groups to the new strand. **Imprinting control regions (ICRs)** — regulatory sequences that can coordinate the silencing of entire gene clusters — are the targets of this differential methylation.

The medical importance of imprinting is most vivid in two disorders caused by defects in the same chromosomal region (15q11-q13). **Prader-Willi syndrome** results when the paternally expressed genes in this region are lost (through deletion of the paternal copy, maternal uniparental disomy, or imprinting defects) — the maternal copies are silenced by imprinting and cannot compensate. **Angelman syndrome** results when the maternally expressed gene *UBE3A* in the same region is lost. Same region, opposite parent-of-origin requirement, completely different clinical syndrome. This demonstrates the key principle: for imprinted genes, losing one parental copy is not rescued by the other because the other copy is already silenced.

Why would evolution produce such a seemingly risky system? The leading explanation is the **parental conflict hypothesis**: paternally expressed genes tend to promote fetal growth (extracting more resources from the mother), while maternally expressed genes tend to restrain it (conserving the mother's resources for future offspring). *Igf2* (paternally expressed, growth-promoting) and *Igf2r* (maternally expressed, growth-restraining) are textbook examples of this tug-of-war. Imprinting thus reflects an evolutionary conflict between maternal and paternal genomes over resource allocation, played out through epigenetic silencing in every cell of the developing embryo.
