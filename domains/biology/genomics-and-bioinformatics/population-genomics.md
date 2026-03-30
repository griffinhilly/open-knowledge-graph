---
id: population-genomics
title: Population Genomics
domain: biology
course: genomics-and-bioinformatics
prerequisites:
- id: variant-calling-and-gwas
  type: hard
- id: population-genetics-intro
  type: hard
- id: molecular-evolution-basics
  type: soft
builds-toward:
- pharmacogenomics
tags:
- population-structure
- selection-scans
- admixture
- Fst
- demographic-history
- allele-frequency
stage: expert
status: validated
---
# Population Genomics

## Core Idea
Population genomics analyzes genome-wide variation across individuals within and between populations to infer demographic history, migration, selection, and adaptation. Key analyses include population structure inference (PCA, ADMIXTURE), selection scans (Fst outliers, extended haplotype homozygosity), demographic modeling (effective population size changes over time), and admixture detection. Whole-genome data provides orders of magnitude more power than single-locus studies, enabling detection of subtle signals like soft sweeps, polygenic adaptation, and recent gene flow between populations.

## How It's Best Learned
Download 1000 Genomes Project VCF data for a single chromosome, compute PCA across populations, and plot the first two components. Observe how continental population groups separate. Then compute Fst between populations for each SNP and identify outlier regions that may be under divergent selection.

## Common Misconceptions
- Population structure in PCA plots reflects continuous variation, not discrete "races" — the clusters are a product of geographic distance and migration history, not fundamental biological boundaries.
- High Fst at a locus does not prove natural selection — genetic drift, especially after population bottlenecks, can produce allele frequency differences by chance.

## Questions

```yaml
- question: "What does a high Fst value at a particular genomic locus indicate?"
  type: multiple-choice
  options: ["The locus has a high mutation rate", "Allele frequencies at that locus differ substantially between the compared populations", "The locus is essential for survival", "The locus is located in a repetitive region"]
  answer: 1
  explanation: "Fst (fixation index) measures the proportion of genetic variance that is attributable to differences between populations rather than within them. An Fst of 0 means allele frequencies are identical across populations; an Fst of 1 means populations are fixed for different alleles. A high Fst at a specific locus, relative to the genome-wide background, suggests that divergent natural selection may have driven allele frequency differences at that locus — though genetic drift after a bottleneck can also produce outlier Fst values."

- question: "PCA of genome-wide SNP data separates individuals into clusters that correspond to biologically distinct human races."
  type: true-false
  answer: false
  explanation: "PCA of human genetic data does show clustering that correlates with geographic ancestry, but this reflects continuous patterns of genetic variation shaped by migration, drift, and isolation by distance — not discrete biological categories. Most human genetic variation exists within populations rather than between them (Fst between continental groups is only ~0.10-0.15). The clusters in a PCA plot shift depending on which populations are sampled, and intermediate populations fill in the gaps between clusters. Human genetic variation is clinal, not categorical."

- question: "Explain how genome-wide data enables detection of recent positive selection that single-locus studies would miss."
  type: short-answer
  answer: "Recent positive selection leaves a characteristic genomic signature: a long haplotype of reduced variation surrounding the selected allele (selective sweep), because the favored allele rose in frequency too quickly for recombination to break down its surrounding haplotype. Detecting this requires comparing haplotype lengths across many loci genome-wide to establish the background expectation, then identifying loci with unusually long haplotypes (using tests like iHS or XP-EHH). A single-locus study cannot establish this genome-wide baseline and therefore cannot distinguish a selected locus from a neutral one that happens to have low diversity."
  explanation: "This illustrates the power of the genome-wide approach: the genome itself provides the null distribution. Methods like iHS compare the haplotype homozygosity of the derived allele to the ancestral allele at each SNP, flagging loci where the derived allele sits on an unusually long undisrupted haplotype — the hallmark of a recent sweep."
```

## Explainer

Population genetics, as a field, developed mathematical theory for how allele frequencies change under mutation, drift, selection, and migration. Population genomics applies these principles to entire genomes, using the massive datasets produced by modern sequencing to answer questions that single-gene studies could not resolve. The genome becomes both the subject of study and the statistical reference frame.

**Population structure** is typically the first analysis. PCA and model-based methods (ADMIXTURE, STRUCTURE) decompose genome-wide variation into components that reflect shared ancestry. In humans, the first few PCs closely mirror continental geography, reflecting ancient migration patterns. Within continents, finer structure emerges — European PCA mirrors the geographic map of Europe. These patterns inform every downstream analysis: GWAS must correct for structure to avoid confounding, selection scans must distinguish drift from selection, and demographic models must account for population splitting and admixture.

**Selection scans** search for genomic regions where natural selection has left a detectable signature. Classic selective sweeps produce regions of reduced variation around the selected allele, unusual allele frequency spectra (Tajima's D), elevated Fst between populations, and extended haplotype homozygosity. Genome-wide data enables systematic scanning for these signatures — comparing each locus to the genome-wide distribution to identify outliers. Iconic examples include the lactase persistence allele in European and East African pastoralists, skin pigmentation genes at different latitudes, and malaria resistance alleles in tropical populations. More subtle signals — soft sweeps (selection on standing variation), polygenic adaptation (many loci shifting slightly in the same direction) — require sophisticated statistical methods and very large sample sizes to detect.

**Demographic inference** uses the patterns of genetic variation across the genome to reconstruct population history. Methods like PSMC (pairwise sequentially Markovian coalescent) estimate changes in effective population size over hundreds of thousands of years from a single diploid genome, by analyzing the distribution of heterozygous sites along the chromosomes. More recent history (thousands of years) can be inferred from rare variants, LD patterns, and identity-by-descent tract lengths. These analyses have revealed population bottlenecks, expansions, and admixture events that corroborate and extend the archaeological and linguistic records of human history, and they are equally powerful when applied to other species for conservation and evolutionary biology.
