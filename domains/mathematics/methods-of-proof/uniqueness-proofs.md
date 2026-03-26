---
id: uniqueness-proofs
title: Uniqueness Proofs
domain: mathematics
course: methods-of-proof
prerequisites:
- id: existence-proofs
  type: hard
- id: existence-and-uniqueness-proofs
  type: soft
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

## Questions

```yaml
- question: "You want to prove that the additive identity in a group is unique. You have already shown that 0 satisfies the identity property (0 + a = a for all a). What is the correct next step in a uniqueness proof?"
  type: multiple-choice
  options:
    - "Show by construction that no other element can satisfy the identity property"
    - "Assume there is a second element 0' that also satisfies the identity property, then derive 0 = 0'"
    - "Use induction to eliminate all candidate identity elements one by one"
    - "Argue that the construction of 0 was the only logically possible one, so uniqueness follows from existence"
  answer: 1
  explanation: "The canonical uniqueness proof template is: assume two objects a and b both satisfy the property P, then prove a = b. Here, you let 0' also be an additive identity. Since 0 is an identity: 0 + 0' = 0'. Since 0' is an identity: 0 + 0' = 0. Therefore 0 = 0'. Both hypotheses were used simultaneously — that is the structural signature of a correct uniqueness proof."

- question: "A student proves constructively that √2 exists as a real number and concludes: 'Since I've shown it exists, it must be unique — there's only one real square root of 2 equal to √2.' Is this reasoning valid?"
  type: multiple-choice
  options:
    - "Yes — existence and uniqueness are the same claim for irrational numbers"
    - "No — existence and uniqueness are separate claims; a separate argument must show no other value satisfies the same defining property"
    - "Yes — constructive existence proofs automatically establish uniqueness because the construction is specific"
    - "No — uniqueness proofs only apply to algebraic objects, not real numbers"
  answer: 1
  explanation: "Existence and uniqueness are logically independent claims. 'An x with property P exists' and 'at most one x with property P exists' must be argued separately. A constructive proof exhibits one object satisfying P but does nothing to rule out others. The uniqueness argument must go further: assume two objects both satisfy P, and derive they are equal. Conflating these two steps is the most common error when working with ∃!x P(x) claims."

- question: "In a uniqueness proof, you use both hypotheses simultaneously — the fact that a satisfies P and the fact that b satisfies P — to derive a = b."
  type: true-false
  answer: true
  explanation: "This simultaneous use of both conditions is the structural signature of a correct uniqueness proof. In the additive identity example: 'e is an identity' gives e + e' = e'; 'e' is an identity' gives e + e' = e. Both hypotheses are needed to conclude e = e'. If you only used one, you couldn't establish equality. This is also why the template is stated with exactly two objects — you need two to derive equality, and two is sufficient."

- question: "Proving that any two elements satisfying property P should be equal primarily establishes pairwise uniqueness — a separate argument is still needed to rule out three or more distinct elements most satisfying P."
  type: true-false
  answer: false
  explanation: "Pairwise equality is sufficient for full uniqueness. If a = b whenever any two objects both satisfy P, then for any third object c also satisfying P, applying the same argument to (a, c) gives a = c, and to (b, c) gives b = c. So all three collapse to the same value. The pairwise template captures the general case: you cannot have two distinct elements both satisfying P, let alone three, four, or any number."

- question: "Why is the proof template 'assume a and b both satisfy P, then prove a = b' sufficient to establish that at most one element satisfies P?"
  type: short-answer
  answer: "If any two elements satisfying P must be equal, then you cannot have two distinct elements satisfying P. For any further element c satisfying P, the same argument applied to (a, c) gives a = c, and to (b, c) gives b = c — so all elements satisfying P are identical. Pairwise equality is the minimal, general structure: proving it for any two objects covers all possible cases."
  explanation: "The elegance of the template is that 'at most two objects' is all you ever need to consider. The proof structure is minimal in the same way that proving a statement for arbitrary n is more general than listing cases — assuming two arbitrary objects satisfying P and showing they're equal captures the full content of uniqueness."
```

## Explainer

From your work with existence proofs, you know how to show that an object satisfying some property exists — either constructively (exhibit it explicitly) or non-constructively (use contradiction or a counting argument). Uniqueness is the complementary task: showing that at most one such object can exist. Together, an existence proof and a uniqueness proof establish **∃!x P(x)** — "there exists exactly one x with property P" — which appears in foundational theorems throughout mathematics: unique additive identities in groups, unique limits of sequences, unique prime factorizations, unique solutions to linear systems with full rank.

The canonical uniqueness proof has a fixed structure. Suppose a and b both satisfy property P. Then prove a = b. The key resource is that you have *two* objects, both satisfying P, and you can use both conditions simultaneously as hypotheses. For example, to prove the additive identity in any group is unique: let e and e' both be additive identities. Since e is an identity, e + e' = e'. Since e' is an identity, e + e' = e. Therefore e = e'. Both hypotheses were used — one to evaluate e + e' as e', the other to evaluate the same expression as e — and equality follows.

Why is "assume two objects, derive equality" sufficient rather than assuming three or more? If a = b whenever any two objects both satisfy P, then for any third object c also satisfying P, applying the same argument to (a, c) gives a = c, and to (b, c) gives b = c. So all three are equal. Proving pairwise equality for any two objects satisfying P captures the general case efficiently. This is why the proof template is stated with exactly two objects — it's the minimal, general structure.

Recognizing when uniqueness requires a genuine argument — versus when it is trivial or follows from structure — is part of mathematical maturity. The unique prime factorization of integers (the fundamental theorem of arithmetic) requires Euclid's lemma: if a prime divides a product ab, it divides a or b. Uniqueness of limits in a metric space requires the Hausdorff property (distinct points have disjoint neighborhoods). Uniqueness of solutions to ODEs requires a Lipschitz condition on the vector field. In each case, the argument type is the same — assume two solutions exist, derive they must be equal — but the tools used depend on the specific mathematical context. Planning a uniqueness proof means identifying which property of the system will force a = b.
