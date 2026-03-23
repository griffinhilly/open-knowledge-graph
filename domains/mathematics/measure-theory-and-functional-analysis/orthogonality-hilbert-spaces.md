---
id: orthogonality-hilbert-spaces
title: Orthogonality in Hilbert Spaces
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: hilbert-spaces
  type: hard
builds-toward:
- riesz-representation-theorem-hilbert
tags:
- hilbert-spaces
- geometry
stage: expert
status: draft
---

# Orthogonality in Hilbert Spaces

## Core Idea
Elements u, v are orthogonal if ⟨u, v⟩ = 0. The orthogonal complement M⊥ of a closed subspace M is always closed and satisfies H = M ⊕ M⊥, enabling orthogonal decompositions.

## Questions

```yaml
- question: "Let M be a closed subspace of a Hilbert space H, and let h ∈ H. The orthogonal projection of h onto M is best described as:"
  type: multiple-choice
  options:
    - "The unique element of M with the smallest norm"
    - "The unique element m ∈ M that minimizes ‖h − m‖ — the closest point in M to h"
    - "The element of M⊥ that, when added to h, gives zero"
    - "Any element of M that is orthogonal to h"
  answer: 1
  explanation: "The orthogonal decomposition theorem guarantees that h = m + m⊥ uniquely, where m ∈ M and m⊥ ∈ M⊥. The element m is the orthogonal projection of h onto M, and it is the closest point in M to h: for any other element n ∈ M, ‖h − m‖ ≤ ‖h − n‖. This best-approximation property is the key geometric content. In L²[−π,π], partial sums of Fourier series are projections onto finite-dimensional subspaces, giving the best approximations to a function by trigonometric polynomials of degree ≤ N."

- question: "A student argues: 'Orthogonal decomposition should work for any subspace M, not just closed ones — if M has an orthogonal complement, H = M ⊕ M⊥ should hold.' What is the flaw?"
  type: multiple-choice
  options:
    - "Non-closed subspaces have no orthogonal complement at all"
    - "M⊥ is well-defined for any subspace, but the closest point to h in M may not exist when M is not closed — closure is needed to guarantee the infimum is achieved"
    - "Orthogonal decomposition works for non-closed subspaces in finite dimensions but fails only in infinite dimensions"
    - "The student is correct — the theorem holds for any subspace, closed or not"
  answer: 1
  explanation: "M⊥ is always well-defined and closed (for any M), but the problem is existence of the closest point. The infimum of {‖h − m‖ : m ∈ M} is always finite, but may not be achieved — there may be no element in M that actually attains the minimum distance — if M is not closed. In infinite-dimensional spaces, a non-closed subspace may contain sequences converging to elements outside M, so the infimum-achieving limit escapes M. Closure ensures the minimizer exists within M."

- question: "M⊥ is always a closed subspace of H, even if M itself is not closed."
  type: true-false
  answer: true
  explanation: "M⊥ = {v ∈ H : ⟨v, m⟩ = 0 for all m ∈ M} is an intersection of sets of the form {v : ⟨v, m⟩ = 0}, each of which is closed (the kernel of the continuous linear map v ↦ ⟨v, m⟩). An intersection of closed sets is closed, so M⊥ is always closed regardless of whether M is. The closure of M⊥ follows from continuity of the inner product, not from any property of M itself."

- question: "If M is a closed subspace of a Hilbert space H, then M ∩ M⊥ can contain non-zero elements, since some vectors might project non-trivially onto both M and its complement."
  type: true-false
  answer: false
  explanation: "M ∩ M⊥ = {0}. If v ∈ M ∩ M⊥, then since v ∈ M⊥, we have ⟨v, m⟩ = 0 for all m ∈ M. But v ∈ M, so in particular ⟨v, v⟩ = 0, which gives ‖v‖² = 0, hence v = 0. The only vector orthogonal to itself is the zero vector. This trivial intersection is why the decomposition h = m + m⊥ is unique and the sum is a true direct sum."

- question: "How do Fourier series illustrate the orthogonal decomposition theorem in L²[−π,π]? Identify the subspace, the inner product, and what the theorem guarantees."
  type: short-answer
  answer: "In H = L²[−π,π], the inner product is ⟨f, g⟩ = ∫f(x)g(x)dx. The trigonometric functions {1, cos(x), sin(x), cos(2x), sin(2x), …} form an orthonormal system — each pair has inner product zero, each has unit norm. Each finite collection of these functions spans a closed subspace (a space of trigonometric polynomials). The orthogonal decomposition theorem, extended to the full orthonormal basis, guarantees that any f ∈ L²[−π,π] decomposes uniquely as a Fourier series, and each Fourier coefficient is computed as the inner product ⟨f, eₙ⟩."
  explanation: "Fourier coefficients are inner products: aₙ = (1/π)⟨f, cos(nx)⟩, bₙ = (1/π)⟨f, sin(nx)⟩. The partial sums of the Fourier series are orthogonal projections onto finite-dimensional subspaces, giving the best L² approximation to f by trigonometric polynomials of degree ≤ N. The full theorem guarantees that the series converges in L² norm to f itself. This makes abstract Hilbert space geometry the engine behind one of the most widely used tools in mathematics, physics, and engineering."
```

## Explainer

In ℝ², two vectors are perpendicular when their dot product is zero: the x-axis and y-axis are orthogonal because (1,0)·(0,1) = 0. In a Hilbert space H, the exact same definition works in infinite dimensions: elements u and v are **orthogonal** if ⟨u, v⟩ = 0. This is not a metaphor — it is the literal extension of the geometric notion of perpendicularity. The inner product that defines the Hilbert space is what makes this generalization possible; in a mere Banach space, you have no inner product and hence no notion of angle.

Given a closed subspace M ⊆ H, the **orthogonal complement** M⊥ is the set of all elements in H that are orthogonal to every element of M: M⊥ = {v ∈ H : ⟨v, m⟩ = 0 for all m ∈ M}. Several structural facts hold. First, M⊥ is always a closed subspace, regardless of what M looks like — the condition ⟨v, m⟩ = 0 is preserved under limits because the inner product is continuous. Second, M and M⊥ have trivial intersection: the only vector orthogonal to itself is zero, since ⟨v, v⟩ = 0 implies ‖v‖ = 0. In finite dimensions, you already know this from linear algebra: the row space and null space of a matrix are orthogonal complements in ℝⁿ.

The central theorem is the **orthogonal decomposition**: if M is a closed subspace of H, then every element h ∈ H can be written uniquely as h = m + m⊥, where m ∈ M and m⊥ ∈ M⊥. This is written H = M ⊕ M⊥ (the **direct sum**). The element m is called the **orthogonal projection** of h onto M, and it is the closest point in M to h. This projection property is enormously useful: it gives you the best approximation of h from the subspace M, in the sense of minimizing the norm ‖h − m‖.

In L²[−π,π], Fourier series illustrate orthogonal decomposition concretely. The functions {1, cos(x), sin(x), cos(2x), sin(2x), ...} form an **orthonormal basis** — mutually orthogonal functions each with unit norm. Every square-integrable function decomposes uniquely into a sum of these basis elements, and each Fourier coefficient is the inner product of the function with the corresponding basis element. The decomposition theorem guarantees that this sum converges in L², making the abstract theorem the engine behind one of the most useful tools in applied mathematics.
