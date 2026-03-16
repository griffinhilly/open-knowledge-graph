---
id: solving-quadratics-by-factoring
title: Solving Quadratics by Factoring
domain: mathematics
course: algebra-1
prerequisites:
  - id: factoring-completely
    type: hard
  - id: solving-multi-step-equations
    type: hard
builds-toward:
  - quadratic-formula
  - graphing-quadratics
tags: [quadratics, factoring, zero-product-property, solving]
stage: abstract-reasoning
status: validated
---

# Solving Quadratics by Factoring

## Core Idea
The zero product property states: if ab = 0, then a = 0 or b = 0 (or both). This allows us to solve quadratic equations by factoring. First, set the equation equal to zero. Then factor. Then set each factor equal to zero and solve. For x² − 5x + 6 = 0, factor to get (x − 2)(x − 3) = 0, giving x = 2 or x = 3. Quadratic equations can have 0, 1, or 2 real solutions. This method only works when the quadratic can be factored over the integers — for others, the quadratic formula is needed.

## How It's Best Learned
Emphasize the critical first step: the equation must be set equal to zero before factoring. Practice the full sequence — rearrange, factor, apply zero product property, solve each factor, check. Include quadratics where students must first distribute or combine terms. Verify solutions by substitution. Connect to graphing — the solutions are the x-intercepts of the parabola.

## Common Misconceptions
- Factoring without first setting the equation to zero (e.g., solving x² − 5x = −6 as x(x − 5) = −6 and then setting x = −6 or x − 5 = −6).
- Finding only one solution when there are two.
- Forgetting that x² = 0 gives x = 0 as a solution (not "no solution").

## Explainer

From your work with factoring, you know how to break a polynomial like x² − 5x + 6 into factors (x − 2)(x − 3). Solving quadratics by factoring uses that skill to answer a new question: for which x-values does the polynomial equal zero? The key is the **zero product property**: if two quantities multiply to zero, at least one of them must be zero. This is the only time multiplication guarantees a factor is zero, and it's why the method only works after you set the equation equal to zero.

The process has a non-negotiable first step: rearrange the equation so that one side is exactly zero. This is where many errors occur. If you have x² − 5x = 6 and factor the left side as x(x − 5) = 6, you cannot then set x = 6 or x − 5 = 6 — because if two things multiply to 6, there are infinitely many possibilities. The zero product property only applies to a product that equals zero. So always move everything to one side first, getting x² − 5x − 6 = 0, factor to get (x − 6)(x + 1) = 0, then set each factor to zero: x = 6 or x = −1.

Once the product equals zero, each factor is treated independently. Setting each factor equal to zero reduces the quadratic to two separate linear equations — which you already know how to solve from your multi-step equation work. You get one solution from each factor, which is why quadratics can have up to two solutions. The special case of a repeated factor like (x − 3)² = 0 gives x = 3 twice, which counts as one **repeated root** (or a root of **multiplicity** two).

The geometric meaning ties this together: the solutions are exactly the **x-intercepts** of the parabola y = f(x). A quadratic with two real factors crosses the x-axis at two points. A perfect square factor (repeated root) touches but doesn't cross the axis at that point. A quadratic with no real factorization has no real x-intercepts — the parabola lives entirely above or below the x-axis. Factoring is the fastest method when the roots are integers, but the quadratic formula (your next topic) handles every case.
