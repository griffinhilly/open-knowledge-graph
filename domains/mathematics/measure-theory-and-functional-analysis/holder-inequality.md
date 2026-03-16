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
stage: advanced
status: draft
---

# Hölder's and Minkowski's Inequalities

## Core Idea
Hölder's inequality states ∫|fg| dμ ≤ ‖f‖ₚ‖g‖_q for conjugate exponents 1/p + 1/q = 1. Minkowski's inequality proves ‖f+g‖ₚ ≤ ‖f‖ₚ + ‖g‖ₚ, establishing that Lᵖ is a normed space.

## Explainer

From your work on Lᵖ spaces, you know that ‖f‖ₚ = (∫|f|ᵖ dμ)^(1/p) is a candidate norm on equivalence classes of measurable functions. But calling it a norm requires verification: positivity and homogeneity are straightforward, but the triangle inequality — ‖f + g‖ₚ ≤ ‖f‖ₚ + ‖g‖ₚ — is far from obvious. **Hölder's inequality** is the engine that makes **Minkowski's inequality** possible, and together they establish that Lᵖ is a genuine normed space.

Hölder's inequality states ∫|fg| dμ ≤ ‖f‖ₚ‖g‖_q whenever 1/p + 1/q = 1, called **conjugate exponents**. The special case p = q = 2 is the Cauchy-Schwarz inequality, which you may recognize from Euclidean geometry. Hölder extends it to all conjugate pairs. The proof rests on **Young's inequality**: for nonnegative reals a and b, ab ≤ aᵖ/p + b^q/q, which follows from the concavity of the logarithm. The conjugacy condition 1/p + 1/q = 1 is precisely the constraint that makes Young's inequality tight and the Hölder bound sharp — achieved when |f|ᵖ and |g|^q are proportional almost everywhere.

Minkowski's inequality, ‖f + g‖ₚ ≤ ‖f‖ₚ + ‖g‖ₚ, is the triangle inequality in disguise, and its proof is a careful deployment of Hölder. Write |f + g|ᵖ = |f + g|^(p−1)|f + g| ≤ |f + g|^(p−1)(|f| + |g|), integrate, then apply Hölder's inequality to each term with exponent pair (p, q). The algebra closes because p − p/q = 1, which is exactly the consequence of 1/p + 1/q = 1. What looks like computational bookkeeping is actually a tight logical machine driven by the duality between p and q.

The conceptual picture is worth holding: Hölder says you can "multiply" a function in Lᵖ by a function in Lq and the product lands in L¹ — this is a **duality** statement. Minkowski says Lᵖ is closed under addition — this is the **convexity** statement that makes it a normed vector space. Every subsequent result in functional analysis — completeness of Lᵖ (Riesz-Fischer theorem), the identification of the dual of Lᵖ with Lq, the Hahn-Banach theorem applied to Lᵖ — depends on having these genuine norms in hand. Hölder and Minkowski are the load-bearing inequalities for the entire Lᵖ theory.
