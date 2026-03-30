---
id: variant-calling-and-gwas
title: Variant Calling and Genome-Wide Association Studies
domain: biology
course: genomics-and-bioinformatics
prerequisites:
- id: dna-sequencing-technologies
  type: hard
- id: single-nucleotide-polymorphisms-snps
  type: hard
- id: population-genetics-intro
  type: hard
- id: probability-distributions
  type: soft
builds-toward:
- population-genomics
- pharmacogenomics
tags:
- variant-calling
- GWAS
- SNP
- GATK
- Manhattan-plot
- linkage-disequilibrium
stage: expert
status: validated
---
# Variant Calling and Genome-Wide Association Studies

## Core Idea
Variant calling identifies positions where an individual's genome differs from a reference sequence, detecting single nucleotide variants (SNVs), small insertions/deletions (indels), and structural variants. Tools like GATK HaplotypeCaller use Bayesian models that integrate base quality scores, mapping quality, and local realignment to distinguish true variants from sequencing errors. Genome-wide association studies (GWAS) test whether any of these variants are statistically associated with a phenotype (disease, trait) across a population, typically testing millions of SNPs and correcting for multiple testing using a genome-wide significance threshold of p < 5e-8. Associated variants identify genomic regions, not necessarily causal genes.

## How It's Best Learned
Walk through the GATK Best Practices pipeline on a small dataset: align reads, mark duplicates, call variants, and filter. Then examine a published GWAS Manhattan plot and trace one significant peak to its genomic context — what genes are nearby? Is the lead SNP coding or regulatory? Is the causal variant known?

## Common Misconceptions
- A GWAS hit does not identify the causal variant — it identifies a region in linkage disequilibrium with the causal variant, which may be a noncoding regulatory element rather than a protein-coding change.
- Variant calling accuracy depends heavily on sequencing depth; calling heterozygous variants reliably typically requires 30x coverage or more.

## Questions

```yaml
- question: "Why does GATK's variant calling pipeline use a Bayesian framework rather than simply counting how many reads show the reference versus alternate allele?"
  type: multiple-choice
  options: ["Bayesian methods are faster computationally", "The Bayesian framework integrates base quality scores, mapping quality, and prior expectations to distinguish true variants from sequencing errors", "Simple allele counting cannot detect indels", "Bayesian methods do not require a reference genome"]
  answer: 1
  explanation: "Raw allele counts are confounded by sequencing errors, mapping artifacts, and variable coverage. A Bayesian model incorporates the probability that each base call is correct (base quality), the confidence of the read's genomic placement (mapping quality), and prior expectations about variant frequency. It outputs a posterior probability for each possible genotype (homozygous reference, heterozygous, homozygous alternate), providing a principled way to call variants even at modest coverage where a simple majority-vote approach would be unreliable."

- question: "A GWAS identifies a SNP significantly associated with type 2 diabetes. This SNP is the mutation that causes the disease."
  type: true-false
  answer: false
  explanation: "The associated SNP is typically a tag SNP — one of many correlated variants in a region of linkage disequilibrium. The causal variant may be the tag SNP itself, but more often it is a different variant in the same LD block. Furthermore, most GWAS hits fall in noncoding regions and likely affect gene regulation rather than protein sequence. Fine-mapping, functional studies, and eQTL (expression quantitative trait locus) analyses are needed to move from a GWAS association signal to the actual causal variant and mechanism."

- question: "Explain why the genome-wide significance threshold for GWAS is typically set at p < 5e-8 rather than the conventional p < 0.05."
  type: short-answer
  answer: "A GWAS typically tests approximately 1 million independent SNPs (after accounting for linkage disequilibrium) for association with a phenotype. At p < 0.05, this would produce ~50,000 false positives. The threshold of 5e-8 approximates a Bonferroni correction for 1 million tests (0.05 / 1,000,000 = 5e-8), controlling the genome-wide false positive rate at 5%. This stringent threshold means that only very strong statistical signals survive, requiring large sample sizes (often tens to hundreds of thousands of individuals) to detect the typically small effects of individual variants on complex traits."
  explanation: "The 5e-8 threshold has become a community standard for human GWAS. It is conservative (Bonferroni assumes independence, but SNPs in LD are correlated), but its stringency has proven valuable — GWAS results that pass this threshold replicate in independent cohorts at very high rates, demonstrating that the threshold effectively controls false discoveries."
```

## Explainer

Every human genome contains roughly 4-5 million positions where it differs from the reference sequence. Identifying these variants and determining which ones influence health and traits are two of the central tasks of modern genomics. Variant calling is the computational process of finding the variants; GWAS is the statistical framework for linking them to phenotypes.

**Variant calling** starts with aligned sequencing reads (BAM files) and asks, at each genomic position, whether the observed reads support a variant. The challenge is that not every apparent difference is a real variant — sequencing errors (1% per base for Illumina), mapping errors (reads from paralogous regions assigned to the wrong location), and PCR duplicates (identical reads from amplification rather than independent sampling) all create false variant signals. The GATK Best Practices pipeline addresses each issue: reads are aligned with BWA-MEM, duplicates are marked (Picard), and HaplotypeCaller performs local de novo assembly of the reads in active regions, then evaluates all possible haplotypes using a pair-HMM to calculate genotype likelihoods. Variant quality score recalibration (VQSR) uses known true variants (from dbSNP, HapMap) as training data to separate true variants from artifacts.

**GWAS** tests the association between genetic variants and a phenotype across many individuals. The typical design genotypes hundreds of thousands of SNPs (using genotyping arrays) in thousands to millions of people, imputes additional variants using reference panels, and tests each SNP for association using linear or logistic regression, including covariates for population structure (principal components), age, sex, and other confounders. Results are displayed as Manhattan plots — genomic position on the x-axis, -log10(p-value) on the y-axis — where significant peaks rise above the genome-wide threshold of 5e-8.

A GWAS peak identifies a **region** associated with a trait, not a causal mechanism. The lead SNP is usually in linkage disequilibrium with many other variants, any of which could be causal. Most associations (~90%) fall in noncoding regions, suggesting regulatory rather than protein-coding effects. **Fine-mapping** methods (FINEMAP, SuSiE) use LD structure to narrow the set of potentially causal variants. Integration with epigenomic data (which regulatory elements are active in the relevant tissue?), eQTL data (which variants affect gene expression?), and functional validation experiments is typically required to go from a statistical association to a biological mechanism. Despite these challenges, GWAS has identified thousands of robust trait-associated loci, transformed our understanding of the genetic architecture of complex diseases, and forms the foundation for polygenic risk scores used in personalized medicine.
