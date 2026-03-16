---
id: riesz-representation-hilbert
title: Riesz Representation Theorem for Hilbert Spaces
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: orthogonality-and-projections
  type: hard
builds-toward:
- orthonormal-bases-in-hilbert
tags:
- hilbert-spaces
- representation
stage: abstract-reasoning
status: draft
---

# Riesz Representation Theorem for Hilbert Spaces

## Core Idea
The Riesz representation theorem states that for any bounded linear functional f on a Hilbert space H, there exists a unique y ∈ H such that f(x) = ⟨x, y⟩ for all x. This establishes an isometric isomorphism between H and its dual H*.

## Explainer

From your study of orthogonality and projections, you know that every element of a Hilbert space H can be decomposed relative to closed subspaces, and that the inner product ⟨·, ·⟩ is the fundamental tool for measuring angles and projecting vectors. Fix any vector y ∈ H and define the function f_y(x) = ⟨x, y⟩. This function takes vectors to scalars, is linear (from linearity of the inner product in the first slot), and is bounded — |f_y(x)| ≤ ‖y‖ · ‖x‖ by Cauchy-Schwarz. So every vector y in H produces a bounded linear functional on H. The **Riesz Representation Theorem** says the converse is also true: every bounded linear functional arises this way.

To see why, take any bounded linear functional f: H → ℝ (or ℂ). If f is the zero functional, take y = 0. Otherwise, consider the kernel of f — the set ker(f) = {x : f(x) = 0}. This is a closed subspace of H (boundedness of f ensures continuity, continuity ensures the kernel is closed). By the orthogonal decomposition you studied, H splits as ker(f) ⊕ ker(f)^⊥. Since f is not zero, ker(f)^⊥ is at least one-dimensional; pick a unit vector z there. The vector y = f(z)̄ · z does the job: a short calculation confirms f(x) = ⟨x, y⟩ for all x, and uniqueness follows from the fact that two vectors representing the same functional must differ by an element of ker(f) ∩ ker(f)^⊥ = {0}.

The upshot is an **isometric isomorphism** between H and its **dual space** H* (the space of all bounded linear functionals on H). The map y ↦ f_y is bijective and norm-preserving: ‖f_y‖ = ‖y‖. This means you never need to treat H and H* as different objects — they are, in a precise sense, the same space. This is a special feature of Hilbert spaces; for general Banach spaces the dual can be very different from the original space.

The theorem has far-reaching consequences. In quantum mechanics, it justifies identifying "bra" vectors with "ket" vectors in the Dirac formalism. In optimization and variational calculus, it translates problems phrased in terms of functionals back into geometric problems in H itself. For orthonormal bases in Hilbert spaces — the next topic — the Riesz theorem underpins the expansion f(x) = Σ ⟨x, eₙ⟩ eₙ by guaranteeing that the coefficients ⟨x, eₙ⟩ fully encode the action of any bounded functional on the space.
