---
id: composition-of-functions-sets
title: Function Composition and Functional Structure
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: functions-and-function-properties
  type: hard
builds-toward:
- well-founded-relations-and-recursion
- natural-numbers-as-iterative-construction
tags:
- composition
- structure
- identity
stage: formal-systems
status: validated
---

# Function Composition and Functional Structure

## Core Idea
Given f: A → B and g: B → C, their composition (g ∘ f): A → C is defined by (g ∘ f)(a) = g(f(a)). Composition is associative and has an identity function id_A for each set, making it a fundamental operation. Bijections compose to bijections, and injections/surjections preserve their properties under composition.

## Questions

```yaml
- question: "Given f: A → B defined by f(a) = a + 1 and g: B → C defined by g(b) = b², what is (g ∘ f)(3)?"
  type: multiple-choice
  options:
    - "10 (computing g(3) = 9, then f(9) = 10)"
    - "16 (computing f(3) = 4, then g(4) = 16)"
    - "7 (adding f(3) + g(3) = 4 + 9)"
    - "12 (multiplying f(3) × g(3) = 4 × 3)"
  answer: 1
  explanation: "The notation g ∘ f means 'apply f first, then g.' So (g ∘ f)(3) = g(f(3)) = g(4) = 16. Option A reverses the order — applying g first, then f — which is a common mistake. The symbol g ∘ f is read 'g after f,' and the right-to-left application order follows mathematical convention where the function closest to the argument is applied first."

- question: "Suppose g ∘ f is an injective (one-to-one) function. What can we conclude?"
  type: multiple-choice
  options:
    - "Both f and g must be injective"
    - "f must be injective, but g need not be"
    - "g must be injective, but f need not be"
    - "Neither f nor g is required to be injective"
  answer: 1
  explanation: "If g ∘ f is injective and f(a₁) = f(a₂), then g(f(a₁)) = g(f(a₂)), so (g ∘ f)(a₁) = (g ∘ f)(a₂), which forces a₁ = a₂. So f must be injective. But g need not be: g could be non-injective on its full codomain, as long as it is injective on the image of f. The dual fact is: if g ∘ f is surjective, then g must be surjective (though f need not be)."

- question: "The composition of two bijections is always a bijection."
  type: true-false
  answer: true
  explanation: "If f: A → B and g: B → C are both bijections (injective and surjective), then g ∘ f is injective (composition of injections is injective) and surjective (composition of surjections is surjective), hence a bijection. This also means g ∘ f has a two-sided inverse, namely f⁻¹ ∘ g⁻¹: C → A. This fact underlies why bijections form a group under composition."

- question: "Function composition is commutative: for any functions f and g with compatible domains, f ∘ g typically equals g ∘ f."
  type: true-false
  answer: false
  explanation: "Composition is generally not commutative. For example, if f(x) = x + 1 and g(x) = x², then (f ∘ g)(x) = x² + 1 but (g ∘ f)(x) = (x + 1)² = x² + 2x + 1 — clearly different. Furthermore, f ∘ g and g ∘ f may not even both be defined if the domains and codomains don't align. Composition IS associative (h ∘ (g ∘ f) = (h ∘ g) ∘ f), but associativity and commutativity are different properties."

- question: "Why does the notation g ∘ f indicate that f is applied first, and why does this right-to-left order matter?"
  type: short-answer
  answer: "The notation comes from how functions are written in mathematics: to apply g after f to an element a, you write g(f(a)), where the innermost function (f) acts first. The symbol g ∘ f mirrors this: f is on the right, closest to the input, so it is applied first. The order matters because composition is not commutative — f ∘ g and g ∘ f generally produce different functions, and may not even both be defined if the codomain of one doesn't match the domain of the other."
  explanation: "This right-to-left convention can feel counterintuitive but is consistent throughout mathematics. The codomain of f must equal the domain of g for g ∘ f to be defined — this domain-matching requirement enforces the order and prevents ambiguity. In category theory, this convention is standardized and extended to arbitrary morphisms."
```

## Explainer

From your study of functions, you know a function f: A → B is a rule that assigns each element of A exactly one element of B. **Composition** asks: what happens when you apply two functions in sequence? If f takes elements of A to elements of B, and g takes elements of B to elements of C, then the composition **(g ∘ f)** takes elements of A directly to C by doing f first, then g. Written out: (g ∘ f)(a) = g(f(a)). The output of f becomes the input of g.

Notice the notation: g ∘ f is read "g after f" or "g of f," and is applied right to left. This matches mathematical convention where function application is written on the right of the argument: you write g(f(a)), not f(g(a)). The codomain of f must match the domain of g — otherwise composition is undefined. This domain-matching requirement is what makes the order of functions in a composition non-interchangeable in general: f ∘ g and g ∘ f are typically different functions (or may not even both be defined if A ≠ C).

Two algebraic properties make composition deeply useful. First, it is **associative**: (h ∘ g) ∘ f = h ∘ (g ∘ f) whenever the types align. This means you can compose a chain of functions without worrying about which pair you combine first — the result is the same. You can verify this directly: both sides send a to h(g(f(a))). Second, each set A has an **identity function** id_A: A → A defined by id_A(a) = a, and this identity acts as a neutral element: f ∘ id_A = f and id_B ∘ f = f. Together, associativity and identity make the collection of functions on a set into a **monoid** — the algebraic structure behind sequential processes.

Composition interacts cleanly with injectivity, surjectivity, and bijectivity. The composition of two injections is injective, the composition of two surjections is surjective, and the composition of two bijections is a bijection. Furthermore, if g ∘ f is injective then f must be injective (though g need not be), and if g ∘ f is surjective then g must be surjective (though f need not be). These facts let you decompose structure: to show a function is a bijection, it is often easiest to exhibit a two-sided inverse — a function h such that h ∘ f = id_A and f ∘ h = id_B. This inverse, when it exists, is unique and is itself a bijection. Composition is therefore the algebraic glue that connects functions into structures like groups of symmetries, categories, and recursive constructions — the topics you'll build on next.
