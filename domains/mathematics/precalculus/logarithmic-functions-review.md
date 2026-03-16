---
id: logarithmic-functions-review
title: Logarithmic Functions Review
domain: mathematics
course: precalculus
prerequisites:
  - id: exponential-functions-review
    type: hard
  - id: inverse-functions-review
    type: hard
builds-toward:
  - derivatives-of-logarithmic-functions
tags: [logarithms, inverse, exponential]
stage: formal-systems
status: validated
---

# Logarithmic Functions Review

## Core Idea
The logarithm log_b(x) is the inverse of the exponential function b^x: it answers "what exponent of b gives x?" The natural logarithm ln(x) = log_e(x) is the inverse of e^x. Logarithm laws (product, quotient, power rules) convert multiplication into addition, making them essential for solving exponential equations. The natural logarithm has the simplest derivative (1/x), making it central to calculus.

## How It's Best Learned
Connect logs to exponents through the equivalence: log_b(x) = y means b^y = x. Practice converting between exponential and logarithmic forms. Master the three log laws and use them to expand and condense expressions. Solve exponential equations by taking logarithms of both sides.

## Common Misconceptions
- Believing log(a + b) = log(a) + log(b): there is no sum rule for logarithms.
- Confusing ln(x) with log(x): in math, ln means base e; in many calculators, log means base 10.
- Forgetting that the domain of log(x) is x > 0 only.

## Explainer

From inverse functions, you know the central idea: if f and f⁻¹ are inverses, then f⁻¹(f(x)) = x and f(f⁻¹(x)) = x, and the graph of f⁻¹ is the reflection of f across the line y = x. You also know exponential functions: f(x) = bˣ takes any real exponent and returns a positive output. The **logarithm** log_b(x) is simply the inverse of bˣ. Asking "what is log_b(x)?" is asking "what power of b gives x?" — that is, log_b(x) = y means exactly bʸ = x. This single equivalence converts every log question into an exponential question and vice versa.

The domain and range swap in the expected way. Since bˣ has domain all reals and range (0, ∞), its inverse log_b(x) has domain (0, ∞) and range all reals. This is why log(0) and log(negative) are undefined — there is no real exponent that makes b raised to it equal to 0 or a negative number. The graph of log_b(x) is the exponential curve reflected over y = x: it passes through (1, 0) since b⁰ = 1, rises slowly to the right, and falls toward −∞ as x → 0⁺.

The three **logarithm laws** are the most useful computational tools, and each one is a direct restatement of an exponent rule. The **product rule** log_b(xy) = log_b(x) + log_b(y) restates bᵐ · bⁿ = bᵐ⁺ⁿ: multiplying two numbers corresponds to adding their exponents. The **quotient rule** log_b(x/y) = log_b(x) − log_b(y) restates bᵐ/bⁿ = bᵐ⁻ⁿ. The **power rule** log_b(xⁿ) = n · log_b(x) restates (bᵐ)ⁿ = bᵐⁿ. Historically, logarithms were invented *because* of the product rule — multiplying large numbers is hard, but adding their logarithms is easy, so 17th-century astronomers computed products as sums using log tables.

The **natural logarithm** ln(x) = log_e(x), where e ≈ 2.718, holds a special place because of calculus: d/dx[ln(x)] = 1/x, the cleanest derivative among all logarithms. Any base-b logarithm can be converted using the **change of base formula**: log_b(x) = ln(x)/ln(b). This means a single logarithm function is sufficient for computation — calculators typically provide ln and log₁₀, and everything else can be derived. To solve exponential equations like 3ˣ = 17, take ln of both sides: x = ln(17)/ln(3).
