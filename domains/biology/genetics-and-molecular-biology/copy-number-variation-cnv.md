---
id: copy-number-variation-cnv
title: Copy Number Variation and Structural Variants
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: genomics-overview
  type: hard
- id: unequal-crossing-over-duplication
  type: hard
builds-toward:
- variant-annotation-interpretation
tags:
- copy-number-variation
- structural-variants
- cnv
- genomic-variation
- disease-association
stage: formal-systems
status: draft
---

# Copy Number Variation and Structural Variants

## Core Idea
Copy number variations (CNVs) are segments ≥1 kb that differ in copy number between individuals, representing the most common form of structural variation in human genomes (~12% of the genome is CNV). CNVs can be benign or cause disease through gene dosage imbalance; recurrent CNVs associated with neurodevelopmental disorders often involve duplications and deletions of genomic regions with segmental duplications. CNVs contribute to both genetic disease and human evolution.

## Explainer

From your study of genomics and unequal crossing over, you know that genomes are not static blueprints — they can gain or lose segments through errors in recombination. **Copy number variations** (CNVs) are the result: stretches of DNA, typically 1 kilobase or larger, that exist in different numbers of copies in different individuals. Where you might carry two copies of a particular genomic region (one per chromosome), another person might carry one, three, or even ten copies. These are not rare mutations — CNVs collectively affect more base pairs of the human genome than single-nucleotide polymorphisms (SNPs) do.

The primary mechanism generating CNVs is **nonallelic homologous recombination** (NAHR), which is essentially the unequal crossing over you have already studied, applied at a genomic scale. When two stretches of highly similar sequence (**segmental duplications**) flank a region, the recombination machinery can misalign them during meiosis. Crossover between misaligned copies produces one chromosome with a duplication and another with a deletion. This is why CNV "hotspots" cluster in regions rich in segmental duplications. Other mechanisms include nonhomologous end joining (NHEJ) and replication-based errors like fork stalling and template switching.

Many CNVs are **benign** — they fall in non-coding regions or involve genes that are dosage-insensitive. Some are even adaptive: populations with historically high-starch diets tend to carry more copies of the *AMY1* gene (encoding salivary amylase), enhancing starch digestion. But when a CNV deletes or duplicates a dosage-sensitive gene, the consequences can be severe. The classic example is the 22q11.2 deletion syndrome (DiGeorge syndrome): a 3-megabase deletion on chromosome 22 removes about 30 genes and causes heart defects, immune deficiency, and learning difficulties. Similarly, duplications of the 17p12 region cause Charcot-Marie-Tooth disease type 1A by increasing the dosage of the *PMP22* gene, which encodes a peripheral nerve myelin protein.

Detecting CNVs requires methods that go beyond standard SNP genotyping. **Array comparative genomic hybridization** (array CGH) compares fluorescence intensity between a test and reference genome across thousands of genomic probes, revealing regions of gain or loss. Modern whole-genome sequencing detects CNVs through read-depth analysis (regions with more copies produce more sequencing reads) and by identifying discordant paired-end reads that span deletion or duplication breakpoints. Understanding CNVs has transformed clinical genetics — they are now routinely assessed in patients with intellectual disability, autism spectrum disorder, and congenital anomalies, and they explain a significant fraction of cases that were previously considered idiopathic.
