---
id: bpp-complexity-class
title: 'BPP: Bounded Error Probabilistic Polynomial Time'
domain: computer-science
course: theory-of-computation
prerequisites:
- id: probabilistic-turing-machines
  type: hard
- id: complexity-class-p-definition
  type: hard
tags:
- complexity-classes
- randomized-algorithms
stage: advanced
status: draft
---

# BPP: Bounded Error Probabilistic Polynomial Time

## Core Idea
BPP is the class of languages decided by a probabilistic PTM in polynomial time with two-sided error at most 1/3 (amplifiable to any ε > 0 via repetition). BPP trivially contains P. It is widely believed (but unproven) that BPP ⊆ NP and BPP ⊆ P with high probability, though NP ⊆ BPP would cause PH to collapse, suggesting BPP is 'small' relative to NP. BPP captures practical randomized algorithms where error probability is controllable and output distribution matters.

## Explainer

You already know that P captures problems solvable efficiently by deterministic machines, and that probabilistic Turing machines extend the deterministic model by allowing random coin flips during computation. **BPP** (Bounded-error Probabilistic Polynomial time) is the complexity class that asks: what can we solve efficiently if we allow randomness, provided we keep errors under control? Specifically, a language L is in BPP if there exists a probabilistic Turing machine that runs in polynomial time and, for every input, gives the correct answer with probability at least 2/3. The machine can err on both sides — it might say "yes" when the answer is "no," or "no" when the answer is "yes" — but each type of error occurs with probability at most 1/3.

The choice of 1/3 as the error bound might seem arbitrary, and in a deep sense it is. The remarkable property of BPP is **error amplification**: by running the same algorithm multiple times and taking a majority vote, you can drive the error probability down exponentially. Run it 100 times and accept the majority answer, and your error probability drops to something astronomically small — far below the chance of a cosmic ray flipping a bit in your deterministic computer. This means the 1/3 threshold is not special; any constant strictly between 0 and 1/2 defines the same class. What matters is the gap between the success probability and 1/2.

Every problem in P is trivially in BPP — a deterministic algorithm is just a probabilistic one that never flips coins, so its error probability is zero. The deeper question is whether BPP is *strictly* larger than P. Most complexity theorists believe BPP = P, meaning randomness does not actually help for decision problems when you have enough time. Evidence for this belief comes from **derandomization** results: under plausible circuit complexity assumptions, every BPP algorithm can be simulated deterministically in polynomial time using pseudorandom generators. The celebrated proof that primality testing is in P (the AKS algorithm) is a concrete example — the randomized Miller-Rabin test was in BPP for decades before a deterministic polynomial algorithm was found.

BPP's relationship to NP is subtle. BPP is not known to be contained in NP, nor is NP known to be contained in BPP. However, if NP ⊆ BPP, the polynomial hierarchy would collapse to its second level — a consequence considered unlikely. This suggests that BPP is "small" and does not contain the hard problems in NP. In practice, BPP captures the power of real-world randomized algorithms: problems like polynomial identity testing and certain approximation tasks where flipping coins yields efficient solutions with controllable, negligible error. The class formalizes the intuition that an algorithm you can trust 99.9999% of the time is, for all practical purposes, as good as a deterministic one.
