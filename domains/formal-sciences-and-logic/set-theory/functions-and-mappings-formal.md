---
id: functions-and-mappings-formal
title: 'Functions and Mappings: Formal Definition'
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: relations-as-set-subsets
  type: hard
builds-toward:
- injections-surjections-bijections-classification
tags:
- functions
- mappings
- domain-codomain-range
stage: formal-systems
status: validated
---

# Functions and Mappings: Formal Definition

## Core Idea
A function f: A → B is a relation from A to B where each element of A is paired with exactly one element of B. This definition generalizes functions beyond real arithmetic to arbitrary sets. The domain A and codomain B are essential parts of the definition; the range is the set of all actual outputs f(A).

## Questions

```yaml
- question: "Let f: ℝ → ℝ be defined by f(x) = x², and let g: ℝ → [0, ∞) be defined by g(x) = x². Are f and g the same function?"
  type: multiple-choice
  options:
    - "Yes — they have the same rule, so they are the same function"
    - "Yes — they have the same domain and the same range, so they are the same function"
    - "No — they have different codomains, and the codomain is part of the function's specification"
    - "It depends on context; in some frameworks they are equal and in others they are not"
  answer: 2
  explanation: "The codomain is part of the specification of a function, not an afterthought. f: ℝ → ℝ and g: ℝ → [0, ∞) differ in their codomain even though they have the same rule and the same range. Two functions are equal if and only if they have the same domain, the same codomain, and the same graph (set of ordered pairs). Changing the codomain gives a different function — a fact that matters for properties like surjectivity: g is surjective, but f is not."

- question: "Which condition is required for a relation R ⊆ A × B to qualify as a function from A to B?"
  type: multiple-choice
  options:
    - "Every element of B must appear as a second coordinate in R"
    - "Every element of A must appear as a first coordinate in exactly one ordered pair in R"
    - "No element of B may appear as a second coordinate more than once"
    - "The relation must be symmetric: if (a, b) ∈ R then (b, a) ∈ R"
  answer: 1
  explanation: "A function must be total (every element of A has an output) and single-valued (each element of A has exactly one output). This is precisely 'each element of A appears as a first coordinate in exactly one pair.' Option A would require surjectivity, which is not part of the function definition. Option C would rule out many-to-one functions like f(x) = x², where different inputs can map to the same output. Option D describes symmetry, a property of relations that has nothing to do with functions."

- question: "The range of a function f: A → B is always a subset of the codomain B, but it need not equal B."
  type: true-false
  answer: true
  explanation: "The range (image) f(A) = {f(a) : a ∈ A} is the set of actual outputs, and by definition every actual output is an element of the codomain B, so f(A) ⊆ B. But f need not hit every element of B — that stronger condition (f(A) = B) is surjectivity. For example, f: ℝ → ℝ defined by f(x) = x² has range [0, ∞), which is a proper subset of ℝ."

- question: "Two functions with the same rule are always equal, regardless of their specified domains and codomains."
  type: true-false
  answer: false
  explanation: "Domain and codomain are constitutive parts of a function's identity, not mere annotations. The function f: ℝ → ℝ given by f(x) = x² and g: [0, ∞) → ℝ given by g(x) = x² are different functions — they have different domains. Similarly, changing the codomain (as in the ℝ → ℝ vs. ℝ → [0,∞) example) produces different functions even with the same rule. Two functions are equal iff they agree on domain, codomain, and all output values."

- question: "Why does the formal set-theoretic definition of a function specify both the domain and codomain as part of the function, rather than just the rule that maps inputs to outputs?"
  type: short-answer
  answer: "The domain and codomain determine the function's identity and what properties it can have. Without fixing the domain, there is no well-defined set of inputs and 'totality' has no meaning. Without fixing the codomain, surjectivity cannot be defined (surjectivity means every element of the codomain is hit — but which set is the codomain?). Two functions with identical rules but different codomains differ in surjectivity. The set-theoretic definition (a function IS a set of ordered pairs, plus a specified domain and codomain) makes these distinctions precise and enables function equality, composition, and classification into injective/surjective/bijective."
  explanation: "This also explains why the set-of-pairs definition is preferable to a 'rule-based' definition: two different-looking rules (f(x) = x+1−1 and g(x) = x) define the same function from ℤ to ℤ, because their graphs are identical. Extensionality — judging equality by behavior, not description — is fundamental to rigorous mathematics."
```

## Explainer

You already know that a relation from A to B is a subset of the Cartesian product A × B — a collection of ordered pairs (a, b) where a ∈ A and b ∈ B. A **function** f: A → B is a relation with two additional constraints: it is **total** (every element of A appears as a first coordinate) and **single-valued** (no element of A appears as a first coordinate more than once). In other words, for every a ∈ A there exists *exactly one* b ∈ B such that (a, b) ∈ f. Writing "f(a) = b" is shorthand for "(a, b) ∈ f." This is the set-theoretic definition of function — a function *is* a set of ordered pairs satisfying these two conditions.

The distinction between **domain**, **codomain**, and **range** is essential and often confused. The domain A is the set of all inputs — every element of A must have an output. The codomain B is the declared "output type" — it is part of the specification of f and need not equal the set of actual outputs. The **range** (or image) f(A) = {f(a) : a ∈ A} is the set of values that f actually takes; it is a subset of B, but may be a proper subset. For example, the function f: ℝ → ℝ defined by f(x) = x² has domain ℝ, codomain ℝ, and range [0, ∞) ⊊ ℝ. Changing the codomain to [0, ∞) gives a *different function* — same rule, different specification — even though the rule and range are identical.

Why define functions as sets of pairs rather than as "rules"? The set-theoretic definition is required for rigor in contexts where "rule" is ambiguous or where functions are constructed by set operations. For instance, the axiom of choice constructs functions whose rule cannot be written down explicitly; the set-of-pairs definition handles these without awkwardness. It also makes function equality precise: two functions f and g from A to B are equal iff they have the same graph — the same set of pairs — regardless of how they are described. This extensional notion of equality is fundamental: f(x) = x + 1 − 1 and g(x) = x are the *same* function from ℤ to ℤ.

This formal definition generalizes immediately to arbitrary sets, not just number systems. Functions between finite sets (used in combinatorics and group theory), functions between sets of strings (formal language theory), and functions between structures (homomorphisms in algebra) all fall under the same definition. The building blocks — total, single-valued relations — extend naturally to **partial functions** (drop totality) and **multivalued functions** (drop single-valuedness), which arise in computability theory and analysis. Mastering the formal definition of function here is the foundation for all of these, and for the classification of functions as injective, surjective, or bijective that follows immediately from it.
