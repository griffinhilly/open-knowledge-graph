---
id: stars-and-bars
title: 'Stars and Bars: Combinations with Repetition'
domain: mathematics
course: discrete-math
prerequisites:
- id: combinations
  type: hard
- id: counting-principles
  type: hard
builds-toward:
- generating-functions-intro
tags:
- stars-and-bars
- combinations-with-repetition
- counting
- combinatorics
stage: formal-systems
status: validated
---
# Stars and Bars: Combinations with Repetition

## Core Idea
The stars-and-bars technique counts the number of ways to distribute k identical objects into n distinct bins where each bin can hold any number, giving C(n+k−1, k). The idea is to arrange k stars (objects) and n−1 bars (dividers between bins) in a row — each arrangement corresponds to a distribution. This formula solves a wide class of problems: choosing k items from n types with repetition allowed, or counting non-negative integer solutions to x₁ + x₂ + ⋯ + xₙ = k.

## How It's Best Learned
Draw literal stars and bars diagrams: 'ooo|o|oo' represents 3 in bin 1, 1 in bin 2, 2 in bin 3. Converting between the visual and the formula builds reliable intuition. Extend to variations with minimum or maximum constraints using variable substitution.

## Common Misconceptions
- Confusing stars-and-bars (with repetition) with standard combinations (without repetition).
- Forgetting that n−1 bars, not n bars, are needed to create n bins.
- Not recognizing that 'non-negative integer solutions to a sum' problems are stars-and-bars in disguise.

## Questions

```yaml
- question: "How many non-negative integer solutions does x₁ + x₂ + x₃ = 7 have?"
  type: multiple-choice
  options:
    - "C(7, 3) = 35"
    - "C(7, 2) = 21"
    - "C(9, 2) = 36"
    - "C(10, 3) = 120"
  answer: 2
  explanation: "This is a stars-and-bars problem: distributing 7 identical objects (k=7) into 3 bins (n=3). The formula is C(n+k−1, k) = C(3+7−1, 7) = C(9, 7) = C(9, 2) = 36. Option A, C(7,3), is the number of ways to choose 3 items from 7 without repetition — a completely different question. Option B omits accounting for the extra n−1 positions for the bars. Option D overcounts by treating the objects as distinct."

- question: "In how many ways can 5 identical cookies be distributed among 4 children if every child must receive at least 1 cookie?"
  type: multiple-choice
  options:
    - "C(8, 5) = 56 — apply stars-and-bars directly with k=5 and n=4"
    - "C(4, 1) = 4 — substitute yᵢ = xᵢ − 1 to absorb the minimum, leaving 1 cookie to distribute freely"
    - "C(5, 4) = 5"
    - "C(8, 4) = 70"
  answer: 1
  explanation: "When each child must get at least 1, give each child 1 cookie first, leaving 5 − 4 = 1 cookie to distribute without constraint. Now apply stars-and-bars: C(4 + 1 − 1, 1) = C(4, 1) = 4. Option A ignores the 'at least 1' constraint entirely, giving the unconstrained answer. The substitution yᵢ = xᵢ − 1 transforms lower-bound constraints into unconstrained problems — a technique that generalizes to any minimum value."

- question: "Stars-and-bars requires n − 1 bars (not n bars) to divide k stars into n groups."
  type: true-false
  answer: true
  explanation: "Think physically: one cut divides a line into 2 pieces, two cuts into 3 pieces. In general, n−1 dividers create n sections. This is why the total number of symbols is k stars + (n−1) bars = k+n−1, and why we choose which k of those k+n−1 positions hold stars — giving C(k+n−1, k). A common error is using n bars, which would create n+1 bins rather than n."

- question: "The number of ways to choose 4 items from a menu of 6 options (with repetition allowed, order irrelevant) is C(6, 4) = 15."
  type: true-false
  answer: false
  explanation: "Choosing with repetition uses stars-and-bars: C(n+k−1, k) = C(6+4−1, 4) = C(9, 4) = 126. C(6, 4) = 15 counts selections without repetition — where you cannot pick the same item twice. Whenever repetition is allowed and order doesn't matter, you need stars-and-bars, not standard combinations. The much larger answer (126 vs 15) reflects the additional freedom to repeat items."

- question: "Explain why n − 1 bars are needed to create n bins in the stars-and-bars model, and why the total arrangement count is C(n+k−1, k)."
  type: short-answer
  answer: "Each bar is a divider between adjacent bins. Just as 1 fence post divides a line into 2 segments, n−1 dividers create exactly n sections. With k stars and n−1 bars, there are k+(n−1) = k+n−1 total symbols. Every distinct arrangement is determined by which k of those k+n−1 positions hold stars (the rest are bars), giving C(k+n−1, k) arrangements — each corresponding to exactly one distribution."
  explanation: "The bijection is what makes stars-and-bars so powerful: it transforms an open-ended distribution problem into a combinations problem you already know how to count. The derivation also explains why recognizing 'sum = k, non-negative integers' as stars-and-bars works — each variable xᵢ counts the stars in bin i, and the sum constraint is automatically satisfied by the fixed total of k stars."
```

## Explainer

You already know **combinations**: C(n, k) counts the ways to choose k distinct items from n, where order doesn't matter. That formula assumes you can't pick the same item twice. Stars and bars extends this to the case where repetition is allowed — you can pick any item as many times as you like. The trick is finding a clever bijection that reduces this new problem to a combinations problem you already know how to solve.

Imagine you have k identical balls and n labeled boxes, and you want to count every possible distribution (some boxes may be empty). Represent each ball as a star (★) and use n−1 bars (|) as dividers between boxes. A row of k stars and n−1 bars uniquely describes a distribution: count the stars in each segment. For example, with k=5 balls and n=3 boxes, the arrangement ★★|★|★★ means 2 in box 1, 1 in box 2, 2 in box 3. Every arrangement of 5 stars and 2 bars corresponds to exactly one distribution, and vice versa. So the count is just the number of ways to arrange k stars and n−1 bars — choose which k positions (out of k + n−1 total) hold stars: **C(n+k−1, k)**.

The same formula covers a problem that looks unrelated: how many non-negative integer solutions does x₁ + x₂ + ⋯ + xₙ = k have? Each solution is a tuple (x₁, …, xₙ) where xᵢ counts how many balls go into box i. It's the same problem in disguise, so the answer is the same: C(n+k−1, k). This equivalence is worth internalizing — whenever you see "sum equals a constant, all terms non-negative integers," that's stars and bars.

Constraints change the formula through substitution. If each box must hold **at least 1** ball (strict positivity), put one ball in each box first, leaving k−n balls to distribute freely. The answer becomes C(n + (k−n) − 1, k−n) = C(k−1, k−n). If a box has an **upper bound** (say, box 1 holds at most 3), use inclusion-exclusion: count all distributions, then subtract those where box 1 holds 4 or more. The power of stars and bars is that it turns distribution and allocation problems — which feel open-ended — into straightforward combinations calculations, as long as you correctly encode the constraints.
