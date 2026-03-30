---
id: brouwer-fixed-point-theorem-homological
title: Brouwer Fixed Point Theorem (Homological Proof)
domain: mathematics
course: algebraic-topology
prerequisites:
- id: degree-theory-maps-spheres
  type: hard
- id: relative-homology-long-exact-sequence
  type: soft
- id: singular-homology-groups
  type: hard
builds-toward:
- lefschetz-fixed-point-theorem
tags: [algebraic-topology, brouwer-fixed-point, applications, degree-theory]
stage: expert
status: validated
---
# Brouwer Fixed Point Theorem (Homological Proof)

## Core Idea
The Brouwer fixed point theorem states that every continuous map f : D^n -> D^n has a fixed point: there exists x in D^n with f(x) = x. The homological proof proceeds by contradiction: if f had no fixed point, we could construct a retraction r : D^n -> S^{n-1} = boundary(D^n), but no such retraction exists because it would force the identity on H_{n-1}(S^{n-1}) = Z to factor through H_{n-1}(D^n) = 0. This argument showcases how algebraic topology converts a geometric claim into an algebraic impossibility.

## Questions

```yaml
- question: "The key step in the homological proof of Brouwer's theorem is showing that no retraction r: D^n → S^{n-1} exists. What algebraic contradiction does a retraction produce?"
  type: multiple-choice
  options:
    - "It would make H_n(D^n) nonzero"
    - "The composition S^{n-1} →^i D^n →^r S^{n-1} would be the identity, forcing id_*: H_{n-1}(S^{n-1}) → H_{n-1}(S^{n-1}) to factor through H_{n-1}(D^n) = 0, which means id = 0 on Z — a contradiction"
    - "It would make π_1(D^n) non-trivial"
    - "It would violate the excision theorem"
  answer: 1
  explanation: "If r: D^n → S^{n-1} is a retraction (r ∘ i = id where i: S^{n-1} ↪ D^n), then on homology: r_* ∘ i_* = id_* on H_{n-1}. But i_*: H_{n-1}(S^{n-1}) → H_{n-1}(D^n) has target H_{n-1}(D^n) = 0 (since D^n is contractible), so i_* = 0, and r_* ∘ i_* = r_* ∘ 0 = 0. But id_* on H_{n-1}(S^{n-1}) ≅ Z is the identity, not zero. Contradiction. Therefore no retraction exists."

- question: "The Brouwer fixed point theorem fails for open disks — there exist continuous maps from the open disk to itself with no fixed points."
  type: true-false
  answer: true
  explanation: "The open disk is homeomorphic to all of R^n, and the translation map x ↦ x + (1,0,...,0) on R^n has no fixed points. The Brouwer theorem requires the domain to be the CLOSED disk D^n, which is compact. Compactness is essential: the retraction argument uses the fact that S^{n-1} is the boundary of D^n and that D^n is contractible while S^{n-1} has nontrivial homology. The open disk is also contractible but has no boundary in the relevant sense."

- question: "How does one construct the hypothetical retraction r: D^n → S^{n-1} from a fixed-point-free map f: D^n → D^n?"
  type: short-answer
  answer: "For each x ∈ D^n, since f(x) ≠ x, consider the ray starting at f(x) and passing through x. This ray hits the boundary sphere S^{n-1} at a unique point r(x). Formally, r(x) = x + t(x - f(x)) where t ≥ 0 is chosen so |r(x)| = 1. This map r is continuous (because f is continuous and the ray direction varies continuously) and satisfies r(x) = x for x ∈ S^{n-1} (since the ray from f(x) through x, with x already on the boundary, hits the boundary at x). So r is a retraction of D^n onto S^{n-1}."
  explanation: "The geometric picture is clear: for each interior point x, draw a ray from f(x) through x and extend it to the boundary. If x is on the boundary, the ray starts at f(x) (which is in the interior since the map goes D^n → D^n) and passes through x, which is already on the boundary — so r(x) = x. The no-fixed-point assumption ensures f(x) ≠ x, so the ray direction is well-defined."

- question: "The Brouwer fixed point theorem can be proved using the fundamental group for n = 2 but requires homology for n ≥ 3."
  type: true-false
  answer: false
  explanation: "The fundamental group proof works for n = 2 (the retraction r: D^2 → S^1 would give a surjection r_*: π_1(D^2) → π_1(S^1), but π_1(D^2) = 0 and π_1(S^1) = Z, contradiction). However, this argument does NOT work for n = 3: π_1(D^3) = π_1(S^2) = 0, so the fundamental group sees no contradiction. The homological proof works uniformly in all dimensions by using H_{n-1}(S^{n-1}) = Z and H_{n-1}(D^n) = 0. The statement in the question is wrong because the fundamental group proof works for n = 2 (via π_1) but fails to even address n ≥ 3 — it's not that it 'requires' homology for large n, but that only homology provides a uniform proof."
```

## Explainer

The **Brouwer fixed point theorem** is one of the most famous results in topology, with applications across mathematics, economics (Nash equilibrium), and physics. The statement is simple: every continuous map from the closed n-disk D^n to itself has at least one fixed point. The proof using homology is clean, elegant, and illustrates the "algebraic topology method" perfectly: assume the conclusion fails, derive an algebraic consequence, and show the algebraic consequence is impossible.

The proof has two steps. **Step 1**: show that if f : D^n -> D^n has no fixed point, then there exists a retraction r : D^n -> S^{n-1} (a continuous map that is the identity on S^{n-1}). Construction: for each x in D^n, since f(x) != x, the ray from f(x) through x is well-defined and intersects S^{n-1} at a unique point r(x). When x is already on S^{n-1}, the ray from f(x) through x hits the boundary at x itself (since f(x) is in D^n, which is "behind" x relative to the outward direction). So r is the identity on S^{n-1}, making it a retraction.

**Step 2**: show that no retraction D^n -> S^{n-1} can exist. If r : D^n -> S^{n-1} is a retraction and i : S^{n-1} hookrightarrow D^n is the inclusion, then r compose i = id on S^{n-1}. On homology: r_* compose i_* = id_* on H_{n-1}(S^{n-1}) = Z. But i_* : H_{n-1}(S^{n-1}) -> H_{n-1}(D^n), and H_{n-1}(D^n) = 0 (since D^n is contractible), so i_* is the zero map. Therefore r_* compose i_* = 0, but id_* is the identity on Z. The identity on Z is not the zero map. Contradiction.

This proof is a paradigm of the algebraic topology method. The original problem (existence of a fixed point) is a statement about continuous maps between geometric objects. Algebraic topology translates it into a statement about group homomorphisms (the identity on Z cannot factor through the zero group), which is obviously true. The "hard work" is done by the homology functor: it converts the geometric situation (no retraction exists) into an algebraic impossibility (a nonzero map cannot factor through zero). The proof works uniformly in all dimensions, unlike approaches based on the fundamental group (which only work in dimension 2) or on smooth approximation and Sard's theorem (which require more technical machinery).

The Brouwer theorem generalizes in several directions. The **Lefschetz fixed point theorem** replaces the disk with any compact polyhedron and gives a numerical criterion (the Lefschetz number) for the existence of fixed points. The **Schauder fixed point theorem** extends Brouwer to infinite-dimensional convex compact sets in Banach spaces. In economics, the Brouwer theorem (via its close relative, the Kakutani fixed point theorem) is the key ingredient in proving the existence of Nash equilibria in game theory. In numerical analysis, the Brouwer theorem guarantees the existence of solutions to certain systems of nonlinear equations. The homological proof not only establishes the theorem but explains WHY it is true: the disk has the "wrong" homology to admit a retraction onto its boundary.
