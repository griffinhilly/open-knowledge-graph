---
id: function-transformations
title: "Function Transformations: Shifts, Stretches, and Reflections"
domain: mathematics
course: precalculus
prerequisites:
  - id: function-notation-review
    type: hard
  - id: domain-and-range
    type: soft
builds-toward:
  - graphing-sine-and-cosine
  - amplitude-period-phase-shift
tags: [functions, transformations, graphing]
stage: formal-systems
status: validated
---

# Function Transformations: Shifts, Stretches, and Reflections

## Core Idea
Every function y = f(x) can be transformed by modifying the input or output: vertical/horizontal shifts move the graph, vertical/horizontal stretches scale it, and reflections flip it across an axis. These transformations follow predictable algebraic patterns: y = af(b(x - h)) + k encodes all of them in a single template. This framework lets you graph any transformed function quickly by reading off the parameters.

## How It's Best Learned
Build intuition by starting with a simple parent function (like f(x) = x^2) and applying one transformation at a time. Use graphing technology to verify predictions. Emphasize the "inside vs. outside" distinction: changes inside the argument affect x (and act opposite to intuition), changes outside affect y (and act as expected).

## Common Misconceptions
- Horizontal shifts feel backwards: f(x - 3) shifts right, not left.
- Confusing the order of transformations when multiple are combined.
- Forgetting that horizontal stretches/compressions also shift asymptotes and key features.

## Explainer

You know from function notation that f(x) is a machine: input x, output f(x). Function transformations ask a new question: what happens to the graph if you modify the machine's input or output systematically? The answer is completely mechanical — there is one master formula y = af(b(x − h)) + k, and each parameter controls exactly one type of transformation. Once you can read this formula, you can graph any transformed function quickly by reading off the parameters without recomputing the function from scratch.

Start with the **outside** changes, which modify the output directly. Adding k gives y = f(x) + k, which shifts every point up by k — all y-values increase by k, so the graph lifts vertically. Multiplying the output by a gives y = af(x), which stretches vertically by factor |a| (if |a| > 1, stretching; if |a| < 1, compressing) and reflects across the x-axis if a < 0. These act intuitively: you're directly scaling or shifting the y-values and the graph responds as you'd expect.

Now the **inside** changes, which modify the input before it enters f, and they feel counterintuitive. Replacing x with (x − h) gives y = f(x − h), which shifts the graph *right* by h even though you're subtracting. The reason: to get the same output you used to get at x = 0, you now need x = h (so that x − h = 0). Every feature of the graph migrates right by h. If h is negative, it shifts left. Replacing x with bx gives y = f(bx), which *compresses* horizontally by factor b when |b| > 1 (events happen sooner) and *stretches* when |b| < 1 (events spread out). A reflection across the y-axis corresponds to b = −1. The mnemonic: **outside changes act as you expect; inside changes act opposite to what the algebra suggests**.

The full formula y = af(b(x − h)) + k combines all four in a consistent order. To graph it: identify the **parent function** f, apply the horizontal shift h (move right by h), apply the horizontal scale b (compress/stretch/reflect horizontally), apply the vertical scale a (stretch/compress/reflect vertically), then apply the vertical shift k. Key features transform by the same rules as individual points: a vertex at (x₀, y₀) on the parent moves to (x₀/b + h, ay₀ + k); a horizontal asymptote y = c becomes y = ac + k. This framework carries directly into trigonometry, where the same parameters become amplitude (a), frequency (b), phase shift (h), and vertical midline (k) — making function transformations an indispensable foundation for everything that follows.
