---
id: dual-spaces-bounded-functionals
title: Dual Spaces and Bounded Linear Functionals
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: operator-norm
  type: hard
builds-toward:
- hahn-banach-theorem
tags:
- duality
stage: expert
status: validated
---

# Dual Spaces and Bounded Linear Functionals

## Core Idea
The dual space X* = B(X, ℝ) consists of all bounded linear functionals on X. As a Banach space under the operator norm, X* encodes geometric and topological information about X through the Hahn-Banach and Riesz representation theorems.

## Questions

```yaml
- question: "Let X be a normed vector space that is not complete (not a Banach space). Which of the following best describes its dual space X*?"
  type: multiple-choice
  options:
    - "X* is also incomplete, since it inherits the incompleteness of X"
    - "X* is always a Banach space, regardless of whether X is complete"
    - "X* is empty if X is not complete, since bounded functionals require completeness"
    - "X* has the same topology as X but a different norm"
  answer: 1
  explanation: "The dual space X* is automatically a Banach space — complete under the operator norm — even when X itself is incomplete. This follows because bounded linear maps into a complete space inherit completeness: the scalar field ℝ is complete, and a Cauchy sequence of bounded functionals {φₙ} converges pointwise (since {φₙ(x)} is Cauchy in ℝ for each x), defining a limit functional that is bounded and linear. The argument makes no use of completeness of X. This is one of the most useful properties of dual spaces: X* is always a Banach space regardless of what X is."

- question: "The statement 'X* separates points of X' means which of the following?"
  type: multiple-choice
  options:
    - "Every individual bounded functional on X maps distinct elements to distinct real numbers"
    - "If φ(x) = φ(y) for every φ ∈ X*, then x = y"
    - "X* contains at least one functional that is injective on all of X"
    - "Bounded functionals can distinguish vectors only within finite-dimensional subspaces"
  answer: 1
  explanation: "The separation property says: if every functional in X* assigns the same value to x and y, then x = y — equivalently, distinct vectors can be distinguished by some functional in X*. This is a property of the *collective* dual space, not any individual functional (option A is too strong — no single φ need be injective on all of X). The separation property is guaranteed by the Hahn-Banach theorem and means no information about X is 'hidden' from its dual: the collection of measuring devices in X* sees everything."

- question: "The dual space X* of any normed vector space X is automatically a Banach space (complete under the operator norm), even if X itself is not a Banach space."
  type: true-false
  answer: true
  explanation: "True. Completeness of X* follows from the completeness of the scalar field ℝ, not from X. If {φₙ} is Cauchy in X*, then for each fixed x ∈ X, the sequence {φₙ(x)} is Cauchy in ℝ (since |φₙ(x) − φₘ(x)| ≤ ‖φₙ − φₘ‖·‖x‖), hence converges. This defines a limit functional φ, which one verifies is bounded and linear, with ‖φₙ − φ‖ → 0. The completeness of X is never invoked. This automatic completeness is a principal reason dual spaces are preferred in analysis."

- question: "The dual of the Banach space Lᵖ(μ) (for 1 < p < ∞) consists of all bounded linear functionals of the form f ↦ ∫fg dμ where g ∈ Lᵖ(μ) — that is, g lives in the same Lᵖ space."
  type: true-false
  answer: false
  explanation: "False. The dual of Lᵖ(μ) is Lᵍ(μ) where the exponents satisfy 1/p + 1/q = 1 — the Hölder conjugate, not Lᵖ itself. For example, the dual of L³(μ) is L^(3/2)(μ), not L³(μ). The Riesz representation theorem states every φ ∈ (Lᵖ)* has the form φ(f) = ∫fg dμ for a unique g ∈ Lᵍ, and ‖φ‖ = ‖g‖_q. The Hölder conjugate relationship 1/p + 1/q = 1 is precisely what makes ∫fg dμ well-defined and bounded via Hölder's inequality. (The special case p = q = 2 — the dual of L² is L² — is where the misconception likely originates.)"

- question: "Explain intuitively what a bounded linear functional 'does' geometrically to a normed space X, and how this relates to the idea that X* encodes information about X."
  type: short-answer
  answer: "A bounded linear functional φ: X → ℝ partitions X into parallel level hyperplanes {x : φ(x) = c}. It is a 'projection' of X onto the real line, picking out one linear 'direction.' The collection of all such projections in X* collectively encodes the full geometry of X: two vectors that every functional maps to the same value must be identical (the separation property). The norm of φ measures how finely it distinguishes nearby vectors. For example, on L²([0,1]), the functional φ_g(f) = ∫f(x)g(x)dx measures how much f resembles g in a precise inner-product sense."
  explanation: "This geometric picture becomes precise through the Hahn-Banach theorem, which guarantees enough functionals exist to separate any two points and to 'touch' every point on the unit sphere. Duality also encodes convexity: closed convex sets in X are intersections of half-spaces defined by functionals. This makes dual spaces central to optimization (Lagrangian duality), PDEs (weak formulations treat solutions as elements of dual spaces), and the representation theory of function spaces."
```

## Explainer

You already know the operator norm: for a bounded linear map T: X → Y between normed spaces, ‖T‖ = sup{‖Tx‖ : ‖x‖ ≤ 1}. A **bounded linear functional** is simply a bounded linear map whose codomain is the scalar field ℝ (or ℂ). Instead of sending vectors to vectors, it sends vectors to numbers. The canonical examples are everywhere: integration f ↦ ∫ f dμ is linear and bounded under integrability conditions; evaluation at a fixed point f ↦ f(x₀) is a functional on spaces of continuous functions; the inner product with a fixed vector, y ↦ ⟨y, x⟩, is a functional on any inner product space.

The **dual space** X* is the collection of all bounded linear functionals on X, equipped with the operator norm ‖φ‖ = sup{|φ(x)| : ‖x‖ ≤ 1}. This is not just a set — it is itself a Banach space. Even if X is not complete, X* automatically is, because the scalar field is complete and bounded linear maps into a complete space inherit completeness under the operator norm. This automatic completeness is one of the principal reasons the dual space is useful: you can always take limits of functionals freely.

The deep content is that X* encodes the geometry of X from the outside. A bounded functional φ ∈ X* is a "measuring device" for X — it carves X into level hyperplanes {x : φ(x) = c}, and the Hahn-Banach theorem (your next topic) guarantees that X* is rich enough to separate any two distinct points. If φ(x) = φ(y) for every φ ∈ X*, then x = y. This means the dual collectively "sees" everything in X; no information is hidden from it.

For concrete Banach spaces, duals can be explicitly identified with familiar spaces. The dual of Lᵖ(μ) is Lᵍ(μ) where 1/p + 1/q = 1 — the Hölder conjugate pair. Every bounded functional on Lᵖ has the form f ↦ ∫ fg dμ for a unique g ∈ Lᵍ. This is a striking identification: the abstract collection of measuring devices on Lᵖ is another Lᵍ space. The duality between Lᵖ and Lᵍ is precisely the same Hölder conjugate relationship underlying the Hölder and Minkowski inequalities, now reappearing as a structural theorem about the functional-analytic architecture of these spaces.
