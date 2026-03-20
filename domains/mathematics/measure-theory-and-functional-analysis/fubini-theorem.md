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

## Explainer

From your work with product measures, you know how to build a measure μ⊗ν on the Cartesian product X × Y from component measures μ and ν, and you know the Lebesgue integral of a function on that product space. **Fubini's theorem** answers the practical question: must you integrate over X × Y as a single inseparable entity, or can you compute the double integral by integrating one variable at a time? The answer, under the right conditions, is that iterated integration always works and always gives the same result regardless of the order.

The key condition in Fubini's theorem is that f must be **integrable** — meaning ∫|f| d(μ⊗ν) < ∞. When this holds, three things are simultaneously true: for μ-almost every x the function y ↦ f(x, y) is ν-integrable; the function x ↦ ∫f(x, y) dν(y) defined almost everywhere is μ-integrable; and the resulting iterated integral equals the double integral. The same holds with the order of x and y reversed. Crucially, Fubini does not merely say the iterated integrals exist — it guarantees they agree with the integral over the product space.

**Tonelli's theorem** is the companion result for non-negative measurable functions, and its role is to let you *verify* integrability when you don't know it in advance. For f ≥ 0, Tonelli allows iterated integration in either order even without the L¹ hypothesis — the iterated integrals are always equal (possibly both infinite). In practice, the two theorems work in tandem: use Tonelli on |f| to confirm it is integrable, then apply Fubini to f itself to switch the order. This combination is the standard tool in measure theory for computing or bounding integrals on product spaces.

Why can the order matter for non-integrable functions? The classic cautionary example is a function on [0,1]×[0,1] that integrates to different values when the order of integration is swapped. Fubini's integrability hypothesis rules these out. The deeper reason is that the product measure μ⊗ν distributes mass uniformly across the product in a way that fails to "see" cancellation between positive and negative parts unless the total variation is finite. This is precisely the L¹ condition. Understanding this failure mode clarifies why Fubini is a theorem requiring proof, not a tautology: the structure of the Lebesgue integral on product spaces is nontrivial, and the theorem says that integrability is exactly what makes everything coherent.
