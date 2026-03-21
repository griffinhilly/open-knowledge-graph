---
id: integer-order-of-operations
title: Integer Order of Operations
domain: mathematics
course: prealgebra
prerequisites:
  - id: order-of-operations
    type: hard
  - id: adding-integers
    type: hard
  - id: subtracting-integers
    type: hard
  - id: multiplying-integers
    type: hard
  - id: dividing-integers
    type: hard
builds-toward:
  - variable-expressions
  - one-step-equations
tags: [order-of-operations, integers, PEMDAS]
stage: abstract-reasoning
status: validated
---

# Integer Order of Operations

## Core Idea
The order of operations (PEMDAS/GEMS) learned with whole numbers applies identically when integers are involved: parentheses first, then exponents, then multiplication and division left to right, then addition and subtraction left to right. The challenge here is that negative signs introduce new opportunities for error at every step. An expression like −3² evaluates to −9 (square 3 first, then negate), while (−3)² = 9. Mastering order of operations with integers is the bridge between arithmetic and algebraic expression evaluation.

## How It's Best Learned
Give students expressions with increasing complexity: start with two operations, then three, then nested parentheses. Emphasize writing out each step on a new line rather than trying to do multiple operations at once. Highlight the distinction between −3² and (−3)² with explicit discussion. Use error-analysis exercises where students find and correct mistakes in worked examples.

## Common Misconceptions
- The most common error: treating −3² as (−3)² = 9 instead of −(3²) = −9.
- Students sometimes do addition before multiplication when the addition "comes first" reading left to right.
- Forgetting that multiplication and division are equal priority (left to right), as are addition and subtraction.

## Questions

```yaml
- question: "What is the value of −5²?"
  type: multiple-choice
  options:
    - "25, because squaring a negative gives a positive"
    - "−25, because exponentiation applies to 5 first, then the negation is applied"
    - "−10, because −5² means −5 + (−5)"
    - "0, because −5 and 5 cancel each other"
  answer: 1
  explanation: "−5² means −(5²) = −(25) = −25. The exponent applies only to the base 5, not to the negative sign in front. Negation is treated as multiplication by −1, which has lower precedence than exponentiation in the order of operations. If you wanted to square the entire quantity including the negative, you would write (−5)² = (−5)(−5) = 25. The distinction between −5² and (−5)² is one of the most consequential single-character differences in arithmetic."

- question: "A student evaluates 8 − (−4 + 6) and gets 18. Which mistake explains this error?"
  type: multiple-choice
  options:
    - "They evaluated addition before subtraction even though subtraction comes first reading left to right"
    - "They distributed the subtraction incorrectly — treating −(−4 + 6) as +(−4) + 6 instead of subtracting the entire quantity (which equals 2)"
    - "They computed −4 + 6 as −2 instead of +2"
    - "They forgot to apply parentheses before subtraction"
  answer: 1
  explanation: "The correct evaluation: −4 + 6 = 2, then 8 − 2 = 6. The student got 18 by treating 8 − (−4 + 6) as 8 − (−4) + 6 = 8 + 4 + 6 = 18. This error comes from incorrectly distributing the subtraction: they flipped the sign of −4 to get +4, but then also kept the +6 instead of negating it. When subtracting a parenthetical expression, the subtraction applies to the entire result inside — not to each term separately unless you distribute a negative sign across all terms, which would give 8 + 4 − 6 = 6."

- question: "−3² and (−3)² evaluate to the same number because both expressions involve squaring something negative."
  type: true-false
  answer: false
  explanation: "−3² = −(3²) = −9, while (−3)² = (−3)(−3) = 9. They differ by a sign of 18. The difference is what is being squared: in −3², only the 3 is squared and the negative is applied afterward. In (−3)², the entire quantity −3 is squared. The parentheses literally change the base of the exponent from 3 to −3, which changes the result entirely. This is one of the most important distinctions in integer arithmetic."

- question: "In the expression −2 · (−3) · (−4), the product is negative because there is an odd number of negative factors."
  type: true-false
  answer: true
  explanation: "Counting negative factors is a reliable shortcut for determining the sign of a product or quotient: an even count of negative factors gives a positive result; an odd count gives a negative result. Here there are three negative factors (−2, −3, −4), which is odd, so the product is negative. Checking: (−2)(−3) = 6, then 6 · (−4) = −24. The shortcut works because each pair of negatives cancels to a positive, and one negative is left over."

- question: "Explain why −3² equals −9 rather than 9. What order-of-operations rule governs this, and how does writing (−3)² instead change the result?"
  type: short-answer
  answer: "In −3², the order of operations requires exponentiation before any multiplication (including the implicit multiplication by −1 that represents negation). So the 3 is squared first to get 9, and then the negative sign is applied: −(9) = −9. In (−3)², the parentheses change what is being squared — now the entire quantity −3 is the base of the exponent, so (−3)² = (−3)(−3) = 9. The parentheses move the negative sign inside the base, so it participates in the squaring rather than being applied afterward."
  explanation: "The core insight is that negation is not the same as being part of the base. Without parentheses, the negative sign is an operation applied to the result of the exponentiation, not a property of the number being raised to a power. This is why −x² is always non-positive (for real x), while (−x)² = x² is always non-negative — a distinction with major consequences in algebra."
```

## Explainer

You already know how to add, subtract, multiply, and divide integers, and you've learned the basic order of operations with whole numbers. The challenge in this topic isn't a new rule — the order of operations is identical — it's that negative signs create new traps at every step that don't exist with positive numbers. Mastering this topic means learning to see those traps before you fall into them.

The most important trap is the **sign of a negated exponent**. When you see −3², the exponent is applied to 3 first (giving 9), and then negated (giving −9). This is because negation is treated as multiplication by −1, and multiplication happens *after* exponentiation in the order of operations. If you wanted (−3)², you'd need the parentheses: the negative is now inside, so the squaring applies to the entire quantity −3, giving (−3)² = (−3)(−3) = 9. This single distinction — −3² = −9 but (−3)² = 9 — accounts for an enormous number of errors in algebra and beyond.

The second key challenge is tracking signs through multiplication and division. You know that a negative times a negative is positive, and a negative times a positive is negative. But in a chain like −2 · (−3) · (−4) · 5, you must count negative factors: three negatives multiply to give a negative result (since negative × negative = positive, then positive × negative = negative). Rushing through these steps without tracking the sign at each stage is where errors creep in. A reliable strategy is to determine the sign of the final answer first (count negatives: even → positive, odd → negative), then multiply the absolute values separately.

The third trap is in mixed addition and subtraction with negatives. An expression like 8 − (−3 + 7) requires careful parentheses work. The subtraction of the entire quantity (−3 + 7) = 4 gives 8 − 4 = 4. If you instead distribute the subtraction — treating it as 8 − (−3) + 7 = 8 + 3 + 7 = 18 — you've made an error. When subtracting a parenthetical, the subtraction applies to the entire result of what's inside; you can only distribute it if you flip every sign inside. Writing out each step on its own line, never skipping operations, is the surest way to evaluate these expressions correctly. The rules haven't changed from whole numbers — only the opportunities for sign errors have multiplied.
