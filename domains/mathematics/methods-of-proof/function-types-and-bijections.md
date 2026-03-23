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
status: validated
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

## Questions

```yaml
- question: "Consider the function f: ℝ → ℝ defined by f(x) = x². Which statement is correct?"
  type: multiple-choice
  options:
    - "f is injective but not surjective, because distinct positive inputs give distinct outputs"
    - "f is surjective but not injective, because every non-negative real number is an output"
    - "f is neither injective nor surjective"
    - "f is bijective, because every input has exactly one output"
  answer: 2
  explanation: "f fails injectivity: f(2) = f(−2) = 4, so two different inputs give the same output. f fails surjectivity: no real number maps to −1 (no x satisfies x² = −1), so negative numbers are not in the image. Option A is wrong because f(2) = f(−2). Option B confuses the image (non-negative reals) with the codomain (all reals). Option D confuses 'each input has one output' (the definition of being a function at all) with bijectivity."

- question: "Which modification would turn f(x) = x² into a bijective function?"
  type: multiple-choice
  options:
    - "Restrict the domain to all integers"
    - "Restrict the domain to [0, ∞) and the codomain to [0, ∞)"
    - "Restrict only the codomain to [0, ∞), keeping the domain as ℝ"
    - "Restrict only the domain to [0, ∞), keeping the codomain as ℝ"
  answer: 1
  explanation: "Restricting domain to [0, ∞) makes f injective (non-negative inputs give distinct outputs). Restricting codomain to [0, ∞) makes f surjective (every non-negative number is now hit). Both restrictions together produce a bijection. Option C fails: restricting only the codomain to [0, ∞) fixes surjectivity but f(2)=f(−2) still breaks injectivity. Option D fails: restricting only the domain to [0, ∞) makes it injective but negative numbers remain in the codomain with no preimage, so it is not surjective. This illustrates why domain and codomain are both part of the function's definition."

- question: "A function can be injective without being surjective, and surjective without being injective — these are independent properties."
  type: true-false
  answer: true
  explanation: "Injectivity and surjectivity are genuinely independent. The function f(x) = eˣ from ℝ to ℝ is injective (distinct inputs give distinct outputs) but not surjective (negative numbers have no preimage). A constant function f(x) = 0 from ℝ to ℝ is surjective only if the codomain is {0}, but fails injectivity for any domain with more than one element. A bijection requires both properties simultaneously, and many functions have neither."

- question: "If a function f: A → B is injective, then every element of B must be the output of some element of A."
  type: true-false
  answer: false
  explanation: "This is the definition of surjectivity, not injectivity. Injectivity says: different inputs give different outputs (if f(x) = f(y) then x = y). It says nothing about whether every element of B is reached. A function can be injective while leaving many elements of B with no preimage — for instance, f: {1,2} → {1,2,3} defined by f(1)=1, f(2)=2 is injective but 3 ∈ B has no preimage. Confusing these two properties is one of the most common errors in beginning set theory."

- question: "Why do mathematicians define the cardinality of infinite sets using bijections rather than by direct counting?"
  type: short-answer
  answer: "Counting works for finite sets because we can match elements to natural numbers 1, 2, 3, ... and read off the size. But for infinite sets, there is no 'last number' to read off — direct counting never terminates. A bijection provides a size-comparison without requiring a count: if a bijection f: A → B exists, then A and B are matched element-for-element with nothing left over on either side, so they have the same cardinality. Crucially, this definition reveals that not all infinite sets are the same size — there is no bijection between ℕ and ℝ, so these infinite sets have different cardinalities."
  explanation: "The bijection-based definition of cardinality is one of Cantor's great insights. The natural numbers and the even numbers are both countably infinite (there is a bijection n ↦ 2n), but the natural numbers and the real numbers are NOT in bijection — there are 'more' reals than naturals (Cantor's diagonal argument). This would be invisible to any approach based on naive counting."
```

## Explainer

You already know that sets are collections of elements with membership, union, intersection, and complement. A **function** f: A → B is a rule that assigns to each element of A (the **domain**) exactly one element of B (the **codomain**). The word "exactly one" is the defining constraint — every input gets an output, and no input gets two different outputs simultaneously. Functions are the basic machinery for relating sets to one another, and the three types — injective, surjective, bijective — classify what kinds of relationships they establish.

An **injective** (one-to-one) function never sends two different inputs to the same output: if f(x) = f(y), then x = y. Injectivity is a constraint on the domain side — it says no two elements of A "collide" under f. A simple test: the function f(x) = x² from ℝ to ℝ fails injectivity because f(2) = f(−2) = 4. But f(x) = x² from [0, ∞) to ℝ is injective, because restricting the domain eliminates the collision. This illustrates why domain matters: the same rule can be injective or not depending on where it is defined.

A **surjective** (onto) function has every element of B as an output: for every b ∈ B, there exists some a ∈ A with f(a) = b. Surjectivity is a constraint on the codomain side — it says f's image exhausts all of B. The function f(x) = x² from ℝ to ℝ fails surjectivity because negative numbers have no preimage. But f(x) = x² from ℝ to [0, ∞) is surjective, because the codomain has been trimmed to match the image. Again, the codomain is part of the function's definition, not an afterthought.

A **bijective** function is both injective and surjective: every element of B is hit exactly once. Bijections establish a **perfect pairing** between A and B — they are the set-theoretic notion of "A and B have the same size." This is the foundation of cardinality: two sets are said to have the same cardinality if a bijection exists between them. This definition works for infinite sets too: the natural numbers and the even numbers have the same cardinality because n ↦ 2n is a bijection, even though the even numbers seem "smaller." Bijections are also exactly the functions that have inverses — if f: A → B is bijective, then f⁻¹: B → A exists and is itself a bijection.
