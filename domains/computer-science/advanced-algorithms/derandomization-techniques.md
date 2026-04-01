---
id: derandomization-techniques
title: Derandomization Techniques
domain: computer-science
course: advanced-algorithms
prerequisites:
- id: randomized-algorithms
  type: hard
- id: bpp-complexity-class
  type: hard
- id: universal-and-perfect-hashing
  type: soft
- id: expander-graphs
  type: soft
tags:
- derandomization
- pseudorandom-generators
- method-of-conditional-expectations
- pairwise-independence
- nisan-wigderson
stage: expert
status: validated
---

# Derandomization Techniques

## Core Idea
Derandomization converts randomized algorithms into deterministic ones while preserving their efficiency guarantees. The central question is whether randomness is truly necessary for efficient computation -- equivalently, whether P = BPP. Techniques range from the elementary (the method of conditional expectations, which converts an existential probabilistic argument into a greedy deterministic construction) to the deep (Nisan-Wigderson pseudorandom generators, which fool bounded computations with short seeds under circuit lower bound assumptions). Limited independence (pairwise, k-wise) often suffices where full independence seems required, enabling derandomization by exhaustive enumeration over a polynomial-size sample space.

## Questions

```yaml
- question: "The method of conditional expectations derandomizes a randomized algorithm by doing what?"
  type: multiple-choice
  options:
    - "Replacing all random bits with zeros"
    - "Greedily fixing each random bit to the value that keeps the conditional expectation of the objective at least as good as the unconditional expectation"
    - "Running the randomized algorithm many times and taking the best result"
    - "Replacing the random number generator with a hash function"
  answer: 1
  explanation: "The method of conditional expectations uses the probabilistic method constructively. If E[X] >= t, then at least one setting of the random bits achieves X >= t. Fix the first bit to whichever value (0 or 1) keeps E[X | b1] >= t. Then fix the second bit to maintain E[X | b1, b2] >= t, and so on. Each step is deterministic and computable (provided the conditional expectation can be efficiently evaluated), and the final fully-determined assignment achieves X >= t. This converts the randomized MAX-SAT 7/8-approximation into a deterministic one."

- question: "A randomized algorithm uses n independent random bits, but its analysis only requires pairwise independence among O(n) random variables. How many truly random bits suffice for derandomization via pairwise-independent hash families?"
  type: multiple-choice
  options:
    - "O(1) bits"
    - "O(log n) bits"
    - "O(n / log n) bits"
    - "O(n) bits"
  answer: 1
  explanation: "A family of pairwise-independent random variables over {0,1}^n can be constructed from O(log n) truly random bits using linear hash functions over a finite field. Since only O(log n) seed bits are needed, we can enumerate all 2^O(log n) = poly(n) seeds deterministically, evaluate the algorithm on each, and return the best result. The total running time is polynomial times the original algorithm's running time. This technique derandomizes any algorithm whose correctness proof only uses pairwise independence (e.g., Chebyshev-based analyses)."

- question: "The Nisan-Wigderson pseudorandom generator construction assumes the existence of a function computable in E = DTIME(2^O(n)) that requires circuits of size 2^(epsilon * n). Under this assumption, BPP = P."
  type: true-false
  answer: true
  explanation: "Nisan and Wigderson showed that a sufficiently hard function (hard for exponential-size circuits) can be used to construct a pseudorandom generator that stretches O(log n) random bits into poly(n) bits that are indistinguishable from truly random bits by any polynomial-size circuit. Since BPP algorithms are polynomial-size circuits, they cannot distinguish the pseudorandom bits from real randomness. Enumerating all poly(n) seeds (2^O(log n) of them) and taking a majority vote derandomizes any BPP algorithm. The assumption -- that E contains functions requiring exponential circuits -- is widely believed but unproven, which is why BPP = P remains a conjecture."

- question: "Explain why expander graphs are useful for derandomization, particularly in the context of reducing the number of random bits needed for probability amplification."
  type: short-answer
  answer: "Standard probability amplification by independent repetition requires O(k) independent runs to reduce error to 2^(-k), using O(k * r) random bits if each run uses r bits. The expander walk technique replaces independent samples with a random walk on an expander graph whose vertices are the 2^r possible random strings. Starting from a random vertex and taking k steps on the expander uses only r + O(k) random bits total (r for the starting vertex, O(1) per step for the neighbor choice). The expander mixing lemma guarantees that the walk visits vertices that are 'nearly independent' -- specifically, the fraction of bad starting points that lead to too many failures along the walk decreases exponentially in k. This achieves the same exponential error reduction with far fewer random bits."
  explanation: "This is a key result by Ajtai-Komlos-Szemeredi and Impagliazzo-Zuckerman. The expander walk essentially provides a cheap source of nearly-independent samples. The savings from O(k * r) bits to r + O(k) bits can be dramatic -- for example, amplifying a BPP algorithm with error 1/3 to error 2^(-n) uses O(n * poly(n)) random bits naively but only poly(n) + O(n) bits with expander walks. Combined with the Nisan-Wigderson generator, this is part of the toolkit suggesting that randomness can be eliminated entirely under plausible complexity assumptions."
```

## Explainer

Randomized algorithms are often simpler and faster than their deterministic counterparts, but the question of whether randomness is truly necessary is one of the deepest in complexity theory. Derandomization techniques systematically remove the need for randomness while preserving efficiency. The most basic technique is the **method of conditional expectations**, which converts a probabilistic existence argument into a constructive deterministic algorithm. If the expected value of some objective is at least t (so a random assignment achieves t in expectation), then you can fix each random bit greedily: choose the value that keeps the conditional expectation at least t. After all bits are fixed, you have a deterministic assignment achieving at least t. This requires being able to compute conditional expectations efficiently, which is possible for many natural objectives (like the number of satisfied clauses in MAX-SAT).

A more powerful approach exploits **limited independence**. Many randomized algorithms do not actually need their random variables to be fully independent -- pairwise independence or k-wise independence suffices for the analysis (typically because the proof only uses Chebyshev's inequality or bounded moments). A family of pairwise-independent random variables over n bits can be constructed from just O(log n) seed bits using linear functions over finite fields. Since the seed space has polynomial size, you can enumerate all seeds deterministically and pick the best one. This transforms a randomized algorithm into a deterministic one with only a polynomial overhead, provided the analysis relies on limited independence.

At the deepest level, **pseudorandom generators (PRGs)** aim to derandomize all of BPP. The Nisan-Wigderson construction builds a PRG that stretches O(log n) truly random bits into polynomially many bits that no polynomial-size circuit can distinguish from truly random bits. The construction uses a combinatorial design to extract pseudorandom bits from a hard function -- one that is computable in exponential time but requires exponential-size circuits. Under this hardness assumption, BPP = P: every efficient randomized algorithm can be made deterministic with only polynomial overhead. The hardness assumption is widely believed (it follows from standard conjectures about circuit lower bounds) but remains unproven, keeping the P vs BPP question formally open.

**Expander graphs** provide another route to reducing randomness. Standard probability amplification repeats a randomized algorithm independently O(k) times to reduce error probability to 2^(-k), but each repetition uses fresh random bits. The expander walk technique replaces independent repetitions with a walk on an expander graph whose vertices represent random seeds. Because expanders have strong mixing properties, consecutive vertices on a random walk are "nearly independent" for the purposes of error analysis. This reduces the random bit requirement from O(k * r) to r + O(k), where r is the number of bits per trial. Combined with limited independence and PRGs, these techniques form a comprehensive toolkit suggesting that randomness, while convenient, may be computationally eliminable -- that the class BPP equals P.

The practical impact of derandomization extends beyond theory. The method of conditional expectations is routinely used to convert randomized approximation algorithms (like the randomized 7/8-approximation for MAX-3SAT) into deterministic ones. Pairwise-independent hashing underlies deterministic data structures and streaming algorithms. Even when full derandomization is impractical, understanding which properties of randomness an algorithm actually needs (full independence? pairwise? k-wise?) often leads to simpler analyses and more efficient implementations that use fewer random bits.
