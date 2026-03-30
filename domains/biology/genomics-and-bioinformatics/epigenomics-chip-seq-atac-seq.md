---
id: epigenomics-chip-seq-atac-seq
title: "Epigenomics: ChIP-seq and ATAC-seq"
domain: biology
course: genomics-and-bioinformatics
prerequisites:
- id: dna-sequencing-technologies
  type: hard
- id: chromatin-remodeling-and-histone-acetylation
  type: hard
- id: dna-methylation-and-epigenetic-silencing
  type: hard
- id: rna-seq-analysis-pipeline
  type: soft
builds-toward:
- gene-regulatory-networks
- multi-omics-integration
tags:
- ChIP-seq
- ATAC-seq
- histone-modification
- chromatin-accessibility
- peak-calling
- epigenetics
stage: expert
status: validated
---
# Epigenomics: ChIP-seq and ATAC-seq

## Core Idea
Epigenomic methods profile chromatin state and regulatory activity across the genome. ChIP-seq (chromatin immunoprecipitation followed by sequencing) maps where specific proteins (transcription factors) or histone modifications (H3K4me3, H3K27ac) occur across the genome by using antibodies to pull down protein-DNA complexes. ATAC-seq (assay for transposase-accessible chromatin) identifies open chromatin regions by using a transposase that preferentially inserts into accessible DNA. Both methods produce genome-wide maps of regulatory activity, enabling identification of active promoters, enhancers, silencers, and transcription factor binding sites. Peak calling algorithms (MACS2) identify enriched regions above background.

## How It's Best Learned
Visualize ChIP-seq and ATAC-seq tracks alongside RNA-seq and gene annotation tracks in a genome browser (IGV or UCSC). Observe how H3K4me3 peaks mark active promoters, H3K27ac marks active enhancers, and ATAC-seq peaks coincide with both. Compare a gene that is expressed in the tissue to one that is silent and note the differences in epigenomic landscape.

## Common Misconceptions
- ChIP-seq peaks are not precise to single-base resolution — they represent enriched regions typically spanning hundreds of base pairs, with the actual binding site somewhere within the peak.
- ATAC-seq measures accessibility, not activity — an open chromatin region is available for factor binding but is not necessarily being actively used for transcription.

## Questions

```yaml
- question: "What is the fundamental difference in what ChIP-seq and ATAC-seq measure?"
  type: multiple-choice
  options: ["ChIP-seq measures gene expression while ATAC-seq measures chromatin structure", "ChIP-seq maps the locations of specific proteins or histone modifications while ATAC-seq maps regions of open chromatin regardless of which factors are bound", "ChIP-seq works on DNA while ATAC-seq works on RNA", "ChIP-seq requires more input material but ATAC-seq requires more computational analysis"]
  answer: 1
  explanation: "ChIP-seq is targeted: you choose an antibody against a specific protein (e.g., CTCF) or histone modification (e.g., H3K27ac), and the experiment tells you where in the genome that factor or mark is located. ATAC-seq is untargeted: it identifies all regions of open, accessible chromatin using a transposase that inserts into accessible DNA. ATAC-seq tells you which regions are open to regulatory activity without specifying which factors are responsible. They are complementary: ATAC-seq provides a map of potentially active regulatory regions, and ChIP-seq identifies which specific factors or marks are present at those regions."

- question: "An ATAC-seq peak at a genomic region proves that the region is actively driving transcription of a nearby gene."
  type: true-false
  answer: false
  explanation: "ATAC-seq identifies regions of open chromatin — DNA that is physically accessible to proteins. While active regulatory elements (promoters, enhancers) are typically in open chromatin, accessibility alone does not prove active transcription. A region may be accessible but unoccupied, poised but not active, or accessible due to recent transcription factor departure. Functional validation requires additional evidence: H3K27ac ChIP-seq for active enhancer status, RNA-seq for gene expression, reporter assays for regulatory activity, or CRISPR perturbation experiments."

- question: "Explain why ChIP-seq experiments require an input control or IgG control, and what artifacts can arise without one."
  type: short-answer
  answer: "The input control (sequencing of DNA before immunoprecipitation) or IgG control (using a non-specific antibody) captures background signal — regions that are enriched in the sequencing library for reasons unrelated to the protein of interest. These include open chromatin regions (which are more easily fragmented and sequenced), repetitive regions, PCR amplification biases, and mappability artifacts. Without a control, peak callers cannot distinguish true binding sites from these systematic background enrichments, producing false-positive peaks at highly accessible or highly amplified regions."
  explanation: "MACS2 and other peak callers work by comparing the ChIP signal to the control signal at each genomic position. Regions where the ChIP signal significantly exceeds the control are called as peaks. The control effectively normalizes out the biases inherent in chromatin fragmentation, library preparation, and sequencing, making the experiment interpretable."
```

## Explainer

The genome sequence is the same in nearly every cell of an organism, yet different cell types express radically different sets of genes. Epigenomic regulation — the system of chemical modifications to DNA and histones, chromatin accessibility, and three-dimensional genome organization — determines which genes are active in which cells. ChIP-seq and ATAC-seq are the primary tools for mapping this regulatory landscape genome-wide.

**ChIP-seq** works by cross-linking proteins to DNA in living cells (using formaldehyde), fragmenting the chromatin by sonication, using an antibody to immunoprecipitate the protein (and its associated DNA), and then sequencing the recovered DNA fragments. The resulting reads pile up at genomic locations where the target protein was bound. For transcription factors, the peaks are typically narrow (a few hundred base pairs centered on the binding site). For histone modifications, the peaks can be broad (spanning entire gene bodies for marks like H3K36me3) or narrow (at promoters for H3K4me3). The combination of multiple histone marks defines chromatin states: active promoters (H3K4me3 + H3K27ac), active enhancers (H3K4me1 + H3K27ac), repressed regions (H3K27me3), and heterochromatin (H3K9me3). Tools like ChromHMM learn these combinations and segment the genome into functional chromatin states.

**ATAC-seq** takes a complementary approach. Instead of asking where a specific factor is, it asks where the chromatin is accessible — where is the DNA physically open and available for regulatory proteins to bind? The Tn5 transposase preferentially inserts into accessible DNA, tagging those regions with sequencing adapters. After sequencing, reads pile up at open chromatin regions. ATAC-seq requires far fewer cells than ChIP-seq (thousands versus millions), works without antibodies (eliminating antibody quality issues), and captures the full landscape of regulatory potential in a single experiment. Fragment size analysis provides additional information: nucleosome-free fragments (~150 bp) come from accessible regulatory regions, while mono-nucleosomal fragments (~200 bp) reveal nucleosome positioning.

In practice, epigenomic experiments are most informative when integrated with each other and with gene expression data. An active enhancer should show: an ATAC-seq peak (accessible), H3K4me1 and H3K27ac ChIP-seq peaks (enhancer-specific marks), transcription factor ChIP-seq peaks (bound factors), and nearby gene expression (by RNA-seq). This convergent evidence approach, applied genome-wide across many cell types and conditions, has produced the comprehensive regulatory maps of projects like ENCODE and the Roadmap Epigenomics Project, fundamentally changing how we understand gene regulation and interpret disease-associated noncoding variants.
