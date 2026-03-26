---
id: group-definition-and-examples
title: Group Definition and Examples
domain: mathematics
course: abstract-algebra
prerequisites:
- id: binary-operations-and-algebraic-structures
  type: hard
builds-toward:
- basic-group-properties
- permutation-groups
- ring-definition-and-examples
tags:
- groups
- definitions
- examples
stage: advanced
status: validated
---

# Group Definition and Examples

## Core Idea
A group is a set G with a binary operation satisfying closure, associativity, identity, and inverse axioms. Examples include integers under addition, nonzero reals under multiplication, and permutations under composition. Groups provide unified language for studying symmetry.

## How It's Best Learned
Start with the four group axioms and verify them for small examples like Z/nZ and U(n). Practice checking whether given sets with operations form groups.

## Common Misconceptions
- Assuming all groups are abelian; symmetric groups S_n are non-abelian for n ≥ 3.
- Confusing identity and inverse elements; they are distinct in general.

## Questions

```yaml
- question: "Which of the following is NOT a group under the given operation?"
  type: multiple-choice
  options: ["(Z, +): integers under addition", "(R\\{0}, ×): nonzero reals under multiplication", "(Z, ×): integers under multiplication", "(Z/7Z, +): integers mod 7 under addition"]
  answer: 2
  explanation: "Integers under multiplication fail the inverse axiom: the element 2 has no multiplicative inverse in Z (1/2 is not an integer). The other three sets satisfy all four group axioms: closure, associativity, identity, and inverses."

- question: "Nearly every group is commutative — that is, a * b = b * a for most elements a and b."
  type: true-false
  answer: false
  explanation: "Groups need not be commutative. The symmetric group S_3 (permutations of 3 elements) is a standard counterexample: composing two permutations in different orders typically gives different results. Groups where commutativity holds are called abelian; non-abelian groups are common and important."

- question: "In the group (Z/4Z, +) — integers mod 4 under addition — what is the inverse of the element 3?"
  type: short-answer
  answer: "1, because 3 + 1 = 4 ≡ 0 (mod 4), the identity element."
  explanation: "The inverse of an element a is whatever element b satisfies a + b = e, where e is the identity. Here e = 0, and 3 + 1 = 4 = 0 mod 4, so the inverse of 3 is 1. This illustrates that the inverse is not always the additive negative in the usual integer sense."
```

## Explainer

You have already worked with binary operations — ways of combining two elements of a set to get a third. A group is what happens when a binary operation behaves especially well: it satisfies four axioms that together guarantee the operation has enough structure to do meaningful algebra. The four axioms are closure (the result stays in the set), associativity (grouping does not matter), the existence of an identity element (one element that leaves everything unchanged), and the existence of inverses (every element has a partner that "undoes" it).

The integers under addition are the prototypical group. Closure: adding two integers always gives an integer. Associativity: (a + b) + c = a + (b + c) always. Identity: 0, because a + 0 = a. Inverses: for any integer a, its inverse is −a, because a + (−a) = 0. Every axiom is obviously satisfied, which is why (Z, +) appears in almost every introduction to group theory.

Checking whether something is NOT a group is equally instructive. The integers under multiplication (Z, ×) fail at inverses: the integer 2 would need an inverse 1/2, but 1/2 is not an integer. Removing that failure — by restricting to nonzero rationals, or nonzero reals — produces a group. The point is that each axiom is a genuine constraint, and removing any one of them gives you a weaker structure (a monoid without inverses, or a semigroup without identity).

The most important misconception to unlearn early is that all groups are commutative. The symmetric group S_n — the set of all permutations of n objects under composition — is the classic counterexample. For n ≥ 3, the order in which you apply two permutations changes the result, so S_3 is non-abelian. Non-abelian groups are not pathological exceptions; they describe the symmetry of most geometric objects and underlie much of modern physics.

Groups provide a unified language for talking about symmetry in wildly different contexts: rotations and reflections of a polygon, shuffles of a deck of cards, solutions to a polynomial equation, transformations of a crystal lattice. Recognizing that all of these share the same four axioms is what makes abstract algebra powerful — you prove a theorem once for any group, and it instantly applies everywhere.
