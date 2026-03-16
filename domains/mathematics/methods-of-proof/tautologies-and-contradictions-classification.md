---
id: tautologies-and-contradictions-classification
title: Tautologies and Contradictions
domain: mathematics
course: methods-of-proof
prerequisites:
- id: truth-tables-and-evaluation
  type: hard
builds-toward:
- rules-of-logical-inference
- proving-by-contradiction
tags:
- logic
- tautology
- contradiction
- contingency
stage: formal-systems
status: draft
---

# Tautologies and Contradictions

## Core Idea
A tautology is a statement that is always true, regardless of the truth values of its components. A contradiction is always false. A contingency is sometimes true and sometimes false. Tautologies are the foundation of valid logical inferences.

## How It's Best Learned
Construct truth tables for various formulas and classify the results. Identify tautologies by recognizing patterns like p ∨ ¬p.

## Common Misconceptions
- Thinking a statement is a tautology if it is true in some cases.
- Confusing tautologies with true statements (tautologies are always true, but true statements might not be).

## Explainer

When you build a truth table for a compound statement, the rightmost column gives you a verdict for each possible combination of truth values. Three outcomes are possible: the column is all T's, all F's, or a mix. A **tautology** produces all T's — it is true no matter what. A **contradiction** produces all F's — it is false no matter what. A **contingency** produces a mix — its truth depends on the values of its components. These three categories are exhaustive and mutually exclusive.

The simplest tautology is P ∨ ¬P — "P or not P." This is true regardless of whether P is true or false, because exactly one of P and ¬P is always true. Similarly, the simplest contradiction is P ∧ ¬P — "P and not P" — which is always false because P and ¬P can never both be true simultaneously. These feel trivial, but they are the atomic units of a much larger system: any logical equivalence P ≡ Q can be verified by checking that P ↔ Q is a tautology, and any valid argument can be checked by confirming its logical form is a tautology.

**Tautologies are the currency of logical inference.** When a logician writes an inference rule — "from P and P → Q, conclude Q" — what they are saying is that (P ∧ (P → Q)) → Q is a tautology. The rule is valid precisely because the corresponding conditional is always true, regardless of what P and Q happen to be. This is why your next topics, rules of logical inference and proof by contradiction, build directly on tautologies: a proof step is valid exactly when the underlying logical form is a tautology.

Contradictions play an equally important role in proof by contradiction. That proof strategy works by assuming ¬P (the negation of what you want to prove) and then deriving a contradiction — a statement of the form Q ∧ ¬Q. Since a contradiction is always false, and you derived it from ¬P by valid steps, the assumption ¬P must be false. Therefore P is true. The power of contradiction-detection is that any statement of the form (something) ∧ ¬(something) immediately signals logical impossibility, giving you a route back to the original claim. Recognizing contradictions — especially disguised ones — is one of the key skills that separates routine calculation from genuine mathematical reasoning.
