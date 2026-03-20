---
id: frameshift-insertions-deletions
title: Frameshift Mutations and Insertions/Deletions
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: point-mutations-silent-missense-nonsense
  type: hard
- id: genetic-code
  type: soft
builds-toward:
- spontaneous-mutation-rates-causes
tags:
- mutations
- indels
- frameshift
- translation
stage: advanced
status: draft
---

# Frameshift Mutations and Insertions/Deletions

## Core Idea
Insertions or deletions that are not multiples of three nucleotides shift the reading frame, altering all downstream codons and usually producing non-functional proteins. The severity of frameshift mutations is typically greater than point mutations because they affect all codons downstream of the mutation.

## How It's Best Learned
Manually translate a sequence, then insert or delete nucleotides and retranslate to visualize how the reading frame shifts and codons change. Compare frameshift effects with missense or nonsense mutations on the same region.

## Common Misconceptions
- Assuming a deletion in one codon is recovered by an insertion elsewhere in the same gene.
- Not recognizing that small indels in regulatory regions can have large effects.
- Underestimating the probability of frameshift mutations in homopolymeric tracts.

## Explainer

From your study of point mutations, you know that a single nucleotide change can be silent (synonymous), alter an amino acid (missense), or create a premature stop codon (nonsense). **Frameshift mutations** are fundamentally different in their destructive potential because they do not just change one codon — they corrupt every codon downstream of the mutation. The reason lies in how the ribosome reads mRNA: it processes the sequence in consecutive, non-overlapping triplets starting from the start codon. There are no commas or spaces between codons. The **reading frame** is set by the start position and maintained by reading exactly three nucleotides at a time.

Now imagine deleting a single nucleotide from the middle of a coding sequence. The ribosome still reads in triplets, but every triplet after the deletion is shifted by one position. Consider the sequence AUG-GCU-UAC-GGA coding for Met-Ala-Tyr-Gly. Delete the first G from GCU to get AUG-CUU-ACG-GA..., which now reads Met-Leu-Thr-and then a completely different downstream sequence. Every amino acid after the deletion is wrong. The same logic applies to single-nucleotide insertions — adding one base shifts the reading frame in the opposite direction. The result is almost always a nonfunctional protein, because the entire downstream amino acid sequence is garbled and a premature stop codon is usually encountered within a short distance.

The key distinction is **divisibility by three**. An insertion or deletion of exactly 3 nucleotides (or 6, 9, etc.) adds or removes whole codons without disturbing the reading frame of surrounding codons — these are called **in-frame indels** and may produce a protein with one or a few extra or missing amino acids, potentially retaining some function. But a 1-, 2-, 4-, or 5-nucleotide indel shifts the frame and is almost always catastrophic. This is why frameshift mutations are generally more damaging than missense mutations: a missense changes one amino acid while a frameshift changes all of them from that point onward.

Frameshifts are especially common in **homopolymeric tracts** — runs of the same nucleotide like AAAAAAA or CCCCCCC. During replication, the polymerase can slip on these repetitive sequences, causing the template and new strand to misalign by one or more repeats. This **replication slippage** inserts or deletes nucleotides, and if the tract is within a coding region, the result is a frameshift. Microsatellite instability in cancers with mismatch repair defects (like Lynch syndrome) is driven by exactly this mechanism. Understanding frameshifts also explains why certain engineered mutations — like inserting a single nucleotide near the start of a gene — can be used experimentally to completely knock out gene function.
