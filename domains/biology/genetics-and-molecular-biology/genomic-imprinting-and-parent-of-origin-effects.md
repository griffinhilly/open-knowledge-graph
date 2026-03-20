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
stage: advanced
status: draft
---

# Genomic Imprinting and Parent-of-Origin Effects

## Core Idea
Genomic imprinting is the epigenetic silencing of one parental allele during gametogenesis, such that gene expression depends critically on parent-of-origin. Imprinting is established through DNA methylation and repressive histone modifications during gametogenesis and is maintained through cell division via hemimethylated DNA recognition. The phenomenon violates Mendelian expectations: identical heterozygous genotypes produce different phenotypes depending on which parent contributed the mutant allele. Imprinted gene clusters are controlled by imprinting control regions (ICRs) that coordinate silencing of multiple genes. Defects in imprinting cause disorders such as Prader-Willi syndrome (paternal Igf2r imprinting defect), Angelman syndrome (maternal UBE3A silencing), and Beckwith-Wiedemann syndrome; some cancers show abnormal imprinting of growth-promoting genes.

## Explainer

In standard Mendelian genetics, it doesn't matter which parent contributed a particular allele — a dominant allele from the mother works the same as one from the father. **Genomic imprinting** is a striking exception. For a small but critically important set of genes (around 100–200 in mammals), the cell "remembers" which parent each allele came from and silences one copy based on that parental origin. The result is functional **monoallelic expression**: only the maternal or only the paternal copy is active, even though both are present in the genome.

The molecular mechanism relies on the **epigenetic** tools you've encountered in your prerequisite study — primarily **DNA methylation**. During gametogenesis, imprinting marks are erased in primordial germ cells and then re-established in a sex-specific pattern. In the developing egg, certain genes get methylated (silenced); in the developing sperm, a different set gets methylated. After fertilization, these marks persist through every cell division because maintenance methyltransferases recognize hemimethylated DNA at replication forks and copy the methyl groups to the new strand. **Imprinting control regions (ICRs)** — regulatory sequences that can coordinate the silencing of entire gene clusters — are the targets of this differential methylation.

The medical importance of imprinting is most vivid in two disorders caused by defects in the same chromosomal region (15q11-q13). **Prader-Willi syndrome** results when the paternally expressed genes in this region are lost (through deletion of the paternal copy, maternal uniparental disomy, or imprinting defects) — the maternal copies are silenced by imprinting and cannot compensate. **Angelman syndrome** results when the maternally expressed gene *UBE3A* in the same region is lost. Same region, opposite parent-of-origin requirement, completely different clinical syndrome. This demonstrates the key principle: for imprinted genes, losing one parental copy is not rescued by the other because the other copy is already silenced.

Why would evolution produce such a seemingly risky system? The leading explanation is the **parental conflict hypothesis**: paternally expressed genes tend to promote fetal growth (extracting more resources from the mother), while maternally expressed genes tend to restrain it (conserving the mother's resources for future offspring). *Igf2* (paternally expressed, growth-promoting) and *Igf2r* (maternally expressed, growth-restraining) are textbook examples of this tug-of-war. Imprinting thus reflects an evolutionary conflict between maternal and paternal genomes over resource allocation, played out through epigenetic silencing in every cell of the developing embryo.
