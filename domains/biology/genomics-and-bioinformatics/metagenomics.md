---
id: metagenomics
title: Metagenomics
domain: biology
course: genomics-and-bioinformatics
prerequisites:
- id: genome-assembly
  type: hard
- id: blast-and-database-searching
  type: hard
- id: dna-sequencing-technologies
  type: soft
builds-toward:
- multi-omics-integration
tags:
- metagenomics
- microbiome
- 16S-rRNA
- shotgun-sequencing
- taxonomic-profiling
- MAGs
stage: expert
status: validated
---
# Metagenomics

## Core Idea
Metagenomics sequences all DNA from an environmental sample (soil, ocean, gut) to characterize the community of organisms present without culturing them individually. Amplicon sequencing (16S/18S/ITS) uses a single marker gene for taxonomic profiling, while shotgun metagenomics sequences all DNA randomly, enabling both taxonomic and functional characterization. Computational challenges include assembling genomes from mixed communities (metagenome-assembled genomes, or MAGs), binning contigs by organism of origin, and handling uneven coverage across species. Metagenomics has revealed vast microbial diversity, with most environmental microbes unculturable by standard methods.

## How It's Best Learned
Analyze a 16S rRNA amplicon dataset from a human gut sample using QIIME2: denoise with DADA2, assign taxonomy, compute alpha and beta diversity, and compare communities between healthy and diseased individuals. Then examine a shotgun metagenomics dataset and see how functional profiling (HUMAnN) adds information that 16S alone cannot provide.

## Common Misconceptions
- 16S rRNA amplicon sequencing is not metagenomics in the strict sense — it profiles community composition using one marker gene but does not capture the full genomic content of the community.
- Detecting a species' DNA in a metagenomic sample does not prove the organism is alive or active — DNA persists after cell death.

## Questions

```yaml
- question: "What is the primary advantage of shotgun metagenomics over 16S rRNA amplicon sequencing?"
  type: multiple-choice
  options: ["Shotgun metagenomics is cheaper per sample", "Shotgun metagenomics provides both taxonomic and functional information from all organisms, not just bacteria", "Shotgun metagenomics requires no computational analysis", "Shotgun metagenomics uses longer reads"]
  answer: 1
  explanation: "16S amplicon sequencing targets a single bacterial/archaeal marker gene, providing taxonomic composition but no functional information and missing eukaryotes and viruses entirely. Shotgun metagenomics sequences all DNA in the sample, enabling identification of all organisms (bacteria, archaea, fungi, viruses), functional profiling of the community's metabolic potential (what genes and pathways are present), and even assembly of individual genomes from the mixture. The tradeoff is higher cost and greater computational complexity."

- question: "Metagenome-assembled genomes (MAGs) are always complete, contiguous genomes equivalent to those produced by single-organism sequencing."
  type: true-false
  answer: false
  explanation: "MAGs are reconstructed by binning contigs from a metagenomic assembly based on composition (GC content, tetranucleotide frequency) and coverage patterns across samples. They are typically incomplete (missing some genes), fragmented (many contigs rather than closed chromosomes), and may contain contamination from other organisms' DNA. Quality is assessed using metrics like completeness and contamination (CheckM), with high-quality MAGs defined as >90% complete and <5% contaminated. They are invaluable for studying uncultured organisms but are not equivalent to reference-quality genome assemblies."

- question: "Explain why assembling genomes from metagenomic data is more challenging than assembling a single organism's genome."
  type: short-answer
  answer: "A metagenomic sample contains DNA from dozens to thousands of species at vastly different abundances. The assembler must simultaneously reconstruct multiple genomes from mixed reads, distinguishing reads from different organisms that may share similar sequences (conserved genes, mobile elements). Low-abundance organisms have insufficient coverage for reliable assembly, while dominant organisms are over-represented. Closely related strains complicate the de Bruijn graph with highly similar but non-identical sequences. After assembly, contigs must be binned — assigned to putative organisms — using composition and coverage signals, introducing additional error."
  explanation: "This is why metagenomic assembly often requires much deeper sequencing than single-organism projects, and why the resulting MAGs are graded by quality. Co-assembly across multiple related samples can improve results by leveraging differential abundance of organisms across conditions."
```

## Explainer

Most microorganisms cannot be grown in laboratory culture — estimates suggest 99% of environmental microbes resist standard culturing techniques. Before metagenomics, these organisms were invisible to science. By extracting and sequencing all DNA from an environment, metagenomics bypasses culture entirely, opening a window into the full diversity of microbial communities in any habitat: soil, oceans, the human gut, deep-sea vents, hospital surfaces.

The two main approaches serve different purposes. **Amplicon sequencing** (most commonly 16S rRNA for bacteria) PCR-amplifies a specific marker gene from the community DNA, sequences the amplicons, and uses the sequences to identify which organisms are present and at what relative abundances. This is fast, inexpensive, and well-standardized, but it only tells you who is there — not what they can do. It also targets only organisms with the selected marker gene (16S misses viruses and eukaryotes). **Shotgun metagenomics** fragments all community DNA and sequences it without any targeted amplification. This captures everything — bacterial, archaeal, viral, eukaryotic, and plasmid DNA — and enables both taxonomic profiling (by matching reads to reference databases with tools like Kraken2 or MetaPhlAn) and functional profiling (mapping reads to gene databases with HUMAnN to identify metabolic pathways present in the community).

The most ambitious metagenomic analysis is **genome reconstruction**. By assembling reads into contigs and then grouping contigs by organism (binning), researchers can reconstruct near-complete genomes of uncultured organisms — metagenome-assembled genomes (MAGs). Binning algorithms use two signals: sequence composition (each organism has a characteristic GC content and tetranucleotide frequency) and coverage co-variation (contigs from the same genome should have correlated abundance patterns across multiple samples). Tools like MetaBAT2 and MaxBin2 automate this process. Quality assessment (CheckM) evaluates completeness and contamination by checking for expected single-copy marker genes. High-quality MAGs have enabled the discovery of entirely new phyla, metabolic capabilities, and ecological roles, expanding the tree of life dramatically.

Metagenomic studies have transformed our understanding of human health (the gut microbiome influences digestion, immunity, and even neurological function), agriculture (soil microbiomes affect crop productivity), and ecology (ocean microbiomes drive global carbon cycling). The field continues to evolve with long-read sequencing enabling more complete MAGs, metatranscriptomics (RNA-seq of communities) revealing which genes are actually active, and integration with metabolomics to connect community function to measured biochemistry.
