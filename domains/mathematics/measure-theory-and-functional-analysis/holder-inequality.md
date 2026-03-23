---
id: holder-inequality
title: Hölder's and Minkowski's Inequalities
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: lp-spaces
  type: hard
builds-toward:
- lp-completeness
tags:
- inequalities
stage: expert
status: validated
---

# Hölder's and Minkowski's Inequalities

## Core Idea
Hölder's inequality states ∫|fg| dμ ≤ ‖f‖ₚ‖g‖_q for conjugate exponents 1/p + 1/q = 1. Minkowski's inequality proves ‖f+g‖ₚ ≤ ‖f‖ₚ + ‖g‖ₚ, establishing that Lᵖ is a normed space.

## Questions

```yaml
- question: "Why is Hölder's inequality needed to prove that ‖f + g‖ₚ ≤ ‖f‖ₚ + ‖g‖ₚ (Minkowski's inequality), rather than just applying the ordinary triangle inequality for integrals?"
  type: multiple-choice
  options:
    - "The ordinary triangle inequality applies to real numbers, not integrals, so a completely new approach is required"
    - "The ordinary triangle inequality gives ∫|f+g|ᵖ ≤ (∫|f|ᵖ + ∫|g|ᵖ), but the pth root then creates a term (∫|f|ᵖ + ∫|g|ᵖ)^(1/p) that does not split into ‖f‖ₚ + ‖g‖ₚ; Hölder's inequality is needed to handle this"
    - "Hölder's inequality is needed only when p = 2; for other values of p, the result is trivial"
    - "Minkowski's inequality is actually equivalent to the triangle inequality for real numbers and needs no further proof"
  answer: 1
  explanation: "The difficulty is that (a + b)^(1/p) ≠ a^(1/p) + b^(1/p) for p > 1, so you cannot simply split the integral and take roots separately. The actual proof factors out |f+g|^(p−1) from ∫|f+g|ᵖ, then applies Hölder's inequality to bound ∫|f+g|^(p−1)|f| and ∫|f+g|^(p−1)|g| in terms of ‖f‖ₚ, ‖g‖ₚ, and ‖f+g‖ₚ^(p−1). The algebra closes because 1/p + 1/q = 1 makes everything balance. Hölder is the essential engine; Minkowski is the payoff."

- question: "Hölder's inequality ∫|fg| dμ ≤ ‖f‖ₚ‖g‖_q is an equality (the bound is sharp) when:"
  type: multiple-choice
  options:
    - "f and g are both square-integrable (both in L²)"
    - "|f|ᵖ and |g|^q are proportional almost everywhere"
    - "f = g almost everywhere"
    - "The measure μ is a probability measure"
  answer: 1
  explanation: "Hölder's inequality comes from integrating Young's inequality ab ≤ aᵖ/p + b^q/q, which is an equality exactly when aᵖ = b^q (i.e., a and b are in a specific proportional relationship). Translating back, the Hölder bound is sharp when |f(x)|ᵖ and |g(x)|^q are proportional a.e. — meaning one function is essentially a scalar multiple of a power of the other. This sharpness characterizes the 'maximally aligned' pair in the Lᵖ–L^q duality and is central to identifying the dual space of Lᵖ."

- question: "Minkowski's inequality ‖f+g‖ₚ ≤ ‖f‖ₚ + ‖g‖ₚ would hold trivially from basic properties of integrals, so Hölder's inequality is not actually needed in its proof."
  type: true-false
  answer: false
  explanation: "This is precisely wrong. The triangle inequality for Lᵖ is far from trivial for p ≠ 1, ∞. The proof for 1 < p < ∞ requires Hölder's inequality in an essential way: after writing |f+g|ᵖ = |f+g|^(p−1)|f+g| ≤ |f+g|^(p−1)(|f|+|g|) and integrating, you must bound ∫|f+g|^(p−1)|f| using Hölder with exponents (p, q) where 1/p + 1/q = 1. The algebra only closes because p − p/q = 1, which is a direct consequence of the conjugacy relation. Remove Hölder and the proof collapses."

- question: "Without Minkowski's inequality, ‖f‖ₚ = (∫|f|ᵖ dμ)^(1/p) would still define a valid norm on Lᵖ, since the positivity and homogeneity axioms are easily verified."
  type: true-false
  answer: false
  explanation: "A norm requires three properties: positivity (‖f‖ₚ = 0 iff f = 0), homogeneity (‖cf‖ₚ = |c|‖f‖ₚ), and the triangle inequality (‖f+g‖ₚ ≤ ‖f‖ₚ + ‖g‖ₚ). The first two are indeed straightforward from the definition. But the triangle inequality — which is exactly Minkowski's inequality — is the non-trivial condition. Without it, ‖·‖ₚ is only a quasi-norm or a functional, not a genuine norm. Minkowski's inequality is the load-bearing result that licenses calling Lᵖ a normed space."

- question: "Explain why Hölder's inequality is called a 'duality' result and how it serves as the engine for proving Minkowski's inequality as a 'convexity' result."
  type: short-answer
  answer: "Hölder's inequality says that a function f in Lᵖ and a function g in L^q (the dual exponent, 1/p + 1/q = 1) can be multiplied and the product is integrable (in L¹): ∫|fg| ≤ ‖f‖ₚ‖g‖_q. This is a duality statement — Lᵖ and L^q are paired spaces, and their product lands in L¹. Minkowski's inequality says Lᵖ is closed under addition (the triangle inequality), which is the convexity statement that makes Lᵖ a normed vector space. The proof of Minkowski uses Hölder by isolating the 'dual' factor |f+g|^(p−1) ∈ L^q and applying Hölder to both ∫|f+g|^(p−1)|f| and ∫|f+g|^(p−1)|g|."
  explanation: "The Lᵖ–L^q duality that Hölder establishes is one of the central structures of functional analysis. It reappears in the identification of the dual space of Lᵖ (for 1 ≤ p < ∞) with L^q, in the Hahn-Banach theorem, and in the definition of weak convergence. Minkowski's inequality is the immediate practical payoff — it makes Lᵖ a normed space — but Hölder's deeper significance is as a statement about the pairing structure between complementary function spaces."
```

## Explainer

From your work on Lᵖ spaces, you know that ‖f‖ₚ = (∫|f|ᵖ dμ)^(1/p) is a candidate norm on equivalence classes of measurable functions. But calling it a norm requires verification: positivity and homogeneity are straightforward, but the triangle inequality — ‖f + g‖ₚ ≤ ‖f‖ₚ + ‖g‖ₚ — is far from obvious. **Hölder's inequality** is the engine that makes **Minkowski's inequality** possible, and together they establish that Lᵖ is a genuine normed space.

Hölder's inequality states ∫|fg| dμ ≤ ‖f‖ₚ‖g‖_q whenever 1/p + 1/q = 1, called **conjugate exponents**. The special case p = q = 2 is the Cauchy-Schwarz inequality, which you may recognize from Euclidean geometry. Hölder extends it to all conjugate pairs. The proof rests on **Young's inequality**: for nonnegative reals a and b, ab ≤ aᵖ/p + b^q/q, which follows from the concavity of the logarithm. The conjugacy condition 1/p + 1/q = 1 is precisely the constraint that makes Young's inequality tight and the Hölder bound sharp — achieved when |f|ᵖ and |g|^q are proportional almost everywhere.

Minkowski's inequality, ‖f + g‖ₚ ≤ ‖f‖ₚ + ‖g‖ₚ, is the triangle inequality in disguise, and its proof is a careful deployment of Hölder. Write |f + g|ᵖ = |f + g|^(p−1)|f + g| ≤ |f + g|^(p−1)(|f| + |g|), integrate, then apply Hölder's inequality to each term with exponent pair (p, q). The algebra closes because p − p/q = 1, which is exactly the consequence of 1/p + 1/q = 1. What looks like computational bookkeeping is actually a tight logical machine driven by the duality between p and q.

The conceptual picture is worth holding: Hölder says you can "multiply" a function in Lᵖ by a function in Lq and the product lands in L¹ — this is a **duality** statement. Minkowski says Lᵖ is closed under addition — this is the **convexity** statement that makes it a normed vector space. Every subsequent result in functional analysis — completeness of Lᵖ (Riesz-Fischer theorem), the identification of the dual of Lᵖ with Lq, the Hahn-Banach theorem applied to Lᵖ — depends on having these genuine norms in hand. Hölder and Minkowski are the load-bearing inequalities for the entire Lᵖ theory.
