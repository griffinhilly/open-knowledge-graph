---
id: direct-proof
title: Direct Proof
domain: mathematics
course: methods-of-proof
prerequisites:
- id: proof-structure-and-terminology
  type: hard
- id: logical-equivalences
  type: soft
- id: even-and-odd-numbers
  type: soft
- id: factors-and-multiples
  type: soft
builds-toward:
- proof-by-contrapositive
- proof-by-contradiction
- proof-by-cases
- existence-proofs
- mathematical-induction
tags:
- direct-proof
- proof-technique
- divisibility
- even-odd
stage: formal-systems
status: validated
---

# Direct Proof

## Core Idea
A direct proof of P → Q assumes P is true and uses logical deduction — applying definitions, algebraic manipulations, and previously proven results — to conclude Q. It is the most natural proof strategy: start from what you know and derive what you want to show. Canonical first examples include proving that the sum of two even integers is even, or that the product of two odd integers is odd.

## How It's Best Learned
Work heavily with divisibility and even/odd parity as the first domain, since the algebra is simple and the logical structure is clear. Require students to write out every step, including why each step is valid. Gradually reduce scaffolding as fluency builds.

## Common Misconceptions
- Beginning by assuming what is to be proven (circular reasoning).
- Skipping algebraic steps because they feel obvious — rigor requires justification.
- Confusing the direction: a direct proof of P → Q is not the same as proving Q → P.
