---
id: logical-equivalences
title: Logical Equivalences
domain: mathematics
course: methods-of-proof
prerequisites:
- id: truth-tables
  type: hard
- id: conditional-and-biconditional
  type: hard
builds-toward:
- proof-structure-and-terminology
- direct-proof
- proof-by-contrapositive
- proof-by-contradiction
tags:
- logical-equivalence
- De-Morgans-laws
- tautology
- double-negation
- absorption
stage: formal-systems
status: validated
---

# Logical Equivalences

## Core Idea
Two statements are logically equivalent if they have identical truth values in every possible case, written P ≡ Q. Key equivalences include De Morgan's laws (¬(P ∧ Q) ≡ ¬P ∨ ¬Q), double negation (¬¬P ≡ P), and the equivalence of a conditional to its contrapositive (P → Q ≡ ¬Q → ¬P). Logical equivalences allow mathematicians to rewrite statements into more convenient forms without changing their meaning.

## How It's Best Learned
Verify each equivalence via truth table first, then learn to apply them symbolically. Focus on De Morgan's laws and the contrapositive equivalence, as these appear constantly in proof writing. Practice simplifying complex logical expressions step-by-step.

## Common Misconceptions
- Mistaking logical equivalence (always same truth value) with material biconditional (same truth value in a specific scenario).
- Incorrectly distributing negation: ¬(P ∧ Q) ≠ ¬P ∧ ¬Q.
- Assuming the conditional and its converse are equivalent.
