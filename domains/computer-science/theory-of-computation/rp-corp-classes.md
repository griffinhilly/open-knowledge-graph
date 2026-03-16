---
id: rp-corp-classes
title: RP and coRP Complexity Classes
domain: computer-science
course: theory-of-computation
prerequisites:
- id: probabilistic-turing-machines
  type: hard
builds-toward:
- bpp-complexity-class
tags:
- complexity-classes
- one-sided-error
stage: advanced
status: draft
---

# RP and coRP Complexity Classes

## Core Idea
RP (randomized polynomial time) allows one-sided error: if x ∈ L, accept with probability ≥ 1/2; if x ∉ L, always reject (no false negatives, possibly false positives). coRP is the complement. Both are contained in BPP. RP is the probabilistic analog of NP; coRP to coNP. These classes model practical algorithms where false answers only occur in one direction and are amplifiable via repetition. RP and coRP provide finer granularity than BPP for understanding randomized algorithm error structures.

## Explainer

From your work with probabilistic Turing machines, you know that randomness can be a computational resource — a machine that flips coins during its execution can sometimes solve problems more efficiently than a deterministic one. **RP** and **coRP** capture a particularly clean and useful form of randomized computation: algorithms that can only make mistakes in one direction.

An **RP** (Randomized Polynomial time) algorithm has this guarantee: if the true answer is "no," the algorithm always says "no" — it never produces a false positive. But if the true answer is "yes," the algorithm might incorrectly say "no" with probability up to 1/2. Think of it like a metal detector that never beeps for non-metal objects but might miss some metal ones. The key insight is that this one-sided error is easily fixable by repetition: run the algorithm k times, and if it ever says "yes," accept. The probability of missing a true "yes" k times in a row is at most (1/2)^k, which shrinks exponentially. After 100 repetitions, the failure probability is less than 10^-30.

**coRP** is the mirror image: if the true answer is "yes," the algorithm always says "yes" (no false negatives), but it might incorrectly say "yes" when the answer is really "no" (false positives allowed). The classic example is the Miller-Rabin primality test, which sits in coRP: if it declares a number composite, it is certainly composite, but if it declares a number prime, there is a small chance of error. Again, repetition drives the error probability to negligible levels.

Both RP and coRP sit inside **BPP** (bounded-error probabilistic polynomial time), which allows two-sided error. The containment chain is P ⊆ RP ⊆ BPP and P ⊆ coRP ⊆ BPP. It is widely conjectured that P = BPP — that randomness does not actually help for decision problems — which would collapse RP and coRP into P as well. But proving this remains open. In practice, RP and coRP algorithms are valued precisely because their one-sided error makes them trustworthy in one direction without any repetition at all: when an RP algorithm says "yes," you can believe it unconditionally.
