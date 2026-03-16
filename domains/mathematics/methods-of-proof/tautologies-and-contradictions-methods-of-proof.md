---
id: tautologies-and-contradictions-methods-of-proof
title: Tautologies and Contradictions
domain: mathematics
course: methods-of-proof
prerequisites:
- id: truth-tables
  type: hard
builds-toward:
- proof-by-contradiction
tags:
- tautology
- contradiction
- validity
stage: formal-systems
status: draft
---

# Tautologies and Contradictions

## Core Idea
A tautology is always true regardless of truth assignments; a contradiction is always false. Recognizing these is crucial: if assuming negation of a statement yields a contradiction, the statement must be true.

## How It's Best Learned
Compare tautologies (p ∨ ¬p) with contingencies (p ∧ ¬q) that can be either true or false.

## Common Misconceptions
- Treating a frequently-true statement as a tautology when it could be false in some cases.
- Confusing contradictions with statements that are merely false in specific cases.

## Explainer

Every logical statement lives somewhere on a spectrum between always-true and always-false. From your truth table work, you know that a compound statement can be true under some truth assignments and false under others — these are called **contingencies** and they're the typical case. But at the extremes are two special cases: **tautologies** are true under every possible truth assignment, and **contradictions** are false under every possible truth assignment. These are not just statements that happen to be true or false — they're true or false as a matter of logical structure alone, independent of any facts about the world.

The canonical tautology is p ∨ ¬p: "p or not p." No matter whether p is true or false, exactly one of the disjuncts is true, so the whole statement is always true. It captures the law of excluded middle. The canonical contradiction is p ∧ ¬p: "p and not p." This is always false because no statement can simultaneously be true and false. Notice these two are negations of each other: ¬(p ∧ ¬p) ≡ p ∨ ¬p, and a tautology's negation is always a contradiction.

The proof-theoretic importance of contradictions is enormous. **Proof by contradiction** works as follows: to prove a statement Q is true, assume ¬Q and derive a contradiction — a statement of the form (R ∧ ¬R). Once you've derived a logical impossibility, the assumption ¬Q must be false, which means Q must be true. The classical example is the irrationality of √2: assume √2 = p/q in lowest terms, derive that both p and q must be even (contradicting "lowest terms"), and conclude the assumption was false. The power of this method depends entirely on understanding that a contradiction is not just a "false thing" but a statement that cannot possibly be true under any assignment — so reaching it proves the starting assumption was impossible.

Tautologies play a complementary role as rewriting tools. In formal logic and computer science, rules of inference are tautologies: modus ponens says that ((p → q) ∧ p) → q is always true. When you apply a proof rule, you're instantiating a tautology. Recognizing a tautology tells you that an argument form is universally valid — it works for any specific statements you plug in. Recognizing a contradiction tells you that a set of assumptions is inconsistent — they can never all be simultaneously true — which is why reaching one during a proof demolishes the premises that led there.
