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

## Questions

```yaml
- question: "The graph of y = f(x) has a vertex at (0, 4). Where is the vertex on the graph of y = f(x − 3)?"
  type: multiple-choice
  options:
    - "(−3, 4) — the graph shifts left because you're subtracting"
    - "(3, 4) — the graph shifts right despite the subtraction"
    - "(0, 1) — subtracting from the input compresses the graph vertically"
    - "(0, 7) — the vertex moves up by 3"
  answer: 1
  explanation: "Replacing x with (x − 3) is an inside change — it modifies the input. To produce the same output the function used to produce at x = 0, you now need x = 3 (so that x − 3 = 0). The entire graph shifts rightward by 3, even though the algebra shows subtraction. This is the central counterintuitive rule: inside changes act opposite to what the algebra suggests."

- question: "The function y = f(2x) is applied to the parent y = f(x). What happens to the graph?"
  type: multiple-choice
  options:
    - "It stretches horizontally by a factor of 2 — multiplying x by 2 spreads the graph out"
    - "It compresses horizontally by a factor of 2 — the graph is narrowed"
    - "It stretches vertically by a factor of 2 — multiplying makes outputs larger"
    - "It shifts rightward by 2 units"
  answer: 1
  explanation: "Replacing x with 2x compresses the graph horizontally by a factor of 2 — every feature occurs at half the x-value it used to. A point previously at x = 4 now appears at x = 2 (because 2·2 = 4). Again, the inside change acts opposite to intuition: multiplying by 2 inside makes the graph narrower, not wider. Stretching horizontally would correspond to y = f(x/2)."

- question: "The graph of y = f(x − 4) is the graph of y = f(x) shifted 4 units to the right."
  type: true-false
  answer: true
  explanation: "True. Replacing x with (x − 4) is an inside change that shifts the graph rightward by 4, despite the subtraction. The key: to get f's original output at x = 0, you now need x = 4 (so x − 4 = 0). Every point migrates 4 units to the right. This feels backwards because we're subtracting, but inside changes act opposite to intuition."

- question: "The transformations y = f(x) + 3 and y = f(x + 3) both move the graph upward by 3 units."
  type: true-false
  answer: false
  explanation: "False. y = f(x) + 3 is an outside change — it adds 3 to the output, shifting the graph vertically upward by 3. But y = f(x + 3) is an inside change — it modifies the input, shifting the graph horizontally to the LEFT by 3 (not upward). The two transformations move the graph in completely different directions. Outside changes affect y (act as expected); inside changes affect x (act opposite to intuition)."

- question: "Why do horizontal transformations — like f(x − h) or f(bx) — act opposite to what the algebra seems to suggest?"
  type: short-answer
  answer: "Because input changes must be 'undone' to produce the same output. To get the output f used to produce at x = 0, you now need x = h when the argument is (x − h). The graph shifts right (toward larger x) to compensate for the subtraction. Similarly, y = f(bx) compresses rather than stretches because each output now occurs at 1/b of its original x-value."
  explanation: "The intuition: a transformation applied to the input changes 'where you need to be' to get a given output — not 'what output you get.' Outside transformations directly scale or shift outputs and behave as expected. Inside transformations redefine the input mapping, and the graph moves in the opposite direction of the algebraic operation to compensate."
```

## Explainer

You know from function notation that f(x) is a machine: input x, output f(x). Function transformations ask a new question: what happens to the graph if you modify the machine's input or output systematically? The answer is completely mechanical — there is one master formula y = af(b(x − h)) + k, and each parameter controls exactly one type of transformation. Once you can read this formula, you can graph any transformed function quickly by reading off the parameters without recomputing the function from scratch.

Start with the **outside** changes, which modify the output directly. Adding k gives y = f(x) + k, which shifts every point up by k — all y-values increase by k, so the graph lifts vertically. Multiplying the output by a gives y = af(x), which stretches vertically by factor |a| (if |a| > 1, stretching; if |a| < 1, compressing) and reflects across the x-axis if a < 0. These act intuitively: you're directly scaling or shifting the y-values and the graph responds as you'd expect.

Now the **inside** changes, which modify the input before it enters f, and they feel counterintuitive. Replacing x with (x − h) gives y = f(x − h), which shifts the graph *right* by h even though you're subtracting. The reason: to get the same output you used to get at x = 0, you now need x = h (so that x − h = 0). Every feature of the graph migrates right by h. If h is negative, it shifts left. Replacing x with bx gives y = f(bx), which *compresses* horizontally by factor b when |b| > 1 (events happen sooner) and *stretches* when |b| < 1 (events spread out). A reflection across the y-axis corresponds to b = −1. The mnemonic: **outside changes act as you expect; inside changes act opposite to what the algebra suggests**.

The full formula y = af(b(x − h)) + k combines all four in a consistent order. To graph it: identify the **parent function** f, apply the horizontal shift h (move right by h), apply the horizontal scale b (compress/stretch/reflect horizontally), apply the vertical scale a (stretch/compress/reflect vertically), then apply the vertical shift k. Key features transform by the same rules as individual points: a vertex at (x₀, y₀) on the parent moves to (x₀/b + h, ay₀ + k); a horizontal asymptote y = c becomes y = ac + k. This framework carries directly into trigonometry, where the same parameters become amplitude (a), frequency (b), phase shift (h), and vertical midline (k) — making function transformations an indispensable foundation for everything that follows.
