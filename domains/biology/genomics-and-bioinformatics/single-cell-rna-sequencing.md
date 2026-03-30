---
id: single-cell-rna-sequencing
title: Single-Cell RNA Sequencing
domain: biology
course: genomics-and-bioinformatics
prerequisites:
- id: rna-seq-analysis-pipeline
  type: hard
- id: differential-gene-expression
  type: hard
- id: data-structures-and-algorithms-basics
  type: soft
builds-toward:
- spatial-transcriptomics
- multi-omics-integration
tags:
- scRNA-seq
- cell-clustering
- UMAP
- droplet-based
- cell-type-annotation
- 10x-Genomics
stage: expert
status: validated
---
# Single-Cell RNA Sequencing

## Core Idea
Single-cell RNA sequencing (scRNA-seq) profiles gene expression in individual cells rather than bulk tissue averages, revealing cellular heterogeneity, rare cell types, and cell state transitions. Droplet-based platforms (10x Genomics Chromium) encapsulate single cells with barcoded beads to tag each cell's transcripts uniquely. Analysis involves quality filtering, normalization, dimensionality reduction (PCA, UMAP), clustering to identify cell types, and differential expression between clusters. scRNA-seq has revealed that tissues previously thought to be homogeneous contain diverse cell populations with distinct transcriptional programs.

## How It's Best Learned
Analyze a published scRNA-seq dataset (e.g., PBMCs from 10x Genomics) using Scanpy or Seurat. Perform the standard workflow: filter low-quality cells, normalize, find highly variable genes, run PCA and UMAP, cluster, and annotate clusters using known marker genes. Compare the UMAP visualization before and after batch correction if multiple samples are involved.

## Common Misconceptions
- scRNA-seq does not capture all transcripts in a cell; current methods detect only 10-30% of expressed genes per cell (dropout), requiring specialized statistical approaches.
- Clusters on a UMAP plot do not necessarily represent discrete cell types — they can reflect continuous processes like differentiation gradients.

## Questions

```yaml
- question: "Why is dropout (failure to detect expressed genes) a more significant problem in scRNA-seq than in bulk RNA-seq?"
  type: multiple-choice
  options: ["scRNA-seq uses lower quality sequencing chemistry", "Each cell provides only picograms of RNA, so low-abundance transcripts are frequently lost during capture and amplification", "scRNA-seq does not perform PCR amplification", "Bulk RNA-seq uses longer reads that capture more genes"]
  answer: 1
  explanation: "A single cell contains roughly 10 picograms of total RNA — orders of magnitude less than a bulk sample. During library preparation, the capture and reverse transcription of such small quantities is inherently stochastic: a transcript present at a few copies may be captured in one cell but missed in another. This produces an excess of zero counts (dropout) that does not reflect true absence of expression. Specialized imputation methods and models that account for zero-inflation are used to handle this."

- question: "Cell clusters identified in a UMAP visualization of scRNA-seq data always correspond to distinct, discrete cell types."
  type: true-false
  answer: false
  explanation: "UMAP is a dimensionality reduction method that preserves local neighborhood structure, but it can create apparent clusters from continuous data and can separate or merge groups depending on parameter settings. Apparent clusters may represent discrete cell types, continuous differentiation states, cell cycle phases, or even technical batch effects. Biological validation using known marker genes, trajectory analysis, and independent experimental methods is needed to determine whether clusters represent genuinely distinct cell populations."

- question: "Explain the role of highly variable gene (HVG) selection in the scRNA-seq analysis workflow."
  type: short-answer
  answer: "HVG selection identifies genes whose expression varies more across cells than expected from technical noise alone. These genes carry the biological signal that distinguishes cell types and states. By restricting downstream analysis (PCA, clustering) to the top 1,000-3,000 HVGs, you remove the noise contributed by non-informative genes (housekeeping genes, lowly expressed genes dominated by dropout) and focus computational resources on the features that actually differentiate cells. This improves clustering quality and reduces computational cost."
  explanation: "Without HVG selection, PCA would be dominated by technical noise and highly expressed but non-variable housekeeping genes, producing components that do not separate cell types. The variance-mean relationship is used to identify genes with excess variability: genes must have variance above what is expected at their mean expression level to qualify as highly variable."
```

## Explainer

Bulk RNA-seq measures the average gene expression across millions of cells — like blending a fruit salad and analyzing the smoothie's composition. You can tell there are strawberries and bananas, but you cannot tell which pieces are next to which. Single-cell RNA-seq sequences each cell individually, preserving the identity and heterogeneity that bulk methods erase. This resolution has transformed our understanding of development, immune responses, cancer, and tissue organization.

The dominant platform, **10x Genomics Chromium**, uses microfluidics to encapsulate individual cells in oil droplets, each containing a gel bead coated with barcoded oligonucleotides. Inside each droplet, the cell is lysed, its mRNA captured on the bead via poly-T sequences, and each transcript tagged with a cell-specific barcode and a unique molecular identifier (UMI). After reverse transcription and amplification, the barcoded cDNA from thousands of cells is pooled and sequenced together. Computational demultiplexing uses the barcodes to assign each read back to its cell of origin, and UMI counting eliminates PCR amplification bias. A typical experiment profiles 5,000-20,000 cells.

The **analysis workflow** begins with quality control: removing cells with too few genes detected (empty droplets or dead cells), too many genes (possible doublets — two cells in one droplet), or high mitochondrial gene percentages (indicator of cell stress or lysis). After normalization, the key step is selecting highly variable genes (HVGs) — genes whose expression varies across cells more than expected from noise. PCA on HVGs reduces the data from ~20,000 dimensions to 20-50 principal components that capture the major axes of biological variation. UMAP or t-SNE then projects these components into 2D for visualization, and graph-based clustering algorithms (Louvain, Leiden) identify groups of transcriptionally similar cells.

**Cell type annotation** — assigning biological identities to clusters — is both the goal and the bottleneck. Automated methods compare cluster expression profiles to reference databases (CellTypist, SingleR), but manual annotation using known marker genes remains the gold standard for novel tissues or species. Downstream analyses include differential expression between clusters, trajectory inference (ordering cells along developmental paths using tools like Monocle or scVelo), RNA velocity (predicting future cell states from spliced/unspliced transcript ratios), and integration of multiple datasets to build comprehensive cell atlases. The Human Cell Atlas project aims to map every cell type in the human body, using scRNA-seq as its primary technology.
