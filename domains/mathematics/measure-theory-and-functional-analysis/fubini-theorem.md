---
id: fubini-theorem
title: Fubini's Theorem and Tonelli's Theorem
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: product-measures-definition
  type: hard
- id: lebesgue-integral-general-definition
  type: hard
builds-toward:
- lp-space-completeness-riesz-fischer
tags:
- integration
- fubini-theorem
stage: advanced
status: draft
---

# Fubini's Theorem and Tonelli's Theorem

## Core Idea
Fubini's theorem: for integrable f on X × Y, ∫∫f d(μ⊗ν) = ∫(∫f(x,y) dν(y)) dμ(x). Tonelli's version handles non-negative functions without integrability, allowing interchange of iteration under more general conditions.

## Questions

```yaml
- question: "You want to evaluate ∫∫f(x,y) d(μ⊗ν) by computing the inner integral first with respect to y, then the outer with respect to x. You have not verified that f is integrable. The correct approach is:"
  type: multiple-choice
  options:
    - "Proceed directly — Fubini's theorem allows iterated integration for any measurable f on a product space"
    - "Verify that both component measures are sigma-finite, which is sufficient to apply Fubini to any measurable f"
    - "Apply Tonelli's theorem to |f| first to verify ∫|f| d(μ⊗ν) < ∞, then apply Fubini to f"
    - "Compute both iterated integrals and check that they agree before trusting either result"
  answer: 2
  explanation: "Fubini's theorem requires the integrability hypothesis ∫|f| d(μ⊗ν) < ∞. The standard workflow when this is not known is to apply Tonelli to |f|: since |f| ≥ 0, Tonelli allows iterated integration without the L¹ hypothesis. If ∫(∫|f(x,y)| dν) dμ < ∞, then f is integrable and Fubini applies. Sigma-finiteness (option B) is needed for the product measure construction but does not alone make f integrable. Checking agreement of both orders (option D) doesn't help — non-integrable functions can produce equal iterated integrals that still don't equal the double integral."

- question: "The key reason Fubini's theorem requires ∫|f| d(μ⊗ν) < ∞ is:"
  type: multiple-choice
  options:
    - "To ensure the product measure μ⊗ν assigns finite total measure to X × Y"
    - "Without integrability, swapping the order of iterated integration can yield different values — including disagreement with the double integral over the product space"
    - "To allow Tonelli's theorem to be applied as a preliminary step before Fubini"
    - "To guarantee that the slices f(x, ·) are continuous for μ-almost every x"
  answer: 1
  explanation: "The classic counterexample — a function on [0,1]×[0,1] where ∫(∫f dy) dx ≠ ∫(∫f dx) dy — shows iterated integration can be order-dependent without integrability. Functions with non-integrable positive and negative parts can 'cancel' differently depending on which direction you integrate first. The L¹ condition rules out this pathology: when |f| has finite integral over the product space, positive and negative contributions balance absolutely, making the result order-independent and equal to the double integral."

- question: "For a non-negative measurable function, Tonelli's theorem allows iterated integration in either order even if both iterated integrals are infinite."
  type: true-false
  answer: true
  explanation: "This is the key feature that makes Tonelli useful as a preliminary tool. For f ≥ 0 and σ-finite measures, iterated integration in either order always gives the same result — possibly both +∞. Non-negative functions cannot produce the cancellation pathology requiring Fubini's integrability hypothesis, because there are no negative parts to cancel in order-dependent ways. In practice: apply Tonelli to |f| to verify integrability, then apply Fubini to f itself."

- question: "If both iterated integrals of a function f are finite and equal, Fubini's theorem guarantees that f is integrable over the product space."
  type: true-false
  answer: false
  explanation: "Fubini's theorem is an implication in one direction: integrability of f implies all three quantities (both iterated integrals and the double integral) are equal. It is not a biconditional. There exist non-integrable functions for which both iterated integrals happen to be equal and finite, yet ∫|f| d(μ⊗ν) = ∞. Finite equal iterated integrals do not imply integrability. Tonelli applied to |f| is the correct tool for verifying the L¹ hypothesis."

- question: "What does the existence of a function for which the two iterated integrals depend on the order of integration tell us about why Fubini's theorem requires a proof rather than being a tautology?"
  type: short-answer
  answer: "Such a function demonstrates that iterated integration on a product space is not automatically order-independent — the equality of the two iterated integrals and the double integral is a non-trivial fact that requires conditions. Without integrability, a function with cancelling positive and negative parts can produce different sums depending on which variable is integrated first: the cancellation pattern depends on order. Integrability (finite total variation) prevents this by ensuring positive and negative parts each have finite integral separately, making the result stable across integration orders. The theorem says exactly that integrability is the condition under which all three quantities necessarily agree — a genuine theorem requiring proof, not a definition."
  explanation: "The canonical counterexample on [0,1]×[0,1] defines f so that integrating in one order gives 0 and in the other gives a nonzero value. The mechanism is that f oscillates between large positive and large negative values whose cancellation depends on the order of summation. Integrability (∫|f| < ∞) rules this out by requiring positive and negative parts to be each separately finite, so cancellation is stable regardless of integration order. This is why Fubini is a theorem: it identifies precisely the condition that makes the Lebesgue integral on product spaces coherent."
```

## Explainer

From your work with product measures, you know how to build a measure μ⊗ν on the Cartesian product X × Y from component measures μ and ν, and you know the Lebesgue integral of a function on that product space. **Fubini's theorem** answers the practical question: must you integrate over X × Y as a single inseparable entity, or can you compute the double integral by integrating one variable at a time? The answer, under the right conditions, is that iterated integration always works and always gives the same result regardless of the order.

The key condition in Fubini's theorem is that f must be **integrable** — meaning ∫|f| d(μ⊗ν) < ∞. When this holds, three things are simultaneously true: for μ-almost every x the function y ↦ f(x, y) is ν-integrable; the function x ↦ ∫f(x, y) dν(y) defined almost everywhere is μ-integrable; and the resulting iterated integral equals the double integral. The same holds with the order of x and y reversed. Crucially, Fubini does not merely say the iterated integrals exist — it guarantees they agree with the integral over the product space.

**Tonelli's theorem** is the companion result for non-negative measurable functions, and its role is to let you *verify* integrability when you don't know it in advance. For f ≥ 0, Tonelli allows iterated integration in either order even without the L¹ hypothesis — the iterated integrals are always equal (possibly both infinite). In practice, the two theorems work in tandem: use Tonelli on |f| to confirm it is integrable, then apply Fubini to f itself to switch the order. This combination is the standard tool in measure theory for computing or bounding integrals on product spaces.

Why can the order matter for non-integrable functions? The classic cautionary example is a function on [0,1]×[0,1] that integrates to different values when the order of integration is swapped. Fubini's integrability hypothesis rules these out. The deeper reason is that the product measure μ⊗ν distributes mass uniformly across the product in a way that fails to "see" cancellation between positive and negative parts unless the total variation is finite. This is precisely the L¹ condition. Understanding this failure mode clarifies why Fubini is a theorem requiring proof, not a tautology: the structure of the Lebesgue integral on product spaces is nontrivial, and the theorem says that integrability is exactly what makes everything coherent.
