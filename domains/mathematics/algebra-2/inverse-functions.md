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

## Explainer

Think of a function as a machine: you put in an input, it produces an output. The **inverse function** is the reverse machine — you give it the output and it tells you what the original input was. If f(3) = 7, then f⁻¹(7) = 3. If f(x) = 2x + 3 converts Fahrenheit to some scale, then f⁻¹ converts back. The relationship is captured by the composition rules: f(f⁻¹(x)) = x and f⁻¹(f(x)) = x — doing f then undoing it returns you exactly where you started.

Not every function has an inverse, and this is where the **one-to-one** (or injective) requirement comes in. A function fails to have an inverse when two different inputs produce the same output — because then the reverse machine wouldn't know which original input to return. For example, f(x) = x² sends both 3 and −3 to 9. If you ask "what input gave output 9?", the function can't answer uniquely. The **horizontal line test** detects this visually: if any horizontal line crosses the graph more than once, the function is not one-to-one and has no inverse on that domain. You can *create* an inverse by restricting the domain — for x² restricted to x ≥ 0, the inverse is √x.

To find the inverse algebraically, you're essentially solving for the input in terms of the output. Start with y = f(x), swap x and y to get x = f(y), then solve for y. The swap step encodes the reversal: x (the original output) is now the input, and y (the original input) is now the output. For f(x) = 2x + 3: swap to get x = 2y + 3, solve to get y = (x − 3)/2. So f⁻¹(x) = (x − 3)/2. Always verify by composing: f(f⁻¹(x)) = 2·((x − 3)/2) + 3 = (x − 3) + 3 = x. ✓

Graphically, f and f⁻¹ are **reflections over the line y = x**. This is because swapping x and y in the equation is exactly what reflecting over y = x does to a graph. If you plot f(x) = 2x + 3 and f⁻¹(x) = (x − 3)/2 on the same axes, they are mirror images across the diagonal line. This geometric picture connects the algebra to a visual structure and reinforces why domain restrictions matter: if you restrict x² to x ≥ 0, its graph is the right half of the parabola, and its reflection over y = x is the upper half of √x — they fit together perfectly.
