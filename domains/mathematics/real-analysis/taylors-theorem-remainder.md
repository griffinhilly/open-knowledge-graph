---
id: taylors-theorem-remainder
title: Taylor's Theorem with Remainder
domain: mathematics
course: real-analysis
prerequisites:
- id: mean-value-theorem-rigorous
  type: hard
- id: rigorous-derivative-definition
  type: hard
builds-toward:
- lhopitals-rule-rigorous
tags:
- taylor
- remainder
- polynomial-approximation
stage: advanced
status: draft
---

# Taylor's Theorem with Remainder

## Core Idea
Taylor's Theorem states that a smooth function f can be approximated by a polynomial: f(x) = Pₙ(x) + Rₙ(x), where Pₙ is the n-th Taylor polynomial and Rₙ is a remainder term. Rigorous forms (Lagrange and integral remainders) quantify the approximation error, essential for understanding convergence of Taylor series and deriving error bounds.

## Explainer

From your study of rigorous derivatives, you know that differentiability at a point gives a linear approximation: f(x) ≈ f(a) + f'(a)(x−a). This is the tangent line approximation, accurate to first order near a. Taylor's theorem is the systematic generalization: if you know all derivatives up to order n at a point a, you can build a polynomial that matches f and all its derivatives at a. The **n-th Taylor polynomial** is Pₙ(x) = Σ_{k=0}^{n} f^(k)(a)/k! · (x−a)^k. Taylor's theorem with remainder makes the approximation exact by accounting for the error Rₙ(x) = f(x) − Pₙ(x).

The **Lagrange remainder** gives the most concrete control over the error: Rₙ(x) = f^(n+1)(c)/(n+1)! · (x−a)^(n+1) for some c strictly between a and x. The formula looks exactly like the next term of the Taylor polynomial, but with an unknown intermediate point c substituted in place of a. You cannot compute c, but you can bound it: if |f^(n+1)(t)| ≤ M for all t in the interval between a and x, then |Rₙ(x)| ≤ M/(n+1)! · |x−a|^(n+1). The proof strategy mirrors the Mean Value Theorem (which you know): construct an auxiliary function that vanishes at both endpoints a and x, then apply Rolle's theorem n+1 times in succession to force the (n+1)-th derivative to equal the remainder expression at some intermediate point.

The **integral remainder** gives an alternative representation: Rₙ(x) = 1/n! · ∫_a^x (x−t)^n f^(n+1)(t) dt. This form is harder to compute explicitly but more revealing: the remainder is a weighted average of the (n+1)-th derivative, where the weight (x−t)^n concentrates near x. The Lagrange form is obtained by applying the MVT for integrals to this formula — so the mysterious intermediate point c is precisely where the weighted average is "achieved."

The remainder has two critical applications. First, **error control**: given a target precision ε, choose n large enough so that M/(n+1)! · |x−a|^(n+1) < ε. This is exactly how computational software evaluates sin x, cos x, and eˣ — by truncating their Taylor series and using the remainder bound to verify accuracy. Second, **series convergence**: the infinite Taylor series Σ f^(k)(a)/k! · (x−a)^k converges to f(x) if and only if Rₙ(x) → 0 as n → ∞. For eˣ, sin x, and cos x, the factorial denominator dominates and the remainder vanishes everywhere; for some other functions, the radius of convergence is finite. Taylor's theorem with remainder is thus the bridge between polynomial approximation (which is local and finite) and power series (which are global and infinite) — it tells you precisely when and how far the bridge extends.
