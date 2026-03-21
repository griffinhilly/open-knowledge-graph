---
id: monotone-convergence-theorem-analysis
title: Monotone Convergence Theorem
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: lebesgue-integral-non-negative
  type: hard
builds-toward:
- fatou-lemma-measure-theory
- dominated-convergence-theorem
tags:
- convergence-theorems
stage: advanced
status: draft
---

# Monotone Convergence Theorem

## Core Idea
If 0 ≤ fₙ ≤ f_{n+1} pointwise for all n and fₙ → f, then ∫fₙ dμ → ∫f dμ. This is the most fundamental convergence theorem for the Lebesgue integral, allowing us to interchange limit and integral under monotonicity.

## Questions

```yaml
- question: "Let fₙ = n · χ_{(0, 1/n)} on [0,1] with Lebesgue measure. The functions are non-negative and fₙ → 0 pointwise (a.e.). A student applies the MCT to conclude ∫fₙ dλ → 0. What is wrong?"
  type: multiple-choice
  options:
    - "Nothing — the MCT applies to any non-negative sequence converging pointwise, and the conclusion is correct"
    - "The sequence is not monotone increasing — MCT requires fₙ ≤ f_{n+1} pointwise, and this sequence fails that condition"
    - "The limit function f = 0 is not measurable, so MCT cannot be applied"
    - "The MCT only applies on finite measure spaces, and [0,1] must be extended to ℝ"
  answer: 1
  explanation: "The MCT requires 0 ≤ f₁ ≤ f₂ ≤ ... monotone pointwise. For this sequence, at x = 1/4: f₁(1/4)=1, f₂(1/4)=2, f₃(1/4)=3, f₄(1/4)=4, f₅(1/4)=0 — the sequence is NOT non-decreasing at every point. In fact ∫fₙ dλ = 1 for all n, so ∫fₙ dλ does not converge to 0. This is the classic counterexample showing why monotonicity is indispensable."

- question: "The Lebesgue integral of a non-negative measurable function f is defined as ∫f dμ = lim ∫sₙ dμ, where sₙ ↑ f is an increasing sequence of simple functions approximating f from below. Why is the MCT essential to this definition?"
  type: multiple-choice
  options:
    - "It guarantees that every non-negative measurable function can be approximated by simple functions, which wouldn't otherwise be possible"
    - "It ensures the integral is always finite, which is required for the definition to make sense"
    - "It guarantees the limit lim ∫sₙ dμ is the same regardless of which approximating sequence is chosen, making the definition consistent"
    - "It proves that simple functions are dense in the space of non-negative measurable functions"
  answer: 2
  explanation: "The definition must be well-defined: ∫f dμ should be a property of f itself, not of a particular approximating sequence. Different choices of sₙ ↑ f yield different sequences of simple-function integrals, and the MCT guarantees they all converge to the same limit. Without this, the integral would be ambiguous. This is why MCT is the constructive engine of Lebesgue integration theory, not merely a convergence result."

- question: "The Monotone Convergence Theorem guarantees that if 0 ≤ f₁ ≤ f₂ ≤ ... converges pointwise to f, then ∫fₙ dμ → ∫f dμ, and this limit is necessarily a finite real number."
  type: true-false
  answer: false
  explanation: "The MCT allows the limit to be +∞. For example, fₙ = χ_{[0,n]} on ℝ with Lebesgue measure: the sequence is increasing, fₙ → χ_{[0,∞)} pointwise, and ∫fₙ dλ = n → ∞ = ∫χ_{[0,∞)} dλ. The MCT applies perfectly, and the conclusion is that both sides equal +∞. The theorem handles the infinite case gracefully — no finiteness assumption is needed."

- question: "A monotone increasing sequence of measurable functions that are not non-negative can fail to satisfy ∫fₙ dμ → ∫f dμ even when fₙ → f pointwise."
  type: true-false
  answer: true
  explanation: "Consider fₙ = −χ_{[n,∞)} on ℝ with Lebesgue measure. The sequence is increasing (fₙ(x) ≤ f_{n+1}(x) for all x) and fₙ → 0 pointwise as n → ∞. But ∫fₙ dλ = −∞ for every n, while ∫0 dλ = 0. The interchange fails catastrophically because mass is lost at infinity. This is why non-negativity is not a technical convenience — it prevents mass from 'escaping' to −∞ and destroying the convergence."

- question: "Why do the non-negativity and monotone increasing conditions in the MCT prevent the 'mass escape' phenomenon that can cause the limit of integrals to differ from the integral of the limit?"
  type: short-answer
  answer: "Non-negativity ensures integrals are non-negative real numbers (or +∞), so the sequence of integrals ∫fₙ dμ is a non-negative, non-decreasing sequence — it converges to a limit in [0, ∞] with no possibility of oscillation or loss. Monotonicity means each new function only adds measure-theoretic 'mass' rather than redistributing it: whatever area is captured under fₙ is still captured under f_{n+1}. This prevents mass from 'escaping' to regions where it wouldn't be counted in the limit, which is the failure mode in examples with negative functions or non-monotone sequences."
  explanation: "The key contrast is with unconstrained limits: a sequence can converge pointwise while concentrating increasing mass near infinity (or near a single point), causing the integrals to diverge even as the pointwise limit is zero (e.g., the 'moving bump' sequence). Monotonicity forbids mass from moving around; non-negativity forbids mass from canceling. Together they guarantee that the Lebesgue integral — defined by approximating from below — can be legitimately exchanged with the pointwise limit."
```

## Explainer

One of the central challenges in integration theory — which you encountered when building the Lebesgue integral for non-negative functions — is determining when you can swap a limit and an integral: ∫(lim fₙ) = lim ∫fₙ. For Riemann integrals, the swap requires uniform convergence, a very stringent condition. The **Monotone Convergence Theorem** (MCT) shows that for the Lebesgue integral, pointwise monotone convergence is enough, making it a far more powerful tool.

The theorem says: if 0 ≤ f₁ ≤ f₂ ≤ f₃ ≤ ... pointwise and fₙ → f pointwise, then ∫fₙ dμ → ∫f dμ (with the limit possibly being +∞). The key insight is that the integrals ∫fₙ form a non-decreasing sequence of non-negative extended real numbers — they converge to a limit in [0, ∞], with no oscillation possible. The Lebesgue integral was built to handle exactly this situation: it measures "area under the curve" by approximating from below with simple functions (finite linear combinations of indicator functions), and monotone convergence means those approximations converge to the right answer without any mass being lost or gained.

A concrete example anchors the intuition. Let fₙ = χ_{[0,n]} on ℝ with Lebesgue measure — the indicator function of the interval [0, n]. The sequence is increasing (fₙ(x) ≤ f_{n+1}(x) everywhere), and fₙ → f = χ_{[0,∞)} pointwise. The integrals are ∫fₙ dλ = n → ∞ = ∫f dλ. The MCT applies, and the conclusion is that both sides are ∞ — the theorem handles infinite limits gracefully without requiring any finiteness assumption.

The MCT is not just a convergence result — it is the constructive engine for the entire Lebesgue integration theory. Any non-negative measurable function f can be approximated from below by an increasing sequence of **simple functions** sₙ ↑ f (this is a standard construction using dyadic approximations). Defining ∫f dμ = lim ∫sₙ dμ is consistent and well-defined precisely because the MCT guarantees the limit exists and is independent of the approximating sequence. Everything built afterward — Fatou's Lemma, the Dominated Convergence Theorem, L^p spaces — relies on this foundation. The non-negativity and monotonicity hypotheses are not just technical conveniences; they are exactly what prevents the mass-escaping behavior that makes unconstrained limits of integrals unreliable.
