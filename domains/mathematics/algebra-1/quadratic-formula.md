---
id: quadratic-formula
title: The Quadratic Formula
domain: mathematics
course: algebra-1
prerequisites:
- id: solving-quadratics-by-factoring
  type: hard
- id: square-roots-intro
  type: hard
- id: literal-equations
  type: soft
- id: radical-expressions-simplifying
  type: soft
- id: vertex-form
  type: soft
builds-toward:
- discriminant
- complex-numbers-intro
- solving-quadratic-equations-completing-the-square
tags:
- quadratic-formula
- quadratics
- solving
- roots
stage: abstract-reasoning
status: validated
---
# The Quadratic Formula

## Core Idea
The quadratic formula solves any quadratic equation ax² + bx + c = 0: x = (−b ± sqrt(b² − 4ac)) / (2a). It works for every quadratic — factorable or not — making it the most powerful tool for finding roots. The formula is derived by completing the square on the general quadratic equation. The ± symbol indicates there can be two solutions. The expression under the square root, b² − 4ac, is the discriminant and determines the nature of the solutions. The quadratic formula is one of the most important formulas in all of mathematics.

## How It's Best Learned
First use it on equations that can also be factored, so students can verify their answers. Then apply it to non-factorable quadratics. Emphasize careful substitution — especially handling negative b and negative c. Practice simplifying the radical and the fraction. Show the derivation via completing the square for advanced students. Use it alongside factoring to build judgment about which method is faster.

## Common Misconceptions
- Forgetting the 2a in the denominator (dividing only by a or only by 2).
- Not putting the entire numerator over 2a (computing −b ± sqrt(...)/2a instead of (−b ± sqrt(...))/2a).
- Sign errors when b is negative (−b becomes positive, and b² is always positive).
- Not simplifying the final answer (leaving sqrt(32) instead of 4sqrt(2)).

## Questions

```yaml
- question: "The equation 2x² + 3x - 5 = 0 has a = 2, b = 3, c = -5. What is the value of the discriminant (b² - 4ac)?"
  type: multiple-choice
  options: ["-31", "9", "49", "-49"]
  answer: 2
  explanation: "b² - 4ac = (3)² - 4(2)(-5) = 9 + 40 = 49. A common error is computing 4(2)(-5) as -40 instead of +40, since multiplying two negatives (the 4ac term with c = -5) yields a positive contribution when subtracted."

- question: "When using the quadratic formula on x² - 6x + 9 = 0, you get x = (6 ± 0) / 2. This means the equation has two different real solutions."
  type: true-false
  answer: false
  explanation: "When the discriminant equals zero, the ± contributes nothing — both 'solutions' collapse to the same value (x = 3). The quadratic has exactly one repeated root, not two distinct solutions. Geometrically, the parabola just touches the x-axis at one point."

- question: "Why does the quadratic formula work on equations that factoring cannot easily solve?"
  type: short-answer
  answer: "The quadratic formula is derived by completing the square on the general form ax² + bx + c = 0, so it works for any values of a, b, and c — including irrational or complex roots that have no simple integer factors."
  explanation: "Factoring relies on finding integer (or simple rational) pairs that multiply to ac and add to b. Many quadratics have irrational roots (like sqrt(2)) that cannot be found by factoring. The quadratic formula bypasses this limitation because it is an algebraic derivation that handles all cases."
```

## Explainer

When you learned to solve quadratics by factoring, you found that some equations factor neatly — like x² - 5x + 6 = (x - 2)(x - 3) — but others resist factoring entirely. Try factoring x² + 3x - 7 = 0 and you will quickly get stuck. The quadratic formula exists precisely for this reason: it solves *every* quadratic equation, factorable or not.

The formula comes from completing the square on the general equation ax² + bx + c = 0. If you divide by a, move the constant term, complete the square on the left, and then take the square root of both sides, you arrive at x = (-b ± sqrt(b² - 4ac)) / (2a). Every step is algebra you already know; the formula just packages the result so you never have to repeat those steps. The ± symbol is doing critical work: when you take a square root, both the positive and negative values are valid, which is why quadratics can have two solutions.

The expression under the square root — b² - 4ac — is called the discriminant, and it tells you what kind of answers to expect before you even compute them. If it is positive, you get two distinct real roots. If it is zero, both roots collapse to the same value (a repeated root). If it is negative, you are trying to take the square root of a negative number, which leads to complex numbers — a topic you will encounter soon.

When applying the formula, the most common source of errors is not the formula itself but careless substitution. Pay special attention to the sign of b: if b = -4, then -b = 4 and b² = 16 (not -16). Also, the entire expression (-b ± sqrt(...)) is the numerator, all divided by 2a — not just the square root part. Writing out the substitution step explicitly before simplifying will save you from most mistakes.

Finally, remember that the quadratic formula does not replace factoring — it supplements it. On an exam, if you can see the factors quickly, factoring is faster. If you cannot, or if the coefficients are messy, the formula is your reliable fallback. Developing judgment about which method to use is part of algebraic fluency.
