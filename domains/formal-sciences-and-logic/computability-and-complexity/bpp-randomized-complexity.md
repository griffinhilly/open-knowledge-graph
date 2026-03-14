---
id: bpp-randomized-complexity
title: BPP and Randomized Complexity
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: probabilistic-computation
  type: hard
- id: np-and-polynomial-time
  type: hard
builds-toward:
- interactive-proofs
- circuit-complexity
tags:
- complexity
- randomness
- derandomization
- BPP
stage: formal-systems
status: draft
---

# BPP and Randomized Complexity

## Core Idea
BPP (Bounded-error Probabilistic Polynomial time) is the class of decision problems solvable by a probabilistic Turing machine in polynomial time with error probability at most 1/3 on every input. The error can be driven exponentially small by independent repetition and majority voting. BPP sits between P and PSPACE (P is in BPP is in PSPACE), and is widely conjectured to equal P — meaning randomness likely does not help for decision problems. The Adleman-Sipser-Gacs theorem shows BPP is in P/poly (solvable by polynomial-size circuits), and conditional derandomization results based on circuit lower bounds support BPP = P.

## How It's Best Learned
Study the Miller-Rabin primality test as a concrete BPP algorithm: it runs in polynomial time, always says "prime" for primes, and says "composite" with high probability for composites. Then prove the error-reduction lemma (amplification by repetition) to see why the 1/3 threshold is arbitrary. Finally, study Adleman's theorem (BPP is in P/poly) to understand the derandomization paradigm.

## Common Misconceptions
- BPP requires bounded error on EVERY input, not just on average — this is much stronger than average-case efficiency.
- BPP is not known to contain NP, and is widely believed not to — randomness helps with efficiency, not with verifying arbitrary certificates.
