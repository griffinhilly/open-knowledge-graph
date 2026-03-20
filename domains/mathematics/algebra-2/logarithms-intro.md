---
id: logarithms-intro
title: Logarithms Introduction
domain: mathematics
course: algebra-2
prerequisites:
  - id: exponential-functions-and-graphs
    type: hard
  - id: inverse-functions
    type: hard
builds-toward:
  - logarithm-properties
  - solving-logarithmic-equations
  - natural-logarithm-and-e
tags: [logarithms, inverse, exponential, definition]
stage: formal-systems
status: validated
---

# Logarithms Introduction

## Core Idea
A logarithm answers the question: "To what exponent must we raise the base to get this number?" Formally, log_b(x) = y means b^y = x. The logarithm function is the inverse of the exponential function. Key values: log_b(1) = 0, log_b(b) = 1, log_b(b^n) = n. Common logarithm: log(x) = log_10(x). Natural logarithm: ln(x) = log_e(x). The domain of log_b(x) is x > 0.

## How It's Best Learned
Start with the conversion between exponential and logarithmic forms: 2^3 = 8 means log_2(8) = 3. Practice converting in both directions. Evaluate logarithms by asking "what exponent gives me this?" Graph y = log_b(x) as the reflection of y = b^x over y = x. Emphasize that log is undefined for zero and negative numbers.

## Common Misconceptions
- Thinking log_b(0) is defined (it is not; you cannot raise a positive base to any power and get 0).
- Confusing log_b(x) with b*x or x/b (log is an exponent, not multiplication or division).
- Not recognizing that log and ln are the same concept with different bases.
- Thinking log(a + b) = log(a) + log(b) (this is wrong; the product rule is log(a*b) = log(a) + log(b)).

## Questions

```yaml
- question: "What is log_2(32)?"
  type: multiple-choice
  options: ["4", "5", "16", "6"]
  answer: 1
  explanation: "log_2(32) asks: 'To what power must we raise 2 to get 32?' Since 2^5 = 32, the answer is 5. A common error is confusing log_2(32) with 32/2 = 16 or with 2 × 32. Logarithms are exponents, not multiplication or division."

- question: "log(a + b) = log(a) + log(b) for any positive values of a and b."
  type: true-false
  answer: false
  explanation: "This is one of the most common logarithm errors. The product rule states log(a × b) = log(a) + log(b) — multiplication inside the log becomes addition outside. There is no corresponding rule for log(a + b). For example, log(1 + 9) = log(10) = 1, but log(1) + log(9) = 0 + log(9) ≈ 0.954, which is different."

- question: "Why is log_b(x) undefined when x = 0 or when x is negative?"
  type: short-answer
  answer: "log_b(x) = y means b^y = x. For any positive base b, b^y is always positive regardless of what y is — you cannot raise a positive number to any real power and get 0 or a negative result. So there is no real exponent y that satisfies b^y = 0 or b^y = -5, making the logarithm undefined for non-positive inputs."
  explanation: "This connects directly to the prerequisite topic on exponential functions: the range of b^y (for b > 0, b ≠ 1) is the set of all positive real numbers. Since the logarithm is the inverse of the exponential, its domain must be exactly the range of the exponential — positive reals only. The domain restriction is a consequence of the inverse relationship, not an arbitrary rule."
```

## Explainer

You already know exponential functions: equations like y = 2^x, where the base is fixed and the exponent varies. You can ask: "If x = 3, what is y?" and quickly get y = 8. Logarithms let you run this question in reverse: "If y = 8 and the base is 2, what was x?" The answer — the exponent — is what the logarithm gives you. Formally, log_2(8) = 3, because 2^3 = 8.

This inverse relationship is the entire foundation. Every logarithm statement is secretly an exponential statement in disguise. log_b(x) = y means exactly the same thing as b^y = x. Converting fluently between these two forms — "exponential form" and "logarithmic form" — is the first skill to develop. For example, 10^2 = 100 translates to log_10(100) = 2, and log_3(9) = 2 translates to 3^2 = 9. When you are stuck evaluating a logarithm, convert to exponential form and ask: "What exponent makes this true?"

Because logarithms are inverses of exponentials, their graph is the reflection of y = b^x over the line y = x. The exponential function has a horizontal asymptote at y = 0 (it approaches zero but never reaches it), which becomes a vertical asymptote at x = 0 for the logarithm. This explains the domain restriction: log_b(x) is only defined for x > 0. You cannot ask "what exponent gives me 0?" because no real power of a positive base ever equals zero. And you cannot ask "what exponent gives me -5?" for the same reason. The domain restriction is not arbitrary — it flows directly from the range of the exponential function.

Some logarithms are used so frequently they get special names. log_10(x), written simply as log(x), is called the common logarithm and is used extensively in science (pH, decibels, the Richter scale). log_e(x), written as ln(x), is the natural logarithm with base e ≈ 2.718. Both behave identically to log_b(x) with their respective bases; the choice of base changes the scale but not the underlying concept. You will explore natural logarithms and their special properties — particularly in calculus — in a dedicated topic.

A misconception worth addressing directly: logarithms are not a form of multiplication. log_b(x) is not b times x or x divided by b — it is an exponent. This confusion leads to the false belief that log(a + b) = log(a) + log(b), by analogy with distribution. The actual rule is log(a × b) = log(a) + log(b): multiplication inside the logarithm becomes addition outside. This is a consequence of exponent rules (b^m × b^n = b^{m+n}), which you will prove and apply in the next topic on logarithm properties.
