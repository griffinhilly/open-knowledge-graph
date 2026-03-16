---
id: single-nucleotide-polymorphisms-snps
title: Single Nucleotide Polymorphisms and Genetic Variation
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: genomics-overview
  type: hard
- id: dna-mutations
  type: hard
builds-toward:
- variant-annotation-interpretation
tags:
- snps
- single-nucleotide-polymorphisms
- genetic-variation
- allelic-variation
- gwas
stage: formal-systems
status: draft
---

# Single Nucleotide Polymorphisms and Genetic Variation

## Core Idea
Single nucleotide polymorphisms (SNPs) are single-base variations that occur ~1 per 300 bp in the human genome, with ~4-5 million SNPs per person. Most SNPs are neutral (in intergenic or 3rd-codon-position sites), though tag SNPs in linkage disequilibrium with functional variants enable genome-wide association studies (GWAS). SNPs are the most abundant genetic markers and form the basis for understanding genetic diversity, population structure, and disease susceptibility.

## Explainer

You already know that mutations are changes in DNA sequence — but not every mutation is a SNP. A **single nucleotide polymorphism (SNP)** is specifically a single-base position where two or more variants exist in a population at a frequency of at least 1%. This frequency threshold is what distinguishes a SNP from a rare mutation: if fewer than 1 in 100 people carry the variant, it is typically classified as a rare variant rather than a polymorphism. With roughly one SNP every 300 base pairs, the human genome contains millions of these common variation points, making SNPs by far the most abundant type of genetic marker.

Most SNPs have no detectable effect on the organism. This makes sense when you consider where they tend to fall. The vast majority occur in **intergenic regions** — stretches of DNA between genes that do not encode proteins. Among SNPs that fall within genes, many land in the **third position of codons**, where the genetic code's redundancy (wobble) means a base change often codes for the same amino acid. These **synonymous SNPs** change the DNA letter but not the protein product. Only a small fraction of SNPs are **nonsynonymous** — altering the amino acid sequence — and an even smaller fraction meaningfully affect protein function or gene regulation.

The real power of SNPs lies in their use as **genetic markers**. Because SNPs are so densely distributed and easy to genotype with modern microarray technology, researchers can scan hundreds of thousands of SNPs simultaneously across thousands of individuals in a **genome-wide association study (GWAS)**. The principle behind GWAS relies on **linkage disequilibrium (LD)**: nearby positions on a chromosome tend to be inherited together because recombination is unlikely to separate them over a few generations. A **tag SNP** is a SNP that is correlated with (in LD with) a block of neighboring variants. By genotyping just the tag SNP, you effectively survey the entire LD block. If a tag SNP shows up more frequently in people with a disease than in controls, something in that chromosomal neighborhood likely contributes to disease risk — even if the tag SNP itself is not the causal variant.

SNPs also serve as the foundation for understanding **population structure** and ancestry. Different human populations carry different SNP frequencies because of genetic drift, natural selection, and migration patterns over thousands of years. Panels of ancestry-informative SNPs can distinguish continental populations and trace migration histories. In clinical genetics, SNPs in drug-metabolizing enzymes (pharmacogenomics) predict whether a patient will respond well or poorly to specific medications. The key conceptual shift is to see SNPs not as individual mutations with individual effects, but as a dense coordinate system for mapping the genome — most SNPs are signposts, not destinations, and their value comes from what they point to rather than what they do themselves.
