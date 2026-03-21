---
id: odd-and-even-numbers-patterns-3rd
title: Odd and Even Numbers and Patterns
domain: mathematics
course: 3rd-grade
prerequisites:
- id: even-and-odd-numbers
  type: soft
builds-toward:
- even-and-odd-functions
tags:
- odd-even
- patterns
- number-sense
stage: concrete-operations
status: draft
---

# Odd and Even Numbers and Patterns

## Core Idea
Even numbers are divisible by 2 (0, 2, 4, 6, 8...); odd numbers have a remainder of 1 when divided by 2 (1, 3, 5, 7, 9...). Patterns emerge: even + even = even, odd + odd = even, even + odd = odd.

## Questions

```yaml
- question: "Without calculating, which of these pairs must produce an odd sum?"
  type: multiple-choice
  options:
    - "24 + 16 — both are even"
    - "13 + 9 — both are odd"
    - "35 + 14 — one odd, one even"
    - "42 + 28 — both are even"
  answer: 2
  explanation: "Odd + Even = Odd. 35 is odd and 14 is even, so their sum is odd (35 + 14 = 49). Option A: Even + Even = Even. Option B: Odd + Odd = Even — the two leftover units pair up, making an even result. Option D: Even + Even = Even. The parity rules let you predict the result without adding."

- question: "A student claims: 'Adding two odd numbers always gives an odd answer.' Which example directly disproves this?"
  type: multiple-choice
  options:
    - "3 + 5 = 8 — both are odd, but the sum is even"
    - "2 + 6 = 8 — both are even, and the sum is even"
    - "7 + 2 = 9 — one odd, one even"
    - "4 + 4 = 8 — both are even"
  answer: 0
  explanation: "3 + 5 = 8: both 3 and 5 are odd, yet the sum is 8, which is even. This directly contradicts the claim. Odd + odd = even, always. The other examples don't involve two odd numbers being added, so they can't disprove a claim specifically about odd + odd."

- question: "The sum of two odd numbers is always even."
  type: true-false
  answer: true
  explanation: "True — and this surprises many students. Each odd number has one extra unpaired unit. When you combine two odd numbers, those two leftover units pair up with each other, leaving nothing unpaired in the total. For example: 3 + 5 = 8, 7 + 9 = 16, 11 + 13 = 24. This holds without exception."

- question: "You must calculate the actual sum to determine whether 47 + 38 is odd or even."
  type: true-false
  answer: false
  explanation: "False. Parity rules let you predict without calculating. 47 is odd and 38 is even; odd + even = odd. So 47 + 38 must be odd — and indeed, 47 + 38 = 85, which is odd. Using known structure to predict outcomes without full calculation is exactly what these rules are for."

- question: "Why does odd + odd always equal even? Use the idea of 'pairs' in your explanation."
  type: short-answer
  answer: "Every even number is made entirely of pairs with nothing left over. Every odd number is an even number plus one extra lone unit. When you add two odd numbers, you combine two sets of pairs plus two lone units. Those two lone units pair up with each other, so the final total has no leftovers — which means it is even."
  explanation: "The 'one extra' in each odd number is the key. Two extras combine into one pair, restoring the all-pairs structure that defines an even number. Visualizing this with dots — ●● ●● ● + ●● ●● ● = ●● ●● ●● ●● — makes the logic concrete and memorable."
```

## Explainer

You already know how to identify whether a number is odd or even — even numbers can be split into two equal groups with nothing left over, while odd numbers always have one "leftover." In third grade, the focus shifts from *identifying* odd and even numbers to *predicting* how they behave when you add them together. These predictions are patterns you can discover, verify, and ultimately explain.

The key insight is that **even numbers are made of pairs**. You can always arrange an even number of objects into two equal rows with nothing left over. Think of 6 as three pairs: ●● ●● ●●. An **odd number** is like an even number with one extra: 7 is three pairs plus one lonely dot: ●● ●● ●● ●. This "one extra" is the defining feature that drives every pattern.

Now add two even numbers. Each is made of pairs, so combining them gives you a collection that is *still* all pairs — nothing is left over. Even + even = even. Add two odd numbers: each brings its "one extra" dot. When you combine them, the two leftover dots pair up with each other, leaving nothing unpaired. Odd + odd = even. That result surprises many students — two odds make an even — but it is perfectly logical once you picture the dots. Finally, add an even and an odd: the even contributes nothing extra, the odd contributes its one lonely dot, and that dot stays unpaired. Even + odd = odd.

These three rules — even + even = even, odd + odd = even, even + odd = odd — let you predict the parity (oddness or evenness) of a sum *without calculating it*. Is 48 + 37 odd or even? Even + odd = odd, so the answer is odd, even before you add. You can verify: 85 is indeed odd. This kind of reasoning — using known structure to predict outcomes — is an early form of mathematical generalization, a skill that becomes central in algebra and number theory much later.
