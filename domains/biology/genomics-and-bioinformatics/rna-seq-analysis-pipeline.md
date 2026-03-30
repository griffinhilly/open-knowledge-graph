---
id: rna-seq-analysis-pipeline
title: RNA-seq Analysis Pipeline
domain: biology
course: genomics-and-bioinformatics
prerequisites:
- id: dna-sequencing-technologies
  type: hard
- id: gene-expression-overview
  type: hard
- id: transcription
  type: hard
- id: rna-processing
  type: soft
- id: gene-prediction
  type: soft
builds-toward:
- differential-gene-expression
- single-cell-rna-sequencing
- spatial-transcriptomics
tags:
- RNA-seq
- transcriptomics
- read-mapping
- gene-expression
- FPKM
- TPM
stage: expert
status: validated
---
# RNA-seq Analysis Pipeline

## Core Idea
RNA-seq quantifies gene expression by sequencing the RNA molecules present in a sample. The standard analysis pipeline involves quality control of raw reads, alignment to a reference genome or transcriptome (using splice-aware aligners like STAR or HISAT2), quantification of reads per gene or transcript, and normalization to account for sequencing depth and gene length differences. Key normalization metrics include TPM (transcripts per million) for within-sample comparisons and methods like DESeq2's size factors for between-sample comparisons. The pipeline transforms raw sequencing data into a gene-by-sample expression matrix suitable for downstream analysis.

## How It's Best Learned
Process a small RNA-seq dataset end-to-end: run FastQC on raw reads, trim adapters with Trimmomatic, align to a reference with STAR, count reads per gene with featureCounts, and normalize. Compare raw counts to TPM values for a housekeeping gene versus a tissue-specific gene to understand why normalization matters.

## Common Misconceptions
- FPKM and TPM are not interchangeable; TPM sums to the same value in every sample (making cross-sample comparison of proportions valid), while FPKM does not.
- More reads does not always mean higher expression — it may reflect longer transcripts capturing more reads, which is why length normalization is essential.

## Questions

```yaml
- question: "Why do RNA-seq aligners like STAR and HISAT2 need to be 'splice-aware'?"
  type: multiple-choice
  options: ["Because RNA sequences contain introns that must be removed computationally", "Because mRNA has been spliced, so reads spanning exon-exon junctions will not align contiguously to the genome", "Because splice-aware aligners are faster than standard aligners", "Because RNA-seq reads contain adapter sequences at splice sites"]
  answer: 1
  explanation: "mRNA molecules have had their introns removed by splicing, so the exon-exon junctions in the mRNA do not exist as contiguous sequences in the genomic DNA. When an RNA-seq read spans a splice junction, part of the read maps to one exon and part to the next exon, with an intron-sized gap in between on the genome. Standard DNA aligners would fail to map such reads. Splice-aware aligners like STAR recognize these split alignments and correctly place junction-spanning reads, which is critical for accurate quantification and isoform detection."

- question: "TPM (transcripts per million) and FPKM (fragments per kilobase per million) always give identical gene expression rankings within a single sample."
  type: true-false
  answer: true
  explanation: "Within a single sample, TPM and FPKM rank genes identically because they differ only by a sample-specific scaling factor. Both normalize for gene length and sequencing depth. The critical difference emerges in cross-sample comparisons: TPM values sum to one million in every sample, meaning that the proportion of expression attributed to each gene is directly comparable across samples. FPKM values do not sum to a constant across samples, making proportional comparisons between samples unreliable. For this reason, TPM is now generally preferred."

- question: "Explain why raw read counts cannot be directly compared between genes of different lengths to assess relative expression levels."
  type: short-answer
  answer: "A longer gene captures more sequencing reads simply because it presents a larger target for random fragmentation and sequencing, not because it is more highly expressed. A 10-kb gene will accumulate roughly 10 times more reads than a 1-kb gene at the same expression level. Without normalizing for gene length, raw counts systematically overestimate the expression of long genes relative to short ones. Length normalization (dividing counts by gene length) corrects this bias, allowing fair comparison of expression levels across genes of different sizes."
  explanation: "This is a fundamental sampling bias in RNA-seq. During library preparation, RNA molecules are fragmented, and each fragment has an equal probability of being sequenced. Longer transcripts produce more fragments, hence more reads, for the same number of original RNA molecules. This is why all standard expression metrics (RPKM, FPKM, TPM) include a length normalization step."
```

## Explainer

RNA-seq has become the standard method for measuring gene expression genome-wide. Rather than measuring predetermined targets (like microarrays), RNA-seq sequences whatever RNA is present in the sample, providing an unbiased, quantitative snapshot of the transcriptome. But going from raw sequencing reads to reliable expression estimates requires a multi-step pipeline, each step with important decisions that affect the final results.

The pipeline begins with **quality control and preprocessing**. FastQC or MultiQC examines raw reads for adapter contamination, quality score distributions, GC content bias, and duplication levels. Adapter sequences (ligated during library preparation) are trimmed, and low-quality bases are removed. This step is straightforward but essential — contaminated or low-quality reads introduce noise and waste computational resources in alignment.

**Alignment** maps reads to their genomic origin. Because mRNA has been spliced, reads that span exon-exon junctions must be split across the intron in the genome alignment. Splice-aware aligners like STAR and HISAT2 use known splice site annotations (and can discover novel junctions) to handle these split reads correctly. An alternative approach, pseudoalignment (Salmon, kallisto), skips genomic alignment entirely and quantifies expression by matching reads to a transcriptome reference, trading some information (genomic location) for dramatic speed improvements. The choice depends on whether downstream analyses need genomic coordinates (variant calling, splice analysis) or only gene/transcript quantification.

**Quantification** counts how many reads map to each gene or transcript. Tools like featureCounts and HTSeq-count assign aligned reads to genomic features using gene annotation files. The output is a count matrix: rows are genes, columns are samples, and each entry is the number of reads observed for that gene in that sample. These raw counts must then be **normalized** to be interpretable. Within-sample normalization (TPM, FPKM) corrects for gene length and sequencing depth, enabling comparison of expression levels between genes in the same sample. Between-sample normalization (DESeq2's median-of-ratios, edgeR's TMM) adjusts for differences in library composition and size between samples, enabling differential expression analysis — the subject of the next topic.

The entire pipeline, from raw FASTQ files to a normalized expression matrix, can be run using workflow managers like Nextflow (nf-core/rnaseq) or Snakemake, which ensure reproducibility and handle the orchestration of multiple tools. Understanding each step is nonetheless essential, because parameter choices at every stage — alignment stringency, multi-mapping handling, counting mode, normalization method — affect the biological conclusions drawn from the data.
