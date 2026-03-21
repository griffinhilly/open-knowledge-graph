---
id: kernel-and-image
title: Kernel and Image of Linear Transformations
domain: mathematics
course: linear-algebra
prerequisites:
- id: linear-transformation-matrix-representation
  type: hard
- id: rank-nullity-theorem
  type: hard
builds-toward:
- linear-transformations-advanced
- least-squares-approximation
tags:
- kernel
- image
- null-space
- column-space
stage: formal-systems
status: draft
---

# Kernel and Image of Linear Transformations

## Core Idea
The kernel ker(T) = {v : T(v) = 0} is the null space of the matrix A. The image im(T) = {T(v) : v ∈ V} is the column space of A. These subspaces determine when T is injective (ker(T) = {0}) or surjective (im(T) = W). The rank-nullity theorem: dim(ker(T)) + dim(im(T)) = dim(domain).

## How It's Best Learned
Compute kernel by solving Ax = 0 (null space). Find image by identifying pivot columns and their span. Relate geometric intuition: kernel is directions that collapse to zero; image is reachable outputs.

## Questions

```yaml
- question: "A linear transformation T: ℝ⁴ → ℝ³ has a kernel that is a 2-dimensional plane through the origin. What can you conclude about the image of T?"
  type: multiple-choice
  options:
    - "The image is all of ℝ³, since the domain has higher dimension than the codomain"
    - "The image is a 2-dimensional subspace of ℝ³ (a plane through the origin)"
    - "The image is a 1-dimensional subspace of ℝ³ (a line through the origin)"
    - "Nothing can be concluded about the image without computing T explicitly"
  answer: 1
  explanation: "By the rank-nullity theorem: dim(ker T) + dim(im T) = dim(domain). With dim(ker T) = 2 and dim(domain) = 4, we get dim(im T) = 4 − 2 = 2. So the image is a 2-dimensional subspace of ℝ³. Option A is wrong — a larger domain does not guarantee surjectivity. The rank-nullity theorem gives us the image dimension directly from the kernel dimension, with no additional computation needed."

- question: "You've found one solution x₀ to the system Ax = b. The kernel of A is most relevant to:"
  type: multiple-choice
  options:
    - "Whether the system has any solution at all"
    - "How many solutions the system has — once one solution exists, the kernel tells you all others"
    - "Whether b lies in the column space of A"
    - "The dimension of the output space of A"
  answer: 1
  explanation: "Whether Ax = b has any solution at all depends on whether b lies in the image (column space) of A — that's the image's job. But once you know one solution x₀ exists, every other solution has the form x₀ + v where v is in ker(A). If ker(A) = {0}, the solution is unique. If ker(A) has higher dimension, there are infinitely many solutions. The kernel tells you the 'size' of the solution set once you know one exists."

- question: "The image of a linear transformation T: ℝⁿ → ℝᵐ is a subspace of the codomain ℝᵐ, not a subspace of the domain ℝⁿ."
  type: true-false
  answer: true
  explanation: "Correct. The image is {T(v) : v ∈ ℝⁿ} — the set of all outputs. These outputs live in the codomain ℝᵐ. The kernel, by contrast, is a subspace of the domain ℝⁿ — it consists of inputs that map to zero, so it lives in the domain. Keeping this straight is important: the rank-nullity theorem says dim(ker T) + dim(im T) = n, where n is the domain dimension, because both the kernel (domain subspace) and image dimension (capped by both domain and codomain) are constrained by n."

- question: "If T: ℝⁿ → ℝᵐ is injective (ker T = {0}), then T must map onto all of ℝᵐ (T is also surjective)."
  type: true-false
  answer: false
  explanation: "Injectivity and surjectivity are independent properties unless n = m. T: ℝ² → ℝ³ defined by T(x,y) = (x, y, 0) is injective (ker T = {0}) but not surjective (only the xy-plane is reachable). Injectivity means no two inputs share an output; surjectivity means every output is reachable. By rank-nullity, an injective T: ℝⁿ → ℝᵐ has rank n — so T is also surjective only if n = m."

- question: "The rank-nullity theorem states that dim(ker T) + dim(im T) = dim(domain). Why does this imply a fundamental trade-off between what a transformation 'forgets' and what it 'covers'?"
  type: short-answer
  answer: "Because the domain dimension is fixed, increasing the kernel dimension (collapsing more of the domain to zero — 'forgetting' more) must decrease the image dimension (reaching a smaller subspace of the codomain — 'covering' less), and vice versa. A transformation cannot both collapse a large subspace to zero and produce outputs spanning a large subspace — the sum of these two dimensions is constrained to equal the domain dimension."
  explanation: "This trade-off has a concrete consequence: a transformation from ℝ⁴ to ℝ³ that is surjective (covers all of ℝ³, rank = 3) must have a 1-dimensional kernel — it can't avoid losing some information. Conversely, if the kernel is a plane (rank 2), the image is also a plane — it covers less of the codomain. Understanding this trade-off is essential for reasoning about systems of linear equations, least-squares problems, and the geometry of transformations."
```

## Explainer

Every linear transformation T: V → W partitions its input space V into two fundamental subspaces. The **kernel** (also called the null space) is the collection of all vectors that T sends to the zero vector: ker(T) = {v ∈ V : T(v) = 0}. Think of the kernel as the "invisible" part of the domain — everything in it collapses to a single point (the zero vector in W) and leaves no trace in the output. The **image** (also called the column space or range) is the collection of all vectors that T can actually produce: im(T) = {T(v) : v ∈ V}. It answers the question "what outputs are reachable?"

From your prerequisite on matrix representations, you know T corresponds to a matrix A. Computing the kernel means solving the homogeneous system Ax = 0 — exactly the null space computation you've seen before. The image is the span of A's columns: any output T(v) = Av is a linear combination of the columns of A, weighted by the entries of v. So "which outputs are reachable?" is the same as "which vectors lie in the column space of A?"

The kernel determines **injectivity** (one-to-one-ness) of T. If ker(T) = {0} — the only vector sent to zero is zero itself — then T is injective: distinct inputs always produce distinct outputs. If the kernel contains nonzero vectors, then T collapses information: two different inputs (v and v + k, where k is in the kernel) map to the same output. The image determines **surjectivity** (onto-ness): T is surjective if and only if im(T) = W, meaning every vector in the target space is reachable.

The **rank-nullity theorem**, which you've already studied, ties these together with a single equation: dim(ker(T)) + dim(im(T)) = dim(V). The dimension of the kernel is called the **nullity**; the dimension of the image is called the **rank**. This is a conservation law: if T collapses a lot of information (large kernel, high nullity), it can only reach a small subspace of W (low rank). There is a precise trade-off between how much T "forgets" and how much it "covers." For a 3×3 matrix with rank 2, the nullity is 1 — the kernel is a line through the origin, and the image is a plane in ℝ³.
