---
id: dna-methylation-epigenetic-regulation
title: DNA Methylation and Epigenetic Regulation
domain: biology
course: cell-biology
prerequisites:
- id: gene-regulation-eukaryotes
  type: hard
- id: histone-modifications-epigenetic
  type: soft
builds-toward:
- histone-post-translational-modifications-acetylation
tags:
- DNA-methylation
- epigenetics
- gene-regulation
stage: abstract-reasoning
status: draft
---

# DNA Methylation and Epigenetic Regulation

## Core Idea
DNA methylation, primarily at cytosines in CpG dinucleotides, is a covalent epigenetic modification that silences genes by blocking transcription factor binding or recruiting methyl-binding proteins (MeCP2, MBD1). Maintenance methyltransferase (DNMT1) copies methylation patterns to newly synthesized DNA during replication, enabling heritable silencing across cell divisions independent of underlying DNA sequence. Aberrant methylation patterns (hypermethylation of CpG islands at gene promoters, hypomethylation of repetitive elements) characterize cancer and developmental diseases.

## How It's Best Learned
Map DNA methylation genome-wide using bisulfite sequencing; measure methyltransferase activity in vitro. Inhibit DNA methylation with 5-azacytidine and assess effects on gene expression and cell phenotype.

## Common Misconceptions
- DNA methylation always silences genes; unmethylated CpG islands at promoters are normally associated with transcription. - Methylation is erased and reset during differentiation; some patterns are remarkably stable.

## Explainer

You know from eukaryotic gene regulation that transcription depends on the accessibility of promoter and enhancer regions, and from histone modifications that chromatin structure is a major determinant of that accessibility. **DNA methylation** adds another layer to this regulatory system — one that operates directly on the DNA molecule itself rather than on the histone proteins around which it is wrapped. Together with histone modifications, methylation constitutes the cell's epigenetic memory: a system for recording gene expression states that persists across cell divisions without altering the underlying DNA sequence.

The chemistry is straightforward. **DNA methyltransferases (DNMTs)** transfer a methyl group from S-adenosylmethionine (SAM) to the 5-position of cytosine, producing **5-methylcytosine (5mC)**. In mammals, this modification occurs almost exclusively at **CpG dinucleotides** — a cytosine followed by a guanine on the same strand. CpG sites are relatively rare in the genome because 5mC spontaneously deaminates to thymine over evolutionary time, but they are concentrated in clusters called **CpG islands** near the promoters of roughly 60–70% of human genes. The key principle is: when CpG islands at a gene's promoter are methylated, that gene is typically silenced; when they are unmethylated, the gene can be expressed.

Methylation silences genes through two mechanisms. First, the methyl group physically protrudes into the major groove of DNA, directly blocking some transcription factors from binding their recognition sequences. Second, and more importantly, methylated CpG sites recruit **methyl-CpG-binding domain proteins** (MeCP2, MBD1, MBD2), which in turn recruit histone deacetylases and chromatin-remodeling complexes that compact the surrounding chromatin into a repressive state. This creates a self-reinforcing loop: DNA methylation recruits histone-modifying enzymes that close chromatin, and closed chromatin can attract additional methyltransferase activity. The result is stable, long-term silencing — exactly what the cell needs for permanently shutting down genes in differentiated tissues.

The heritability of methylation patterns is what makes this system truly epigenetic. After DNA replication, each daughter duplex is **hemimethylated** — the parental strand carries the methyl marks, but the newly synthesized strand does not. **DNMT1**, the **maintenance methyltransferase**, recognizes these hemimethylated CpG sites and methylates the corresponding cytosine on the new strand, faithfully copying the pattern. This is how a liver cell's methylation pattern is transmitted to its daughter cells for decades without any ongoing signal. When this system goes wrong — promoter **hypermethylation** silencing tumor suppressor genes, or genome-wide **hypomethylation** activating transposable elements — the consequences include cancer, developmental disorders, and genomic instability. The reversibility of methylation (via TET enzymes that oxidize 5mC) has also made it a therapeutic target: drugs like 5-azacytidine inhibit DNMTs, reactivating silenced genes in certain leukemias.
