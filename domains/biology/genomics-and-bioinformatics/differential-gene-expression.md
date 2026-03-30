---
id: differential-gene-expression
title: Differential Gene Expression Analysis
domain: biology
course: genomics-and-bioinformatics
prerequisites:
- id: rna-seq-analysis-pipeline
  type: hard
- id: probability-distributions
  type: hard
- id: gene-expression-overview
  type: soft
builds-toward:
- gene-regulatory-networks
- multi-omics-integration
tags:
- DESeq2
- edgeR
- fold-change
- FDR
- multiple-testing
- negative-binomial
stage: expert
status: validated
---
# Differential Gene Expression Analysis

## Core Idea
Differential gene expression (DGE) analysis identifies genes whose expression levels differ significantly between experimental conditions (e.g., treated vs. control, diseased vs. healthy). Tools like DESeq2 and edgeR model RNA-seq count data using the negative binomial distribution (which accounts for both sampling noise and biological variability), estimate per-gene dispersion, and perform statistical tests for each gene. Because thousands of genes are tested simultaneously, multiple testing correction (Benjamini-Hochberg FDR) is essential to control the false discovery rate. Results are typically reported as log2 fold changes with adjusted p-values and visualized using volcano plots and MA plots.

## How It's Best Learned
Run DESeq2 on a small RNA-seq dataset with 3 replicates per condition. Examine the results table: sort by adjusted p-value, filter by fold change, and generate a volcano plot. Then repeat the analysis removing one replicate per condition and observe how statistical power decreases — this demonstrates why biological replication matters more than sequencing depth.

## Common Misconceptions
- A large fold change does not automatically mean statistical significance; low-expression genes can show large fold changes due to noise.
- Biological replicates (independent samples) are not the same as technical replicates (re-sequencing the same library); DGE requires biological replicates to estimate true variability.

## Questions

```yaml
- question: "Why do DESeq2 and edgeR use the negative binomial distribution rather than the Poisson distribution to model RNA-seq count data?"
  type: multiple-choice
  options: ["The negative binomial distribution is computationally faster", "RNA-seq counts have more variance than the Poisson distribution can accommodate due to biological variability between replicates", "The Poisson distribution cannot handle zero counts", "The negative binomial distribution is required for normalized data"]
  answer: 1
  explanation: "The Poisson distribution assumes the mean equals the variance — appropriate if the only source of variability were random sampling of reads. But biological replicates of the same condition show additional variability (biological dispersion), making the variance exceed the mean. The negative binomial distribution has a separate dispersion parameter that captures this extra-Poisson variability (overdispersion). DESeq2 and edgeR estimate gene-specific dispersion by borrowing information across genes with similar expression levels, enabling accurate statistical testing even with few replicates."

- question: "Applying a p-value threshold of 0.05 without multiple testing correction is appropriate when testing 20,000 genes for differential expression."
  type: true-false
  answer: false
  explanation: "Testing 20,000 genes at p < 0.05 would produce approximately 1,000 false positives by chance alone (5% of 20,000). Multiple testing correction is essential. The Benjamini-Hochberg procedure controls the false discovery rate (FDR) — ensuring that among all genes declared significant, only a specified proportion (typically 5% or 10%) are expected to be false discoveries. This is less conservative than Bonferroni correction (which controls the family-wise error rate) but much more appropriate for genomics, where finding most true positives matters alongside controlling false ones."

- question: "Explain why increasing the number of biological replicates improves differential expression analysis more than increasing sequencing depth per sample."
  type: short-answer
  answer: "Biological replicates capture the true variability between independent samples of the same condition, which is what the statistical test needs to estimate to determine whether observed differences between conditions are real. Sequencing depth reduces technical sampling noise but does not reduce biological variability. Beyond a moderate depth (~10-20 million reads for most RNA-seq experiments), additional reads provide diminishing returns for DGE because the variance is dominated by biological rather than technical components. More replicates directly improve the precision of the dispersion estimate and increase statistical power to detect true expression differences."
  explanation: "This is one of the most important experimental design principles in RNA-seq. Three replicates per condition is often treated as a minimum, but power analyses consistently show that increasing from 3 to 6 replicates improves DGE sensitivity far more than doubling sequencing depth. The budget is almost always better spent on more replicates."
```

## Explainer

The RNA-seq pipeline produces a matrix of read counts per gene per sample. The next question — which genes are expressed differently between conditions? — is fundamentally a statistical problem. Differential gene expression analysis applies statistical models to this count data to identify genes with expression changes larger than expected from random variation.

The statistical framework starts with the right **distribution for count data**. RNA-seq counts are not normally distributed; they are discrete, non-negative, and often skewed. The Poisson distribution is a natural starting point (it models count data), but it assumes the variance equals the mean. In practice, biological replicates show more variability than Poisson predicts — called overdispersion. The negative binomial distribution adds a dispersion parameter to capture this biological variability. DESeq2 and edgeR both use the negative binomial model but differ in exactly how they estimate dispersion and normalize data.

A critical technical challenge is **dispersion estimation with few replicates**. With only 3 replicates per condition (common in RNA-seq), estimating the variance of each gene independently would be very noisy. Both DESeq2 and edgeR address this by "borrowing strength" across genes: they assume genes with similar expression levels have similar dispersion, fitting a trend of dispersion versus mean expression and shrinking individual gene estimates toward this trend. This approach — empirical Bayes shrinkage — stabilizes variance estimates and improves statistical power, but it assumes the dispersion-mean relationship is smooth, which generally holds in practice.

**Multiple testing correction** is non-negotiable. Testing 20,000 genes means that even with well-calibrated p-values, a 5% significance threshold produces ~1,000 false positives. The Benjamini-Hochberg procedure converts p-values to adjusted p-values (q-values) that control the false discovery rate — the expected proportion of false positives among all declared significant results. An FDR threshold of 0.05 means you accept that approximately 5% of your significant genes may be false discoveries, which is a reasonable tradeoff in exploratory genomics where downstream validation (qPCR, functional assays) will filter the list further.

Results are typically visualized with **volcano plots** (log2 fold change on x-axis, -log10 adjusted p-value on y-axis), which simultaneously show effect size and statistical significance, making it easy to identify genes that are both biologically meaningful (large fold change) and statistically reliable (low adjusted p-value). The output gene list feeds into pathway analysis, gene ontology enrichment, and network analysis to interpret the biological significance of expression changes.
