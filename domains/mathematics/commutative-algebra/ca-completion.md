---
id: ca-completion
title: Completion
domain: mathematics
course: commutative-algebra
prerequisites:
- id: ca-local-rings
  type: hard
- id: ca-noetherian-rings
  type: hard
- id: ca-modules-over-rings
  type: soft
builds-toward: []
tags:
- completion
- i-adic-topology
- hensels-lemma
- formal-power-series
- complete-local-ring
- inverse-limit
stage: expert
status: validated
---

# Completion

## Core Idea
The I-adic completion of a ring R with respect to an ideal I is the inverse limit of the quotients R/I^n, capturing the "formal neighborhood" of V(I). For a local ring (R, m), the m-adic completion R-hat retains the essential algebraic properties of R while gaining powerful analytic-like tools such as Hensel's lemma, which lifts approximate factorizations to exact ones. Completion is the algebraic analogue of passing from polynomials to power series, or from rational numbers to real numbers, and is indispensable in local algebraic geometry and number theory.

## Questions

```yaml
- question: "What is the m-adic completion of the local ring Z_(p) (integers localized at the prime (p))?"
  type: multiple-choice
  options:
    - "The real numbers R"
    - "The p-adic integers Z_p"
    - "The field Q_p of p-adic numbers"
    - "The polynomial ring Z[x]"
  answer: 1
  explanation: "The m-adic completion of Z_(p) with respect to its maximal ideal (p) is the ring of p-adic integers Z_p = lim Z/p^nZ. This is a complete local ring with maximal ideal (p) and residue field F_p. The fraction field of Z_p is Q_p, the p-adic numbers."

- question: "Hensel's lemma allows lifting a factorization of a polynomial modulo m to a factorization over the complete local ring."
  type: true-false
  answer: true
  explanation: "In its multiplicative form, Hensel's lemma states: if R-hat is a complete local ring with residue field k, and f in R-hat[x] is monic with f mod m = g_0 * h_0 where gcd(g_0, h_0) = 1 in k[x], then f = g * h in R-hat[x] with g, h lifting g_0, h_0. This fails for non-complete rings in general."

- question: "Is the natural map R → R-hat (from a Noetherian local ring to its completion) always injective?"
  type: short-answer
  answer: "Yes, by the Krull intersection theorem: the intersection of m^n over all n is zero in a Noetherian local ring whose maximal ideal contains no idempotents (in particular in a local domain)."
  explanation: "The kernel of R → R-hat is the intersection of all powers of m. The Krull intersection theorem states that in a Noetherian ring, this intersection is killed by an element of the form 1 - a with a in I. For a local ring with I = m, the element 1 - a is a unit, so the intersection is zero. Thus R embeds in R-hat."

- question: "The completion of the polynomial ring k[x] at the ideal (x) is the formal power series ring k[[x]]."
  type: true-false
  answer: true
  explanation: "The quotients k[x]/(x^n) are polynomial rings truncated at degree n. The inverse limit of these is exactly k[[x]], the ring of formal power series. Elements of k[[x]] are formal infinite sums a_0 + a_1 x + a_2 x^2 + ..., which is precisely what completion with respect to (x) produces."

- question: "Why does completion preserve the Noetherian property, and why is this important?"
  type: short-answer
  answer: "If R is a Noetherian local ring, its completion R-hat is also Noetherian (and local). This follows from the fact that R-hat/m-hat^n ≅ R/m^n and a careful analysis of ideal generation. It is important because it allows Noetherian techniques (primary decomposition, dimension theory) to be applied in the completed setting."
  explanation: "The key technical result is that faithful flatness of R → R-hat carries Noetherianness upward. Since R-hat is Noetherian, ideals of R-hat are finitely generated, and many questions about R can be reduced to the complete case where Hensel's lemma and the Cohen structure theorem provide extra tools."
```

## Explainer

**Completion** is the algebraic process of formally adjoining limits of Cauchy sequences with respect to an ideal-adic topology. Given a commutative ring R and an ideal I, the **I-adic topology** on R has the powers I^n as a basis of open neighborhoods of 0. The **I-adic completion** is the inverse limit R-hat = lim R/I^n, whose elements are coherent sequences (r_1, r_2, r_3, ...) with r_n in R/I^n and r_n ≡ r_{n+1} mod I^n. The natural map R → R-hat sends each element to the sequence of its residues, and this map is injective when the intersection of all I^n is zero (guaranteed by the Krull intersection theorem in the Noetherian local case).

The most important instance is the **m-adic completion** of a local ring (R, m). The completion R-hat is again a local ring with maximal ideal m-hat (the closure of m) and the same residue field R/m. The completion of k[x]_(x) is the formal power series ring k[[x]]; the completion of Z_(p) is the p-adic integers Z_p. These examples illustrate the general principle: completion replaces "polynomial-like" objects with "power-series-like" objects, gaining convergence properties at the cost of losing finite presentation.

The central payoff of completion is **Hensel's lemma**, which comes in several versions. The simplest: if f(x) is a polynomial over a complete local ring (R, m) and a in R satisfies f(a) ≡ 0 mod m with f'(a) a unit modulo m, then there exists a unique b in R with f(b) = 0 and b ≡ a mod m. The multiplicative version lifts coprime factorizations from the residue field to the complete ring. Hensel's lemma is the algebraic counterpart of Newton's method -- iterative refinement converges because completeness provides the necessary limits. It is the reason p-adic numbers are so powerful in number theory: factorization questions over Z can be reduced to factorization over the residue field F_p, then lifted to Z_p.

The **Cohen structure theorem** classifies complete local rings: every complete Noetherian local ring containing a field is isomorphic to a quotient k[[x_1, ..., x_n]]/I of a formal power series ring. This structure theorem has no analogue for non-complete rings and is one of the main reasons algebraic arguments often proceed by "passing to the completion." Completion is faithfully flat over the original ring, which means many properties (regularity, depth, being Cohen-Macaulay) can be checked after completion. This interplay between a ring and its completion -- reducing hard questions to the complete case where Cohen's theorem and Hensel's lemma provide powerful tools -- is a central technique in commutative algebra and algebraic geometry.
