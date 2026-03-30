---
id: ca-local-rings
title: Local Rings
domain: mathematics
course: commutative-algebra
prerequisites:
- id: ca-localization
  type: hard
- id: maximal-prime-ideals
  type: hard
builds-toward:
- ca-nakayama-lemma
- ca-going-up-going-down
- ca-krull-dimension
- ca-completion
- ca-regular-local-rings
tags:
- local-ring
- unique-maximal-ideal
- residue-field
- localization-at-prime
stage: expert
status: validated
---

# Local Rings

## Core Idea
A local ring is a commutative ring with exactly one maximal ideal. The elements outside this maximal ideal are precisely the units. Local rings arise naturally from localizing any ring at a prime ideal, and they represent the algebraic analog of "zooming in on a single point" in geometry. Working locally simplifies many problems because the ideal structure collapses to a single chain above the maximal ideal.

## Questions

```yaml
- question: "Which of the following is a local ring?"
  type: multiple-choice
  options:
    - "ℤ, because (0) is its only prime ideal"
    - "k[x]/(x²), because its only maximal ideal is (x̄) and every element not in (x̄) is a unit"
    - "ℤ/6ℤ, because it has only finitely many ideals"
    - "k[x, y], because (x, y) is a maximal ideal"
  answer: 1
  explanation: "In k[x]/(x²), an element a + bx̄ is a unit if and only if a ≠ 0 (since (a + bx̄)(a⁻¹ - ba⁻²x̄) = 1). The non-units are exactly multiples of x̄, which form the ideal (x̄). Since (x̄) is the unique maximal ideal, k[x]/(x²) is local. ℤ has infinitely many maximal ideals (2), (3), (5), .... ℤ/6ℤ has two maximal ideals (2̄) and (3̄). k[x,y] has maximal ideals (x-a, y-b) for each (a,b), so it is not local."

- question: "A commutative ring R is local if and only if the set of non-units forms an ideal."
  type: multiple-choice
  options:
    - "This is true and the ideal of non-units is automatically the unique maximal ideal"
    - "This is false — the non-units can form an ideal without the ring being local"
    - "This is true but only for Noetherian rings"
    - "This is false — in any ring, the non-units form an ideal"
  answer: 0
  explanation: "If the non-units form an ideal 𝔪, then 𝔪 is the unique maximal ideal: any ideal consisting entirely of non-units is contained in 𝔪, and 𝔪 itself is proper (it doesn't contain 1). Conversely, if R has a unique maximal ideal 𝔪, every non-unit lies in some maximal ideal, which must be 𝔪. So the non-units are exactly 𝔪. This clean characterization is often the most useful definition of a local ring."

- question: "The localization of ℤ at the prime ideal (p) is a local ring with residue field 𝔽_p."
  type: true-false
  answer: true
  explanation: "ℤ₍ₚ₎ consists of fractions a/b with p ∤ b. The unique maximal ideal is pℤ₍ₚ₎ = {a/b : p | a, p ∤ b}. The residue field is ℤ₍ₚ₎/pℤ₍ₚ₎ ≅ ℤ/pℤ = 𝔽_p, because modding out by pℤ₍ₚ₎ kills exactly multiples of p and inverts everything else, leaving a copy of the finite field with p elements."

- question: "Every field is a local ring."
  type: true-false
  answer: true
  explanation: "In a field, every nonzero element is a unit, so the only non-unit is 0. The set of non-units is {0} = (0), which is the unique maximal ideal. The residue field is k/(0) ≅ k itself. Fields are the 'trivial' local rings — their unique maximal ideal is as small as possible."

- question: "Explain why localization at a prime ideal always produces a local ring, and what geometric intuition this corresponds to."
  type: short-answer
  answer: "If 𝔭 is a prime of R and S = R \\ 𝔭, then S⁻¹R = R_𝔭 has prime ideals corresponding to primes of R contained in 𝔭. The ideal 𝔭R_𝔭 is the unique maximal ideal because 𝔭 is the largest prime contained in itself. Any element outside 𝔭R_𝔭 has the form a/s with a ∉ 𝔭, so a ∈ S and a/s is a unit in R_𝔭."
  explanation: "Geometrically, Spec(R) is a space whose points are prime ideals. Localizing at 𝔭 'zooms in' to an infinitesimal neighborhood of 𝔭, discarding all geometric information about other points. The resulting local ring R_𝔭 captures the local geometry at 𝔭 — smoothness, singularity type, tangent directions — while ignoring the global structure. This is why local rings are the algebraic analog of germs of functions in differential geometry."
```

## Explainer

A **local ring** is a commutative ring with exactly one maximal ideal, traditionally denoted (R, 𝔪). Equivalently, the set of non-units forms an ideal — which is then automatically the unique maximal ideal. The quotient k = R/𝔪 is a field called the **residue field**. Local rings are the algebraic structures that describe "what happens at a single point," and most of commutative algebra operates by reducing questions to the local case.

The most important source of local rings is **localization at a prime ideal**. If 𝔭 is a prime ideal of R, then R_𝔭 = S⁻¹R (where S = R \ 𝔭) is a local ring with maximal ideal 𝔭R_𝔭. For example, ℤ₍₅₎ consists of fractions a/b where 5 does not divide b, and its unique maximal ideal is 5ℤ₍₅₎. In this ring, 2, 3, 7, and all primes other than 5 become units (they are invertible), and the only "interesting" arithmetic is divisibility by 5. The residue field is ℤ₍₅₎/5ℤ₍₅₎ ≅ 𝔽₅.

Local rings also arise as quotients and completions. The ring k[x]/(x²) — the "dual numbers" over k — is local with maximal ideal (x̄). It has a single "infinitesimal direction" represented by x̄, with x̄² = 0. In algebraic geometry, this ring describes the first-order neighborhood of a point, and maps from Spec(k[x]/(x²)) into a variety represent tangent vectors. The power series ring k[[x]] is a complete local ring with maximal ideal (x), modeling the "formal" neighborhood of a point.

The power of local rings comes from the **local-global principle**: many module-theoretic properties (being zero, being free, being finitely generated) can be checked locally — that is, after localizing at every maximal ideal. Since localizations at maximal ideals are local rings, this reduces questions about general rings to questions about local rings. In the local setting, you have tools like Nakayama's lemma, the structure theory of regular local rings, and completion, none of which are available globally. This is why the passage from global to local is the most common first move in commutative algebra.
