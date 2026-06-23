---
id: functions-and-function-properties
title: Functions as Sets and Their Characteristics
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: binary-relations-definition-and-properties
  type: hard
- id: ordered-pairs-and-tuples
  type: hard
builds-toward:
- injections-surjections-and-inverse-functions
- composition-of-functions-sets
tags:
- functions
- mappings
- domain-codomain
stage: formal-systems
status: validated
---

# Functions as Sets and Their Characteristics

## Core Idea
A function f: A → B is a relation where each a ∈ A pairs with exactly one b ∈ B. Functions are entirely definable as subsets of A × B, making them fully set-theoretic objects. The domain A and codomain B are essential parts of a function's definition.

## Questions

```yaml
- question: "Let A = {1, 2} and B = {a, b, c}. Which of the following subsets of A × B is NOT a valid function from A to B?"
  type: multiple-choice
  options:
    - "{(1, a), (2, b)}"
    - "{(1, a), (1, b), (2, c)}"
    - "{(1, c), (2, c)}"
    - "{(1, a), (2, a)}"
  answer: 1
  explanation: "A function requires each element of the domain to map to exactly one element of the codomain. In option B, element 1 is paired with both a and b — violating the 'exactly one' requirement. Options A, C, and D each assign every element of A to a single element of B, so all three are valid functions (even though C and D are not injective)."

- question: "Two functions f and g from A to B are the same function if and only if they have the same domain A and the same codomain B."
  type: true-false
  answer: false
  explanation: "Domain and codomain only specify the type signature — f: A → B and g: A → B. Two functions with the same domain and codomain can differ in which element of B each a ∈ A maps to. Functions are equal only if f(a) = g(a) for every a ∈ A, meaning their underlying subsets of A × B are identical."

- question: "What is the difference between the codomain and the image of a function f: A → B?"
  type: short-answer
  answer: "The codomain B is the declared target set — all allowable outputs. The image is {f(a) | a ∈ A}, the set of outputs actually achieved. The image is always a subset of the codomain, but they are equal only when f is surjective."
  explanation: "Conflating codomain and image is a common error. For example, f: ℝ → ℝ defined by f(x) = x² has codomain ℝ but image [0, ∞) — negative numbers are in the codomain but never output. The distinction matters for defining surjectivity and for inverses."
```

## Explainer

You have seen functions in algebra — f(x) = 2x + 1, for example — but set theory demands a more precise account. What *is* a function, stripped of notation and intuition? The answer is: a function is a set of ordered pairs satisfying a particular constraint.

Given sets A and B, a function f: A → B is a subset of the Cartesian product A × B with the property that every element a ∈ A appears as the first component of exactly one pair in f. The pair (a, b) ∈ f means f(a) = b. This is not a new concept but a more explicit one: the "rule" of a function is nothing more than the set of all input-output pairs. This set-theoretic view makes functions first-class mathematical objects that can themselves be elements of sets, compared for equality, and reasoned about with the same tools used for any set.

The "exactly one b for each a" condition has two parts. First, every element of A must appear — no element of the domain is left unmapped. Second, no element of A can appear twice with different outputs — the mapping must be *deterministic*. If either condition fails, the relation is not a function. A relation where some inputs map to multiple outputs is called a multi-valued relation; a relation where some inputs have no output is called a partial function. Both are useful concepts, but neither is a function in the full sense.

The codomain B is a declared part of the function's identity. Two functions can have the same domain, the same input-output behavior, but different codomains — and they are formally different functions. This matters in practice: f: ℤ → ℤ defined by f(n) = n² and g: ℤ → ℕ defined by g(n) = n² have the same values everywhere but different codomains, which affects whether they can be surjective. The *image* of f — the set {f(a) | a ∈ A} — is a subset of the codomain that records which outputs are actually achieved. When the image equals the codomain, the function is surjective, a property you will formalize in the next topic.

Understanding functions as sets lets you apply all of set theory to them. Two functions are equal precisely when they are equal as sets — same domain, same codomain, same pairs. This foundation also prepares you for function composition, which you will see is simply a set-theoretic operation on relations, and for comparing the sizes of infinite sets via injections and surjections.
