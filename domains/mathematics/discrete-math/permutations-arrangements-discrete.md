---
id: permutations-arrangements-discrete
title: Permutations and Arrangements
domain: mathematics
course: discrete-math
prerequisites:
- id: counting-fundamentals-discrete
  type: hard
- id: factorial
  type: hard
builds-toward:
- combinations-selections-discrete
- binomial-theorem-discrete
tags:
- permutations
- arrangements
- ordering
- P(n,r)
stage: formal-systems
status: draft
---

# Permutations and Arrangements

## Core Idea
A permutation is an ordered arrangement of distinct objects. The number of r-permutations of n objects is P(n, r) = n!/(n−r)!. When order matters—choosing a president, vice-president, and treasurer—permutations apply.

## How It's Best Learned
Use the multiplication principle to derive P(n, r): first position has n choices, second has n−1, etc. Practice distinguishing permutations (order matters) from combinations (order doesn't).

## Common Misconceptions
Permutations require distinct objects; if objects repeat, the formula changes. The formula P(n, r) assumes choosing without replacement and that order distinguishes arrangements.

## Questions

```yaml
- question: "A club of 10 members needs to elect a president, a vice-president, and a treasurer. How many ways can these three distinct offices be filled?"
  type: multiple-choice
  options:
    - "C(10, 3) = 120, because we are choosing 3 people from 10"
    - "10 × 10 × 10 = 1000, because each office independently has 10 candidates"
    - "P(10, 3) = 720, because the offices are distinct and order of assignment matters"
    - "3! = 6, because there are 3 offices to arrange"
  answer: 2
  explanation: "The offices are distinguishable (president ≠ vice-president ≠ treasurer), so assigning Alice as president and Bob as VP is different from assigning Bob as president and Alice as VP. This means order matters — it's a permutation problem. P(10, 3) = 10 × 9 × 8 = 720. Option A (combinations) would be correct if the three selected people formed an unranked committee with no distinct roles."

- question: "How many distinct 3-letter arrangements can be formed using letters from {A, B, C, D, E} with no repetition?"
  type: multiple-choice
  options:
    - "10, because C(5, 3) = 10"
    - "60, because P(5, 3) = 5!/2! = 60"
    - "125, because each of 3 positions has 5 choices"
    - "15, because 5 × 3 = 15"
  answer: 1
  explanation: "We are choosing 3 letters from 5 and arranging them in order — order matters (ABC ≠ BAC), and no letter repeats. P(5, 3) = 5!/(5−3)! = 5!/2! = 5 × 4 × 3 = 60. Option A gives C(5,3) = 10, which counts unordered selections (combinations) — correct if you only cared which letters were chosen, not their order. Option C (125) counts arrangements with repetition, which is n^r = 5³, not applicable here."

- question: "Arranging all n distinct objects in a complete sequence is a special case of permutations: P(n, n) = n!."
  type: true-false
  answer: true
  explanation: "P(n, n) = n!/(n−n)! = n!/0! = n!/1 = n!. When you arrange all n objects (r = n), you're filling every slot, so the count is n × (n−1) × ⋯ × 1 = n!. This is exactly the 'number of ways to order n distinct objects' that factorial was introduced to count. Permutations generalize this: P(n, r) counts ordered arrangements when you only fill r of n slots."

- question: "Permutations count arrangements where the order of selection does not affect the outcome."
  type: true-false
  answer: false
  explanation: "This describes combinations, not permutations. Permutations count ordered arrangements, where swapping two elements produces a *different* outcome. For example, (Alice, Bob) and (Bob, Alice) are two distinct permutations of the same two people — because in a permutation context (like ranking first and second place), the order is what matters. Combinations count unordered selections, where {Alice, Bob} and {Bob, Alice} are the same."

- question: "Explain why the formula P(n, r) = n!/(n−r)! has (n−r)! in the denominator."
  type: short-answer
  answer: "The numerator n! counts all ways to arrange all n objects in a complete sequence. But we only want to fill r slots — we use n, n−1, …, n−r+1 for those r choices, and the remaining (n−r) objects are not placed at all. Those unplaced objects can be in any order among themselves without changing the outcome, so we divide by (n−r)! to cancel the arrangements of the unused objects. The result n!/(n−r)! = n × (n−1) × ⋯ × (n−r+1) counts only the ordered choices for the r occupied slots."
  explanation: "The denominator isn't arbitrary — it precisely removes the overcounting caused by treating the unchosen objects as though they have meaningful positions. When r = n, (n−r)! = 0! = 1, so nothing is canceled and P(n,n) = n! as expected."
```

## Explainer

A **permutation** is any ordered arrangement of objects. "Ordered" is the key word: the arrangement (Alice, Bob, Carol) is different from (Bob, Alice, Carol), even though they involve the same three people. When you studied the multiplication principle in counting fundamentals, you learned to multiply independent choices. Permutations apply that principle to sequential slots where each choice reduces the available options.

Suppose you want to arrange 3 of 5 students in a line for a photo. The first slot has 5 choices. Once that student is placed, the second slot has only 4 remaining choices. The third slot has 3. The total is 5 × 4 × 3 = 60. This is **P(5, 3)** — the number of ways to arrange 3 objects chosen from 5, where order matters. In general, **P(n, r) = n × (n−1) × ⋯ × (n−r+1)**, which collapses neatly using the factorial you learned: P(n, r) = n! / (n−r)!. The (n−r)! in the denominator cancels the tail of the factorial that was never used.

The factorial connection is worth pausing on. Factorial was introduced as "the number of ways to arrange n distinct objects in a complete sequence." That is just P(n, n) = n!/0! = n!. Permutations generalize this to partial arrangements — you're selecting r of the n objects to place, and the order of placement distinguishes outcomes. When r = n, you recover the factorial.

The hardest skill in permutation problems is distinguishing whether order matters. Consider: "How many ways can you choose a president and a vice-president from a 10-person club?" The offices are distinct — who gets which role matters — so this is a permutation: P(10, 2) = 90. Compare to "How many 2-person committees can be chosen from 10 people?" Committees don't have ranked roles; {Alice, Bob} is the same committee as {Bob, Alice}. That is a combination problem, which you'll study next. The test is simple: if swapping two choices produces a different outcome, it's a permutation.

One important boundary: the standard formula assumes you are choosing **without replacement** (no object appears twice) and that all objects are **distinct**. If objects can repeat (e.g., digit sequences where the same digit can reappear), the count is n^r, not P(n, r). If objects are not all distinct (e.g., arrangements of the letters in "MISSISSIPPI"), the formula must be divided by the factorials of the repeated element counts. The formula P(n, r) = n!/(n−r)! is the clean, foundational case; understanding its assumptions helps you recognize when a variant is needed.
