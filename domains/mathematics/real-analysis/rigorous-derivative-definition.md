---
id: rigorous-derivative-definition
title: Rigorous Definition of the Derivative
domain: mathematics
course: real-analysis
prerequisites:
- id: epsilon-delta-continuity
  type: hard
- id: limit-laws
  type: soft
builds-toward:
- mean-value-theorem-rigorous
- taylors-theorem-remainder
- interchange-limit-derivative
tags:
- derivative
- definition
- rigor
stage: advanced
status: draft
---

# Rigorous Definition of the Derivative

## Core Idea
The derivative f'(c) is defined rigorously as lim_{h→0} [f(c+h) - f(c)]/h, where the limit is in the ε-δ sense: for every ε > 0, there exists δ > 0 such that |h| < δ (h ≠ 0) implies |[f(c+h) - f(c)]/h - f'(c)| < ε. This definition generalizes to higher dimensions and abstract spaces, making it the standard in modern analysis.

## Explainer

You already know the ε-δ definition of a limit and continuity. The derivative is built directly on top of those ideas — it is simply the limit of a specific expression called the **difference quotient**. The expression [f(c+h) − f(c)] / h computes the slope of the secant line through the points (c, f(c)) and (c+h, f(c+h)). As h → 0, these two points move together and the secant line approaches the tangent line. The derivative f'(c) is the number this slope converges to — if it converges at all.

The ε-δ formulation unpacks what "converges" means precisely. Saying f'(c) = L means: for every ε > 0, there exists δ > 0 such that whenever 0 < |h| < δ, the difference quotient is within ε of L. This is the same ε-δ machinery you used for continuity, now applied to the function g(h) = [f(c+h) − f(c)] / h at h = 0. Notice that g is only defined for h ≠ 0 — we never actually evaluate h = 0 in the limit. This is why we write 0 < |h| < δ rather than just |h| < δ. The rigor forces you to track that the value at h = 0 is irrelevant; only the approach matters.

Why bother with the ε-δ formulation when the intuitive picture is clear? Because intuition fails at corners, cusps, and pathological functions. Consider f(x) = |x| at x = 0. The difference quotient is h/|h|, which equals +1 for h > 0 and −1 for h < 0. There is no single number L that the quotient approaches, so f is not differentiable at 0 — the ε-δ definition reveals this automatically. Similarly, there exist functions that are continuous everywhere but differentiable nowhere (the Weierstrass function), a fact that shocked 19th-century mathematicians and that requires the rigorous definition to even state precisely.

The formal definition also generalizes cleanly. In higher dimensions, the analogous definition replaces h with a vector **h** ∈ ℝⁿ and requires that the ratio [f(**x** + **h**) − f(**x**) − L(**h**)] / ‖**h**‖ → 0 as ‖**h**‖ → 0, where L is now a linear map — the **total derivative** or Fréchet derivative. In abstract normed spaces, the same structure applies. The one-variable ε-δ definition is therefore not just a pedantic restatement of calculus; it is the template for the entire edifice of modern analysis. Mastering it here means every generalization you encounter later will feel like a familiar pattern rather than a new idea.
