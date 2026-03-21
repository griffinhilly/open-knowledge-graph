---
id: inverse-functions
title: Inverse Functions
domain: mathematics
course: algebra-2
prerequisites:
- id: function-notation-review
  type: hard
- id: equations-variables-both-sides
  type: hard
- id: composition-of-functions
  type: soft
builds-toward:
- logarithms-intro
- radical-functions-and-graphs
tags:
- functions
- inverse
- one-to-one
- horizontal-line-test
stage: formal-systems
status: validated
---
# Inverse Functions

## Core Idea
The inverse function f^(-1) "undoes" f: if f(a) = b, then f^(-1)(b) = a. Graphically, f and f^(-1) are reflections over the line y = x. A function has an inverse if and only if it is one-to-one (passes the horizontal line test). To find f^(-1) algebraically: swap x and y in y = f(x), then solve for y. The composition f(f^(-1)(x)) = x and f^(-1)(f(x)) = x verifies the inverse relationship.

## How It's Best Learned
Start with simple examples: if f(x) = 2x + 3, find f^(-1)(x) by swapping and solving. Verify by composition. Use the horizontal line test to determine invertibility. Graph functions and their inverses to see the y = x reflection. Discuss restricting domains to create invertible functions (e.g., restricting x^2 to x >= 0).

## Common Misconceptions
- Confusing f^(-1)(x) with 1/f(x) (inverse function vs. reciprocal).
- Thinking every function has an inverse (only one-to-one functions do).
- Forgetting to swap x and y before solving.
- Not restricting the domain when needed (e.g., finding the inverse of x^2 without specifying x >= 0).

## Questions

```yaml
- question: "If f(x) = 2x + 6, what is f⁻¹(x)?"
  type: multiple-choice
  options:
    - "1/(2x + 6) — the reciprocal of f(x)"
    - "2x − 6 — subtracting 6 from the original function"
    - "(x − 6)/2 — swapping x and y, then solving for y"
    - "(x + 6)/2 — a sign error when isolating the variable"
  answer: 2
  explanation: "To find the inverse, swap x and y in y = 2x + 6 to get x = 2y + 6, then solve for y: y = (x − 6)/2. Verify by composition: f(f⁻¹(x)) = 2·((x−6)/2) + 6 = (x−6) + 6 = x. ✓ Option A is the most common mistake — confusing the inverse function f⁻¹ with the reciprocal 1/f(x). These are completely different: f⁻¹ undoes f, while 1/f(x) is just the multiplicative reciprocal. Option D gets the sign wrong when solving 2y = x − 6."

- question: "Which function does NOT have an inverse over its natural domain?"
  type: multiple-choice
  options:
    - "f(x) = 3x − 1"
    - "f(x) = x³"
    - "f(x) = x²"
    - "f(x) = eˣ"
  answer: 2
  explanation: "f(x) = x² fails the horizontal line test on its natural domain (all real numbers): the horizontal line y = 4 crosses the graph at both x = 2 and x = −2. Since two different inputs produce the same output (f(2) = f(−2) = 4), the function is not one-to-one, and no inverse exists. The other three functions are all strictly monotone over their domains — f(x) = 3x−1 and f(x) = eˣ are strictly increasing, f(x) = x³ is strictly increasing everywhere — so each passes the horizontal line test."

- question: "The notation f⁻¹(x) means the same thing as [f(x)]⁻¹ = 1/f(x)."
  type: true-false
  answer: false
  explanation: "False — this is one of the most common misconceptions in algebra. f⁻¹(x) denotes the inverse function, which undoes what f does: if f(a) = b, then f⁻¹(b) = a. The expression 1/f(x) is the reciprocal, which has no such relationship. For example, if f(x) = 2x, then f⁻¹(x) = x/2 (divides by 2), while 1/f(x) = 1/(2x) (a completely different function). The notation is unfortunate but standard — the exponent −1 on a function name always means 'inverse function,' not 'reciprocal.'"

- question: "The graph of f⁻¹ is the reflection of the graph of f across the line y = x."
  type: true-false
  answer: true
  explanation: "True. Reflecting a graph across the line y = x swaps every point (a, b) to (b, a) — which is exactly the relationship between f and f⁻¹. If the point (a, b) is on the graph of f (meaning f(a) = b), then the point (b, a) is on the graph of f⁻¹ (meaning f⁻¹(b) = a). This geometric fact explains why the inverse can be found algebraically by swapping x and y: swapping coordinates in the equation is the algebraic version of reflecting over y = x."

- question: "Explain why f(x) = x² does not have an inverse on its natural domain, and describe how restricting the domain to x ≥ 0 fixes this problem."
  type: short-answer
  answer: "f(x) = x² is not one-to-one on all real numbers because it maps two different inputs to the same output: f(2) = 4 and f(−2) = 4. An inverse function would need to answer 'what input produced 4?' — but there are two valid answers (2 and −2), making the inverse ambiguous and not a function. Restricting the domain to x ≥ 0 removes the negative inputs, keeping only the right half of the parabola. This restricted version is strictly increasing, so each output corresponds to exactly one input. The inverse of x² on x ≥ 0 is √x (with range y ≥ 0), and the two graphs are reflections of each other across y = x."
  explanation: "Domain restriction is a general technique: any non-one-to-one function can be made invertible by selecting a portion of its domain on which it is monotone. For x², x ≥ 0 is the conventional choice, giving the standard square root. The inverse only exists on the restricted domain, and its range is restricted accordingly — this is why √x returns only non-negative values."
```

## Explainer

Think of a function as a machine: you put in an input, it produces an output. The **inverse function** is the reverse machine — you give it the output and it tells you what the original input was. If f(3) = 7, then f⁻¹(7) = 3. If f(x) = 2x + 3 converts Fahrenheit to some scale, then f⁻¹ converts back. The relationship is captured by the composition rules: f(f⁻¹(x)) = x and f⁻¹(f(x)) = x — doing f then undoing it returns you exactly where you started.

Not every function has an inverse, and this is where the **one-to-one** (or injective) requirement comes in. A function fails to have an inverse when two different inputs produce the same output — because then the reverse machine wouldn't know which original input to return. For example, f(x) = x² sends both 3 and −3 to 9. If you ask "what input gave output 9?", the function can't answer uniquely. The **horizontal line test** detects this visually: if any horizontal line crosses the graph more than once, the function is not one-to-one and has no inverse on that domain. You can *create* an inverse by restricting the domain — for x² restricted to x ≥ 0, the inverse is √x.

To find the inverse algebraically, you're essentially solving for the input in terms of the output. Start with y = f(x), swap x and y to get x = f(y), then solve for y. The swap step encodes the reversal: x (the original output) is now the input, and y (the original input) is now the output. For f(x) = 2x + 3: swap to get x = 2y + 3, solve to get y = (x − 3)/2. So f⁻¹(x) = (x − 3)/2. Always verify by composing: f(f⁻¹(x)) = 2·((x − 3)/2) + 3 = (x − 3) + 3 = x. ✓

Graphically, f and f⁻¹ are **reflections over the line y = x**. This is because swapping x and y in the equation is exactly what reflecting over y = x does to a graph. If you plot f(x) = 2x + 3 and f⁻¹(x) = (x − 3)/2 on the same axes, they are mirror images across the diagonal line. This geometric picture connects the algebra to a visual structure and reinforces why domain restrictions matter: if you restrict x² to x ≥ 0, its graph is the right half of the parabola, and its reflection over y = x is the upper half of √x — they fit together perfectly.
