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

## Explainer

Recall from the characteristic equation method that for a second-order linear ODE y'' + py' + qy = 0, you try y = e^{rx}, substitute in, and get a quadratic equation in r. When that quadratic has two distinct roots r₁ and r₂, you get two independent solutions e^{r₁x} and e^{r₂x} and you're done. But a **repeated root** — when the discriminant is zero and r₁ = r₂ = r — gives only one solution e^{rx} from the characteristic equation, leaving you one solution short of a complete general solution.

The **reduction-of-order** method finds the missing second solution. The idea: if you already know one solution y₁ = e^{rx}, try y₂ = v(x)·y₁ = v(x)·e^{rx} for some unknown function v(x). Substitute y₂ into the ODE and apply the product rule (which you know) to differentiate. The key algebraic miracle is that the terms involving v(x) itself cancel — because y₁ is already a solution — and you're left with an equation only in v' and v''. Setting w = v' reduces this to a first-order ODE for w, which you can solve. For the repeated-root case, you end up with w'' = 0 (after substitution), so w is constant and v(x) = c₁ + c₂x. This gives y₂ = (c₁ + c₂x)e^{rx}, and factoring out c₁e^{rx} (a multiple of y₁) leaves the independent part y₂ = xe^{rx}.

Geometrically, the two solutions e^{rx} and xe^{rx} span a two-dimensional solution space. The factor of x makes them **linearly independent** — neither is a constant multiple of the other — so their linear combination y = (c₁ + c₂x)e^{rx} provides the full family of solutions. You can verify independence using the **Wronskian** (which you'll study next): W(e^{rx}, xe^{rx}) = e^{2rx} ≠ 0, confirming the two solutions are independent.

The reduction-of-order technique is more general than the repeated-root setting. Given *any* known solution y₁ to a second-order linear ODE — whether or not it came from a characteristic equation — you can use the same substitution y₂ = v(x)·y₁ to find a second independent solution. This is particularly valuable for variable-coefficient equations like Euler–Cauchy equations, where you might guess one solution by inspection and need a systematic method to find the second. The pattern of "multiply a known solution by an unknown function, substitute, and watch the equation reduce in order" recurs throughout differential equations and is worth internalizing as a general strategy.
