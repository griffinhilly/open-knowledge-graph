---
id: higher-order-partial-derivatives
title: Higher-Order Partial Derivatives
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: partial-derivatives
  type: hard
- id: higher-order-derivatives
  type: soft
builds-toward:
- second-partials-test
tags:
- second-order
- mixed-partials
- Clairaut
stage: formal-systems
status: validated
---

# Higher-Order Partial Derivatives

## Core Idea
Higher-order partial derivatives are obtained by differentiating partial derivatives with respect to any variable. The second-order mixed partial ∂²f/∂x∂y means 'differentiate first with respect to y, then with respect to x.' Clairaut's theorem states that if the mixed partials are continuous, the order of differentiation does not matter: ∂²f/∂x∂y = ∂²f/∂y∂x. For functions with continuous second-order partials, there are three distinct second-order derivatives: f_xx, f_yy, and f_xy.

## Common Misconceptions
- ∂²f/∂x∂y means differentiate with respect to y first, then x — the notation is read right to left.
- Clairaut's theorem requires continuity of the mixed partials, not just their existence.
- The Hessian matrix collects all second-order partial derivatives and is symmetric when Clairaut's theorem applies.

## Questions

```yaml
- question: "A student computes ∂²f/∂x∂y for f(x,y) = x³y by differentiating with respect to x first (getting 3x²y, then 3x²), while another student differentiates with respect to y first (getting x³, then 3x²). Both get 3x². The first student concludes: 'The notation ∂²f/∂x∂y means differentiate x first, since x appears first in the denominator.' What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "The notation actually means differentiate with respect to y first, then x; they got the same answer only because Clairaut's theorem applies here"
    - "The student is correct — in Leibniz notation, you differentiate the leftmost variable first"
    - "Clairaut's theorem doesn't apply to polynomials, so both computations are coincidentally correct"
    - "Both computations are invalid — higher-order partials require the limit definition"
  answer: 0
  explanation: "In Leibniz notation, ∂²f/∂x∂y is read right to left: the variable closest to f (rightmost in the denominator, here y) is differentiated first. So the correct interpretation is: differentiate with respect to y, then differentiate the result with respect to x. The two students got the same answer only because f = x³y has continuous mixed partials, so Clairaut's theorem guarantees f_xy = f_yx. The notation convention, however, designates y-first — and for functions where mixed partials are not continuous, the order would matter."

- question: "For a function f(x,y) with continuous second-order partial derivatives, how many *distinct* second-order partial derivatives does it have?"
  type: multiple-choice
  options:
    - "Four — f_xx, f_xy, f_yx, and f_yy are all potentially different"
    - "Two — only the pure second derivatives f_xx and f_yy carry independent information"
    - "Three — f_xx, f_yy, and f_xy, since Clairaut's theorem guarantees f_xy = f_yx"
    - "One — the Hessian determinant summarizes all second-order behavior in a single number"
  answer: 2
  explanation: "When the mixed partial derivatives are continuous, Clairaut's theorem guarantees f_xy = f_yx — so the four formally distinct second-order partial derivatives collapse to three independent ones: f_xx (pure second derivative in x), f_yy (pure second derivative in y), and f_xy = f_yx (the shared mixed partial). All three appear on the Hessian matrix, which is symmetric precisely because of this equality. Option A would be correct for a pathological function where mixed partials are not continuous."

- question: "The Hessian matrix H of a function f(x,y) is generally symmetric."
  type: true-false
  answer: false
  explanation: "The Hessian is symmetric only when Clairaut's theorem applies — that is, when the mixed partial derivatives f_xy and f_yx are continuous. Pathological functions exist where f_xy(0,0) ≠ f_yx(0,0), making the Hessian asymmetric at that point. In practice, virtually every function encountered in applied work has continuous mixed partials (and therefore a symmetric Hessian), but the theorem requires continuity as a hypothesis, not just existence of the mixed partials."

- question: "In Leibniz notation, ∂²f/∂y∂x means: differentiate with respect to y first, then x."
  type: true-false
  answer: false
  explanation: "The notation is read right to left: the variable closest to f in the denominator is differentiated first. In ∂²f/∂y∂x, x is closest to f (rightmost), so you differentiate with respect to x first, then y. This is the opposite of left-to-right reading. The easy mnemonic: peel off variables from right to left, just as you peel off operators in function composition. Note this is also opposite to subscript notation: f_yx means differentiate x first, then y — adding to the confusion between conventions."

- question: "Clairaut's theorem states that mixed partial derivatives are equal when they are continuous. Why does the theorem require *continuity* of the mixed partials — isn't it enough that they simply exist?"
  type: short-answer
  answer: "Existence alone is not sufficient. Pathological functions can be constructed where f_xy(0,0) and f_yx(0,0) both exist but are unequal. Continuity of the mixed partials at a point is what forces the two orders of differentiation to agree. The continuity condition ensures the limiting processes involved in computing f_xy and f_yx interact in a well-behaved way. Without it, the order of differentiation can affect the result."
  explanation: "A classic counterexample is f(x,y) = xy(x²−y²)/(x²+y²) for (x,y) ≠ (0,0), f(0,0) = 0. For this function, f_xy(0,0) = 1 and f_yx(0,0) = −1. Both mixed partials exist at the origin but are unequal — and they are discontinuous there. Clairaut's theorem is not violated because the hypothesis (continuity of the mixed partials) fails at that point. This shows that mere existence is genuinely weaker than continuity in this context."
```

## Explainer

From your work with partial derivatives, you know that ∂f/∂x measures the rate of change of f in the x-direction with y held fixed, and ∂f/∂y does the same in y with x held fixed. Higher-order partial derivatives simply repeat this process: take a partial derivative, and then take a partial derivative of the result. For a function f(x, y), the **second-order partial derivatives** are f_xx (differentiate twice with respect to x), f_yy (twice with respect to y), and the **mixed partial derivatives** f_xy and f_yx (differentiate with respect to one variable, then the other). All four exist whenever f is sufficiently smooth.

The most important warning is about notation. The Leibniz notation ∂²f/∂x∂y is read right to left: differentiate with respect to y first, then differentiate the result with respect to x. In subscript notation, f_xy means differentiate with respect to x first, then y — the opposite convention. Different textbooks use different conventions, so always verify which order is intended. The practical rule: in ∂²f/∂x∂y, the variable closest to f (on the right) is differentiated first. For f(x,y) = x²y³, the computation of ∂²f/∂x∂y goes: ∂f/∂y = 3x²y², then ∂/∂x(3x²y²) = 6xy².

**Clairaut's theorem** is the key result: if the mixed partial derivatives f_xy and f_yx are both continuous at a point, then f_xy = f_yx at that point — the order of differentiation does not matter. For virtually every function encountered in practice, this condition holds everywhere, and you can differentiate in whichever order is computationally easier. The continuity requirement is not merely a technicality: pathological functions exist where f_xy(0,0) ≠ f_yx(0,0), but those functions necessarily have discontinuous mixed partials at the origin. In smooth settings, Clairaut's theorem is essentially always available.

All of the second-order information about f is collected into the **Hessian matrix**: H = [[f_xx, f_xy], [f_xy, f_yy]] (when Clairaut's theorem applies and the off-diagonal entries are equal). The Hessian is the multivariable analogue of the second derivative. Just as f''(a) > 0 tells you a critical point is a local minimum in single-variable calculus, the Hessian's determinant and the sign of f_xx determine whether a critical point of f(x,y) is a local minimum, local maximum, or saddle point — this is the second partials test, your next topic. Mastering the computation of f_xx, f_yy, and f_xy is the prerequisite for that test, making the Hessian the natural destination toward which higher-order partials build.
