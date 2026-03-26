---
id: orthogonality-and-projections
title: Orthogonality and Orthogonal Projections
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: hilbert-spaces
  type: hard
builds-toward:
- riesz-representation-hilbert
- orthonormal-bases-in-hilbert
tags:
- hilbert-spaces
- projections
stage: expert
status: validated
---

# Orthogonality and Orthogonal Projections

## Core Idea
Vectors x and y in a Hilbert space are orthogonal if ⟨x,y⟩ = 0. For a closed convex set K, there is a unique nearest point. Orthogonal projection onto a closed subspace M is the linear operator P_M: H → M projecting each x to the nearest point in M.

## Questions

```yaml
- question: "A vector x ∈ H is projected onto a closed subspace M, yielding a candidate point m₀ ∈ M. A student checks whether m₀ is the orthogonal projection by computing x − m₀ and testing ⟨x − m₀, m⟩ = 0 for all m ∈ M. The test passes. What can we conclude?"
  type: multiple-choice
  options:
    - "Nothing — this test only works in finite-dimensional spaces"
    - "m₀ is the orthogonal projection P_M x, and it is the unique nearest point in M to x"
    - "m₀ is a projection but may not be the nearest point in M"
    - "x must already be in M, since the error is orthogonal to everything"
  answer: 1
  explanation: "The orthogonality condition ⟨x − m₀, m⟩ = 0 for all m ∈ M uniquely characterizes the orthogonal projection in any Hilbert space, finite- or infinite-dimensional. This condition is equivalent to minimizing ‖x − m‖ over M. The two characterizations — nearest point and orthogonal error — are identical: m₀ is both. Option C is wrong because no two distinct points in a closed convex set can both be nearest."

- question: "An operator P on a Hilbert space satisfies P² = P and ⟨Px, y⟩ = ⟨x, Py⟩ for all x, y. A student claims P must be the zero operator because 'applying it twice with no change means it collapsed everything to zero.' What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing — P² = P does imply P = 0 in infinite dimensions"
    - "The student forgot that P² = P is satisfied by the identity operator I as well as by 0"
    - "P² = P (idempotence) means that any vector already in the range of P is fixed by P — not sent to zero"
    - "The self-adjoint condition overrides the idempotence condition"
  answer: 2
  explanation: "Idempotence P² = P means that once you project onto M, re-applying P leaves you in M unchanged — P fixes every vector in its own range. Both P = 0 and P = I satisfy P² = P, but so does every orthogonal projection onto any subspace. The geometric meaning is: a vector already in M is its own nearest point in M, so projecting it again does nothing. This is the opposite of 'collapsing to zero.'"

- question: "If P_M x = x for some nonzero vector x, then x must not be in the subspace M."
  type: true-false
  answer: false
  explanation: "P_M x = x means x is fixed by the projection — its nearest point in M is itself, which happens precisely when x ∈ M. The statement has it backwards: P_M x = x if and only if x is already in M. Conversely, P_M x = 0 would mean the nearest point of x in M is the origin, which occurs when x ∈ M⊥."

- question: "The orthogonal projection P_M is idempotent (P_M² = P_M) because projecting a vector that is already in M gives back that same vector."
  type: true-false
  answer: true
  explanation: "This is exactly the geometric content of idempotence. If y = P_M x ∈ M, then the nearest point in M to y is y itself, so P_M y = y. Therefore P_M(P_M x) = P_M x, which is P_M² = P_M. The self-adjoint condition ⟨P_M x, y⟩ = ⟨x, P_M y⟩ is an independent property expressing the symmetry of perpendicularity."

- question: "Why does the orthogonality of the error vector x − P_M x to every vector in M uniquely characterize the orthogonal projection? What goes wrong if the error is not fully orthogonal to M?"
  type: short-answer
  answer: "If x − m₀ is not orthogonal to some m₁ ∈ M, we can find a better approximation to x by moving m₀ toward m₁, reducing the distance. Only when the error is orthogonal to the entire subspace is there no direction within M that improves the approximation. The Pythagorean theorem in Hilbert space formalizes this: ‖x − m‖² = ‖x − P_M x‖² + ‖P_M x − m‖² for any m ∈ M, showing the projection error is the minimum possible."
  explanation: "The orthogonality condition eliminates all 'first-order improvements' — it says you're at a critical point of the distance function restricted to M. Because M is a convex set and the distance is a strictly convex function, the critical point is a global minimum. The uniqueness follows from strict convexity: two distinct minimizers would average to a point with even smaller distance, contradiction."
```

## Explainer

Your study of Hilbert spaces gave you a complete inner product space: a vector space equipped with ⟨·,·⟩ satisfying linearity, symmetry, and positive-definiteness, and complete with respect to the induced norm ||x|| = √⟨x,x⟩. The inner product does something coordinate geometry does not — it defines angles. Two vectors are **orthogonal** when ⟨x, y⟩ = 0, the algebraic condition capturing a 90-degree angle. In ℝ² this is familiar; the power of Hilbert space theory is that the same condition works for spaces of functions. Two functions f and g in L²[0,1] are orthogonal when ∫₀¹ f(x)g(x) dx = 0 — the integral of their product vanishes.

The **projection theorem** is the central result of this topic. Let M be a closed subspace of a Hilbert space H (closed meaning it contains its own limit points). For any x ∈ H, there is a unique element P_M x ∈ M that minimizes the distance ||x - m|| over all m ∈ M. This nearest point is the **orthogonal projection** of x onto M. The intuition from ℝ²: drop a perpendicular from a point to a line — where it lands is the closest point on the line, and the perpendicular segment is the error. This exact geometric picture generalizes without change to any Hilbert space, including infinite-dimensional ones.

The error vector x - P_M x is always orthogonal to M: ⟨x - P_M x, m⟩ = 0 for every m ∈ M. This **orthogonality condition** characterizes the projection uniquely, and it is often the most useful way to compute P_M x in practice. The projection operator P_M: H → H is linear, **idempotent** (P_M² = P_M — projecting twice is the same as projecting once), and **self-adjoint** (⟨P_M x, y⟩ = ⟨x, P_M y⟩). The idempotence expresses that once you're already in M, projection doesn't move you. Self-adjointness is the abstract version of the geometric symmetry of perpendicularity.

Orthogonal projections are the engine behind several major constructions. Least-squares solutions to overdetermined systems are projections of the target vector onto a column space. Fourier series decompose a function as a sum of projections onto subspaces spanned by sine and cosine functions — the coefficients are inner products precisely because projection onto a one-dimensional subspace spanned by a unit vector e is just ⟨x, e⟩e. The direct sum decomposition H = M ⊕ M⊥ — every element uniquely splits into a component in M and a component orthogonal to M — is the cornerstone of the Riesz representation theorem and the spectral theory of self-adjoint operators that lie ahead.
