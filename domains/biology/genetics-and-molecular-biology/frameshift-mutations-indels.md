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

## Questions

```yaml
- question: "A coding sequence contains the deletion of 4 nucleotides beginning at position 10. What is the most likely consequence for the encoded protein?"
  type: multiple-choice
  options:
    - "One amino acid is removed from the protein but the rest of the sequence is unaffected"
    - "All amino acids from position 4 onward are changed because the reading frame is shifted by 4"
    - "All amino acids downstream of position 10 are changed because 4 is not divisible by 3, shifting the reading frame"
    - "The mutation is silent because 4 nucleotides encode no complete codon"
  answer: 2
  explanation: "A deletion of 4 nucleotides — not divisible by 3 — shifts the reading frame. Every codon from the deletion site onward is composed of different nucleotides than before, encoding a completely different amino acid sequence. The ribosome reads in non-overlapping triplets from a fixed starting point; remove 4 nucleotides and all subsequent triplets shift by 4 mod 3 = 1 position, scrambling every downstream amino acid. Option A describes an in-frame deletion (divisible by 3). Option D is wrong — the ribosome does not skip; it continues reading in the now-shifted frame. Option B incorrectly states 'from position 4' — the effect begins at the site of the deletion."

- question: "A frameshift mutation at position 50 of a 300-codon gene is compared to a missense mutation at the same position. Which best describes the difference in their effects on the protein?"
  type: multiple-choice
  options:
    - "Both mutations affect only the single amino acid at position 50; the rest of the protein is unchanged"
    - "The missense mutation changes all amino acids from position 50 onward; the frameshift only changes position 50"
    - "The frameshift scrambles every amino acid from position 50 to the end of the protein; the missense mutation changes only the amino acid at position 50"
    - "Both mutations are equally likely to introduce a premature stop codon"
  answer: 2
  explanation: "This is the key reason frameshifts are so catastrophic compared to point mutations. A missense mutation substitutes one nucleotide, changing one codon and thus one amino acid — the rest of the reading frame is intact. A frameshift shifts the entire downstream reading frame, meaning every codon from the mutation site onward encodes a different amino acid (or becomes a stop codon). The analogy: changing one letter in a sentence vs. removing a letter and re-spacing all subsequent words. Option B reverses the descriptions. Option D is wrong — missense mutations do not introduce stop codons by definition; frameshifts frequently encounter new stop codons in the shifted frame."

- question: "A deletion of exactly 6 nucleotides from within a coding sequence will preserve the reading frame of all codons downstream of the deletion site."
  type: true-false
  answer: true
  explanation: "Because the genetic code is read in non-overlapping triplets, removing a number of nucleotides that is a multiple of 3 removes complete codons without disrupting the alignment of downstream codons. A 6-nucleotide (2-codon) deletion removes two amino acids from the protein but leaves every subsequent codon intact. This is called an in-frame deletion, and its effect on protein function depends on which amino acids were deleted and whether they are structurally critical. In-frame deletions can be tolerated (the ΔF508 deletion in CFTR removes one amino acid but is not a frameshift) or devastating, but they are structurally distinct from frameshifts."

- question: "A frameshift mutation affects only the amino acid encoded at the position of the insertion or deletion; downstream amino acids remain encoded by the original sequence."
  type: true-false
  answer: false
  explanation: "This is the defining misconception about frameshifts. Because mRNA is read in consecutive, non-overlapping triplets from a fixed starting point, any shift in that starting point changes every codon that follows. Insert one nucleotide and every subsequent triplet is composed of different nucleotides — the reading frame is disrupted globally from the mutation site to the end of the mRNA. This is fundamentally different from a point mutation, which substitutes one nucleotide and thus affects only the codon containing it. The frame-wide disruption is why frameshifts cause loss-of-function in virtually all cases."

- question: "Why does inserting or deleting a single nucleotide in a coding sequence alter every amino acid downstream of the mutation site, while inserting or deleting three nucleotides may not change any downstream amino acids?"
  type: short-answer
  answer: "The genetic code is read in consecutive, non-overlapping triplets (codons) beginning from a fixed start point. Each codon's identity depends entirely on which three nucleotides are grouped together. Inserting or deleting one nucleotide shifts the grouping of all subsequent nucleotides by one position — every downstream codon is now composed of different nucleotides, encoding different amino acids (or a premature stop codon). The disruption propagates to the end of the mRNA because codons are read sequentially with no mechanism to re-establish the original frame. Inserting or deleting three nucleotides (one complete codon) adds or removes exactly one set of grouped nucleotides without shifting the register of any subsequent codon — downstream triplets are grouped the same way they were before."
  explanation: "The key concept is that codons are defined by their position within a reading frame, not by the nucleotide sequence alone. Shift the frame and every subsequent nucleotide is 'reassigned' to a different codon. This is why frameshift severity scales with how far downstream from the start the mutation occurs — mutations early in the gene corrupt more of the protein — and why in-frame indels (multiples of 3) are structurally distinct."
```

## Explainer

From your study of the genetic code, you know that mRNA is read in consecutive, non-overlapping **triplets** (codons), each specifying one amino acid. The identity of every codon depends entirely on where the reading starts — shift that starting point by even one nucleotide, and every subsequent codon changes. This is the basis of **frameshift mutations**: insertions or deletions of nucleotides whose number is not a multiple of three knock the reading frame out of register, scrambling the entire downstream amino acid sequence.

Consider a concrete example. Suppose a coding sequence reads: `AUG-GCA-UUC-GAA-UAA` (Met-Ala-Phe-Glu-Stop). Now insert a single nucleotide (say, a U) after the first codon: `AUG-UGC-AUU-CGA-AUA-A...`. Every codon after the insertion is different. The protein now reads Met-Cys-Ile-Arg-Ile-... — a completely unrelated amino acid sequence. Worse, the original stop codon (UAA) is destroyed because its nucleotides are now split across different codons. The ribosome will continue translating until it encounters a new stop codon in the shifted frame, which may come much later (producing a longer, nonfunctional protein) or much sooner (producing a truncated fragment). Either way, the protein almost certainly loses its function.

This is why frameshifts are far more destructive than most **point mutations** (single-nucleotide substitutions). A missense point mutation changes only one amino acid; a silent mutation changes none. But a frameshift corrupts *every* amino acid from the mutation site onward. The severity is analogous to the difference between misspelling one word in a sentence versus removing a single letter and then re-breaking all subsequent words: "THE CAT ATE" becomes "THE CTA TE..." — nonsense from the deletion point forward. Deletions of exactly three nucleotides (or multiples of three) are different: they remove one or more amino acids but leave the rest of the reading frame intact. These **in-frame deletions** may or may not disrupt protein function, depending on which amino acids are lost and whether they are structurally critical.

Frameshifts occur at elevated rates in regions containing **microsatellites** — short tandem repeats like AAAAA or CACACACA. During DNA replication, the newly synthesized strand can slip on the template in these repetitive regions (a process called **slipped-strand mispairing**), adding or deleting one or more repeat units. This is why microsatellite loci are hotspots for frameshift mutations, a fact exploited clinically in detecting cancers with mismatch repair deficiency (microsatellite instability). Understanding frameshifts connects your knowledge of the genetic code's triplet structure to the real consequences of mutations in disease and evolution.
