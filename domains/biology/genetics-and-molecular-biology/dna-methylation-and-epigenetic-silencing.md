---
id: dna-methylation-and-epigenetic-silencing
title: DNA Methylation and Epigenetic Gene Silencing
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: epigenetics-intro
  type: hard
- id: dna-structure
  type: soft
builds-toward:
- genomic-imprinting-and-parent-of-origin-effects
- x-inactivation-and-dosage-compensation
tags:
- dna-methylation
- cpg-islands
- methyl-binding-proteins
- dnmts
- silencing
stage: advanced
status: draft
---

# DNA Methylation and Epigenetic Gene Silencing

## Core Idea
DNA methylation—the covalent addition of methyl groups typically at cytosine residues in CpG dinucleotides—is a covalent modification that suppresses gene expression and is essential for normal development, X-inactivation, and genomic imprinting. DNA methyltransferases (DNMT1, DNMT3A, DNMT3B) catalyze methylation; DNMT1 maintains methylation patterns during DNA replication by recognizing hemimethylated DNA. Methyl-binding proteins (MeCP2, MBD1-MBD4) recognize 5-methylcytosine and recruit repressive chromatin complexes containing HDACs and histone methyltransferases. Methylation patterns are stably maintained through cell division, establishing a heritable but reversible epigenetic code. Aberrant methylation (hypermethylation of tumor suppressor genes, hypomethylation of oncogenes) is implicated in cancer and developmental disorders.

## Explainer

From your introduction to epigenetics, you understand that cells can regulate gene expression through mechanisms that don't alter the DNA sequence itself. DNA methylation is the most chemically direct of these mechanisms: an enzyme physically attaches a **methyl group** (–CH₃) to the 5-carbon of cytosine, converting it to **5-methylcytosine**. This modification occurs almost exclusively at **CpG dinucleotides** — places where a cytosine is followed by a guanine on the same strand. The human genome contains roughly 28 million CpG sites, and about 70-80% of them are methylated in any given cell type. The critical exception is **CpG islands** — clusters of CpG sites near gene promoters that are typically unmethylated in normal cells, keeping those genes accessible for transcription.

The mechanism by which methylation silences genes operates through two complementary pathways. First, the methyl group itself can physically block transcription factors from binding to the promoter — it occupies space in the major groove of DNA where proteins need to make contact. Second, and more importantly, a family of **methyl-CpG-binding proteins** (MeCP2, MBD1-4) specifically recognizes methylated CpGs and recruits **histone deacetylases (HDACs)** and histone methyltransferases. These enzymes modify the histone proteins that DNA wraps around, compacting the chromatin into a tightly packed, transcriptionally inactive state. Methylation thus triggers a cascade: methylated DNA attracts proteins that restructure chromatin, which buries the gene and prevents the transcription machinery from accessing it.

What makes methylation an epigenetic mechanism — rather than just a regulatory one — is its **heritability through cell division**. When DNA replicates, each daughter strand is initially unmethylated, producing **hemimethylated** DNA (one strand methylated, one not). The maintenance methyltransferase **DNMT1** recognizes these hemimethylated sites and adds methyl groups to the new strand, faithfully copying the methylation pattern. This is why a liver cell's daughter cells are liver cells, not neurons: the methylation patterns that silence neuron-specific genes are propagated every time the cell divides. Meanwhile, **DNMT3A** and **DNMT3B** are *de novo* methyltransferases that establish new methylation patterns during embryonic development, setting up the tissue-specific gene expression programs that define each cell type.

When this system goes wrong, the consequences can be severe. **Hypermethylation** of CpG islands at tumor suppressor gene promoters silences genes that normally restrain cell growth — this is a common early event in many cancers and functionally equivalent to deleting the gene. Conversely, **hypomethylation** can activate oncogenes or repetitive elements that are normally kept silent, destabilizing the genome. The reversibility of methylation — unlike a DNA mutation, a methyl group can be actively or passively removed — makes it an attractive target for cancer therapy. Drugs like azacitidine and decitabine inhibit DNA methyltransferases, reactivating silenced tumor suppressor genes. Understanding methylation thus connects basic molecular biology to both normal development and disease.
