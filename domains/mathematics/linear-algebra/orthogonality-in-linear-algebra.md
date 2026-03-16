---
id: orthogonality-in-linear-algebra
title: Orthogonality
domain: mathematics
course: linear-algebra
prerequisites:
- id: inner-product-spaces
  type: hard
builds-toward:
- orthonormal-bases
- orthogonal-projections
tags:
- orthogonal
- perpendicular
- orthogonal complement
- orthogonal set
stage: formal-systems
status: validated
---

# Orthogonality

## Core Idea
Two vectors u and v in an inner product space are orthogonal if ⟨u,v⟩ = 0. A set of vectors is orthogonal if every pair of distinct vectors in the set is orthogonal, and orthonormal if additionally each vector has unit norm. Orthogonal sets are automatically linearly independent (assuming no zero vectors). The orthogonal complement of a subspace W is the set of all vectors orthogonal to every vector in W; this complement is itself a subspace, and V = W ⊕ W⊥ (direct sum decomposition). Orthogonality is the key geometric tool behind projections and the Gram-Schmidt process.

## How It's Best Learned
Verify orthogonality using dot products in R² and R³ before generalizing. Compute orthogonal complements of lines and planes in R³ by setting up dot product equations. Note that W⊥⊥ = W (taking the complement twice returns the original subspace).

## Common Misconceptions
- Orthogonal does not mean 'in the direction of the axes'; it means perpendicular in the inner product sense.
- Orthogonal sets are linearly independent, but independent sets are NOT necessarily orthogonal.
- In R³, the orthogonal complement of a plane is a line and vice versa — dimension always satisfies dim(W) + dim(W⊥) = n.

## Explainer

From inner product spaces, you know the inner product ⟨u, v⟩ generalizes the notion of a dot product: it measures a kind of "alignment" between two vectors. When the inner product of two vectors equals zero, they are perfectly unaligned — there is no component of one in the direction of the other. This is the definition of **orthogonality**: u and v are orthogonal if ⟨u, v⟩ = 0. In ℝ² and ℝ³ with the standard dot product, this reduces to the familiar right-angle condition. But in more abstract inner product spaces — spaces of functions, for example — orthogonality still makes precise sense even when "right angle" has no visual meaning.

A collection of vectors is called an **orthogonal set** if every pair of distinct vectors in it is orthogonal. The important consequence is that orthogonal sets (containing no zero vector) are automatically linearly independent. Here is the argument: if Σᵢ cᵢvᵢ = 0 with the vᵢ mutually orthogonal, take the inner product of both sides with any particular vⱼ. Every cross term ⟨vᵢ, vⱼ⟩ vanishes by orthogonality, leaving only cⱼ‖vⱼ‖² = 0, so cⱼ = 0. This works for every j, proving independence. The argument is short, but it is worth internalizing: orthogonality *implies* independence, but independence *does not imply* orthogonality.

The **orthogonal complement** W⊥ of a subspace W is the collection of all vectors in the ambient space that are orthogonal to every vector in W. In ℝ³, the orthogonal complement of a line through the origin is a plane through the origin (perpendicular to that line), and the orthogonal complement of a plane is a line. The key dimension formula always holds: dim(W) + dim(W⊥) = n, where n is the dimension of the full space. This means the two subspaces together account for all of V: every vector x can be written uniquely as x = w + w⊥ where w ∈ W and w⊥ ∈ W⊥. This is the **direct sum decomposition** V = W ⊕ W⊥.

That direct sum decomposition is not just a bookkeeping fact — it is the foundation for orthogonal projection. The component w in the decomposition x = w + w⊥ is the orthogonal projection of x onto W: the closest point in W to x. When W is spanned by a single unit vector e, this projection is simply ⟨x, e⟩ · e. The residual w⊥ = x − w is orthogonal to W by construction. This is the geometry behind least-squares problems, Fourier series, and the Gram-Schmidt algorithm — all of which rely on decomposing vectors into components inside and outside a subspace.

One subtlety worth noting: W⊥⊥ = W (taking the complement twice returns the original subspace), which confirms that orthogonal complementation is a perfect involution on subspaces. Also, the intersection W ∩ W⊥ contains only the zero vector: a vector orthogonal to itself satisfies ⟨v, v⟩ = ‖v‖² = 0, which forces v = 0. These properties make orthogonality an unusually clean and well-behaved geometric structure — one that the Gram-Schmidt process exploits by systematically building an orthogonal (or orthonormal) basis for any subspace.
