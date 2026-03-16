---
id: alternative-rna-splicing
title: Alternative Splicing and Protein Isoforms
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: rna-splicing-introns-exons-spliceosome
  type: hard
builds-toward:
- protein-evolution
- gene-expression-overview
tags:
- alternative-splicing
- splicing
- isoforms
- protein-diversity
stage: formal-systems
status: draft
---

# Alternative Splicing and Protein Isoforms

## Core Idea
Alternative splicing allows a single gene to produce multiple protein isoforms by including or excluding different exons, using alternative splice sites, or retaining introns. This greatly increases protein diversity without increasing genome size and allows tissue-specific or condition-specific protein expression.

## How It's Best Learned
Map exon-intron structures of a gene with multiple isoforms and identify which exons are included in each splice variant. Consider how alternative splicing alters protein function, localization, or stability. Study examples in immunoglobulin or muscle protein genes.

## Common Misconceptions
- Assuming alternative splicing is rare or exotic when it occurs for most human genes.
- Not recognizing that splice-site mutations can disrupt normal splicing patterns and cause disease.
- Thinking alternative splicing is purely constitutive when it is highly regulated by tissue and developmental stage.

## Explainer

From your study of RNA splicing, you know that pre-mRNA contains exons (coding regions) and introns (non-coding regions), and that the spliceosome removes introns and joins exons to produce mature mRNA. In constitutive splicing, every exon is included in the final transcript every time. **Alternative splicing** changes the rules: the spliceosome can mix and match which exons are included, producing different mRNA variants — and therefore different proteins — from the same gene.

There are several patterns of alternative splicing. In **exon skipping**, the most common form in animals, an entire exon is either included or left out. In **alternative 5' or 3' splice site** selection, the spliceosome recognizes a different boundary within the same exon, making it longer or shorter. In **intron retention**, an intron that would normally be removed is kept in the mature mRNA, often introducing a premature stop codon that truncates the protein. A single gene can combine multiple patterns, producing dozens or even thousands of distinct isoforms. The Drosophila *Dscam* gene, which encodes a cell-surface receptor involved in neuronal wiring, can theoretically generate over 38,000 distinct mRNA variants through combinatorial exon selection — more splice variants from one gene than the total number of genes in the fly genome.

What controls which exons are included? Regulatory proteins called **splicing factors** bind to sequences within the pre-mRNA near splice sites. Some are enhancers (SR proteins) that recruit the spliceosome to a nearby splice site, promoting exon inclusion. Others are silencers (hnRNP proteins) that block spliceosome assembly, causing exon skipping. Because different cell types express different combinations of splicing factors, the same gene can produce one protein isoform in the brain and a completely different isoform in muscle. For example, the *tropomyosin* gene produces distinct variants in skeletal muscle, smooth muscle, and non-muscle cells, each with different actin-binding properties suited to the contractile needs of that tissue.

The biological significance of alternative splicing is hard to overstate. Over 95% of human multi-exon genes undergo alternative splicing, meaning our roughly 20,000 protein-coding genes produce well over 100,000 distinct proteins. This is a major reason why organism complexity does not scale linearly with gene number — humans have roughly the same number of genes as a nematode worm, but far more complex alternative splicing regulation. When alternative splicing goes wrong — through mutations in splice sites or splicing factors — the consequences can be severe. Aberrant splicing underlies diseases including spinal muscular atrophy, certain cancers, and frontotemporal dementia, making it a growing target for therapeutic intervention.
