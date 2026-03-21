---
id: functions-domain-codomain-range
title: 'Functions: Domain, Codomain, and Range'
domain: mathematics
course: methods-of-proof
prerequisites:
- id: cartesian-products-relations
  type: hard
builds-toward:
- injective-surjective-bijective-functions
- function-composition-and-inverses
tags:
- functions
- domain
- codomain
- range
stage: formal-systems
status: draft
---

# Functions: Domain, Codomain, and Range

## Core Idea
A function f: A → B is a relation where each element of A (the domain) maps to exactly one element of B (the codomain). The range is the set of all elements in B that are actually outputs of f. Distinguishing codomain from range is critical: the codomain is fixed by definition, while the range is determined by which outputs are attained.

## Questions

```yaml
- question: "Consider f: ℝ → ℝ defined by f(x) = x². A student says 'we can just redefine the codomain to [0, ∞) to make this function surjective — the formula is the same either way.' What is the most precise response?"
  type: multiple-choice
  options:
    - "The student is wrong; surjectivity depends only on the formula, not the codomain"
    - "The student is correct; the codomain is just a label and doesn't affect whether the function is surjective"
    - "Both functions are valid, but f: ℝ → ℝ is not surjective while f: ℝ → [0, ∞) is a different, surjective function — codomain is part of the function's specification"
    - "Surjectivity cannot be determined until you know the range, which is the same regardless of the codomain"
  answer: 2
  explanation: "The codomain is part of a function's formal definition, not merely a label. f: ℝ → ℝ and f: ℝ → [0, ∞), both defined by f(x) = x², are technically different mathematical objects — they differ in their codomain. The first is not surjective (negative reals are never outputs); the second is surjective (every nonneg­ative real is an output). Changing the codomain changes the function, and whether it is surjective depends on whether the range equals the declared codomain."

- question: "Which of the following correctly identifies the range of f: ℝ → ℝ defined by f(x) = sin(x)?"
  type: multiple-choice
  options:
    - "ℝ, because the codomain is ℝ and the range must equal the codomain"
    - "[−1, 1], the set of all values actually produced as outputs of f"
    - "[0, 1], since sine is nonnegative for inputs in [0, π]"
    - "The range cannot be determined without knowing the specific inputs"
  answer: 1
  explanation: "The range is the set of outputs actually attained: {f(x) : x ∈ ℝ} = [−1, 1]. The codomain (ℝ) is the declared target set, which is larger than the range. The range is always a subset of the codomain, but can be strictly smaller — as it is here. The function is not surjective precisely because the range does not equal the codomain."

- question: "Two functions with the same formula but different declared codomains are the same mathematical function."
  type: true-false
  answer: false
  explanation: "A function is formally specified by three things: its domain, its codomain, and its rule. Changing any one of these produces a different function. f: ℝ → ℝ and f: ℝ → [0, ∞), both given by f(x) = x², differ in codomain and are therefore different functions — most importantly, one is surjective and one is not. This distinction only matters in rigorous mathematics, but it is essential for correctly defining and reasoning about properties like surjectivity."

- question: "The range of a function f: A → B is always a subset of its codomain B."
  type: true-false
  answer: true
  explanation: "By definition, the range is {f(a) : a ∈ A} — the set of all outputs produced by elements of A. Every output must land in B (that is what it means for the function to map into B), so the range is contained in B. The range equals B if and only if f is surjective. In all other cases, the range is a proper subset of B."

- question: "Why does the distinction between codomain and range matter for determining whether a function is surjective? Give an example."
  type: short-answer
  answer: "A function is surjective if and only if its range equals its codomain — every element of the codomain is achieved as an output. If the codomain and range are confused, surjectivity becomes undefined or circular. For example, f(x) = x² with codomain ℝ is not surjective (negative numbers are never outputs, so range ≠ codomain). But with codomain [0, ∞), the same formula gives a surjective function (every nonneg­ative real is achieved). The codomain is what you promise; the range is what you deliver — surjectivity asks whether the promise is kept."
  explanation: "This distinction also controls how function composition and inverses work. A surjective function can be right-inverted; one that is not surjective cannot. Without distinguishing codomain from range, you cannot meaningfully define or check surjectivity."
```

## Explainer

You already know that a Cartesian product A × B consists of ordered pairs (a, b), and that a relation is a subset of A × B. A **function** f: A → B is a special kind of relation: one where every element of A appears as the first coordinate of exactly one pair. In other words, every input has exactly one output. What distinguishes a function from a general relation is this uniqueness requirement — no input maps to two different outputs, and no input is left without an output.

The three terms **domain**, **codomain**, and **range** capture different aspects of a function's scope. The domain is the set A of all permitted inputs — the function must be defined on every element of A. The codomain is the set B declared as the target — it is a promise about where outputs land, chosen as part of the function's definition. The range (also called image) is {f(a) : a ∈ A} ⊆ B — the collection of outputs actually produced. The range is always a subset of the codomain, but can be strictly smaller.

The distinction between codomain and range is subtle but critical. Consider f: ℝ → ℝ defined by f(x) = x². The codomain is ℝ (all real numbers), but the range is [0, ∞) — no output is negative. You could alternatively write f: ℝ → [0, ∞), declaring the codomain to be just the nonneg­atives. These are technically different functions even though the formula is identical, because the codomain is part of the function's specification. This matters enormously for **surjectivity**: f is surjective (onto) if and only if every element of the codomain is achieved as an output — i.e., range = codomain. Whether f(x) = x² is surjective depends entirely on the declared codomain.

This framework also clarifies well-definedness. When you define a function by a formula or rule, you must verify: (1) the formula applies to every element of the domain, and (2) each domain element maps to a unique output. In abstract algebra, functions are often defined on equivalence classes, and checking well-definedness — verifying the output doesn't depend on which representative you chose — is a required proof step. The domain-codomain-range framework makes that checklist precise.
