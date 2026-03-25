---
id: injective-surjective-bijective
title: Injective, Surjective, and Bijective Functions
domain: mathematics
course: methods-of-proof
prerequisites:
- id: equivalence-relations
  type: soft
- id: function-types-and-bijections
  type: soft
builds-toward:
- cardinality-and-countability
tags:
- functions
- injective
- surjective
stage: formal-systems
status: validated
---
# Injective, Surjective, and Bijective Functions

## Core Idea
A function f: A → B is injective (one-to-one) if distinct inputs give distinct outputs; surjective (onto) if every element of B is mapped to; bijective if both. Bijections establish correspondences and are essential for comparing cardinalities.

## Questions

```yaml
- question: "Consider f: ℝ → ℝ defined by f(x) = x². A student claims this function is surjective because 'every input produces an output.' What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "The student is correct — every real input does produce a real output, so the function is surjective"
    - "Surjectivity requires every element of the codomain to be hit by some input — but negative reals are never outputs of f(x) = x², so f is not surjective from ℝ to ℝ"
    - "The student's reasoning works for ℝ → ℝ but would fail for ℝ → [0, ∞)"
    - "The function is not surjective because it is also not injective"
  answer: 1
  explanation: "Surjectivity is a claim about the codomain, not about the domain. The codomain is ℝ (all reals), but f(x) = x² only produces non-negative outputs — no negative number is ever hit. A student who confuses 'every input has an output' (true of every function, by definition) with 'every output is hit by some input' (surjectivity) is conflating the definition of a function with the additional property of surjectivity. Note that f: ℝ → [0, ∞) defined by the same rule *is* surjective — the codomain is part of the function's specification."

- question: "Let f: ℕ → ℕ be defined by f(n) = 2n. Which properties does this function have?"
  type: multiple-choice
  options:
    - "Injective only — distinct inputs produce distinct outputs, but odd natural numbers are never hit"
    - "Surjective only — every element of ℕ is an even number times two"
    - "Bijective — every natural number is the image of exactly one natural number"
    - "Neither injective nor surjective"
  answer: 0
  explanation: "f(n) = 2n is injective: if 2n₁ = 2n₂ then n₁ = n₂, so no two distinct inputs share an output. But it is not surjective onto ℕ: the number 3 (or any odd number) is never an output of f. This is a classic illustration that injectivity and surjectivity are independent properties — a function can have one without the other. It also shows that the codomain matters: f: ℕ → {even natural numbers} defined by the same rule would be bijective."

- question: "A bijection f: A → B implies that the inverse function f⁻¹: B → A exists as a well-defined function."
  type: true-false
  answer: true
  explanation: "A function has a well-defined inverse exactly when it is bijective. Injectivity ensures that each output came from exactly one input (so the inverse rule 'go back to where you came from' is unambiguous). Surjectivity ensures that every element of B has a preimage at all (so the inverse is defined on all of B). A function that is injective but not surjective has a partial inverse; one that is surjective but not injective fails to have an inverse because some outputs came from multiple inputs."

- question: "Whether a function is surjective depends only on its rule of assignment and is unaffected by how the codomain is defined."
  type: true-false
  answer: false
  explanation: "Surjectivity is explicitly codomain-dependent. The same rule f(x) = x² defines a non-surjective function from ℝ to ℝ (negative reals are never hit) but a surjective function from ℝ to [0, ∞) (every non-negative real is hit). Changing only the codomain, without changing the rule, can turn a non-surjective function into a surjective one. This is why the codomain is treated as part of the function's definition, not just a background assumption."

- question: "Explain why bijections are the correct tool for comparing the sizes of infinite sets, and give an example illustrating the key idea."
  type: short-answer
  answer: "A bijection establishes a perfect one-to-one correspondence between two sets: every element of each set is matched with exactly one element of the other, with no leftovers on either side. Two sets have the same cardinality — the same 'size' in the most fundamental sense — if and only if a bijection exists between them. For finite sets this matches ordinary counting. For infinite sets it produces surprising results: the function f(n) = 2n is a bijection between ℕ and the even natural numbers, showing these sets have the same cardinality even though one is a proper subset of the other. This is what it means for infinite sets to have the same size."
  explanation: "The example of ℕ and the even numbers is the classic illustration of Cantor's insight that 'same size' for infinite sets cannot mean 'same number of elements' in the ordinary sense — it must mean 'there is a bijection.' This is why bijections, and not counting, are the fundamental tool in cardinality theory."
```

## Explainer

A function f: A → B assigns each element of A (the domain) exactly one element of B (the codomain). But the same definition allows very different behaviors: multiple inputs might map to the same output, or some outputs might never be hit at all. The properties of injectivity, surjectivity, and bijectivity classify functions by how thoroughly they respect the structure of their domain and codomain.

A function is **injective** (one-to-one) if no two distinct inputs produce the same output: if f(a₁) = f(a₂) then a₁ = a₂. Injectivity is a statement about the domain — the function doesn't "collapse" any distinct elements together. The contrapositive form is often used in proofs: to show injectivity, assume f(a₁) = f(a₂) and derive a₁ = a₂. For example, f(x) = 2x from ℝ to ℝ is injective: 2x₁ = 2x₂ immediately gives x₁ = x₂. The function f(x) = x² is not injective over ℝ because f(2) = f(−2) = 4.

A function is **surjective** (onto) if every element b ∈ B is the image of at least one element a ∈ A: for every b there exists a with f(a) = b. Surjectivity is a statement about the codomain — the function hits everything. Notice that surjectivity depends critically on how the codomain is defined. The function f(x) = x² is not surjective from ℝ to ℝ (negative numbers are never hit), but it is surjective from ℝ to [0, ∞). This is why the codomain is part of the function's definition.

A function is **bijective** if it is both injective and surjective — a perfect one-to-one correspondence between domain and codomain. Every element of B is hit by exactly one element of A. Bijections are the right notion of "same size" for sets: if a bijection exists between A and B, they have the same cardinality. This works even for infinite sets — the existence of a bijection between the natural numbers and the even numbers shows they have the same cardinality despite one being a proper subset of the other. A bijection is also exactly the condition under which the inverse function f⁻¹: B → A exists as a function.
