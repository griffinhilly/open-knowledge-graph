---
id: logical-equivalence
title: Logical Equivalence
domain: mathematics
course: methods-of-proof
prerequisites:
- id: truth-tables-and-evaluation
  type: hard
builds-toward:
- converse-inverse-contrapositive
- negating-quantifiers
tags:
- logic
- equivalence
- tautology
stage: formal-systems
status: draft
---

# Logical Equivalence

## Core Idea
Two statements are logically equivalent if they have the same truth value in every possible scenario. Equivalences are identified using truth tables or known logical rules (like De Morgan's laws). Recognizing equivalences allows us to rewrite statements in more useful forms.

## How It's Best Learned
Use truth tables to verify equivalence. Memorize common equivalences (De Morgan's laws, double negation) and practice rewriting statements.

## Common Misconceptions
- Confusing logical equivalence with semantic similarity.
- Thinking two statements are equivalent if they are true in one case.
- Forgetting that equivalence must hold in ALL cases.

## Explainer

From truth tables, you know how to evaluate the truth value of a compound statement given the truth values of its atomic parts. **Logical equivalence** takes this one step further: two statements P and Q are logically equivalent, written P ≡ Q, if they produce exactly the same truth value in every possible row of their joint truth table. They don't have to look alike — they just have to behave identically across all inputs. Think of it like two different programs that always produce the same output on every input: same behavior, different code.

The most important logical equivalences to internalize are **De Morgan's laws**: ¬(P ∧ Q) ≡ (¬P ∨ ¬Q) and ¬(P ∨ Q) ≡ (¬P ∧ ¬Q). In plain language: "not (P and Q)" is the same as "not-P or not-Q," and "not (P or Q)" is the same as "not-P and not-Q." A helpful analogy: "It's not the case that it's raining AND cold" is equivalent to "it's not raining OR it's not cold" — if the conjunction fails, at least one conjunct must be false. You can verify these with a truth table, but once you've checked them once, you can use them freely as rewriting rules.

A second critical equivalence is the **contrapositive**: (P → Q) ≡ (¬Q → ¬P). An implication and its contrapositive are logically the same statement. "If it rains, the ground gets wet" says exactly the same thing as "if the ground is not wet, it did not rain." This equivalence is practically invaluable for proofs: when proving "if P then Q" is difficult directly, proving "if not-Q then not-P" is often easier, and the two proofs are logically interchangeable.

Logical equivalence is the engine behind **proof by transformation**: instead of building a proof from scratch, you rewrite statements into equivalent forms until you reach something obviously true or a known result. Each rewriting step must preserve truth across all cases. This is why the distinction matters so much — you cannot substitute a merely true statement for another merely true statement; you need them to be equivalent (same truth behavior everywhere). Mastering a toolkit of equivalences (De Morgan, contrapositive, double negation, distributive laws) lets you reshape logical expressions the same way algebraic identities let you reshape equations.
