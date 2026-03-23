---
id: multiplication-facts-6s-through-9s
title: 'Multiplication Facts: 6s, 7s, 8s, and 9s'
domain: mathematics
course: 3rd-grade
prerequisites:
- id: multiplication-facts-3s-4s
  type: hard
- id: commutative-property-multiplication
  type: soft
builds-toward:
- multiplication-facts-within-100
tags:
- facts
- multiplication
- fluency
stage: concrete-operations
status: validated
---

# Multiplication Facts: 6s, 7s, 8s, and 9s

## Core Idea
Complete the multiplication facts table: 6 × 1 through 9 × 9. The 9s facts have a pattern—digits sum to 9 and the tens digit is one less than the multiplier.

## How It's Best Learned
Derive unknown facts from known ones (e.g., 6 × 7 = (5 × 7) + 7). Use the commutative property to reduce facts to memorize.

## Common Misconceptions
Forgetting that 7 × 8 = 8 × 7; struggling with less obvious fact patterns.

## Questions

```yaml
- question: "A student can't remember 7 × 8. She knows 5 × 8 = 40 and 2 × 8 = 16. How can she figure out 7 × 8?"
  type: multiple-choice
  options:
    - "Add 40 + 16 = 56, because 5 groups of 8 plus 2 groups of 8 equals 7 groups of 8"
    - "Multiply 7 × 5 = 35, then multiply 7 × 8 separately and average them"
    - "Add 5 + 2 = 7 and then multiply 7 × 8 at the end"
    - "She cannot know without memorizing 7 × 8 directly"
  answer: 0
  explanation: "7 × 8 = (5 × 8) + (2 × 8) = 40 + 16 = 56. This uses the distributive property: 7 groups of 8 equals 5 groups of 8 plus 2 more groups of 8. Breaking an unknown fact into two known facts and combining them is the core fluency strategy. Option D is false — fluency includes deriving facts from known ones, not just retrieving them from memory."

- question: "Using the 9s pattern, what is 9 × 7?"
  type: multiple-choice
  options:
    - "54"
    - "81"
    - "63"
    - "72"
  answer: 2
  explanation: "For any 9s fact (9 × n): the tens digit of the product is n − 1, and the two digits sum to 9. For 9 × 7: tens digit = 7 − 1 = 6; ones digit = 9 − 6 = 3. Product = 63. Verification: 10 × 7 − 7 = 70 − 7 = 63 ✓. Option A (54) is 9 × 6; option B (81) is 9 × 9; option D (72) is 9 × 8."

- question: "If you know 4 × 9 = 36, you immediately know 9 × 4 = 36 without any additional calculation."
  type: true-false
  answer: true
  explanation: "The commutative property guarantees this. For every multiplication fact a × b = c, you also know b × a = c. This is especially valuable when learning the 6s through 9s, because many of those facts involve smaller numbers (like 4 × 6, 3 × 9) that you already know from the other direction. The commutative property doesn't just cut the total memorization burden in half — it specifically makes the harder facts feel more accessible."

- question: "The only way to reliably know 8 × 7 = 56 is to have memorized that specific fact directly, since it cannot be derived from other facts."
  type: true-false
  answer: false
  explanation: "Any multiplication fact can be derived from known facts using the distributive property. For 8 × 7: use 8 × 5 = 40, then add 8 × 2 = 16: 40 + 16 = 56. Or use 8 × 8 = 64 minus one group of 8: 64 − 8 = 56. Multiple derivation paths exist for every fact. The goal of fluency practice is to make these derivations so fast that the answer fires automatically — but the derivation routes are always there as backup."

- question: "Explain how to figure out 9 × 8 using the 9s pattern, then verify your answer using a different method."
  type: short-answer
  answer: "9s pattern: tens digit = 8 − 1 = 7; digits must sum to 9, so ones digit = 2; product = 72. Verification using 'ten minus one group': 10 × 8 − 8 = 80 − 8 = 72. ✓"
  explanation: "The 9s pattern is a reliable internal check: the tens digit is always one less than the multiplier, and the digits always sum to 9. For 9 × 8: 7 and 2, giving 72. The 'ten-minus-one-group' strategy is an independent verification path that also explains WHY the pattern works — multiplying by 9 is the same as multiplying by 10 and removing one group. Two methods that agree build both confidence and deeper understanding."
```

## Explainer

You already know your 1s through 5s facts, and you know the commutative property — that 3 × 7 = 7 × 3. That second fact is more useful than it might seem. Every fact with a 6, 7, 8, or 9 that also involves a number 5 or below is one you already know from the other direction. For example, 6 × 4 is the same as 4 × 6, which you already memorized. That cuts the new facts down considerably.

The **9s facts** have a reliable pattern worth memorizing: the tens digit of the product is always one less than the multiplier, and the two digits of the product always sum to 9. So 9 × 7: the tens digit is 6 (one less than 7), and 6 + 3 = 9, so the product is 63. You can check any 9s fact this way. Alternatively, think of it as one group less than a 10s fact: 9 × 7 = (10 × 7) − 7 = 70 − 7 = 63.

The **6s and 8s** have a useful pattern for even multipliers: they're always even numbers, and the 6s facts always end in their multiplier's ones digit when you multiply 6 by an even number. More practically: use known facts to derive unknown ones. 6 × 7 is hard to remember, but 5 × 7 = 35 is easy — just add one more group of 7: 35 + 7 = 42. This "plus one group" strategy turns a hard fact into an easy calculation.

The hardest facts for most students are **7 × 8** and **6 × 8**. For 7 × 8: use 5 × 8 = 40, then add two more groups of 8: 40 + 16 = 56. Or use 8 × 8 = 64 and subtract one group of 8: 64 − 8 = 56. The point isn't to memorize tricks — it's to develop enough fluency with the structure of multiplication that unknown facts feel reachable, not random. As you practice, the derived-fact path gets shorter and shorter until the fact fires automatically.
