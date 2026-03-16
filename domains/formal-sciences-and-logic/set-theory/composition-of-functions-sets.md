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
status: draft
---

# Function Composition and Functional Structure

## Core Idea
Given f: A → B and g: B → C, their composition (g ∘ f): A → C is defined by (g ∘ f)(a) = g(f(a)). Composition is associative and has an identity function id_A for each set, making it a fundamental operation. Bijections compose to bijections, and injections/surjections preserve their properties under composition.

## Explainer

From your study of functions, you know a function f: A → B is a rule that assigns each element of A exactly one element of B. **Composition** asks: what happens when you apply two functions in sequence? If f takes elements of A to elements of B, and g takes elements of B to elements of C, then the composition **(g ∘ f)** takes elements of A directly to C by doing f first, then g. Written out: (g ∘ f)(a) = g(f(a)). The output of f becomes the input of g.

Notice the notation: g ∘ f is read "g after f" or "g of f," and is applied right to left. This matches mathematical convention where function application is written on the right of the argument: you write g(f(a)), not f(g(a)). The codomain of f must match the domain of g — otherwise composition is undefined. This domain-matching requirement is what makes the order of functions in a composition non-interchangeable in general: f ∘ g and g ∘ f are typically different functions (or may not even both be defined if A ≠ C).

Two algebraic properties make composition deeply useful. First, it is **associative**: (h ∘ g) ∘ f = h ∘ (g ∘ f) whenever the types align. This means you can compose a chain of functions without worrying about which pair you combine first — the result is the same. You can verify this directly: both sides send a to h(g(f(a))). Second, each set A has an **identity function** id_A: A → A defined by id_A(a) = a, and this identity acts as a neutral element: f ∘ id_A = f and id_B ∘ f = f. Together, associativity and identity make the collection of functions on a set into a **monoid** — the algebraic structure behind sequential processes.

Composition interacts cleanly with injectivity, surjectivity, and bijectivity. The composition of two injections is injective, the composition of two surjections is surjective, and the composition of two bijections is a bijection. Furthermore, if g ∘ f is injective then f must be injective (though g need not be), and if g ∘ f is surjective then g must be surjective (though f need not be). These facts let you decompose structure: to show a function is a bijection, it is often easiest to exhibit a two-sided inverse — a function h such that h ∘ f = id_A and f ∘ h = id_B. This inverse, when it exists, is unique and is itself a bijection. Composition is therefore the algebraic glue that connects functions into structures like groups of symmetries, categories, and recursive constructions — the topics you'll build on next.
