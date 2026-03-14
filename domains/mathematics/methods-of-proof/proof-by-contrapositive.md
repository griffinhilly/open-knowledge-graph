---
id: proof-by-contrapositive
title: Proof by Contrapositive
domain: mathematics
course: methods-of-proof
prerequisites:
- id: direct-proof
  type: hard
- id: logical-equivalences
  type: hard
builds-toward:
- proof-by-contradiction
tags:
- contrapositive
- proof-technique
- logical-equivalence
stage: formal-systems
status: validated
---

# Proof by Contrapositive

## Core Idea
To prove P → Q by contrapositive, you instead prove ¬Q → ¬P, which is logically equivalent. This strategy is advantageous when the negation of Q provides strong, concrete information to work with, while P itself is abstract or hard to use. A proof by contrapositive is a direct proof — just of a different (but equivalent) conditional. The key step is recognizing that P → Q and ¬Q → ¬P are two sides of the same coin.

## How It's Best Learned
Choose examples where the contrapositive is clearly easier: 'If n² is even, then n is even' is hard to prove directly but easy by contrapositive. Always state explicitly: 'We prove the contrapositive. Assume ¬Q...' so the logical structure is transparent.

## Common Misconceptions
- Confusing the contrapositive (¬Q → ¬P) with the inverse (¬P → ¬Q) — only the contrapositive is equivalent.
- Forgetting to state that you are proving the contrapositive, making the proof confusing.
- Assuming that if contrapositive works, contradiction must also be needed — often contrapositive alone is cleaner.
