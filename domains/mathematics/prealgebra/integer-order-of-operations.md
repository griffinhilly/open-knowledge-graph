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

## Explainer

You already know how to add, subtract, multiply, and divide integers, and you've learned the basic order of operations with whole numbers. The challenge in this topic isn't a new rule — the order of operations is identical — it's that negative signs create new traps at every step that don't exist with positive numbers. Mastering this topic means learning to see those traps before you fall into them.

The most important trap is the **sign of a negated exponent**. When you see −3², the exponent is applied to 3 first (giving 9), and then negated (giving −9). This is because negation is treated as multiplication by −1, and multiplication happens *after* exponentiation in the order of operations. If you wanted (−3)², you'd need the parentheses: the negative is now inside, so the squaring applies to the entire quantity −3, giving (−3)² = (−3)(−3) = 9. This single distinction — −3² = −9 but (−3)² = 9 — accounts for an enormous number of errors in algebra and beyond.

The second key challenge is tracking signs through multiplication and division. You know that a negative times a negative is positive, and a negative times a positive is negative. But in a chain like −2 · (−3) · (−4) · 5, you must count negative factors: three negatives multiply to give a negative result (since negative × negative = positive, then positive × negative = negative). Rushing through these steps without tracking the sign at each stage is where errors creep in. A reliable strategy is to determine the sign of the final answer first (count negatives: even → positive, odd → negative), then multiply the absolute values separately.

The third trap is in mixed addition and subtraction with negatives. An expression like 8 − (−3 + 7) requires careful parentheses work. The subtraction of the entire quantity (−3 + 7) = 4 gives 8 − 4 = 4. If you instead distribute the subtraction — treating it as 8 − (−3) + 7 = 8 + 3 + 7 = 18 — you've made an error. When subtracting a parenthetical, the subtraction applies to the entire result of what's inside; you can only distribute it if you flip every sign inside. Writing out each step on its own line, never skipping operations, is the surest way to evaluate these expressions correctly. The rules haven't changed from whole numbers — only the opportunities for sign errors have multiplied.
