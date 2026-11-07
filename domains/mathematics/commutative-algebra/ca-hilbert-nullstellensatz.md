---
id: ca-hilbert-nullstellensatz
title: Hilbert's Nullstellensatz
domain: mathematics
course: commutative-algebra
prerequisites:
  - id: ca-noether-normalization
    type: hard
  - id: ca-prime-and-maximal-ideals
    type: hard
  - id: ca-ideal-operations
    type: soft
  - id: ca-hilbert-basis-theorem
    type: soft
builds-toward:
  - ca-spec-and-zariski-topology
  - ca-krull-dimension
tags: [commutative-algebra, nullstellensatz, algebraic-geometry, maximal-ideals, radical-ideals, affine-varieties]
stage: expert
status: validated
---

# Hilbert's Nullstellensatz

## Core Idea
Hilbert's Nullstellensatz ("theorem of zeros") links ideals in a polynomial ring to the sets of points where polynomials vanish. Let k be an algebraically closed field and R = k[x₁, ..., xₙ]. The weak form says every maximal ideal of R has the form (x₁ - a₁, ..., xₙ - aₙ) for a point (a₁, ..., aₙ) in kⁿ; equivalently, a system of polynomial equations with no common solution generates the unit ideal. The strong form says that if a polynomial f vanishes on the common zero set V(J) of an ideal J, then some power of f lies in J, so I(V(J)) = √J. This sets up an inclusion-reversing bijection between radical ideals of R and algebraic subsets of kⁿ.

## How It's Best Learned
Begin in one variable, where the theorem reduces to the fact that every nonconstant polynomial over k has a root, and see how it fails over ℝ with x² + 1. Prove the weak form from Zariski's lemma (a field that is finitely generated as a k-algebra is a finite extension of k), which follows from Noether normalization. Then derive the strong form with the Rabinowitsch trick of adjoining a new variable y and the polynomial 1 - yf. Use small examples such as J = (x², y) to see why the radical appears.

## Common Misconceptions
- The Nullstellensatz holds over any field. (It needs k algebraically closed; over ℝ the ideal (x² + 1) is maximal in ℝ[x] but has no zeros in ℝ.)
- If f vanishes on V(J), then f is in J. (Only some power of f must be in J; for J = (x²) in k[x], the polynomial x vanishes on V(J) = {0} but x is not in J.)
- Distinct ideals always have distinct zero sets. (J and √J have the same zero set; the correspondence with zero sets is one-to-one only for radical ideals.)

## Questions

```yaml
- question: "Over an algebraically closed field k, which ideals of k[x, y] are maximal?"
  type: multiple-choice
  options:
    - "Exactly the ideals (x - a, y - b) for a, b in k"
    - "Exactly the principal ideals (f) with f irreducible"
    - "Exactly the prime ideals"
    - "Only the ideal (x, y)"
  answer: 0
  explanation: "This is the weak Nullstellensatz: maximal ideals correspond to points of k². An irreducible f generates a prime ideal that is not maximal, since (f) is contained in (x - a, y - b) for any point on the curve f = 0. The zero ideal is prime but not maximal."

- question: "In k[x] with k algebraically closed, let J = (x²). The polynomial x vanishes at every point of V(J) but does not belong to J."
  type: true-false
  answer: true
  explanation: "V(J) = {0}, and x vanishes there. But x is not a multiple of x², so x ∉ J. Its square x² is in J, which matches the strong Nullstellensatz: I(V(J)) = √J = (x)."

- question: "Explain why the Nullstellensatz fails over ℝ using the ideal (x² + y² + 1) in ℝ[x, y]."
  type: short-answer
  answer: "x² + y² + 1 has no real zeros, so its zero set in ℝ² is empty, yet the ideal is proper, not the unit ideal."
  explanation: "Over an algebraically closed field, an empty zero set forces the ideal to contain 1. Over ℝ, a proper ideal can have no zeros, so the link between ideals and zero sets breaks down."

- question: "What is the role of the extra variable in the Rabinowitsch trick?"
  type: short-answer
  answer: "If f vanishes on V(J), then J together with 1 - yf has no common zero in kⁿ⁺¹, so by the weak form 1 lies in J + (1 - yf); substituting y = 1/f and clearing denominators shows some power of f lies in J."
  explanation: "The new variable converts 'f vanishes wherever J does' into 'a system has no solutions,' which is what the weak Nullstellensatz handles. Clearing the denominators 1/fᵐ is what produces the power of f."
```

## Explainer

Algebraic geometry studies the sets of solutions of polynomial equations. For an ideal J in R = k[x₁, ..., xₙ], let V(J) be the set of points in kⁿ where every polynomial in J vanishes. For a set X of points, let I(X) be the ideal of all polynomials that vanish on X. The Nullstellensatz, due to David Hilbert, describes exactly how these two operations relate when k is algebraically closed, for example k = ℂ.

The weak Nullstellensatz. Every maximal ideal of R has the form (x₁ - a₁, ..., xₙ - aₙ). Equivalently, if J ≠ R, then V(J) is nonempty. In plain terms, a system of polynomial equations has a solution unless the equations can be combined, with polynomial coefficients, to give 1 = 0. In one variable this is the fact that every nonconstant polynomial has a root in k.

The proof rests on Zariski's lemma. If m is a maximal ideal, then R/m is a field that is finitely generated as a k-algebra. Noether normalization shows such a field is a finite, hence algebraic, extension of k. Since k is algebraically closed, R/m = k. Each xᵢ then equals some aᵢ modulo m, so m contains (x₁ - a₁, ..., xₙ - aₙ). That ideal is already maximal, so the two are equal.

The strong Nullstellensatz. For any ideal J, I(V(J)) = √J, the set of f with fᵐ ∈ J for some m. One inclusion is easy: if fᵐ vanishes on V(J), so does f. For the other, suppose f vanishes on V(J). In n + 1 variables, the ideal generated by J and 1 - yf has no zeros, since at any zero of J we have f = 0 and 1 - yf = 1. By the weak form, 1 = Σ gᵢhᵢ + g(1 - yf) with hᵢ ∈ J. Substituting y = 1/f and multiplying through by a high power of f shows fᵐ ∈ J.

The result is a dictionary. Radical ideals of R correspond one-to-one with algebraic subsets of kⁿ, larger ideals giving smaller sets. Prime ideals correspond to irreducible sets, and maximal ideals correspond to points. The hypothesis on k matters. Over ℝ, the ideal (x² + 1) is maximal in ℝ[x], yet x² + 1 has no real root.

This correspondence motivates defining Spec R as the set of prime ideals with the Zariski topology. Through Noether normalization, it also ties the Krull dimension of R/J to the geometric dimension of V(J).
