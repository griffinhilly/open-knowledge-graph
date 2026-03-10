---
id: proof-by-contradiction
title: Proof by Contradiction
domain: mathematics
course: methods-of-proof
prerequisites:
- id: direct-proof
  type: hard
- id: logical-equivalences
  type: hard
- id: negation-of-quantifiers
  type: soft
builds-toward:
- existence-proofs
- cardinality-and-countability
- cantor-diagonalization
tags:
- contradiction
- reductio-ad-absurdum
- proof-technique
- irrationality
stage: formal-systems
status: draft
---

# Proof by Contradiction

## Core Idea
In a proof by contradiction, you assume the negation of what you wish to prove and derive a logical impossibility — a statement that contradicts a known truth, an axiom, or the hypothesis itself. Since a logical system cannot contain a true contradiction, the assumption must be false, and therefore the original statement must be true. The irrationality of √2 is the canonical example: assume √2 = p/q in lowest terms, then derive that both p and q are even.

## How It's Best Learned
Prove the irrationality of √2 as a class exercise — it is short, memorable, and has been called one of the most elegant proofs in mathematics. Practice identifying what the negation of the goal looks like before starting the proof. Distinguish from proof by contrapositive: contradiction assumes ¬(conclusion) and derives any contradiction, not just ¬(hypothesis).

## Common Misconceptions
- Confusing contradiction with contrapositive — both involve negations, but contradiction is more general.
- Fabricating a contradiction instead of deriving one logically from the assumption.
- Assuming that any surprise or unintuitive result constitutes a contradiction.
