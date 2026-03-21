---
id: scientific-notation-operations
title: Operations with Scientific Notation
domain: mathematics
course: prealgebra
prerequisites:
- id: scientific-notation-intro
  type: hard
- id: exponent-rules-product-power-quotient
  type: soft
- id: negative-exponents
  type: soft
builds-toward: []
tags:
- scientific-notation
- exponents
- multiplication
- division
stage: abstract-reasoning
status: validated
---
# Operations with Scientific Notation

## Core Idea
Multiplying and dividing numbers in scientific notation leverages exponent rules to keep calculations manageable. To multiply, multiply the coefficients and add the exponents: (3 × 10⁴)(2 × 10⁵) = 6 × 10⁹. To divide, divide the coefficients and subtract the exponents: (8 × 10⁷) / (4 × 10³) = 2 × 10⁴. If the resulting coefficient falls outside the range 1 to 10, adjust it by shifting the decimal and compensating the exponent. This skill is essential in science and engineering, where quantities like distances, masses, and speeds span many orders of magnitude.

## How It's Best Learned
Have students practice multiplication and division separately before mixing operations. Emphasize the two-step process: handle coefficients and powers of ten independently, then adjust if the coefficient is not between 1 and 10. Use real-world science problems (e.g., speed of light times travel time) to reinforce why the notation matters.

## Common Misconceptions
- Multiplying the exponents instead of adding them when multiplying numbers in scientific notation.
- Forgetting to re-adjust the coefficient when the product or quotient falls outside [1, 10) — for example, leaving an answer as 12 × 10⁵ instead of converting to 1.2 × 10⁶.

## Questions

```yaml
- question: "What is the correct result of (4 × 10³) × (5 × 10⁴)?"
  type: multiple-choice
  options:
    - "20 × 10¹² — multiply both the coefficients and the exponents"
    - "9 × 10⁷ — add the coefficients and add the exponents"
    - "2.0 × 10⁸ — multiply the coefficients, add the exponents, then adjust to proper form"
    - "20 × 10⁷ — multiply the coefficients and add the exponents, but forget to adjust"
  answer: 2
  explanation: "Step 1: Multiply coefficients: 4 × 5 = 20. Step 2: Add exponents: 3 + 4 = 7. Intermediate result: 20 × 10⁷. Step 3: Adjust — 20 is not in [1, 10), so rewrite as 2.0 × 10¹, compensating the exponent: 2.0 × 10⁸. Option A (multiplying exponents) is the most common error — exponent rules say 10³ × 10⁴ = 10^(3+4), not 10^(3×4). Option D is partially correct but leaves the answer in non-standard form."

- question: "What is (6 × 10⁸) ÷ (3 × 10⁵)?"
  type: multiple-choice
  options:
    - "2 × 10³"
    - "2 × 10¹³"
    - "3 × 10³"
    - "18 × 10³"
  answer: 0
  explanation: "Step 1: Divide the coefficients: 6 ÷ 3 = 2. Step 2: Subtract the exponents: 8 − 5 = 3. Result: 2 × 10³. No adjustment needed since 2 is already in [1, 10). Option B (2 × 10¹³) is the 'add instead of subtract' error — confusing multiplication rules with division. Option D (18 × 10³) results from multiplying the coefficients instead of dividing."

- question: "When multiplying two numbers in scientific notation, you multiply the coefficients and also multiply the exponents of 10."
  type: true-false
  answer: false
  explanation: "You ADD the exponents, not multiply them. This follows from the product rule for exponents: 10ᵃ × 10ᵇ = 10^(a+b). Multiplying the exponents would give 10^(a×b), which is a much larger (or smaller) number and produces a wrong answer. For example, (10²)(10³) = 10⁵, not 10⁶. The confusion likely arises because you do multiply the coefficients — so students mistakenly apply multiplication to the exponents as well."

- question: "After multiplying (3 × 10⁷) by (4 × 10²), the intermediate result 12 × 10⁹ must be rewritten as 1.2 × 10¹⁰ to be in proper scientific notation."
  type: true-false
  answer: true
  explanation: "Scientific notation requires the coefficient to be at least 1 and less than 10. The intermediate result 12 × 10⁹ has a coefficient of 12, which is outside the valid range. Moving the decimal one place left in 12 gives 1.2 (dividing by 10), so the exponent must increase by 1 to compensate (multiplying by 10): 12 × 10⁹ = 1.2 × 10¹⁰. This adjustment step is required to write the answer in standard scientific notation form."

- question: "Describe the two-step process for multiplying two numbers in scientific notation, and explain why an adjustment step is sometimes needed afterward."
  type: short-answer
  answer: "Step 1: Multiply the coefficients together and add the exponents: (a × 10ᵐ)(b × 10ⁿ) = (a × b) × 10^(m+n). Step 2: If the resulting coefficient is not in [1, 10), adjust it by shifting the decimal point and compensating the exponent. For example, if the coefficient is 15, rewrite as 1.5 × 10¹ and increase the exponent by 1. If the coefficient is 0.3, rewrite as 3 × 10⁻¹ and decrease the exponent by 1."
  explanation: "The adjustment is needed because the product of two coefficients that are each in [1, 10) can range from 1 up to just under 100 — so it may need one decimal shift. This is not an error to fix; it is an expected part of the procedure. Similarly for division: dividing two coefficients in [1, 10) can give a result less than 1, requiring a shift in the other direction."
```
