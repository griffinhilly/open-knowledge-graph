---
id: combinations
title: Combinations
domain: mathematics
course: algebra-2
prerequisites:
  - id: permutations
    type: hard
builds-toward:
  - binomial-theorem
  - probability-with-combinatorics
tags: [combinatorics, combinations, counting, order-irrelevant]
stage: abstract-reasoning
status: validated
---

# Combinations

## Core Idea
A combination is a selection of objects where order does not matter. The number of combinations of n objects taken r at a time is C(n,r) = n!/(r!(n-r)!). C(n,r) = P(n,r)/r! because each combination of r objects can be arranged in r! ways. C(n,r) = C(n, n-r) by symmetry. Combinations count subsets, committee selections, and any scenario where only the group membership matters, not the arrangement.

## How It's Best Learned
Contrast directly with permutations using the same scenario: choosing 3 people from 10 for a committee (combination) vs. choosing president, VP, and secretary (permutation). Derive C(n,r) from P(n,r) by dividing out the redundant orderings. Practice identifying whether a problem requires permutations or combinations. Connect to Pascal's Triangle and the binomial coefficients.

## Common Misconceptions
- Using permutations when combinations are appropriate (and vice versa).
- Thinking C(n,r) and P(n,r) are the same.
- Forgetting that C(n,0) = 1 (there is exactly one way to choose nothing).
- Not recognizing the symmetry C(n,r) = C(n, n-r).

## Questions

```yaml
- question: "A committee of 3 is chosen from 8 candidates. Which expression gives the number of possible committees?"
  type: multiple-choice
  options: ["8 × 7 × 6", "8! / (3! × 5!)", "8! / 5!", "3! / 8!"]
  answer: 1
  explanation: "C(8,3) = 8!/(3! × 5!) = 56. Option A (8 × 7 × 6 = 336) is P(8,3), which counts ordered selections — it overcounts because committee {Alice, Bob, Carol} and {Carol, Bob, Alice} are treated as different. Dividing by 3! = 6 corrects for this: 336/6 = 56. Option C omits the r! in the denominator; Option D inverts the formula entirely."

- question: "C(10, 3) and P(10, 3) give the same count when choosing 3 people from 10."
  type: true-false
  answer: false
  explanation: "P(10,3) = 720 counts ordered arrangements; C(10,3) = 120 counts unordered groups. C(10,3) = P(10,3)/3! = 720/6 = 120. They are equal only in the trivial case r = 1, where there is only one way to arrange a single item."

- question: "Explain why C(10, 7) = C(10, 3) without computing either value."
  type: short-answer
  answer: "Choosing 7 items from 10 is equivalent to choosing which 3 items to leave out. Every selection of 7 items corresponds to exactly one set of 3 rejected items, so the two counts must be equal. This is the symmetry C(n,r) = C(n, n-r)."
  explanation: "This symmetry — C(n,r) = C(n, n-r) — follows from the formula: n!/(r!(n-r)!) = n!/((n-r)!r!). The two denominators are the same, just written in reverse order. Conceptually, selecting a subset is the same decision as selecting its complement."
```

## Explainer

When you studied permutations, order mattered. Choosing a president, vice-president, and secretary from 10 people gives 10 × 9 × 8 = 720 distinct outcomes, because switching the president and VP produces a different result. Combinations address a different question: what if order does not matter? Choosing 3 people for a committee — where all three members have equal standing — counts as one outcome regardless of the order you name them. Combinations count groups, not arrangements.

The formula follows directly from permutations. P(n, r) counts all ordered selections. But each group of r people can be arranged in r! ways, and all r! of those arrangements represent the *same* committee. So P(n, r) overcounts each combination exactly r! times. Dividing corrects for this: C(n, r) = P(n, r) / r! = n! / (r! × (n−r)!). For the committee example: P(10, 3) = 720, divided by 3! = 6 gives C(10, 3) = 120. There are 120 distinct committees.

The most important skill in combinatorics is identifying which formula applies. The question to ask is: does the order of selection matter for the outcome? If switching two elements produces a *different* valid outcome (first vs. second place, lock combinations, phone PINs), use permutations. If the group membership is all that matters (teams, committees, card hands, subsets), use combinations. This distinction is the source of the most common errors in counting problems.

A beautiful property of combinations is the symmetry C(n, r) = C(n, n−r). Choosing 3 items from 10 gives the same count as choosing 7 items from 10, because selecting a group of 3 is exactly equivalent to deciding which 7 to leave out. Every choice of 3 "picked" corresponds to exactly one group of 7 "not picked," so the two counts must match. This symmetry often provides a faster path to an answer: if you need C(20, 17), computing C(20, 3) is much easier.

Combinations also appear throughout Pascal's Triangle: the entry in row n, position r (counting from 0) is exactly C(n, r). This is why the binomial theorem — which you will see next — involves combinations as coefficients. The connection runs deep: combinations count the ways to choose which terms to multiply when expanding (x + y)^n, making combinatorics the bridge between counting and algebra.
