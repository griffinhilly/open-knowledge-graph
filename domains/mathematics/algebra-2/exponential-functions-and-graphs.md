---
id: exponential-functions-and-graphs
title: Exponential Functions and Graphs
domain: mathematics
course: algebra-2
prerequisites:
  - id: exponent-rules-product-power-quotient
    type: hard
  - id: rational-exponents
    type: soft
builds-toward:
  - exponential-growth-and-decay
  - logarithms-intro
  - natural-logarithm-and-e
tags: [exponential, functions, graphing, growth]
stage: abstract-reasoning
status: validated
---

# Exponential Functions and Graphs

## Core Idea
An exponential function has the form f(x) = a*b^x where b > 0, b != 1. If b > 1, the function models exponential growth; if 0 < b < 1, exponential decay. Key features: the graph passes through (0, a), has a horizontal asymptote at y = 0, is always positive (for a > 0), and increases/decreases without bound. Exponential functions grow faster than any polynomial for large x. Transformations shift, stretch, and reflect the basic curve.

## How It's Best Learned
Graph y = 2^x and y = (1/2)^x as parent functions. Apply transformations. Compare growth rates by graphing y = x^2 and y = 2^x on the same axes. Discuss real-world contexts: population growth, radioactive decay, compound interest. Introduce the natural base e as a special exponential base.

## Common Misconceptions
- Confusing exponential growth (b^x) with polynomial growth (x^b).
- Thinking the graph touches or crosses the x-axis (it approaches but never reaches the horizontal asymptote).
- Not recognizing that (1/2)^x = 2^(-x) (decay is growth reflected).
- Thinking b must be an integer.

## Questions

```yaml
- question: "The graph of f(x) = 3^x gets closer and closer to the x-axis as x decreases toward negative infinity. What does this tell you about the x-axis?"
  type: multiple-choice
  options: ["The x-axis is a vertical asymptote of the function", "The x-axis is a horizontal asymptote the graph never actually reaches", "The graph eventually crosses the x-axis at a very negative x value", "The function becomes zero when x is sufficiently negative"]
  answer: 1
  explanation: "For f(x) = 3^x, as x → -∞, f(x) → 0 from above but never equals 0, because 3 raised to any power is always positive. The x-axis (y = 0) is a horizontal asymptote: the graph approaches it indefinitely but never touches or crosses it. This is a fundamental feature of all exponential functions with positive base — the output is always positive."

- question: "The functions f(x) = (1/2)^x and g(x) = 2^(-x) are different exponential functions with different growth behaviors."
  type: true-false
  answer: false
  explanation: "(1/2)^x = (2^(-1))^x = 2^(-x) by exponent rules. They are the same function. This also reveals a general principle: exponential decay (base between 0 and 1) is the same as growth with a negative exponent. The graph of decay is the reflection of the growth curve across the y-axis."

- question: "Why does an exponential function like 2^x eventually outgrow any polynomial function like x^100, even though x^100 seems enormous?"
  type: short-answer
  answer: "In a polynomial, the base grows while the exponent is fixed. In an exponential, the exponent grows while the base is fixed. As x increases, the exponent in 2^x keeps increasing, causing the function to repeatedly multiply by 2 — so it compounds indefinitely. A polynomial grows by adding increasingly large terms, but an exponential grows by multiplying, which dominates for large enough x."
  explanation: "The key distinction is what role x plays. In x^100, x is the base — it grows, but each increase only adds one more factor. In 2^x, x is the exponent — each unit increase multiplies the entire previous value by 2. Compounding multiplication always overtakes polynomial growth eventually, no matter how large the polynomial's degree."
```

## Explainer

You already know how to work with expressions like 2³ or 5⁴ from your study of exponent rules. An exponential *function* takes that idea and lets the exponent be a variable: f(x) = 2^x means the base is fixed at 2 and x — the input — is the exponent. This flip in roles is what makes exponential functions behave so differently from polynomials like x² or x³, where x is the base.

The graph of f(x) = b^x has several features that follow directly from the algebra. When x = 0, any nonzero base raised to the 0 power equals 1, so the graph always passes through (0, 1). For large positive x with b > 1, the function grows rapidly — each unit step multiplies the output by b. For large negative x, the exponents are large negative numbers, so the output becomes a very small positive fraction, approaching zero but never reaching it. This is why y = 0 is a horizontal asymptote: the function gets arbitrarily close but can never equal zero, because b raised to any real power is always positive.

Decay is not a different kind of function — it is the same structure with a base between 0 and 1. The function (1/2)^x gets smaller as x increases, because repeatedly multiplying by 1/2 halves the value each time. Using your exponent rules: (1/2)^x = 2^(-x), which means the decay curve is exactly the growth curve reflected across the y-axis. This connection between growth and decay is worth internalizing — it means you only need to understand one shape.

The comparison with polynomial growth is one of the most important conceptual ideas here. For small values of x, x² or x¹⁰⁰ can dwarf 2^x. But eventually the exponential wins, because in 2^x the exponent keeps growing and each step multiplies by a constant factor. The polynomial only adds; the exponential compounds. This is why population growth, compound interest, and viral spread are all modeled exponentially — the pattern of "multiply by a constant ratio each period" is precisely what these phenomena share.

Transformations of exponential functions follow the same rules you have seen with other functions: f(x) = a · b^(x - h) + k shifts the graph horizontally by h, vertically by k, and stretches it by a. The asymptote shifts from y = 0 to y = k. When you encounter logarithms next, you will find that they are defined specifically to answer the question "for what x does b^x equal this value?" — the exponential and logarithmic functions are inverses of each other, which is why understanding the graph of 2^x now will make logarithms much more intuitive.
