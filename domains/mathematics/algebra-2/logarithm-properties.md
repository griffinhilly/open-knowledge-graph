---
id: logarithm-properties
title: Logarithm Properties
domain: mathematics
course: algebra-2
prerequisites:
  - id: logarithms-intro
    type: hard
  - id: exponent-rules-product-power-quotient
    type: hard
builds-toward:
  - solving-exponential-equations
  - solving-logarithmic-equations
tags: [logarithms, properties, product-rule, quotient-rule, power-rule]
stage: formal-systems
status: validated
---

# Logarithm Properties

## Core Idea
Logarithm properties mirror exponent rules: Product Rule: log_b(MN) = log_b(M) + log_b(N). Quotient Rule: log_b(M/N) = log_b(M) - log_b(N). Power Rule: log_b(M^p) = p*log_b(M). Change of Base: log_b(x) = log_a(x)/log_a(b). These properties allow expansion, condensation, and evaluation of logarithmic expressions and are essential for solving exponential and logarithmic equations.

## How It's Best Learned
Derive each property from the corresponding exponent rule. Practice expanding single logarithms into sums/differences and condensing sums/differences into single logarithms. Use the change of base formula to evaluate logarithms with unusual bases on a calculator. Give problems that require multiple properties in combination.

## Common Misconceptions
- Applying the product rule to log(M + N) (there is no simplification for log of a sum).
- Thinking log(M/N) = log(M)/log(N) (the quotient rule gives subtraction, not division of logs).
- Confusing log(M^p) = p*log(M) with (log M)^p.
- Forgetting that these properties require M, N > 0.

## Questions

```yaml
- question: "Which expression is equivalent to log(12)?"
  type: multiple-choice
  options: ["log(2) · log(6)", "log(4) + log(3)", "log(8) + log(4)", "log(2) + log(10)"]
  answer: 1
  explanation: "By the product rule, log(M · N) = log(M) + log(N). Since 4 × 3 = 12, log(4) + log(3) = log(12). Option A has no logarithm rule for products of logs (that would give log(2^log(6)), not log(12)). Option C gives log(32) and option D gives log(20)."

- question: "log(M + N) = log(M) + log(N) for any positive M and N."
  type: true-false
  answer: false
  explanation: "The product rule says log(M · N) = log(M) + log(N) — it applies to the log of a product, not a sum. There is no simplification rule for log(M + N). For example, log(10 + 10) = log(20) ≈ 1.30, but log(10) + log(10) = 1 + 1 = 2. Confusing addition inside the log with addition outside the log is the most common logarithm error."

- question: "Use the power rule to explain step-by-step why log₂(8) = 3."
  type: short-answer
  answer: "8 = 2³, so log₂(8) = log₂(2³) = 3 · log₂(2) = 3 · 1 = 3"
  explanation: "The power rule states log_b(M^p) = p · log_b(M). Recognizing that 8 = 2³ lets you rewrite the argument as a power of the base, then pull the exponent out front. Since log_b(b) = 1 always, log₂(2) = 1, so the result is 3 · 1 = 3. This shows the power rule is consistent with the definition of logarithm."
```

## Explainer

Logarithm properties are not arbitrary rules to memorize — they are the direct mirror images of exponent rules you already know. If you understand why exponent rules work, logarithm properties follow naturally.

Recall that exponents have a product rule: b^m · b^n = b^(m+n). Logarithms are exponents (log_b(x) asks "what exponent gives x?"), so taking the log of a product M · N means adding the exponents that produce M and N: log_b(MN) = log_b(M) + log_b(N). The quotient rule follows the same logic in reverse: b^m / b^n = b^(m-n), so log_b(M/N) = log_b(M) − log_b(N). And the power rule (b^m)^p = b^(mp) translates to log_b(M^p) = p · log_b(M) — the exponent moves in front as a multiplier.

The most important thing to notice is what these rules do NOT say. The product rule applies to log(M · N), not to log(M + N). There is no simplification for the logarithm of a sum. This is the most common error in logarithm work — writing log(x + 3) = log(x) + log(3) when that transformation is simply invalid. Whenever you see a sum or difference inside a logarithm, stop: no rule applies.

These properties let you do two powerful things: expand and condense. Expanding means rewriting a single logarithm as a sum or difference (useful for solving equations): log(x²y/z) = 2log(x) + log(y) − log(z). Condensing means combining a sum or difference into a single logarithm (also useful for solving): 2log(x) + log(y) − log(z) = log(x²y/z). Problems may ask for either direction, so practice recognizing which form you're starting with and which you're trying to reach.

The change-of-base formula, log_b(x) = log(x)/log(b), is a practical tool rather than a structural property. It lets you evaluate any logarithm on a calculator that only has log base 10 or ln (natural log). For example, log₅(125) = log(125)/log(5) = 2.097/0.699 = 3. (You can verify: 5³ = 125.) When solving exponential equations with unusual bases — like 3^x = 50 — the change-of-base formula is often the final step that produces a numerical answer.
