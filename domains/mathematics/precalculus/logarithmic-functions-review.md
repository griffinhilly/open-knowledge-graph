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

## Questions

```yaml
- question: "A student writes: log(5 + 3) = log(5) + log(3). What is wrong?"
  type: multiple-choice
  options:
    - "Nothing — the sum rule for logarithms is valid for positive values"
    - "The product rule applies instead: log(5 + 3) should equal log(5) · log(3)"
    - "There is no sum rule for logarithms; log(5 + 3) = log(8), which cannot be further simplified using log laws"
    - "The student should have written log(5 + 3) = log(5) − log(3)"
  answer: 2
  explanation: "The logarithm product rule converts multiplication into addition: log(xy) = log(x) + log(y). There is no analogous rule for sums — log(a + b) does not simplify further using log laws and is not equal to log(a) + log(b). This is one of the most common student errors. The correct evaluation is simply log(8). Confusing the product rule with a nonexistent sum rule likely comes from over-generalizing the product → addition pattern."

- question: "To solve 5^x = 12 for x, which approach is correct?"
  type: multiple-choice
  options:
    - "x = 12/5"
    - "x = log(12) · log(5)"
    - "x = ln(12) / ln(5), using the change-of-base formula after taking logarithms of both sides"
    - "x = ln(12) − ln(5)"
  answer: 2
  explanation: "Taking ln of both sides gives ln(5^x) = ln(12), then using the power rule: x · ln(5) = ln(12), so x = ln(12)/ln(5). This is exactly the change-of-base formula. Option D (ln(12) − ln(5)) would be correct for ln(12/5), not ln(12)/ln(5) — another common confusion between quotient rule and change-of-base. Option A ignores the exponent structure entirely."

- question: "The function log_b(x) has domain (0, ∞) and range (−∞, ∞), because it is the inverse of b^x, whose domain is all reals and range is (0, ∞)."
  type: true-false
  answer: true
  explanation: "Inverting a function swaps domain and range. Since b^x accepts any real input and always produces a positive output, its inverse log_b(x) must accept only positive inputs and can produce any real output. This is why log(0) and log(negative) are undefined — there is no real exponent that makes b^x equal to 0 or a negative number."

- question: "The logarithm law log_b(a + b) = log_b(a) + log_b(b) holds for all positive values of a and b."
  type: true-false
  answer: false
  explanation: "There is no sum rule for logarithms. The product rule log_b(xy) = log_b(x) + log_b(y) converts multiplication into addition, but there is no corresponding identity for sums. For example, log(2 + 3) = log(5) ≈ 0.699, while log(2) + log(3) = log(6) ≈ 0.778 — these are not equal. This is listed as one of the most common misconceptions for this topic."

- question: "Why does the product rule log_b(xy) = log_b(x) + log_b(y) hold? Explain using what logarithms represent."
  type: short-answer
  answer: "A logarithm is an exponent: log_b(x) = m means b^m = x, and log_b(y) = n means b^n = y. Therefore xy = b^m · b^n = b^(m+n) by the exponent product rule. Taking log_b of both sides: log_b(xy) = m + n = log_b(x) + log_b(y). The product rule works because multiplying two numbers corresponds to adding their exponents — and log_b is asking 'what is the exponent?' So the product of the numbers corresponds exactly to the sum of their logarithms."
  explanation: "This derivation shows that all three log laws (product, quotient, power) are just restatements of exponent rules. If you forget a log law, you can re-derive it immediately from the corresponding exponent rule. This also explains why there is no sum rule: there is no exponent rule of the form b^(m+n) = b^m + b^n — exponents don't add when you add the bases."
```

## Explainer

From inverse functions, you know the central idea: if f and f⁻¹ are inverses, then f⁻¹(f(x)) = x and f(f⁻¹(x)) = x, and the graph of f⁻¹ is the reflection of f across the line y = x. You also know exponential functions: f(x) = bˣ takes any real exponent and returns a positive output. The **logarithm** log_b(x) is simply the inverse of bˣ. Asking "what is log_b(x)?" is asking "what power of b gives x?" — that is, log_b(x) = y means exactly bʸ = x. This single equivalence converts every log question into an exponential question and vice versa.

The domain and range swap in the expected way. Since bˣ has domain all reals and range (0, ∞), its inverse log_b(x) has domain (0, ∞) and range all reals. This is why log(0) and log(negative) are undefined — there is no real exponent that makes b raised to it equal to 0 or a negative number. The graph of log_b(x) is the exponential curve reflected over y = x: it passes through (1, 0) since b⁰ = 1, rises slowly to the right, and falls toward −∞ as x → 0⁺.

The three **logarithm laws** are the most useful computational tools, and each one is a direct restatement of an exponent rule. The **product rule** log_b(xy) = log_b(x) + log_b(y) restates bᵐ · bⁿ = bᵐ⁺ⁿ: multiplying two numbers corresponds to adding their exponents. The **quotient rule** log_b(x/y) = log_b(x) − log_b(y) restates bᵐ/bⁿ = bᵐ⁻ⁿ. The **power rule** log_b(xⁿ) = n · log_b(x) restates (bᵐ)ⁿ = bᵐⁿ. Historically, logarithms were invented *because* of the product rule — multiplying large numbers is hard, but adding their logarithms is easy, so 17th-century astronomers computed products as sums using log tables.

The **natural logarithm** ln(x) = log_e(x), where e ≈ 2.718, holds a special place because of calculus: d/dx[ln(x)] = 1/x, the cleanest derivative among all logarithms. Any base-b logarithm can be converted using the **change of base formula**: log_b(x) = ln(x)/ln(b). This means a single logarithm function is sufficient for computation — calculators typically provide ln and log₁₀, and everything else can be derived. To solve exponential equations like 3ˣ = 17, take ln of both sides: x = ln(17)/ln(3).
