---
id: small-rnas-mirna-and-rnai
title: 'Small RNAs: miRNA and RNA Interference Pathways'
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: gene-regulation-eukaryotes
  type: hard
- id: rna-structure-and-base-pairing
  type: soft
builds-toward:
- transcription-factors-and-gene-regulation
tags:
- mirna
- sirna
- risc
- gene-silencing
- rnai
stage: formal-systems
status: draft
---

# Small RNAs: miRNA and RNA Interference Pathways

## Core Idea
MicroRNAs (miRNAs) are small regulatory RNAs (~22 nucleotides) that bind mRNA targets through base complementarity, typically repressing translation or promoting mRNA degradation. Pri-miRNA is transcribed as a long primary transcript (>1 kb), cleaved by Drosha in the nucleus to pre-miRNA (~70 nt), exported from nucleus via Exportin-5, and cleaved by Dicer in the cytoplasm to generate mature miRNA. The RNA-Induced Silencing Complex (RISC), guided by miRNA, scans mRNAs for target sites; perfect complementarity triggers endonucleolytic cleavage by Argonaute protein, while imperfect pairing (typical in animals) represses translation. miRNAs regulate hundreds of genes each, controlling development, differentiation, stress responses, and disease processes; dysregulation of miRNA pathways is implicated in cancer.

## Explainer

You already know that eukaryotic gene regulation operates at multiple levels — transcription factors controlling when genes are turned on, chromatin modifications controlling accessibility, and post-transcriptional mechanisms fine-tuning output. Small RNAs represent one of the most powerful post-transcriptional regulators, functioning as sequence-specific guides that direct protein machinery to silence target mRNAs. The central insight is simple: a short RNA molecule, roughly 22 nucleotides long, can use **base-pairing complementarity** — the same Watson-Crick rules you learned in RNA structure — to find and regulate specific messenger RNAs among thousands in the cytoplasm.

**MicroRNAs (miRNAs)** are endogenous small RNAs encoded in the organism's own genome, often in intergenic regions or within introns of protein-coding genes. Their biogenesis follows a stepwise maturation pathway. RNA Polymerase II transcribes a long **primary miRNA (pri-miRNA)**, which folds into a hairpin structure due to internal complementarity. In the nucleus, the RNase III enzyme **Drosha** (partnered with DGCR8) recognizes and cleaves this hairpin, releasing a ~70-nucleotide **precursor miRNA (pre-miRNA)** with a characteristic stem-loop shape. Exportin-5 shuttles the pre-miRNA to the cytoplasm, where a second RNase III enzyme, **Dicer**, cuts away the loop to produce a short double-stranded RNA duplex. One strand — the **guide strand** — is loaded into the **RNA-Induced Silencing Complex (RISC)**, whose catalytic core is an **Argonaute** protein. The other strand, called the passenger strand, is typically discarded.

Once loaded into RISC, the miRNA guide strand scans cytoplasmic mRNAs for complementary sequences, usually found in the 3' untranslated region (UTR). In animals, miRNA-target pairing is typically imperfect — the critical determinant of targeting is complementarity in the **seed region** (nucleotides 2–8 of the miRNA). This imperfect pairing leads to translational repression and gradual mRNA destabilization rather than immediate cleavage. In plants, by contrast, miRNA-target pairing is often near-perfect, triggering Argonaute's endonuclease activity to slice the mRNA directly. The **RNA interference (RNAi)** pathway, triggered by exogenous double-stranded RNA or experimentally introduced **small interfering RNAs (siRNAs)**, follows a similar mechanism but with perfect complementarity leading to direct mRNA cleavage.

The biological impact of miRNAs is enormous precisely because each miRNA can regulate hundreds of target genes, and each mRNA can be targeted by multiple miRNAs. This creates a dense regulatory network that fine-tunes protein output across the transcriptome. miRNAs rarely act as binary on/off switches — instead, they buffer and dampen gene expression, sharpening developmental transitions and maintaining homeostasis. When miRNA regulation breaks down — through mutations in miRNA genes, their processing machinery, or target sites — the consequences can be severe. Many cancers show characteristic miRNA expression profiles, with some miRNAs acting as tumor suppressors (their loss permits oncogene overexpression) and others as oncogenes (their overexpression silences tumor suppressors).
