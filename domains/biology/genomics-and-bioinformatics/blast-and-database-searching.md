---
id: blast-and-database-searching
title: BLAST and Database Searching
domain: biology
course: genomics-and-bioinformatics
prerequisites:
- id: pairwise-sequence-alignment
  type: hard
- id: probability-density-functions
  type: soft
builds-toward:
- functional-annotation
- comparative-genomics
tags:
- BLAST
- E-value
- homology-search
- sequence-database
stage: advanced
status: validated
---
# BLAST and Database Searching

## Core Idea
BLAST (Basic Local Alignment Search Tool) rapidly searches sequence databases by finding short exact matches (seeds), extending them into high-scoring segment pairs, and evaluating statistical significance using E-values. Unlike exact Smith-Waterman, BLAST uses heuristics to achieve speed suitable for searching millions of sequences. The E-value quantifies how many alignments of equal or better score would be expected by chance in a database of that size, making it the primary filter for distinguishing genuine homology from random similarity.

## How It's Best Learned
Run a BLAST search at NCBI with a known protein sequence, then interpret the results: sort by E-value, examine the top hits, and check whether the aligned regions correspond to known domains. Repeat with a randomized version of the same sequence to see what background noise looks like.

## Common Misconceptions
- A low E-value does not mean the sequences have the same function — it means they share significant sequence similarity, which suggests common ancestry but not necessarily conserved function.
- BLAST is not guaranteed to find the mathematically optimal alignment; it is a heuristic that can miss weak but real homologies.

## Questions

```yaml
- question: "A BLAST search returns a hit with an E-value of 1e-50. What does this E-value tell you?"
  type: multiple-choice
  options: ["There is a 1e-50 probability the hit is a true homolog", "You would expect 1e-50 alignments of this score or better by chance in a database this size", "The alignment covers 50% of the query sequence", "The sequences share 50% identity"]
  answer: 1
  explanation: "The E-value (expect value) is the number of alignments with an equal or better score that you would expect to see purely by chance when searching a database of that particular size. An E-value of 1e-50 means such a score would essentially never arise by chance, providing very strong evidence that the similarity reflects true homology. The E-value is not a probability of homology, not a measure of coverage, and not a percent identity."

- question: "BLAST is guaranteed to find the optimal local alignment between a query and every sequence in the database."
  type: true-false
  answer: false
  explanation: "BLAST uses a heuristic seeding strategy: it first finds short exact matches (words) between the query and database sequences, then extends these seeds. This makes BLAST fast enough for large databases, but it can miss alignments that lack a sufficiently high-scoring seed — particularly weak homologies between distantly related sequences. The exact Smith-Waterman algorithm guarantees the optimal local alignment but is too slow for routine database searches."

- question: "Why does the E-value of a BLAST hit depend on the size of the database being searched?"
  type: short-answer
  answer: "A larger database contains more sequences, which means more opportunities for random matches to achieve high scores by chance. The E-value scales roughly linearly with database size: the same alignment score will have a higher (worse) E-value in a larger database because the expected number of chance hits increases. This is why E-values from searches against different databases cannot be directly compared without accounting for database size."
  explanation: "This is analogous to multiple testing in statistics. Searching 10 million sequences instead of 10 thousand means a million times more chances for a spurious match, so the threshold for significance must account for that. BLAST's statistical model (based on Karlin-Altschul statistics) formalizes this relationship."
```

## Explainer

Searching a sequence against a database to find relatives is the bread-and-butter operation of bioinformatics. You have a gene or protein sequence and want to know: what is this? What organisms have something similar? What is its likely function? The Smith-Waterman algorithm gives the exact best local alignment, but running it against millions of database sequences would take days. BLAST, developed by Altschul et al. in 1990, solves this by trading guaranteed optimality for enormous speed gains through a clever heuristic strategy.

BLAST works in three stages. First, it breaks the query into short "words" (typically 3 amino acids for protein, 11 nucleotides for DNA) and identifies all database sequences containing exact or near-exact matches to those words. This seeding step is extremely fast because it uses precomputed lookup tables. Second, it extends each seed in both directions using ungapped alignment, stopping when the score drops below a threshold. Third, it takes the highest-scoring extensions and performs gapped alignment in a narrow band around them. This three-stage filter eliminates the vast majority of database sequences before any expensive computation happens.

The statistical framework behind BLAST results is what makes them interpretable. The key metric is the **E-value** (expect value), derived from Karlin-Altschul statistics. For any alignment score S, the E-value tells you how many alignments scoring at least S you would expect purely by chance in a database of that size with sequences of those compositions. An E-value of 0.001 means you would expect such a score by chance roughly once in every 1,000 database searches. Crucially, E-values depend on database size — the same alignment score produces a higher E-value in a larger database because there are more random comparisons being made, just as running more statistical tests increases the chance of a spurious result.

In practice, E-values below about 1e-5 are generally considered strong evidence of homology, while values between 1e-5 and 0.01 merit careful inspection. But BLAST results require biological judgment beyond the E-value. Two sequences may be clearly homologous (share common ancestry) yet have diverged in function. Conversely, BLAST may miss genuine homologs if the sequences have diverged so far that the seed-finding heuristic fails — a limitation that more sensitive methods like PSI-BLAST and HMM-based searches (HMMER) address by building position-specific profiles from multiple related sequences.
