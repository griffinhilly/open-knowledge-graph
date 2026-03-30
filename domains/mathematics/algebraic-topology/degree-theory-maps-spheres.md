---
id: degree-theory-maps-spheres
title: Degree Theory for Maps of Spheres
domain: mathematics
course: algebraic-topology
prerequisites:
- id: homology-of-spheres
  type: hard
- id: singular-homology-groups
  type: hard
- id: hurewicz-theorem
  type: soft
builds-toward:
- brouwer-fixed-point-theorem-homological
- borsuk-ulam-theorem
- lefschetz-fixed-point-theorem
tags: [algebraic-topology, degree-theory, maps-of-spheres, winding-number]
stage: expert
status: validated
---
# Degree Theory for Maps of Spheres

## Core Idea
The degree of a continuous map f : S^n -> S^n is the integer d such that the induced map f_* : H_n(S^n) -> H_n(S^n) sends the generator [S^n] to d[S^n]. Since H_n(S^n) = Z, f_* is determined by this single integer. The degree classifies maps of spheres up to homotopy (two maps are homotopic if and only if they have the same degree), satisfies deg(g compose f) = deg(g) * deg(f), and has powerful consequences: the antipodal map has degree (-1)^{n+1}, reflections have degree -1, and maps with nonzero degree are surjective.

## Questions

```yaml
- question: "What is the degree of the antipodal map a: S^n → S^n defined by a(x) = -x?"
  type: multiple-choice
  options:
    - "1"
    - "-1"
    - "(-1)^n"
    - "(-1)^{n+1}"
  answer: 3
  explanation: "The antipodal map is the composition of (n+1) reflections, each reflecting one coordinate of R^{n+1}. Each reflection has degree -1 (it reverses the orientation of one axis). Therefore deg(a) = (-1)^{n+1}. For S^1 (n=1): deg = (-1)^2 = 1, which is correct since rotation by π is homotopic to the identity on S^1 (you can continuously rotate). Wait — actually the antipodal map on S^1 sends (cos θ, sin θ) → (-cos θ, -sin θ) = rotation by π, which has degree 1. For S^2 (n=2): deg = (-1)^3 = -1, which is correct since the antipodal map reverses orientation of S^2."

- question: "If f: S^n → S^n has degree 0, then f is homotopic to a constant map."
  type: true-false
  answer: true
  explanation: "A theorem of Hopf states that two continuous maps S^n → S^n are homotopic if and only if they have the same degree. Since a constant map has degree 0 (the induced map on H_n sends [S^n] to 0), any map of degree 0 is homotopic to a constant. Combined with the Hurewicz theorem (π_n(S^n) ≅ H_n(S^n) ≅ Z), this says the homotopy class of f is completely determined by its degree — the single integer deg(f) is a complete homotopy invariant for self-maps of spheres."

- question: "If f: S^n → S^n has no fixed points (f(x) ≠ x for all x), what can you conclude about deg(f)?"
  type: multiple-choice
  options:
    - "deg(f) = 0"
    - "deg(f) = 1"
    - "deg(f) = (-1)^{n+1} (same as the antipodal map)"
    - "deg(f) = -1"
  answer: 2
  explanation: "If f has no fixed points, then f(x) ≠ x for all x, so the line segment from f(x) to -x never passes through the origin (since f(x) and x are distinct unit vectors, f(x) ≠ x implies f(x) and -x are not antipodal in a way that creates the origin issue — actually the correct statement is: t·f(x) + (1-t)·(-x) ≠ 0 because if it were zero, f(x) = x). Therefore H(x,t) = (tf(x) + (1-t)(-x))/|tf(x) + (1-t)(-x)| is a valid homotopy from -x to f(x), so f is homotopic to the antipodal map a(x) = -x, giving deg(f) = (-1)^{n+1}."

- question: "Explain why deg(g ∘ f) = deg(g) · deg(f) for maps f, g: S^n → S^n."
  type: short-answer
  answer: "By functoriality of homology: (g ∘ f)_* = g_* ∘ f_*. The induced map f_*: H_n(S^n) → H_n(S^n) is multiplication by deg(f), and g_* is multiplication by deg(g). Their composition is multiplication by deg(g) · deg(f). Since (g ∘ f)_* is multiplication by deg(g ∘ f), we get deg(g ∘ f) = deg(g) · deg(f). This multiplicativity makes the degree a homomorphism from the monoid of self-maps of S^n (under composition) to the integers (under multiplication)."
  explanation: "This multiplicativity has strong consequences. For instance, if f is a homeomorphism, then f ∘ f^{-1} = id has degree 1, so deg(f) · deg(f^{-1}) = 1, forcing deg(f) = ±1. Homeomorphisms have degree ±1. If deg(f) ≠ 0, then f is surjective (it covers S^n with nonzero 'algebraic multiplicity'). If |deg(f)| > 1, then f maps every point of S^n to at least one other point as well — it 'wraps' the sphere multiple times."

- question: "For n = 1, the degree of a map f: S^1 → S^1 coincides with the classical winding number."
  type: true-false
  answer: true
  explanation: "For S^1, the degree is the induced map on H_1(S^1) ≅ Z. The fundamental class [S^1] is the generator corresponding to one counterclockwise traversal. The map f wraps S^1 around itself some integer number of times, and this integer — the winding number — is exactly deg(f). The homological definition of degree generalizes the winding number from circles to arbitrary-dimensional spheres, providing a unified framework for counting 'how many times a map wraps around its target.'"
```

## Explainer

**Degree theory** assigns an integer to every continuous map f : S^n -> S^n, measuring "how many times f wraps the sphere around itself." Since H_n(S^n) = Z with generator [S^n] (the fundamental class), the induced homomorphism f_* : H_n(S^n) -> H_n(S^n) is multiplication by some integer d. This integer is the **degree** of f, denoted deg(f). It generalizes the classical winding number (for n = 1) to all dimensions and is the most important single invariant of maps between spheres.

The degree has a clean set of properties. **Functoriality** gives deg(g compose f) = deg(g) * deg(f). The identity has degree 1, and constant maps have degree 0. A reflection (negating one coordinate in R^{n+1}) has degree -1, since it reverses the orientation of S^n. The **antipodal map** a(x) = -x is the composition of (n+1) reflections (one for each coordinate), so deg(a) = (-1)^{n+1}. This means the antipodal map is homotopic to the identity when n is odd and has degree -1 when n is even — a key fact underlying the Borsuk-Ulam theorem and the nonexistence of nowhere-vanishing vector fields on even-dimensional spheres.

The **Hopf degree theorem** states that two maps f, g : S^n -> S^n are homotopic if and only if deg(f) = deg(g). In other words, the degree is a **complete homotopy invariant** for self-maps of spheres. Combined with the Hurewicz theorem (pi_n(S^n) = H_n(S^n) = Z), this means the homotopy classes of maps S^n -> S^n are in bijection with the integers, with the degree providing the bijection. Every integer occurs as the degree of some map (e.g., the map z -> z^d on S^1, or its higher-dimensional analogues), so [S^n, S^n] = Z.

Degree theory has far-reaching applications. A map with **nonzero degree** is surjective (it must hit every point of the target sphere with nonzero algebraic multiplicity). This is the key observation in the **Brouwer fixed point theorem**: if f : D^n -> D^n had no fixed point, we could construct a map S^{n-1} -> S^{n-1} of degree 1 that is also a retraction, contradicting degree properties. The **hairy ball theorem** (no nowhere-vanishing continuous tangent vector field on S^{2k}) follows from degree theory: such a vector field would give a homotopy from the identity to the antipodal map, but these have different degrees (1 versus -1) on even-dimensional spheres. The **Borsuk-Ulam theorem** and the computation of the **Lefschetz number** also rely on degree theory as their foundation.

For smooth maps, the degree has an alternative differential-topological characterization: deg(f) = sum of signs of the Jacobian determinant at preimages of a regular value. This connects the homological degree to the analytical notion of local orientation-preserving or orientation-reversing behavior. A map that wraps S^n around S^n d times, covering the target with the same orientation everywhere, has degree d. A map that covers the target with both orientations has degree equal to the algebraic sum. This geometric picture makes the degree intuitive: it counts "signed wrapping."
