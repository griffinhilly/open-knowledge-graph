---
id: uniqueness-proofs
title: Uniqueness Proofs
domain: mathematics
course: methods-of-proof
prerequisites:
- id: existence-proofs
  type: hard
builds-toward:
- injective-surjective-bijective
tags:
- uniqueness
- existence-and-uniqueness
- proof-technique
stage: formal-systems
status: validated
---

# Uniqueness Proofs

## Core Idea
A uniqueness proof shows that if an object satisfying some property exists, it is the only one. The standard technique is to assume two objects a and b both satisfy the property and then prove a = b. Uniqueness proofs commonly appear after existence proofs (together they establish ∃!x P(x), 'there exists a unique x') and are ubiquitous in algebra and analysis — for example, unique inverses, unique limits, or unique prime factorizations.

## How It's Best Learned
Practice with: uniqueness of additive identity in the integers, uniqueness of prime factorization (at least the uniqueness part). Stress the structure: assume x and y both satisfy P, and derive x = y.

## Common Misconceptions
- Proving existence and neglecting the uniqueness argument entirely when ∃! is required.
- Assuming uniqueness follows from existence in all cases — it does not.
- Making circular arguments by simply restating that only one solution is possible.

## Explainer

From your work with existence proofs, you know how to show that an object satisfying some property exists — either constructively (exhibit it explicitly) or non-constructively (use contradiction or a counting argument). Uniqueness is the complementary task: showing that at most one such object can exist. Together, an existence proof and a uniqueness proof establish **∃!x P(x)** — "there exists exactly one x with property P" — which appears in foundational theorems throughout mathematics: unique additive identities in groups, unique limits of sequences, unique prime factorizations, unique solutions to linear systems with full rank.

The canonical uniqueness proof has a fixed structure. Suppose a and b both satisfy property P. Then prove a = b. The key resource is that you have *two* objects, both satisfying P, and you can use both conditions simultaneously as hypotheses. For example, to prove the additive identity in any group is unique: let e and e' both be additive identities. Since e is an identity, e + e' = e'. Since e' is an identity, e + e' = e. Therefore e = e'. Both hypotheses were used — one to evaluate e + e' as e', the other to evaluate the same expression as e — and equality follows.

Why is "assume two objects, derive equality" sufficient rather than assuming three or more? If a = b whenever any two objects both satisfy P, then for any third object c also satisfying P, applying the same argument to (a, c) gives a = c, and to (b, c) gives b = c. So all three are equal. Proving pairwise equality for any two objects satisfying P captures the general case efficiently. This is why the proof template is stated with exactly two objects — it's the minimal, general structure.

Recognizing when uniqueness requires a genuine argument — versus when it is trivial or follows from structure — is part of mathematical maturity. The unique prime factorization of integers (the fundamental theorem of arithmetic) requires Euclid's lemma: if a prime divides a product ab, it divides a or b. Uniqueness of limits in a metric space requires the Hausdorff property (distinct points have disjoint neighborhoods). Uniqueness of solutions to ODEs requires a Lipschitz condition on the vector field. In each case, the argument type is the same — assume two solutions exist, derive they must be equal — but the tools used depend on the specific mathematical context. Planning a uniqueness proof means identifying which property of the system will force a = b.
