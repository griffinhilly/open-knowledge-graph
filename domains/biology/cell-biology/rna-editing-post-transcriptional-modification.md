---
id: rna-editing-post-transcriptional-modification
title: RNA Editing and Post-Transcriptional Modification
domain: biology
course: cell-biology
prerequisites:
- id: rna-types-and-structure
  type: hard
- id: transcription
  type: soft
builds-toward:
- transfer-rna-structure-and-aminoacylation
tags:
- RNA-editing
- post-transcriptional
- protein-diversity
stage: abstract-reasoning
status: draft
---

# RNA Editing and Post-Transcriptional Modification

## Core Idea
RNA editing involves post-transcriptional insertion, deletion, or substitution of nucleotides, with adenosine-to-inosine (A-to-I, catalyzed by ADAR enzymes) and cytidine-to-uridine (C-to-U, catalyzed by APOBEC enzymes) being the major types. A-to-I editing can change codons (creating new start/stop codons) or alter RNA structure and protein binding properties; notably, APOBEC1-mediated editing of APOB mRNA generates the truncated APOB48 protein from the same transcript. RNA editing provides an additional post-transcriptional layer of proteomic diversity independent of alternative splicing or alternative translation start sites.

## How It's Best Learned
Identify edited sites by comparing cDNA sequences to genomic DNA; measure editing efficiency at specific sites. Characterize ADAR and APOBEC substrate requirements and cellular localization.

## Common Misconceptions
- RNA editing is rare; estimates suggest >50% of human genes undergo A-to-I editing. - Inosine is the same as guanosine; inosine pairs with cytosine and is read as guanosine by translation machinery.

## Explainer

You know that transcription copies DNA into RNA and that RNA structure determines how it functions. But the transcript that leaves the gene is not always the final message. **RNA editing** is a set of post-transcriptional mechanisms that chemically modify individual nucleotides within an RNA molecule, changing its sequence — and therefore its meaning — without altering the underlying DNA. This adds a layer of information processing between genome and proteome that is invisible if you only compare DNA to protein.

The most common type of RNA editing in mammals is **adenosine-to-inosine (A-to-I) editing**, catalyzed by enzymes called **ADARs** (adenosine deaminases acting on RNA). ADAR removes an amino group from adenosine, converting it to inosine. The key consequence: the translation machinery reads inosine as if it were guanosine. So an A-to-I edit in a codon effectively changes an A to a G, which can alter the amino acid specified. For example, editing at a single site in the glutamate receptor GluA2 changes a glutamine codon (CAG) to an arginine codon (CIG, read as CGG), and this single amino acid substitution is essential for normal brain function — unedited GluA2 channels allow too much calcium into neurons.

The second major type is **cytidine-to-uridine (C-to-U) editing**, catalyzed by **APOBEC** enzymes. The textbook example is apolipoprotein B (APOB) mRNA. In the liver, the full-length mRNA is translated into APOB100, a large protein that assembles VLDL particles. In the intestine, APOBEC1 edits a specific cytidine to uridine, creating a premature stop codon midway through the transcript. The result is a truncated protein, APOB48, which assembles chylomicrons instead. Same gene, same mRNA, but a single nucleotide edit produces two functionally distinct proteins in different tissues.

What makes RNA editing conceptually important is that it breaks the one-gene-one-protein assumption in a way that is distinct from alternative splicing. Splicing rearranges existing exons; editing chemically rewrites individual nucleotides. And the scale is much larger than once thought — over half of human genes show evidence of A-to-I editing, mostly in non-coding regions like Alu elements in introns and UTRs, where editing affects RNA folding, stability, and interactions with regulatory proteins. Editing is also tissue-specific and developmentally regulated, meaning the same transcript can carry different edits in different cell types. The genome, it turns out, is less a fixed blueprint and more a starting draft that cells revise post-transcriptionally to meet local needs.
