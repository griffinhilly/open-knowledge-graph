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
stage: formal-systems
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

## Questions

```yaml
- question: "A gene has a 1-nucleotide deletion 50 bp after the start codon, and then 150 bp further downstream, a 1-nucleotide insertion. A student predicts the protein is probably functional from the insertion site onward, since these two changes together restore the original reading frame. What is the most important problem with this prediction?"
  type: multiple-choice
  options:
    - "The prediction is correct — when the reading frame is restored, downstream amino acids are normal"
    - "The reading frame is restored after the insertion, but the 150-nucleotide region between the two mutations is still completely frameshifted — encoding wrong amino acids and almost certainly containing a premature stop codon that terminates translation before the insertion site"
    - "Single-nucleotide deletions and insertions can never cancel each other out in any circumstance"
    - "The insertion would need to be in the same codon as the deletion to have any compensating effect"
  answer: 1
  explanation: "The student correctly identifies that a -1 deletion followed by a +1 insertion yields a net frameshift of zero — downstream codons after the insertion are back in the correct reading frame. But this ignores what happens in between. The 150-nucleotide stretch between the two mutations is read in the wrong frame, producing a completely garbled amino acid sequence. Critically, in a randomly frameshifted sequence, a stop codon (UAA, UAG, or UGA) appears on average every ~20 codons — so the ribosome almost certainly terminates translation before ever reaching the 'restored' region downstream of the insertion. Compensating mutations only produce near-normal proteins when they are very close together."

- question: "Why is a 3-nucleotide deletion in a coding sequence typically much less damaging than a 1-nucleotide deletion?"
  type: multiple-choice
  options:
    - "Three-nucleotide deletions are repaired more efficiently by cellular proofreading mechanisms"
    - "A 3-nucleotide deletion removes one complete codon without shifting the reading frame of any downstream codon, potentially producing a protein missing just one amino acid; a 1-nucleotide deletion shifts every downstream codon, garbling the entire rest of the protein"
    - "Three-nucleotide deletions only occur in non-coding introns, so they cannot affect protein sequence"
    - "A 1-nucleotide deletion is more likely to occur in an essential gene, making it more harmful by coincidence"
  answer: 1
  explanation: "The genetic code is read in strict non-overlapping triplets. A deletion of exactly 3 nucleotides (or any multiple of 3) removes whole codons but leaves the reading frame intact — the ribosome resumes reading correctly immediately after the deletion. The protein may be missing one or a few amino acids and may lose function if those residues are critical, but the rest of the sequence is unaffected. A 1-nucleotide deletion shifts the triplet boundaries for every codon that follows, producing a completely different and usually nonfunctional amino acid sequence from that point on."

- question: "A frameshift mutation in the middle of a long protein-coding gene almost always produces a nonfunctional protein, even if the mutation occurs far from the active site, partly because the scrambled downstream codons frequently contain a premature stop codon."
  type: true-false
  answer: true
  explanation: "In a randomly scrambled sequence (i.e., the wrong reading frame), stop codons (UAA, UAG, UGA) occur with the frequency expected by chance — approximately once every 20 codons. So even if the frameshift occurs hundreds of nucleotides upstream of the active site, the ribosome will almost certainly encounter a premature stop codon well before completing translation of the full-length protein. The truncated, garbled protein that results is typically nonfunctional and is often targeted for degradation."

- question: "An insertion of 4 nucleotides into a protein-coding sequence is less damaging to protein function than an insertion of 3 nucleotides, because 4 is larger and therefore removes more of the downstream coding sequence."
  type: true-false
  answer: false
  explanation: "The key variable is not the size of the indel but whether the size is divisible by three. A 3-nucleotide insertion adds exactly one codon without disturbing the reading frame of any downstream codon — it is an in-frame indel that may add one amino acid but leaves the rest of the protein intact. A 4-nucleotide insertion shifts the reading frame (4 mod 3 = 1), corrupting every downstream codon. By the same logic, a 6-nt insertion is less damaging than a 4-nt insertion, and a 9-nt insertion less damaging than a 7-nt insertion. Size is misleading; divisibility by three is what matters."

- question: "Explain in terms of how the ribosome reads mRNA why a single-nucleotide deletion corrupts every codon downstream, while a deletion of exactly 3 nucleotides can be tolerated much better."
  type: short-answer
  answer: "The ribosome reads mRNA in consecutive, non-overlapping triplets starting from the AUG start codon — there are no punctuation marks or spaces between codons. The reading frame is defined entirely by where counting begins and is maintained by always advancing exactly 3 nucleotides per codon. If one nucleotide is deleted, the ribosome still advances 3 at a time, but every triplet after the deletion is now shifted by one position relative to the original sequence. What was codon 10 is now read as the last 2 nucleotides of what was codon 10 plus the first nucleotide of what was codon 11 — a completely different codon. This shift propagates through the rest of the mRNA. A 3-nucleotide deletion, by contrast, removes exactly one triplet. The ribosome skips that codon but then resumes reading the original sequence in the original frame — because 3 nucleotides gone means the next nucleotide after the deletion is still the first nucleotide of the next original codon."
  explanation: "This is why the divisibility-by-three rule is the central principle for predicting frameshift severity. It also explains why even very short frameshifted regions (between two compensating mutations) are likely to be lethal to protein function — the scrambled codons don't just change amino acids, they almost certainly introduce a premature stop that prevents translation from reaching the corrected region."
```

## Explainer

From your study of point mutations, you know that a single nucleotide change can be silent (synonymous), alter an amino acid (missense), or create a premature stop codon (nonsense). **Frameshift mutations** are fundamentally different in their destructive potential because they do not just change one codon — they corrupt every codon downstream of the mutation. The reason lies in how the ribosome reads mRNA: it processes the sequence in consecutive, non-overlapping triplets starting from the start codon. There are no commas or spaces between codons. The **reading frame** is set by the start position and maintained by reading exactly three nucleotides at a time.

Now imagine deleting a single nucleotide from the middle of a coding sequence. The ribosome still reads in triplets, but every triplet after the deletion is shifted by one position. Consider the sequence AUG-GCU-UAC-GGA coding for Met-Ala-Tyr-Gly. Delete the first G from GCU to get AUG-CUU-ACG-GA..., which now reads Met-Leu-Thr-and then a completely different downstream sequence. Every amino acid after the deletion is wrong. The same logic applies to single-nucleotide insertions — adding one base shifts the reading frame in the opposite direction. The result is almost always a nonfunctional protein, because the entire downstream amino acid sequence is garbled and a premature stop codon is usually encountered within a short distance.

The key distinction is **divisibility by three**. An insertion or deletion of exactly 3 nucleotides (or 6, 9, etc.) adds or removes whole codons without disturbing the reading frame of surrounding codons — these are called **in-frame indels** and may produce a protein with one or a few extra or missing amino acids, potentially retaining some function. But a 1-, 2-, 4-, or 5-nucleotide indel shifts the frame and is almost always catastrophic. This is why frameshift mutations are generally more damaging than missense mutations: a missense changes one amino acid while a frameshift changes all of them from that point onward.

Frameshifts are especially common in **homopolymeric tracts** — runs of the same nucleotide like AAAAAAA or CCCCCCC. During replication, the polymerase can slip on these repetitive sequences, causing the template and new strand to misalign by one or more repeats. This **replication slippage** inserts or deletes nucleotides, and if the tract is within a coding region, the result is a frameshift. Microsatellite instability in cancers with mismatch repair defects (like Lynch syndrome) is driven by exactly this mechanism. Understanding frameshifts also explains why certain engineered mutations — like inserting a single nucleotide near the start of a gene — can be used experimentally to completely knock out gene function.
