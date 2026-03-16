---
id: function-composition-and-inverses
title: Function Composition and Inverse Functions
domain: mathematics
course: methods-of-proof
prerequisites:
- id: injective-surjective-bijective-functions
  type: hard
builds-toward:
- cardinality-countability-infinity
tags:
- functions
- composition
- inverses
stage: formal-systems
status: draft
---

# Function Composition and Inverse Functions

## Core Idea
Function composition (f ∘ g)(x) = f(g(x)) combines functions sequentially. A function has an inverse if and only if it is a bijection: f^{−1}(f(x)) = x and f(f^{−1}(y)) = y for all x, y. Composition and inverses are essential operations used throughout mathematics and critical for proofs about cardinality.

## Explainer

**Function composition** is the operation of chaining two functions: (f ∘ g)(x) = f(g(x)) means "first apply g, then apply f to the result." Think of a factory assembly line: g processes raw input into an intermediate product, and f processes that intermediate product into the final output. The order matters — f ∘ g and g ∘ f are generally different, just as applying heat then pressure gives a different result than pressure then heat. In composition, the output type of g must match the input type of f: if g: A → B and f: B → C, then f ∘ g: A → C is well-defined.

Composition is associative: (f ∘ g) ∘ h = f ∘ (g ∘ h). This means the parentheses don't matter when chaining three or more functions — a useful fact in proofs. There is also an identity function id_A(x) = x for any set A, which acts as a neutral element: f ∘ id = f and id ∘ f = f. Together, associativity and identity make the collection of functions from a set to itself into a **monoid** under composition.

The connection to your prerequisite on **injections, surjections, and bijections** is direct: a function f: A → B has an inverse f^{-1}: B → A satisfying f^{-1} ∘ f = id_A and f ∘ f^{-1} = id_B if and only if f is a bijection. The intuition is two-sided. Injectivity is needed because if f(x) = f(y) for x ≠ y, then f^{-1} cannot map that output back to a unique input — there would be ambiguity. Surjectivity is needed because if some y ∈ B has no preimage, then f^{-1}(y) would be undefined. A bijection avoids both problems: every input maps to a distinct output, and every output has exactly one input.

Inverses are heavily used in cardinality arguments. To show two sets A and B have the same cardinality, you exhibit a bijection f: A → B; the existence of f^{-1}: B → A then follows for free. The compositions f^{-1} ∘ f = id_A and f ∘ f^{-1} = id_B are precisely the conditions that say "f pairs every element of A with exactly one element of B, with no elements of B left over." This is why bijections are the correct notion of "same size" for infinite sets, and why composition is the language in which these size comparisons are expressed.
