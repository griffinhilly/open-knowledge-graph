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

## Questions

```yaml
- question: "A student has the equation x² − 5x = 6. They factor the left side as x(x − 5) = 6 and conclude x = 6 or x − 5 = 6, giving x = 6 or x = 11. What error did they make?"
  type: multiple-choice
  options:
    - "They factored the left side incorrectly"
    - "They applied the zero product property without first setting the equation equal to zero"
    - "They should have used the quadratic formula for this equation"
    - "They found two solutions when this equation has only one"
  answer: 1
  explanation: "The zero product property states that if a product equals zero, one of the factors must be zero. It does NOT apply when a product equals any other number — if two things multiply to 6, there are infinitely many possibilities. The required first step is to move all terms to one side: x² − 5x − 6 = 0, then factor to (x − 6)(x + 1) = 0, giving x = 6 or x = −1. The student's error of skipping this step is the most common mistake in solving quadratics by factoring."

- question: "Which of the following quadratic equations has exactly one real solution?"
  type: multiple-choice
  options:
    - "x² − 5x + 6 = 0"
    - "x² − 6x + 9 = 0"
    - "x² − 4 = 0"
    - "x² + 2x − 8 = 0"
  answer: 1
  explanation: "x² − 6x + 9 = 0 factors as (x − 3)² = 0, giving x = 3 as a repeated root — one solution (technically multiplicity 2, but only one distinct value). The others factor as (x−2)(x−3) = 0 (two solutions: 2 and 3), (x−2)(x+2) = 0 (two solutions: 2 and −2), and (x+4)(x−2) = 0 (two solutions: −4 and 2). A repeated factor means the parabola touches the x-axis at exactly one point without crossing it."

- question: "To solve the equation (x + 4)(x − 3) = 0, you can set each factor equal to zero independently because the product equals zero."
  type: true-false
  answer: true
  explanation: "This is the zero product property in action. Because the product of the two factors is zero, at least one factor must be zero — there is no other way a product can be zero. Setting x + 4 = 0 gives x = −4, and setting x − 3 = 0 gives x = 3. Both values satisfy the original equation. The reason you can treat the factors independently is that zero is the only number with this special 'forcing' property."

- question: "If (x + 2)(x − 3) = 6, you can find the solutions by setting x + 2 = 6 or x − 3 = 6."
  type: true-false
  answer: false
  explanation: "The zero product property only applies when a product equals zero, not any other number. If x + 2 = 6 then x = 4, and checking: (4+2)(4−3) = 6×1 = 6, so x = 4 happens to work — but x − 3 = 6 gives x = 9, and (9+2)(9−3) = 11×6 = 66 ≠ 6. The correct method is to expand and rearrange: x² − x − 6 = 6 → x² − x − 12 = 0 → (x − 4)(x + 3) = 0, giving x = 4 or x = −3."

- question: "Why must a quadratic equation be set equal to zero before you can use the zero product property? What goes wrong if you skip this step?"
  type: short-answer
  answer: "The zero product property is specifically about products that equal zero: if ab = 0, then a = 0 or b = 0. This works because zero is the only number with the property that one factor must be zero. If the product equals any other number — say 6 — then there are infinitely many factor pairs that multiply to 6, so you cannot set each factor equal to that number and solve independently. Skipping the 'set equal to zero' step leads to equations like x(x−5) = 6, which incorrectly suggests x = 6 or x−5 = 6 as solutions."
  explanation: "The zero product property is a uniquely powerful tool precisely because it only works for zero. Any equation of the form ab = k where k ≠ 0 cannot be solved by splitting into a = k or b = k. Setting the equation equal to zero first converts the problem into exactly the form where this property applies, turning the quadratic into two simple linear equations."
```

## Explainer

From your work with factoring, you know how to break a polynomial like x² − 5x + 6 into factors (x − 2)(x − 3). Solving quadratics by factoring uses that skill to answer a new question: for which x-values does the polynomial equal zero? The key is the **zero product property**: if two quantities multiply to zero, at least one of them must be zero. This is the only time multiplication guarantees a factor is zero, and it's why the method only works after you set the equation equal to zero.

The process has a non-negotiable first step: rearrange the equation so that one side is exactly zero. This is where many errors occur. If you have x² − 5x = 6 and factor the left side as x(x − 5) = 6, you cannot then set x = 6 or x − 5 = 6 — because if two things multiply to 6, there are infinitely many possibilities. The zero product property only applies to a product that equals zero. So always move everything to one side first, getting x² − 5x − 6 = 0, factor to get (x − 6)(x + 1) = 0, then set each factor to zero: x = 6 or x = −1.

Once the product equals zero, each factor is treated independently. Setting each factor equal to zero reduces the quadratic to two separate linear equations — which you already know how to solve from your multi-step equation work. You get one solution from each factor, which is why quadratics can have up to two solutions. The special case of a repeated factor like (x − 3)² = 0 gives x = 3 twice, which counts as one **repeated root** (or a root of **multiplicity** two).

The geometric meaning ties this together: the solutions are exactly the **x-intercepts** of the parabola y = f(x). A quadratic with two real factors crosses the x-axis at two points. A perfect square factor (repeated root) touches but doesn't cross the axis at that point. A quadratic with no real factorization has no real x-intercepts — the parabola lives entirely above or below the x-axis. Factoring is the fastest method when the roots are integers, but the quadratic formula (your next topic) handles every case.
