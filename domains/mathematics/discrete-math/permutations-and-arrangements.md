---
id: permutations-and-arrangements
title: Permutations and Ordered Arrangements
domain: mathematics
course: discrete-math
prerequisites:
- id: counting-principles-fundamentals
  type: hard
builds-toward:
- combinations-and-selections
- derangements
tags:
- combinatorics
- permutations
stage: formal-systems
status: validated
---

# Permutations and Ordered Arrangements

## Core Idea
A permutation is an ordered arrangement of objects where the sequence matters. The number of permutations of n distinct objects taken r at a time is P(n,r) = n!/(n-r)!. Permutations count the ways to select and arrange r items from n items when order is significant.

## How It's Best Learned
Use visual representations like seating arrangements, password creation, or race rankings. Compare small cases (2–3 objects) and count manually before deriving the formula.

## Common Misconceptions
- Confusing permutations with combinations (order matters in permutations!).
- Misapplying the factorial formula.
- Not reducing n!/(n-r)! correctly.

## Questions

```yaml
- question: "An election has 10 candidates. A voter must rank their top 3 choices in order (1st place, 2nd place, 3rd place). How many distinct ranked ballots are possible?"
  type: multiple-choice
  options:
    - "30 (10 × 3)"
    - "120 (10 × 3 × 4)"
    - "720 (P(10,3) = 10 × 9 × 8)"
    - "210 (C(10,3) = 10!/(3!7!))"
  answer: 2
  explanation: "Since the ranking order matters — ranking Alice 1st and Bob 2nd is a different ballot than ranking Bob 1st and Alice 2nd — this is a permutation problem. P(10,3) = 10 × 9 × 8 = 720. The first choice has 10 options, the second has 9 (one used), and the third has 8. Option D (210) is the combination count — it would be correct if we only asked 'which 3 candidates are on the ballot' without distinguishing their ranking."

- question: "A password consists of 4 distinct letters chosen from the 26-letter alphabet, where order matters (so 'ABCD' and 'DCBA' are different passwords). Which expression gives the number of possible passwords?"
  type: multiple-choice
  options:
    - "26⁴ = 456,976"
    - "P(26,4) = 26 × 25 × 24 × 23 = 358,800"
    - "C(26,4) = 14,950"
    - "4! = 24"
  answer: 1
  explanation: "Since each of the 4 positions must be a distinct letter and order matters, this is P(26,4) = 26!/(26-4)! = 26 × 25 × 24 × 23 = 358,800. Option A (26⁴) would be correct if letters could repeat — then each of 4 positions independently has 26 choices. With the 'distinct' constraint, each subsequent position loses one available letter. Option C (combinations) ignores the order distinction between passwords like 'ABCD' and 'DCBA'."

- question: "The number of ways to arrange all 7 books on a shelf is 7! = 5,040."
  type: true-false
  answer: true
  explanation: "When arranging all n distinct objects in a sequence, the first position has n choices, the second has n-1, and so on down to 1. This gives n! total arrangements. For 7 books: 7 × 6 × 5 × 4 × 3 × 2 × 1 = 5,040. This is the special case P(n,n) = n!/(n-n)! = n!/0! = n!/1 = n!. Each distinct ordering corresponds to a unique permutation, so every book placed in every position must be counted."

- question: "When selecting 3 people from a group of 8 for the roles of president, vice president, and treasurer, the number of ways equals the number of ways to simply choose any 3 people from the group of 8."
  type: true-false
  answer: false
  explanation: "Assigning named roles makes order matter: selecting Alice as president, Bob as VP, and Carol as treasurer is different from Alice as treasurer, Bob as president, and Carol as VP. This is a permutation problem: P(8,3) = 8 × 7 × 6 = 336. Choosing 3 people without role distinctions is a combination: C(8,3) = 56. The permutation count is always r! times the combination count (here 6 × 56 = 336), reflecting the number of ways to assign the r roles to the chosen group."

- question: "How do you determine whether a counting problem requires permutations rather than combinations? Give a concrete test and apply it to an example."
  type: short-answer
  answer: "Ask: would swapping two of the selected items produce a genuinely different outcome? If yes, order matters and you need permutations. If no, use combinations. Example: assigning 1st, 2nd, and 3rd place in a race — swapping Alice and Bob gives a different result (Alice-gold vs. Bob-gold), so use P(n,r). Selecting any 3 finalists for a participation prize — swapping Alice and Bob gives the same group, so use C(n,r). The formula P(n,r) = n!/(n-r)! captures the dwindling-slot pattern for ordered selections; C(n,r) = P(n,r)/r! divides out the orderings we don't want to distinguish."
  explanation: "This swap test is the most reliable practical heuristic. It works because combinations treat all orderings of a selection as equivalent — C(n,r) = P(n,r)/r! precisely because there are r! orderings of any r-element selection. If the problem requires distinguishing those orderings, you want the full P(n,r) count; if not, divide by r! to collapse them."
```

## Explainer

A **permutation** is what you get when order matters. From the multiplication principle — your prerequisite — you already know that sequential independent choices multiply. Permutations are exactly that pattern applied to the specific situation of selecting and arranging items from a set without replacement.

Imagine you're assigning 3 trophies (gold, silver, bronze) to 3 of 8 runners in a race. The gold medal choice has 8 options, the silver has 7 (one runner already took gold), and the bronze has 6. The total is 8 × 7 × 6 = 336. This is P(8, 3): 8 people, choosing 3, where the order of selection (who gets which medal) matters. The general formula P(n, r) = n!/(n-r)! captures exactly this "dwindling slot" pattern: you multiply from n down to n-r+1, which is the same as n! divided by the (n-r)! that you're *not* using.

The **factorial** n! = n × (n-1) × (n-2) × … × 1 represents the special case where r = n: arranging *all* n items. If you have 5 books to arrange on a shelf, the first slot has 5 choices, the second has 4, and so on: 5! = 120 arrangements. As n grows, factorials explode — 10! = 3,628,800 — which is why exact counting with permutations is more tractable than brute enumeration.

The crucial conceptual boundary is the distinction between permutations and combinations. Permutations count arrangements where **order matters**. If you're assigning runners to medals, (Alice-gold, Bob-silver) is different from (Bob-gold, Alice-silver). But if you're just selecting 3 runners for *any* podium recognition without distinguishing the prizes, those two selections count as the same group. That's the combinations side of the coin. Any time you're counting permutations but suspect order shouldn't matter, ask yourself: would swapping two chosen items give a genuinely different outcome? If not, you need combinations instead.
