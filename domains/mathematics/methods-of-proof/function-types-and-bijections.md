---
id: function-types-and-bijections
title: Function Types and Bijections
domain: mathematics
course: methods-of-proof
prerequisites:
- id: set-operations-and-notation
  type: hard
tags:
- functions
- injective
- surjective
- bijective
stage: formal-systems
status: draft
---

# Function Types and Bijections

## Core Idea
A function f: A → B assigns each element of A to exactly one element of B. A function is injective (one-to-one) if different inputs give different outputs, surjective (onto) if every element of B is an output, and bijective if both properties hold. Bijections are structure-preserving maps that establish set equivalence and are central to counting and cardinality arguments.

## How It's Best Learned
Verify these properties for specific functions using definitions. Draw diagrams showing injective, surjective, and bijective mappings.

## Common Misconceptions
- Confusing injective with surjective (they are independent properties).
- Thinking a function must be bijective (it need not be).
- Assuming a function is determined only by its rule (domain and codomain matter).

## Explainer

You already know that sets are collections of elements with membership, union, intersection, and complement. A **function** f: A → B is a rule that assigns to each element of A (the **domain**) exactly one element of B (the **codomain**). The word "exactly one" is the defining constraint — every input gets an output, and no input gets two different outputs simultaneously. Functions are the basic machinery for relating sets to one another, and the three types — injective, surjective, bijective — classify what kinds of relationships they establish.

An **injective** (one-to-one) function never sends two different inputs to the same output: if f(x) = f(y), then x = y. Injectivity is a constraint on the domain side — it says no two elements of A "collide" under f. A simple test: the function f(x) = x² from ℝ to ℝ fails injectivity because f(2) = f(−2) = 4. But f(x) = x² from [0, ∞) to ℝ is injective, because restricting the domain eliminates the collision. This illustrates why domain matters: the same rule can be injective or not depending on where it is defined.

A **surjective** (onto) function has every element of B as an output: for every b ∈ B, there exists some a ∈ A with f(a) = b. Surjectivity is a constraint on the codomain side — it says f's image exhausts all of B. The function f(x) = x² from ℝ to ℝ fails surjectivity because negative numbers have no preimage. But f(x) = x² from ℝ to [0, ∞) is surjective, because the codomain has been trimmed to match the image. Again, the codomain is part of the function's definition, not an afterthought.

A **bijective** function is both injective and surjective: every element of B is hit exactly once. Bijections establish a **perfect pairing** between A and B — they are the set-theoretic notion of "A and B have the same size." This is the foundation of cardinality: two sets are said to have the same cardinality if a bijection exists between them. This definition works for infinite sets too: the natural numbers and the even numbers have the same cardinality because n ↦ 2n is a bijection, even though the even numbers seem "smaller." Bijections are also exactly the functions that have inverses — if f: A → B is bijective, then f⁻¹: B → A exists and is itself a bijection.
