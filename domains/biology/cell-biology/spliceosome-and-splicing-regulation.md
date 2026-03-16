---
id: spliceosome-and-splicing-regulation
title: Spliceosome and Splicing Regulation
domain: biology
course: cell-biology
prerequisites:
- id: rna-splicing-mechanisms
  type: hard
- id: gene-regulation-eukaryotes
  type: soft
builds-toward:
- rna-editing-post-transcriptional-modification
tags:
- splicing
- spliceosome
- snRNP
stage: abstract-reasoning
status: draft
---

# Spliceosome and Splicing Regulation

## Core Idea
The spliceosome is a dynamic ribonucleoprotein complex containing five small nuclear RNAs (snRNAs: U1, U2, U4, U5, U6) and over 100 proteins that catalyzes pre-mRNA splicing with exquisite precision at conserved splice sites. Splicing is coupled to transcription, occurring as RNA polymerase II elongates; the C-terminal domain of Pol II recruits splicing factors. Alternative splicing (exon skipping, intron retention, alternative 5' or 3' splice sites) allows a single gene to produce multiple protein isoforms, greatly expanding proteomic diversity without increasing genome size.

## How It's Best Learned
Isolate and characterize spliceosome assembly intermediates; measure splicing kinetics on defined substrates. Map splice site usage genome-wide using RNA-seq; identify tissue-specific or signal-dependent alternative splicing events.

## Common Misconceptions
- The spliceosome cleaves snRNAs to catalyze splicing; snRNAs are the catalytic engine and intact throughout. - Alternative splicing is rare; it occurs in >90% of human genes.

## Explainer

From your study of RNA splicing mechanisms, you understand that eukaryotic pre-mRNA contains introns that must be removed and exons that must be joined before the mRNA can be translated. The **spliceosome** is the molecular machine that performs this task — and it is one of the most complex and dynamic assemblies in the cell, rivaling the ribosome in size and sophistication.

The spliceosome is built from five **small nuclear ribonucleoprotein particles (snRNPs)**, each containing one snRNA molecule (U1, U2, U4, U5, or U6) wrapped in a set of proteins. Unlike the ribosome, which exists as a pre-assembled machine, the spliceosome assembles anew on each intron it removes. U1 snRNP recognizes the 5' splice site through base-pairing between its snRNA and the pre-mRNA sequence. U2 snRNP then binds the branch point sequence within the intron, bulging out a critical adenosine residue. The U4/U6·U5 tri-snRNP joins, and a series of dramatic rearrangements follow: U1 and U4 are displaced, allowing U6 to base-pair with the 5' splice site and with U2 to form the catalytic core. It is the RNA components — not the proteins — that catalyze the two transesterification reactions that cut the intron and join the exons, making the spliceosome a **ribozyme** at heart.

Splicing does not wait until transcription is finished. The spliceosome assembles on the pre-mRNA while **RNA polymerase II** is still elongating the transcript. The C-terminal domain (CTD) of Pol II — a long, repetitive tail that you encountered in transcription regulation — serves as a landing pad for splicing factors, physically coupling transcription speed to splice site recognition. This has a profound consequence: how fast Pol II transcribes through a region can influence which splice sites are used. A slow polymerase gives weak splice sites more time to be recognized; a fast polymerase may cause them to be skipped.

This coupling enables **alternative splicing**, the process that allows a single gene to produce multiple distinct mRNA variants and therefore multiple protein isoforms. The human genome has roughly 20,000 protein-coding genes, yet produces over 100,000 distinct proteins — alternative splicing accounts for much of this expansion. The most common form is **exon skipping**, where a cassette exon is included in some transcripts and excluded in others. Which pattern wins depends on a tug-of-war between **splicing enhancers** (sequences bound by SR proteins that promote exon inclusion) and **splicing silencers** (sequences bound by hnRNP proteins that promote exon skipping). Different cell types express different ratios of these regulatory proteins, so the same gene can produce a muscle-specific isoform, a brain-specific isoform, and a liver-specific isoform — all from a single genomic locus.
