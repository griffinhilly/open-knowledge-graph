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
status: validated
---

# Single Nucleotide Polymorphisms and Genetic Variation

## Core Idea
Single nucleotide polymorphisms (SNPs) are single-base variations that occur ~1 per 300 bp in the human genome, with ~4-5 million SNPs per person. Most SNPs are neutral (in intergenic or 3rd-codon-position sites), though tag SNPs in linkage disequilibrium with functional variants enable genome-wide association studies (GWAS). SNPs are the most abundant genetic markers and form the basis for understanding genetic diversity, population structure, and disease susceptibility.

## Questions

```yaml
- question: "A genome-wide association study identifies a tag SNP that occurs significantly more often in people with Type 2 diabetes than in healthy controls. What is the correct interpretation?"
  type: multiple-choice
  options:
    - "The tag SNP itself directly causes Type 2 diabetes by altering a protein involved in glucose metabolism"
    - "Something in the chromosomal region surrounding the tag SNP likely contributes to Type 2 diabetes risk — the tag SNP is a marker, not necessarily the causal variant"
    - "People with the tag SNP will definitely develop Type 2 diabetes because the SNP is disease-causing"
    - "The association is spurious — SNPs are neutral by definition and cannot be associated with disease"
  answer: 1
  explanation: "A tag SNP is a marker in linkage disequilibrium with a block of nearby variants. It flags a chromosomal neighborhood, not a specific causal variant. If the tag SNP is associated with Type 2 diabetes, the actual functional variant affecting disease risk is likely somewhere in the same LD block — it could be the tag SNP itself, a nearby coding SNP, a regulatory variant, or an insertion/deletion. GWAS identifies genomic regions worth investigating, not confirmed causal variants. The key insight is that tag SNPs are signposts pointing to regions, not destinations with known functional effects."

- question: "Why are most SNPs in the human genome neutral — having no detectable effect on fitness or phenotype?"
  type: multiple-choice
  options:
    - "Because SNPs are always located in repetitive DNA regions that have no function"
    - "Because the mutation rate is too low for SNPs to affect protein-coding sequences"
    - "Because most SNPs fall in intergenic regions or in synonymous codon positions, where base changes do not alter amino acid sequences or gene regulation"
    - "Because natural selection has eliminated all SNPs that could affect phenotype"
  answer: 2
  explanation: "The human genome is mostly non-coding: roughly 98% of the sequence lies outside protein-coding exons. SNPs that fall in intergenic regions have no direct effect on protein sequence. Among SNPs within genes, many land in the third position of codons, where the genetic code's redundancy (wobble) means many base changes code for the same amino acid — these synonymous or silent SNPs change the DNA letter without changing the protein. Only a small minority of SNPs are nonsynonymous (amino acid-changing), and an even smaller fraction meaningfully affect function. Neutrality is the default expectation for a random base change in a large genome."

- question: "In genome-wide association studies, a tag SNP is useful because genotyping it surveys the genetic variation of the entire linkage disequilibrium block surrounding it, not just the tag SNP's own variant."
  type: true-false
  answer: true
  explanation: "This is the core principle that makes GWAS practical. Because nearby positions on a chromosome tend to be inherited together (they are in linkage disequilibrium), a tag SNP that correlates with the other variants in its LD block serves as a proxy for all of them. Genotyping arrays that include well-chosen tag SNPs can therefore survey hundreds of thousands of common variants across the genome without needing to directly genotype every single SNP. If the tag SNP shows disease association, the entire LD block — potentially containing dozens of variants — is implicated and can be fine-mapped."

- question: "If a SNP is identified in a GWAS as strongly associated with a disease, it must be a nonsynonymous coding SNP that alters protein function."
  type: true-false
  answer: false
  explanation: "GWAS associations do not require the identified SNP (or even the causal variant in the same LD block) to be coding. Many GWAS hits map to intronic or intergenic regions, where the functional variant may affect gene regulation — a promoter element, an enhancer, a splice site — rather than the amino acid sequence of a protein. The tag SNP itself is often not in a coding region; it simply flags a chromosomal neighborhood. Fine-mapping and functional follow-up are required to identify the actual causal variant and its mechanism. Assuming GWAS hits must be nonsynonymous coding variants is one of the most common misinterpretations of the field."

- question: "What is linkage disequilibrium, and why does it make SNPs useful as genetic markers even when the SNPs themselves are not the functional variants of interest?"
  type: short-answer
  answer: "Linkage disequilibrium (LD) is the tendency for alleles at nearby positions on a chromosome to be inherited together — they are correlated because recombination rarely separates adjacent positions in a few generations. This creates blocks of variants that travel through populations as units. A tag SNP that is in high LD with a functional variant will show up more often in people who carry the functional variant, making the tag SNP a reliable proxy for the functional variant. GWAS exploits this: by genotyping a well-chosen set of tag SNPs, researchers can survey millions of common variants across the genome at lower cost, because each tag SNP represents an entire LD block of variants, not just itself."
  explanation: "The practical consequence is that SNPs are most valuable not for what they individually do, but for what they point to. A SNP with no functional consequence can still be an excellent marker for a nearby variant that does have functional consequence, if the two are in high LD. This is why the key conceptual shift is from thinking of SNPs as individual mutations with individual effects to thinking of them as a dense coordinate system for mapping the genome. Their value is geographic: they mark locations and allow researchers to narrow down the search space for causal variants."
```

## Explainer

You already know that mutations are changes in DNA sequence — but not every mutation is a SNP. A **single nucleotide polymorphism (SNP)** is specifically a single-base position where two or more variants exist in a population at a frequency of at least 1%. This frequency threshold is what distinguishes a SNP from a rare mutation: if fewer than 1 in 100 people carry the variant, it is typically classified as a rare variant rather than a polymorphism. With roughly one SNP every 300 base pairs, the human genome contains millions of these common variation points, making SNPs by far the most abundant type of genetic marker.

Most SNPs have no detectable effect on the organism. This makes sense when you consider where they tend to fall. The vast majority occur in **intergenic regions** — stretches of DNA between genes that do not encode proteins. Among SNPs that fall within genes, many land in the **third position of codons**, where the genetic code's redundancy (wobble) means a base change often codes for the same amino acid. These **synonymous SNPs** change the DNA letter but not the protein product. Only a small fraction of SNPs are **nonsynonymous** — altering the amino acid sequence — and an even smaller fraction meaningfully affect protein function or gene regulation.

The real power of SNPs lies in their use as **genetic markers**. Because SNPs are so densely distributed and easy to genotype with modern microarray technology, researchers can scan hundreds of thousands of SNPs simultaneously across thousands of individuals in a **genome-wide association study (GWAS)**. The principle behind GWAS relies on **linkage disequilibrium (LD)**: nearby positions on a chromosome tend to be inherited together because recombination is unlikely to separate them over a few generations. A **tag SNP** is a SNP that is correlated with (in LD with) a block of neighboring variants. By genotyping just the tag SNP, you effectively survey the entire LD block. If a tag SNP shows up more frequently in people with a disease than in controls, something in that chromosomal neighborhood likely contributes to disease risk — even if the tag SNP itself is not the causal variant.

SNPs also serve as the foundation for understanding **population structure** and ancestry. Different human populations carry different SNP frequencies because of genetic drift, natural selection, and migration patterns over thousands of years. Panels of ancestry-informative SNPs can distinguish continental populations and trace migration histories. In clinical genetics, SNPs in drug-metabolizing enzymes (pharmacogenomics) predict whether a patient will respond well or poorly to specific medications. The key conceptual shift is to see SNPs not as individual mutations with individual effects, but as a dense coordinate system for mapping the genome — most SNPs are signposts, not destinations, and their value comes from what they point to rather than what they do themselves.
