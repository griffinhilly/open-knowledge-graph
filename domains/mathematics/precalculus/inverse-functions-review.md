---
id: inverse-functions-review
title: Inverse Functions Review
domain: mathematics
course: precalculus
prerequisites:
- id: function-notation-review
  type: hard
- id: domain-and-range
  type: hard
- id: composition-of-functions-advanced
  type: soft
builds-toward:
- inverse-trigonometric-functions
- derivatives-of-logarithmic-functions
tags:
- functions
- inverses
- one-to-one
stage: formal-systems
status: validated
---
# Inverse Functions Review

## Core Idea
An inverse function f^(-1) reverses the action of f: if f(a) = b, then f^(-1)(b) = a. A function has an inverse if and only if it is one-to-one (passes the horizontal line test). The domain of f becomes the range of f^(-1) and vice versa. Graphically, f and f^(-1) are reflections across the line y = x. Inverse functions are the foundation for logarithms, inverse trig functions, and solving equations.

## How It's Best Learned
Start with simple examples (linear functions), find inverses algebraically by swapping x and y and solving, then verify by composing f(f^(-1)(x)) = x. Use the horizontal line test to determine invertibility, and discuss restricting domains to create invertible functions.

## Common Misconceptions
- Confusing f^(-1)(x) with 1/f(x): inverse function vs. reciprocal.
- Forgetting to swap domain and range when finding the inverse.
- Assuming all functions have inverses without checking one-to-one.

## Questions

```yaml
- question: "If f(3) = 7, what is f⁻¹(7)?"
  type: multiple-choice
  options:
    - "1/7 — since f⁻¹ means the reciprocal of the output"
    - "3 — since the inverse reverses the input-output pair"
    - "1/3 — since the inverse undoes multiplication by 3"
    - "Cannot be determined without knowing the formula for f"
  answer: 1
  explanation: "The inverse function reverses input and output: f(3) = 7 means f⁻¹(7) = 3 by definition. You don't need the formula — just the input-output relationship. Option A is the classic confusion between f⁻¹(x) (inverse function) and [f(x)]⁻¹ = 1/f(x) (reciprocal). These are completely different things in function notation."

- question: "The function f(x) = x² is defined over all real numbers. Which statement is true?"
  type: multiple-choice
  options:
    - "f⁻¹(x) = √x for all real x, since squaring and square-rooting are inverse operations"
    - "f has no inverse over all reals, because f(2) = f(−2) = 4 — two inputs produce the same output"
    - "f⁻¹(x) = −√x recovers the original input for all real x"
    - "f has an inverse because every output in the range has at least one corresponding input"
  answer: 1
  explanation: "Since f(2) = f(−2) = 4, f is not one-to-one over all reals — the horizontal line y = 4 hits the parabola twice. The inverse can't exist because it can't decide whether to return 2 or −2 for the input 4. Option A sounds reasonable but ignores this non-uniqueness. To get a valid inverse, you must restrict the domain to x ≥ 0 (giving f⁻¹(x) = √x) or x ≤ 0 (giving f⁻¹(x) = −√x), but not both simultaneously."

- question: "If (5, 12) is a point on the graph of f, then (12, 5) is a point on the graph of f⁻¹."
  type: true-false
  answer: true
  explanation: "Inverse functions swap the roles of input and output: f(5) = 12 implies f⁻¹(12) = 5 by definition. Graphically, this corresponds to reflecting the point (5, 12) across the line y = x to get (12, 5). This coordinate swap is the defining geometric property of the inverse — which is why the graphs of f and f⁻¹ are always reflections of each other across y = x."

- question: "The notation f⁻¹(x) means the same as [f(x)]⁻¹ = 1/f(x)."
  type: true-false
  answer: false
  explanation: "The −1 superscript in function notation denotes the inverse function, not the reciprocal. f⁻¹(x) is the function that undoes f, satisfying f⁻¹(f(x)) = x. For example, if f(x) = 2x, then f⁻¹(x) = x/2, while 1/f(x) = 1/(2x) — completely different functions. The notation is confusingly similar to the reciprocal exponent in arithmetic, but in function composition context, f⁻¹ always means inverse, not reciprocal."

- question: "Why must a function be one-to-one to have an inverse, and what happens if it isn't?"
  type: short-answer
  answer: "A function must be one-to-one because the inverse must assign a unique output to each input. If two inputs a ≠ b both map to the same output (f(a) = f(b)), the inverse can't decide which input to return — it would need to produce two outputs for one input, violating the definition of a function. If a function isn't one-to-one over its full domain, you can still define a partial inverse by restricting the domain to a region where it is one-to-one, as with restricting x² to x ≥ 0 to define √x."
  explanation: "The inverse function is itself a function, so it must pass the vertical line test — each input maps to exactly one output. Non-one-to-one functions create ambiguity: the inverse at an output value c doesn't know which of the multiple preimages to return. Domain restriction resolves this by discarding the ambiguous inputs. This is exactly why arcsin is defined only on [−π/2, π/2] — sin is not one-to-one over all reals, so you pick the interval where it is."
```

## Explainer

You know from your study of function notation that a function f takes an input x and produces an output f(x). An **inverse function** f⁻¹ does exactly the reverse: it takes the output of f and recovers the original input. Formally, if f(a) = b, then f⁻¹(b) = a. This is not about reciprocals — f⁻¹(x) is not 1/f(x) — it's about undoing. If f multiplies by 3, then f⁻¹ divides by 3. If f adds 5, then f⁻¹ subtracts 5. If f takes a square (with appropriate domain), f⁻¹ takes a square root.

The critical question is: when does an inverse exist? Here, your knowledge of domain and range becomes essential. A function can only be inverted if it is **one-to-one**: every output comes from exactly one input. If two different inputs produced the same output, which one would the inverse recover? It cannot do both. The geometric test is the **horizontal line test** — if any horizontal line crosses the graph more than once, the function is not one-to-one and has no inverse (over that full domain). The standard function f(x) = x² fails this test over all reals (since f(2) = f(−2) = 4), but succeeds if you restrict the domain to x ≥ 0 — which is exactly how the square root function is defined as the inverse of the "right half" of the parabola.

To find the inverse algebraically: write y = f(x), then swap x and y (since the inverse reverses the roles of input and output), and solve for y. That expression in y is f⁻¹(x). The domain of f⁻¹ is the range of f, and the range of f⁻¹ is the domain of f — they swap. You can always verify: the composition f(f⁻¹(x)) = x and f⁻¹(f(x)) = x should both hold (wherever defined). This composition identity is the *definition* of what it means for two functions to be inverses of each other.

Graphically, f and f⁻¹ are reflections of each other across the line y = x. This is because swapping x and y in the equation is precisely the algebraic description of reflecting across y = x. If the point (2, 5) is on the graph of f, then (5, 2) is on the graph of f⁻¹. This visual symmetry is a powerful check: if the graph of f doesn't look like a reflection of the graph of f⁻¹ across y = x, something has gone wrong.

This topic is the conceptual prerequisite for two major upcoming ideas. Logarithms are the inverse functions of exponentials — log_b(x) asks "what power of b gives x?" — and inverse trigonometric functions like arcsin, arccos, arctan are inverses of the trig functions restricted to appropriate domains. Every time you solve an equation by "undoing" an operation — taking a log of both sides, applying arcsin to isolate an angle — you are using inverse functions. Understanding the one-to-one requirement now prevents confusion later about why arcsin(sin(x)) ≠ x for all x.
