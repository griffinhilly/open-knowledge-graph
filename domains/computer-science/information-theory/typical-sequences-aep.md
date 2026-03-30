---
id: typical-sequences-aep
title: Typical Sequences and the AEP
domain: computer-science
course: information-theory
prerequisites:
- id: shannon-entropy
  type: hard
- id: source-coding-theorem
  type: hard
- id: expected-value
  type: hard
builds-toward:
- channel-coding-theorem
- rate-distortion-theory
tags:
- typical set
- asymptotic equipartition property
- AEP
- law of large numbers
- typicality
stage: expert
status: validated
---

# Typical Sequences and the AEP

## Core Idea
The asymptotic equipartition property (AEP) states that for a long sequence of n i.i.d. random variables, -(1/n) log p(X_1, ..., X_n) converges to H(X) in probability. This means almost all observed sequences have probability approximately 2^(-nH), forming the "typical set" of about 2^(nH) sequences. Although the total number of possible sequences is |alphabet|^n, the typical set is exponentially smaller (when H < log|alphabet|) yet carries nearly all the probability. The AEP is the law of large numbers applied to information and is the foundational tool for proving both source coding and channel coding theorems.

## Questions

```yaml
- question: "A source has alphabet {A, B, C} with probabilities {0.7, 0.2, 0.1} and entropy H ≈ 1.157 bits. For sequences of length n = 1000, approximately how many typical sequences are there, and how does this compare to the total number of sequences?"
  type: multiple-choice
  options:
    - "About 2^1157 typical sequences out of 3^1000 ≈ 2^1585 total — the typical set is a vanishingly small fraction of all sequences but contains nearly all the probability"
    - "About 3^1000 typical sequences — all sequences are typical for large n"
    - "About 1000 typical sequences — one for each position"
    - "About 2^1000 typical sequences — one bit per symbol"
  answer: 0
  explanation: "The typical set has approximately 2^(nH) = 2^(1000 * 1.157) ≈ 2^1157 sequences. The total number of sequences is 3^1000 ≈ 2^1585. The ratio is 2^1157 / 2^1585 = 2^(-428), an astronomically small fraction. Yet these ~2^1157 sequences account for probability approaching 1. The other 2^1585 - 2^1157 ≈ 2^1585 sequences are individually very improbable and collectively carry negligible total probability. This is the AEP: probability concentrates on a 'thin' typical set."

- question: "The AEP guarantees that every high-probability sequence belongs to the typical set."
  type: true-false
  answer: false
  explanation: "The typical set is defined by approximate probability: sequences x^n where 2^(-n(H+epsilon)) <= p(x^n) <= 2^(-n(H-epsilon)). The most probable individual sequence (e.g., all-A for a biased source) has probability much higher than 2^(-nH) and is NOT in the typical set. But its probability is just one sequence — while it may be the single most likely outcome, the typical set contains exponentially many sequences whose collective probability approaches 1. The distinction between the most probable sequence and the set of collectively probable sequences is crucial."

- question: "Explain how the AEP enables the source coding theorem's achievability: why can a source with entropy H be compressed to approximately nH bits for long sequences?"
  type: short-answer
  answer: "The AEP shows that with high probability, the source output falls in the typical set, which contains approximately 2^(nH) sequences. To encode a typical sequence, assign each one a unique binary index — this requires about nH bits (log2 of 2^(nH)). Atypical sequences (which have negligible total probability) can be encoded separately with a flag bit and their raw representation, adding negligible overhead. So the expected code length is approximately nH bits, or H bits per symbol. The AEP provides the bridge between entropy as an abstract quantity and entropy as an achievable compression rate."
  explanation: "This argument also reveals why the source coding theorem is an asymptotic result: the AEP relies on the law of large numbers, which requires large n for the concentration to be tight. For small n, the typical set is not well-separated from the atypical set, and compression cannot achieve H bits per symbol."
```

## Explainer

The AEP is the information-theoretic manifestation of the law of large numbers. For i.i.d. random variables X_1, ..., X_n, the log-probability of the sequence is a sum: log p(X_1, ..., X_n) = sum log p(X_i). By the law of large numbers, the average (1/n) sum log p(X_i) converges to E[log p(X)] = -H(X). So -(1/n) log p(X^n) converges to H(X). This means the probability of almost every observed sequence is approximately 2^(-nH).

The **typical set** A_epsilon^(n) consists of all sequences x^n satisfying |-(1/n) log p(x^n) - H(X)| <= epsilon. The AEP guarantees three properties: (1) Pr(X^n in A_epsilon^(n)) > 1 - delta for large enough n. (2) |A_epsilon^(n)| <= 2^(n(H+epsilon)) — the typical set is small. (3) Each typical sequence has probability between 2^(-n(H+epsilon)) and 2^(-n(H-epsilon)) — they are all approximately equiprobable at the exponential scale. Property 3 explains the name "equipartition": probability is roughly equally distributed among typical sequences.

This structure is the engine behind Shannon's theorems. For **source coding**: since there are about 2^(nH) typical sequences carrying nearly all the probability, assigning nH-bit indices to them achieves near-entropy compression. For **channel coding**: at the receiver, the output sequence is typical given the true codeword. If the code rate R < C, the number of codewords (2^(nR)) is small enough that no other codeword's typical output set overlaps significantly. The decoder can identify the correct codeword with high probability by checking which codeword's conditional typical set contains the received sequence.

The AEP extends beyond i.i.d. sources. For stationary ergodic sources, the Shannon-McMillan-Breiman theorem provides an analogous result: -(1/n) log p(X_1, ..., X_n) converges to the entropy rate almost surely. This generalization underpins information theory's applicability to structured sources like natural language and time series, where successive symbols are far from independent.
