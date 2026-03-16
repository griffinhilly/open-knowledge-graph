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

## Explainer

You already know that NP captures problems where a lucky guess — a non-deterministic choice — can verify a solution in polynomial time. BPP introduces a different kind of luck: instead of a single all-knowing guess, the machine flips coins and must get the right answer with high probability regardless of the input. The key word is "regardless": a **BPP algorithm** must work well on every input, not just on easy ones or on average. This is much stronger than an average-case guarantee.

The defining threshold of 2/3 correctness (equivalently, error at most 1/3) looks arbitrary — and it is. The power of BPP comes from **error amplification**: run the algorithm independently k times and take a majority vote. The probability that the majority is wrong drops exponentially in k by the Chernoff bound. So a BPP machine with 51% success probability can be boosted to 1 − 2^{−100} confidence using polynomially many repetitions. The 1/3 threshold is just a convenient landmark; any constant less than 1/2 gives the same class.

Where does BPP sit in the complexity landscape you know? P ⊆ BPP ⊆ PSPACE — randomness cannot help you escape polynomial space, but it might help you avoid exponential time. The biggest open question is whether BPP = P, meaning whether every randomized polynomial-time algorithm could be derandomized into a deterministic one. Most complexity theorists believe the answer is yes. **Adleman's theorem** provides indirect evidence: every BPP problem can be solved by polynomial-size Boolean circuits (BPP ⊆ P/poly). The circuit proof is elegant — for each input length, a good random seed exists by a counting argument, and hardwiring that seed into the circuit gives a deterministic solution.

A concrete anchor is the **Miller-Rabin primality test**: given a number n, it samples random witnesses and declares n composite if any witness exposes it. For a composite n, at least 3/4 of all possible witnesses are revealing, so the error probability after k rounds is at most (1/4)^k — exponentially small. Prime numbers never get a false composite verdict. This is a canonical BPP algorithm: polynomial time, bounded error on every input, and practically fast. (It has since been superseded by AKS, a deterministic polynomial algorithm — consistent with the BPP = P conjecture.) Understanding BPP through this example illustrates how randomness can substitute for exponential search while keeping error tightly controlled.
