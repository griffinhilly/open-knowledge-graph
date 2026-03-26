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
stage: expert
status: validated
---

# Riesz Representation Theorem for Hilbert Spaces

## Core Idea
The Riesz representation theorem states that for any bounded linear functional f on a Hilbert space H, there exists a unique y ∈ H such that f(x) = ⟨x, y⟩ for all x. This establishes an isometric isomorphism between H and its dual H*.

## Questions

```yaml
- question: "A bounded linear functional f: H → ℝ is defined on a Hilbert space H. According to the Riesz Representation Theorem, which statement is correct?"
  type: multiple-choice
  options:
    - "f(x) = ⟨x, y⟩ for some y ∈ H, but y may not be unique"
    - "f(x) = ⟨x, y⟩ for a unique y ∈ H, and ‖f‖ = ‖y‖"
    - "This representation holds only when H is finite-dimensional"
    - "f(x) = ‖x‖ · ‖y‖ for some y ∈ H by the Cauchy-Schwarz inequality"
  answer: 1
  explanation: "The theorem guarantees both existence and uniqueness of the representing vector y. Uniqueness follows because if f(x) = ⟨x, y₁⟩ = ⟨x, y₂⟩ for all x, then ⟨x, y₁ − y₂⟩ = 0 for all x, which forces y₁ − y₂ = 0. The norm equality ‖f‖ = ‖y‖ makes the map y ↦ f_y an isometry. Option C is a common mistake: the theorem holds for all Hilbert spaces, finite or infinite-dimensional. Option D confuses the Cauchy-Schwarz bound |⟨x,y⟩| ≤ ‖x‖‖y‖ with the functional itself."

- question: "What makes Hilbert spaces special compared to general Banach spaces regarding their dual?"
  type: multiple-choice
  options:
    - "Hilbert spaces are always finite-dimensional, making their dual trivially equal to themselves"
    - "The norm of a Hilbert space is always defined by an inner product, which forces H ≅ H* isometrically"
    - "Bounded linear functionals only exist on Hilbert spaces, not on general Banach spaces"
    - "Every Banach space is isometrically isomorphic to its dual, just as every Hilbert space is"
  answer: 1
  explanation: "The inner product is the key. The map y ↦ f_y where f_y(x) = ⟨x, y⟩ is an isometric isomorphism from H onto H*. For general Banach spaces X, the dual X* can be a completely different space — for example, the dual of L¹ is L^∞, not L¹. Self-duality is a special feature of Hilbert space geometry, arising because the inner product provides a canonical way to identify vectors with functionals."

- question: "The proof of the Riesz Representation Theorem uses the fact that the kernel of a bounded linear functional is a closed subspace of H."
  type: true-false
  answer: true
  explanation: "True, and this is the pivotal step. Continuity of f (which follows from boundedness) ensures that ker(f) = f⁻¹({0}) is closed. The orthogonal complement ker(f)^⊥ is then non-trivial (since f ≠ 0), and the representing vector y is constructed from a unit vector in ker(f)^⊥. Without closedness, the orthogonal decomposition H = ker(f) ⊕ ker(f)^⊥ would not be valid."

- question: "For any Banach space X, there is typically an isometric isomorphism between X and its dual X*."
  type: true-false
  answer: false
  explanation: "False. Hilbert spaces are self-dual (H ≅ H* isometrically) by the Riesz theorem, but this is special. For Banach spaces the dual can be entirely different. The dual of L^p is L^q where 1/p + 1/q = 1 (for p ≠ 2), so (L^p)* ≅ L^q ≇ L^p when p ≠ 2. The dual of L^1 is L^∞, not L^1. Only for p = 2, where L² is a Hilbert space, does self-duality hold."

- question: "Explain in your own words why the Riesz Representation Theorem implies that a Hilbert space is 'self-dual,' and why this is a special feature not shared by all Banach spaces."
  type: short-answer
  answer: "The Riesz theorem says every bounded linear functional on H has the form f(x) = ⟨x, y⟩ for a unique y ∈ H. This means the map φ: H → H* defined by φ(y) = f_y is a bijection — every element of H gives a functional and every functional comes from an element of H. Since the map is also an isometry (‖f_y‖ = ‖y‖) and conjugate-linear, it is an isometric isomorphism H ≅ H*. This self-duality is special because it requires the rich structure of an inner product. In a general Banach space, the norm does not provide a canonical way to pair vectors with functionals, so X and X* can have completely different structures (e.g., the dual of L¹ is L^∞)."
  explanation: "Intuition: the inner product ⟨·, y⟩ is already a bounded linear functional for every y, and every bounded functional arises this way. So H and H* are in perfect one-to-one correspondence. In Banach spaces without inner products, there is no such built-in pairing, and the dual can look nothing like the original space."
```

## Explainer

From your study of orthogonality and projections, you know that every element of a Hilbert space H can be decomposed relative to closed subspaces, and that the inner product ⟨·, ·⟩ is the fundamental tool for measuring angles and projecting vectors. Fix any vector y ∈ H and define the function f_y(x) = ⟨x, y⟩. This function takes vectors to scalars, is linear (from linearity of the inner product in the first slot), and is bounded — |f_y(x)| ≤ ‖y‖ · ‖x‖ by Cauchy-Schwarz. So every vector y in H produces a bounded linear functional on H. The **Riesz Representation Theorem** says the converse is also true: every bounded linear functional arises this way.

To see why, take any bounded linear functional f: H → ℝ (or ℂ). If f is the zero functional, take y = 0. Otherwise, consider the kernel of f — the set ker(f) = {x : f(x) = 0}. This is a closed subspace of H (boundedness of f ensures continuity, continuity ensures the kernel is closed). By the orthogonal decomposition you studied, H splits as ker(f) ⊕ ker(f)^⊥. Since f is not zero, ker(f)^⊥ is at least one-dimensional; pick a unit vector z there. The vector y = f(z)̄ · z does the job: a short calculation confirms f(x) = ⟨x, y⟩ for all x, and uniqueness follows from the fact that two vectors representing the same functional must differ by an element of ker(f) ∩ ker(f)^⊥ = {0}.

The upshot is an **isometric isomorphism** between H and its **dual space** H* (the space of all bounded linear functionals on H). The map y ↦ f_y is bijective and norm-preserving: ‖f_y‖ = ‖y‖. This means you never need to treat H and H* as different objects — they are, in a precise sense, the same space. This is a special feature of Hilbert spaces; for general Banach spaces the dual can be very different from the original space.

The theorem has far-reaching consequences. In quantum mechanics, it justifies identifying "bra" vectors with "ket" vectors in the Dirac formalism. In optimization and variational calculus, it translates problems phrased in terms of functionals back into geometric problems in H itself. For orthonormal bases in Hilbert spaces — the next topic — the Riesz theorem underpins the expansion f(x) = Σ ⟨x, eₙ⟩ eₙ by guaranteeing that the coefficients ⟨x, eₙ⟩ fully encode the action of any bounded functional on the space.
