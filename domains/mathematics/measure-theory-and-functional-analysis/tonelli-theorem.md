---
id: tonelli-theorem
title: Tonelli's Theorem
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: product-measures-fubini-theorem
  type: hard
tags:
- product-measures
stage: expert
status: draft
---

# Tonelli's Theorem

## Core Idea
Tonelli's theorem extends Fubini's iteration to non-negative measurable functions that may not be integrable, using iterated integrals with values in [0,∞]. It complements Fubini by handling the non-integrable case.

## Questions

```yaml
- question: "You want to compute ∫∫ f(x,y) d(μ×ν) for a function f of indefinite sign by switching the order of integration. What is the correct two-step procedure?"
  type: multiple-choice
  options:
    - "Apply Fubini directly — it always allows switching order as long as f is measurable"
    - "Apply Tonelli to f, then use the result to apply Fubini"
    - "Apply Tonelli to |f| to verify finiteness of the iterated integral, then apply Fubini to f"
    - "Apply Fubini to |f| to check absolute integrability, then apply Tonelli to f"
  answer: 2
  explanation: "The correct strategy is Tonelli first on |f|, then Fubini on f. Tonelli applies to non-negative functions without any integrability precondition — if the iterated integral of |f| is finite, then f is integrable over the product space, and Fubini applies. Option A is wrong because Fubini requires f to be integrable as a precondition — you cannot use it to establish integrability. Option B inverts the roles. Option D confuses the two theorems."

- question: "Why can Tonelli's theorem be applied to a non-negative measurable function even when its integral equals +∞, whereas Fubini's theorem cannot?"
  type: multiple-choice
  options:
    - "Tonelli uses a different definition of the integral that avoids infinity entirely"
    - "Non-negative functions have integrals valued in [0,∞], so iterated integrals are always well-defined — there is no risk of the indeterminate form ∞ − ∞"
    - "Tonelli's theorem only applies when the integral is finite; the statement about +∞ is a misstatement"
    - "Fubini can also handle +∞ integrals, so there is no real difference"
  answer: 1
  explanation: "The key is the sign constraint. For f ≥ 0, every integral is a non-negative extended real number in [0,∞]. Adding or comparing such values never produces the indeterminate form ∞ − ∞, so iterated integrals are always well-defined — even when they diverge. Functions of indefinite sign can produce ∞ − ∞ when integrated, which is why Fubini requires absolute integrability (∫|f| < ∞) as a precondition."

- question: "Tonelli's theorem applies to any non-negative measurable function on a product measure space, even if its double integral is +∞."
  type: true-false
  answer: true
  explanation: "This is exactly Tonelli's scope. For f ≥ 0, the iterated integrals and the double integral are all equal in [0,∞] — finite or infinite — with no integrability precondition. This is what makes Tonelli useful: it applies unconditionally to non-negative functions, allowing you to compute or check integrability by iteration."

- question: "To check whether a function f (of indefinite sign) is integrable over a product space, you should apply Fubini's theorem to f directly."
  type: true-false
  answer: false
  explanation: "Fubini's theorem requires you to *already know* f is integrable — it cannot be used to establish integrability. The correct approach is to apply Tonelli to |f| (which is non-negative and so Tonelli applies unconditionally). If the iterated integral of |f| is finite, then f is integrable, and you can then invoke Fubini. Attempting Fubini first without this check can produce invalid results when f is not actually integrable."

- question: "Explain the 'chicken-and-egg' problem Tonelli solves, and describe the standard two-theorem strategy for computing double integrals of functions with indefinite sign."
  type: short-answer
  answer: "Fubini's theorem lets you switch integration order, but only if you already know the function is integrable. Yet computing the double integral to check integrability seems to require switching the integration order — a circularity. Tonelli breaks this by handling non-negative functions with no precondition: apply Tonelli to |f| to compute the iterated integral; if it is finite, |f| is integrable over the product space. This licenses applying Fubini to f itself for the actual computation."
  explanation: "The two-theorem strategy — Tonelli on |f| to establish integrability, Fubini on f to compute — is one of the most repeated proof patterns in measure theory. Without Tonelli, there would be no principled way to verify the precondition that Fubini requires, making double integrals of indefinite-sign functions difficult to handle rigorously."
```

## Explainer

From Fubini's theorem, you know that double integrals over product spaces can be computed as iterated integrals — integrate one variable at a time, in either order — provided the function is integrable (i.e., ∫∫|f| d(μ×ν) < ∞). But Fubini's theorem requires you to *already know* the function is integrable before you can swap the order of integration. This creates a chicken-and-egg problem: how do you verify integrability without computing the integral, and how do you compute the integral without knowing you can iterate?

**Tonelli's theorem** resolves this by handling **non-negative measurable functions** separately, with no integrability assumption. For f ≥ 0, all integrals are well-defined in [0, ∞] — they either converge to a finite value or diverge to +∞, but they never produce undefined expressions involving ∞ − ∞. Tonelli states: if f: X×Y → [0, ∞] is measurable with respect to the product σ-algebra, then the iterated integrals are equal to the double integral, even if all three equal +∞. Crucially, the iterated integrals equal each other and equal the double integral *without* any finiteness precondition.

The practical power of Tonelli is that it gives you a **strategy for verifying integrability**: to check whether f (not necessarily non-negative) is in L¹(X×Y), apply Tonelli to |f| first. If the iterated integral ∫(∫|f(x,y)| dν(y)) dμ(x) is finite, then |f| is integrable over the product space, and you can then apply Fubini to f itself to compute the integral by iteration. This two-step procedure — Tonelli to establish integrability, then Fubini to compute — is one of the most common patterns in measure theory.

Together, Fubini and Tonelli form a complete toolkit for handling double integrals. Fubini tells you that integration order doesn't matter *when* a function is integrable; Tonelli tells you *how to check* integrability and handles the non-negative case outright. The distinction matters because for functions of indefinite sign that fail to be absolutely integrable, iterated integrals in different orders can yield different finite values — a phenomenon that neither theorem allows for functions in their respective domains. The pairing of the two results is so natural that many texts present them together as "Fubini-Tonelli."
