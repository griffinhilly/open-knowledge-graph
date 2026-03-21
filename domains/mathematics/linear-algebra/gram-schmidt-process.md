---
id: gram-schmidt-process
title: Gram-Schmidt Orthogonalization Process
domain: mathematics
course: linear-algebra
prerequisites:
- id: orthogonal-vectors-orthonormal-bases
  type: hard
builds-toward:
- least-squares-approximation
tags:
- gram-schmidt
- orthogonalization
- basis
stage: formal-systems
status: draft
---

# Gram-Schmidt Orthogonalization Process

## Core Idea
The Gram-Schmidt process converts any basis into an orthonormal basis by iterative orthogonalization: orthogonalize each vector against all previous ones. Starting with v₁, compute u_k = v_k − Σ_{j<k} ⟨v_k, e_j⟩e_j and normalize. The process yields an orthonormal basis spanning the same space.

## Questions

```yaml
- question: "You apply Gram-Schmidt to a basis {v₁, v₂, v₃}. After computing e₁ (normalized v₁), you form u₂ = v₂ − ⟨v₂, e₁⟩e₁. What is guaranteed about u₂ before normalization?"
  type: multiple-choice
  options:
    - "u₂ has unit length"
    - "u₂ is perpendicular to e₁"
    - "u₂ lies in a different subspace than v₂"
    - "u₂ equals v₂ rotated exactly 90 degrees around the origin"
  answer: 1
  explanation: "The step u₂ = v₂ − ⟨v₂, e₁⟩e₁ subtracts from v₂ exactly its component in the e₁ direction (the projection). Computing ⟨u₂, e₁⟩ = ⟨v₂, e₁⟩ − ⟨v₂, e₁⟩⟨e₁, e₁⟩ = ⟨v₂, e₁⟩ − ⟨v₂, e₁⟩ = 0 confirms orthogonality. u₂ is not yet normalized (that comes next), does not 'rotate' v₂ (it changes direction by subtraction), and stays in the same span as v₁ and v₂."

- question: "After applying Gram-Schmidt to three basis vectors of a plane in ℝ⁴, a student claims the resulting orthonormal vectors now describe a different plane because they point in different directions than the originals. Is this correct?"
  type: multiple-choice
  options:
    - "Yes — Gram-Schmidt rotates the basis to align with coordinate axes, changing which plane is described"
    - "No — Gram-Schmidt only changes how the plane is described (the basis), not the plane itself; the orthonormal vectors span exactly the same subspace as the originals"
    - "Yes — normalization rescales the vectors, which alters the geometry of what they span"
    - "No — but only if the original basis vectors were already mutually orthogonal"
  answer: 1
  explanation: "This is the crucial invariant of Gram-Schmidt: the subspace spanned does not change. At each step, uₖ = vₖ − (projections onto previous vectors) is a linear combination of vₖ and the earlier basis vectors — so it lies in the span of {v₁, …, vₖ}. The orthonormal set {e₁, …, eₖ} therefore spans the same k-dimensional subspace as {v₁, …, vₖ}. You are changing the *representation* of the space, not the space itself."

- question: "Gram-Schmidt changes the subspace being described because the resulting orthonormal vectors are not parallel to the original basis vectors."
  type: true-false
  answer: false
  explanation: "The direction of individual basis vectors changes, but the subspace spanned — the set of all linear combinations — does not. Because each new orthonormal vector is a linear combination of the original vectors (and vice versa), the two sets span exactly the same subspace. Gram-Schmidt is a change of basis within a fixed subspace, not a change of subspace."

- question: "If two of the original basis vectors are already orthogonal to each other, the Gram-Schmidt projection step between them will produce a zero projection, leaving those vectors unchanged up to normalization."
  type: true-false
  answer: true
  explanation: "If v₂ is already perpendicular to e₁, then ⟨v₂, e₁⟩ = 0, so the subtraction step u₂ = v₂ − 0·e₁ = v₂ leaves v₂ unchanged. Gram-Schmidt 'discovers' that no projection needs to be removed. This is correct behavior — the algorithm handles the already-orthogonal case gracefully and the only remaining step is normalization."

- question: "Explain the geometric meaning of 'subtracting the projection' in a Gram-Schmidt step. Why does subtracting the projection of vₖ onto e₁ guarantee that the result is perpendicular to e₁?"
  type: short-answer
  answer: "The projection ⟨vₖ, e₁⟩·e₁ is the component of vₖ in the direction of e₁ — its 'shadow' onto e₁. When you subtract this shadow, you remove everything vₖ shares with the e₁ direction, leaving only the part that is perpendicular to e₁. Algebraically: ⟨vₖ − ⟨vₖ, e₁⟩e₁, e₁⟩ = ⟨vₖ, e₁⟩ − ⟨vₖ, e₁⟩·⟨e₁, e₁⟩ = ⟨vₖ, e₁⟩ − ⟨vₖ, e₁⟩ = 0. The dot product is zero, confirming orthogonality."
  explanation: "This geometric intuition — project, then subtract the projection — is why Gram-Schmidt works. The projection captures exactly how much of vₖ 'points in the e₁ direction'; subtracting it leaves the remainder pointing purely perpendicular. Repeating for each previous direction strips out all overlap with the established basis, guaranteeing the new vector is orthogonal to all of them."
```

## Explainer

You already know what an **orthonormal basis** is: a set of basis vectors that are mutually perpendicular (orthogonal) and each has length 1 (unit vectors). Working in an orthonormal basis makes calculations dramatically simpler — projections reduce to dot products, coordinates are just inner products, and many matrix algorithms become numerically stable. The Gram-Schmidt process is the algorithm for building such a basis starting from any ordinary basis you happen to have.

The key geometric idea is **projection and subtraction**. Suppose you have two vectors, v₁ and v₂, that are not perpendicular. Take v₁ as your first basis vector (just normalize it to get e₁). Now, v₂ points in some direction that has a component *along* e₁ and a component *perpendicular* to e₁. The component along e₁ is the projection: proj = ⟨v₂, e₁⟩ · e₁. If you subtract that projection from v₂, you get a new vector that is perpendicular to e₁ by construction — you've stripped out everything v₂ shared with the e₁ direction. Normalize what's left and you have e₂. Two orthonormal vectors, done.

The process extends by induction. For the k-th vector vₖ, subtract away its projection onto *every* basis vector already computed: uₖ = vₖ − ⟨vₖ, e₁⟩e₁ − ⟨vₖ, e₂⟩e₂ − … − ⟨vₖ, e_{k−1}⟩e_{k−1}. Each subtraction removes the component of vₖ that overlaps with a previously established direction, leaving a remainder that is perpendicular to all of them. Normalize this remainder to get eₖ. Crucially, the resulting orthonormal set spans exactly the same subspace as the original vectors — you haven't changed *what* space you're describing, only *how* you're describing it.

This process has a matrix factorization interpretation: Gram-Schmidt on the columns of a matrix A produces the **QR decomposition**, A = QR, where Q has orthonormal columns and R is upper triangular. The QR decomposition is one of the workhorses of numerical linear algebra — it underlies the standard algorithm for computing eigenvalues and is the basis of stable least-squares solvers. When you later study least-squares approximation, you'll see that the orthogonal projections Gram-Schmidt builds are exactly the geometry behind finding the best-fit solution when a system has no exact answer.
