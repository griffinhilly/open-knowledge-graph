---
id: truth-values-and-statements
title: Truth Values and Statements
domain: mathematics
course: methods-of-proof
prerequisites: []
builds-toward:
- logical-connectives-and-operators
- truth-tables-and-evaluation
- conditional-implication-statements
tags:
- logic
- statements
- foundations
stage: formal-systems
status: draft
---

# Truth Values and Statements

## Core Idea
A statement is a declarative sentence that is either true or false, but not both. In mathematics, we work with statements that can be analyzed for their truth value. Understanding what counts as a mathematical statement is foundational to all proof work.

## How It's Best Learned
Start with simple examples (e.g., '2 + 2 = 4' is true, '5 > 10' is false) and non-examples (e.g., 'What time is it?' is not a statement). Practice classifying sentences as statements or non-statements.

## Common Misconceptions
- Assuming questions or commands are statements.
- Thinking that statements must be true (false statements are still statements).
- Confusing the meaning of a statement with its truth value.

## Explainer

Mathematics runs on claims that are either true or false. Before you can reason about numbers, sets, functions, or proofs, you need a precise notion of what kinds of sentences can even have a truth value. A **statement** (also called a **proposition**) is a declarative sentence that is, in principle, either true or false — no other possibility exists. "Seven is prime" is a statement; it is true. "The square root of two is rational" is a statement; it is false. "What is the value of x?" is a question, not a statement — it cannot be true or false.

This binary structure — true or false, and nothing else — is called the **law of the excluded middle**, a foundational assumption of classical logic. It is what makes proof by contradiction possible: if you assume something is false and derive a contradiction, you conclude it must be true, because there is no third option. The assumption is not trivially obvious — constructive mathematicians sometimes question it for certain kinds of statements about infinite objects. But in standard mathematics, every well-formed statement has exactly one **truth value**.

Not every sentence in ordinary language qualifies. Commands ("Compute the integral") and questions ("Is 17 prime?") have no truth value. Open sentences like "x + 3 = 7" depend on the variable x — they become true or false only once x is specified or quantified. These are called **predicates**, and they become statements when the variable is either substituted with a specific value ("5 + 3 = 7" is false) or bound by a quantifier ("For all x, x + 3 = 7" is a statement — a false one). Recognizing this distinction between statements and predicates is the first step toward working with quantifiers, which will drive nearly all of proof logic.

Being careful about what counts as a statement pays off throughout all proof work. A proof is a sequence of statements, each either a hypothesis, a previously established fact, or a logical consequence of earlier lines — every line must be a genuine statement with a definite truth value. A false statement is still a statement; what matters is not truth but the capacity to be true or false. From these simple building blocks — declarative sentences with binary truth values — all of mathematical logic is constructed: connectives combine statements, quantifiers range predicates over domains, and proofs chain statements together in truth-preserving steps.
