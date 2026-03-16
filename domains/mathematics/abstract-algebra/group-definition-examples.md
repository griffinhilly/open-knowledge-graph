---
id: group-definition-examples
title: Group Definition and Examples
domain: mathematics
course: abstract-algebra
prerequisites:
- id: binary-operations-algebraic-structures
  type: hard
builds-toward:
- group-basic-properties
- permutation-groups
- ring-definition-examples
tags:
- groups
- closure
- associativity
- identity
- inverse
stage: advanced
status: draft
---

# Group Definition and Examples

## Core Idea
A group is a set G with a binary operation satisfying four axioms: closure, associativity, existence of an identity element, and existence of inverses for every element. Groups appear throughout mathematics and physics as the formalization of symmetry.

## Explainer

The concept of a group captures what it means for an operation to be "fully reversible and rearrangeable." You already know from binary operations that combining elements is not always well-behaved — the four group axioms pin down exactly the properties needed to do algebra reliably. **Closure** means the operation stays inside the set. **Associativity** means you can regroup computations: (a ∗ b) ∗ c = a ∗ (b ∗ c). The **identity element** is the "do nothing" element — it leaves everything unchanged. And **inverses** let you undo any move, so no element is a dead end.

Consider integer addition as your first example: you can add any two integers and stay in ℤ (closure); grouping doesn't change the result — (3 + 4) + 5 = 3 + (4 + 5) (associativity); 0 leaves everything unchanged (identity); and every n has −n (inverse). So (ℤ, +) is a group. Now contrast with integer multiplication: 2 has no multiplicative inverse inside ℤ (since 1/2 ∉ ℤ), so (ℤ, ×) is not a group. But (ℚ \ {0}, ×) is. Whether something forms a group depends on both the *set* and the *operation* together.

The power of the group definition is its breadth. The six rotations of an equilateral triangle form a group. The set of all permutations of {1, 2, 3} forms a group under composition. The nonzero real numbers form a group under multiplication. These look completely different, yet they all satisfy the same four axioms. A theorem proved for abstract groups — say, that the identity is unique, or that inverses are unique — automatically applies to all of these at once. This is the abstraction payoff: you prove something once and it lands everywhere.

When working with groups, always verify all four axioms explicitly until intuition develops. Closure is the one most often overlooked: even if the operation is familiar, the *set* might not be closed under it. The even integers under addition are closed; the odd integers are not (odd + odd = even). Groups build toward subgroups, homomorphisms, quotient groups, and ultimately to classifying all possible symmetric structures in mathematics — but the four axioms are the foundation everything rests on.
