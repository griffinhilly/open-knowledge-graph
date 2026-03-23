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

## Questions

```yaml
- question: "A patient with intellectual disability is found to carry a deletion of one copy of a gene on chromosome 22 involved in neural development. What primarily determines whether this CNV causes the patient's symptoms?"
  type: multiple-choice
  options:
    - "The size of the deletion in base pairs — larger deletions are always more harmful"
    - "Whether the deleted gene is dosage-sensitive — if two copies are required for normal function, losing one copy will have consequences; if one copy is sufficient, the deletion may be benign"
    - "Whether the deletion is inherited or arose de novo — de novo CNVs are always pathogenic while inherited ones are benign"
    - "The number of segmental duplications flanking the deletion — more segmental duplications indicate a more harmful variant"
  answer: 1
  explanation: "Gene dosage sensitivity is the key determinant. Many genes function normally with one copy (haploinsufficiency tolerance); others require two functional copies for adequate protein production. CNVs are pathogenic when they alter the copy number of dosage-sensitive genes. The 22q11.2 deletion (DiGeorge syndrome) is severe because it removes dosage-sensitive developmental regulators. Size alone doesn't determine pathogenicity — a large CNV in a gene-poor region may be benign while a tiny deletion of a critical gene is catastrophic. De novo status increases suspicion of pathogenicity but inheritance doesn't guarantee benignity."

- question: "Why do CNV 'hotspots' — genomic regions that frequently generate new CNVs — cluster in areas rich in segmental duplications?"
  type: multiple-choice
  options:
    - "Segmental duplications are AT-rich and therefore more prone to double-strand breaks during replication"
    - "Segmental duplications are transcribed at high rates, creating R-loops that destabilize the nearby genomic regions"
    - "The highly similar sequences in flanking segmental duplications can misalign during meiosis, causing the recombination machinery to cross over between non-allelic copies, generating duplications on one chromosome and deletions on the other"
    - "Segmental duplications contain transposons that actively excise and reinsert, carrying adjacent sequences with them"
  answer: 2
  explanation: "The mechanism is nonallelic homologous recombination (NAHR). Homologous recombination normally occurs between paired alleles — the same position on sister chromatids or homologs. When flanking segmental duplications are highly similar in sequence, the recombination machinery can mistake one copy for the other and cross over between them instead of between the actual alleles. This misalignment produces one chromosome with a duplication and one with a deletion. The 22q11.2 region, 17p12, and other CNV hotspots are all flanked by segmental duplications that facilitate this misalignment."

- question: "CNVs collectively affect more base pairs of the human genome than single-nucleotide polymorphisms (SNPs) do, even though SNPs are more numerous as individual variants."
  type: true-false
  answer: true
  explanation: "This is a striking and counterintuitive finding from human genomics. There are far more SNPs than CNVs in any two human genomes, but each CNV affects a stretch of DNA typically 1 kilobase or larger — some span megabases. SNPs, by definition, each affect a single base pair. When you sum the total base pairs affected, the larger size of CNVs outweighs their lower count, so CNVs account for more total genomic variation. This is why CNVs, despite being discovered later than SNPs, are recognized as a major form of human genetic diversity."

- question: "Copy number variations are rare mutations affecting a small percentage of the human genome, and the vast majority of CNVs detected in the population are associated with disease."
  type: true-false
  answer: false
  explanation: "Both claims are wrong. CNVs are common — approximately 12% of the human genome consists of CNV-prone regions, and most individuals carry dozens to hundreds of CNVs. The majority of common CNVs are benign, falling in non-coding regions or affecting dosage-insensitive genes. Some are adaptive: AMY1 copy number variation correlates with starch digestive capacity. Disease-associated CNVs are a subset, typically involving large deletions or duplications of dosage-sensitive genes. Conflating 'structural variant' with 'pathogenic variant' is a fundamental misunderstanding."

- question: "Why might populations with a long history of high-starch diets carry more copies of the AMY1 gene, and what general principle about CNVs does this example illustrate?"
  type: short-answer
  answer: "AMY1 encodes salivary amylase, which begins starch digestion in the mouth. More AMY1 copies produce more salivary amylase protein, increasing starch breakdown efficiency and potentially improving caloric extraction from starch-rich foods. In populations where starchy tubers, grains, or roots were dietary staples for many generations, individuals with higher AMY1 copy number may have had a survival or reproductive advantage, leading to positive selection for higher copy number. This illustrates that CNVs are not inherently pathological — they are a form of heritable genetic variation that can be neutral, harmful, or beneficial depending on context and gene function."
  explanation: "The AMY1 example is important because it demonstrates CNVs as a mechanism of adaptive evolution, not just disease. It shows that copy number — how many times a gene is present — can be a quantitative tuning mechanism for gene expression levels. This connects CNVs to the broader concept of dosage sensitivity: just as some genes are sensitive to reduced copy number (haploinsufficiency), others respond to increased copy number with proportionally increased protein output, which can be adaptive."
```

## Explainer

From your study of genomics and unequal crossing over, you know that genomes are not static blueprints — they can gain or lose segments through errors in recombination. **Copy number variations** (CNVs) are the result: stretches of DNA, typically 1 kilobase or larger, that exist in different numbers of copies in different individuals. Where you might carry two copies of a particular genomic region (one per chromosome), another person might carry one, three, or even ten copies. These are not rare mutations — CNVs collectively affect more base pairs of the human genome than single-nucleotide polymorphisms (SNPs) do.

The primary mechanism generating CNVs is **nonallelic homologous recombination** (NAHR), which is essentially the unequal crossing over you have already studied, applied at a genomic scale. When two stretches of highly similar sequence (**segmental duplications**) flank a region, the recombination machinery can misalign them during meiosis. Crossover between misaligned copies produces one chromosome with a duplication and another with a deletion. This is why CNV "hotspots" cluster in regions rich in segmental duplications. Other mechanisms include nonhomologous end joining (NHEJ) and replication-based errors like fork stalling and template switching.

Many CNVs are **benign** — they fall in non-coding regions or involve genes that are dosage-insensitive. Some are even adaptive: populations with historically high-starch diets tend to carry more copies of the *AMY1* gene (encoding salivary amylase), enhancing starch digestion. But when a CNV deletes or duplicates a dosage-sensitive gene, the consequences can be severe. The classic example is the 22q11.2 deletion syndrome (DiGeorge syndrome): a 3-megabase deletion on chromosome 22 removes about 30 genes and causes heart defects, immune deficiency, and learning difficulties. Similarly, duplications of the 17p12 region cause Charcot-Marie-Tooth disease type 1A by increasing the dosage of the *PMP22* gene, which encodes a peripheral nerve myelin protein.

Detecting CNVs requires methods that go beyond standard SNP genotyping. **Array comparative genomic hybridization** (array CGH) compares fluorescence intensity between a test and reference genome across thousands of genomic probes, revealing regions of gain or loss. Modern whole-genome sequencing detects CNVs through read-depth analysis (regions with more copies produce more sequencing reads) and by identifying discordant paired-end reads that span deletion or duplication breakpoints. Understanding CNVs has transformed clinical genetics — they are now routinely assessed in patients with intellectual disability, autism spectrum disorder, and congenital anomalies, and they explain a significant fraction of cases that were previously considered idiopathic.
