---
id: p-vs-np-problem
title: The P vs. NP Problem
domain: computer-science
course: theory-of-computation
prerequisites:
- id: nondeterministic-complexity
  type: hard
builds-toward:
- np-completeness
- cook-levin-theorem
tags:
- P-vs-NP
- open-problem
- complexity
- foundations
stage: advanced
status: draft
---

# The P vs. NP Problem

## Core Idea
The P vs. NP problem asks whether every problem whose solution can be verified in polynomial time can also be solved in polynomial time: does P = NP? It is one of the seven Millennium Prize Problems and widely considered the most important open question in computer science. Most researchers believe P ≠ NP — that some problems are intrinsically harder to solve than to verify — but no proof exists. A P = NP proof would imply efficient algorithms for optimization, cryptography, and AI problems; P ≠ NP underpins the security of virtually all modern cryptographic systems.

## How It's Best Learned
Study why the question is hard to resolve: both directions require proving a lower bound (that no polynomial algorithm exists) or an algorithm, both of which have resisted all attempts. Examine the philosophical and practical consequences of each outcome.

## Common Misconceptions
- Thinking P ≠ NP has been proved — it has not; it remains open.
- Assuming NP-hard problems have no fast algorithms in practice — heuristics, approximations, and special-case algorithms often work well even if worst-case hardness holds.
- Conflating P ≠ NP with 'cryptography is secure' — this logical implication exists, but a proof of P ≠ NP wouldn't directly yield secure cryptographic constructions.
