---
id: pseudorandom-generators
title: Pseudorandom Generators
domain: computer-science
course: cryptography
prerequisites:
- id: one-way-functions
  type: hard
- id: random-number-generation
  type: soft
tags:
- prg
- computational-indistinguishability
- seed-expansion
- hard-core-bit
stage: expert
status: validated
---

# Pseudorandom Generators

## Core Idea
A pseudorandom generator (PRG) is a deterministic function G: {0,1}^n → {0,1}^l(n) with l(n) > n (expansion) such that the output on a random seed is computationally indistinguishable from a truly random string of length l(n). No efficient statistical test can tell PRG output from random with non-negligible advantage. PRGs exist if and only if one-way functions exist (HILL theorem). The Goldreich-Levin hard-core bit construction turns any OWF into a PRG by extracting one pseudorandom bit per invocation, then iterating. PRGs are the theoretical foundation of stream ciphers and the basis for building pseudorandom functions.

## Questions

```yaml
- question: "A PRG G maps 128-bit seeds to 256-bit outputs. There are 2^128 possible outputs (one per seed), but 2^256 possible 256-bit strings. Why doesn't this make PRG output trivially distinguishable from random?"
  type: short-answer
  answer: "The 2^128 outputs form a vanishing fraction (2^{-128}) of all 2^256 strings, so a distinguisher with unlimited computation could check membership in this set. But no efficient (polynomial-time) distinguisher can perform this check — it would require either inverting G (which is hard by the OWF assumption) or enumerating all 2^128 seeds. Computational indistinguishability means no polynomial-time test can detect the difference, not that the distributions are identical. The distinction between information-theoretic and computational indistinguishability is precisely the gap that makes PRGs possible."
  explanation: "This is the fundamental insight of computational cryptography. Perfect randomness requires as many random bits as output bits (Shannon's theorem). PRGs cheat by producing output that is statistically biased but computationally indistinguishable from random. Any test that detects the bias requires super-polynomial time, so for all practical purposes the output is random."

- question: "The Goldreich-Levin theorem states that any one-way function f has a hard-core predicate: a bit b(x) that is easy to compute from x but indistinguishable from random given only f(x). How does this yield a PRG?"
  type: multiple-choice
  options:
    - "The hard-core bit is used as the PRG's expansion factor"
    - "Given OWF f and hard-core predicate b, define G(x) = (f(x), b(x)). The output is one bit longer than the input (the hard-core bit is the 'extra' bit), and indistinguishability follows because b(x) looks random given f(x). Iterating this construction by feeding f(x) back as input yields arbitrary-length expansion"
    - "The hard-core bit replaces the need for a seed"
    - "Hard-core predicates are used to verify PRG output, not to construct it"
  answer: 1
  explanation: "G(x) = (f(x), b(x)) expands by exactly one bit. Since b(x) is indistinguishable from random given f(x), the output (f(x), b(x)) is indistinguishable from (f(x), r) where r is a truly random bit. Iterating — computing G(x) = (f(f(...f(x)...)), b(x), b(f(x)), ..., b(f^{n-1}(x))) — produces n pseudorandom bits from one seed. Each bit is hard-core with respect to the remaining state, so the full output is indistinguishable from random. This is the HILL construction that proves OWFs imply PRGs."

- question: "A PRG with expansion factor 2 (mapping n bits to 2n bits) can be composed with itself to achieve any polynomial expansion factor."
  type: true-false
  answer: true
  explanation: "Given G: {0,1}^n → {0,1}^{2n}, split the output into two n-bit halves: G(s) = (s0, s1). Use s0 as the seed for the next application: G(s0) = (s00, s01). This tree-based construction produces 2^k * n bits from an n-bit seed after k levels, with each level doubling the output. A hybrid argument shows that distinguishing the composed output from random requires distinguishing a single application — if the single-step PRG is secure, so is the composed version."

- question: "Why is computational indistinguishability (rather than statistical indistinguishability) the right definition for PRGs?"
  type: multiple-choice
  options:
    - "Statistical indistinguishability is impossible to achieve with deterministic functions"
    - "Computational indistinguishability requires that no polynomial-time algorithm can distinguish the distributions, which is exactly the threat model in cryptography (polynomial-time adversaries). Statistical indistinguishability would require the output distribution to be close to uniform in total variation distance — impossible when the output is longer than the seed, since only 2^n of 2^{l(n)} strings are reachable"
    - "Computational indistinguishability is weaker and therefore easier to prove"
    - "Statistical tests are unreliable, so computational indistinguishability avoids them"
  answer: 1
  explanation: "A PRG with expansion maps 2^n inputs to 2^{l(n)} outputs where l(n) > n. The output distribution has weight on only 2^n points in a space of 2^{l(n)}, so its statistical distance from uniform is at least 1 - 2^{n-l(n)} — essentially 1 for any meaningful expansion. Statistical indistinguishability is literally impossible. Computational indistinguishability is achievable because detecting this statistical bias requires super-polynomial computation. This is the core idea enabling all of computational cryptography."

- question: "A CSPRNG used in practice (like ChaCha20) and a theoretical PRG built from OWFs serve the same conceptual purpose but differ dramatically in efficiency. What explains the gap?"
  type: short-answer
  answer: "The OWF-to-PRG construction (HILL theorem) is an existential proof — it shows PRGs exist if OWFs exist but produces an impractical construction that extracts one bit at a time through iterated OWF evaluation. Practical CSPRNGs like ChaCha20 are designed directly for efficiency using concrete assumptions about a specific cipher's security, without going through the OWF abstraction. The theoretical construction proves possibility; the practical design achieves performance. They meet the same definition but are separated by many orders of magnitude in speed."
  explanation: "This gap between theory and practice is common in cryptography. Theory provides feasibility results and definitional frameworks; practice provides efficient instantiations justified by concrete security analysis. The theoretical result assures us that the goal is achievable; the practical construction is what actually gets deployed."
```

## Explainer

A **pseudorandom generator (PRG)** is a deterministic algorithm that stretches a short, truly random **seed** into a longer output that is computationally indistinguishable from a truly random string of the same length. The seed might be 128 bits; the output might be megabytes. No efficient algorithm — no statistical test, no machine learning model, no adversarial strategy running in polynomial time — can tell the PRG's output from genuine randomness with non-negligible advantage. This is a strictly computational guarantee: an all-powerful adversary could detect the pseudorandomness (only 2^128 of the 2^{huge} possible output strings are reachable), but no adversary with bounded resources can.

The existence of PRGs is equivalent to the existence of **one-way functions** — the most fundamental assumption in cryptography. The forward direction (OWFs imply PRGs) was proven by Hastad, Impagliazzo, Levin, and Luby (the HILL theorem). The construction uses the **Goldreich-Levin hard-core bit**: given any one-way function f, there exists a predicate b(x) that is easy to compute from x but looks random given only f(x). Define G(x) = (f(x), b(x)) — this expands by one bit, and the extra bit is pseudorandom. Iterating (compute f, extract a hard-core bit, use f(x) as the new state) yields arbitrary expansion. The reverse direction is simpler: a PRG is itself a one-way function (inverting G on a random output requires finding the seed from an exponentially small set).

PRGs are the theoretical foundation of **stream ciphers** (which produce a long keystream from a short key and encrypt by XOR) and the first step in the construction chain that builds all of symmetric cryptography from OWFs: OWFs → PRGs → pseudorandom functions → MACs → secure encryption. Each step in this chain is proven by reduction, ensuring that breaking the higher-level primitive implies breaking the lower-level one, which ultimately implies breaking the one-way function.

In practice, deployed CSPRNGs (ChaCha20, AES-CTR used as a PRNG) are not built through the theoretical OWF-to-PRG construction — that construction is correct but horrendously slow, extracting one pseudorandom bit per OWF invocation. Instead, practical PRGs are designed directly using concrete ciphers and analyzed under specific assumptions about those ciphers. The theoretical framework provides the **definitions** (what it means to be pseudorandom) and the **feasibility result** (PRGs can exist), while practice provides efficient instantiations. Understanding the theory explains why the definitions look the way they do and what guarantees they provide — which is essential for correctly using and analyzing the practical constructions.
