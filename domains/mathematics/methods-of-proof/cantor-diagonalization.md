---
id: cantor-diagonalization
title: Cantor's Diagonalization Argument
domain: mathematics
course: methods-of-proof
prerequisites:
- id: cardinality-and-countability
  type: hard
- id: proof-by-contradiction
  type: soft
tags:
- diagonalization
- uncountability
- Cantor
- real-numbers
- power-set
stage: formal-systems
status: draft
---

# Cantor's Diagonalization Argument

## Core Idea
Cantor's diagonalization argument proves that the real numbers in [0,1] are uncountable: assume for contradiction that they can be listed r₁, r₂, r₃, …, then construct a new real number d whose nth decimal digit differs from the nth digit of rₙ. This number d is in [0,1] but differs from every entry on the list, contradicting the assumption. The same argument shows that for any set A, the power set P(A) has strictly greater cardinality than A, implying there is no largest infinity.

## How It's Best Learned
Work through the argument step by step with a concrete table of decimal expansions. Explicitly construct d and verify it is not on the list. Then discuss implications: there are infinitely many levels of infinity. Contrast with the countability of ℚ to emphasize how different ℝ is.

## Common Misconceptions
- Thinking the constructed number d could appear somewhere else on the list — d was built precisely to differ from every listed element.
- Worrying about decimal ambiguity (e.g., 0.999… = 1.000…) — this is handled by using digits 1 and 2 only, avoiding nines and zeros.
- Assuming the argument only works for real numbers — it generalizes to any power set.
