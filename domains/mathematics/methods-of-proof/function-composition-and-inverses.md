---
id: function-composition-and-inverses
title: Function Composition and Inverse Functions
domain: mathematics
course: methods-of-proof
prerequisites:
- id: injective-surjective-bijective-functions
  type: hard
- id: function-types-and-bijections
  type: soft
builds-toward:
- cardinality-and-countability-methods-of-proof
tags:
- functions
- composition
- inverses
stage: formal-systems
status: validated
---
# Function Composition and Inverse Functions

## Core Idea
Function composition (f ∘ g)(x) = f(g(x)) combines functions sequentially. A function has an inverse if and only if it is a bijection: f^{−1}(f(x)) = x and f(f^{−1}(y)) = y for all x, y. Composition and inverses are essential operations used throughout mathematics and critical for proofs about cardinality.

## Questions

```yaml
- question: "Consider f: ℝ → ℝ defined by f(x) = x². Does f have an inverse function? Why or why not?"
  type: multiple-choice
  options:
    - "Yes — every function defined on ℝ has an inverse"
    - "Yes — f is surjective onto the non-negative reals, so an inverse exists"
    - "No — f is not injective, since f(2) = f(−2) = 4, so no unique reversal is possible"
    - "No — f is not surjective onto all of ℝ, and surjectivity is the only condition needed for an inverse"
  answer: 2
  explanation: "A function has an inverse if and only if it is a bijection — both injective AND surjective. Here, f fails injectivity: two distinct inputs (2 and −2) map to the same output (4), so there is no way to define f⁻¹(4) unambiguously. Option D is wrong because both conditions are required: surjectivity ensures f⁻¹ is total (defined everywhere on the codomain), and injectivity ensures it is well-defined (no ambiguity). Failing either one prevents an inverse."

- question: "If g: A → B and f: B → C, what are the domain and codomain of the composition f ∘ g?"
  type: multiple-choice
  options:
    - "B → B, since both functions pass through B"
    - "A → B, inheriting g's domain and codomain"
    - "A → C, using g's domain and f's codomain"
    - "B → C, inheriting f's domain and codomain"
  answer: 2
  explanation: "Composition f ∘ g means 'first apply g, then apply f to the result.' g takes inputs from A and produces outputs in B; f then takes those B values and produces outputs in C. The overall function therefore maps from g's domain (A) to f's codomain (C): f ∘ g: A → C. The intermediate set B is consumed internally — it does not appear in the type of the composite function. This is why the output type of g must match the input type of f for composition to be well-defined."

- question: "Function composition is associative: for functions f, g, h with compatible types, (f ∘ g) ∘ h = f ∘ (g ∘ h)."
  type: true-false
  answer: true
  explanation: "True. Associativity means the parentheses don't matter when chaining three or more functions — you always get 'apply h first, then g, then f.' This can be verified directly: ((f ∘ g) ∘ h)(x) = (f ∘ g)(h(x)) = f(g(h(x))), and (f ∘ (g ∘ h))(x) = f((g ∘ h)(x)) = f(g(h(x))). The same result. Associativity is an important algebraic property used throughout proofs, and it is one reason the collection of functions from a set to itself forms a monoid under composition."

- question: "If f: A → B is a bijection with inverse f⁻¹: B → A, then f ∘ f⁻¹ and f⁻¹ ∘ f are the same identity function."
  type: true-false
  answer: false
  explanation: "False — they are identity functions on different sets. f⁻¹ ∘ f = id_A (first apply f to get a B-element, then f⁻¹ to return to A), while f ∘ f⁻¹ = id_B (first apply f⁻¹ to get an A-element, then f to return to B). These are distinct functions with different domains (id_A: A → A vs. id_B: B → B). When A ≠ B, they cannot be the same function. This distinction matters in cardinality proofs, where both conditions together confirm a genuine bijection between A and B."

- question: "Why does a function need to be both injective AND surjective to have an inverse? What goes wrong if only one condition holds?"
  type: short-answer
  answer: "Injectivity ensures the inverse is well-defined: if two inputs map to the same output (f(x) = f(y) with x ≠ y), then f⁻¹ cannot map that output back to a unique input — there is ambiguity about whether f⁻¹ should return x or y. Surjectivity ensures the inverse is total: if some element y in the codomain has no preimage, then f⁻¹(y) would be undefined, so f⁻¹ wouldn't be a function at all. Both conditions together guarantee that f pairs every input with a distinct output, with every output covered — exactly what is needed to reverse the mapping unambiguously."
  explanation: "The two conditions address two distinct failure modes of reversal. An injective-but-not-surjective function has a well-defined but partial inverse (undefined on elements with no preimage). A surjective-but-not-injective function has a total but multi-valued 'inverse' (relations, not functions). Only a bijection avoids both problems. This is why bijections are the correct notion of 'same size' for sets: the existence of a bijection guarantees a perfect, reversible pairing."
```

## Explainer

**Function composition** is the operation of chaining two functions: (f ∘ g)(x) = f(g(x)) means "first apply g, then apply f to the result." Think of a factory assembly line: g processes raw input into an intermediate product, and f processes that intermediate product into the final output. The order matters — f ∘ g and g ∘ f are generally different, just as applying heat then pressure gives a different result than pressure then heat. In composition, the output type of g must match the input type of f: if g: A → B and f: B → C, then f ∘ g: A → C is well-defined.

Composition is associative: (f ∘ g) ∘ h = f ∘ (g ∘ h). This means the parentheses don't matter when chaining three or more functions — a useful fact in proofs. There is also an identity function id_A(x) = x for any set A, which acts as a neutral element: f ∘ id = f and id ∘ f = f. Together, associativity and identity make the collection of functions from a set to itself into a **monoid** under composition.

The connection to your prerequisite on **injections, surjections, and bijections** is direct: a function f: A → B has an inverse f^{-1}: B → A satisfying f^{-1} ∘ f = id_A and f ∘ f^{-1} = id_B if and only if f is a bijection. The intuition is two-sided. Injectivity is needed because if f(x) = f(y) for x ≠ y, then f^{-1} cannot map that output back to a unique input — there would be ambiguity. Surjectivity is needed because if some y ∈ B has no preimage, then f^{-1}(y) would be undefined. A bijection avoids both problems: every input maps to a distinct output, and every output has exactly one input.

Inverses are heavily used in cardinality arguments. To show two sets A and B have the same cardinality, you exhibit a bijection f: A → B; the existence of f^{-1}: B → A then follows for free. The compositions f^{-1} ∘ f = id_A and f ∘ f^{-1} = id_B are precisely the conditions that say "f pairs every element of A with exactly one element of B, with no elements of B left over." This is why bijections are the correct notion of "same size" for infinite sets, and why composition is the language in which these size comparisons are expressed.
