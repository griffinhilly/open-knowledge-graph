---
id: combinations-and-selections
title: Combinations and Unordered Selections
domain: mathematics
course: discrete-math
prerequisites:
- id: permutations-and-arrangements
  type: hard
builds-toward:
- binomial-coefficients
- multinomial-theorem
tags:
- combinatorics
- combinations
stage: formal-systems
status: draft
---

# Combinations and Unordered Selections

## Core Idea
A combination is an unordered selection of objects where the sequence does not matter. The number of combinations of n objects taken r at a time is C(n,r) = n! / (r!(n-r)!). Combinations count selections where we care only about which items are chosen, not their order.

## How It's Best Learned
Compare permutations and combinations side-by-side using the same scenario (e.g., selecting committee members). Show why dividing by r! removes the ordering.

## Common Misconceptions
- Mixing up C(n,r) and P(n,r).
- Incorrectly applying the formula or mishandling cancellation.
- Not recognizing when a problem requires unordered selection.

## Explainer

You already know from permutations that P(n, r) = n! / (n−r)! counts the number of ordered selections — the number of ways to arrange r items chosen from n. The key question combinations answer is: what if the order does not matter? If you are choosing 3 people for a committee from a group of 10, the selection {Alice, Bob, Carol} is the same committee regardless of whether Alice was named first, second, or third. Permutations would count all 6 orderings of that trio as distinct; combinations count them as one.

The fix is precise: every combination of r items corresponds to exactly r! different orderings. So P(n, r) overcounts by exactly r! for every distinct group. Dividing removes that overcount: **C(n, r)** = P(n, r) / r! = n! / (r! · (n−r)!). This ratio is also written as "n choose r" — a notation that emphasizes the selection interpretation. For the committee example, C(10, 3) = 720 / 6 = 120 distinct committees.

The hardest part of using combinations is recognizing when a problem is asking for unordered selection. The signal is that the items being chosen are interchangeable in their roles — committee members, pizza toppings, cards dealt, students selected for a group. If the items have distinct roles (president, vice president, secretary), order matters and permutations apply. Ask yourself: if I swap two chosen items, do I get a meaningfully different outcome? If yes, use permutations. If no, use combinations.

Two properties are worth internalizing. First, C(n, r) = C(n, n−r): choosing r items to include is the same as choosing n−r items to exclude. This symmetry cuts calculation time and provides a useful sanity check. Second, the values C(n, r) are exactly the binomial coefficients — the numbers that appear in Pascal's triangle and in the expansion of (a + b)ⁿ. Every entry in Pascal's triangle is the count of a combinatorial selection, which is why combinations appear everywhere in probability, algebra, and counting arguments.
