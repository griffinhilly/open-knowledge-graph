---
id: frameshift-mutations-indels
title: Frameshift Mutations and Reading Frame Disruption
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: genetic-code
  type: hard
- id: dna-mutations
  type: hard
builds-toward:
- missense-nonsense-silent-mutation-effects
tags:
- frameshift
- insertions-deletions
- indels
- reading-frame
- genetic-mutations
stage: advanced
status: draft
---

# Frameshift Mutations and Reading Frame Disruption

## Core Idea
Frameshift mutations result from insertion or deletion of nucleotides not divisible by 3, causing the reading frame to shift and producing entirely different amino acid sequences downstream. A single frameshift can render a protein nonfunctional or truncated at a premature stop codon. Frameshift mutations typically cause severe loss-of-function phenotypes, are strongly selected against, and occur at higher rates in regions with repetitive sequences (microsatellites) where slipped-strand mispairing occurs.

## How It's Best Learned
Write out DNA sequences with frameshifts and translate them using all three reading frames to see how sequences diverge downstream. Work with real examples of frameshift disease mutations.

## Common Misconceptions
- Assuming a single frameshift is compensated by another frameshift (only in rare cases with in-frame stop-codon removal).
- Thinking all insertions/deletions are deleterious (in-frame indels affecting only specific domains may be tolerated).
- Confusing frameshift mutations with point mutations in their consequences.

## Explainer

From your study of the genetic code, you know that mRNA is read in consecutive, non-overlapping **triplets** (codons), each specifying one amino acid. The identity of every codon depends entirely on where the reading starts — shift that starting point by even one nucleotide, and every subsequent codon changes. This is the basis of **frameshift mutations**: insertions or deletions of nucleotides whose number is not a multiple of three knock the reading frame out of register, scrambling the entire downstream amino acid sequence.

Consider a concrete example. Suppose a coding sequence reads: `AUG-GCA-UUC-GAA-UAA` (Met-Ala-Phe-Glu-Stop). Now insert a single nucleotide (say, a U) after the first codon: `AUG-UGC-AUU-CGA-AUA-A...`. Every codon after the insertion is different. The protein now reads Met-Cys-Ile-Arg-Ile-... — a completely unrelated amino acid sequence. Worse, the original stop codon (UAA) is destroyed because its nucleotides are now split across different codons. The ribosome will continue translating until it encounters a new stop codon in the shifted frame, which may come much later (producing a longer, nonfunctional protein) or much sooner (producing a truncated fragment). Either way, the protein almost certainly loses its function.

This is why frameshifts are far more destructive than most **point mutations** (single-nucleotide substitutions). A missense point mutation changes only one amino acid; a silent mutation changes none. But a frameshift corrupts *every* amino acid from the mutation site onward. The severity is analogous to the difference between misspelling one word in a sentence versus removing a single letter and then re-breaking all subsequent words: "THE CAT ATE" becomes "THE CTA TE..." — nonsense from the deletion point forward. Deletions of exactly three nucleotides (or multiples of three) are different: they remove one or more amino acids but leave the rest of the reading frame intact. These **in-frame deletions** may or may not disrupt protein function, depending on which amino acids are lost and whether they are structurally critical.

Frameshifts occur at elevated rates in regions containing **microsatellites** — short tandem repeats like AAAAA or CACACACA. During DNA replication, the newly synthesized strand can slip on the template in these repetitive regions (a process called **slipped-strand mispairing**), adding or deleting one or more repeat units. This is why microsatellite loci are hotspots for frameshift mutations, a fact exploited clinically in detecting cancers with mismatch repair deficiency (microsatellite instability). Understanding frameshifts connects your knowledge of the genetic code's triplet structure to the real consequences of mutations in disease and evolution.
