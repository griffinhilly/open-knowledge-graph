---
id: randomized-complexity-classes
title: Randomized Algorithms and Probabilistic Complexity Classes
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: probabilistic-computation
  type: hard
- id: bpp-randomized-complexity
  type: hard
builds-toward:
- approximation-hardness-results
tags:
- randomized-algorithms
- BPP
- RP
- ZPP
stage: advanced
status: draft
---

# Randomized Algorithms and Probabilistic Complexity Classes

## Core Idea
Randomized Turing machines accept strings with bounded probability. RP (random polynomial time) languages can be verified with one-sided error; BPP (bounded-error probabilistic polynomial time) allows two-sided error. Surprisingly, BPP ⊆ PSPACE and likely BPP = P, suggesting randomness does not provide a fundamental advantage for polynomial-time computation, though random algorithms are practically powerful.

## Explainer

You already know that a **probabilistic Turing machine** is like an NTM but each nondeterministic branch is taken with equal probability, so the machine's computation is a random variable over its random coin flips. The key question is: how do you define "accepts" when there is a distribution over outcomes? Different answers produce different complexity classes, distinguished by the type and amount of error they tolerate.

**ZPP** (zero-error probabilistic polynomial time) is the most demanding: the machine always gives the correct answer, but is allowed to output "don't know" on some fraction of inputs, provided the expected running time is polynomial. In practice, ZPP = RP ∩ co-RP. **RP** (randomized polynomial time) allows one-sided error: if the answer is YES, the machine accepts with probability ≥ 1/2; if the answer is NO, the machine always rejects. You can never get a false NO, only a false YES. co-RP is the mirror image: no false YES, possible false NO. The asymmetry in RP makes it useful for primality testing: a composite is always detected, but a prime might occasionally be misclassified (though in practice this probability is made negligible).

**BPP** (bounded-error probabilistic polynomial time) is the most permissive of the main classes: the machine accepts correctly with probability ≥ 2/3 on both YES and NO inputs. The choice of 2/3 is arbitrary — by **error amplification** (running the machine k times independently and taking the majority vote), you can reduce the error probability to 2^{−k} at the cost of only a polynomial factor in k. This makes BPP robust: the exact threshold doesn't matter as long as it's bounded away from 1/2. BPP is widely believed to equal P, because pseudorandom number generators can apparently simulate randomness computationally — if one-way functions exist, then P = BPP.

The relationship between these classes and the deterministic hierarchy is: P ⊆ ZPP ⊆ RP ⊆ BPP ⊆ PSPACE, and RP ⊆ NP. Whether RP = NP or BPP = P are major open questions. Intuitively, BPP ⊆ PSPACE because you can deterministically enumerate all possible random strings and take the majority answer, which is in PSPACE. The practical lesson is that randomness is a powerful *engineering* tool — randomized algorithms are often simpler and faster than their deterministic counterparts — but theoretically, it likely provides no asymptotic computational advantage.
