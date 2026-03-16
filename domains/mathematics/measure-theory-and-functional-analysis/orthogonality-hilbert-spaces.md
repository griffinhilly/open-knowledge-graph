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
stage: advanced
status: draft
---

# Orthogonality in Hilbert Spaces

## Core Idea
Elements u, v are orthogonal if ⟨u, v⟩ = 0. The orthogonal complement M⊥ of a closed subspace M is always closed and satisfies H = M ⊕ M⊥, enabling orthogonal decompositions.

## Explainer

In ℝ², two vectors are perpendicular when their dot product is zero: the x-axis and y-axis are orthogonal because (1,0)·(0,1) = 0. In a Hilbert space H, the exact same definition works in infinite dimensions: elements u and v are **orthogonal** if ⟨u, v⟩ = 0. This is not a metaphor — it is the literal extension of the geometric notion of perpendicularity. The inner product that defines the Hilbert space is what makes this generalization possible; in a mere Banach space, you have no inner product and hence no notion of angle.

Given a closed subspace M ⊆ H, the **orthogonal complement** M⊥ is the set of all elements in H that are orthogonal to every element of M: M⊥ = {v ∈ H : ⟨v, m⟩ = 0 for all m ∈ M}. Several structural facts hold. First, M⊥ is always a closed subspace, regardless of what M looks like — the condition ⟨v, m⟩ = 0 is preserved under limits because the inner product is continuous. Second, M and M⊥ have trivial intersection: the only vector orthogonal to itself is zero, since ⟨v, v⟩ = 0 implies ‖v‖ = 0. In finite dimensions, you already know this from linear algebra: the row space and null space of a matrix are orthogonal complements in ℝⁿ.

The central theorem is the **orthogonal decomposition**: if M is a closed subspace of H, then every element h ∈ H can be written uniquely as h = m + m⊥, where m ∈ M and m⊥ ∈ M⊥. This is written H = M ⊕ M⊥ (the **direct sum**). The element m is called the **orthogonal projection** of h onto M, and it is the closest point in M to h. This projection property is enormously useful: it gives you the best approximation of h from the subspace M, in the sense of minimizing the norm ‖h − m‖.

In L²[−π,π], Fourier series illustrate orthogonal decomposition concretely. The functions {1, cos(x), sin(x), cos(2x), sin(2x), ...} form an **orthonormal basis** — mutually orthogonal functions each with unit norm. Every square-integrable function decomposes uniquely into a sum of these basis elements, and each Fourier coefficient is the inner product of the function with the corresponding basis element. The decomposition theorem guarantees that this sum converges in L², making the abstract theorem the engine behind one of the most useful tools in applied mathematics.
