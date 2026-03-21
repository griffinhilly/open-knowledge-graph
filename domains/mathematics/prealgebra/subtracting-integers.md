---
id: subtracting-integers
title: Subtracting Integers
domain: mathematics
course: prealgebra
prerequisites:
- id: adding-integers
  type: hard
- id: absolute-value
  type: soft
- id: opposites-and-additive-inverses
  type: soft
builds-toward:
- integer-order-of-operations
- one-step-equations
- combining-like-terms
tags:
- integers
- subtraction
- operations
stage: abstract-reasoning
status: validated
---
# Subtracting Integers

## Core Idea
Subtracting an integer is equivalent to adding its opposite: a − b = a + (−b). This single rule converts every subtraction problem into an addition problem, which students already know how to handle. For example, 3 − (−5) = 3 + 5 = 8, and −2 − 4 = −2 + (−4) = −6. The "add the opposite" rule is not just a trick — it reflects the deep algebraic structure that subtraction is not a separate operation but addition with an inverse. This concept is essential for simplifying expressions, solving equations, and working with polynomials.

## How It's Best Learned
Demonstrate on the number line: subtracting a positive means moving left, subtracting a negative means moving right (reversing direction). Use integer chip models to show that removing a negative chip is the same as adding a positive one. Once students see why the rule works, practice converting subtraction to addition before computing. Emphasize double negatives: −(−5) = +5.

## Common Misconceptions
- Students often struggle with subtracting a negative, writing 3 − (−5) = −2 instead of 8.
- Some students think "two negatives make a positive" applies universally, not just when a negative is subtracted.
- Forgetting to convert subtraction to addition before applying integer addition rules.

## Questions

```yaml
- question: "A student evaluates 3 − (−5) and writes the answer as −2. Which error most likely caused this?"
  type: multiple-choice
  options:
    - "They added 3 and 5 to get 8, then incorrectly applied a negative sign"
    - "They subtracted 5 from 3, ignoring the negative sign on −5"
    - "They correctly applied the 'add the opposite' rule but made an arithmetic error"
    - "They converted the problem to −3 + 5 instead of 3 + 5"
  answer: 1
  explanation: "The answer −2 results from computing 3 − 5 = −2 — the student dropped the negative sign on −5 and just subtracted 5. The correct application of 'add the opposite' converts 3 − (−5) to 3 + 5 = 8. Subtracting a negative number is the same as adding a positive, so the answer moves right on the number line (increases), not left."

- question: "Which of the following is equivalent to −4 − (−9)?"
  type: multiple-choice
  options:
    - "−4 − 9"
    - "−4 + 9"
    - "4 − 9"
    - "4 + 9"
  answer: 1
  explanation: "Subtracting a number is the same as adding its opposite: a − b = a + (−b). So −4 − (−9) = −4 + 9 = 5. The opposite of −9 is +9. Options A and C fail to apply the conversion rule. Option D incorrectly flips the sign of −4 as well. Once you convert to −4 + 9, apply integer addition rules: different signs, so subtract absolute values (9 − 4 = 5) and keep the sign of the larger absolute value (positive), giving 5."

- question: "The expression −7 − 3 and the expression −7 + (−3) are equivalent."
  type: true-false
  answer: true
  explanation: "This is the 'add the opposite' rule directly: subtracting 3 is the same as adding −3. Both expressions give −7 + (−3) = −10. Same signs, so add the absolute values (7 + 3 = 10) and keep the negative sign. This example shows that the conversion rule always works, even when the subtracted number is positive."

- question: "Subtracting a negative number always produces a negative result."
  type: true-false
  answer: false
  explanation: "Subtracting a negative is the same as adding a positive, which increases the value — the result depends on both numbers. 3 − (−5) = 3 + 5 = 8, which is positive. Even −2 − (−10) = −2 + 10 = 8, also positive. The result can be positive, negative, or zero depending on the starting value and the size of the subtracted negative. The 'two negatives' in a subtraction expression signal that you move right (add), not that the answer is negative."

- question: "Explain in your own words why subtracting a negative number gives the same result as adding a positive number. Use either number line reasoning or algebraic reasoning."
  type: short-answer
  answer: "Algebraically: subtraction is defined as adding the opposite, so a − b = a + (−b). When b is already negative, say b = −5, the opposite of b is −(−5) = +5. So a − (−5) = a + 5. On a number line: subtracting a positive moves left; subtracting a negative reverses that direction, so you move right — exactly the same as adding a positive. Integer chips say the same: removing a negative chip (−) from a pile has the same net effect as adding a positive chip (+)."
  explanation: "All three models — algebraic, geometric (number line), and physical (chips) — point to the same conclusion: the two negatives in 'subtract a negative' cancel out, producing a positive additive effect. The rule isn't arbitrary; it's a consequence of the definition of subtraction and the meaning of negative numbers."
```

## Explainer

From adding integers, you know how to handle sums like (−3) + (−5) = −8 and 7 + (−4) = 3. Subtraction of integers builds directly on this: the core rule is that **subtracting a number is the same as adding its opposite**. Written algebraically: a − b = a + (−b). This is not a trick or a shortcut — it is a definition. Subtraction is literally just addition with a sign flip on the second number. Once you apply this rule, every subtraction problem becomes an addition problem you already know how to solve.

Try it on a few examples. 9 − 4 becomes 9 + (−4) = 5, which matches the ordinary arithmetic you already know. Now the interesting cases: 3 − (−5) becomes 3 + (+5) = 8. Subtracting a negative flips it to a positive — you move right on the number line, not left. And −2 − 7 becomes −2 + (−7) = −9. On the number line, subtracting a positive number means moving left: you start at −2 and move 7 units left to reach −9.

The **number line** makes this geometric. Moving right corresponds to adding a positive; moving left corresponds to subtracting a positive (or equivalently, adding a negative). Here is the key insight for double negatives: subtracting a negative means reversing the left-going direction — so you move right instead. Subtracting −5 is the same as moving 5 units to the right, just like adding +5. Integer chip models say the same thing differently: removing a negative chip from a pile has the same net effect as adding a positive chip. Whether you think about it geometrically or algebraically, the conclusion is identical: two negatives in a subtraction produce a positive effect.

The procedure to follow every time: (1) rewrite the subtraction as addition of the opposite, (2) then apply your integer addition rules. Never try to "compute" a subtraction involving negatives without converting first — this is where errors creep in. For example, (−6) − (−2): convert to (−6) + 2, then apply the rule for adding integers with different signs: |6| − |2| = 4, keep the sign of the larger absolute value (negative), result = −4. Step 1 (convert) and Step 2 (add) are two separate, clean operations that together handle any integer subtraction correctly.
