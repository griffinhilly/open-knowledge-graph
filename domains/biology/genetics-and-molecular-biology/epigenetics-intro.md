---
id: epigenetics-intro
title: Epigenetics
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: gene-regulation-eukaryotes
  type: hard
- id: dna-structure
  type: soft
builds-toward:
- genomics-overview
tags:
- epigenetics
- methylation
- histone modification
- chromatin
- imprinting
stage: advanced
status: validated
---

# Epigenetics

## Core Idea
Epigenetics refers to heritable changes in gene expression that do not involve alterations to the DNA sequence. Key mechanisms include DNA methylation (addition of methyl groups to cytosine, typically silencing genes) and histone modification (acetylation, methylation, phosphorylation altering chromatin accessibility). These marks can be maintained through cell divisions and in some cases transmitted across generations. Genomic imprinting — where a gene is expressed from only one parental allele based on its epigenetic marks — is one striking example with clinical implications in disorders like Prader-Willi and Angelman syndrome.

## How It's Best Learned
Compare open (euchromatin) and closed (heterochromatin) chromatin states and the histone modifications associated with each. Trace how an epigenetic mark is copied to daughter strands after DNA replication.

## Common Misconceptions
- Epigenetic changes are not mutations; the DNA sequence is unchanged.
- Not all epigenetic marks are heritable across generations; most are reset during gametogenesis.

## Explainer

From your study of eukaryotic gene regulation, you know that cells control which genes are expressed through transcription factors, enhancers, and chromatin structure. **Epigenetics** extends this picture by revealing that some of these regulatory states can be locked in and faithfully copied when a cell divides — even passed to daughter cells that never see the original signal. The DNA sequence itself is unchanged, but chemical modifications to the DNA and its associated histone proteins create a second layer of heritable information sitting "on top of" the genetic code.

The two best-understood epigenetic mechanisms work through distinct chemistry but converge on the same outcome: controlling whether chromatin is open (accessible for transcription) or closed (silent). **DNA methylation** involves adding a methyl group (–CH₃) to cytosine bases, predominantly at CpG dinucleotides. When a gene's promoter region is heavily methylated, transcription factors generally cannot bind, and the gene is silenced. After DNA replication, the newly synthesized strand is initially unmethylated, but **maintenance methyltransferase (DNMT1)** recognizes the half-methylated CpG sites and methylates the new strand to match the old one — this is how the mark is copied through cell divisions. **Histone modifications** are more diverse: acetylation of histone tails generally opens chromatin (by neutralizing positive charges, loosening DNA-histone contacts), while certain methylation patterns on histones (like H3K9me3) recruit proteins that compact chromatin into silent heterochromatin. The interplay between DNA methylation and histone modifications creates stable, self-reinforcing chromatin states.

A striking demonstration of epigenetics in action is **genomic imprinting**. In most genes, both the maternal and paternal copies are expressed. But for ~100 imprinted genes in humans, only one parental copy is active — the other is silenced by epigenetic marks established during egg or sperm development. The IGF2 gene, for example, is expressed only from the paternal allele; the maternal copy is methylated and silent. If you inherit a defective paternal copy, you cannot compensate with the maternal one because it is epigenetically shut off. This explains why deletions of the same chromosomal region cause completely different diseases depending on which parent contributed it: loss of the paternal copy at 15q11-13 causes Prader-Willi syndrome (obesity, intellectual disability), while loss of the maternal copy causes Angelman syndrome (seizures, movement disorder) — same deletion, opposite parent, different imprinted genes affected.

The scope of epigenetics extends well beyond imprinting. Every cell in your body has the same DNA, yet a neuron and a liver cell express radically different gene sets. Epigenetic marks established during development lock in cell-type-specific expression patterns, which is why a skin cell stays a skin cell through thousands of divisions. Environmental factors — nutrition, stress, toxins — can alter epigenetic marks, providing a molecular mechanism for how experience can modify gene expression without mutating DNA. However, most epigenetic marks are erased and reset during gametogenesis (the production of eggs and sperm), which limits true transgenerational epigenetic inheritance in mammals. The cases where marks do escape this reprogramming are fascinating exceptions, not the rule.
