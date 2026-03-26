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
status: validated
---

# Taylor's Theorem with Remainder

## Core Idea
Taylor's Theorem states that a smooth function f can be approximated by a polynomial: f(x) = Pₙ(x) + Rₙ(x), where Pₙ is the n-th Taylor polynomial and Rₙ is a remainder term. Rigorous forms (Lagrange and integral remainders) quantify the approximation error, essential for understanding convergence of Taylor series and deriving error bounds.

## Questions

```yaml
- question: "A student wants to approximate e^0.1 using the Taylor series centered at 0, with error below 0.0001. She knows |f⁽ⁿ⁺¹⁾(t)| ≤ 2 for all t ∈ [0, 0.1]. Using the Lagrange remainder, what must she find?"
  type: multiple-choice
  options:
    - "The smallest n such that 2/(n+1)! · (0.1)ⁿ⁺¹ < 0.0001"
    - "The smallest n such that 2ⁿ⁺¹/(n+1)! < 0.0001, ignoring the (x−a) factor"
    - "She should use n = 4 because the fifth derivative of eˣ equals eˣ ≈ 1"
    - "She must use n = ∞ because only the full Taylor series is exact"
  answer: 0
  explanation: "The Lagrange remainder bound is |Rₙ(x)| ≤ M/(n+1)! · |x−a|ⁿ⁺¹, where M bounds |f⁽ⁿ⁺¹⁾| on the interval and x−a = 0.1. She needs to find n so this bound is below 0.0001. Option B forgets to include the crucial (0.1)ⁿ⁺¹ factor, which shrinks rapidly and makes the bound tighter. Option D is the key misconception: the remainder theorem tells you exactly when a finite polynomial gives sufficient accuracy — the whole point is to avoid needing infinitely many terms."

- question: "For f(x) = sin x and its Taylor series centered at 0, the series converges to sin x for all x. What does Taylor's theorem with remainder tell you about Rₙ(x) as n → ∞?"
  type: multiple-choice
  options:
    - "Rₙ(x) = 0 for some sufficiently large finite n"
    - "Rₙ(x) → 0 as n → ∞, which is exactly what it means for the series to converge to sin x"
    - "The (n+1)-th derivative of sin x must vanish, forcing Rₙ to zero"
    - "Rₙ(x) converges to a constant correction term that the series approximates away"
  answer: 1
  explanation: "Taylor's theorem with remainder makes this precise: the Taylor series Σ f⁽ᵏ⁾(a)/k! · (x−a)ᵏ converges to f(x) if and only if Rₙ(x) → 0 as n → ∞. For sin x, the (n+1)-th derivative is bounded by 1 in absolute value, so |Rₙ(x)| ≤ |x|ⁿ⁺¹/(n+1)! → 0 for every x (factorials dominate any fixed power). Option A is wrong: the series is infinite — no finite truncation is exact. This equivalence between series convergence and remainder decay is the main theoretical payoff of Taylor's theorem."

- question: "The Lagrange remainder Rₙ(x) looks exactly like the (n+1)-th term of the Taylor polynomial, except that the derivative is evaluated at an unknown intermediate point c between a and x rather than at a."
  type: true-false
  answer: true
  explanation: "This is precisely right. The n-th Taylor polynomial has terms f⁽ᵏ⁾(a)/k! · (x−a)ᵏ. The Lagrange remainder is f⁽ⁿ⁺¹⁾(c)/(n+1)! · (x−a)ⁿ⁺¹ for some c ∈ (a, x). Structurally it is the next Taylor term, but with the derivative evaluated at the intermediate point c instead of a. You cannot find c explicitly, but you can bound f⁽ⁿ⁺¹⁾ over the interval to get a concrete error bound without knowing c."

- question: "If a smooth function f has a Taylor series that converges for most x, then the series necessarily converges to f(x)."
  type: true-false
  answer: false
  explanation: "This is a subtle but important falsehood. A function can be smooth (have derivatives of all orders everywhere) and have a convergent Taylor series that converges to the wrong value — or converges to f(x) only at the center. The canonical example is f(x) = e^{−1/x²} (defined as 0 at x = 0): all its derivatives at 0 are 0, so its Taylor series is identically 0, converging everywhere — but not to f(x) for x ≠ 0. Taylor's theorem with remainder identifies the actual condition: the series converges to f(x) at x if and only if Rₙ(x) → 0 as n → ∞."

- question: "Why isn't it sufficient to know that a function has derivatives of all orders and a convergent Taylor series to conclude the series equals the function? What condition does Taylor's theorem with remainder actually require?"
  type: short-answer
  answer: "The condition is that the remainder Rₙ(x) → 0 as n → ∞. A convergent Taylor series is just a convergent series of numbers — it is not guaranteed to converge to f(x) unless the remainder vanishes in the limit. Taylor's theorem with remainder identifies precisely this gap: f(x) = Pₙ(x) + Rₙ(x), and the series converges to f(x) exactly when the error Rₙ(x) disappears as we take more terms."
  explanation: "This distinction between 'the Taylor series converges' and 'the Taylor series converges to f' is what distinguishes real analysis from naive calculus. In calculus courses, students often assume these are the same. The Lagrange remainder provides the tool to verify the stronger condition: if you can show |Rₙ(x)| ≤ M/(n+1)! · |x−a|ⁿ⁺¹ → 0, you have genuinely proven the series represents the function — not just that an infinite sum exists."
```

## Explainer

From your study of rigorous derivatives, you know that differentiability at a point gives a linear approximation: f(x) ≈ f(a) + f'(a)(x−a). This is the tangent line approximation, accurate to first order near a. Taylor's theorem is the systematic generalization: if you know all derivatives up to order n at a point a, you can build a polynomial that matches f and all its derivatives at a. The **n-th Taylor polynomial** is Pₙ(x) = Σ_{k=0}^{n} f^(k)(a)/k! · (x−a)^k. Taylor's theorem with remainder makes the approximation exact by accounting for the error Rₙ(x) = f(x) − Pₙ(x).

The **Lagrange remainder** gives the most concrete control over the error: Rₙ(x) = f^(n+1)(c)/(n+1)! · (x−a)^(n+1) for some c strictly between a and x. The formula looks exactly like the next term of the Taylor polynomial, but with an unknown intermediate point c substituted in place of a. You cannot compute c, but you can bound it: if |f^(n+1)(t)| ≤ M for all t in the interval between a and x, then |Rₙ(x)| ≤ M/(n+1)! · |x−a|^(n+1). The proof strategy mirrors the Mean Value Theorem (which you know): construct an auxiliary function that vanishes at both endpoints a and x, then apply Rolle's theorem n+1 times in succession to force the (n+1)-th derivative to equal the remainder expression at some intermediate point.

The **integral remainder** gives an alternative representation: Rₙ(x) = 1/n! · ∫_a^x (x−t)^n f^(n+1)(t) dt. This form is harder to compute explicitly but more revealing: the remainder is a weighted average of the (n+1)-th derivative, where the weight (x−t)^n concentrates near x. The Lagrange form is obtained by applying the MVT for integrals to this formula — so the mysterious intermediate point c is precisely where the weighted average is "achieved."

The remainder has two critical applications. First, **error control**: given a target precision ε, choose n large enough so that M/(n+1)! · |x−a|^(n+1) < ε. This is exactly how computational software evaluates sin x, cos x, and eˣ — by truncating their Taylor series and using the remainder bound to verify accuracy. Second, **series convergence**: the infinite Taylor series Σ f^(k)(a)/k! · (x−a)^k converges to f(x) if and only if Rₙ(x) → 0 as n → ∞. For eˣ, sin x, and cos x, the factorial denominator dominates and the remainder vanishes everywhere; for some other functions, the radius of convergence is finite. Taylor's theorem with remainder is thus the bridge between polynomial approximation (which is local and finite) and power series (which are global and infinite) — it tells you precisely when and how far the bridge extends.
