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

## Questions

```yaml
- question: "Consider f(x) = |x| at x = 0. What does the difference quotient [f(0+h) − f(0)]/h equal, and what does this imply about differentiability?"
  type: multiple-choice
  options:
    - "It equals 0 for all small h, so f'(0) = 0"
    - "It equals +1 for h > 0 and −1 for h < 0, so the limit does not exist and f is not differentiable at 0"
    - "It equals 1 for all small h because |h|/h → 1 as h → 0"
    - "The limit is 0 because f is continuous at 0, and continuity implies differentiability"
  answer: 1
  explanation: "For h > 0, [|0+h| − |0|]/h = h/h = 1. For h < 0, [|0+h| − |0|]/h = (−h)/h = −1. There is no single value L that the difference quotient approaches from both sides — the left-hand and right-hand limits disagree. The ε-δ definition therefore correctly concludes that f is not differentiable at 0. This is the corner in the graph of |x|: geometrically, no unique tangent line exists at x = 0."

- question: "In the ε-δ definition of the derivative, the condition is written as 0 < |h| < δ (with a strict lower bound). Why is the strict inequality 0 < |h| necessary?"
  type: multiple-choice
  options:
    - "Because the difference quotient [f(c+h) − f(c)]/h is undefined at h = 0, so we must exclude it from the limit"
    - "To ensure the secant line has positive slope"
    - "To make the definition consistent with the continuity definition, which also uses strict inequalities"
    - "Because δ itself must be strictly positive, which forces |h| to be positive as well"
  answer: 0
  explanation: "Division by h = 0 is undefined — the difference quotient does not exist at h = 0. In a limit, we ask what value the expression *approaches* as h → 0, but we never evaluate h = 0 itself. The strict inequality 0 < |h| precisely encodes this: we consider all h that are close to 0 but nonzero. This is the same reason all ε-δ limit definitions exclude the point itself — a limit describes approach behavior, not the value at the point."

- question: "If a function f is continuous at c, then f is necessarily differentiable at c."
  type: true-false
  answer: false
  explanation: "Continuity is necessary but not sufficient for differentiability. f(x) = |x| is continuous everywhere (no jumps or gaps) but is not differentiable at x = 0 because the difference quotient has different left and right limits. More strikingly, the Weierstrass function is continuous at every point on ℝ but differentiable at no point. The existence of such functions was historically shocking — intuition about smoothness fails dramatically for continuous functions in general."

- question: "The difference quotient [f(c+h) − f(c)]/h represents the slope of the secant line through the points (c, f(c)) and (c+h, f(c+h)) on the graph of f."
  type: true-false
  answer: true
  explanation: "This is the geometric interpretation of the difference quotient: it is the rise [f(c+h) − f(c)] divided by the run [h], which is exactly the slope of the line connecting the two points. As h → 0, the second point approaches the first and the secant line approaches the tangent line. The derivative is the slope of this limiting tangent — if the limit exists."

- question: "Why is the ε-δ formulation of the derivative more than a formal restatement of 'slope of the tangent line'? What does the rigorous definition reveal that geometric intuition alone misses?"
  type: short-answer
  answer: "Geometric intuition works for smooth curves but fails at corners, cusps, and pathological functions. The ε-δ definition automatically detects non-differentiability: for |x| at 0, the difference quotient approaches +1 from the right and −1 from the left, so no L satisfies the ε-δ criterion. It also proves the existence of continuous-everywhere-differentiable-nowhere functions (Weierstrass), which are geometrically inconceivable by intuition. Furthermore, the ε-δ structure generalizes cleanly to the Fréchet derivative in ℝⁿ and abstract normed spaces, whereas the tangent-line picture does not."
  explanation: "The real-analysis approach is not pedantry — it provides the machinery to handle all the ways functions can fail to be differentiable, and it provides the template for analysis in higher dimensions. Every generalization of calculus to multivariable and functional settings builds on this same ε-δ limit structure."
```

## Explainer

You already know the ε-δ definition of a limit and continuity. The derivative is built directly on top of those ideas — it is simply the limit of a specific expression called the **difference quotient**. The expression [f(c+h) − f(c)] / h computes the slope of the secant line through the points (c, f(c)) and (c+h, f(c+h)). As h → 0, these two points move together and the secant line approaches the tangent line. The derivative f'(c) is the number this slope converges to — if it converges at all.

The ε-δ formulation unpacks what "converges" means precisely. Saying f'(c) = L means: for every ε > 0, there exists δ > 0 such that whenever 0 < |h| < δ, the difference quotient is within ε of L. This is the same ε-δ machinery you used for continuity, now applied to the function g(h) = [f(c+h) − f(c)] / h at h = 0. Notice that g is only defined for h ≠ 0 — we never actually evaluate h = 0 in the limit. This is why we write 0 < |h| < δ rather than just |h| < δ. The rigor forces you to track that the value at h = 0 is irrelevant; only the approach matters.

Why bother with the ε-δ formulation when the intuitive picture is clear? Because intuition fails at corners, cusps, and pathological functions. Consider f(x) = |x| at x = 0. The difference quotient is h/|h|, which equals +1 for h > 0 and −1 for h < 0. There is no single number L that the quotient approaches, so f is not differentiable at 0 — the ε-δ definition reveals this automatically. Similarly, there exist functions that are continuous everywhere but differentiable nowhere (the Weierstrass function), a fact that shocked 19th-century mathematicians and that requires the rigorous definition to even state precisely.

The formal definition also generalizes cleanly. In higher dimensions, the analogous definition replaces h with a vector **h** ∈ ℝⁿ and requires that the ratio [f(**x** + **h**) − f(**x**) − L(**h**)] / ‖**h**‖ → 0 as ‖**h**‖ → 0, where L is now a linear map — the **total derivative** or Fréchet derivative. In abstract normed spaces, the same structure applies. The one-variable ε-δ definition is therefore not just a pedantic restatement of calculus; it is the template for the entire edifice of modern analysis. Mastering it here means every generalization you encounter later will feel like a familiar pattern rather than a new idea.
