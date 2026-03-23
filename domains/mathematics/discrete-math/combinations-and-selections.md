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
status: validated
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

## Questions

```yaml
- question: "A school needs to select 4 students to form a study group (no assigned roles). A second school needs to select a president, vice-president, secretary, and treasurer from 4 students. Both schools are choosing from 20 students. Which school's selection process has more possible outcomes?"
  type: multiple-choice
  options:
    - "The study group — unordered selections always outnumber ordered arrangements"
    - "The officer election — because the four chosen students can be arranged in 4! = 24 different role assignments, multiplying the count"
    - "They are equal — both select exactly 4 students from 20"
    - "The study group — because C(20,4) > P(20,4)"
  answer: 1
  explanation: "The officer election uses permutations P(20,4) = 20×19×18×17 = 116,280 because each ordering of the same 4 students represents a different outcome (different people in each role). The study group uses combinations C(20,4) = P(20,4)/4! = 116,280/24 = 4,845 because the same 4 students form one group regardless of order. Permutations are always ≥ combinations for r ≥ 2, so the ordered process has far more outcomes. Option D has the inequality backwards."

- question: "How many ways can a committee of 3 be chosen from a group of 8 people?"
  type: multiple-choice
  options:
    - "8 × 7 × 6 = 336, because the order in which members are chosen matters"
    - "C(8,3) = 8! / (3! × 5!) = 56"
    - "3! = 6, because there are 3 positions to fill"
    - "P(8,3) = 336, divided by 2 = 168, because only some orderings matter"
  answer: 1
  explanation: "C(8,3) = 8!/(3! × 5!) = (8×7×6)/(3×2×1) = 336/6 = 56. A committee has no ordered roles, so {Alice, Bob, Carol} is the same committee as {Bob, Carol, Alice} — the 6 orderings of any trio are all the same outcome. Dividing P(8,3) = 336 by r! = 3! = 6 removes all this overcounting, giving 56 distinct committees. Option A uses the permutation formula, which overcounts by 6 for every committee."

- question: "C(n, r) = C(n, n−r), which means choosing 3 items from 10 gives the same count as choosing 7 items from 10."
  type: true-false
  answer: true
  explanation: "This symmetry holds because choosing r items to include is identical to choosing n−r items to exclude — the same partition of the full set is described from two perspectives. C(10,3) = C(10,7) = 120. This property is a useful computational shortcut: when r > n/2, compute C(n, n−r) instead, which involves smaller factorials. It also appears as the left-right symmetry in Pascal's triangle."

- question: "The number of ways to arrange 5 books on a shelf equals the number of ways to choose 5 books from a collection of 5."
  type: true-false
  answer: false
  explanation: "Arranging 5 books on a shelf is a permutation problem where order matters: P(5,5) = 5! = 120. Choosing 5 books from a collection of 5 — if all 5 must be chosen — gives C(5,5) = 1, because there is only one way to include all items. The arrangement question asks 'how many orderings of these items exist?', while the selection question (choosing all 5 from 5) asks 'in how many ways can we pick all of them?' — trivially one. These are completely different calculations."

- question: "Why does C(n, r) = P(n, r) / r! ? What overcounting does dividing by r! correct for?"
  type: short-answer
  answer: "P(n, r) counts ordered selections — it treats {Alice, Bob, Carol} and {Bob, Alice, Carol} and all other orderings as distinct outcomes. For every group of r specific items, P(n, r) counts all r! different orderings of that group. When we only care which items are chosen (not their order), each distinct group gets counted r! times by P(n, r). Dividing by r! removes this overcounting, leaving exactly one count per unique group. For r = 3: every combination is counted 3! = 6 times by P(n, r), so C(n, r) = P(n, r)/6."
  explanation: "The key insight is that P(n, r) overcounts by exactly r! for each combination — not approximately, but exactly. This is because every set of r items has exactly r! orderings, each counted once by the permutation formula. Combinations cancel this systematic overcounting uniformly, which is why the formula is exact and not an approximation."
```

## Explainer

You already know from permutations that P(n, r) = n! / (n−r)! counts the number of ordered selections — the number of ways to arrange r items chosen from n. The key question combinations answer is: what if the order does not matter? If you are choosing 3 people for a committee from a group of 10, the selection {Alice, Bob, Carol} is the same committee regardless of whether Alice was named first, second, or third. Permutations would count all 6 orderings of that trio as distinct; combinations count them as one.

The fix is precise: every combination of r items corresponds to exactly r! different orderings. So P(n, r) overcounts by exactly r! for every distinct group. Dividing removes that overcount: **C(n, r)** = P(n, r) / r! = n! / (r! · (n−r)!). This ratio is also written as "n choose r" — a notation that emphasizes the selection interpretation. For the committee example, C(10, 3) = 720 / 6 = 120 distinct committees.

The hardest part of using combinations is recognizing when a problem is asking for unordered selection. The signal is that the items being chosen are interchangeable in their roles — committee members, pizza toppings, cards dealt, students selected for a group. If the items have distinct roles (president, vice president, secretary), order matters and permutations apply. Ask yourself: if I swap two chosen items, do I get a meaningfully different outcome? If yes, use permutations. If no, use combinations.

Two properties are worth internalizing. First, C(n, r) = C(n, n−r): choosing r items to include is the same as choosing n−r items to exclude. This symmetry cuts calculation time and provides a useful sanity check. Second, the values C(n, r) are exactly the binomial coefficients — the numbers that appear in Pascal's triangle and in the expansion of (a + b)ⁿ. Every entry in Pascal's triangle is the count of a combinatorial selection, which is why combinations appear everywhere in probability, algebra, and counting arguments.
