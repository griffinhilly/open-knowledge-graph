---
id: repeated-roots-reduction-of-order
title: Repeated Roots and Reduction of Order
domain: mathematics
course: differential-equations
prerequisites:
- id: characteristic-equation-method
  type: hard
- id: product-rule
  type: hard
builds-toward:
- wronskian-linear-independence
tags:
- repeated-roots
- reduction-of-order
- second-solution
stage: formal-systems
status: draft
---

# Repeated Roots and Reduction of Order

## Core Idea
When the characteristic equation has a repeated root r, one solution is e^(rx), but we need a second linearly independent solution. The reduction-of-order method yields y₂ = x·e^(rx). The general solution is y = (c₁ + c₂x)e^(rx). For higher multiplicities, additional solutions involve higher powers of x. This technique extends beyond repeated roots to finding second solutions from any known solution.

## Questions

```yaml
- question: "The characteristic equation for y'' − 4y' + 4y = 0 has a repeated root r = 2. A student writes the general solution as y = c₁e^(2x) + c₂e^(2x). What is wrong with this answer?"
  type: multiple-choice
  options:
    - "The student should use r = ±2 as two separate roots, giving y = c₁e^(2x) + c₂e^(−2x)"
    - "The two terms are not linearly independent — both are multiples of e^(2x), so this reduces to y = Ce^(2x) with only one free constant, which cannot be a general solution to a second-order ODE"
    - "The exponent should be 4x, not 2x, because the characteristic root must be squared"
    - "This ODE actually has complex roots, not repeated real roots, because the discriminant is negative"
  answer: 1
  explanation: "A general solution to a second-order ODE must have two linearly independent solutions and two free constants. Writing c₁e^(2x) + c₂e^(2x) = (c₁ + c₂)e^(2x) = Ce^(2x) is really just one free constant disguised as two — the terms are proportional and therefore linearly dependent. The characteristic equation only gives one independent solution for a repeated root; the second independent solution xe^(2x) must be found by reduction of order, giving the correct general solution y = (c₁ + c₂x)e^(2x)."

- question: "In the reduction-of-order substitution y₂ = v(x)·e^(rx), after substituting into the ODE and differentiating with the product rule, the terms containing v(x) itself cancel. Why does this cancellation occur?"
  type: multiple-choice
  options:
    - "Because e^(rx) becomes zero when differentiated twice and substituted back"
    - "Because e^(rx) is already a solution to the ODE — when the coefficient of v(x) is collected, it equals exactly the left-hand side of the ODE evaluated at y₁ = e^(rx), which is zero by definition"
    - "Because v(x) is assumed to be a constant throughout the reduction-of-order method"
    - "Because the product rule always eliminates all terms involving the original undifferentiated factor"
  answer: 1
  explanation: "This cancellation is the elegant core of the method. When you substitute y₂ = v(x)·y₁ into the ODE and expand using the product rule, you collect terms in v, v', and v''. The coefficient of v turns out to be exactly y₁'' + py₁' + qy₁ — which equals zero because y₁ is a solution to the ODE. This leaves an equation only in v' and v'', which is a first-order ODE for w = v'. The technique 'reduces the order' by one, making it solvable."

- question: "If the characteristic equation of a second-order linear ODE has two distinct real roots, reduction of order is still needed to find the second independent solution."
  type: true-false
  answer: false
  explanation: "Reduction of order is only needed when the characteristic equation fails to yield two independent solutions — specifically, when there is a repeated root. For two distinct real roots r₁ ≠ r₂, the characteristic equation directly produces two solutions e^(r₁x) and e^(r₂x), which are automatically linearly independent (neither is a constant multiple of the other). The general solution c₁e^(r₁x) + c₂e^(r₂x) is complete without any further work."

- question: "The general solution to a second-order ODE with repeated root r is y = (c₁ + c₂x)e^(rx), and the two basis solutions e^(rx) and xe^(rx) are linearly independent."
  type: true-false
  answer: true
  explanation: "Linear independence means neither solution is a constant multiple of the other. Although both contain the factor e^(rx), the extra factor of x in xe^(rx) prevents proportionality — there is no constant C such that xe^(rx) = C·e^(rx) for all x. This can be confirmed by the Wronskian: W(e^(rx), xe^(rx)) = e^(rx)·(e^(rx) + rxe^(rx)) − rxe^(rx)·e^(rx) = e^(2rx) ≠ 0, confirming independence. The general solution therefore has two genuinely free constants as required."

- question: "Explain why a repeated root in the characteristic equation produces only one solution, and what the reduction-of-order technique does to find the missing second solution."
  type: short-answer
  answer: "The characteristic equation method tries y = e^(rx) and produces a quadratic in r. A repeated root r means the quadratic has only one value of r, yielding one solution e^(rx). No other exponential form e^(sx) works because s would have to equal r. To find the second solution, reduction of order tries y₂ = v(x)·e^(rx) — multiplying the known solution by an unknown function. After substituting and differentiating, the v(x) terms cancel (because e^(rx) already satisfies the ODE), leaving a simpler equation for v'(x). Solving gives v(x) = c₁ + c₂x, so the second independent solution is y₂ = xe^(rx)."
  explanation: "The reduction-of-order technique is more general than just repeated roots — it works for any second-order linear ODE given one known solution, including variable-coefficient equations. The key insight is that knowing one solution lets you 'factor out' its structure and reduce the remaining problem by one order of difficulty."
```

## Explainer

Recall from the characteristic equation method that for a second-order linear ODE y'' + py' + qy = 0, you try y = e^{rx}, substitute in, and get a quadratic equation in r. When that quadratic has two distinct roots r₁ and r₂, you get two independent solutions e^{r₁x} and e^{r₂x} and you're done. But a **repeated root** — when the discriminant is zero and r₁ = r₂ = r — gives only one solution e^{rx} from the characteristic equation, leaving you one solution short of a complete general solution.

The **reduction-of-order** method finds the missing second solution. The idea: if you already know one solution y₁ = e^{rx}, try y₂ = v(x)·y₁ = v(x)·e^{rx} for some unknown function v(x). Substitute y₂ into the ODE and apply the product rule (which you know) to differentiate. The key algebraic miracle is that the terms involving v(x) itself cancel — because y₁ is already a solution — and you're left with an equation only in v' and v''. Setting w = v' reduces this to a first-order ODE for w, which you can solve. For the repeated-root case, you end up with w'' = 0 (after substitution), so w is constant and v(x) = c₁ + c₂x. This gives y₂ = (c₁ + c₂x)e^{rx}, and factoring out c₁e^{rx} (a multiple of y₁) leaves the independent part y₂ = xe^{rx}.

Geometrically, the two solutions e^{rx} and xe^{rx} span a two-dimensional solution space. The factor of x makes them **linearly independent** — neither is a constant multiple of the other — so their linear combination y = (c₁ + c₂x)e^{rx} provides the full family of solutions. You can verify independence using the **Wronskian** (which you'll study next): W(e^{rx}, xe^{rx}) = e^{2rx} ≠ 0, confirming the two solutions are independent.

The reduction-of-order technique is more general than the repeated-root setting. Given *any* known solution y₁ to a second-order linear ODE — whether or not it came from a characteristic equation — you can use the same substitution y₂ = v(x)·y₁ to find a second independent solution. This is particularly valuable for variable-coefficient equations like Euler–Cauchy equations, where you might guess one solution by inspection and need a systematic method to find the second. The pattern of "multiply a known solution by an unknown function, substitute, and watch the equation reduce in order" recurs throughout differential equations and is worth internalizing as a general strategy.
